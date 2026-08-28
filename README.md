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
0 · BASELINE             ← when a real current design exists
```

Sibling options are rendered together, option ids remain stable across conversation, and later turns branch from earlier work without erasing the visible exploration history.

## Status

**v0.6 — baseline-aware persistent options canvas.**

The plugin can be selected directly as an Open Design Active Plugin and remains community-safe by requesting only `prompt:inject`.

v0.6 simplifies the visible document grammar, adds a conditional current-state baseline for redesign/existing-project work, and derives the exploration filename from the actual design subject rather than hard-coding a plugin-specific filename.

## What the plugin changes

### Turn-first visual document

The primary artifact begins directly with the newest exploration turn. The workflow is represented by the turn/option structure itself rather than by a separate page-level project narrative.

### Conditional baseline

When the user provides a real current state — for example an imported codebase, existing screen, screenshot, design file, or prior artifact — the plugin preserves that current state as `0 · Baseline` before exploring alternatives.

For genuinely greenfield work, no baseline is invented.

### Contextual artifact naming

The exploration artifact gets a concise name derived from the subject, for example:

```text
search-and-go-exploration.html
checkout-flow-exploration.html
analytics-dashboard-exploration.html
```

The name stays stable across follow-up turns.

### Newest turn first

A new design turn is inserted above older turns. Earlier work remains visible and keeps its original identity.

### Stable option ids

Options use short ids such as `1a`, `1b`, `2a`. Those ids connect the canvas and chat:

```text
Keep 2a's hierarchy, but use the interaction from 1c.
```

### Design reasoning next to the work

Each option contains:

- a stable id and concise direction name;
- the rendered design itself;
- compact reasoning about its hypothesis, key move, advantage, and tradeoff.

Each turn also ends with a few concrete follow-up ideas for navigating the design space.

### Quiet canvas

The exploration surface stays visually subordinate: neutral background, lightweight labels, subtle separators, and enough whitespace to compare the actual designs.

### Progressive authoring when available

The skill prefers to establish the contextually named exploration file early and fill the current turn incrementally when the host can refresh previews on file changes. The exact streaming granularity still depends on the active agent and host editing path, so progressive rendering is treated as an enhancement rather than a correctness requirement.

## Install

```bash
od plugin install github:tungloong/parallel-design-exploration
```

Then select **Parallel Design Exploration** directly as the Active Plugin.

If an older version is installed, reinstall or upgrade it so Open Design sees the current manifest and skill package.

## Runtime model

Existing-design task:

```text
TURN 1 · explore alternatives

1a                     1b                     1c
[design]               [design]               [design]
[explanation]          [explanation]          [explanation]

Try next: ...

────────────────────────────────────────────
0 · BASELINE
[current design]
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

────────────────────────────────────────────
0 · BASELINE
[current design]
```

For greenfield work, the document begins at Turn 1 with no invented baseline.

See [`examples/single-document-exploration.html`](examples/single-document-exploration.html).

## Design principles

1. Diverge before converge.
2. Preserve a real current state before varying it.
3. Prototype alternatives rather than merely describing them.
4. Juxtapose sibling options in one visual field.
5. Keep the newest turn first while preserving prior work.
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

Open Design's host may still apply its own discovery and design-direction guidance. This plugin treats that guidance as context while preserving the requested parallel exploration structure.

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
