#!/usr/bin/env python3
"""Lightweight repository checks for Parallel Design Exploration.

Uses only the Python standard library so it can run locally and in GitHub Actions.
"""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def validate_skill_frontmatter(skill: str) -> str:
    if not skill.startswith("---\n"):
        fail("SKILL.md: missing YAML frontmatter")
        return ""

    try:
        frontmatter = skill.split("---\n", 2)[1]
    except IndexError:
        fail("SKILL.md: malformed YAML frontmatter")
        return ""

    allowed = {
        "name",
        "description",
        "license",
        "compatibility",
        "metadata",
        "allowed-tools",
    }
    keys = []
    for line in frontmatter.splitlines():
        if not line or line[0].isspace() or ":" not in line:
            continue
        keys.append(line.split(":", 1)[0].strip())

    unexpected = sorted(set(keys) - allowed)
    if unexpected:
        fail(f"SKILL.md: unsupported top-level frontmatter keys: {unexpected}")

    description_match = re.search(
        r"^description:\s*\|\n(?P<body>(?:^[ \t]+.*\n?)*)",
        frontmatter,
        re.MULTILINE,
    )
    if not description_match:
        fail("SKILL.md: description should be a multiline routing description")
    else:
        description = description_match.group("body").lower()
        trigger_terms = ("variant", "alternative", "mockup", "direction", "prototype")
        if not any(term in description for term in trigger_terms):
            fail("SKILL.md: description lacks design-exploration trigger vocabulary")

    version_match = re.search(r'^\s+version:\s*["\']?([^"\'\s]+)', frontmatter, re.MULTILINE)
    if not version_match:
        fail("SKILL.md: metadata.version missing")
        return ""
    return version_match.group(1)


def canonical_css(skill: str) -> str:
    match = re.search(
        r"## 5\. Canonical canvas substrate.*?```css\n(?P<css>.*?)\n```",
        skill,
        re.DOTALL,
    )
    if not match:
        fail("SKILL.md: canonical substrate CSS block not found")
        return ""
    return match.group("css").strip()


def style_text(html: str) -> str:
    match = re.search(r"<style>\n(?P<css>.*?)\n\s*</style>", html, re.DOTALL)
    if not match:
        return ""
    lines = match.group("css").splitlines()
    normalized = [re.sub(r"^\s{4}", "", line) for line in lines]
    return "\n".join(normalized).strip()


class CanvasParser(HTMLParser):
    def __init__(self, path: str) -> None:
        super().__init__()
        self.path = path
        self.ids: set[str] = set()
        self.hrefs: list[str] = []
        self.canvas_count = 0

    def handle_starttag(self, tag: str, attrs_list: list[tuple[str, str | None]]) -> None:
        attrs = {key: value for key, value in attrs_list}
        classes = set((attrs.get("class") or "").split())
        element_id = attrs.get("id")

        if element_id:
            if element_id in self.ids:
                fail(f"{self.path}: duplicate id {element_id!r}")
            self.ids.add(element_id)
            if element_id[0].isdigit():
                fail(f"{self.path}: DOM id {element_id!r} begins with a digit")

        href = attrs.get("href")
        if href and href.startswith("#") and len(href) > 1:
            self.hrefs.append(href[1:])

        if tag == "main" and "pde-canvas" in classes:
            self.canvas_count += 1
            if "data-pde-version" in attrs:
                fail(f"{self.path}: data-pde-version is undefined protocol metadata")

        if "pde-turn" in classes:
            turn = attrs.get("data-turn")
            if turn and element_id != f"t{turn}":
                fail(
                    f"{self.path}: turn data-turn={turn!r} should use id='t{turn}', got {element_id!r}"
                )

        if "pde-option" in classes:
            option = attrs.get("data-option")
            if not option:
                fail(f"{self.path}: pde-option missing data-option")
            elif element_id != f"o-{option}":
                fail(
                    f"{self.path}: option data-option={option!r} should use id='o-{option}', got {element_id!r}"
                )

    def finish(self) -> None:
        if self.canvas_count != 1:
            fail(f"{self.path}: expected exactly one main.pde-canvas, found {self.canvas_count}")
        for target in self.hrefs:
            if target not in self.ids:
                fail(f"{self.path}: href '#{target}' has no matching id")


def validate_html(path: str, expected_css: str) -> None:
    html = read(path)
    parser = CanvasParser(path)
    parser.feed(html)
    parser.finish()

    css = style_text(html)
    if not css:
        fail(f"{path}: style block not found")
    elif expected_css and not css.startswith(expected_css):
        fail(f"{path}: canonical substrate CSS has drifted from SKILL.md")


def main() -> int:
    skill = read("SKILL.md")
    skill_version = validate_skill_frontmatter(skill)

    try:
        manifest = json.loads(read("open-design.json"))
    except json.JSONDecodeError as exc:
        fail(f"open-design.json: invalid JSON: {exc}")
        manifest = {}

    manifest_version = str(manifest.get("version", ""))
    if skill_version and manifest_version != skill_version:
        fail(
            f"version mismatch: SKILL.md={skill_version!r}, open-design.json={manifest_version!r}"
        )

    preview = (
        manifest.get("od", {})
        .get("preview", {})
        .get("entry")
    )
    if preview:
        preview_path = preview.removeprefix("./")
        if not (ROOT / preview_path).exists():
            fail(f"open-design.json: preview entry does not exist: {preview}")

    css = canonical_css(skill)
    validate_html("templates/exploration-board.html", css)
    validate_html("examples/single-document-exploration.html", css)

    if ERRORS:
        print("Validation failed:")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    print("Parallel Design Exploration validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
