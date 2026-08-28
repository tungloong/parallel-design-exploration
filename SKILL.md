---
name: parallel-design-exploration
description: |
  Explore a design problem through multiple fully rendered sibling options in one persistent
  visual document. Preserve reliable current-state evidence when available, keep stable option
  identities across turns, and let the user decide when to converge.
license: MIT
metadata:
  author: tungloong
  version: "0.7.0"
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

Use a **persistent options canvas** when the task benefits from comparing several rendered design possibilities before committing to one direction.

This skill defines an interaction protocol for design exploration. It does not prescribe a product domain, aesthetic, platform, fidelity, or house style. The user's brief and source material determine the design problem; this skill determines how alternatives remain visible, comparable, and referable over time.

## 1. Execution model

Keep the execution model distinct from the visible artifact.

### Acquire design context

Before generating alternatives, inspect the usable context supplied by the user or project:

- current screens or artifacts;
- source code containing the relevant UI;
- screenshots or design files;
- prior exploration artifacts;
- product constraints, design systems, and platform conventions that materially affect the task.

Use this context to understand what exists today and what the user is asking to explore.

### Establish current-state evidence

When a reliable current design can be reconstructed from the supplied context, preserve it as **`0 · Baseline`**. The baseline records the current state for comparison.

The existence of a baseline is independent of whether the user wants to preserve, evolve, or completely rethink that design. A request to "start over" can still have a baseline if a real current state exists; the baseline is evidence, not a requirement to inherit its choices.

If the available material is insufficient to establish a trustworthy current state, omit the baseline. Baseline absence is represented structurally by its absence from the document.

### Generate substantive siblings

Unless the user specifies another count, create **3 materially different sibling options** in a new turn.

Choose axes that matter to the brief, for example:

- information architecture;
- layout and spatial organization;
- interaction model;
- navigation or disclosure strategy;
- density and hierarchy;
- product metaphor;
- platform-native versus custom behavior;
- visual language, typography, or tone when visual direction is part of the question;
- content or copy strategy when that is the design question.

The options should differ enough that a user can explain the distinction between any two in one sentence. Render each far enough that the design itself can be judged rather than merely described.

Use comparable viewport, source content, and constraints when comparison benefits from controlled conditions. These are execution invariants; surface them in the artifact only when they are genuinely useful to understanding a design state.

### Continue additively

Each new exploration generation becomes the next turn. Insert the newest turn before older turns. Preserve prior turns and option identities so the visible document accumulates design history instead of collapsing into a single latest state.

### Converge explicitly

Converge when the user asks to choose, combine, finalize, promote, or continue with a specific option. Until then, keep alternatives alive as alternatives.

## 2. Visible document protocol

The exploration artifact follows a stable DOM grammar so different agents produce the same interaction model.

The direct children of `.pde-canvas` are visible design states: newest turns first, followed by the optional baseline as the oldest state.

```html
<main class="pde-canvas" data-pde-version="1">
  <section class="pde-turn" id="t2" data-turn="2">...</section>
  <section class="pde-turn" id="t1" data-turn="1">...</section>
  <section class="pde-baseline" id="baseline" data-baseline="0">...</section>
</main>
```

For greenfield work without a reliable current state, the baseline section is simply absent.

Visible framing belongs to a specific design state. Method bookkeeping and internal comparison rules remain execution metadata unless they help the user interpret that state.

## 3. Turn protocol

Every turn has a stable turn anchor, compact framing, a sibling option group, and a short set of navigation suggestions.

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

The turn title and optional context describe what this design state is exploring. Keep turn chrome visually subordinate to the options.

The newest turn is the first turn section in the document. Existing turn markup, ids, and meaning stay stable when later turns are added.

## 4. Option protocol

Use stable `{turn}{letter}` identifiers:

```text
1a  1b  1c
2a  2b  2c
```

Each option uses the stable id as both its DOM anchor and its visible identity:

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

  <div class="pde-explain">
    <p><b>Idea</b><span>Core hypothesis.</span></p>
    <p><b>Key move</b><span>What structurally distinguishes this option.</span></p>
    <p><b>Tradeoff</b><span>What this option gains and gives up.</span></p>
  </div>
</article>
```

Option explanation stays close to the design and covers the most useful of:

- **Idea / hypothesis** — what the option believes about the problem;
- **Key move** — the structural or interaction decision that distinguishes it;
- **Why it may work** — what it gains;
- **Tradeoff** — what it makes harder or gives up.

A few specific points are usually more useful than a long case-study narrative.

### Stable references

Every visible reference to an existing turn, option, or baseline uses a link to its document anchor:

```html
<a href="#2a">2a</a>
<a href="#1c">1c</a>
<a href="#baseline">0</a>
```

This keeps conversational identity and spatial navigation aligned.

### Lineage is not the same as baseline context

`data-parent` records an intentional design lineage relationship, not merely the fact that a baseline exists.

Use `data-parent="baseline"` when an option is explicitly an evolution or riff on the baseline. A first-turn option that deliberately rethinks the problem from first principles may coexist with a visible baseline without claiming the baseline as its parent.

For later turns, use parent ids when a variant clearly riffs on or combines earlier work. When a concept has multiple meaningful sources, express those sources in the visible explanation and links; keep the primary `data-parent` for the main lineage anchor when useful.

## 5. Baseline protocol

When a reliable current state exists, render it as the oldest visible state:

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

Represent the current state faithfully enough to support comparison with the new options. Baseline annotations, when useful, identify source, state, or relevant constraints; they do not need to prescribe the future direction.

## 6. Navigation suggestions

End each turn with a small number of concrete paths through the design space. Useful suggestions include:

- riffing on one option;
- combining specific parts from two options;
- exploring a different axis;
- increasing or reducing fidelity;
- converging on an option when the user is ready.

Use stable linked ids wherever a suggestion references existing work.

## 7. Canvas substrate

The canvas is infrastructure for comparison. Use a restrained neutral substrate, compact labels, subtle separators, and enough whitespace for sibling designs to remain the visual focus.

The exploration chrome should remain consistent across turns while individual options may use whatever visual language the brief requires.

## 8. Artifact lifecycle and naming

Maintain one primary exploration artifact for the visible design space.

Derive a concise, stable, kebab-case filename from the actual subject being explored, for example:

```text
search-and-go-exploration.html
checkout-flow-exploration.html
analytics-dashboard-exploration.html
```

If an exploration artifact already exists for the project, continue editing that file across turns. If the host requires a specific entry path, follow the host requirement while preserving this document protocol.

Supporting files may exist when the host, implementation, or requested output genuinely needs them; the persistent options canvas remains the primary visible exploration artifact.

## 9. Progressive authoring

When live preview refreshes as the artifact changes, establish the primary file early and build the newest state incrementally:

1. create or open the exploration artifact;
2. insert the newest turn shell in canonical position;
3. render coherent sibling options as they become ready;
4. add local reasoning;
5. finish with navigation suggestions.

On later turns, establish the new turn at the top first and fill it while older states remain intact.

This is progressive enhancement. Hosts that expose only a final-write workflow still use the same persistent document semantics.

## 10. Open Design compatibility

Open Design may apply host-level discovery or design-direction guidance before this skill runs. Use relevant host guidance as context while preserving the parallel exploration protocol.

If a host-level visual direction is already active, meaningful divergence can still occur in structure, hierarchy, interaction, navigation, density, and content strategy. When visual direction itself is the design question, allow option-local visual systems as far as the host permits.

## Structural validation

Before finishing a turn, verify the protocol rather than a specific visual style:

- `.pde-canvas` contains visible design states in newest-first order;
- every turn has `id="tN"` and `data-turn="N"`;
- every option has a stable `id` and matching `data-option`;
- every visible reference to an existing state links to its anchor;
- a baseline appears when reliable current-state evidence exists and is omitted when it cannot be established;
- baseline presence and `data-parent` lineage are treated as separate concepts;
- older states preserve their ids and meaning;
- sibling options are rendered and directly comparable;
- reasoning stays local to the state it explains;
- the artifact filename reflects the actual subject and remains stable across turns.

The target experience is:

> I can see the current state when one exists, compare several real alternatives at once, refer to any state by a stable id, ask for another riff, and keep the visible path of exploration in one place.
