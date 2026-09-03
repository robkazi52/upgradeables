# Source Note — Drift Suppression

- Slug: `drift-suppression`
- ID: `T1-02`
- Source support: `sufficiently-recovered`
- Mechanism basis: `recovered`
- Final status: `PASS`

## Recovered facts and source anchors

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — ECL / Drift Sink (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — `DRIFT_MONITOR_T1` (historical_assistant_artifact)

## Recovered or normalized purpose

Keep execution aligned after distracting context, repeated transformation, or model error.

## Operational mechanism

Compare current plan, state, or artifact against locked task fields, authoritative source anchors, and region-specific corridor tests. Classify each deviation as authorized change, benign variation, or drift; for drift, restore the smallest affected region from the last validated state, reapply the transform under tighter constraints, and record the cause so recurrence can be prevented.

## Trigger and task use

Triggers: long, branching, or iterative work. Best-fit tasks: long agent workflows, high-fidelity editing, multi-stage synthesis, policy-bound generation.

## Interactions and failure boundary

Companions: task-set-lock-in, controlled-drift-corridors, zero-drift-zones. Failure boundary: Stop publication when a high-impact deviation cannot be repaired or adjudicated.; Do not claim suppression if no independent baseline survives the transformation..

## Unresolved details / interpretation boundary

This is a core Tier-1 recovered control, with later sources reinforcing anchor/check/repair semantics.
