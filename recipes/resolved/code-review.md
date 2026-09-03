# Code / Pull Request Review — Resolved Recipe

Generated discovery view. For normal execution, load the compact
[runtime recipe pack](../../runtime/recipes/code-review.md) instead of full packages.
See the [source recipe notes](../code-review.md) for composition and tests.

`R` stays required after selecting this recipe. `A`, `C`, and `O` require an
active trigger. `X` is excluded without explicit justification.

| Role | Component | Trigger summary | Requires |
|:---:|---|---|---|
| R | [Task-Set Lock-In (`task-set-lock-in@1.1.0`)](../../upgradeables/state/task-set-lock-in/UPGRADEABLE.md) | multi-step work begins or scope changes | — |
| R | [Scoped Loader / Loader Sequencing (`scoped-loader@1.1.0`)](../../upgradeables/context-retrieval/scoped-loader/UPGRADEABLE.md) | a modular workflow has multiple available components | — |
| R | [Grounding / No-Invention (`grounding-no-invention@1.1.0`)](../../upgradeables/truth-grounding/grounding-no-invention/UPGRADEABLE.md) | work relies on documents, data, external facts, or consequential claims | — |
| C | [Canonical Task State (`stateblock@1.1.0`)](../../upgradeables/state/stateblock/UPGRADEABLE.md) | work spans multiple steps or components | — |
| A | [Forethought / Checkpoints (`forethought-checkpoints@1.1.0`)](../../upgradeables/reasoning/forethought-checkpoints/UPGRADEABLE.md) | an action is costly, irreversible, or dependency-sensitive | — |
| A | [Dominant-Driver Isolation Scaffold (`dominant-driver-isolation-scaffold@1.1.0`)](../../upgradeables/reasoning/dominant-driver-isolation-scaffold/UPGRADEABLE.md) | many plausible causes compete for priority | — |
| A | [Anti-Tunnel Vision (`anti-tunnel-vision@1.1.0`)](../../upgradeables/reasoning/anti-tunnel-vision/UPGRADEABLE.md) | premature fixation could hide credible alternatives | — |
| A | [Bidirectional Consistency (`bidirectional-consistency@1.1.0`)](../../upgradeables/validation/bidirectional-consistency/UPGRADEABLE.md) | causal, logical, quantitative, or evidence claims are central | — |
| C | [Protected-Constraint Robustness Test (`invariance-stress-scaffold@1.1.0`)](../../upgradeables/validation/invariance-stress-scaffold/UPGRADEABLE.md) | a patch or rewrite must preserve invariants | — |
| A | [Evidence-Confidence Gate (`epistemic-status-gating@1.1.0`)](../../upgradeables/truth-grounding/epistemic-status-gating/UPGRADEABLE.md) | claims of mixed certainty are present | — |
| C | [Critical Fact Verification (`critical-atomic-verification@1.1.0`)](../../upgradeables/validation/critical-atomic-verification/UPGRADEABLE.md) | small factual errors could change the outcome | — |
| C | [Citation Fidelity Gate (`citation-fidelity@1.1.0`)](../../upgradeables/validation/citation-fidelity/UPGRADEABLE.md) | output contains citations or source-attributed claims | — |
| A | [Parallel Validation System (`parallel-qms@1.1.0`)](../../upgradeables/validation/parallel-qms/UPGRADEABLE.md) | a composed workflow needs structured quality evaluation | — |
| A | [Drift Suppression (`drift-suppression@1.1.0`)](../../upgradeables/drift-control/drift-suppression/UPGRADEABLE.md) | long, branching, or iterative work | — |
| C | [Fail-Closed Abstention (`fail-closed-abstention@1.1.0`)](../../upgradeables/truth-grounding/fail-closed-abstention/UPGRADEABLE.md) | required evidence cannot be verified | — |

Do not merge whole recipes. Add individual cross-cutting components only for
explicit requirements the primary recipe does not cover.
