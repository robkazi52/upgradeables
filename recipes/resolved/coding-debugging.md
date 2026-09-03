# Coding / Debugging — Resolved Recipe

Generated discovery view. Evaluate triggers here, then open only retained packages.
See the [source recipe notes](../coding-debugging.md) for composition and tests.

`R` stays required after selecting this recipe. `A`, `C`, and `O` require an
active trigger. `X` is excluded without explicit justification.

| Role | Component | Trigger summary | Requires |
|:---:|---|---|---|
| R | [Task-Set Lock-In (`task-set-lock-in@1.0.0`)](../../upgradeables/state/task-set-lock-in/UPGRADEABLE.md) | multi-step work begins or scope changes | — |
| A | [StateBlock (`stateblock@1.0.0`)](../../upgradeables/state/stateblock/UPGRADEABLE.md) | work spans multiple steps or components | — |
| A | [Forethought / Checkpoints (`forethought-checkpoints@1.0.0`)](../../upgradeables/reasoning/forethought-checkpoints/UPGRADEABLE.md) | an action is costly, irreversible, or dependency-sensitive | — |
| A | [Dominant-Driver Isolation Scaffold (`dominant-driver-isolation-scaffold@1.0.0`)](../../upgradeables/reasoning/dominant-driver-isolation-scaffold/UPGRADEABLE.md) | many possible causes compete | — |
| A | [Anti-Tunnel Vision (`anti-tunnel-vision@1.0.0`)](../../upgradeables/reasoning/anti-tunnel-vision/UPGRADEABLE.md) | premature fixation is plausible | — |
| A | [Bidirectional Consistency (`bidirectional-consistency@1.0.0`)](../../upgradeables/validation/bidirectional-consistency/UPGRADEABLE.md) | causal, logical, quantitative, or evidence claims are central | — |
| R | [Invariance Stress Scaffold (`invariance-stress-scaffold@1.0.0`)](../../upgradeables/validation/invariance-stress-scaffold/UPGRADEABLE.md) | a patch or rewrite must preserve invariants | — |
| R | [Micro-Repair (`micro-repair@1.0.0`)](../../upgradeables/editing-repair/micro-repair/UPGRADEABLE.md) | a defect is localized | — |
| A | [CRISPR Editing (`crispr-edit@1.0.0`)](../../upgradeables/editing-repair/crispr-edit/UPGRADEABLE.md) | a change is small and local | — |
| C | [Surgery Editing (`surgery-edit@1.0.0`)](../../upgradeables/editing-repair/surgery-edit/UPGRADEABLE.md) | layers, Cores, or workflows require major replacement | — |
| A | [Structured Refinement Cycles (`structured-refinement@1.0.0`)](../../upgradeables/editing-repair/structured-refinement/UPGRADEABLE.md) | revision has multiple defect classes | — |
| A | [Bounded ExIt (`bounded-exit@1.0.0`)](../../upgradeables/reasoning/bounded-exit/UPGRADEABLE.md) | a draft needs iterative improvement | — |
| A | [Parallel Quality Management System (`parallel-qms@1.0.0`)](../../upgradeables/validation/parallel-qms/UPGRADEABLE.md) | a composed workflow needs structured quality evaluation | — |
| A | [Drift Suppression (`drift-suppression@1.0.0`)](../../upgradeables/drift-control/drift-suppression/UPGRADEABLE.md) | long, branching, or iterative work | — |

Do not merge whole recipes. Add individual cross-cutting components only for
explicit requirements the primary recipe does not cover.
