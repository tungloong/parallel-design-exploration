# Parallel Design Exploration

A community-oriented Open Design scenario for **persistent parallel prototyping inside one visual document**.

Instead of treating design iteration as one mutable latest state:

```text
brief → one answer → modify → replace → modify
```

this plugin keeps the design space visible:

```text
TURN 3:  3a   3b   3c   ← newest
TURN 2:  2a   2b   2c
TURN 1:  1a   1b   1c
```

Sibling options are rendered together, option ids remain stable across conversation, and later turns branch from earlier work without erasing the visible exploration history.

## Status

**v0.5 — persistent options canvas.**

The plugin can be selected directly as an Open Design Active Plugin and remains community-safe by requesting only `prompt:inject`.

v0.5 focuses the contract on a reusable interaction model rather than any particular test prompt or product type.

## What the plugin changes

### One persistent visual document

The primary artifact is `design-exploration.html`. The exploration itself lives in that document rather than in a launcher that points to disconnected alternatives.

### Newest turn first

A new design round is inserted above older rounds. Earlier work remains visible and keeps its original identity.

### Stable option ids

Options use short ids such as `1a`, `1b`, `2a`. Those ids connect the canvas and chat:

```text
Keep 2a's hierarchy, but use the interaction from 1c.
```

### Richer design reasoning

Each option has:

- a stable id and concise direction name;
- the rendered design itself;
- a compact explanation of its hypothesis, key move, advantage, and tradeoff.

Each turn also explains the purpose of the round and ends with a few concrete follow-up ideas.

### Quiet canvas

The exploration surface uses a restrained neutral background, lightweight labels, subtle separators, and minimal chrome. The canvas is infrastructure; the design options should carry the personality.

### Progressive authoring when available

The skill prefers to establish the exploration file early and fill the current turn incrementally when the host can refresh previews on file changes. Open Design already has live project/artifact preview infrastructure, and many built-in prototype skills declare debounced HTML preview reloads. The exact streaming granularity still depends on the active agent and host editing path, so progressive rendering is treated as an enhancement rather than a correctness requirement.

## Install

```bash
od plugin install github:tungloong/parallel-design-exploration
```

Then select **Parallel Design Exploration** directly as the Active Plugin.

If an older version is installed, reinstall or upgrade it so Open Design sees the current manifest and skill package.

## Runtime model

First turn:

```text
TURN 1 · explore the problem

1a                     1b                     1c
[design]               [design]               [design]
[explanation]          [explanation]          [explanation]

Try next: ...
```

Follow-up turn:

```text
TURN 2 · riffs on 1b

2a                     2b                     2c
[design]               [design]               [design]
[explanation]          [explanation]          [explanation]

Try next: ...

────────────────────────────────────────────
TURN 1 · unchanged
1a                     1b                     1c
```

See [`examples/single-document-exploration.html`](examples/single-document-exploration.html).

## Design principles

1. Diverge before converge.
2. Prototype alternatives rather than merely describing them.
3. Juxtapose sibling options in one visual field.
4. Use one persistent exploration document.
5. Put the newest turn first while preserving prior turns.
6. Give every option a stable conversational identity.
7. Make lineage explicit when later options branch from earlier ones.
8. Explain design hypotheses and tradeoffs close to the design.
9. Keep the canvas visually subordinate to the options.
10. Let the user decide when to converge.

## Open Design compatibility

The plugin is intentionally shaped like a community-safe standalone scenario:

```text
kind: scenario
taskKind: new-generation
mode: prototype
surface: web
capabilities: [prompt:inject]
```

Open Design's host may still apply its own discovery and design-direction guidance. This plugin treats that guidance as context while preserving the requested parallel exploration structure. A future host-level parallel direction policy could make unrestricted multi-style divergence even stronger, but the persistent options canvas does not depend on such an upstream change.

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
Explore three materially different ways to solve this design problem. Keep the options together and do not converge yet.
```

Later:

```text
Take 1b as the parent and show three different riffs on it.
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
