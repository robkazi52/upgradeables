# Source Note — Compute-Adaptive Drift Constraining

- Slug: `compute-adaptive-drift`
- ID: `T4-10`
- Source support: `strongly-derivable`
- Mechanism basis: `normalized-from-recovered`
- Final status: `PASS`

## Recovered facts and source anchors

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — Compute-Adaptive Drift (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — ECL / Drift Sink (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 10.3 Drift widths (historical_assistant_artifact)

## Recovered or normalized purpose

Maintain semantic reliability across weak and strong runtimes without burdening every runtime identically.

## Operational mechanism

Classify the task risk and runtime's demonstrated capacity, then choose an enforcement profile: weaker or unverified runtimes receive smaller steps, explicit state, more frequent source checks, and tighter drift corridors; stronger verified runtimes may combine steps and reduce scaffolding. The semantic acceptance tests, authority hierarchy, citations, and zero-drift fields never relax.

## Trigger and task use

Triggers: compute/depth varies across a task. Best-fit tasks: cross-model skills, variable tool availability, cost-limited execution, mixed-capability agents.

## Interactions and failure boundary

Companions: controlled-drift-corridors, drift-suppression, micro-scaffolding. Failure boundary: Do not relax controls for high-impact claims without demonstrated validation performance.; Fall back to the strict profile when runtime behavior is unstable or unobservable..

## Unresolved details / interpretation boundary

The purpose is directly recovered, but the detailed calibration profile is a conservative normalization from capability-scaling and drift-width architecture.
