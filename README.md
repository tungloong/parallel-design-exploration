# Parallel Design Exploration

An experimental Open Design skill/plugin for **parallel prototyping on a persistent exploration canvas**.

Instead of the common agent loop:

```text
brief → choose one direction → generate → overwrite → refine
```

this skill aims for:

```text
                     ┌─ 1A ── 2A
brief → baseline ────┼─ 1B ── 2B
                     └─ 1C ── 2C

          all prior work remains visible
```

The goal is to reproduce the most useful part of a traditional design studio / large-canvas workflow in an agentic design environment: **make alternatives concrete, place them next to one another, and preserve the path that produced them.**

## What it changes

Open Design's default new-generation pipeline uses a direction-picking stage before artifact generation. This plugin intentionally changes the interaction contract:

- directions become **fully rendered sibling prototypes**, not only direction cards;
- the user does not have to pick a winner before seeing the alternatives;
- variants are presented side by side in one neutral working board;
- subsequent feedback appends a new round instead of mutating the old round;
- every variant has stable identity and parent lineage;
- convergence happens only when the user asks for it.

## Status

**v0.1 — behavior contract / reference implementation.**

This first version is deliberately lightweight. It packages the exploration behavior as a portable `SKILL.md` plus an Open Design `open-design.json` sidecar. It does not modify Open Design core UI or add a native infinite-canvas renderer.

The board therefore uses normal HTML as the compatibility layer.

## Repository structure

```text
.
├── SKILL.md
├── open-design.json
├── references/
│   ├── parallel-prototyping.md
│   ├── exploration-canvas.md
│   └── checklist.md
├── templates/
│   ├── exploration-board.html
│   └── exploration.schema.json
└── examples/
    └── mobile-ui-exploration.md
```

## Core behavior

### First round

```text
ROUND 1

1A                     1B                     1C
[full prototype]       [full prototype]       [full prototype]
rationale              rationale              rationale
trade-off              trade-off              trade-off
```

### Follow-up round

```text
ROUND 1
1A        1B        1C

ROUND 2
2A        2B        2C
↑         ↑         ↑
1A        1B        1C
```

Old variants are not silently rewritten.

A follow-up may also branch several descendants from one promising earlier direction:

```text
1B
├── 2A
├── 2B
└── 2C
```

## Design principles

1. Diverge before converge.
2. Prototype alternatives rather than merely describing them.
3. Juxtapose alternatives so visual comparison is immediate.
4. Preserve previous explorations by default.
5. Treat each iteration as additive.
6. Make lineage explicit.
7. Allow branching from any prior state.
8. Keep the exploration board visually neutral.
9. Let the human decide when to converge.

## Why

The workflow is grounded in established design practice rather than being an AI-specific prompt trick. The references included in this repository cover:

- **parallel prototyping** research showing benefits from developing alternatives in parallel;
- the broader divergence-before-convergence logic used in design methods;
- artboard/frame/infinite-canvas workflows that keep alternatives spatially visible;
- visual exploration organization and version-history patterns in modern design tools.

See [`references/parallel-prototyping.md`](references/parallel-prototyping.md) and [`references/exploration-canvas.md`](references/exploration-canvas.md).

## Open Design compatibility

Open Design plugins are anchored by portable `SKILL.md` files; `open-design.json` adds Open Design-specific metadata and pipeline wiring. This repository follows that model.

The v0.1 pipeline intentionally does **not** use `direction-picker`, because its normal interaction is to collect a direction choice and then converge. Instead, the skill itself instructs the planning/generation stages to render all siblings before asking for selection.

## Example request

```text
Use parallel-design-exploration.

Explore the search screen for this iOS app. I want structurally different interaction
ideas, not cosmetic themes. Keep all alternatives on one board and do not recommend
a winner yet.
```

On a later turn:

```text
I like 1B's input placement, but I want to see three different ways of handling the
results while keeping that interaction model. Preserve Round 1.
```

Expected result: three Round 2 descendants of `1B`, while Round 1 remains available for comparison.

## Next steps

Potential follow-ups after validating v0.1 in real Open Design sessions:

- native board/lineage rendering instead of a compatibility HTML board;
- automatic `exploration.json` reconciliation;
- artifact-level immutable snapshots for siblings;
- visual branch connectors and compare mode;
- explicit `Explore` vs `Converge` modes;
- integration with Open Design's file/version history without hiding historical variants in a separate panel;
- an upstream feature proposal for a first-class Parallel Exploration scenario.

## License

MIT.
