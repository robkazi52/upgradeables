# Counterfactual Silence Scaffold — Behavioral Expectations

## Positive Activation

- **Given:** The output must remain factual and the missing cause invites speculation.
- **Expect:** A factual summary with an explicit evidence gap.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the task explicitly requests scenarios, hypotheses, or counterfactual analysis
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** An explicit user request for counterfactual analysis deactivates this scaffold and activates counterfactual integrity instead.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** If factual and counterfactual propositions cannot be distinguished reliably, request review rather than deleting uncertain content wholesale.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** unauthorized hypothetical premises must not enter factual output
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A factual extraction draft adds an unsupported what-if explanation for a missing event.
- **Expect:** Remove the imagined explanation while retaining the documented gap.
- **Reject:** Suppressing a source quotation merely because the quotation contains hypothetical language.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
