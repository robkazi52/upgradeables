# Model-Capability Scaffolding Scale (`model-size-drift-scaling@1.1.0`)

Recovered name: Drift-Stability Scaling with Model Size

Purpose: Avoid fossilized over-scaffolding on more reliable models without mistaking model strength for permission to remove essential controls.

Activate when: adapting a workflow across model capability levels.

Do not use when: there is no comparative reliability evidence; the control is a non-negotiable invariant.

Requires: none.

## Runtime mechanism

Classify controls as invariant, compensatory, or convenience scaffolds; measure each target model on task-relevant drift, instruction retention, state consistency, and validation behavior; reduce only compensatory repetition whose function is demonstrably supplied by the base model. Preserve invariant truth, safety, authority, and external-state checks and restore removed scaffolds automatically when regression thresholds fail. DSS-MS scales control density by measured reliability; FPMS decides the wider host profile.

## Procedure

1. Inventory controls and classify each as invariant, compensatory, or convenience.
2. Evaluate the target model on representative drift, state, truth, and failure cases.
3. Map measured reliability to a predeclared scaffold tier.
4. Remove or compress one compensatory control class at a time while retaining invariants.
5. Run regression and adversarial tests against the prior configuration.

## Guardrails

- Mandatory even on strong models: truth and safety gates; explicit external-state checks; task-relevant regression tests.
- Conflict/precedence: Invariant controls do not scale away; High task risk may force a heavier profile than average model reliability suggests.
- Stop or fail when: size-as-capability assumption; invariant removal.

Full package and provenance: [`model-size-drift-scaling`](../../upgradeables/meta-control/model-size-drift-scaling/UPGRADEABLE.md).
