# Parallel Design Exploration

An experimental Open Design scenario for **parallel prototyping on a persistent exploration canvas**.

Instead of the common agent loop:

```text
brief → choose one direction → generate → overwrite → refine
```

this scenario aims for:

```text
                     ┌─ 1A ── 2A
brief → baseline ────┼─ 1B ── 2B
                     └─ 1C ── 2C

          all prior work remains visible
```

The goal is to reproduce the most useful part of a traditional design studio / large-canvas workflow in an agentic design environment: **make alternatives concrete, place them next to one another, and preserve the path that produced them.**

## Status

**v0.2 — standalone Active Plugin scenario.**

The repository still has a portable `SKILL.md`, but its Open Design sidecar is now authored as a `new-generation` **scenario** so it can own a project/run directly. It does not depend on Web Prototype.

The board uses normal HTML as the compatibility layer; v0.2 does not add a native infinite-canvas renderer to Open Design core.

## Why v0.2 changed the manifest

The first version was scaffolded as `od.kind: skill` and declared a required `brief` plugin input. That was a poor fit for the Open Design one-click Active Plugin path:

- Open Design applies a plugin **before** starting the run;
- required `od.inputs` must therefore already have values or defaults at apply time;
- the user's free-form chat prompt is not automatically copied into an input named `brief`;
- v0.1's required `brief` had no default, so applying the plugin could fail before an active snapshot was created.

v0.2 treats the user's chat prompt itself as the design brief. The only manifest input is optional `variantCount`, defaulting to 3.

The manifest also now uses the same standalone shape as first-party prototype examples:

```text
kind: scenario
taskKind: new-generation
mode: prototype
surface: web
```

and uses standard Open Design stage ids:

```text
discovery → plan → generate → critique
```

Crucially, the `plan` stage does **not** contain `direction-picker`; the scenario renders all sibling directions before asking the user to converge.

## Install as a standalone Open Design plugin

```bash
od plugin install github:tungloong/parallel-design-exploration
```

GitHub-installed third-party plugins are restricted by default in Open Design. Because this scenario declares its own pipeline and writes artifacts, trust it before using it as an Active Plugin:

```bash
od plugin trust parallel-design-exploration
```

If you already installed an older version, reinstall it so the daemon picks up the v0.2 manifest. Use the uninstall/install flow supported by your Open Design build, then trust the newly installed record again if necessary.

After installation, select **Parallel Design Exploration** directly as the project/plugin entry point. You should not need to select Web Prototype first.

## Expected Active Plugin behavior

When correctly applied, the run should have an Applied Plugin Snapshot for `parallel-design-exploration`, containing this scenario's own pipeline and full local `SKILL.md` context.

The first exploration round should look conceptually like:

```text
ROUND 1

1A                     1B                     1C
[full prototype]       [full prototype]       [full prototype]
rationale              rationale              rationale
trade-off              trade-off              trade-off
```

A later turn appends rather than replaces:

```text
ROUND 1
1A        1B        1C

ROUND 2
2A        2B        2C
↑         ↑         ↑
1A        1B        1C
```

A follow-up may also branch several descendants from one promising earlier direction:

```text
1B
├── 2A
├── 2B
└── 2C
```

## What it changes

Open Design's default new-generation scenario can expose a direction picker before artifact generation. This scenario intentionally changes that interaction contract:

- directions become **fully rendered sibling prototypes**, not only direction cards;
- the user does not have to pick a winner before seeing the alternatives;
- variants are presented side by side in one neutral working board;
- subsequent feedback appends a new round instead of mutating the old round;
- every variant has stable identity and parent lineage;
- convergence happens only when the user asks for it.

## Repository structure

```text
.
├── SKILL.md
├── open-design.json
├── LICENSE
├── references/
│   ├── parallel-prototyping.md
│   ├── exploration-canvas.md
│   └── checklist.md
├── templates/
│   ├── exploration-board.html
│   └── exploration.schema.json
└── examples/
    ├── mobile-ui-exploration.md
    └── mobile-search/
        ├── board.html
        ├── exploration.json
        └── round-1/
            ├── 1A.html
            ├── 1B.html
            └── 1C.html
```

The references and templates are declared as plugin assets so they are part of the applied bundle rather than relying on a separate plugin for design behavior.

## Design principles

1. Diverge before converge.
2. Prototype alternatives rather than merely describing them.
3. Juxtapose alternatives so visual comparison is immediate.
4. Preserve previous explorations by default.
5. Treat each iteration as additive.
6. Make lineage explicit.
7. Allow branching from any prior state.
8. Keep the exploration board visually neutral.
9. Let the human decide when to converge.

## Why

The workflow is grounded in established design practice rather than being an AI-specific prompt trick. The references included in this repository cover:

- **parallel prototyping** research showing benefits from developing alternatives in parallel;
- the broader divergence-before-convergence logic used in design methods;
- artboard/frame/infinite-canvas workflows that keep alternatives spatially visible;
- visual exploration organization and version-history patterns in modern design tools.

See [`references/parallel-prototyping.md`](references/parallel-prototyping.md) and [`references/exploration-canvas.md`](references/exploration-canvas.md).

## Example request

Once the plugin itself is Active, the prompt can remain focused on the actual product problem:

```text
Explore the search screen for this iOS app. I want structurally different interaction
ideas, not cosmetic themes. Keep all alternatives on one board and do not recommend
a winner yet.
```

On a later turn:

```text
I like 1B's input placement, but I want to see three different ways of handling the
results while keeping that interaction model. Preserve Round 1.
```

Expected result: three Round 2 descendants of `1B`, while Round 1 remains available for comparison.

## Optional Skill consumption

`SKILL.md` remains portable. Clients that support Agent Skills can use the same repository as a methodology Skill. In Open Design, however, the primary v0.2 target is the **standalone Active Plugin scenario** described above.

## Local validation

After cloning the repo into an environment with the Open Design CLI:

```bash
od plugin validate .
od plugin install .
```

Then run a real exploration and check it against `references/checklist.md`.

## Next steps

Potential follow-ups after validating v0.2 in real Open Design sessions:

- native board/lineage rendering instead of a compatibility HTML board;
- automatic `exploration.json` reconciliation;
- artifact-level immutable snapshots for siblings;
- visual branch connectors and compare mode;
- explicit `Explore` vs `Converge` modes;
- integration with Open Design's file/version history without hiding historical variants in a separate panel;
- an upstream feature proposal for a first-class Parallel Exploration scenario.

## License

MIT.
