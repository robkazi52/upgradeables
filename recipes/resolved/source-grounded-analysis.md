# Source-Grounded Analysis — Resolved Recipe

Generated discovery view. For normal execution, load the compact
[runtime recipe pack](../../runtime/recipes/source-grounded-analysis.md) instead of full packages.
See the [source recipe notes](../source-grounded-analysis.md) for composition and tests.

`R` stays required after selecting this recipe. `A`, `C`, and `O` require an
active trigger. `X` is excluded without explicit justification.

| Role | Component | Trigger summary | Requires |
|:---:|---|---|---|
| R | [Task-Set Lock-In (`task-set-lock-in@1.1.0`)](../../upgradeables/state/task-set-lock-in/UPGRADEABLE.md) | multi-step work begins or scope changes | — |
| R | [Mode Lock-In (`mode-lock-in@1.1.0`)](../../upgradeables/state/mode-lock-in/UPGRADEABLE.md) | a task can drift between modes | — |
| R | [Grounding / No-Invention (`grounding-no-invention@1.1.0`)](../../upgradeables/truth-grounding/grounding-no-invention/UPGRADEABLE.md) | work relies on documents, data, external facts, or consequential claims | — |
| A | [Safe Rewrite Logic (`safe-rewrite@1.1.0`)](../../upgradeables/editing-repair/safe-rewrite/UPGRADEABLE.md) | paraphrasing, polishing, or format conversion | — |
| R | [Citation Fidelity Gate (`citation-fidelity@1.1.0`)](../../upgradeables/validation/citation-fidelity/UPGRADEABLE.md) | output contains citations or source-attributed claims | — |
| A | [Immutable Content Zones (`zero-drift-zones@1.1.0`)](../../upgradeables/drift-control/zero-drift-zones/UPGRADEABLE.md) | content contains fidelity-locked atoms | — |
| A | [Bounded Change Rules (`controlled-drift-corridors@1.1.0`)](../../upgradeables/drift-control/controlled-drift-corridors/UPGRADEABLE.md) | synthesis or creativity must coexist with fidelity | — |
| A | [Counterfactual Integrity Gate (`counterfactual-integrity@1.1.0`)](../../upgradeables/truth-grounding/counterfactual-integrity/UPGRADEABLE.md) | counterfactual or hypothetical reasoning is used | — |
| A | [Minimal Local Correction (`micro-repair@1.1.0`)](../../upgradeables/editing-repair/micro-repair/UPGRADEABLE.md) | a specific defect has been localized | — |
| A | [Placeholder Suppression (`placeholder-suppression@1.1.0`)](../../upgradeables/output/placeholder-suppression/UPGRADEABLE.md) | templates or staged artifacts are finalized | — |
| A | [Parallel Validation System (`parallel-qms@1.1.0`)](../../upgradeables/validation/parallel-qms/UPGRADEABLE.md) | a composed workflow needs structured quality evaluation | — |

Do not merge whole recipes. Add individual cross-cutting components only for
explicit requirements the primary recipe does not cover.
