# Long-Context Source Fidelity — Resolved Recipe

Generated discovery view. For normal execution, load the compact
[runtime recipe pack](../../runtime/recipes/long-context-source-fidelity.md) instead of full packages.
See the [source recipe notes](../long-context-source-fidelity.md) for composition and tests.

`R` stays required after selecting this recipe. `A`, `C`, and `O` require an
active trigger. `X` is excluded without explicit justification.

| Role | Component | Trigger summary | Requires |
|:---:|---|---|---|
| R | [Working-Memory Lock-In (`working-memory-lock-in@1.1.0`)](../../upgradeables/state/working-memory-lock-in/UPGRADEABLE.md) | critical state competes with large context | — |
| R | [Ordered Memory-State Update Engine (`sequential-memory-state-engine@1.1.0`)](../../upgradeables/state/sequential-memory-state-engine/UPGRADEABLE.md) | state changes across steps or source chunks | — |
| R | [Canonical Task State (`stateblock@1.1.0`)](../../upgradeables/state/stateblock/UPGRADEABLE.md) | work spans multiple steps or components | — |
| R | [Stable Long-Context (`stable-long-context@1.1.0`)](../../upgradeables/state/stable-long-context/UPGRADEABLE.md) | large corpus or long-running workflow | — |
| R | [Immutable Content Zones (`zero-drift-zones@1.1.0`)](../../upgradeables/drift-control/zero-drift-zones/UPGRADEABLE.md) | content contains fidelity-locked atoms | — |
| R | [Drift Suppression (`drift-suppression@1.1.0`)](../../upgradeables/drift-control/drift-suppression/UPGRADEABLE.md) | long, branching, or iterative work | — |
| C | [Image Text Fidelity Capture (`image-text-fidelity-capture@1.1.0`)](../../upgradeables/truth-grounding/image-text-fidelity-capture/UPGRADEABLE.md) | an image contains source text to transcribe | — |
| A | [Checkpointed Work Reflection (`reflectos@1.1.0`)](../../upgradeables/validation/reflectos/UPGRADEABLE.md) | output needs a deliberate quality pass | — |
| R | [Fail-Closed Abstention (`fail-closed-abstention@1.1.0`)](../../upgradeables/truth-grounding/fail-closed-abstention/UPGRADEABLE.md) | required evidence cannot be verified | — |
| A | [Independent Evidence Redundancy (`truth-redundancy@1.1.0`)](../../upgradeables/truth-grounding/truth-redundancy/UPGRADEABLE.md) | a consequential claim can be independently checked | — |
| C | [Citation Fidelity Gate (`citation-fidelity@1.1.0`)](../../upgradeables/validation/citation-fidelity/UPGRADEABLE.md) | output contains citations or source-attributed claims | — |
| A | [State Snapshot (`state-snapshot@1.1.0`)](../../upgradeables/state/state-snapshot/UPGRADEABLE.md) | a workflow pauses, hands off, or persists | — |

Do not merge whole recipes. Add individual cross-cutting components only for
explicit requirements the primary recipe does not cover.
