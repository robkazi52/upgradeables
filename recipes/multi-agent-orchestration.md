# Multi-Agent / Orchestration Recipe

R = required, A = automatically recommended, C = conditional, O = optional,
X = normally exclude. These are recipe defaults, not universal truths.

| Upgradeable | Class |
|---|:---:|
| `architect-orchestrator` | R |
| `scoped-loader` | R |
| `state-routing-bus` | R |
| `stateblock` | R |
| `state-snapshot` | R |
| `domain-mode-isolation` | R |
| `resonance` | A |
| `parallel-qms` | A |
| `multi-layer-consistency` | A |
| `external-state-automation` | C |



## Composition

Frame and lock the task, establish explicit state, load evidence and behavior
components, perform the task, then run applicable validators. Increase depth
with risk; remove scaffolding that has no active trigger.

## Tests

Test required activation, unnecessary-module exclusion, authority conflict,
unsupported evidence, long-context continuation where applicable, and a
strong-model configuration that preserves mandatory invariants.
