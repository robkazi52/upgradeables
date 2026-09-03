# Fail-Closed Abstention (`fail-closed-abstention@1.1.0`)

Purpose: Ensure that missing essential support produces an explicit bounded result rather than fabricated closure.

Activate when: required evidence cannot be verified.

Do not use when: the failed condition is optional and does not affect the supported deliverable; a harmless creative task has no factual commitment gate.

Requires: none.

## Runtime mechanism

Consume explicit validator outcomes and distinguish essential from optional failures. If an essential condition is failed or unverifiable, block the affected conclusion, preserve any independently supported subset, and state the unresolved dependency; never synthesize a missing fact merely to obtain a pass.

## Procedure

1. List the conditions required to commit the conclusion.
2. Read each condition's pass, fail, or unverifiable result.
3. Determine which failures invalidate only one claim and which invalidate the whole conclusion.
4. Remove or narrow invalidated claims while preserving independently supported content.
5. Return the supported subset plus the unresolved dependency or an explicit abstention.

## Guardrails

- Mandatory even on strong models: no essential failed gate may be bypassed by fluency or confidence.
- Conflict/precedence: A request for a definitive answer cannot override a failed required truth gate; Preserve supported content unless higher authority requires withholding the entire output.
- Stop or fail when: A conclusion cannot be committed while any indispensable evidence or integrity condition remains failed or unverifiable.

Full package and provenance: [`fail-closed-abstention`](../../upgradeables/truth-grounding/fail-closed-abstention/UPGRADEABLE.md).
