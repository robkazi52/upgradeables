# Minimum Sufficient Explanation (`explanation-minimality-scaffold@1.1.0`)

Recovered name: Explanation Minimality Scaffold

Purpose: Remove explanatory material that does not change comprehension, verification, decision, or safe execution while retaining required rationale and caveats.

Activate when: verbosity can obscure the answer.

Do not use when: the user requests a tutorial or exhaustive rationale; high-stakes action requires full assumptions and warnings.

Requires: none.

## Runtime mechanism

Set an explanation contract consisting of the outcome, the minimum causal or evidentiary bridge, required caveats, and the next action. Draft those blocks first, then test every additional sentence with a deletion probe: if removal does not impair correctness, comprehension, verification, safety, or actionability for the target reader, delete it. This mechanism is modern; only the exact historical scaffold name was recovered.

## Procedure

1. Identify the reader, requested depth, decision or action, and risk tier.
2. List mandatory explanation blocks: answer, indispensable why, evidence or method needed for trust, caveats, and next action.
3. Draft one compact block for each mandatory need.
4. Run a deletion probe sentence by sentence against correctness, comprehension, verification, safety, and actionability.
5. Restore any deleted bridge whose absence creates a knowledge jump; stop when remaining content is necessary or explicitly requested.

## Guardrails

- Mandatory even on strong models: reader-and-risk calibration; mandatory-block check; deletion probe.
- Conflict/precedence: User-requested detail and risk-mandated disclosure override brevity; When a deletion creates ambiguity about scope, uncertainty, or authority, restore the qualifying content.
- Stop or fail when: terse but unactionable output; missing causal bridge.

Full package and provenance: [`explanation-minimality-scaffold`](../../upgradeables/output/explanation-minimality-scaffold/UPGRADEABLE.md).
