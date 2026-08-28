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

**v0.10 — stable artifact identity and immutable delivered states.**

The plugin can be selected directly as an Open Design Active Plugin and requests only `prompt:inject`, keeping the scenario compatible with the community plugin trust model.

v0.10 formalizes the temporal side of the protocol:

- one exploration session has one stable primary artifact;
- each delivered turn becomes a historical design-state snapshot;
- normal follow-up work prepends a new turn to that same artifact;
- earlier states keep their identity, visible content, and rendering meaning;
- new implementation extends styles and behavior without unintentionally restyling historical states.

The visual substrate introduced in v0.9 remains intentionally small and stable so the model can spend its creative effort on the designs themselves.

## Core protocol

### One persistent artifact identity

The first generation establishes the primary exploration artifact. Its subject-derived filename becomes part of the session identity:

```text
search-and-go-exploration.html
checkout-flow-exploration.html
analytics-dashboard-exploration.html
```

Follow-up turns resolve and update that same artifact rather than creating a new latest copy.

### Immutable delivered states

Once a turn has been shown to the user, it becomes part of the historical record.

A normal follow-up changes this:

```text
Turn 1
0 · Baseline
```

into this:

```text
Turn 2   ← new
Turn 1   ← same historical state
0 · Baseline
```

Requests to riff on, deepen, combine, or refine earlier work normally create descendant options in a new turn. Direct correction of an earlier state is a different operation and happens only when the user explicitly asks to change that historical state itself.

Historical preservation applies to rendering meaning, not only DOM ids. New-turn CSS and behavior should be additive or scoped so previously delivered states still look and behave as they did when delivered.

See [`references/artifact-state-mutation.md`](references/artifact-state-mutation.md) for the state-transition model.

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

This substrate is the base canvas chrome, not a visual-direction suggestion. The design inside each option remains free to use whatever visual language the brief calls for.

See [`templates/exploration-board.html`](templates/exploration-board.html) for the minimal substrate and [`references/canvas-substrate.md`](references/canvas-substrate.md) for the rationale.

## Optional local explanation

Design reasoning can stay close to an option when it materially improves understanding, but it is not a fixed option schema. Depending on the work, an explanation can be one sentence, a short paragraph, bullets, or absent when the design is already clear.

The protocol standardizes **identity, history, mutation, and spatial comparison** rather than the designer's writing style.

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
4. Keep one stable primary artifact for the exploration session.
5. Treat delivered states as persistent historical snapshots.
6. Give design states stable conversational identities.
7. Treat baseline evidence and design lineage as separate concepts.
8. Keep the canvas chrome stable and lightweight.
9. Let the user's brief determine the domain, style, fidelity, and variation axes.
10. Let the user direct convergence.

## Open Design compatibility

The plugin is intentionally shaped as a community-safe standalone scenario:

```text
kind: scenario
taskKind: new-generation
mode: prototype
surface: web
capabilities: [prompt:inject]
```

Open Design can still contribute host-level discovery, craft, or design-direction context. The skill uses that context while maintaining the persistent parallel exploration model, stable artifact identity, immutable history semantics, and canonical substrate.

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
- [`references/artifact-state-mutation.md`](references/artifact-state-mutation.md)
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
