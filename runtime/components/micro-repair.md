# Minimal Local Correction (`micro-repair@1.1.0`)

Recovered name: Micro-Repair

Purpose: Restore local correctness or completeness with the minimum semantic blast radius.

Activate when: a specific defect has been localized.

Do not use when: the artifact architecture is globally wrong; the same defect repeats systemically.

Requires: none.

## Runtime mechanism

Define a repair window around the smallest unit that fails an explicit criterion, freeze the surrounding accepted region, patch only that unit and any directly required connective token, then compare the window before and after. Widen once only when a direct dependency proves the first window insufficient; recurring or architecture-level failure escalates instead of allowing scope creep.

## Procedure

1. Identify the exact failed criterion and the smallest text, field, rule, or code unit causing it.
2. Mark the surrounding accepted content and locked facts as frozen.
3. Draft the smallest replacement that satisfies the criterion.
4. Check boundary coherence with the immediately preceding and following units.
5. Verify the target defect is gone and no frozen atom changed.

## Guardrails

- Mandatory even on strong models: smallest-fault localization; changed-atom comparison; systemic-failure escalation.
- Conflict/precedence: Do not preserve a frozen neighbor if it is proven part of the defect; explicitly widen the window instead; A locked invariant outranks local fluency.
- Stop or fail when: scope creep; cosmetic rewriting around a defect.

Full package and provenance: [`micro-repair`](../../upgradeables/editing-repair/micro-repair/UPGRADEABLE.md).
