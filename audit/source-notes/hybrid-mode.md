# Source Note — HYBRID Mode

- Slug: `hybrid-mode`
- ID: `T4-08`
- Source support: `sufficiently-recovered`
- Mechanism basis: `recovered`
- Final status: `PASS`

## Recovered facts and source anchors

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 10. Tier-4 / Meta-Supervisor recovered family (historical_recovery_inventory)

## Recovered or normalized purpose

Combine broad planning capability with conservative implementation without letting speculative branch assumptions leak into committed work.

## Operational mechanism

Run POWER only to generate and compare bounded plans, then collapse to one plan and construct a handoff containing locked goals, selected decisions, rejected assumptions, evidence needs, risks, and execution invariants. A supervisor validates the handoff before activating SAFE, which executes only the committed plan with narrow drift and atomic checks. Re-enter POWER only through a checkpoint when execution exposes an architecture-level defect.

## Trigger and task use

Triggers: work includes both broad design and grounded execution. Best-fit tasks: architecture followed by implementation, research plan followed by evidence extraction, migration design followed by cutover, complex repository builds.

## Interactions and failure boundary

Companions: power-mode, safe-mode, ultimate-suite-supervisor. Failure boundary: mode leakage; uncollapsed execution; lost constraints at handoff; silent oscillation; POWER used to bypass SAFE evidence rules.

## Unresolved details / interpretation boundary

The historical catalog explicitly describes POWER for planning, SAFE for execution, supervisor-controlled transitions, and HYBRID as the accepted default philosophy.
