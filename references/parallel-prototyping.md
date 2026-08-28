# Reference: Parallel Prototyping

This skill treats parallel prototyping as its primary design-method foundation.

## 1. Dow et al. — Parallel prototyping vs serial iteration

**Steven P. Dow, Alana Glassco, Jonathan Kass, Melissa Schwarz, Daniel L. Schwartz, Scott R. Klemmer.**

*Parallel Prototyping Leads to Better Design Results, More Divergence, and Increased Self-Efficacy.* ACM Transactions on Computer-Human Interaction, 17(4), Article 18, 2010.

DOI: https://doi.org/10.1145/1879831.1879836

ACM: https://dl.acm.org/doi/10.1145/1879831.1879836

### What the study compared

The study contrasted two iteration structures:

```text
SERIAL
prototype → critique → prototype → critique → prototype

PARALLEL
prototype A ─┐
prototype B ─┼→ critique/comparison → later refinement
prototype C ─┘
```

The authors frame serial iteration as vulnerable to **fixation**: continuously refining one option without sufficiently considering alternatives.

In the reported experiment, participants in the parallel condition created multiple prototypes before feedback. The paper reports that parallel work produced more diverse alternatives and stronger final outcomes by the study's expert-rating and click-through measures, while participants also reported a larger increase in task-specific confidence.

### Implications for this skill

The relevant lesson is not "always generate exactly three designs." It is structural:

- keep multiple design hypotheses alive long enough to compare them;
- delay commitment until alternatives are concrete;
- solicit feedback across alternatives rather than only on the current answer;
- avoid treating every follow-up as an instruction to polish one incumbent design;
- preserve diversity between siblings instead of producing cosmetic variants.

This is why the skill forbids an automatic winner during an exploration round.

## 2. Hartmann et al. — Design as Exploration / Juxtapose

**Björn Hartmann, Loren Yu, Abel Allison, Yeonsoo Yang, Scott R. Klemmer.**

*Design As Exploration: Creating Interface Alternatives through Parallel Authoring and Runtime Tuning.* UIST 2008.

Stanford HCI publication page: https://hci.stanford.edu/publications/paper.php?id=16

Project page: https://hci.stanford.edu/research/juxtapose/

### Why it matters here

Juxtapose is especially relevant because it treats **multiple interface alternatives as first-class authoring objects**, not just sketches that disappear before implementation.

Its core premise is that multiple prototypes support:

- comparative reasoning;
- grounded team discussion;
- situated exploration;
- faster surveying of alternatives.

It also identifies a tooling problem that remains recognizable today: authoring tools often center a single current artifact even though exploration benefits from multiple alternatives.

### Implications for this skill

Our design object should therefore be closer to:

```text
Exploration
├── Alternative A
├── Alternative B
└── Alternative C
```

than:

```text
CurrentArtifact
└── latest.html
```

The board and manifest exist to make alternatives explicit and addressable.

## 3. Divergence before convergence

Parallel prototyping belongs to a broader family of design practices that separate **divergence** from **convergence**.

Operationally, this skill interprets that as two different modes:

### Explore mode

- increase meaningful alternatives;
- keep siblings visible;
- compare trade-offs;
- branch from promising ideas;
- avoid declaring a winner.

### Converge mode

- select or combine specific variants;
- preserve provenance of the selected ideas;
- create a promoted design artifact;
- retain the exploration record instead of deleting it.

The mode transition should be explicit. A follow-up comment such as "the keyboard occupies too much space" is normally exploration feedback, not permission to erase Round 1 and silently replace it.

## 4. Comparison requires comparable representations

Parallel alternatives are only useful when comparison is fair.

For UI prototypes, siblings in the same round should therefore use, whenever practical:

- the same device/viewport dimensions;
- the same content/data scenario;
- similar prototype fidelity;
- the same key user task;
- consistent zoom on the board.

Otherwise differences in fidelity or framing can dominate differences in design hypothesis.

## 5. What counts as meaningful divergence

Strong sibling differences often concern:

- information architecture;
- primary interaction model;
- navigation model;
- hierarchy;
- sequence and disclosure;
- product metaphor;
- spatial organization;
- density;
- direct manipulation vs command/action models;
- system-native vs custom interaction.

Weak divergence includes a set of alternatives where the only changes are:

- color palette;
- typeface;
- corner radius;
- shadows;
- minor spacing;
- decorative treatment.

Visual style can be a valid exploration dimension, but style-only alternatives should be intentional and clearly labeled as such.

## 6. Design rule derived from the references

> Generate alternatives far enough to compare the design, not merely the description of the design.

That rule is the core distinction between this skill and a conventional direction picker.
