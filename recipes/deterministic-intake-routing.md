# Deterministic Intake / Routing Recipe

R = required, A = automatically recommended, C = conditional, O = optional,
X = normally exclude. These are recipe defaults, not universal truths.

| Upgradeable | Class |
|---|:---:|
| `task-set-lock-in` | R |
| `clarification-gateway` | A |
| `grounding-no-invention` | R |
| `scoped-loader` | R |
| `domain-mode-isolation` | R |
| `stateblock` | R |
| `structured-state-projection` | A |
| `authority-anchor-enforcement` | A |
| `external-state-automation` | C |
| `authenticity-anti-evasion` | R |

## Recovered Procedure

1. Classify the task and required output without drafting it.
2. Extract required inputs field by field; mark missing values `Not documented`.
3. Emit an explicit routing object with only recovered/authorized fields.
4. Use that object to scoped-load the selected task/domain OS, blueprint, and permitted references.
5. Run the drafting/execution stage separately, then validate.

Routing to a source folder does not establish that its content applies. Intake never imports another domain's rules or performs the downstream task.

## Composition

Frame and lock the task, establish explicit state, load evidence and behavior
components, perform the task, then run applicable validators. Increase depth
with risk; remove scaffolding that has no active trigger.

## Tests

Test required activation, unnecessary-module exclusion, authority conflict,
unsupported evidence, long-context continuation where applicable, and a
strong-model configuration that preserves mandatory invariants.
