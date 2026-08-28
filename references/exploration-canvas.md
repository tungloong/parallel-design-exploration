# Reference: Persistent Exploration Canvas

Parallel prototyping explains **why** multiple alternatives should stay alive. The exploration canvas explains **how** they should remain visible and navigable.

This skill combines two forms of history:

```text
SPATIAL HISTORY
A      B      C
side-by-side alternatives

TEMPORAL HISTORY
Round 1 → Round 2 → Round 3
prior states remain recoverable and visible
```

The key design principle is that the current state should not erase the path that produced it.

## 1. Figma — canvas as a working area for exploration

Figma describes the canvas as the working area where designers have room to **explore and iterate on ideas**.

Official guide:
https://help.figma.com/hc/en-us/articles/15297425105303-Explore-design-files

The same guide explains that Pages can be used to:

- manage designs by milestone or status;
- keep a scratchpad of ideas;
- archive older designs.

This is important because it separates two jobs:

- the **canvas** exposes active alternatives spatially;
- **pages/version history** provide additional organization and recovery.

### Implication for this skill

Do not make the user open separate files merely to remember what the previous round looked like. The most relevant prior alternatives should remain on the working board.

## 2. Figma Sections — named regions for ideation

Figma Sections are explicitly intended to group related ideas and designate areas of the canvas for collaboration or ideation.

Official guide:
https://help.figma.com/hc/en-us/articles/9771500257687-Organize-your-canvas-with-sections

A useful analogue for this skill is:

```text
Section / Round 1
[1A] [1B] [1C]

Section / Round 2
[2A] [2B] [2C]
```

The board therefore treats a **round** as a spatial region, not merely a timestamp in hidden history.

## 3. Figma version history — evolution without destructive replacement

Figma design files maintain version history so users can inspect previous iterations and capture milestones.

Official overview:
https://help.figma.com/hc/en-us/articles/15297425105303-Explore-design-files

This is a second safety layer rather than a replacement for spatial comparison.

### Spatial exploration vs version history

```text
Spatial exploration
Used for: active comparison
Visible: A / B / C together
Question: "Which idea is stronger and why?"

Version history
Used for: recovery / temporal trace
Visible: v1 / v2 / v3 in a history UI
Question: "What did this artifact look like before?"
```

Claude Design-like exploration benefits from combining both mental models: alternatives are spatially visible **and** older states are not destroyed.

## 4. Artboards and frames — multiple bounded designs in one document

Long before AI design agents, visual design tools normalized the idea that one document can contain multiple bounded design surfaces.

Adobe Illustrator's multiple-artboard model allowed multiple artboards to be created, positioned, reordered, and viewed in one document. Artboards have long been used for related pages, assets, storyboards, and design alternatives.

Figma frames and similar UI-design primitives continue the same broad working pattern: duplicate a bounded design, move it beside the original, and explore another state without first destroying the source.

### Implication for this skill

Each variant should behave conceptually like an artboard/frame:

- bounded;
- independently addressable;
- comparable in scale with siblings;
- safe to preserve when a descendant is created.

## 5. The pin-up wall mental model

Before digital canvases, design studios already used a spatial review model: sketches, alternatives, intermediate states, and developed proposals are pinned up together so a group can compare them.

The important property is **juxtaposition**.

When alternatives are simultaneously visible, critique naturally becomes relational:

- "A's hierarchy is clearer than B's."
- "B's interaction is stronger, but C handles density better."
- "Can we branch from B and borrow C's result treatment?"

This is qualitatively different from reviewing one latest artifact at a time.

## 6. Board grammar for an agent

An agent tends to optimize every HTML file as a designed deliverable. That instinct is harmful here.

The exploration board is infrastructure, analogous to the empty canvas around artboards. It should not compete with the designs.

### Good board qualities

- neutral background;
- simple round labels;
- stable variant ids;
- consistent prototype viewport sizes;
- enough whitespace to distinguish siblings;
- minimal metadata close to each variant;
- optional lineage indicators;
- large working width on desktop;
- previous rounds remain reachable without opening another artifact.

### Bad board qualities

- landing-page hero;
- marketing copy;
- decorative gradients;
- editorial alternating sections;
- large CTA buttons;
- "recommended" treatment on one variant;
- summary-first structure that forces reading before comparison;
- replacing old variants with updated versions.

## 7. Persistent exploration is not the same as keeping every pixel forever

The immutable unit is the **historical variant**, not necessarily the board shell.

The board itself may be reorganized as it grows. For example, it may change from a 3-column grid to a horizontally scrollable row or add round navigation.

What must remain stable:

- variant identity;
- historical prototype content;
- parent lineage;
- round association;
- feedback/provenance when available.

## 8. Recommended spatial hierarchy

For desktop:

```text
[small workspace header]

BASELINE
[baseline]

ROUND 1
[1A]   [1B]   [1C]

ROUND 2
[2A]   [2B]   [2C]

ROUND 3
...
```

A user should be able to zoom out mentally and understand the design trajectory.

## 9. Design rule derived from the references

> History that matters for active design reasoning should remain visible in the design space, not only recoverable from a hidden version menu.

This is why this skill treats "append, do not replace" as a core behavior rather than an implementation detail.
