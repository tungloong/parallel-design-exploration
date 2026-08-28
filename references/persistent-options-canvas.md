# Persistent Options Canvas — behavioral reference

This note documents the interaction model implemented by the plugin. It is a behavioral synthesis grounded in parallel prototyping, persistent visual workspaces, and established design-tool patterns.

## Core model

A persistent options canvas combines two kinds of design memory:

- **spatial memory** — sibling alternatives from the same exploration turn remain visible together;
- **temporal memory** — later turns are added while earlier work remains visible.

The result behaves more like a studio wall than a single mutable mockup.

## State model

The complete visible document is the canvas, whose direct states are ordered newest-first:

```text
Turn 3   ← newest
Turn 2
Turn 1
0 · Baseline   ← when a reliable current state exists
```

A turn contains sibling options. The optional baseline is a reference state representing what exists before exploration.

### Baseline is evidence, lineage is descent

A baseline answers: **what is the current state?**

Lineage answers: **which earlier design is this option intentionally derived from?**

These are separate concepts. A project can have a visible baseline while a new option starts from first principles. Another option may explicitly riff on the baseline or a prior option and record that lineage.

## Stable identities

Turns and options receive stable anchors:

```text
t1, t2, t3
1a, 1b, 1c
2a, 2b, 2c
```

The same identities are used in the visual document and in conversation. A sentence such as:

```text
Combine the structure of 2a with the interaction from 1c.
```

can link directly to those states inside the canvas.

## Sibling comparison

Options within a turn are shown together whenever the medium allows. The layout makes comparison immediate and keeps the sibling relationship visually obvious.

The options vary on dimensions that matter to the brief: structure, hierarchy, interaction, navigation, visual language, content strategy, or other relevant axes.

## Complete visible document

The canvas is the visible artifact, rather than one section inside a separate presentation wrapper. Turn framing, option labels, local annotation, continuation cues, and baseline context all live inside the state structure of the canvas.

This gives the protocol a clear ownership boundary while keeping the surrounding visual system intentionally lightweight.

## Annotation near the work

Annotations help make differences legible, but their form follows the design rather than a fixed review schema.

Depending on the work, an option may benefit from:

- one concise sentence;
- a short paragraph;
- a few bullets;
- a compact tradeoff note;
- little or no additional prose when the design is already self-explanatory.

The stable part of the protocol is the option identity and its place in history; the annotation remains expressive.

## Navigation suggestions

A turn can end with a few concise next-step paths: riff on one option, combine specific parts, explore another axis, or converge when the user is ready.

## Canvas styling

The substrate is intentionally quiet: neutral background, compact labels, restrained separators, and enough whitespace for the rendered options to carry the visual personality of the brief.

## Progressive rendering

When the host refreshes HTML as project files change, progressive authoring can make the design space appear while generation is still in progress:

1. establish the newest turn shell;
2. render coherent sibling options incrementally;
3. add local annotation where useful;
4. add continuation cues when useful.

The same interaction model also works in hosts that expose only a final-write workflow.

## Method lineage

The behavior is consistent with long-standing design practices such as parallel prototyping, pin-up critique, artboard duplication, design-space exploration, and persistent visual workspaces.

Modern AI design tools make the pattern especially useful because alternatives can be produced quickly enough that visible divergence can become a normal interaction rather than an expensive exception.
