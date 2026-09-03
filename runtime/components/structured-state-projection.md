# Structured State Projection (`structured-state-projection@1.1.0`)

Purpose: Reduce context, privacy, and authority leakage between components.

Activate when: a component needs a bounded state view.

Do not use when: one trusted consumer legitimately needs the whole safe state; field dependencies are unknown.

Requires: none.

## Runtime mechanism

A modern interpretation is to define a projection contract listing allowed fields, necessary derived values, redactions, provenance, version, and write-back rights. Materialize the view from canonical state at invocation time and merge returned deltas only through the canonical owner's validation path.

## Procedure

1. Identify the consumer and its minimum information need.
2. Declare included, derived, redacted, and mandatory safety fields.
3. Generate the view from an identified canonical state version.
4. Attach provenance and freshness metadata.
5. Validate any returned delta against the consumer's write rights before canonical merge.

## Guardrails

- Mandatory even on strong models: least privilege; mandatory constraints; version/provenance.
- Conflict/precedence: Mandatory safety and authority fields override a consumer's request to omit them; A returned projection delta cannot overwrite fields outside declared write scope.
- Stop or fail when: Do not project when required field dependencies or safety constraints are unknown; Treat this mechanism as provisional until original concept-specific documentation is recovered.

Full package and provenance: [`structured-state-projection`](../../upgradeables/state/structured-state-projection/UPGRADEABLE.md).
