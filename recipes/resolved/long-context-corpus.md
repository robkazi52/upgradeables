# Long-Context / Corpus — Resolved Recipe

Generated discovery view. Evaluate triggers here, then open only retained packages.
See the [source recipe notes](../long-context-corpus.md) for composition and tests.

`R` stays required after selecting this recipe. `A`, `C`, and `O` require an
active trigger. `X` is excluded without explicit justification.

| Role | Component | Trigger summary | Requires |
|:---:|---|---|---|
| R | [StateBlock (`stateblock@1.0.0`)](../../upgradeables/state/stateblock/UPGRADEABLE.md) | work spans multiple steps or components | — |
| R | [Sequential Memory State Engine (SMSE) (`sequential-memory-state-engine@1.0.0`)](../../upgradeables/state/sequential-memory-state-engine/UPGRADEABLE.md) | state changes across steps or source chunks | — |
| A | [Working-Memory Lock-In (`working-memory-lock-in@1.0.0`)](../../upgradeables/state/working-memory-lock-in/UPGRADEABLE.md) | critical state competes with large context | — |
| R | [Stable Long-Context (`stable-long-context@1.0.0`)](../../upgradeables/state/stable-long-context/UPGRADEABLE.md) | large corpus or long-running workflow | — |
| R | [Activation-Budget Funnel (`activation-budget-funnel@1.0.0`)](../../upgradeables/context-retrieval/activation-budget-funnel/UPGRADEABLE.md) | many sources or modules compete for attention | — |
| A | [Attention Compression Scaffold (`attention-compression-scaffold@1.0.0`)](../../upgradeables/context-retrieval/attention-compression-scaffold/UPGRADEABLE.md) | source volume exceeds the active workspace | — |
| A | [Neuro-Focus (`neuro-focus@1.0.0`)](../../upgradeables/context-retrieval/neuro-focus/UPGRADEABLE.md) | large sources or a narrow debug region demand concentration | — |
| R | [Drift Suppression (`drift-suppression@1.0.0`)](../../upgradeables/drift-control/drift-suppression/UPGRADEABLE.md) | long, branching, or iterative work | — |
| A | [Global Coherence Heartbeat (`coherence-heartbeat@1.0.0`)](../../upgradeables/validation/coherence-heartbeat/UPGRADEABLE.md) | a workflow is long or multi-stage | — |
| C | [Cross-Context Resonance Lock (`cross-context-resonance-lock@1.0.0`)](../../upgradeables/orchestration/cross-context-resonance-lock/UPGRADEABLE.md) | related contexts must stay aligned across a long task | — |
| A | [State Snapshot (`state-snapshot@1.0.0`)](../../upgradeables/state/state-snapshot/UPGRADEABLE.md) | a workflow pauses, hands off, or persists | — |
| C | [Citation Fidelity Gate (`citation-fidelity@1.0.0`)](../../upgradeables/validation/citation-fidelity/UPGRADEABLE.md) | output contains citations or source-attributed claims | — |

Do not merge whole recipes. Add individual cross-cutting components only for
explicit requirements the primary recipe does not cover.
