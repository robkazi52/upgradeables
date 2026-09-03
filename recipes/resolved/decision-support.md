# Decision Support — Resolved Recipe

Generated discovery view. Evaluate triggers here, then open only retained packages.
See the [source recipe notes](../decision-support.md) for composition and tests.

`R` stays required after selecting this recipe. `A`, `C`, and `O` require an
active trigger. `X` is excluded without explicit justification.

| Role | Component | Trigger summary | Requires |
|:---:|---|---|---|
| R | [Task-Set Lock-In (`task-set-lock-in@1.1.0`)](../../upgradeables/state/task-set-lock-in/UPGRADEABLE.md) | multi-step work begins or scope changes | — |
| R | [Decision-First Scaffold (`decision-first-scaffold@1.1.0`)](../../upgradeables/reasoning/decision-first-scaffold/UPGRADEABLE.md) | Activate when the task requires analysis risks becoming directionless. | — |
| R | [Grounding / No-Invention (`grounding-no-invention@1.1.0`)](../../upgradeables/truth-grounding/grounding-no-invention/UPGRADEABLE.md) | work relies on documents, data, external facts, or consequential claims | — |
| A | [Risk-Tier Scaling (`risk-tier-scaling@1.1.0`)](../../upgradeables/meta-control/risk-tier-scaling/UPGRADEABLE.md) | task risk varies or must be classified | — |
| A | [Anti-Tunnel Vision (`anti-tunnel-vision@1.1.0`)](../../upgradeables/reasoning/anti-tunnel-vision/UPGRADEABLE.md) | Activate when the task requires premature fixation is plausible. | — |
| A | [Bidirectional Consistency (`bidirectional-consistency@1.1.0`)](../../upgradeables/validation/bidirectional-consistency/UPGRADEABLE.md) | causal, logical, quantitative, or evidence claims are central | — |
| A | [Truth Priority Hierarchy (`truth-priority-hierarchy@1.1.0`)](../../upgradeables/truth-grounding/truth-priority-hierarchy/UPGRADEABLE.md) | evidence classes or authorities conflict | — |
| C | [Citation Fidelity Gate (`citation-fidelity@1.1.0`)](../../upgradeables/validation/citation-fidelity/UPGRADEABLE.md) | output contains citations or source-attributed claims | — |
| C | [Dynamic Depth Allocation (`dynamic-depth-allocation@1.1.0`)](../../upgradeables/meta-control/dynamic-depth-allocation/UPGRADEABLE.md) | task regions vary in difficulty or risk | — |
| A | [Parallel Quality Management System (`parallel-qms@1.1.0`)](../../upgradeables/validation/parallel-qms/UPGRADEABLE.md) | a composed workflow needs structured quality evaluation | — |

Do not merge whole recipes. Add individual cross-cutting components only for
explicit requirements the primary recipe does not cover.
