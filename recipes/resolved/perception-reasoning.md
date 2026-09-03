# Perception & Spatial Reasoning — Resolved Recipe

Generated discovery view. Evaluate triggers here, then open only retained packages.
See the [source recipe notes](../perception-reasoning.md) for composition and tests.

`R` stays required after selecting this recipe. `A`, `C`, and `O` require an
active trigger. `X` is excluded without explicit justification.

| Role | Component | Trigger summary | Requires |
|:---:|---|---|---|
| R | [Task-Set Lock-In (`task-set-lock-in@1.1.0`)](../../upgradeables/state/task-set-lock-in/UPGRADEABLE.md) | multi-step work begins or scope changes | — |
| R | [Grounding / No-Invention (`grounding-no-invention@1.1.0`)](../../upgradeables/truth-grounding/grounding-no-invention/UPGRADEABLE.md) | work relies on documents, data, external facts, or consequential claims | — |
| R | [Anti-Tunnel Vision (`anti-tunnel-vision@1.1.0`)](../../upgradeables/reasoning/anti-tunnel-vision/UPGRADEABLE.md) | Activate when the task requires premature fixation is plausible. | — |
| R | [Bounded ExIt (`bounded-exit@1.1.0`)](../../upgradeables/reasoning/bounded-exit/UPGRADEABLE.md) | a draft needs iterative improvement | — |
| R | [Micro-Scaffolding (`micro-scaffolding@1.1.0`)](../../upgradeables/foundation/micro-scaffolding/UPGRADEABLE.md) | Activate when the task requires multi-step or high-constraint work. | — |
| A | [Bidirectional Consistency (`bidirectional-consistency@1.1.0`)](../../upgradeables/validation/bidirectional-consistency/UPGRADEABLE.md) | causal, logical, quantitative, or evidence claims are central | — |
| A | [Forethought / Checkpoints (`forethought-checkpoints@1.1.0`)](../../upgradeables/reasoning/forethought-checkpoints/UPGRADEABLE.md) | an action is costly, irreversible, or dependency-sensitive | — |
| A | [CoT-Structured State Block (`cot-structured-state-block@1.1.0`)](../../upgradeables/state/cot-structured-state-block/UPGRADEABLE.md) | structured intermediate task state must survive across steps | — |
| C | [Decision-First Scaffold (`decision-first-scaffold@1.1.0`)](../../upgradeables/reasoning/decision-first-scaffold/UPGRADEABLE.md) | Activate when the task requires analysis risks becoming directionless. | — |
| C | [Invariance Stress Scaffold (`invariance-stress-scaffold@1.1.0`)](../../upgradeables/validation/invariance-stress-scaffold/UPGRADEABLE.md) | a patch or rewrite must preserve invariants | — |
| C | [Counterfactual Integrity Gate (`counterfactual-integrity@1.1.0`)](../../upgradeables/truth-grounding/counterfactual-integrity/UPGRADEABLE.md) | counterfactual or hypothetical reasoning is used | — |
| O | [Multiverse Engine (`multiverse-reasoning@1.1.0`)](../../upgradeables/reasoning/multiverse-reasoning/UPGRADEABLE.md) | competing hypotheses or designs would add value | — |
| O | [Reasoning Budget / Cognitive Governor (`cognitive-governor@1.1.0`)](../../upgradeables/meta-control/cognitive-governor/UPGRADEABLE.md) | effort allocation materially affects cost or quality | — |
| X | [Global Coherence Heartbeat (`coherence-heartbeat@1.1.0`)](../../upgradeables/validation/coherence-heartbeat/UPGRADEABLE.md) | a workflow is long or multi-stage | — |
| X | [Meta-Supervisor Bundle (`meta-supervisor@1.1.0`)](../../upgradeables/meta-control/meta-supervisor/UPGRADEABLE.md) | complex scaffolding itself needs supervision | — |

Do not merge whole recipes. Add individual cross-cutting components only for
explicit requirements the primary recipe does not cover.
