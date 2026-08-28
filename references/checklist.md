# Parallel Exploration Review Checklist

Background documentation for reviewing a persistent options-canvas run.

## A. Context and baseline evidence

- [ ] The agent inspected the available design context before generating alternatives.
- [ ] A reliable current state is rendered as `0 · Baseline` when one can be established.
- [ ] A baseline is omitted when the available material is insufficient to reconstruct a trustworthy current state.
- [ ] The baseline is treated as comparison evidence rather than an automatic design constraint.
- [ ] Baseline presence and `data-parent` lineage are treated as separate concepts.

## B. Divergence

- [ ] There are multiple sibling alternatives unless the user explicitly requested one.
- [ ] The default sibling count is 3 unless the brief or user specifies otherwise.
- [ ] Each sibling represents a consequentially different design hypothesis.
- [ ] Differences are substantive on axes relevant to the brief rather than superficial token changes.
- [ ] Exploration remains open until the user asks to converge.

## C. Visible document protocol

- [ ] There is one primary persistent exploration artifact.
- [ ] `.pde-canvas` contains visible design states in newest-first order.
- [ ] Every turn has a stable `id="tN"` and matching `data-turn="N"`.
- [ ] Every option has a stable DOM `id` and matching `data-option`.
- [ ] Every visible reference to an existing turn, option, or baseline links to its document anchor.
- [ ] The optional baseline is the oldest visible state.
- [ ] Project-method bookkeeping stays out of the visible canvas unless it genuinely helps interpret a design state.

## D. Turn structure

- [ ] The newest turn appears before older turns.
- [ ] Turn framing concisely explains the design question or riff represented by that state.
- [ ] Sibling options are directly comparable within the same turn.
- [ ] Older turns retain their original ids and meaning.
- [ ] Descendant turns expose meaningful lineage to earlier options where applicable.
- [ ] The turn ends with a small number of useful paths for continuing the design space.

## E. Option anatomy

For each option:

- [ ] The stable id and concise direction name are visible.
- [ ] The design is rendered far enough to evaluate rather than merely described.
- [ ] Reasoning is local to the option it explains.
- [ ] The core idea or hypothesis is legible.
- [ ] The distinguishing move is legible.
- [ ] Tradeoffs are stated when useful.
- [ ] `data-parent` reflects intentional lineage rather than generic project context.

## F. Comparison quality

- [ ] Siblings use comparable viewport/device dimensions when direct visual comparison benefits from controlled conditions.
- [ ] Siblings use comparable content or data scenarios where that improves fairness.
- [ ] Fidelity differences do not accidentally bias the comparison.
- [ ] The canvas chrome remains visually subordinate to the designs.

## G. Artifact lifecycle

- [ ] The filename is derived from the actual subject or a host-required entry path.
- [ ] The primary filename remains stable across follow-up turns.
- [ ] Later turns extend the existing exploration artifact instead of replacing its visible history.

## H. Progressive authoring

When the host supports preview refreshes:

- [ ] The primary document is established early enough to become visible during generation.
- [ ] The newest turn can take shape through coherent incremental updates.
- [ ] Progressive authoring preserves stable ids and historical states.

If the host exposes only a final-write workflow, this section is informational rather than a failure condition.

## I. Convergence

When the user asks to choose, combine, finalize, promote, or proceed with a direction:

- [ ] Source option ids are named.
- [ ] Combined directions identify their contributing earlier states where useful.
- [ ] The exploration history remains available as design context.

## Final test

The exploration succeeds if the user can truthfully say:

> I can see the current state when one exists, compare several real options at once, navigate to any referenced state by id, ask for another riff, and keep the visible path of exploration in one place.
