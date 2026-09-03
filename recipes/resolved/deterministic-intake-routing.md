# Deterministic Intake / Routing — Resolved Recipe

Generated discovery view. Evaluate triggers here, then open only retained packages.
See the [source recipe notes](../deterministic-intake-routing.md) for composition and tests.

`R` stays required after selecting this recipe. `A`, `C`, and `O` require an
active trigger. `X` is excluded without explicit justification.

| Role | Component | Trigger summary | Requires |
|:---:|---|---|---|
| R | [Task-Set Lock-In (`task-set-lock-in@1.1.0`)](../../upgradeables/state/task-set-lock-in/UPGRADEABLE.md) | multi-step work begins or scope changes | — |
| A | [Clarification Gateway (`clarification-gateway@1.1.0`)](../../upgradeables/foundation/clarification-gateway/UPGRADEABLE.md) | required variables are missing or instructions conflict | — |
| R | [Grounding / No-Invention (`grounding-no-invention@1.1.0`)](../../upgradeables/truth-grounding/grounding-no-invention/UPGRADEABLE.md) | work relies on documents, data, external facts, or consequential claims | — |
| R | [Scoped Loader / Loader Sequencing (`scoped-loader@1.1.0`)](../../upgradeables/context-retrieval/scoped-loader/UPGRADEABLE.md) | a modular workflow has multiple available components | — |
| R | [Domain / Mode Isolation (`domain-mode-isolation@1.1.0`)](../../upgradeables/state/domain-mode-isolation/UPGRADEABLE.md) | multiple domains or semantic modes coexist | — |
| R | [StateBlock (`stateblock@1.1.0`)](../../upgradeables/state/stateblock/UPGRADEABLE.md) | work spans multiple steps or components | — |
| A | [Structured State Projection (`structured-state-projection@1.1.0`)](../../upgradeables/state/structured-state-projection/UPGRADEABLE.md) | a component needs a bounded state view | — |
| A | [Authority Anchor Enforcement (`authority-anchor-enforcement@1.1.0`)](../../upgradeables/orchestration/authority-anchor-enforcement/UPGRADEABLE.md) | Activate when the task requires multiple instruction authorities coexist. | — |
| C | [External State Automation (`external-state-automation@1.1.0`)](../../upgradeables/persistence/external-state-automation/UPGRADEABLE.md) | continuation requires real external state | — |
| R | [Authenticity & Anti-Evasion Principle (`authenticity-anti-evasion@1.1.0`)](../../upgradeables/truth-grounding/authenticity-anti-evasion/UPGRADEABLE.md) | claims about evidence, actions, or completion are emitted | — |

Do not merge whole recipes. Add individual cross-cutting components only for
explicit requirements the primary recipe does not cover.
