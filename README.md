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

**v0.3 — community-safe standalone Active Plugin scenario.**

The repository has a portable `SKILL.md` plus an Open Design `open-design.json` sidecar. In Open Design it is authored as a `new-generation` **scenario**, so it can be selected directly as the Active Plugin and does not depend on Web Prototype.

The board uses normal HTML as the compatibility layer; v0.3 does not add a native infinite-canvas renderer to Open Design core.

## Why v0.3 changed the manifest again

After comparing the plugin against Open Design's actual `plugins/community/` catalog, v0.2 was still too close to a first-party trusted plugin: it declared its own pipeline and filesystem-writing capability.

That is a poor default for a directly installed community/GitHub plugin because Open Design's community trust model starts those installs as **restricted**. A manifest-owned pipeline causes additional capabilities to be required before the plugin can apply.

v0.3 follows the community-safe pattern instead:

```text
kind: scenario
taskKind: new-generation
mode: prototype
surface: web
capabilities: [prompt:inject]
```

It deliberately does **not** declare a custom `od.pipeline`, `fs:write`, or shell capability.

Open Design's host `new-generation` scenario supplies normal planning, artifact writing, live preview, and critique. Parallel Design Exploration supplies the design-method contract through `SKILL.md`, references, templates, and examples.

This is similar to the pattern used by community design skills such as Hallmark: the skill can contain detailed generation/editing behavior without requiring the plugin manifest itself to own filesystem execution.

See [`references/open-design-community-alignment.md`](references/open-design-community-alignment.md).

## Community references used for alignment

We reviewed several representative Open Design community plugins:

- **Community Registry Starter** — standalone `scenario`, `new-generation`, `prototype`, `prompt:inject` only. This is the clearest minimal Active Plugin pattern.
- **Hallmark** — a substantial UI generation/redesign skill whose manifest still requests only `prompt:inject`; most behavior lives in `SKILL.md` and references.
- **Humanize PPT** — a legitimate higher-capability exception that explicitly requests `fs:read`, `fs:write`, and `bash`, and therefore crosses the trust gate.
- **Design System Source Context / Clone Audit** — narrow capability-style plugins using `kind: skill` and `prompt:inject` only.

Our plugin is closer to **Community Registry Starter + Hallmark** than to Humanize PPT: it should be a standalone scenario, but its distinctive behavior is methodological rather than a need for a separate privileged runtime.

## Install as a standalone Open Design plugin

```bash
od plugin install github:tungloong/parallel-design-exploration
```

Because v0.3 requests only the restricted-safe `prompt:inject` capability, a normal direct GitHub install should no longer require an additional capability grant merely to become Active.

If you already installed v0.2, reinstall or upgrade it so Open Design reads the v0.3 manifest instead of a cached v0.2 record/snapshot.

After installation, select **Parallel Design Exploration** directly as the project/plugin entry point. You should not need to select Web Prototype first.

## Expected Active Plugin behavior

When correctly applied, the run should identify `parallel-design-exploration` as the Active Plugin and load the full local `SKILL.md` plus the declared reference/template assets.

The host may still use its built-in `new-generation` pipeline. If a host `direction-picker` appears during planning, the skill contract explicitly prevents it from becoming a convergence gate: candidate directions must be carried forward and rendered before the user is asked to choose.

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

Open Design's conventional new-generation workflow can encourage choosing a direction before artifact generation. This scenario changes the interaction contract at the skill layer:

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
│   ├── open-design-community-alignment.md
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

`SKILL.md` remains portable. Clients that support Agent Skills can use the same repository as a methodology Skill. In Open Design, the primary target is the **standalone Active Plugin scenario** described above.

## Trust UI note

Open Design's current community registry explicitly says community plugins remain restricted until installed and trusted. In the current UI code we reviewed, the visible trust mutation is attached to **marketplace sources** in the Sources tab; plugin detail surfaces display trust and capability metadata, but the reviewed path does not expose a per-installed-plugin capability grant control.

That is another reason v0.3 is intentionally restricted-safe by default.

## Local validation

After cloning the repo into an environment with the Open Design CLI:

```bash
od plugin validate .
od plugin install .
```

Then run a real exploration and check it against `references/checklist.md`.

## Next steps

Potential follow-ups after validating v0.3 in real Open Design sessions:

- native board/lineage rendering instead of a compatibility HTML board;
- automatic `exploration.json` reconciliation;
- artifact-level immutable snapshots for siblings;
- visual branch connectors and compare mode;
- explicit `Explore` vs `Converge` modes;
- integration with Open Design's file/version history without hiding historical variants in a separate panel;
- an optional trusted/advanced distribution lane with a manifest-owned custom pipeline;
- an upstream feature proposal for a first-class Parallel Exploration scenario.

## License

MIT.
