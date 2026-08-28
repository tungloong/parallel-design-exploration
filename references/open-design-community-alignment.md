# Open Design community alignment

This plugin is intentionally shaped to behave like a community-installable Open Design scenario rather than a first-party bundled plugin.

## Reference patterns reviewed

### Community Registry Starter

Open Design's `plugins/community/registry-starter` is a useful baseline for a standalone community scenario:

- `od.kind: scenario`
- `od.taskKind: new-generation`
- `od.mode: prototype`
- only `prompt:inject` is requested
- no custom `od.pipeline`

This demonstrates that a community plugin can be a project/run entry point without owning elevated execution capabilities.

### Hallmark

`plugins/community/hallmark` is a richer design example. Its `SKILL.md` contains detailed instructions for greenfield generation, audits, redesigns, responsive verification, and implementation behavior, while its Open Design manifest still requests only:

```json
["prompt:inject"]
```

The important lesson is that a community design plugin can encode substantial generation behavior in its portable skill contract and let Open Design's host scenario supply normal project execution and artifact-writing machinery.

### Humanize PPT

`plugins/community/humanize-ppt` is the opposite lane. It requests:

```json
["prompt:inject", "fs:read", "fs:write", "bash"]
```

because its workflow explicitly needs broader plugin-level execution. This is legitimate, but it crosses the community trust gate and therefore requires a trusted install/source before those capabilities can be granted.

## Community trust model

The default Open Design community marketplace describes its entries as discoverable by default but restricted until the user installs and trusts them.

Direct GitHub and community installs therefore should assume the restricted capability floor unless a trusted source grants more.

For this plugin, the default distribution goal is **restricted-safe**:

- request only `prompt:inject`;
- do not declare a custom `od.pipeline` in the community-safe manifest;
- let the host's built-in `new-generation` scenario provide its normal execution pipeline;
- keep the distinctive exploration behavior inside `SKILL.md`, references, templates, and examples.

This avoids requiring a capability-grant step just to launch Parallel Design Exploration as an Active Plugin.

## Why no custom pipeline in v0.3

A manifest-owned `od.pipeline` makes the plugin itself responsible for pipeline execution and causes Open Design to require pipeline capability. A direct GitHub install is restricted by default, so this can block activation before a run begins.

Parallel Design Exploration does not fundamentally need plugin-level filesystem or shell privileges. Its core value is an orchestration/design-method contract:

```text
brief
  ↓
diverge
  ↓
1A   1B   1C
  ↓
compare
  ↓
append descendants without overwriting history
```

The host agent already knows how to create and edit project artifacts. The plugin's job is to force the *shape of the exploration*, not to acquire a second filesystem runtime.

## Handling the host direction-picker

When Open Design supplies its normal `new-generation` pipeline, it may expose a direction-picking planning stage.

When this skill is active, that stage must not become a convergence gate. The agent should use candidate directions as planning seeds if useful, but it must continue through generation and render all requested siblings before asking the user to choose.

In other words:

```text
host default:
directions → pick one → generate

Parallel Design Exploration interpretation:
directions → keep several → generate all siblings → compare → user decides when to converge
```

The behavioral override belongs in `SKILL.md`, because that remains portable across Open Design and other Agent Skills clients.

## Current UI implication

Open Design's current Plugins UI exposes trust control for **marketplace sources**. Plugin detail metadata displays trust/capability information, but the reviewed UI path does not expose an individual installed-plugin capability-grant control.

For that reason, the portable default should not depend on a per-plugin grant UI existing.

If a future trusted distribution wants a manifest-owned custom pipeline, it can be introduced as an advanced/trusted lane without changing the portable `SKILL.md` contract.
