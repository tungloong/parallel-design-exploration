# Persistent Options Canvas — behavioral reference

This note documents the interaction pattern implemented by this plugin. It is a behavioral synthesis, not a copy of any proprietary system prompt.

## Core model

A persistent options canvas combines two kinds of design memory:

- **spatial memory** — sibling alternatives from the same exploration round remain visible together;
- **temporal memory** — later rounds are added without erasing earlier work.

The result is a design document that behaves more like a studio wall than a single mutable mockup.

## Interaction grammar

### Turns

Each generation round is a turn. New turns appear before older turns so current work is immediately visible while history remains nearby.

```text
Turn 3
Turn 2
Turn 1
```

### Stable option ids

Options receive short stable ids such as `1a`, `1b`, `2a`. The same ids are used in the visual document and in conversation so users can say things like:

```text
Keep the structure of 2a, but borrow the interaction from 1c.
```

### Sibling comparison

Options within a turn are shown side by side whenever practical. The layout should make visual comparison the default action rather than requiring navigation between alternatives.

### Lineage

A descendant option may point to a parent option from an earlier turn. This makes the evolution of a direction explicit without forcing the entire exploration into a single linear history.

### Explanation

Each option includes compact reasoning near the design: its hypothesis, distinguishing move, likely advantage, and tradeoff. Each turn also explains what the round is exploring.

### Navigation suggestions

A turn ends with a few concise next-step ideas. These suggestions help the user navigate the space without declaring a winner.

## Canvas styling

The exploration surface should be visually quiet: plain neutral background, lightweight labels, restrained separators, and minimal framing. The canvas is infrastructure; the options are the designed objects.

## Progressive rendering

When the host can refresh HTML previews as files change, progressive authoring improves the experience:

1. establish the canvas and new turn shell;
2. render sibling options incrementally;
3. add their reasoning;
4. add turn-level follow-up suggestions.

The document model must still work in hosts that only expose a final-write workflow.

## Method lineage

The behavior is consistent with long-standing design practices such as parallel prototyping, pin-up critique, artboard duplication, design-space exploration, and persistent visual workspaces.

Modern AI design tools make the pattern more valuable because alternatives can be generated quickly enough that visible divergence becomes the default interaction rather than an expensive exception.

## Implementation stance

This repository independently implements the behavioral pattern for Open Design. Public research and observed design-tool behavior may inform the interaction model, but the plugin should remain generic, portable, and suitable for community contribution rather than depending on a particular prompt, product, or proprietary host implementation.
