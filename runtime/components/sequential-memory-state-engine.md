# Ordered Memory-State Update Engine (`sequential-memory-state-engine@1.1.0`)

Recovered name: Sequential Memory State Engine (SMSE)

Purpose: Preserve sequence, provenance, relevance, and current truth across long-running work.

Activate when: state changes across steps or source chunks.

Do not use when: a one-shot task has no state evolution; event ordering cannot be established and ordering is safety-critical.

Requires: none.

## Runtime mechanism

For each event, preserve source and time, normalize it into the state schema, classify affected fields, compare with the current version, resolve contradiction by authority and recency rules, commit an atomic delta, derive consumer-specific projections, and emit a checkpoint. History remains available, but only the resolved current state drives action.

## Procedure

1. Ingest one event with source, time, and authority metadata.
2. Normalize it without discarding the original payload pointer.
3. Classify affected state fields and compare against the current version.
4. Resolve additions, updates, contradictions, and retractions using explicit precedence.
5. Commit the delta atomically and increment the version.

## Guardrails

- Mandatory even on strong models: ordered transitions; provenance; current/history separation.
- Conflict/precedence: Authority outranks recency unless the authoritative source explicitly delegates update power; Unresolvable contradictions remain labeled and block dependent actions rather than being averaged.
- Stop or fail when: Stop dependent actions when a safety-critical contradiction cannot be resolved; Do not assert chronological correctness when timestamps or event identity are missing.

Full package and provenance: [`sequential-memory-state-engine`](../../upgradeables/state/sequential-memory-state-engine/UPGRADEABLE.md).
