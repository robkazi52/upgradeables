# Fail-Closed Abstention — Behavioral Expectations

## Positive Activation

- **Given:** A required decision anchor is missing.
- **Expect:** Returns the supported background and abstains from the recommendation while naming the missing result. Result: A useful bounded summary without unsupported closure.
- **Reject:** Omitting the mechanism or instead doing this: Infer the result from adjacent evidence.

## Negative Activation

- **Given:** the failed condition is optional and does not affect the supported deliverable
- **Expect:** Remain inactive; do not begin the package-specific first step: List the conditions required to commit the conclusion.
- **Reject:** Activating Fail-Closed Abstention solely because its name appears relevant

## Precedence Or Conflict

- **Given:** A request for a definitive answer cannot override a failed required truth gate.
- **Expect:** Honor the conflict rule and preserve this invariant: Tie abstention scope to the failed requirement.
- **Reject:** Silently violating the stated precedence for Fail-Closed Abstention

## Failure Boundary

- **Given:** A conclusion cannot be committed while any indispensable evidence or integrity condition remains failed or unverifiable.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: no essential failed gate may be bypassed by fluency or confidence
- **Reject:** Claiming a successful Fail-Closed Abstention result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** no essential failed gate may be bypassed by fluency or confidence
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** One indispensable truth gate is unverifiable while several optional checks pass.
- **Expect:** Withhold the affected conclusion and return only independently supported content.
- **Reject:** Majority voting that commits because more checks passed than failed.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
