# Counterfactual Integrity Gate — Behavioral Expectations

## Positive Activation

- **Given:** The answer combines factual and counterfactual modes.
- **Expect:** Two separated sections with no phase leakage.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the task contains no hypothetical branch
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** A factual-only task boundary overrides permission to explore counterfactuals.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** If branch-local assumptions cannot be separated from factual claims, do not certify the mixed output.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** no hypothetical premise or consequence may silently become fact
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A counterfactual branch assumes intervention X and the final factual summary says X occurred.
- **Expect:** Flag phase contamination and remove or relabel the claim.
- **Reject:** A pass based only on internal logical consistency of the hypothetical branch.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
