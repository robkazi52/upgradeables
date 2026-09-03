# Temporal Anchor Scaffold (`temporal-anchor-scaffold@1.1.0`)

Purpose: Prevent chronology errors and confusion between event time, publication time, and current validity.

Activate when: time or chronology affects correctness.

Do not use when: time has no bearing on the answer; dates are fabricated or inferred without support.

Requires: none.

## Runtime mechanism

A modern interpretation is a task-local table of events with normalized timestamp or interval, original temporal expression, source, event/publication/effective-time type, confidence, and before/after links. Unknown order stays unknown. Promote only durable verified temporal facts into canonical state and retire the scaffold after the timeline-dependent output is validated.

## Procedure

1. Identify which temporal distinctions affect the decision.
2. Extract expressions verbatim with source pointers.
3. Normalize only supported dates, zones, intervals, and time types.
4. Build explicit ordering links and mark ambiguity or contradiction.
5. Use the scaffold to test time-dependent claims.

## Guardrails

- Mandatory even on strong models: time-type distinction; source pointers; explicit unknown order.
- Conflict/precedence: Source-stated timestamps outrank inferred order; higher-authority corrections supersede earlier dates while retaining history; If timezone or effective date changes the conclusion and cannot be resolved, surface the branch rather than choosing one.
- Stop or fail when: Do not assert total order from partial temporal evidence; Treat the mechanism as provisional until original concept-specific documentation is recovered.

Full package and provenance: [`temporal-anchor-scaffold`](../../upgradeables/state/temporal-anchor-scaffold/UPGRADEABLE.md).
