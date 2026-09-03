# Fail-Closed Abstention — Behavioral Expectations

## Positive Activation

- **Given:** A required decision anchor is missing.
- **Expect:** A useful bounded summary without unsupported closure.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the failed condition is optional and does not affect the supported deliverable
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** A request for a definitive answer cannot override a failed required truth gate.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** A conclusion cannot be committed while any indispensable evidence or integrity condition remains failed or unverifiable.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** no essential failed gate may be bypassed by fluency or confidence
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** One indispensable truth gate is unverifiable while several optional checks pass.
- **Expect:** Withhold the affected conclusion and return only independently supported content.
- **Reject:** Majority voting that commits because more checks passed than failed.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
