# High-Stakes Reasoning — Resolved Recipe

Generated discovery view. For normal execution, load the compact
[runtime recipe pack](../../runtime/recipes/high-stakes-reasoning.md) instead of full packages.
See the [source recipe notes](../high-stakes-reasoning.md) for composition and tests.

`R` stays required after selecting this recipe. `A`, `C`, and `O` require an
active trigger. `X` is excluded without explicit justification.

| Role | Component | Trigger summary | Requires |
|:---:|---|---|---|
| R | [Grounding / No-Invention (`grounding-no-invention@1.1.0`)](../../upgradeables/truth-grounding/grounding-no-invention/UPGRADEABLE.md) | work relies on documents, data, external facts, or consequential claims | — |
| R | [Evidence-Confidence Gate (`epistemic-status-gating@1.1.0`)](../../upgradeables/truth-grounding/epistemic-status-gating/UPGRADEABLE.md) | claims of mixed certainty are present | — |
| R | [Risk-Tier Scaling (`risk-tier-scaling@1.1.0`)](../../upgradeables/meta-control/risk-tier-scaling/UPGRADEABLE.md) | task risk varies or must be classified | — |
| R | [Critical Fact Verification (`critical-atomic-verification@1.1.0`)](../../upgradeables/validation/critical-atomic-verification/UPGRADEABLE.md) | small factual errors could change the outcome | — |
| R | [Independent Evidence Gate (`multi-truth-gating@1.1.0`)](../../upgradeables/truth-grounding/multi-truth-gating/UPGRADEABLE.md) | an important conclusion rests on fragile evidence | — |
| A | [Independent Evidence Redundancy (`truth-redundancy@1.1.0`)](../../upgradeables/truth-grounding/truth-redundancy/UPGRADEABLE.md) | a consequential claim can be independently checked | — |
| R | [Truth Priority Hierarchy (`truth-priority-hierarchy@1.1.0`)](../../upgradeables/truth-grounding/truth-priority-hierarchy/UPGRADEABLE.md) | evidence classes or authorities conflict | — |
| R | [Domain / Mode Isolation (`domain-mode-isolation@1.1.0`)](../../upgradeables/state/domain-mode-isolation/UPGRADEABLE.md) | multiple domains or semantic modes coexist | — |
| C | [Citation Fidelity Gate (`citation-fidelity@1.1.0`)](../../upgradeables/validation/citation-fidelity/UPGRADEABLE.md) | output contains citations or source-attributed claims | — |
| R | [Fail-Closed Abstention (`fail-closed-abstention@1.1.0`)](../../upgradeables/truth-grounding/fail-closed-abstention/UPGRADEABLE.md) | required evidence cannot be verified | — |
| A | [Non-Compensable Constraint Veto (`fermionic-veto@1.1.0`)](../../upgradeables/validation/fermionic-veto/UPGRADEABLE.md) | a defined critical condition must have veto authority | — |
| R | [Parallel Validation System (`parallel-qms@1.1.0`)](../../upgradeables/validation/parallel-qms/UPGRADEABLE.md) | a composed workflow needs structured quality evaluation | — |
| A | [Per-Region Reasoning Depth (`dynamic-depth-allocation@1.1.0`)](../../upgradeables/meta-control/dynamic-depth-allocation/UPGRADEABLE.md) | task regions vary in difficulty or risk | — |

Do not merge whole recipes. Add individual cross-cutting components only for
explicit requirements the primary recipe does not cover.
