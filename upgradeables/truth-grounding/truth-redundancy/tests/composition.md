# Truth Redundancy — Behavioral Expectations

## Positive Activation

- **Given:** A single transcription or calculation error could change the outcome.
- **Expect:** Records both anchors and checks their independence. Result: An anchor pair ready for Multi-Truth Gating.
- **Reject:** Omitting the mechanism or instead doing this: Treat two paragraphs citing the same table as independent.

## Negative Activation

- **Given:** the claim is low risk and an authoritative primary source is decisive
- **Expect:** Remain inactive; do not begin the package-specific first step: Identify the consequential truth atom.
- **Reject:** Activating Truth Redundancy solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Independence is invalid if both anchors share the same unverified upstream source.
- **Expect:** Honor the conflict rule and preserve this invariant: Test independence, not just numerical multiplicity.
- **Reject:** Silently violating the stated precedence for Truth Redundancy

## Failure Boundary

- **Given:** If no genuinely independent second anchor is available, report that limitation and do not claim redundant verification.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: when redundancy is claimed, the anchors must be genuinely independent
- **Reject:** Claiming a successful Truth Redundancy result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** when redundancy is claimed, the anchors must be genuinely independent
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** Two validators both rely on the same incorrect extracted value.
- **Expect:** Reject the pair as non-independent.
- **Reject:** Certify redundancy solely because two validators returned pass.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
