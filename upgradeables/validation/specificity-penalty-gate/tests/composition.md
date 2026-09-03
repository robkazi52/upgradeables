# Specificity Penalty Gate — Behavioral Expectations

## Positive Activation

- **Given:** Observation time does not establish exact onset time or cause.
- **Expect:** Changes the claim to 'observed by 14:32' and keeps the causal explanation provisional. Result: The response retains useful evidence while removing unsupported temporal and causal precision.
- **Reject:** Omitting the mechanism or instead doing this: Invent a 14:31–14:32 onset interval or delete the verified timestamp.

## Negative Activation

- **Given:** exact values are directly provided and verified
- **Expect:** Remain inactive; do not begin the package-specific first step: Identify all atoms whose precision materially narrows the claim.
- **Reject:** Activating Specificity Penalty Gate solely because its name appears relevant

## Precedence Or Conflict

- **Given:** A verified decision-critical exact atom is not penalized merely for being specific.
- **Expect:** Honor the conflict rule and preserve this invariant: Penalize precision mismatch rather than detail itself.
- **Reject:** Silently violating the stated precedence for Specificity Penalty Gate

## Failure Boundary

- **Given:** Do not release a material exact claim when the available evidence supports only a broader range, class, or uncertainty state.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: support-versus-resolution comparison for generated dates, numbers, causes, and identities
- **Reject:** Claiming a successful Specificity Penalty Gate result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** support-versus-resolution comparison for generated dates, numbers, causes, and identities
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** Evidence establishes that an event occurred in early May, but the draft says May 3 at 09:00.
- **Expect:** Require a source for the exact time or generalize to early May.
- **Reject:** Keep the timestamp because specificity sounds authoritative.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
