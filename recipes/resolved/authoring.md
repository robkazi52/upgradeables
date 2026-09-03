# Authoring — Resolved Recipe

Generated discovery view. Evaluate triggers here, then open only retained packages.
See the [source recipe notes](../authoring.md) for composition and tests.

`R` stays required after selecting this recipe. `A`, `C`, and `O` require an
active trigger. `X` is excluded without explicit justification.

| Role | Component | Trigger summary | Requires |
|:---:|---|---|---|
| R | [Task-Set Lock-In (`task-set-lock-in@1.1.0`)](../../upgradeables/state/task-set-lock-in/UPGRADEABLE.md) | multi-step work begins or scope changes | — |
| C | [Grounding / No-Invention (`grounding-no-invention@1.1.0`)](../../upgradeables/truth-grounding/grounding-no-invention/UPGRADEABLE.md) | work relies on documents, data, external facts, or consequential claims | — |
| A | [Style-Alignment Module (`style-alignment@1.1.0`)](../../upgradeables/output/style-alignment/UPGRADEABLE.md) | a style or voice is specified | — |
| C | [Pedagogical Alignment Constraint (`pedagogical-alignment@1.1.0`)](../../upgradeables/output/pedagogical-alignment/UPGRADEABLE.md) | an audience or teaching level is known | — |
| R | [Safe Rewrite Logic (`safe-rewrite@1.1.0`)](../../upgradeables/editing-repair/safe-rewrite/UPGRADEABLE.md) | paraphrasing, polishing, or format conversion | — |
| C | [Citation Fidelity Gate (`citation-fidelity@1.1.0`)](../../upgradeables/validation/citation-fidelity/UPGRADEABLE.md) | output contains citations or source-attributed claims | — |
| R | [Placeholder Suppression (`placeholder-suppression@1.1.0`)](../../upgradeables/output/placeholder-suppression/UPGRADEABLE.md) | templates or staged artifacts are finalized | — |
| A | [Micro-Repair (`micro-repair@1.1.0`)](../../upgradeables/editing-repair/micro-repair/UPGRADEABLE.md) | Activate when the task requires a defect is localized. | — |
| A | [Parallel Quality Management System (`parallel-qms@1.1.0`)](../../upgradeables/validation/parallel-qms/UPGRADEABLE.md) | a composed workflow needs structured quality evaluation | — |

Do not merge whole recipes. Add individual cross-cutting components only for
explicit requirements the primary recipe does not cover.
