# Parallel Exploration Review Checklist

Background documentation for reviewing a persistent options-canvas run.

The checklist focuses on protocol stability rather than a particular visual style or writing format.

## A. Context and baseline

- [ ] The available design context was inspected before alternatives were generated.
- [ ] A trustworthy current state appears as `0 · Baseline` when one can be established.
- [ ] Greenfield or insufficient-context work begins cleanly with Turn 1.
- [ ] Baseline evidence and design lineage are represented as separate concepts.

## B. Divergence

- [ ] The turn contains multiple rendered sibling alternatives.
- [ ] The default sibling count is 3 unless the user or brief calls for another count.
- [ ] Siblings differ on consequential dimensions relevant to the design question.
- [ ] The alternatives are developed far enough for the design itself to be judged.
- [ ] Convergence remains user-directed.

## C. Visible document protocol

- [ ] `main.pde-canvas` owns the complete visible exploration document.
- [ ] Its direct visible state children are ordered newest-first.
- [ ] The optional baseline is the oldest visible state.
- [ ] Every turn has `id="tN"` and matching `data-turn="N"`.
- [ ] Every option has a stable DOM `id` and matching `data-option`.
- [ ] Visible references to existing design-state ids navigate to their anchors.

## D. Turn and history behavior

- [ ] The newest turn appears before earlier turns.
- [ ] Turn framing explains the design question represented by that state when framing is useful.
- [ ] Sibling options are directly comparable within the turn.
- [ ] Earlier turns retain stable ids, meaning, and visible content.
- [ ] Descendant options expose meaningful lineage when they branch from earlier work.
- [ ] Continuation paths, when present, point to concrete moves in the design space.

## E. Option clarity

For each option:

- [ ] The stable id and concise direction name are visible.
- [ ] The design is rendered rather than represented only by prose.
- [ ] Any annotation stays close to the work it explains.
- [ ] The annotation format is proportionate to what the option needs clarified.
- [ ] `data-parent` reflects intentional lineage when a primary parent exists.

## F. Comparison quality

- [ ] Viewport, content, and fidelity are comparable when controlled conditions improve the comparison.
- [ ] The canvas substrate remains visually subordinate to the options.
- [ ] Individual options retain freedom to use the visual language appropriate to the brief.

## G. Artifact lifecycle

- [ ] The primary artifact name reflects the subject or a host-required entry path.
- [ ] The filename remains stable across follow-up turns.
- [ ] Later turns extend the visible exploration history in the same primary artifact.

## H. Progressive authoring

When the host supports live preview refreshes:

- [ ] The primary canvas becomes available early enough to show meaningful progress.
- [ ] The newest turn can take shape through coherent incremental updates.
- [ ] Incremental updates preserve stable ids and historical states.

For final-write hosts, the same document semantics apply without progressive preview.

## Final test

The exploration succeeds if the user can truthfully say:

> I can see the current state when one exists, compare several real options at once, navigate to any referenced state by id, ask for another riff, and keep the visible path of exploration in one place.
