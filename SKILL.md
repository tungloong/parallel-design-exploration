---
name: parallel-design-exploration
description: |
  Explore a design problem through multiple fully rendered sibling variants in one persistent
  design document. Keep prior rounds visibly present, append new rounds instead of overwriting,
  and converge only when the user asks.
license: MIT
metadata:
  author: tungloong
  version: "0.4.0"
triggers:
  - "parallel design exploration"
  - "parallel prototyping"
  - "design alternatives"
  - "design variations"
  - "explore multiple directions"
  - "show multiple directions side by side"
  - "diverge before converge"
od:
  mode: prototype
  surface: web
  platform: desktop
  scenario: design-exploration
---

# Parallel Design Exploration

Create a **persistent design exploration document**, not a presentation page and not a collection of separate prototype files.

The desired interaction model is a design studio wall / large canvas: alternatives from the same round are spatially adjacent, old rounds remain visible, and later feedback grows the same document instead of replacing what came before.

## 0. This skill is self-contained

Do not search the Open Design installation directory for this skill's `references/`, `templates/`, or checklist before starting. Those files are background documentation for humans and plugin development; they are **not runtime prerequisites**.

Do not block generation because an optional plugin asset cannot be located.

The hard runtime contract is fully contained in this `SKILL.md`.

## 1. One persistent artifact — hard requirement

For normal exploration, create **one user-facing HTML artifact** and keep editing that same file across turns.

Preferred semantic name:

```text
design-exploration.html
```

A brief-specific semantic name such as `search-screen-exploration.html` is also fine. Once created, preserve that filename on follow-up turns.

### Do not create this normal-mode structure

```text
board.html
exploration.json
round-1/1A.html
round-1/1B.html
round-1/1C.html
```

That is explicitly **not** the desired experience.

Do not use iframes to compose sibling variants from separate files. The alternatives must be rendered **inline in the same HTML document** so the page itself is the design space.

Do not create `brand-spec.md`, `exploration.json`, PNG exports, or per-variant HTML files unless the user explicitly asks for them or a real supplied brand/reference source makes a brand-spec necessary.

## 2. Document grammar

Use a simple additive DOM structure. Exact class names may vary, but the information model must remain obvious:

```html
<main class="exploration-canvas">
  <section class="round" data-round="1">
    <header>Round 1</header>

    <div class="variants">
      <article class="variant" data-variant="1A" data-parent="baseline">
        <div class="variant-label">1A · Direction name</div>
        <div class="prototype">…complete inline prototype…</div>
        <div class="rationale">…short rationale…</div>
      </article>

      <article class="variant" data-variant="1B" data-parent="baseline">…</article>
      <article class="variant" data-variant="1C" data-parent="baseline">…</article>
    </div>
  </section>
</main>
```

Every variant's interactive DOM and JS should be scoped to that variant. Do not build a launcher that links out to separate designs.

The page must open directly into the comparative field. Do not make the user click cards, tabs, links, or files to see the alternatives.

## 3. First round: diverge before converge

Unless the user requests another count, generate **3 materially different siblings**:

```text
1A    1B    1C
```

They should differ in consequential design hypotheses such as:

- information architecture;
- primary interaction model;
- navigation model;
- spatial organization;
- density/disclosure strategy;
- product metaphor;
- platform-native vs custom interaction;
- visual language, when the brief is explicitly exploring visual directions.

A color/font/radius swap alone is not a distinct direction.

Each sibling should be rendered far enough that the user can compare the design itself, not merely read a description of it.

Each sibling needs only concise supporting text:

- stable id and short name;
- one-line hypothesis or rationale;
- optional gain / sacrifice note when it helps comparison.

Do not rank siblings. Do not add `recommended`, `best`, `continue with this`, winner ribbons, or a recommendation section.

## 4. Canvas is a substrate, not the design

The exploration document's own chrome must be neutral and quiet.

Do not turn the document into:

- a landing page;
- a case study;
- a polished editorial article;
- a marketing presentation;
- a hero + sections + CTA composition.

Avoid decorative hero copy, sticky marketing nav, giant titles, promotional CTAs, alternating showcase sections, decorative narrative, or conclusion blocks.

Prefer:

```text
Round 1

1A                  1B                  1C
[prototype]         [prototype]         [prototype]
short note          short note          short note
```

Keep siblings in the same visual field whenever practical. Use comparable viewport size and content so the comparison is fair.

## 5. Follow-up turns are additive

When the user gives feedback, **edit the same HTML file**.

Never replace Round 1 with the new result.

Append a new round below or beside the existing one:

```text
ROUND 1
1A        1B        1C

ROUND 2
2A        2B        2C
```

Every new variant has an explicit parent, for example:

```text
2A ← 1B
2B ← 1B
2C ← 1C
```

If the user says "keep exploring 1B", several Round 2 siblings may all branch from `1B`.

Historical variant DOM is read-only once a later round exists. Do not silently clean up, restyle, or repair old variants. If a repair is essential, create a descendant and label it as such.

The exploration document grows; previous work does not disappear.

## 6. Open Design host direction handling

Open Design's host may resolve or lock a visual direction before this skill body runs. Do not let that host-level direction collapse the exploration into one design answer.

If the host requires a direction/theme selection:

- treat it as a neutral **canvas/base fallback**, not as the conceptual answer;
- do not make all siblings structurally identical because of it;
- variant-local CSS variables and component rules may differ when that is necessary to express the design hypothesis;
- never ask the user to pick one direction before rendering the siblings;
- if a direction lookup/tool fails, do not debug it beyond one attempt—continue with the exploration.

Do not proactively call `tools directions` merely because this skill discusses directions. If the host already selected a direction, proceed.

## 7. Scope proportionality

Match effort to the brief.

For a vague smoke-test prompt such as "随便画", "test this", or "draw something":

- choose a tiny, clearly fictional UI problem;
- create three small but visibly different inline sketches;
- keep the artifact lightweight;
- do not invent a large product strategy, brand system, data model, or multi-file project;
- do not spend many minutes on tooling diagnostics or elaborate QA.

For a real product brief, increase fidelity as needed.

## 8. Do not turn QA into a side quest

The live HTML artifact is the deliverable.

Do not require a PNG/screenshot export to declare success. If Open Design's normal preview works, use it. If image export fails, note it only if relevant and move on; do not spend the run debugging export infrastructure.

Do not run broad shell/XML/browser validation suites unless the user asks. Avoid `xmllint` on HTML containing JavaScript templates. A concise syntax/structure check is enough for a normal exploration round.

## 9. Minimal completion checklist

Before finishing, verify mentally or with lightweight inspection:

- [ ] Exactly one primary exploration HTML document exists for this exploration.
- [ ] Siblings are inline and simultaneously visible; no iframe/file hopping is required.
- [ ] Default first round has 3 materially different siblings unless the user asked otherwise.
- [ ] Visible ids such as `1A`, `1B`, `1C` exist.
- [ ] The board is neutral, not a presentation page.
- [ ] No winner or recommendation appears unless the user asked to converge.
- [ ] On follow-up turns, earlier rounds remain visible and unchanged.
- [ ] New variants show lineage to their parent.
- [ ] No optional plugin-resource lookup or export failure blocked delivery.

## 10. Convergence

Converge only when the user explicitly asks to choose, combine, finalize, promote, or proceed with a direction.

When converging:

- keep the exploration document intact;
- name the source variants used in the decision;
- if combining ideas, say which parts came from which variants;
- create/promote a final artifact separately if the user wants one.

The target user experience is:

> I open one design document, see several real alternatives at once, give feedback, and the same document grows with the next generation while the previous generation remains visible.
