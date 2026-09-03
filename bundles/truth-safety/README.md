# Truth Safety Bundle

Gate high-impact claims against evidence, conflict, risk, and abstention rules.

## Activation boundary

Activate proportionally to claim impact and available evidence.

## Required and optional components

- [`multi-truth-gating@1.1.0`](../../upgradeables/truth-grounding/multi-truth-gating/UPGRADEABLE.md) — required
- [`truth-redundancy@1.1.0`](../../upgradeables/truth-grounding/truth-redundancy/UPGRADEABLE.md) — optional; activate by trigger
- [`critical-atomic-verification@1.1.0`](../../upgradeables/validation/critical-atomic-verification/UPGRADEABLE.md) — optional; activate by trigger
- [`controlled-drift-corridors@1.1.0`](../../upgradeables/drift-control/controlled-drift-corridors/UPGRADEABLE.md) — optional; activate by trigger
- [`truth-priority-hierarchy@1.1.0`](../../upgradeables/truth-grounding/truth-priority-hierarchy/UPGRADEABLE.md) — required
- [`domain-mode-isolation@1.1.0`](../../upgradeables/state/domain-mode-isolation/UPGRADEABLE.md) — optional; activate by trigger
- [`fail-closed-abstention@1.1.0`](../../upgradeables/truth-grounding/fail-closed-abstention/UPGRADEABLE.md) — required
- [`citation-fidelity@1.1.0`](../../upgradeables/validation/citation-fidelity/UPGRADEABLE.md) — optional; activate by trigger
- [`counterfactual-integrity@1.1.0`](../../upgradeables/truth-grounding/counterfactual-integrity/UPGRADEABLE.md) — optional; activate by trigger
- [`fermionic-veto@1.1.0`](../../upgradeables/validation/fermionic-veto/UPGRADEABLE.md) — optional; activate by trigger
- [`risk-tier-scaling@1.1.0`](../../upgradeables/meta-control/risk-tier-scaling/UPGRADEABLE.md) — optional; activate by trigger

## Load order and critical interactions

Use the metadata `load_order`. Risk tiers allocate checks; evidence priority and abstention resolve failures without inventing support.

## Over-scaffolding boundary

Excessive for low-impact source-free tasks or when redundant checks add no independent evidence.
