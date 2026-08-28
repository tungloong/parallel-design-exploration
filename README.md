# Parallel Design Exploration

An experimental Open Design scenario for **parallel prototyping inside one persistent design document**.

Instead of:

```text
brief → choose one direction → generate → overwrite → refine
```

this scenario aims for:

```text
ROUND 1:  1A   1B   1C
ROUND 2:  2A   2B   2C

all rendered inline in one document; prior rounds stay visible
```

The goal is to reproduce the most useful part of a design-studio / large-canvas workflow in an agentic environment: make alternatives concrete, juxtapose them, and preserve the visible path that produced them.

## Status

**v0.4 — single-document exploration contract.**

The plugin can be selected directly as an Open Design Active Plugin and does not depend on Web Prototype. It remains community-safe by requesting only `prompt:inject`.

The main behavioral change in v0.4 is important: **the exploration itself is one HTML document**. Variants are inline DOM siblings such as `1A`, `1B`, `1C`; they are not separate HTML files embedded into a board with iframes.

## Why v0.4 changed the artifact model

A real Open Design smoke test of v0.3 produced:

```text
focus-rhythm-board.html
exploration.json
round-1/1A.html
round-1/1B.html
round-1/1C.html
brand-spec.md
```

That output followed v0.3's written file model too literally, but it did **not** feel like the desired Claude Design interaction. It forced the design space into several files plus a wrapper board, created extra runtime/QA work, and made the board an index rather than the design document itself.

v0.4 therefore makes this a hard rule:

```text
ONE persistent exploration HTML
  └── Round 1
      ├── 1A inline prototype
      ├── 1B inline prototype
      └── 1C inline prototype
  └── Round 2
      ├── 2A inline prototype
      ├── 2B inline prototype
      └── 2C inline prototype
```

No normal-mode `1A.html` / `1B.html` / `1C.html`, no iframe composition, and no `exploration.json` requirement.

See [`examples/single-document-exploration.html`](examples/single-document-exploration.html).

## Install

```bash
od plugin install github:tungloong/parallel-design-exploration
```

Because the manifest requests only `prompt:inject`, a direct GitHub/community-safe install should not require the elevated filesystem/pipeline grant that blocked v0.2.

If an older version is installed, reinstall or upgrade it so the daemon sees v0.4 rather than a cached older manifest/snapshot.

Then select **Parallel Design Exploration** directly as the Active Plugin.

## Runtime contract

The first round should open as one comparative field:

```text
ROUND 1

1A                     1B                     1C
[inline prototype]     [inline prototype]     [inline prototype]
short rationale        short rationale        short rationale
```

A later turn edits the same HTML and appends:

```text
ROUND 1
1A        1B        1C

ROUND 2
2A        2B        2C
↑         ↑         ↑
1A        1B        1C
```

Old rounds remain visibly present.

## Runtime discipline added in v0.4

The skill is self-contained. Runtime generation must not search Open Design's installation tree for optional `references/` or templates before starting.

For ordinary exploration it also avoids side quests:

- no mandatory PNG/screenshot export;
- no broad shell/XML validation suite;
- no `brand-spec.md` without a real user-supplied brand/reference source;
- no debugging a direction CLI beyond a minimal attempt;
- vague smoke-test prompts stay lightweight instead of becoming large multi-file products.

## Important Open Design host limitation

Open Design's current core discovery prompt is more authoritative than later skill bodies. Its own source states that the discovery/philosophy layer is stacked first and **wins precedence over later sections, including skill bodies**. When no Active Design System exists, that core layer tells the agent to pick and lock one best-matching visual direction before planning.

That means a community-safe `prompt:inject` plugin can reliably change the **artifact/interaction model** (one canvas, parallel siblings, preserved rounds), but it cannot guarantee unrestricted visual-direction divergence if Open Design's core has already locked one global direction.

v0.4 mitigates this by telling the agent to treat any host-selected direction as neutral canvas/base context and to allow variant-local structure/tokens where possible. But a perfect Claude Design clone—where `1A`, `1B`, `1C` may each represent wholly different visual systems—likely requires an upstream Open Design change or a first-class exploration policy in the host prompt/runtime.

A plausible upstream capability would be something like:

```text
directionPolicy: single | parallel
```

with `parallel` skipping the normal global direction lock and carrying several visual directions into generation.

## Community alignment

The plugin remains shaped like a community-safe standalone scenario:

```text
kind: scenario
taskKind: new-generation
mode: prototype
surface: web
capabilities: [prompt:inject]
```

Representative references:

- **Community Registry Starter** — minimal standalone community scenario with `prompt:inject` only.
- **Hallmark** — substantial design behavior living primarily in `SKILL.md`, also `prompt:inject` only.
- **Humanize PPT** — a legitimate higher-capability plugin that requests filesystem/shell powers and therefore crosses the trust boundary.

See [`references/open-design-community-alignment.md`](references/open-design-community-alignment.md).

## Design principles

1. Diverge before converge.
2. Prototype alternatives rather than merely describing them.
3. Juxtapose alternatives in one visual field.
4. Use one persistent design document.
5. Preserve previous rounds visibly by default.
6. Treat each iteration as additive.
7. Make lineage explicit.
8. Keep the canvas visually subordinate to the variants.
9. Let the human decide when to converge.

## Method references

The approach is grounded in established design practice rather than being an AI-specific prompt trick. Repository references cover:

- parallel prototyping research;
- divergence-before-convergence design methods;
- artboard/frame/infinite-canvas workflows;
- visual exploration and version-history patterns.

See [`references/parallel-prototyping.md`](references/parallel-prototyping.md) and [`references/exploration-canvas.md`](references/exploration-canvas.md).

## Example request

```text
Explore the search screen for this iOS app. Show me three materially different ideas
in the same design document. Do not choose a winner yet.
```

Later:

```text
Keep Round 1 visible. Take 1B and branch three different result treatments from it.
```

## Local validation

```bash
od plugin validate .
od plugin install .
```

Then run a smoke test and verify that the normal result is **one exploration HTML**, not a board plus per-variant files.

## Next steps

- test v0.4 with the same `测试一下，随便画` prompt;
- test a real mobile UI brief;
- test Round 2 preservation inside the same HTML;
- decide whether to propose an upstream `parallel` direction policy to Open Design;
- later consider native canvas/lineage UI instead of an HTML compatibility document.

## License

MIT.
