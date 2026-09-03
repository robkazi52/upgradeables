# Source Note — External State Automation

- Slug: `external-state-automation`
- ID: `T2-20`
- Source support: `sufficiently-recovered`
- Mechanism basis: `recovered`
- Final status: `PASS`

## Recovered facts and source anchors

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T2-20. External State Automation (current_consolidated_catalog)

## Recovered or normalized purpose

Serialize and restore important task state through real files, memory stores, databases, or project documents when the host supports persistence.

## Operational mechanism

Declare the actual storage capability and a versioned state schema, serialize only the minimum continuation fields with provenance and timestamp, write through an authorized host operation, and verify the write. On restoration, validate version and integrity before merging; never treat a requested or imagined write as persisted state.

## Trigger and task use

Triggers: continuation requires real external state. Best-fit tasks: multi-session projects, durable agent workflows, long document production.

## Interactions and failure boundary

Companions: state-snapshot, state-routing-bus. Failure boundary: no authorized storage capability is available; write verification, schema validation, integrity, freshness, or restoration reconciliation fails.

## Unresolved details / interpretation boundary

Historical identity, purpose, and core behavior are recovered; v0.2 states the mechanism explicitly without claiming hidden capabilities.
