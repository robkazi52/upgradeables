# Working-Memory Lock-In (`working-memory-lock-in@1.1.0`)

Purpose: Prevent critical goals, constraints, identifiers, or safety conditions from being displaced by incoming context.

Activate when: critical state competes with large context.

Do not use when: nothing needs continuous salience; the proposed lock is large enough to crowd out working context.

Requires: none.

## Runtime mechanism

Select only the invariants whose omission would materially corrupt the task, store canonical pointers plus compact current values, and run a heartbeat before major actions to confirm freshness and consistency. Refresh on accepted state change; if a locked item conflicts or goes stale, block dependent work until reconciled.

## Procedure

1. Rank candidate state by consequence of omission.
2. Lock the smallest critical subset with canonical field pointers and version.
3. Check it before major actions and after context changes.
4. Refresh values only from accepted canonical updates.
5. Block or reconcile when a locked value is missing, stale, or contradictory.

## Guardrails

- Mandatory even on strong models: small high-consequence invariant set; canonical pointers; freshness checks.
- Conflict/precedence: Canonical accepted state overrides cached values after validation; A stale or contradictory safety-critical lock blocks dependent execution; lower-authority context cannot resolve it.
- Stop or fail when: Do not proceed when a critical locked field cannot be reconciled; Shrink the set when lock overhead begins to reduce task performance.

Full package and provenance: [`working-memory-lock-in`](../../upgradeables/state/working-memory-lock-in/UPGRADEABLE.md).
