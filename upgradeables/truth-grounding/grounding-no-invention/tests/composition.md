# Grounding / No-Invention — Behavioral Expectations

## Positive Activation

- **Given:** The workflow must extract structured facts from supplied records.
- **Expect:** Marks the field Not documented and continues with supported fields. Result: A source-faithful intake object with an explicit gap.
- **Reject:** Omitting the mechanism or instead doing this: Infer the date from the surrounding chronology.

## Negative Activation

- **Given:** pure creative generation has no asserted factual source boundary
- **Expect:** Remain inactive; do not begin the package-specific first step: Declare the allowed evidence boundary.
- **Reject:** Activating Grounding / No-Invention solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Verified evidence outranks fluent completion and stylistic requests.
- **Expect:** Honor the conflict rule and preserve this invariant: Mark material uncertainty and undocumented fields.
- **Reject:** Silently violating the stated precedence for Grounding / No-Invention

## Failure Boundary

- **Given:** When an essential material claim lacks support inside the authorized evidence boundary, omit it or fail closed.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: every asserted material fact must remain within the authorized evidence boundary
- **Reject:** Claiming a successful Grounding / No-Invention result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** every asserted material fact must remain within the authorized evidence boundary
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A plausible factual detail is absent from every authorized source.
- **Expect:** Omit or mark the detail unsupported even if it would make the answer more complete.
- **Reject:** Adding the detail from model priors without labeling it external or inferred.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
