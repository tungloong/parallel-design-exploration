# Parallel Design Exploration

A community-oriented Open Design scenario for **persistent parallel prototyping inside one visual document**.

Instead of treating design iteration as one mutable latest state:

```text
brief → one answer → modify → replace → modify
```

the plugin keeps a visible design space:

```text
TURN 3:  3a   3b   3c   ← newest
TURN 2:  2a   2b   2c
TURN 1:  1a   1b   1c   1d
0 · BASELINE             ← when a reliable current design exists
```

Sibling options remain directly comparable, state identities stay stable across conversation, and later exploration can branch from earlier work without erasing visible history.

## Status

**v0.9 — stable canvas chrome, generative design content.**

The plugin can be selected directly as an Open Design Active Plugin and requests only `prompt:inject`, keeping the scenario compatible with the community plugin trust model.

v0.9 separates two responsibilities more sharply:

- the plugin provides a small, stable Options Canvas substrate for turns, ids, spacing, sibling layout, and navigation;
- the model and brief determine the actual design language, artifact size, annotation needs, and exploration axes.

This keeps the workspace recognizable without turning the workspace itself into another design task.

## Core protocol

### One visible exploration document

The primary artifact is one persistent Options Canvas. `main.pde-canvas` owns the complete visible exploration surface, and its direct children are the visible design states:

1. newest exploration turn;
2. older turns in descending order;
3. optional `0 · Baseline` as the oldest state.

### Stable turn and option identities

Turns and options use stable anchors:

```text
t1, t2, t3
1a, 1b, 1c, 1d
2a, 2b, 2c
```

Those ids are shared between canvas and conversation:

```text
Keep 2a's hierarchy, but use the interaction from 1c.
```

Visible references to existing states link back to the corresponding document anchor.

### Reliable baseline evidence

When the supplied project, screen, screenshot, design file, or prior artifact contains a reliable current state, the plugin preserves that state as `0 · Baseline`.

The baseline records **what exists now**. It does not imply that new options must inherit the baseline's design choices. A redesign can keep the current state visible while exploring from first principles.

For greenfield work or insufficient source context, the baseline is absent.

### Lineage where it is meaningful

`data-parent` represents intentional design descent, such as a later variant riffing on `1b`. Baseline presence alone does not make every first-turn option a child of the baseline.

### Rendered sibling alternatives

Each turn contains a compact set of materially different rendered options. A user-specified count wins; otherwise the agent chooses enough siblings to expose meaningful alternatives while keeping comparison practical.

Variation axes come from the actual brief: interaction, structure, hierarchy, navigation, density, visual language, content strategy, or other relevant design dimensions.

## Canonical canvas substrate

The Options Canvas uses a small utility chrome rather than a newly invented page style on every run:

- warm neutral workspace background;
- compact system-ui turn labels;
- compact monospace state ids;
- thin separators between turns;
- `flex-wrap` sibling layout;
- intrinsic artboard sizing;
- transparent option containers;
- a light artifact surface around each rendered design;
- quiet, one-line continuation cues when useful.

The design inside each option remains free to use whatever visual language the brief calls for.

See [`templates/exploration-board.html`](templates/exploration-board.html) for the minimal substrate and [`references/canvas-substrate.md`](references/canvas-substrate.md) for the rationale.

## Optional local explanation

Design reasoning can stay close to an option when it materially improves understanding, but it is not a fixed option schema. Depending on the work, an explanation can be one sentence, a short paragraph, bullets, or absent when the design is already clear.

The protocol standardizes **identity, history, and spatial comparison** rather than the designer's writing style.

## Install

```bash
od plugin install github:tungloong/parallel-design-exploration
```

Then select **Parallel Design Exploration** directly as the Active Plugin.

If an older version is installed, reinstall or upgrade it so Open Design sees the current manifest and skill package.

## Canonical structure

```html
<body>
  <main class="pde-canvas" data-pde-version="1">
    <section class="pde-turn" id="t2" data-turn="2">
      ... 2a · 2b · 2c ...
    </section>

    <section class="pde-turn" id="t1" data-turn="1">
      ... 1a · 1b · 1c · 1d ...
    </section>

    <section class="pde-baseline" id="baseline" data-baseline="0">
      ... faithful current state ...
    </section>
  </main>
</body>
```

For greenfield work, the baseline section is absent.

See [`examples/single-document-exploration.html`](examples/single-document-exploration.html) for a multi-turn example and [`templates/exploration-board.html`](templates/exploration-board.html) for a minimal structural scaffold.

## Design principles

1. Diverge before converge.
2. Render alternatives rather than merely describing them.
3. Keep sibling options directly comparable.
4. Preserve visible exploration history.
5. Give design states stable conversational identities.
6. Treat baseline evidence and design lineage as separate concepts.
7. Keep the canvas chrome stable and lightweight.
8. Let the user's brief determine the domain, style, fidelity, and variation axes.
9. Let the artifact determine its useful intrinsic size on the canvas.
10. Let the user direct convergence.

## Artifact naming

The exploration file is named from the actual subject, for example:

```text
search-and-go-exploration.html
checkout-flow-exploration.html
analytics-dashboard-exploration.html
```

The filename remains stable across later turns. Host-required entry paths take precedence when applicable.

## Open Design compatibility

The plugin is intentionally shaped as a community-safe standalone scenario:

```text
kind: scenario
taskKind: new-generation
mode: prototype
surface: web
capabilities: [prompt:inject]
```

Open Design can still contribute host-level discovery, craft, or design-direction context. The skill uses that context while maintaining the persistent parallel exploration model and its small canonical substrate.

## Method references

The interaction model is grounded in established design practice and modern visual-workspace patterns:

- parallel prototyping and divergence-before-convergence;
- design-space exploration;
- pin-up / studio-wall critique;
- artboards, frames, sections, and persistent visual workspaces;
- stable option identities and visible iteration history.

See:

- [`references/parallel-prototyping.md`](references/parallel-prototyping.md)
- [`references/exploration-canvas.md`](references/exploration-canvas.md)
- [`references/persistent-options-canvas.md`](references/persistent-options-canvas.md)
- [`references/canvas-substrate.md`](references/canvas-substrate.md)
- [`references/open-design-community-alignment.md`](references/open-design-community-alignment.md)

## Example request

```text
Explore several materially different ways to solve this design problem. Keep the alternatives together so I can compare them before choosing a direction.
```

Later:

```text
Take 1b as the main parent and show three different riffs on it.
```

Or:

```text
Combine the structure from 2a with the interaction idea from 1c, then keep exploring.
```

## Local validation

```bash
od plugin validate .
od plugin install .
```

## License

MIT.
