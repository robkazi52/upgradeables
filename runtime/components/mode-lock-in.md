# Mode Lock-In (`mode-lock-in@1.1.0`)

Purpose: Keep behavior stable across long sessions, tool calls, and distracting inputs.

Activate when: a task can drift between modes.

Do not use when: exploration intentionally needs rapid mode switching; the user has not yet chosen among materially different modes.

Requires: none.

## Runtime mechanism

Represent the active mode as a small contract containing its goal, allowed transformations, forbidden behaviors, and exit condition. Recheck the contract at checkpoints; change modes only through an explicit transition that records why, what state carries forward, and which former rules deactivate.

## Procedure

1. Choose the mode from the clarified task and authority stack.
2. Write its operative invariants and exclusions into active state.
3. Tag work products and tool calls with the active mode where useful.
4. At checkpoints, test for deviations from the invariant set.
5. On an authorized switch, record the transition and replace rather than blend incompatible mode rules.

## Guardrails

- Mandatory even on strong models: operative invariants; no silent switching; checkpoint validation.
- Conflict/precedence: Higher-authority instructions may force a mode transition; user content cannot silently do so; When mode and task objective conflict, clarify or reselect rather than weakening either implicitly.
- Stop or fail when: Do not lock an ambiguous high-impact choice before clarification; Release or transition the lock when the task legitimately changes.

Full package and provenance: [`mode-lock-in`](../../upgradeables/state/mode-lock-in/UPGRADEABLE.md).
