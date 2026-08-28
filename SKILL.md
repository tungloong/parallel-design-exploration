---
name: parallel-design-exploration
description: |
  Explore a design problem through multiple fully rendered sibling options in one persistent
  visual document. Preserve existing design context as a baseline when applicable, keep stable
  option identities across turns, and let the user decide when to converge.
license: MIT
metadata:
  author: tungloong
  version: "0.6.0"
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

Use a **persistent options canvas** when the user wants to explore a design space rather than receive one prematurely converged answer.

This is a general design method, not a visual style or product template. Apply it to the user's actual domain, platform, fidelity, source material, and brief.

## 1. Document grammar

Maintain one primary exploration document. Its visible structure is a stack of design states:

```text
TURN 3   ← newest
3a   3b   3c

TURN 2
2a   2b   2c

TURN 1
1a   1b   1c

0 · BASELINE   ← only when an existing design actually exists
```

The document begins with the newest turn. Project context and design reasoning belong close to the relevant turn or option instead of becoming a separate document-level narrative layer.

Sibling options are rendered inline and directly comparable. On follow-up turns, extend the same exploration document and preserve earlier states visibly.

## 2. Choose a contextual artifact name

Choose the primary HTML filename from the actual subject being explored rather than from the plugin name.

Use a concise, stable, kebab-case name such as:

```text
search-and-go-exploration.html
checkout-flow-exploration.html
analytics-dashboard-exploration.html
```

If an exploration artifact already exists for the current project, continue editing that file. Keep the filename stable across later turns.

If the host requires a specific entry path, follow the host requirement while keeping the visible document model defined by this skill.

## 3. Establish a baseline when there is an existing design

Before generating alternatives, determine whether the task has a real current state to vary.

A baseline exists when the user provides or links usable existing design context such as:

- a current screen or artifact;
- an imported project or codebase containing the relevant UI;
- a screenshot or design file representing the current state;
- an earlier artifact that the user explicitly wants to redesign or explore from.

When a reliable current state exists, render it faithfully as **`0 · Baseline`** at a comparable scale. The baseline is a reference state, not a redesign and not one of the sibling alternatives.

First-turn options that derive from that current state may record:

```html
<article id="1a" data-option="1a" data-parent="baseline">
```

When the task is genuinely greenfield and no current design can be established, begin with Turn 1 and omit the baseline relationship rather than inventing one.

## 4. Turn model: newest work first

Each exploration generation is a **turn**.

The first generation creates Turn 1. A later exploration request creates Turn 2, Turn 3, and so on.

Insert every new turn before older turns. Earlier turns keep their original markup, ids, and meaning so they remain visible design history.

A turn needs only enough framing to make the comparison legible:

- a compact turn id;
- a concise name or riff reference;
- the sibling option row;
- a short line of useful next-step prompts.

For descendant turns, the turn label can point back to the option or options being riffed on.

## 5. Stable option identities and lineage

Use stable `{turn}{letter}` option identifiers:

```text
1a  1b  1c
2a  2b  2c
```

Place the id on the outermost option container so it acts as the option's document anchor:

```html
<article class="pde-option" id="1b" data-option="1b">
```

When a later option branches from an earlier one, record the parent explicitly:

```html
<article class="pde-option" id="2a" data-option="2a" data-parent="1b">
```

References inside the document should link to those anchors when practical. In chat, use the same short ids directly.

Ids are stable: do not reuse or renumber historical options.

## 6. Generate real sibling options

Unless the user requests another count, create **3 materially different siblings** in a new exploration turn.

Choose variation axes that matter to the brief, such as:

- information architecture;
- layout and spatial organization;
- interaction model;
- navigation or disclosure strategy;
- density and hierarchy;
- product metaphor;
- platform-native versus custom behavior;
- visual language, typography, or tone when visual direction is part of the question;
- content or copy strategy when that is the design question.

The siblings should differ substantively enough that the user can explain the distinction between any two in one sentence. Render each option far enough that the user can judge the design itself rather than only reading a proposal for it.

Keep viewport, source content, and relevant constraints comparable when that makes the comparison fair.

## 7. Option anatomy

Each option has three layers.

### Identity

Show the stable option id, a concise direction name, and, on descendant turns, an optional parent reference.

```text
2a · Sentence builder   ← 1b
```

### Design

Render the actual screen, component, flow, composition, or prototype at a scale that can be compared with its siblings.

### Explanation

Place compact reasoning close to the option. Cover the most relevant of:

- **Idea / hypothesis** — what this option believes about the problem;
- **Key move** — the structural or interaction decision that distinguishes it;
- **Why it may work** — what it gains;
- **Tradeoff** — what it makes harder or gives up.

Prefer a few specific points over a long case-study narrative.

## 8. Canvas substrate

The exploration surface is infrastructure. Keep it visually quiet so the options carry the personality:

- plain neutral background;
- thin separators between turns;
- compact labels;
- subtle framing where useful;
- generous whitespace.

The substrate should make comparison easier without becoming another design direction of its own.

## 9. Progressive authoring when live preview is available

Prefer a build sequence that gives the user useful visual feedback while generation is still happening.

When the host refreshes an HTML artifact as it changes:

1. create the contextually named exploration file early;
2. establish the newest turn shell;
3. fill sibling options incrementally as they become coherent;
4. add option reasoning;
5. finish with next-step prompts.

On later turns, establish the new turn at the top first and then fill it while leaving older states intact.

This is a progressive-enhancement preference, not a dependency. If the host exposes only a final-write workflow, preserve the same document semantics without inventing custom browser or streaming infrastructure.

## 10. Open Design compatibility

Open Design may apply host-level design guidance before this skill runs. Treat that guidance as context while preserving an explicit request for parallel exploration.

If a host-level visual direction is already active, siblings can still diverge in structure, hierarchy, interaction, content strategy, and other meaningful axes. When the user's brief specifically asks to explore visual directions, allow option-local visual systems as far as the host permits.

## 11. Convergence is explicit

The exploration canvas exists to help the user compare and navigate possibilities. Converge when the user asks to choose, combine, finalize, promote, or continue with a specific option.

When converging:

- preserve the exploration history;
- name the source option ids;
- identify which parts came from which options when combining ideas;
- create or promote a production-oriented artifact if the user wants one.

## Completion check

Before finishing a turn, verify:

- the newest turn is visually first;
- a real existing design is represented as a baseline when applicable;
- no baseline was invented for a greenfield task;
- older states retain stable identities;
- siblings are directly comparable;
- each option contains a rendered design plus useful reasoning;
- descendant options expose lineage;
- the artifact filename reflects the actual subject and remains stable across turns;
- the canvas remains visually subordinate to the work.

The target experience is:

> I can see where the design started when a current state exists, watch the newest exploration take shape, compare several real options at once, reference any option by a stable id, ask for another riff, and keep the visible path of exploration in one place.
