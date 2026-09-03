# Explore-to-Execute Transition (`progressive-mode-shaping@1.1.0`)

Recovered name: Progressive Mode Shaping

Purpose: Narrow a broad exploratory workflow through comparison and selection into precise execution as decisions become locked.

Activate when: work moves from design to execution.

Do not use when: the task is purely exploratory and requires no commitment; the task begins with one already locked deterministic procedure.

Requires: none.

## Runtime mechanism

Track which choices remain open and progressively reduce permitted breadth as evidence and decisions accumulate. Move through explore, compare, choose, plan, execute, and validate states; at each transition retire losing branches, lock accepted constraints, and lower drift. Unlike a hard two-mode switch, shaping may narrow in several evidence-backed increments.

## Procedure

1. Declare the initial exploration boundary and the decisions that must eventually lock.
2. Generate only the breadth justified at the current phase.
3. Compare candidates and record evidence for accepted and rejected choices.
4. Lock decisions and reduce allowed alternatives and drift at each phase transition.
5. Enter execution with one active plan, then validate against the locked state.

## Guardrails

- Mandatory even on strong models: evidence-backed narrowing and retirement of losing branches before execution.
- Conflict/precedence: Host, system, domain, and explicit user authority take precedence over this component; If transition criteria are absent or accepted decisions cannot be distinguished from open options, stop or escalate rather than forcing a nominal success.
- Stop or fail when: transition criteria are absent or accepted decisions cannot be distinguished from open options; narrowing would discard a materially plausible path before comparison.

Full package and provenance: [`progressive-mode-shaping`](../../upgradeables/orchestration/progressive-mode-shaping/UPGRADEABLE.md).
