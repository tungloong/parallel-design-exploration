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

`plugins/community/hallmark` is a richer design example. Its `SKILL.md` contains detailed design and implementation behavior while its Open Design manifest still requests only:

```json
["prompt:inject"]
```

The important lesson is that a community design plugin can encode substantial generation behavior in a portable skill contract and let Open Design's host scenario supply normal project execution and artifact-writing machinery.

### Humanize PPT

`plugins/community/humanize-ppt` represents the broader-capability lane. It requests:

```json
["prompt:inject", "fs:read", "fs:write", "bash"]
```

because its workflow explicitly needs plugin-level execution beyond prompt context. That is legitimate, but it crosses the community trust gate and therefore depends on a trusted install or source.

## Community trust model

The default Open Design community marketplace describes its entries as discoverable by default but restricted until the user installs and trusts them.

Direct GitHub and community installs should therefore assume the restricted capability floor unless a trusted source grants more.

For this plugin, the default distribution model is **restricted-safe**:

- request only `prompt:inject`;
- let the host's built-in `new-generation` scenario provide normal execution and artifact-writing behavior;
- keep the distinctive exploration protocol inside the portable `SKILL.md` contract.

This allows Parallel Design Exploration to launch as an Active Plugin without requiring elevated plugin capabilities simply to produce and update normal project artifacts.

## Why the manifest does not own a custom pipeline

A manifest-owned `od.pipeline` makes the plugin itself responsible for pipeline execution and causes Open Design to require pipeline capability. A restricted community or GitHub install can therefore be blocked before a run begins.

Parallel Design Exploration does not fundamentally require a second filesystem or shell runtime. Its core value is a design-state protocol:

```text
brief
  ↓
parallel rendered options
  ↓
visible comparison
  ↓
stable identities and preserved history
  ↓
user-directed continuation or convergence
```

The host agent already knows how to create and edit project artifacts. The plugin defines how exploration states are organized and maintained.

## Host planning and direction guidance

Open Design's normal `new-generation` path may provide planning or design-direction guidance before the skill runs.

Parallel Design Exploration uses relevant host guidance as context while maintaining several rendered siblings when the user is exploring alternatives. Candidate directions can seed different options without turning the planning stage into an automatic convergence point.

The portable behavior belongs in `SKILL.md` so the same interaction model can survive changes in the host's internal orchestration and remain understandable to other Agent Skills clients.

## UI and trust implication

Open Design's Plugins UI exposes trust control at the marketplace-source level. Plugin detail metadata displays trust and capability information, while the reviewed UI path does not depend on an individual installed-plugin capability-grant control.

The community-safe distribution therefore avoids requiring elevated capabilities for the core exploration experience. A future trusted distribution could introduce host-level enhancements without changing the portable options-canvas protocol.
