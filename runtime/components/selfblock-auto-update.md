# Automatic Canonical-State Update (`selfblock-auto-update@1.1.0`)

Recovered name: SelfBlock Auto-Update

Purpose: Reduce stale state and forgotten deltas during iterative work.

Activate when: the host can update explicit state after steps.

Do not use when: the host cannot write persistent state; every token would trigger an update.

Requires: none.

## Runtime mechanism

Attach an update hook to defined events, compute the smallest state delta, validate it against schema and authority, then atomically merge it into the live SelfBlock while retaining provenance or a change note. The updater may change status and observations but not silently rewrite locked goals, permissions, or immutable evidence.

## Procedure

1. Define update-triggering events and mutable fields.
2. After an event, derive only the factual delta from the result.
3. Reject or quarantine changes to locked or authority-bearing fields.
4. Validate the delta against schema, provenance, and current version.
5. Apply atomically and record timestamp/version or concise change note.

## Guardrails

- Mandatory even on strong models: delta discipline; locked-field protection; version/provenance checks.
- Conflict/precedence: Locked goal, authority, and permission fields cannot be auto-mutated by lower-authority observations; Concurrent deltas require version checking or merge arbitration rather than last-write-wins.
- Stop or fail when: Disable automatic writes when atomicity, schema validation, or authority checks are unavailable; Escalate ambiguous changes to task identity or permissions.

Full package and provenance: [`selfblock-auto-update`](../../upgradeables/state/selfblock-auto-update/UPGRADEABLE.md).
