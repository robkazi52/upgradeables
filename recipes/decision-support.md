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
| `citation-fidelity` | C |
| `dynamic-depth-allocation` | C |
| `parallel-qms` | A |



## Composition

Frame and lock the task, establish explicit state, load evidence and behavior
components, perform the task, then run applicable validators. Increase depth
with risk; remove scaffolding that has no active trigger.

Use Citation Fidelity when a recommendation must cite source material. A
Compare-Contrast Behavior Gene may guide the side-by-side analysis, but it does
not replace decision controls. Parallel QMS may be implemented as sequential,
independent evidence, citation, and logic checks when real parallelism is absent.

## Output contract

Return decision criteria and method, a side-by-side evidence comparison, the
recommendation, claim-local citations when requested, material tradeoffs,
missing information, and uncertainty or sensitivity that could change the result.

## Tests

Test required activation, unnecessary-module exclusion, authority conflict,
unsupported evidence, long-context continuation where applicable, and a
strong-model configuration that preserves mandatory invariants.
