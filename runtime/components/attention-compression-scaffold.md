# Temporary Focused-Context View (`attention-compression-scaffold@1.1.0`)

Recovered name: Attention Compression Scaffold

Purpose: Reduce attention burden while retaining the facts, constraints, provenance, and retrieval pointers required by the current subtask.

Activate when: source volume exceeds the active workspace.

Do not use when: the original context is already small; exact source wording must remain live.

Requires: none.

## Runtime mechanism

Modern operational interpretation: select task-relevant facts, locked literals, decisions, open questions, and source pointers from a larger context; encode them in a compact indexed view; validate that protected meaning and provenance remain recoverable; and keep a route back to the original material. Compression changes representation size, not truth status or authority.

## Procedure

1. Define the current subtask and protected atoms that compression must preserve.
2. Partition context into retain verbatim, summarize with provenance, pointer-only, and retire classes.
3. Build a compact indexed view with stable source references.
4. Check every locked atom and decision against the original context.
5. Use the compact view for the subtask while retaining reload pointers.

## Guardrails

- Mandatory even on strong models: protected-atom preservation; provenance and reloadability; invalidation on state change.
- Conflict/precedence: Zero-drift and source-fidelity requirements override compression goals; If meaning preservation cannot be verified, use the original context or a pointer rather than a lossy substitute.
- Stop or fail when: Do not activate the compressed view when a protected fact, conflict, or provenance link is lost or unverifiable.

Full package and provenance: [`attention-compression-scaffold`](../../upgradeables/context-retrieval/attention-compression-scaffold/UPGRADEABLE.md).
