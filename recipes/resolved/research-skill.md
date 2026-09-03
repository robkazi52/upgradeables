# Research Skill — Resolved Recipe

Generated discovery view. Evaluate triggers here, then open only retained packages.
See the [source recipe notes](../research-skill.md) for composition and tests.

`R` stays required after selecting this recipe. `A`, `C`, and `O` require an
active trigger. `X` is excluded without explicit justification.

| Role | Component | Trigger summary | Requires |
|:---:|---|---|---|
| R | [Task-Set Lock-In (`task-set-lock-in@1.1.0`)](../../upgradeables/state/task-set-lock-in/UPGRADEABLE.md) | multi-step work begins or scope changes | — |
| R | [Scoped Loader / Loader Sequencing (`scoped-loader@1.1.0`)](../../upgradeables/context-retrieval/scoped-loader/UPGRADEABLE.md) | a modular workflow has multiple available components | — |
| R | [StateBlock (`stateblock@1.1.0`)](../../upgradeables/state/stateblock/UPGRADEABLE.md) | work spans multiple steps or components | — |
| R | [Grounding / No-Invention (`grounding-no-invention@1.1.0`)](../../upgradeables/truth-grounding/grounding-no-invention/UPGRADEABLE.md) | work relies on documents, data, external facts, or consequential claims | — |
| A | [Activation-Budget Funnel (`activation-budget-funnel@1.1.0`)](../../upgradeables/context-retrieval/activation-budget-funnel/UPGRADEABLE.md) | many sources or modules compete for attention | — |
| A | [Neuro-Focus (`neuro-focus@1.1.0`)](../../upgradeables/context-retrieval/neuro-focus/UPGRADEABLE.md) | large sources or a narrow debug region demand concentration | — |
| A | [Stable Long-Context (`stable-long-context@1.1.0`)](../../upgradeables/state/stable-long-context/UPGRADEABLE.md) | large corpus or long-running workflow | — |
| A | [Sequential Memory State Engine (SMSE) (`sequential-memory-state-engine@1.1.0`)](../../upgradeables/state/sequential-memory-state-engine/UPGRADEABLE.md) | state changes across steps or source chunks | — |
| A | [Multi-Truth Gating (`multi-truth-gating@1.1.0`)](../../upgradeables/truth-grounding/multi-truth-gating/UPGRADEABLE.md) | an important conclusion rests on fragile evidence | — |
| A | [Citation Fidelity Gate (`citation-fidelity@1.1.0`)](../../upgradeables/validation/citation-fidelity/UPGRADEABLE.md) | output contains citations or source-attributed claims | — |
| A | [Truth Priority Hierarchy (`truth-priority-hierarchy@1.1.0`)](../../upgradeables/truth-grounding/truth-priority-hierarchy/UPGRADEABLE.md) | evidence classes or authorities conflict | — |
| C | [Critical Atomic Verification (`critical-atomic-verification@1.1.0`)](../../upgradeables/validation/critical-atomic-verification/UPGRADEABLE.md) | small factual errors could change the outcome | — |
| A | [Parallel Quality Management System (`parallel-qms@1.1.0`)](../../upgradeables/validation/parallel-qms/UPGRADEABLE.md) | a composed workflow needs structured quality evaluation | — |
| O | [Anti-Tunnel Vision (`anti-tunnel-vision@1.1.0`)](../../upgradeables/reasoning/anti-tunnel-vision/UPGRADEABLE.md) | Activate when the task requires premature fixation is plausible. | — |
| C | [State Snapshot (`state-snapshot@1.1.0`)](../../upgradeables/state/state-snapshot/UPGRADEABLE.md) | a workflow pauses, hands off, or persists | — |

Do not merge whole recipes. Add individual cross-cutting components only for
explicit requirements the primary recipe does not cover.
