# Education / Explanation — Resolved Recipe

Generated discovery view. For normal execution, load the compact
[runtime recipe pack](../../runtime/recipes/education-explanation.md) instead of full packages.
See the [source recipe notes](../education-explanation.md) for composition and tests.

`R` stays required after selecting this recipe. `A`, `C`, and `O` require an
active trigger. `X` is excluded without explicit justification.

| Role | Component | Trigger summary | Requires |
|:---:|---|---|---|
| R | [Pedagogical Alignment Constraint (`pedagogical-alignment@1.1.0`)](../../upgradeables/output/pedagogical-alignment/UPGRADEABLE.md) | an audience or teaching level is known | — |
| A | [Minimum Sufficient Explanation (`explanation-minimality-scaffold@1.1.0`)](../../upgradeables/output/explanation-minimality-scaffold/UPGRADEABLE.md) | verbosity can obscure the answer | — |
| A | [Style-Alignment Module (`style-alignment@1.1.0`)](../../upgradeables/output/style-alignment/UPGRADEABLE.md) | a style or voice is specified | — |
| A | [Grounding / No-Invention (`grounding-no-invention@1.1.0`)](../../upgradeables/truth-grounding/grounding-no-invention/UPGRADEABLE.md) | work relies on documents, data, external facts, or consequential claims | — |
| A | [Micro-Scaffolding (`micro-scaffolding@1.1.0`)](../../upgradeables/foundation/micro-scaffolding/UPGRADEABLE.md) | multi-step or high-constraint work | — |
| R | [Task-Set Lock-In (`task-set-lock-in@1.1.0`)](../../upgradeables/state/task-set-lock-in/UPGRADEABLE.md) | multi-step work begins or scope changes | — |
| A | [Safe Rewrite Logic (`safe-rewrite@1.1.0`)](../../upgradeables/editing-repair/safe-rewrite/UPGRADEABLE.md) | paraphrasing, polishing, or format conversion | — |
| C | [Anti-Tunnel Vision (`anti-tunnel-vision@1.1.0`)](../../upgradeables/reasoning/anti-tunnel-vision/UPGRADEABLE.md) | premature fixation could hide credible alternatives | — |
| C | [Parallel Validation System (`parallel-qms@1.1.0`)](../../upgradeables/validation/parallel-qms/UPGRADEABLE.md) | a composed workflow needs structured quality evaluation | — |

Do not merge whole recipes. Add individual cross-cutting components only for
explicit requirements the primary recipe does not cover.
