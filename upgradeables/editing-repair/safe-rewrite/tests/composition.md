# Safe Rewrite Logic — Behavioral Expectations

## Positive Activation

- **Given:** Length and jargon may change, but findings and uncertainty must not.
- **Expect:** A shorter update with unchanged factual atoms.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the user asks to change substantive meaning
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Truth and locked constraints outrank requested style.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** semantic drift
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** internal atom extraction
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A rewrite request changes tone and length only.
- **Expect:** The skill locks semantic atoms, transforms only tone and length, and compares sensitive facts and citations afterward.
- **Reject:** The skill produces a fluent rewrite with altered certainty, facts, or source mapping.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
