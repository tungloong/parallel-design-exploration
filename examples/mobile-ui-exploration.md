# Example: Mobile Search UI Exploration

This example shows the intended **shape of a session**, not a prescribed visual style.

## User brief

```text
Explore alternative interaction models for an iOS quick-search app.

The user arrives with a specific search intent and should be able to execute the search
without getting pulled into an infinite content feed. I want structurally different
ideas, not three visual themes. Keep the alternatives side by side and do not choose a
winner yet.
```

## Expected Round 1 planning

The agent might identify three distinct hypotheses:

```text
1A — Quiet Canvas
Hypothesis: remove nearly all chrome and let search/result content dominate.

1B — Thumb Search Dock
Hypothesis: make the primary search affordance persist near the thumb zone and let
results expand above it.

1C — Command Results
Hypothesis: treat results as immediately actionable commands rather than feed-like cards.
```

The important point is that these are **hypotheses to render**, not direction cards to show before asking the user to pick one.

## Expected files after Round 1

```text
board.html
exploration.json
round-1/
├── 1A.html
├── 1B.html
└── 1C.html
```

## Example `exploration.json`

```json
{
  "schemaVersion": "0.1",
  "title": "Quick Search — interaction exploration",
  "brief": "Explore structurally different interaction models for a focused iOS search app.",
  "defaults": {
    "viewport": {
      "width": 390,
      "height": 844,
      "scale": 0.72
    }
  },
  "rounds": [
    {
      "number": 1,
      "label": "Round 1 — interaction model",
      "variants": [
        {
          "id": "1A",
          "parent": null,
          "name": "Quiet Canvas",
          "file": "round-1/1A.html",
          "hypothesis": "A nearly chrome-free surface will make intent and completion feel immediate.",
          "rationale": "Search occupies the visual center; results appear without introducing feed-like navigation.",
          "gains": ["low distraction", "clear intent"],
          "sacrifices": ["fewer persistent controls"]
        },
        {
          "id": "1B",
          "parent": null,
          "name": "Thumb Search Dock",
          "file": "round-1/1B.html",
          "hypothesis": "A persistent bottom search dock will support fast one-handed repeated searches.",
          "rationale": "Input stays in reach while results use the space above it.",
          "gains": ["one-handed reachability", "stable search affordance"],
          "sacrifices": ["less vertical result space"]
        },
        {
          "id": "1C",
          "parent": null,
          "name": "Command Results",
          "file": "round-1/1C.html",
          "hypothesis": "Results should emphasize the next action rather than encourage browsing.",
          "rationale": "Each result exposes a compact action path designed to finish the task and leave.",
          "gains": ["fast completion", "strong anti-feed posture"],
          "sacrifices": ["less room for exploratory content"]
        }
      ]
    }
  ]
}
```

## Example feedback

```text
1B feels closest, but the keyboard will actually occupy the lower part of the screen.
Keep the dock idea and show me three different ways to handle results when the keyboard
is already present. Do not delete Round 1.
```

## Correct Round 2 behavior

Do **not** edit `round-1/1B.html` in place.

Create three descendants:

```text
1B — Thumb Search Dock
├── 2A — Compressed result stack
├── 2B — Result peek + expand
└── 2C — Single-result command focus
```

Files become:

```text
board.html
exploration.json
round-1/
├── 1A.html
├── 1B.html
└── 1C.html
round-2/
├── 2A.html
├── 2B.html
└── 2C.html
```

And the manifest appends:

```json
{
  "number": 2,
  "label": "Round 2 — keyboard-aware result strategies",
  "feedback": "Keep 1B's dock model; explore result handling with the keyboard already present.",
  "variants": [
    {
      "id": "2A",
      "parent": "1B",
      "name": "Compressed Result Stack",
      "file": "round-2/2A.html",
      "hypothesis": "Compact stacking can preserve multiple visible results above the keyboard."
    },
    {
      "id": "2B",
      "parent": "1B",
      "name": "Result Peek + Expand",
      "file": "round-2/2B.html",
      "hypothesis": "A small result preview can preserve context while one result expands on demand."
    },
    {
      "id": "2C",
      "parent": "1B",
      "name": "Single-result Command Focus",
      "file": "round-2/2C.html",
      "hypothesis": "Showing the strongest actionable result first can minimize browsing and vertical pressure."
    }
  ]
}
```

## What the board should communicate

At this point the user should be able to see:

```text
ROUND 1
1A        1B        1C

ROUND 2
          ├─ 2A
          ├─ 2B
          └─ 2C
```

The user can now say things like:

- "Go back to 1A and branch a more system-native version."
- "Combine 1C's action treatment with 2B's result expansion."
- "2A is strongest; now converge on that direction."

Those statements are only easy when prior design states remain stable, visible, and addressable.
