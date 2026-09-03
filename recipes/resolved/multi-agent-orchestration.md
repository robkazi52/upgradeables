# Multi-Agent / Orchestration — Resolved Recipe

Generated discovery view. For normal execution, load the compact
[runtime recipe pack](../../runtime/recipes/multi-agent-orchestration.md) instead of full packages.
See the [source recipe notes](../multi-agent-orchestration.md) for composition and tests.

`R` stays required after selecting this recipe. `A`, `C`, and `O` require an
active trigger. `X` is excluded without explicit justification.

| Role | Component | Trigger summary | Requires |
|:---:|---|---|---|
| R | [Modular System Design Orchestrator (`architect-orchestrator@1.1.0`)](../../upgradeables/orchestration/architect-orchestrator/UPGRADEABLE.md) | designing or refactoring a Skill, OS, framework, or workflow | — |
| R | [Scoped Loader / Loader Sequencing (`scoped-loader@1.1.0`)](../../upgradeables/context-retrieval/scoped-loader/UPGRADEABLE.md) | a modular workflow has multiple available components | — |
| R | [Task-State Handoff Router (`state-routing-bus@1.1.0`)](../../upgradeables/orchestration/state-routing-bus/UPGRADEABLE.md) | multiple components must exchange typed state | — |
| R | [Canonical Task State (`stateblock@1.1.0`)](../../upgradeables/state/stateblock/UPGRADEABLE.md) | work spans multiple steps or components | — |
| R | [State Snapshot (`state-snapshot@1.1.0`)](../../upgradeables/state/state-snapshot/UPGRADEABLE.md) | a workflow pauses, hands off, or persists | — |
| R | [Domain / Mode Isolation (`domain-mode-isolation@1.1.0`)](../../upgradeables/state/domain-mode-isolation/UPGRADEABLE.md) | multiple domains or semantic modes coexist | — |
| A | [Cross-Module Coordination (`resonance@1.1.0`)](../../upgradeables/orchestration/resonance/UPGRADEABLE.md) | several active modules must align | — |
| A | [Parallel Validation System (`parallel-qms@1.1.0`)](../../upgradeables/validation/parallel-qms/UPGRADEABLE.md) | a composed workflow needs structured quality evaluation | — |
| A | [Multi-Layer Consistency (`multi-layer-consistency@1.1.0`)](../../upgradeables/validation/multi-layer-consistency/UPGRADEABLE.md) | multiple authority layers are composed | — |
| C | [External State Automation (`external-state-automation@1.1.0`)](../../upgradeables/persistence/external-state-automation/UPGRADEABLE.md) | continuation requires real external state | — |

Do not merge whole recipes. Add individual cross-cutting components only for
explicit requirements the primary recipe does not cover.
