# Retired-Branch Quarantine (`drift-sink-scaffold@1.1.0`)

Recovered name: Drift Sink Scaffold

Purpose: Stop known drift attractors from repeatedly re-entering active reasoning without destroying potentially useful history.

Activate when: discarded branches repeatedly re-enter active reasoning.

Do not use when: the branch is unresolved rather than rejected; quarantine would conceal contrary evidence.

Requires: none.

## Runtime mechanism

A cautious modern interpretation is a reversible quarantine ledger: move an explicitly classified branch out of the active view, record why, by whose authority, its provenance, dependencies, review condition, and stable pointer, then block automatic retrieval unless a matching review trigger fires. The sink is neither deletion nor a semantic garbage collector, and the unrecovered ECL label must not be expanded speculatively.

## Procedure

1. Identify a branch that repeatedly causes drift and classify it as superseded, rejected, irrelevant, or low-authority.
2. Check whether any active claim depends on it and whether contrary-evidence duties require visibility.
3. Create a task-local sink entry with reason, authority, provenance, dependencies, and restore trigger.
4. Remove it from automatic active retrieval while retaining its stable pointer.
5. Review the sink at milestone or trigger events.

## Guardrails

- Mandatory even on strong models: reversibility; authority/reason record; dependency check.
- Conflict/precedence: Higher-authority evidence or audit obligations can force restoration; When a branch contains both obsolete and still-relevant facts, split it rather than sinking the whole branch.
- Stop or fail when: Do not quarantine unresolved contrary evidence or safety-critical information; Treat the mechanism as provisional until original concept-specific documentation is recovered.

Full package and provenance: [`drift-sink-scaffold`](../../upgradeables/drift-control/drift-sink-scaffold/UPGRADEABLE.md).
