# Example: Mobile Search UI Exploration

This walkthrough demonstrates the **session shape** of Parallel Design Exploration. It is an example of the protocol, not a prescribed product style.

## User brief

```text
Explore alternative interaction models for an iOS quick-search app.

The user arrives with a specific search intent and should be able to execute the search
without getting pulled into an infinite content feed. I want structurally different
ideas and I want to compare them before choosing a direction.
```

## Turn 1

The first turn might establish three distinct hypotheses:

```text
1a — Quiet Canvas
Search and result content dominate; almost all surrounding chrome recedes.

1b — Thumb Search Dock
The primary search affordance stays in the thumb zone while results expand above it.

1c — Command Results
Results emphasize the next action rather than feed-like browsing.
```

All three are rendered inside the same exploration document and remain addressable by their stable ids.

A simplified structure looks like:

```html
<main class="pde-canvas" data-pde-version="1">
  <section class="pde-turn" id="t1" data-turn="1">
    <div class="pde-options">
      <article class="pde-option" id="1a" data-option="1a">...</article>
      <article class="pde-option" id="1b" data-option="1b">...</article>
      <article class="pde-option" id="1c" data-option="1c">...</article>
    </div>
  </section>
</main>
```

Annotations can vary with the work. One option may need a single sentence; another may benefit from a short tradeoff note or a few bullets.

## Follow-up feedback

```text
1b feels closest, but the keyboard will already occupy the lower part of the screen.
Keep the dock idea and show me three different ways to handle results in that state.
```

## Turn 2

The next turn branches from `1b`:

```text
2a — Compressed result stack     ← 1b
2b — Result peek + expand        ← 1b
2c — Single-result command       ← 1b
```

The document becomes:

```text
TURN 2
2a        2b        2c
 ↑         ↑         ↑
 └──────── 1b ───────┘

TURN 1
1a        1b        1c
```

And the canonical state structure becomes:

```html
<main class="pde-canvas" data-pde-version="1">
  <section class="pde-turn" id="t2" data-turn="2">
    <article class="pde-option" id="2a" data-option="2a" data-parent="1b">...</article>
    <article class="pde-option" id="2b" data-option="2b" data-parent="1b">...</article>
    <article class="pde-option" id="2c" data-option="2c" data-parent="1b">...</article>
  </section>

  <section class="pde-turn" id="t1" data-turn="1">
    ... original 1a / 1b / 1c ...
  </section>
</main>
```

The newest turn sits above the earlier one while the earlier states keep the same ids and visible content.

## Conversation stays connected to the canvas

Stable ids make follow-up prompts precise:

```text
Go back to 1a and branch a more system-native version.
```

```text
Combine 1c's action treatment with 2b's result expansion.
```

```text
2a is strongest; continue from that direction.
```

The value of the protocol is that each of those sentences refers to a visible, persistent design state rather than an implicit version remembered only by the conversation.
