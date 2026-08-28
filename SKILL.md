---
name: parallel-design-exploration
description: |
  Explore a design problem through multiple fully rendered sibling options in one persistent
  visual document. Keep stable option identities across turns, preserve prior exploration,
  and let the user decide when to converge.
license: MIT
metadata:
  author: tungloong
  version: "0.5.0"
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
  preview:
    type: html
    entry: design-exploration.html
    reload: debounce-100
---

# Parallel Design Exploration

Use a **persistent options canvas** when the user wants to explore a design space rather than receive one prematurely converged answer.

The central interaction model is simple:

- one persistent visual document;
- each design round is a turn;
- each turn contains several sibling options shown together;
- every option has a stable identity that can be referenced in chat;
- later turns branch from earlier options without erasing them;
- the newest turn is visually first;
- the user, not the agent, decides when exploration becomes convergence.

This is a general design method. Apply it to the user's actual domain, fidelity, platform, and brief; do not assume a specific product type or visual style.

## 1. One persistent exploration document

Create and maintain one primary artifact named:

```text
design-exploration.html
```

The document itself is the design space. Sibling options must be rendered inline and directly comparable rather than hidden behind separate files, tabs, or a launcher.

Ancillary files are allowed when the host, the user's requested format, or a real implementation need requires them, but they are secondary. They must not replace the persistent visual canvas as the main exploration surface.

On follow-up turns, edit this same document instead of replacing it with a new latest-state artifact.

## 2. Turn model: newest work first

Treat every exploration generation as a **turn**.

The first round creates Turn 1. A later request creates Turn 2, Turn 3, and so on.

When adding a new turn, insert it **before** older turns so the latest work appears at the top of the document while prior turns remain visually available below it.

```text
TURN 3   ← newest
3a   3b   3c

TURN 2
2a   2b   2c

TURN 1   ← oldest
1a   1b   1c
```

Never delete, renumber, or silently rewrite earlier turns merely to make the document look cleaner. Once a later turn exists, previous turn content represents visible design history.

## 3. Stable option identities

Use stable `{turn}{letter}` option identifiers such as:

```text
1a  1b  1c
2a  2b  2c
```

Place the identifier on the outermost option container so it can act as a document anchor:

```html
<article class="pde-option" id="1b" data-option="1b" data-parent="baseline">
  ...
</article>
```

When a later option branches from an earlier one, record the parent explicitly:

```html
<article class="pde-option" id="2a" data-option="2a" data-parent="1b">
```

References to options inside the document should be links to those anchors when practical. In chat, refer to the same short ids directly: `1b`, `2a`, and so on.

If an existing exploration already uses another stable id convention, preserve it rather than renumbering historical work.

## 4. Generate real sibling options, not descriptions

Unless the user requests another count, create **3 materially different siblings** in a new exploration turn.

Choose variation axes that matter to the brief. Examples include:

- information architecture;
- layout and spatial organization;
- interaction model;
- navigation or disclosure strategy;
- density and hierarchy;
- product metaphor;
- platform-native versus custom behavior;
- visual language, typography, or tone when visual direction is part of the exploration;
- content or copy strategy when that is the design question.

The siblings should be distinct enough that a user can explain the difference between any two in a sentence. Cosmetic token changes alone are not sufficient unless the user explicitly asked for a styling study.

Render each option far enough that the user can judge the design itself rather than only reading a proposal for it.

## 5. Option anatomy

Each option should read as a compact design study with three layers:

### A. Above the design — identity

Show:

- stable option id;
- concise direction name;
- optional parent reference on descendant turns.

Example:

```text
2a · Sentence builder   ← 1b
```

### B. The design itself

Render the actual screen, component, flow, composition, or prototype at a comparable scale to its siblings.

Keep sibling viewport/content conditions comparable when comparison fairness matters.

### C. Below the design — explanation panel

Include concise but useful design reasoning. Prefer 2–4 short points rather than a single vague sentence. Cover the most relevant of:

- **Idea / hypothesis** — what this option believes about the user's problem;
- **Key move** — the structural or interaction decision that distinguishes it;
- **Why it may work** — what it gains;
- **Tradeoff** — what it makes harder or gives up.

The explanation belongs to the option and should help comparison. It should not turn the page into a case study or marketing narrative.

## 6. Turn anatomy

Each turn has four parts:

1. **Turn identity** — a small turn badge/number.
2. **Turn explanation** — one short sentence describing what this round is exploring, and, for a descendant turn, which prior option(s) it riffs on.
3. **Sibling option row** — options laid out side by side in a wrapping horizontal field.
4. **Next-step prompts** — 2–3 short, concrete follow-up ideas the user could ask next.

Example next-step language:

```text
Try next: “more like 2a, but quieter” · “combine the hierarchy of 2b with the interaction from 1c” · “new directions”
```

These are navigation suggestions through the design space, not a recommendation for a winner.

## 7. Canvas substrate

The canvas is a workspace, not the designed object.

Use a restrained neutral substrate so the options carry the visual personality. Prefer:

- a plain off-white, very light gray, or similarly quiet background;
- thin separators between turns;
- small typographic labels;
- subtle option framing only when needed for legibility;
- generous whitespace;
- minimal chrome.

Avoid decorative grid-paper backgrounds, marketing heroes, sticky navigation, large editorial framing, promotional CTAs, or ornamental canvas treatments unless the user explicitly asks for the exploration document itself to be styled that way.

Do not force all options to inherit one visible canvas aesthetic. The substrate should remain subordinate to the design studies.

## 8. Progressive authoring when the host supports live preview

Prefer a build process that gives the user visual feedback during generation.

When the host reloads preview files as they change:

1. create `design-exploration.html` early with the neutral canvas and current turn shell;
2. write the turn header and option slots;
3. fill sibling options incrementally as each becomes coherent;
4. add each option's explanation panel;
5. finish with the turn-level next-step prompts.

On follow-up turns, insert the new turn shell at the top first, then progressively fill it while leaving older turns untouched.

Do not delay the first visible artifact until every sibling and every annotation is complete when the available editing tools can update the preview safely in smaller steps.

This is a preference, not a hard dependency: if the current host only exposes a final-write workflow, preserve the same document model without inventing custom browser or streaming infrastructure.

## 9. Open Design compatibility

Open Design may apply host-level design guidance before this skill runs. Treat such guidance as context, not as a reason to collapse an explicit exploration request into a single answer.

If the host has already selected a visual direction, siblings may still diverge in structure, hierarchy, interaction, and other meaningful axes. When the user's brief explicitly asks to explore visual directions, allow option-local visual systems as far as the host permits.

Do not require the user to pick one candidate before rendering the options when the purpose of the current task is exploration.

## 10. Convergence is explicit

Do not automatically rank or crown a winner during an exploration turn.

Converge when the user asks to choose, combine, finalize, promote, or continue with a specific option.

When converging:

- keep the exploration canvas intact;
- name the source option ids;
- if combining ideas, identify which parts came from which options;
- create or promote a separate final artifact if the user wants a production-oriented deliverable.

## 11. Completion check

Before finishing an exploration turn, verify:

- the newest turn appears before older turns;
- older turns remain visible and retain stable ids;
- siblings are directly comparable in one visual field;
- each option has identity, a rendered design, and useful explanation;
- descendant options expose lineage;
- the turn ends with a few useful follow-up prompts;
- the canvas chrome remains quiet;
- no winner was selected unless the user asked to converge.

The target experience is:

> I can watch the current round take shape, compare several real options at once, reference any option by a stable id, ask for another riff, and keep the whole visible path of exploration in one place.
