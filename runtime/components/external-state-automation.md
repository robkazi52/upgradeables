# External State Automation (`external-state-automation@1.1.0`)

Purpose: Serialize and restore important task state through real files, memory stores, databases, or project documents when the host supports persistence.

Activate when: continuation requires real external state.

Do not use when: the task ends in one session and needs no continuation; the host exposes no authorized persistent storage.

Requires: none.

## Runtime mechanism

Declare the actual storage capability and a versioned state schema, serialize only the minimum continuation fields with provenance and timestamp, write through an authorized host operation, and verify the write. On restoration, validate version and integrity before merging; never treat a requested or imagined write as persisted state.

## Procedure

1. Confirm an authorized storage mechanism, location, lifetime, and data policy.
2. Select the minimum state fields needed for continuation and serialize them with schema and provenance.
3. Write through the real host capability and verify the stored representation.
4. On resume, read and validate schema, integrity, freshness, and authority.
5. Reconcile restored state with current instructions and report any failed or stale persistence.

## Guardrails

- Mandatory even on strong models: capability declaration, minimum-state serialization, write verification, and restore validation.
- Conflict/precedence: Host, system, domain, and explicit user authority take precedence over this component; If no authorized storage capability is available, stop or escalate rather than forcing a nominal success.
- Stop or fail when: no authorized storage capability is available; write verification, schema validation, integrity, freshness, or restoration reconciliation fails.

Full package and provenance: [`external-state-automation`](../../upgradeables/persistence/external-state-automation/UPGRADEABLE.md).
