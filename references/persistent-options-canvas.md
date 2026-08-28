# Persistent Options Canvas — behavioral reference

This note documents the interaction model implemented by the plugin. It is a behavioral synthesis grounded in parallel prototyping, persistent visual workspaces, and observed design-tool patterns.

## Core model

A persistent options canvas combines two kinds of design memory:

- **spatial memory** — sibling alternatives from the same exploration turn remain visible together;
- **temporal memory** — later turns are added without erasing earlier work.

The result behaves more like a studio wall than a single mutable mockup.

## State model

The visible document is a stack of design states:

```text
Turn 3   ← newest
Turn 2
Turn 1
0 · Baseline   ← only when a reliable current state exists
```

A turn contains sibling options. The optional baseline is a reference state representing what exists before exploration.

### Baseline is evidence, not lineage

A baseline answers: **what is the current state?**

Lineage answers: **which earlier design is this option intentionally derived from?**

These are separate concepts. A project can have a visible baseline while a new option deliberately starts from first principles. Conversely, an option may explicitly riff on the baseline and record that lineage.

This distinction keeps redesign work honest: the current state remains visible without silently constraining future directions.

## Stable identities

Turns and options receive stable anchors:

```text
t1, t2, t3
1a, 1b, 1c
2a, 2b, 2c
```

The same identities are used in the visual document and in conversation. Every visible reference to an existing state links back to its anchor, so a sentence such as:

```text
Combine the structure of 2a with the interaction from 1c.
```

is also navigable inside the canvas.

## Sibling comparison

Options within a turn are shown together whenever practical. The layout should make comparison the default action rather than forcing navigation between separate files or views.

The options vary on dimensions that matter to the brief: structure, hierarchy, interaction, navigation, visual language, content strategy, or other relevant axes.

## Visible protocol and execution semantics

The plugin separates two layers:

- **execution semantics** guide how the agent acquires context, controls comparison conditions, generates alternatives, and preserves history;
- **visible document protocol** defines what becomes part of the user's design space.

Execution bookkeeping is not automatically user-facing content. The visible canvas is composed of design states, local reasoning, and navigation cues that help the user understand and continue the exploration.

## Explanation near the work

Each option can include compact reasoning near the rendered design:

- hypothesis;
- distinguishing move;
- likely advantage;
- tradeoff.

The goal is to make the design legible without turning the canvas into a presentation deck.

## Navigation suggestions

Each turn can end with a few concise next-step paths: riff on one option, combine specific parts, explore another axis, or converge when the user is ready.

## Canvas styling

The substrate is intentionally quiet: neutral background, compact labels, restrained separators, and minimal framing. The exploration chrome stays consistent while the options themselves carry the design personality demanded by the brief.

## Progressive rendering

When the host refreshes HTML as project files change, progressive authoring can make the design space appear while generation is still in progress:

1. establish the newest turn shell;
2. render coherent sibling options incrementally;
3. add local reasoning;
4. add navigation suggestions.

The interaction model still works in hosts that only expose a final-write workflow.

## Method lineage

The behavior is consistent with long-standing design practices such as parallel prototyping, pin-up critique, artboard duplication, design-space exploration, and persistent visual workspaces.

Modern AI design tools make the pattern especially useful because alternatives can be produced quickly enough that visible divergence can become a normal interaction rather than an expensive exception.
