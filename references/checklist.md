# Parallel Exploration Checklist

Run this checklist before finishing an exploration round.

## A. Divergence

- [ ] There are multiple sibling alternatives unless the user explicitly requested one.
- [ ] Default sibling count is 3; never exceed 5 without a strong reason.
- [ ] Each sibling represents a consequentially different design hypothesis.
- [ ] Alternatives are not merely color, typeface, radius, shadow, or spacing swaps.
- [ ] No sibling is visually framed as the recommended or winning option.
- [ ] The agent has not prematurely collapsed the round into a single answer.

## B. Prototype fidelity

- [ ] Each direction is rendered far enough to judge the key interaction or product idea.
- [ ] Siblings use comparable viewport/device dimensions.
- [ ] Siblings use comparable content/data scenarios where practical.
- [ ] Fidelity differences do not unfairly bias comparison.
- [ ] Important states required by the brief are visible or clearly represented.

## C. Board quality

- [ ] The board looks like a workspace, not a landing page or case study.
- [ ] Round labels are easy to scan.
- [ ] Stable ids such as `1A`, `1B`, `1C` are visible.
- [ ] Siblings in a round are spatially adjacent whenever practical.
- [ ] Rationale is concise and subordinate to the prototypes.
- [ ] There is no hero section, promotional CTA, winner badge, recommendation banner, or decorative narrative around the work.
- [ ] The board's own styling does not compete with the explored designs.

## D. History and lineage

- [ ] Existing historical variants remain unchanged.
- [ ] No old variant id has been reused.
- [ ] New variants have explicit parent ids.
- [ ] New work is appended as a new round rather than replacing the prior round.
- [ ] A branch from an older variant remains valid even if it is not descended from the latest round.
- [ ] `exploration.json` reflects the visible board state.

## E. Follow-up behavior

- [ ] User feedback was interpreted as a graph transformation, not automatically as permission to overwrite.
- [ ] Only useful descendants were generated; one-to-one descendants are not forced.
- [ ] If the user focused on one prior variant, new siblings may intentionally share that same parent.
- [ ] If a historical variant needed repair, the repair is represented explicitly rather than silently rewriting history.

## F. Convergence guard

Unless the user explicitly asked to choose, combine, finalize, promote, or move forward:

- [ ] No winner is declared.
- [ ] No final recommendation is written.
- [ ] No branch is deleted because it appears weaker.
- [ ] The response invites comparison by making differences legible rather than telling the user what to select.

If the user **did** explicitly request convergence:

- [ ] Source variant ids are recorded.
- [ ] Combined directions name their contributing ancestors.
- [ ] The exploration board remains preserved.
- [ ] The promoted/final artifact is created separately from historical variants.

## G. Final test

The round passes if the user can truthfully say:

> I can see the alternatives, compare them, refer to a specific variant by id, and continue from any useful point without losing the previous work.
