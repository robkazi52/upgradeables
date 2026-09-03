# Stable Long-Context (`stable-long-context@1.1.0`)

Purpose: Extend usable context duration without treating the entire transcript as equally current or important.

Activate when: large corpus or long-running workflow.

Do not use when: all relevant material fits clearly in one short exchange; lossless verbatim retention is required for every item.

Requires: none.

## Runtime mechanism

Maintain an invariant anchor containing task, authority, definitions, accepted decisions, and open obligations; keep detailed material behind stable indexed pointers; periodically reconcile new state, mark superseded items, and regenerate a compact current view. Retrieval expands only the region needed for the next step, and final validation checks output against the anchors rather than conversational recency.

## Procedure

1. Establish task, authority, terminology, and zero-drift facts as anchors.
2. Index detailed evidence and prior artifacts with stable identifiers.
3. At checkpoints, merge accepted deltas and mark replaced state as superseded.
4. Compact the active view while preserving pointers and unresolved items.
5. On resume, load the anchor first, then retrieve only the relevant detail.

## Guardrails

- Mandatory even on strong models: anchored invariants; current-versus-superseded distinction; retrievable provenance.
- Conflict/precedence: Explicit authority and accepted state transitions outrank recency; If compaction cannot preserve a high-impact nuance, retain the original excerpt or pointer in the active view.
- Stop or fail when: Do not compact evidence beyond recoverability when precise citation is required; Rebuild from canonical sources when anchor integrity or version lineage is uncertain.

Full package and provenance: [`stable-long-context`](../../upgradeables/state/stable-long-context/UPGRADEABLE.md).
