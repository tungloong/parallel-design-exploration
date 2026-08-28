# Parallel Exploration Checklist

Background documentation for reviewing a persistent options-canvas run.

## A. Divergence

- [ ] There are multiple sibling alternatives unless the user explicitly requested one.
- [ ] Default sibling count is 3 unless the brief suggests otherwise.
- [ ] Each sibling represents a consequentially different design hypothesis.
- [ ] Differences are substantive on the axes relevant to the brief, not merely cosmetic token swaps.
- [ ] No sibling is framed as the winner unless the user asked to converge.

## B. Persistent options canvas

- [ ] There is one primary exploration document.
- [ ] Siblings are directly visible together rather than requiring file/tab hopping.
- [ ] Every option has a stable short id such as `1a`, `1b`, `2a`.
- [ ] Siblings are spatially adjacent whenever practical.
- [ ] The canvas is visually quiet and subordinate to the design options.

## C. Turn structure

- [ ] The newest turn appears before older turns.
- [ ] The turn header explains what the current round is exploring.
- [ ] Descendant turns identify the earlier option(s) they riff on.
- [ ] Older turns remain visible and retain their original ids.
- [ ] A new turn does not silently redesign historical options.
- [ ] The turn ends with 2–3 useful follow-up ideas for navigating the design space.

## D. Option anatomy

For each option:

- [ ] Stable id and concise direction name are visible.
- [ ] The design itself is rendered far enough to evaluate.
- [ ] The explanation states the core idea/hypothesis.
- [ ] The distinguishing design move is legible.
- [ ] A likely advantage and tradeoff are stated when useful.
- [ ] Parent lineage is present for descendant options.

## E. Comparison fairness

- [ ] Siblings use comparable viewport/device dimensions when the task benefits from direct visual comparison.
- [ ] Siblings use comparable content/data scenarios where practical.
- [ ] Fidelity differences do not unfairly bias comparison.

## F. Progressive authoring

When the host supports preview refreshes:

- [ ] The primary document is established early enough to become visible during generation.
- [ ] The current turn can take shape through incremental file updates rather than waiting unnecessarily for one final monolithic write.
- [ ] Progressive authoring does not compromise stable ids or corrupt earlier turns.

If the host only supports a final-write workflow, this section is informational rather than a failure condition.

## G. Convergence

Unless the user explicitly asks to choose, combine, finalize, promote, or proceed with a direction:

- [ ] No winner is declared.
- [ ] No branch is deleted merely because it appears weaker.

If the user does request convergence:

- [ ] Source option ids are named.
- [ ] Combined directions identify their contributing ancestors.
- [ ] The exploration document remains preserved as design history.

## Final test

The exploration succeeds if the user can truthfully say:

> I can see the newest round immediately, compare its options side by side, refer to any option by id, and continue exploring without losing the path that led here.
