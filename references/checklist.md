# Parallel Exploration Checklist

This is background documentation. The runtime skill is self-contained and must not block on locating this file.

## A. Divergence

- [ ] There are multiple sibling alternatives unless the user explicitly requested one.
- [ ] Default sibling count is 3; never exceed 5 without a strong reason.
- [ ] Each sibling represents a consequentially different design hypothesis.
- [ ] Alternatives are not merely color, typeface, radius, shadow, or spacing swaps.
- [ ] No sibling is visually framed as the recommended or winning option.

## B. Single-document canvas

- [ ] There is one primary exploration HTML document.
- [ ] Variants are rendered inline in that document, not as separate HTML files composed with iframes.
- [ ] The page opens directly into the comparative field; no tab/file/link hopping is required.
- [ ] Stable ids such as `1A`, `1B`, `1C` are visible.
- [ ] Siblings are spatially adjacent whenever practical.
- [ ] The canvas looks like a workspace, not a landing page, case study, or marketing presentation.

## C. Prototype fidelity

- [ ] Each direction is rendered far enough to judge the key interaction or product idea.
- [ ] Siblings use comparable viewport/device dimensions.
- [ ] Siblings use comparable content/data scenarios where practical.
- [ ] Fidelity differences do not unfairly bias comparison.

## D. History and lineage

- [ ] Existing historical variants remain visibly present and unchanged.
- [ ] No old variant id has been reused.
- [ ] New variants have explicit parent ids.
- [ ] New work is appended as a new round inside the same HTML document.
- [ ] A branch from an older variant remains valid even if it is not descended from the latest round.

## E. Runtime discipline

- [ ] Optional plugin references/templates were not treated as runtime prerequisites.
- [ ] No `brand-spec.md` was created without a real user-supplied brand/reference source.
- [ ] No PNG/screenshot export was required merely to finish the round.
- [ ] Direction/theme tooling failures did not become a debugging side quest.
- [ ] A vague smoke-test prompt produced a lightweight exploration rather than an oversized multi-file project.

## F. Convergence guard

Unless the user explicitly asked to choose, combine, finalize, promote, or move forward:

- [ ] No winner is declared.
- [ ] No final recommendation is written.
- [ ] No branch is deleted because it appears weaker.

If the user **did** explicitly request convergence:

- [ ] Source variant ids are recorded.
- [ ] Combined directions name their contributing ancestors.
- [ ] The exploration document remains preserved.

## G. Final test

The round passes if the user can truthfully say:

> I opened one design document, saw several real alternatives at once, and can continue into another round without losing the previous round.
