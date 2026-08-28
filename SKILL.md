---
name: parallel-design-exploration
description: |
  Explore a design problem through several fully rendered sibling options in one persistent
  visual document. Preserve reliable current-state evidence when available, keep stable option
  identities across turns, and let the user decide when to converge.
license: MIT
metadata:
  author: tungloong
  version: "0.9.0"
triggers:
  - "parallel design exploration"
  - "parallel prototyping"
  - "design alternatives"
  - "design variations"
  - "explore multiple directions"
  - "show multiple directions side by side"
  - "diverge before converge"
od:
  mode: prototype
  surface: web
  platform: desktop
  scenario: design-exploration
---

# Parallel Design Exploration

Use a **persistent options canvas** when a design problem benefits from seeing several rendered possibilities before committing to one direction.

The skill owns the exploration protocol: visible history, stable identities, sibling comparison, lineage, and the small amount of canvas chrome required to keep those things legible. The user's brief and design context own the product, aesthetic, fidelity, platform, and content of the designs themselves.

## 1. Establish the design context

Start from usable context supplied by the user or project: current screens, source code, screenshots, design files, prior artifacts, product constraints, design systems, and platform conventions that materially affect the task.

When that context contains a reliable current design, represent it as **`0 · Baseline`**. The baseline is current-state evidence for comparison. It can coexist with a complete rethink because baseline and design lineage are separate concepts.

When no trustworthy current state can be established, begin with Turn 1.

## 2. Render sibling alternatives

Create a compact set of materially different sibling options. A user-specified count takes precedence; otherwise choose enough siblings to expose genuinely different hypotheses while keeping comparison practical.

Choose variation axes from the actual design question: information architecture, layout, interaction, navigation, hierarchy, density, product metaphor, platform behavior, visual language, content strategy, or another consequential dimension.

Render each option far enough that the design itself can be judged. Comparable viewport, content, or fidelity can be useful when controlled conditions improve the comparison.

## 3. Preserve the exploration path

Each new generation becomes the next numbered turn. The newest turn appears first. Earlier turns retain their identities and visible content so the document records both the current design space and the path that produced it.

When a new option is intentionally derived from earlier work, record the primary lineage anchor with `data-parent` and link to the earlier option in the visible canvas.

The user can keep branching, combine ideas, explore another axis, or converge on a direction.

## 4. Complete visible document protocol

The Options Canvas is the complete visible exploration document.

`main.pde-canvas` is the single visible top-level container in the artifact body. Its direct children are design states in temporal order: newest turns first, older turns next, and the optional baseline last.

```html
<body>
  <main class="pde-canvas" data-pde-version="1">
    <section class="pde-turn" id="t2" data-turn="2">...</section>
    <section class="pde-turn" id="t1" data-turn="1">...</section>
    <section class="pde-baseline" id="baseline" data-baseline="0">...</section>
  </main>

  <script>/* optional interaction support */</script>
</body>
```

For greenfield work without a reliable current state, the baseline section is absent.

## 5. Canonical canvas substrate

Canvas chrome is stable infrastructure rather than another design assignment. Use a small, consistent substrate and let the option content carry the visual personality of the brief.

A suitable default is:

```css
*{box-sizing:border-box}
html,body{margin:0;background:#f1efe9;color:#1c1c1a;font-family:ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
a{color:inherit;text-decoration:none}
.pde-canvas{min-width:100%}
.pde-turn,.pde-baseline{padding:40px 44px 32px;border-bottom:1px solid rgba(0,0,0,.08);scroll-margin-top:16px}
.pde-turn-head,.pde-baseline-head,.pde-option-head{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap}
.pde-turn-head,.pde-baseline-head{margin-bottom:20px}
.pde-turn-id,.pde-option-id,.pde-baseline-id{display:inline-flex;border-radius:5px;font:650 10.5px/1 ui-monospace,SFMono-Regular,Menlo,monospace}
.pde-turn-id{padding:4px 8px;background:#1c1c1a;color:#fff}
.pde-option-id,.pde-baseline-id{padding:4px 7px;background:rgba(0,0,0,.075)}
.pde-turn-title,.pde-baseline-title{font:650 13px/1.2 ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
.pde-options{display:flex;flex-wrap:wrap;gap:28px;align-items:flex-start}
.pde-option{flex:none;width:max-content;max-width:100%;display:flex;flex-direction:column;gap:9px;scroll-margin-top:16px}
.pde-option-head{color:rgba(0,0,0,.58);font:400 11px/1.3 ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
.pde-option-name{font-weight:600}
.pde-parent{color:rgba(0,0,0,.48)}
.pde-design{max-width:100%;overflow:hidden;background:#fff;border:1px solid rgba(0,0,0,.08);border-radius:8px;box-shadow:0 1px 3px rgba(0,0,0,.05)}
.pde-option:target .pde-option-id,.pde-baseline:target .pde-baseline-id{background:#2f6fd1;color:#fff}
.pde-next{margin:22px 0 0;color:rgba(0,0,0,.52);font:12px/1.5 ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
```

The substrate establishes turn spacing, small state labels, sibling layout, and the artifact surface. Option containers remain spatial containers rather than presentation cards. Size each `.pde-design` to the artifact it contains; intrinsic artboard sizes and flex wrapping keep the same protocol useful for phones, dashboards, posters, components, and other design formats.

## 6. Turn protocol

A turn needs only a stable turn anchor and its sibling options. A concise turn name is useful when it helps orient the user. Additional framing can appear when the design question genuinely benefits from it.

```html
<section class="pde-turn" id="t2" data-turn="2">
  <header class="pde-turn-head">
    <a class="pde-turn-id" href="#t2">2</a>
    <span class="pde-turn-title">Riffs on <a href="#1b">1b</a></span>
  </header>

  <div class="pde-options">...</div>

  <p class="pde-next">Try next: “...” · “...” · “...”</p>
</section>
```

When continuation cues are useful, keep them to one quiet line with a few concrete moves the user could ask for next.

## 7. Option protocol

Options use stable `{turn}{letter}` identities:

```text
1a  1b  1c
2a  2b  2c
```

The same id is the DOM anchor, visible label, and conversational reference.

```html
<article class="pde-option" id="2a" data-option="2a" data-parent="1b">
  <header class="pde-option-head">
    <a class="pde-option-id" href="#2a">2a</a>
    <span class="pde-option-name">Sentence builder</span>
    <a class="pde-parent" href="#1b">← 1b</a>
  </header>

  <div class="pde-design" style="width:360px">
    <!-- Render the actual screen, component, flow, composition, or prototype. -->
  </div>

  <!-- Optional local explanation when it materially improves understanding. -->
</article>
```

Visible references to existing turns, options, or the baseline link to their anchors:

```html
<a href="#2a">2a</a>
<a href="#1c">1c</a>
<a href="#baseline">0</a>
```

Local explanation is content, not chrome. It can be a sentence, paragraph, bullets, or absent when the design is self-explanatory. Its purpose is simply to make a meaningful design difference easier to understand.

### Lineage

`data-parent` represents intentional design descent. Baseline presence alone does not imply parentage.

When a concept combines several sources, keep the main lineage anchor in `data-parent` and reference other sources in nearby linked text when that helps explain the design.

## 8. Baseline protocol

When reliable current-state evidence exists, render it as the oldest visible state:

```html
<section class="pde-baseline" id="baseline" data-baseline="0">
  <header class="pde-baseline-head">
    <a class="pde-baseline-id" href="#baseline">0</a>
    <span class="pde-baseline-title">Baseline</span>
  </header>

  <div class="pde-design">
    <!-- Faithful current-state rendering. -->
  </div>
</section>
```

Represent the current state faithfully enough to support comparison. Source or state notes can accompany it when they materially improve interpretation.

## 9. Artifact lifecycle and naming

Maintain one primary exploration artifact for the visible design space.

Derive a concise, stable, kebab-case filename from the subject being explored, for example:

```text
search-and-go-exploration.html
checkout-flow-exploration.html
analytics-dashboard-exploration.html
```

Follow-up turns continue editing the same primary artifact. Host-required entry paths take precedence when applicable. Supporting files can exist when the implementation or requested output benefits from them.

## 10. Progressive authoring

When the host refreshes the artifact as files change, establish the primary canvas early and let the newest turn take shape through coherent incremental updates:

1. establish the new turn shell in canonical position;
2. render sibling options as they become coherent;
3. add local explanation and continuation cues when they improve the work.

Hosts that expose only a final-write workflow still use the same document and history semantics.

## 11. Open Design compatibility

Open Design may contribute host-level discovery, craft, or design-direction guidance. Treat that guidance as context for the designs while preserving the persistent options-canvas interaction model and canonical substrate.

A host-level visual direction can coexist with meaningful divergence in structure, hierarchy, interaction, navigation, density, content strategy, or option-local visual systems when visual direction itself is part of the design question.

## Structural validation

Before finishing a turn, confirm that:

- `main.pde-canvas` owns the complete visible exploration document;
- its direct state children are ordered newest-first, with the optional baseline last;
- every turn has `id="tN"` and matching `data-turn="N"`;
- every option has a stable `id` and matching `data-option`;
- references to existing design-state ids navigate to their anchors;
- baseline evidence and design lineage remain separate concepts;
- earlier turns retain their stable identities and visible content;
- sibling options are rendered far enough for direct comparison;
- the canvas uses the stable minimal substrate while the designs themselves carry the brief's visual language;
- the primary artifact name reflects the subject and stays stable across turns.

The target experience is:

> I can see the current state when one exists, compare several real alternatives at once, refer to any state by a stable id, ask for another riff, and keep the visible path of exploration in one place.
