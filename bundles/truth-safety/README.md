# Truth Safety Bundle

Gate high-impact claims against evidence, conflict, risk, and abstention rules.

## Activation boundary

Activate proportionally to claim impact and available evidence.

## Required and optional components

- [`risk-tier-scaling@1.1.0`](../../upgradeables/meta-control/risk-tier-scaling/UPGRADEABLE.md) — required
- [`domain-mode-isolation@1.1.0`](../../upgradeables/state/domain-mode-isolation/UPGRADEABLE.md) — optional; activate by trigger
- [`controlled-drift-corridors@1.1.0`](../../upgradeables/drift-control/controlled-drift-corridors/UPGRADEABLE.md) — optional; activate by trigger
- [`counterfactual-integrity@1.1.0`](../../upgradeables/truth-grounding/counterfactual-integrity/UPGRADEABLE.md) — optional; activate by trigger
- [`truth-redundancy@1.1.0`](../../upgradeables/truth-grounding/truth-redundancy/UPGRADEABLE.md) — optional; activate by trigger
- [`critical-atomic-verification@1.1.0`](../../upgradeables/validation/critical-atomic-verification/UPGRADEABLE.md) — optional; activate by trigger
- [`multi-truth-gating@1.1.0`](../../upgradeables/truth-grounding/multi-truth-gating/UPGRADEABLE.md) — optional; activate by trigger
- [`citation-fidelity@1.1.0`](../../upgradeables/validation/citation-fidelity/UPGRADEABLE.md) — optional; activate by trigger
- [`truth-priority-hierarchy@1.1.0`](../../upgradeables/truth-grounding/truth-priority-hierarchy/UPGRADEABLE.md) — required
- [`fermionic-veto@1.1.0`](../../upgradeables/validation/fermionic-veto/UPGRADEABLE.md) — optional; activate by trigger
- [`fail-closed-abstention@1.1.0`](../../upgradeables/truth-grounding/fail-closed-abstention/UPGRADEABLE.md) — required

## Load order and critical interactions

Use the metadata `load_order`. Risk tier and domain are established before selecting evidence checks; priority and veto resolution precede the final fail-closed decision, while redundant or citation checks activate only when their evidence inputs exist.

## Over-scaffolding boundary

Excessive for low-impact source-free tasks or when redundant checks add no independent evidence.
