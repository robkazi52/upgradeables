# Source Note — Micro-Repair

- Slug: `micro-repair`
- ID: `T2-04`
- Source support: `sufficiently-recovered`
- Mechanism basis: `recovered`
- Final status: `PASS`

## Recovered facts and source anchors

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 1. Canonical current consolidated inventory (historical_recovery_inventory)

## Recovered or normalized purpose

Restore local correctness or completeness with the minimum semantic blast radius.

## Operational mechanism

Define a repair window around the smallest unit that fails an explicit criterion, freeze the surrounding accepted region, patch only that unit and any directly required connective token, then compare the window before and after. Widen once only when a direct dependency proves the first window insufficient; recurring or architecture-level failure escalates instead of allowing scope creep.

## Trigger and task use

Triggers: a specific defect has been localized. Best-fit tasks: one unsupported claim, one missing requirement, awkward transition, local contradiction, small formatting defect.

## Interactions and failure boundary

Companions: safe-rewrite, invariance-stress-scaffold, contradiction-micro-repair. Failure boundary: scope creep; cosmetic rewriting around a defect; repair that breaks a neighboring transition; serial local patches to a global architecture failure.

## Unresolved details / interpretation boundary

The source explicitly establishes smallest-unit correction, preservation of correct surroundings, and preference over regenerative rewriting.
