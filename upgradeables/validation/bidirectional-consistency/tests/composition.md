# Bidirectional Consistency — Behavioral Expectations

## Positive Activation

- **Given:** The code-to-requirement story may be plausible without every criterion actually being entailed.
- **Expect:** Maps criteria to behavior, then reconstructs satisfied criteria from observed behavior alone. Result: One missing error-handling criterion is found despite a plausible forward explanation.
- **Reject:** Omitting the mechanism or instead doing this: Count a criterion as satisfied because the PR description repeats it.

## Negative Activation

- **Given:** the transformation is intentionally irreversible and no reverse contract is claimed
- **Expect:** Remain inactive; do not begin the package-specific first step: Lock the source atoms and declared transformation contract.
- **Reject:** Activating Bidirectional Consistency solely because its name appears relevant

## Precedence Or Conflict

- **Given:** The declared transformation contract determines which information may be lost.
- **Expect:** Honor the conflict rule and preserve this invariant: Keep forward and reverse judgments separately inspectable.
- **Reject:** Silently violating the stated precedence for Bidirectional Consistency

## Failure Boundary

- **Given:** Do not certify when a material source constraint has no forward image or when the result implies a contradictory source condition.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: independent backward reconstruction for lossy or high-stakes transformations
- **Reject:** Claiming a successful Bidirectional Consistency result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** independent backward reconstruction for lossy or high-stakes transformations
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A summary reads plausibly from a report but, read alone, implies the opposite scope limitation.
- **Expect:** Fail the reverse pass and identify the scope inversion.
- **Reject:** Pass solely because every report section was mentioned.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
