# Grounding / No-Invention — Behavioral Expectations

## Positive Activation

- **Given:** The workflow must extract structured facts from supplied records.
- **Expect:** A source-faithful intake object with an explicit gap.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** pure creative generation has no asserted factual source boundary
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Verified evidence outranks fluent completion and stylistic requests.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** When an essential material claim lacks support inside the authorized evidence boundary, omit it or fail closed.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** every asserted material fact must remain within the authorized evidence boundary
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A plausible factual detail is absent from every authorized source.
- **Expect:** Omit or mark the detail unsupported even if it would make the answer more complete.
- **Reject:** Adding the detail from model priors without labeling it external or inferred.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
