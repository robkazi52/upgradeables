# Perception & Spatial Reasoning Recipe

Infer an unstated transformation from input/output examples, falsify competing
hypotheses, and apply the surviving rule with bounded execution checks.

## Task family

Grid puzzles, pattern completion, visual analogies, inductive rule inference, and
spatial transformations such as ARC-style tasks.

R = required, A = automatically recommended, C = conditional, O = optional,
X = normally exclude. These are recipe defaults, not universal truths.

| Upgradeable | Class | Rationale |
|---|:---:|---|
| `task-set-lock-in` | R | Lock a rule only after it explains every training pair. |
| `grounding-no-invention` | R | Derive transformations from observed cells and relations. |
| `anti-tunnel-vision` | R | Try to falsify the favored hypothesis with counterexamples. |
| `bounded-exit` | R | Bound hypothesis/revision cycles and report uncertainty. |
| `micro-scaffolding` | R | Hold the current rule, evidence, invariants, and local checks. |
| `bidirectional-consistency` | A | Check prediction forward and explanatory fit backward. |
| `forethought-checkpoints` | A | Verify dimensions, palette, and prerequisites before output. |
| `cot-structured-state-block` | A | Separate observations, hypotheses, tests, and committed state. |
| `decision-first-scaffold` | C | Compare multiple surviving rules when a decision is required. |
| `invariance-stress-scaffold` | C | Verify cells or relations expected to remain unchanged. |
| `counterfactual-integrity` | C | Keep rejected/hypothetical rules out of committed state. |
| `multiverse-reasoning` | O | Generate two or three materially different candidate rules. |
| `cognitive-governor` | O | Increase effort only when puzzle complexity warrants it. |
| `coherence-heartbeat` | X | Usually excessive for one bounded puzzle. |
| `meta-supervisor` | X | Suite-level supervision normally costs more than it adds here. |

## Composition

Observe without committing, generate only as many candidates as the examples
justify, attempt to falsify each candidate across every training pair, lock one
rule, then construct and verify the output locally. `X` components remain excluded
unless a task-specific trigger overrides the recipe.

## Evidence basis

The mapping is provisional and was motivated by an author-reported ARC session.
The supplied totals are not fully reconciled and the raw runs are not archived;
see [`evidence/arc-agi-benchmarks.md`](../evidence/arc-agi-benchmarks.md). The recipe
does not claim measured superiority.

## Tests

Test rule activation on multiple training pairs, insufficient-evidence behavior,
ambiguous candidates, bounded revision failure, preservation of invariants, output
dimensions, authority conflicts, and exclusion of unnecessary meta machinery.
