# Medical Evidence — Resolved Recipe

Generated discovery view. Evaluate triggers here, then open only retained packages.
See the [source recipe notes](../medical-evidence.md) for composition and tests.

`R` stays required after selecting this recipe. `A`, `C`, and `O` require an
active trigger. `X` is excluded without explicit justification.

| Role | Component | Trigger summary | Requires |
|:---:|---|---|---|
| R | [Task-Set Lock-In (`task-set-lock-in@1.0.0`)](../../upgradeables/state/task-set-lock-in/UPGRADEABLE.md) | multi-step work begins or scope changes | — |
| R | [Grounding / No-Invention (`grounding-no-invention@1.0.0`)](../../upgradeables/truth-grounding/grounding-no-invention/UPGRADEABLE.md) | work relies on documents, data, external facts, or consequential claims | — |
| R | [Risk-Tier Scaling (`risk-tier-scaling@1.0.0`)](../../upgradeables/meta-control/risk-tier-scaling/UPGRADEABLE.md) | task risk varies or must be classified | — |
| R | [Critical Atomic Verification (`critical-atomic-verification@1.0.0`)](../../upgradeables/validation/critical-atomic-verification/UPGRADEABLE.md) | small factual errors could change the outcome | — |
| R | [Truth Priority Hierarchy (`truth-priority-hierarchy@1.0.0`)](../../upgradeables/truth-grounding/truth-priority-hierarchy/UPGRADEABLE.md) | evidence classes or authorities conflict | — |
| C | [Citation Fidelity Gate (`citation-fidelity@1.0.0`)](../../upgradeables/validation/citation-fidelity/UPGRADEABLE.md) | output contains citations or source-attributed claims | — |
| R | [Fail-Closed Abstention (`fail-closed-abstention@1.0.0`)](../../upgradeables/truth-grounding/fail-closed-abstention/UPGRADEABLE.md) | required evidence cannot be verified | — |
| R | [Domain / Mode Isolation (`domain-mode-isolation@1.0.0`)](../../upgradeables/state/domain-mode-isolation/UPGRADEABLE.md) | multiple domains or semantic modes coexist | — |
| R | [Parallel Quality Management System (`parallel-qms@1.0.0`)](../../upgradeables/validation/parallel-qms/UPGRADEABLE.md) | a composed workflow needs structured quality evaluation | — |

Do not merge whole recipes. Add individual cross-cutting components only for
explicit requirements the primary recipe does not cover.
