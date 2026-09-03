# State Snapshot (`state-snapshot@1.1.0`)

Purpose: Create a stable checkpoint that can be resumed or audited after interruption.

Activate when: a workflow pauses, hands off, or persists.

Do not use when: a snapshot would persist prohibited sensitive data; state is invalid or mid-transaction.

Requires: none.

## Runtime mechanism

At an explicit checkpoint, validate and freeze the canonical state version together with schema version, timestamp, task identity, provenance pointers, unresolved items, and a link to any previous snapshot. Consumers resume by verifying lineage and reconciling newer events; the snapshot itself remains immutable.

## Procedure

1. Choose a transaction-safe checkpoint.
2. Validate required fields and unresolved-state labels.
3. Serialize the state plus schema/version, time, identity, and provenance pointers.
4. Compute or record an integrity identifier and predecessor link.
5. On resume, verify integrity and reconcile all post-snapshot events before acting.

## Guardrails

- Mandatory even on strong models: immutable version identity; unresolved items; provenance pointers.
- Conflict/precedence: A newer validated canonical state outranks an older snapshot; If snapshot identity or lineage fails verification, rebuild from authoritative events instead of guessing.
- Stop or fail when: Do not restore when integrity, task identity, or schema compatibility cannot be established; Exclude or redact fields that cannot legally or safely persist.

Full package and provenance: [`state-snapshot`](../../upgradeables/state/state-snapshot/UPGRADEABLE.md).
