# Bidirectional Consistency — Behavioral Expectations

## Positive Activation

- **Given:** The code-to-requirement story may be plausible without every criterion actually being entailed.
- **Expect:** One missing error-handling criterion is found despite a plausible forward explanation.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the transformation is intentionally irreversible and no reverse contract is claimed
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** The declared transformation contract determines which information may be lost.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Do not certify when a material source constraint has no forward image or when the result implies a contradictory source condition.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** independent backward reconstruction for lossy or high-stakes transformations
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A summary reads plausibly from a report but, read alone, implies the opposite scope limitation.
- **Expect:** Fail the reverse pass and identify the scope inversion.
- **Reject:** Pass solely because every report section was mentioned.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
