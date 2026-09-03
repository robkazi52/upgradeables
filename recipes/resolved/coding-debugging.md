# Coding / Debugging — Resolved Recipe

Generated discovery view. For normal execution, load the compact
[runtime recipe pack](../../runtime/recipes/coding-debugging.md) instead of full packages.
See the [source recipe notes](../coding-debugging.md) for composition and tests.

`R` stays required after selecting this recipe. `A`, `C`, and `O` require an
active trigger. `X` is excluded without explicit justification.

| Role | Component | Trigger summary | Requires |
|:---:|---|---|---|
| R | [Task-Set Lock-In (`task-set-lock-in@1.1.0`)](../../upgradeables/state/task-set-lock-in/UPGRADEABLE.md) | multi-step work begins or scope changes | — |
| A | [Canonical Task State (`stateblock@1.1.0`)](../../upgradeables/state/stateblock/UPGRADEABLE.md) | work spans multiple steps or components | — |
| A | [Forethought / Checkpoints (`forethought-checkpoints@1.1.0`)](../../upgradeables/reasoning/forethought-checkpoints/UPGRADEABLE.md) | an action is costly, irreversible, or dependency-sensitive | — |
| A | [Dominant-Driver Isolation Scaffold (`dominant-driver-isolation-scaffold@1.1.0`)](../../upgradeables/reasoning/dominant-driver-isolation-scaffold/UPGRADEABLE.md) | many plausible causes compete for priority | — |
| A | [Anti-Tunnel Vision (`anti-tunnel-vision@1.1.0`)](../../upgradeables/reasoning/anti-tunnel-vision/UPGRADEABLE.md) | premature fixation could hide credible alternatives | — |
| A | [Bidirectional Consistency (`bidirectional-consistency@1.1.0`)](../../upgradeables/validation/bidirectional-consistency/UPGRADEABLE.md) | causal, logical, quantitative, or evidence claims are central | — |
| R | [Protected-Constraint Robustness Test (`invariance-stress-scaffold@1.1.0`)](../../upgradeables/validation/invariance-stress-scaffold/UPGRADEABLE.md) | a patch or rewrite must preserve invariants | — |
| R | [Minimal Local Correction (`micro-repair@1.1.0`)](../../upgradeables/editing-repair/micro-repair/UPGRADEABLE.md) | a specific defect has been localized | — |
| A | [Precision Local System Edit (`crispr-edit@1.1.0`)](../../upgradeables/editing-repair/crispr-edit/UPGRADEABLE.md) | a change is small and local | — |
| C | [Structural System Edit (`surgery-edit@1.1.0`)](../../upgradeables/editing-repair/surgery-edit/UPGRADEABLE.md) | layers, Cores, or workflows require major replacement | — |
| A | [Structured Refinement Cycles (`structured-refinement@1.1.0`)](../../upgradeables/editing-repair/structured-refinement/UPGRADEABLE.md) | revision has multiple defect classes | — |
| A | [Bounded Iteration Stop Rule (`bounded-exit@1.1.0`)](../../upgradeables/reasoning/bounded-exit/UPGRADEABLE.md) | a draft needs iterative improvement | — |
| A | [Parallel Validation System (`parallel-qms@1.1.0`)](../../upgradeables/validation/parallel-qms/UPGRADEABLE.md) | a composed workflow needs structured quality evaluation | — |
| A | [Drift Suppression (`drift-suppression@1.1.0`)](../../upgradeables/drift-control/drift-suppression/UPGRADEABLE.md) | long, branching, or iterative work | — |

Do not merge whole recipes. Add individual cross-cutting components only for
explicit requirements the primary recipe does not cover.
