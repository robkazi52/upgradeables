# Source Note — Critical Atomic Verification

- Slug: `critical-atomic-verification`
- ID: `T3-04`
- Source support: `sufficiently-recovered`
- Mechanism basis: `recovered`
- Final status: `PASS`

## Recovered facts and source anchors

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 1. Canonical current consolidated inventory (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 10.1 Source atomization (historical_assistant_artifact)

## Recovered or normalized purpose

Concentrate verification on the smallest facts whose failure would invalidate the output.

## Operational mechanism

Build a dependency graph from the intended conclusion back to minimal truth-bearing atoms. Mark an atom critical when its falsity, reversal, or absence would change the conclusion or safe action. Verify every critical atom directly at depth proportional to risk; propagate any failed or unknown atom forward so the dependent conclusion is repaired, qualified, or blocked.

## Trigger and task use

Triggers: small factual errors could change the outcome. Best-fit tasks: medical or legal factual synthesis, deployment decisions, financial calculations, requirements verification, citation-heavy research.

## Interactions and failure boundary

Companions: citation-fidelity, risk-tier-scaling, cross-checking-chains. Failure boundary: Do not certify a conclusion while any indispensable atom is false, materially conflicting, or unsupported beyond the allowed risk threshold..

## Unresolved details / interpretation boundary

The critical-atom focus is directly recovered and retains veto semantics for indispensable facts.
