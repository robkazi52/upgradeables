# Truth Redundancy — Behavioral Expectations

## Positive Activation

- **Given:** A single transcription or calculation error could change the outcome.
- **Expect:** An anchor pair ready for Multi-Truth Gating.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the claim is low risk and an authoritative primary source is decisive
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Independence is invalid if both anchors share the same unverified upstream source.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** If no genuinely independent second anchor is available, report that limitation and do not claim redundant verification.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** when redundancy is claimed, the anchors must be genuinely independent
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** Two validators both rely on the same incorrect extracted value.
- **Expect:** Reject the pair as non-independent.
- **Reject:** Certify redundancy solely because two validators returned pass.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
