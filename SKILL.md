---
name: parallel-design-exploration
description: |
  Explore a design problem through multiple fully rendered sibling options in one persistent
  visual document. Preserve reliable current-state evidence when available, keep stable option
  identities across turns, and let the user decide when to converge.
license: MIT
metadata:
  author: tungloong
  version: "0.8.0"
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

Use a **persistent options canvas** when a design problem benefits from comparing several rendered possibilities before committing to one direction.

This skill defines the interaction model of the exploration space. The user's brief, source material, platform, and design context determine what gets designed. The skill keeps alternatives visible, comparable, referable, and historically stable while the exploration continues.

## 1. Exploration model

### Read the design context

Start from the usable context supplied by the user or project: current screens, source code, screenshots, design files, prior artifacts, product constraints, design systems, and platform conventions that materially affect the task.

When that context contains a reliable current design, represent it as **`0 · Baseline`**. The baseline is current-state evidence for comparison. It can coexist with a complete rethink of the product because baseline and design lineage are separate concepts.

When no trustworthy current state can be established, the exploration begins with Turn 1.

### Render substantive siblings

Unless the user specifies another count, create **three materially different sibling options** in each new exploration turn.

Choose variation axes from the actual design question: information architecture, layout, interaction, navigation, hierarchy, density, product metaphor, platform behavior, visual language, content strategy, or another consequential dimension.

Render each option far enough that the design itself can be judged. Comparable viewport, content, and fidelity are useful when controlled conditions improve the comparison.

### Preserve the path of exploration

Each new generation becomes the next numbered turn. The newest turn appears first. Earlier turns retain their identities and remain visible, so the document records both the current design space and the path that produced it.

When a new option is intentionally derived from earlier work, record the main lineage anchor with `data-parent` and link to the earlier option in the visible canvas.

### Let convergence be user-directed

The user can continue branching, combine ideas, explore another axis, or converge on a direction. Stable ids make those moves conversationally precise.

## 2. Complete visible document protocol

The **Options Canvas is the complete visible exploration document**.

`main.pde-canvas` is the single visible top-level container in the artifact body. Every visible piece of exploration chrome, context, design work, annotation, and navigation belongs to a state inside this canvas. Non-rendering support such as scripts may sit outside the main element.

The direct children of `.pde-canvas` are design states in temporal order: newest turns first, then older turns, followed by the optional baseline as the oldest state.

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

## 3. Turn protocol

A turn is one visible exploration state. It contains a stable turn anchor, concise framing when useful, a group of sibling options, and optionally a few paths for continuing the design space.

```html
<section class="pde-turn" id="t2" data-turn="2">
  <header class="pde-turn-head">
    <a class="pde-turn-id" href="#t2">2</a>
    <span class="pde-turn-title">Riffs on <a href="#1b">1b</a></span>
  </header>

  <p class="pde-turn-context">
    Explore three ways to reduce choice friction while keeping the core premise of 1b.
  </p>

  <div class="pde-options">...</div>

  <p class="pde-next">...</p>
</section>
```

Turn framing describes the design question represented by that state. It stays visually subordinate to the rendered options.

## 4. Option protocol

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

  <div class="pde-design">
    <!-- Render the actual screen, component, flow, composition, or prototype. -->
  </div>

  <div class="pde-annotation">
    A short design-facing note that helps the user understand what is distinctive here.
  </div>
</article>
```

### Free-form local annotation

Annotations stay close to the design they explain, but their form follows the work rather than a fixed schema. Depending on the option, a useful annotation may be:

- one sentence naming the core idea;
- a short paragraph explaining the design move and its consequence;
- two or three bullets;
- a compact label plus a tradeoff;
- no extra prose when the distinction is already self-evident.

The purpose is legibility: the user should be able to understand what makes the option meaningfully different without turning every option into the same review form.

### Stable references

Visible references to existing turns, options, or baseline states link to their anchors:

```html
<a href="#2a">2a</a>
<a href="#1c">1c</a>
<a href="#baseline">0</a>
```

This aligns conversational identity with spatial navigation.

### Lineage

`data-parent` represents an intentional design lineage relationship. Baseline presence alone does not imply parentage.

For later turns, use a parent id when an option clearly riffs on earlier work. When a concept combines several sources, keep the main lineage anchor in `data-parent` and reference the other sources in nearby linked text when that helps explain the design.

## 5. Baseline protocol

When reliable current-state evidence exists, render it as the oldest visible state:

```html
<section class="pde-baseline" id="baseline" data-baseline="0">
  <header class="pde-baseline-head">
    <a class="pde-baseline-id" href="#baseline">0</a>
    <span class="pde-baseline-title">Baseline</span>
  </header>

  <div class="pde-baseline-design">
    <!-- Faithful current-state rendering. -->
  </div>
</section>
```

Represent the current state faithfully enough to support comparison. A concise source or state note can accompany it when that context improves interpretation.

## 6. Canvas substrate

The canvas is infrastructure for comparison. Use a quiet, consistent substrate: neutral background, compact state labels, restrained separators, and enough whitespace for sibling designs to remain the focus.

The exploration chrome stays visually stable across turns. Individual options can use whatever visual language the brief calls for.

## 7. Navigation through the design space

A turn can end with a small number of concrete continuation paths: riff on an option, combine specific ideas, explore a different axis, change fidelity, or converge when the user is ready.

Use linked stable ids when a suggestion points to existing work.

## 8. Artifact lifecycle and naming

Maintain one primary exploration artifact for the visible design space.

Derive a concise, stable, kebab-case filename from the subject being explored, for example:

```text
search-and-go-exploration.html
checkout-flow-exploration.html
analytics-dashboard-exploration.html
```

Follow-up turns continue editing the same primary artifact. Host-required entry paths take precedence when applicable. Supporting files can exist when the implementation or requested output genuinely benefits from them.

## 9. Progressive authoring

When the host refreshes the artifact as files change, establish the primary canvas early and let the newest turn take shape through coherent incremental updates. A useful sequence is:

1. establish the new turn shell in canonical position;
2. render sibling options as they become coherent;
3. add local annotations where they improve understanding;
4. add continuation paths when useful.

Hosts that expose only a final-write workflow still use the same document and history semantics.

## 10. Open Design compatibility

Open Design may contribute host-level discovery, craft, or design-direction guidance. Treat that guidance as context for the designs while preserving the persistent options-canvas interaction model.

A host-level visual direction can coexist with meaningful divergence in structure, hierarchy, interaction, navigation, density, or content strategy. When visual direction itself is the design question, option-local visual systems can carry that exploration as far as the host permits.

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
- local annotations are proportionate to what the design needs explained;
- the primary artifact name reflects the subject and stays stable across turns.

The target experience is:

> I can see the current state when one exists, compare several real alternatives at once, refer to any state by a stable id, ask for another riff, and keep the visible path of exploration in one place.
