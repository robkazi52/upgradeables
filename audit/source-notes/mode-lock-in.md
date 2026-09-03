# Source Note — Mode Lock-In

- Slug: `mode-lock-in`
- ID: `T1-05`
- Source support: `sufficiently-recovered`
- Mechanism basis: `recovered`
- Final status: `PASS`

## Recovered facts and source anchors

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 2. November 28, 2025 — frozen T1-Core Bundle v1 (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 8. Working-Memory Lock-In Heartbeats (historical_assistant_artifact)

## Recovered or normalized purpose

Keep behavior stable across long sessions, tool calls, and distracting inputs.

## Operational mechanism

Represent the active mode as a small contract containing its goal, allowed transformations, forbidden behaviors, and exit condition. Recheck the contract at checkpoints; change modes only through an explicit transition that records why, what state carries forward, and which former rules deactivate.

## Trigger and task use

Triggers: a task can drift between modes. Best-fit tasks: strict transformations, long sessions, multi-mode assistants, policy-bound work.

## Interactions and failure boundary

Companions: task-set-lock-in, domain-mode-isolation, drift-suppression. Failure boundary: Do not lock an ambiguous high-impact choice before clarification.; Release or transition the lock when the task legitimately changes..

## Unresolved details / interpretation boundary

Recovered as an early Tier-1 control; later stability-guard material reinforces explicit invariants and controlled transitions.
