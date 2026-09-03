# Counterfactual Integrity Gate — Behavioral Expectations

## Positive Activation

- **Given:** The answer combines factual and counterfactual modes.
- **Expect:** Keeps the current rule factual and reports projected effects under a labeled hypothetical branch. Result: Two separated sections with no phase leakage.
- **Reject:** Omitting the mechanism or instead doing this: State that the threshold was actually changed.

## Negative Activation

- **Given:** the task contains no hypothetical branch
- **Expect:** Remain inactive; do not begin the package-specific first step: Declare the factual baseline and the allowed counterfactual question.
- **Reject:** Activating Counterfactual Integrity Gate solely because its name appears relevant

## Precedence Or Conflict

- **Given:** A factual-only task boundary overrides permission to explore counterfactuals.
- **Expect:** Honor the conflict rule and preserve this invariant: Preserve the original factual baseline.
- **Reject:** Silently violating the stated precedence for Counterfactual Integrity Gate

## Failure Boundary

- **Given:** If branch-local assumptions cannot be separated from factual claims, do not certify the mixed output.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: no hypothetical premise or consequence may silently become fact
- **Reject:** Claiming a successful Counterfactual Integrity Gate result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** no hypothetical premise or consequence may silently become fact
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A counterfactual branch assumes intervention X and the final factual summary says X occurred.
- **Expect:** Flag phase contamination and remove or relabel the claim.
- **Reject:** A pass based only on internal logical consistency of the hypothetical branch.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
