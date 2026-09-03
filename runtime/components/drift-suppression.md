# Drift Suppression (`drift-suppression@1.1.0`)

Purpose: Keep execution aligned after distracting context, repeated transformation, or model error.

Activate when: long, branching, or iterative work.

Do not use when: no semantic baseline or allowed corridor exists; creative divergence is the explicit objective.

Requires: none.

## Runtime mechanism

Compare current plan, state, or artifact against locked task fields, authoritative source anchors, and region-specific corridor tests. Classify each deviation as authorized change, benign variation, or drift; for drift, restore the smallest affected region from the last validated state, reapply the transform under tighter constraints, and record the cause so recurrence can be prevented.

## Procedure

1. Establish baseline anchors and permitted drift corridors before substantive transformation.
2. Run checks at risk-based checkpoints and after context transitions.
3. Compare objective, entities, claims, quantities, obligations, uncertainty, and required structure.
4. Classify discrepancies using authority and corridor rules.
5. Rollback the smallest affected region, tighten the relevant control, and regenerate or request review.

## Guardrails

- Mandatory even on strong models: source/task baseline; risk-based checks; minimal rollback.
- Conflict/precedence: Latest authorized task/source state defines the baseline, not the oldest lock by default; When automated checks and cited source inspection disagree, hold the output and resolve the checker or source version.
- Stop or fail when: Stop publication when a high-impact deviation cannot be repaired or adjudicated; Do not claim suppression if no independent baseline survives the transformation.

Full package and provenance: [`drift-suppression`](../../upgradeables/drift-control/drift-suppression/UPGRADEABLE.md).
