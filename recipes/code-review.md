# Code / Pull Request Review Recipe

R = required, A = automatically recommended but trigger-gated, C = conditional,
O = optional, and X = normally excluded.

| Upgradeable | Class |
|---|:---:|
| `task-set-lock-in` | R |
| `scoped-loader` | R |
| `grounding-no-invention` | R |
| `stateblock` | C |
| `forethought-checkpoints` | A |
| `dominant-driver-isolation-scaffold` | A |
| `anti-tunnel-vision` | A |
| `bidirectional-consistency` | A |
| `invariance-stress-scaffold` | R |
| `epistemic-status-gating` | A |
| `critical-atomic-verification` | C |
| `citation-fidelity` | C |
| `parallel-qms` | A |
| `drift-suppression` | A |
| `fail-closed-abstention` | C |

## Composition

Lock the requested review scope and expected output. Inspect the diff, relevant
callers, contracts, tests, and configuration without assuming unseen behavior.
Look for correctness defects, regressions, unsafe assumptions, missing tests, and
scope drift. This is a review-only recipe: do not activate editing components
unless the user separately asks for fixes.

Parallel QMS means independent evidence, logic, and regression checks. Run those
checks sequentially when the host cannot execute real parallel workers.

## Output contract

Lead with actionable findings ordered by severity. For each finding, identify the
affected file/location, evidence, impact, and a bounded repair direction. Separate
confirmed defects from questions and low-confidence risks. State when no material
finding is supported and summarize remaining test or context gaps.

## Tests

Test a confirmed regression, a false-positive lure, an out-of-scope file, an
unsupported security claim, a clean change, and a review-only request that must
not silently edit code.
