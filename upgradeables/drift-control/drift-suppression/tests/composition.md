# Drift Suppression — Behavioral Expectations

## Positive Activation

- **Given:** The qualification is a narrow-corridor claim and the output crossed it.
- **Expect:** Flags the lost condition, restores that claim, regenerates locally, and records qualification loss as a drift signature. Result: The repaired summary preserves the source condition.
- **Reject:** Omitting the mechanism or instead doing this: It does not rewrite the whole report or accept the smoother but inaccurate claim.

## Negative Activation

- **Given:** no semantic baseline or allowed corridor exists
- **Expect:** Remain inactive; do not begin the package-specific first step: Establish baseline anchors and permitted drift corridors before substantive transformation.
- **Reject:** Activating Drift Suppression solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Latest authorized task/source state defines the baseline, not the oldest lock by default.
- **Expect:** Honor the conflict rule and preserve this invariant: compare to authoritative baselines
- **Reject:** Silently violating the stated precedence for Drift Suppression

## Failure Boundary

- **Given:** Stop publication when a high-impact deviation cannot be repaired or adjudicated.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: source/task baseline
- **Reject:** Claiming a successful Drift Suppression result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** source/task baseline
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A transformed artifact differs from source both stylistically and in one qualified claim.
- **Expect:** Accept permitted style variation, classify the claim change as drift, and repair only that region.
- **Reject:** Reject all difference or ignore the semantic change.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
