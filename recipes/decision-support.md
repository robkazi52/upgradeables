# Decision Support Recipe

R = required, A = automatically recommended, C = conditional, O = optional,
X = normally exclude. These are recipe defaults, not universal truths.

| Upgradeable | Class |
|---|:---:|
| `task-set-lock-in` | R |
| `decision-first-scaffold` | R |
| `grounding-no-invention` | R |
| `risk-tier-scaling` | A |
| `anti-tunnel-vision` | A |
| `bidirectional-consistency` | A |
| `truth-priority-hierarchy` | A |
| `dynamic-depth-allocation` | C |
| `parallel-qms` | A |



## Composition

Frame and lock the task, establish explicit state, load evidence and behavior
components, perform the task, then run applicable validators. Increase depth
with risk; remove scaffolding that has no active trigger.

## Tests

Test required activation, unnecessary-module exclusion, authority conflict,
unsupported evidence, long-context continuation where applicable, and a
strong-model configuration that preserves mandatory invariants.
