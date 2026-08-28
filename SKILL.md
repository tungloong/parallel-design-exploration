---
name: parallel-design-exploration
description: |
  Explore a design problem through multiple fully rendered sibling prototypes in parallel,
  keep every prior exploration visible, and append new rounds without overwriting old work.
  Use when the user wants divergent UI/product design exploration, parallel prototyping,
  side-by-side alternatives, or a persistent exploration canvas before convergence.
license: MIT
metadata:
  author: tungloong
  version: "0.1.0"
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
  scenario: design-exploration
---

# Parallel Design Exploration

Create a **working design exploration canvas**, not a presentation page.

The purpose of this skill is to keep a design space open long enough for useful comparison. It follows the logic of parallel prototyping: generate materially different alternatives at the same time, make them visually comparable, collect feedback, and only converge when the user explicitly asks to converge.

## Core contract

1. **Diverge before converge.** During an exploration round, do not choose a winner, recommend a preferred direction, or quietly collapse alternatives into one answer.
2. **Prototype the alternatives.** A direction is not just a paragraph, mood card, palette, or style label. Each sibling must be rendered far enough that the user can judge the design itself.
3. **Juxtapose, do not summarize.** Sibling variants must be visible in the same comparative field whenever practical.
4. **Never overwrite an exploration.** Earlier rounds are immutable historical design states. New feedback creates descendants; it does not mutate ancestors.
5. **Every iteration is additive.** The exploration board grows over time.
6. **Keep lineage explicit.** Every variant has a stable id and a parent.
7. **Allow branching from old work.** A new variant may descend from any prior variant, not only the latest round.
8. **The board is a workspace, not a showcase.** The board UI must remain visually neutral and subordinate to the prototypes.
9. **Convergence is a user decision.** Do not mark a winner or emit a final recommendation unless the user asks for selection, synthesis, or convergence.

## Resource map

```text
parallel-design-exploration/
├── SKILL.md
├── open-design.json
├── README.md
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

Read `references/parallel-prototyping.md` and `references/exploration-canvas.md` before generating the first round. Run `references/checklist.md` before completing each round.

## Information model

Treat the design exploration as a persistent graph, not as one mutable artifact.

Example:

```text
Baseline
├── 1A  Quiet canvas
│   └── 2A  Quiet canvas + keyboard-aware layout
├── 1B  Thumb search dock
│   ├── 2B  Dock with compact result cards
│   └── 2D  Dock with inline actions
└── 1C  Command results
    └── 2C  Command results + persistent source context
```

The round number describes when a variant was generated. The letter is only a sibling label within that round. The parent relationship is authoritative.

## File model

Prefer independent prototype files plus a neutral board:

```text
board.html
exploration.json
round-1/
  1A.html
  1B.html
  1C.html
round-2/
  2A.html
  2B.html
  2C.html
```

Independent files prevent a later iteration from accidentally rewriting earlier designs, and they keep each prototype usable outside the board.

If the runtime strongly prefers a single HTML artifact, preserve the same semantics inside one document: previous variant DOM must remain intact and new rounds must be appended rather than replacing earlier sections.

## Round 0 — baseline

When a source design exists, preserve it as `0` or `baseline` before exploring.

The baseline area should contain:

- the current design or faithful reconstruction;
- a short, factual problem statement;
- constraints explicitly supplied by the user.

Do not decorate the baseline as a marketing hero.

If there is no source design, start directly at Round 1.

## Round 1 — divergence

Unless the user requests another count, generate **3 distinct sibling prototypes**: `1A`, `1B`, `1C`.

Use 4 or 5 only when the design problem genuinely benefits from broader exploration. Avoid more than 5 siblings in one round.

Each sibling must differ in at least one consequential design hypothesis, such as:

- information architecture;
- primary interaction model;
- navigation model;
- content hierarchy;
- spatial organization;
- density and disclosure strategy;
- dominant product metaphor;
- platform convention vs custom interaction.

A color swap, typeface swap, border radius change, or minor spacing variation is **not** a distinct direction by itself.

For every sibling include:

- stable id (`1A`, `1B`, ...);
- short direction name;
- complete enough prototype to evaluate the key flow;
- 2–4 sentence rationale;
- primary hypothesis;
- what this direction gains;
- what this direction sacrifices;
- parent id (`baseline` for first-round siblings when a baseline exists).

## Board grammar

The board itself should be intentionally boring.

Preferred desktop composition:

```text
ROUND 1

1A                     1B                     1C
[full prototype]       [full prototype]       [full prototype]
short rationale        short rationale        short rationale
trade-off              trade-off              trade-off
```

All siblings in a round should use comparable viewport dimensions and zoom so visual comparison is fair.

Do not add presentation chrome such as:

- hero sections;
- marketing headlines;
- decorative sticky navigation;
- alternating editorial sections;
- CTA banners;
- "recommended" badges;
- winner ribbons;
- conclusion sections;
- decorative gradients unrelated to the prototypes;
- a polished case-study narrative around the board.

A small persistent utility header is allowed for neutral workspace controls such as round navigation, fit-to-view, or lineage visibility.

## Follow-up rounds

When the user gives feedback after Round 1:

1. Read the feedback as a transformation request on the design graph.
2. Preserve every previous variant unchanged.
3. Create a new round number.
4. Generate only the descendants that are useful for the feedback.
5. Assign each new variant an explicit parent.
6. Append the new prototypes and metadata to the board and manifest.

Example:

```text
ROUND 1
1A        1B        1C

ROUND 2
2A        2B        2C
↑         ↑         ↑
1A        1B        1C
```

A follow-up does **not** need a one-to-one descendant for every prior sibling. If feedback says "keep exploring 1B", Round 2 may contain `2A`, `2B`, and `2C` all with parent `1B`.

## Persistent history rules

- Earlier prototype files are read-only once a later round exists.
- Never repurpose an existing id.
- Never replace Round 1 with a cleaner Round 1.
- If a historical prototype has an implementation defect that prevents viewing, create a repair descendant or explicitly annotate the repair; do not silently rewrite history.
- Keep the original user feedback associated with the round it triggered when practical.
- The board may change its own neutral layout to accommodate more content, but it must continue to expose prior rounds.

## Relationship to Open Design direction picking

Open Design's direction-picker can be useful for generating candidate hypotheses, vocabulary, or style seeds. Do **not** stop at direction cards when this skill is active.

The skill changes the default flow from:

```text
directions → pick one → generate
```

to:

```text
directions → generate siblings → compare → user feedback → append descendants
```

Direction cards are planning inputs. The deliverable is the rendered exploration space.

## Convergence

Converge only when the user explicitly asks to choose, combine, finalize, promote, or move forward with a direction.

At convergence:

- preserve the exploration board and all ancestors;
- record which variant(s) contributed to the selected direction;
- if combining ideas, identify the sources (for example `1B structure + 2C result treatment`);
- create a new promoted artifact instead of deleting unused branches.

## Output orientation

Before completing a round, provide only enough orientation for the user to navigate the board. Avoid writing a long prose recommendation that competes with visual comparison.

The desired user state is:

> I can see the alternatives, compare them, point to specific parts, and continue exploring without losing where I came from.
