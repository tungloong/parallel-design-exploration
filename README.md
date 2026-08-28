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
TURN 1:  1a   1b   1c
0 · BASELINE             ← when a reliable current design exists
```

Sibling options remain directly comparable, state identities stay stable across conversation, and later exploration can branch from earlier work without erasing visible history.

## Status

**v0.7 — canonical options canvas protocol.**

The plugin can be selected directly as an Open Design Active Plugin and requests only `prompt:inject`, keeping the scenario compatible with the community plugin trust model.

v0.7 focuses on making the behavior model-independent: execution semantics are separated from visible artifact structure, the canvas follows a canonical DOM grammar, and baseline evidence is treated separately from design lineage.

## Core protocol

### Persistent visual states

The primary artifact is one persistent exploration document. Its direct visible states are:

1. newest exploration turn;
2. older turns in descending order;
3. optional `0 · Baseline` as the oldest state.

The document itself is the exploration history rather than a launcher for disconnected variants.

### Canonical turn and option identities

Turns and options use stable anchors:

```text
t1, t2, t3
1a, 1b, 1c
2a, 2b, 2c
```

Those ids are shared between canvas and conversation:

```text
Keep 2a's hierarchy, but use the interaction from 1c.
```

Every visible reference to existing work links back to the corresponding document anchor.

### Reliable baseline evidence

When the supplied project, screen, screenshot, design file, or prior artifact contains a reliable current state, the plugin preserves that state as `0 · Baseline`.

The baseline records **what exists now**. It does not imply that new options must inherit the baseline's design choices. A redesign can keep the current state visible while exploring from first principles.

For greenfield work or insufficient source context, the baseline is simply absent.

### Lineage where it is meaningful

`data-parent` represents intentional design descent, such as a later variant riffing on `1b`. Baseline presence alone does not make every first-turn option a child of the baseline.

This keeps the design graph semantically accurate while still preserving current-state evidence for comparison.

### Rendered sibling alternatives

A turn normally contains three materially different rendered options unless the user asks for another count. Variation axes come from the actual brief: interaction, structure, hierarchy, navigation, density, visual language, content strategy, or other relevant design dimensions.

### Local reasoning

Each option can carry compact explanation near the rendered design:

- idea or hypothesis;
- key move;
- likely advantage;
- tradeoff.

Turn-level framing stays concise and describes the design question being explored rather than the plugin's internal workflow.

### Quiet comparison surface

The canvas is infrastructure. Neutral substrate, compact labels, subtle separators, and consistent exploration chrome keep attention on the options themselves.

### Progressive authoring when available

When Open Design refreshes the HTML artifact as project files change, the skill prefers to establish the newest turn early and fill sibling options incrementally. Progressive rendering is an enhancement; the same protocol also works with final-write hosts.

## Install

```bash
od plugin install github:tungloong/parallel-design-exploration
```

Then select **Parallel Design Exploration** directly as the Active Plugin.

If an older version is installed, reinstall or upgrade it so Open Design sees the current manifest and skill package.

## Example structure

```html
<main class="pde-canvas" data-pde-version="1">
  <section class="pde-turn" id="t2" data-turn="2">
    ... 2a · 2b · 2c ...
  </section>

  <section class="pde-turn" id="t1" data-turn="1">
    ... 1a · 1b · 1c ...
  </section>

  <section class="pde-baseline" id="baseline" data-baseline="0">
    ... faithful current state ...
  </section>
</main>
```

For greenfield work, omit the baseline section.

See [`examples/single-document-exploration.html`](examples/single-document-exploration.html) for a multi-turn example and [`templates/exploration-board.html`](templates/exploration-board.html) for the canonical structural scaffold.

## Design principles

1. Diverge before converge.
2. Render alternatives rather than merely describing them.
3. Keep sibling options directly comparable.
4. Preserve visible exploration history.
5. Give design states stable conversational identities.
6. Treat baseline evidence and design lineage as separate concepts.
7. Keep reasoning close to the work it explains.
8. Keep the canvas visually subordinate to the designs.
9. Let the user's brief determine the domain, style, and variation axes.
10. Converge when the user chooses to.

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

Open Design may still contribute host-level discovery or design-direction context. The skill uses relevant host guidance while maintaining the persistent parallel exploration protocol.

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
