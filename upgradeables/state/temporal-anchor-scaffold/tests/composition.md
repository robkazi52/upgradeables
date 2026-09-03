# Temporal Anchor Scaffold — Behavioral Expectations

## Positive Activation

- **Given:** Publication date, effective date, and incident time differ.
- **Expect:** Builds a temporary typed timeline, flags the ambiguity, and tests applicability windows. Result: The applicable version is identified with an explicit uncertainty branch.
- **Reject:** Omitting the mechanism or instead doing this: It does not equate publication with effectiveness or guess the relative date.

## Negative Activation

- **Given:** time has no bearing on the answer
- **Expect:** Remain inactive; do not begin the package-specific first step: Identify which temporal distinctions affect the decision.
- **Reject:** Activating Temporal Anchor Scaffold solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Source-stated timestamps outrank inferred order; higher-authority corrections supersede earlier dates while retaining history.
- **Expect:** Honor the conflict rule and preserve this invariant: distinguish event, publication, observation, and effective time
- **Reject:** Silently violating the stated precedence for Temporal Anchor Scaffold

## Failure Boundary

- **Given:** Do not assert total order from partial temporal evidence.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: time-type distinction
- **Reject:** Claiming a successful Temporal Anchor Scaffold result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** time-type distinction
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** Sources provide event, publication, and effective dates plus one unknown ordering relation.
- **Expect:** Keep time types separate, preserve the unknown relation, and retire the task-local timeline after validation.
- **Reject:** Sort all dates into one confident chronology and retain it as permanent truth.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
