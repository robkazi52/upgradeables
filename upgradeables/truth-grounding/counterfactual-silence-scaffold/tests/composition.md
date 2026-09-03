# Counterfactual Silence Scaffold — Behavioral Expectations

## Positive Activation

- **Given:** The output must remain factual and the missing cause invites speculation.
- **Expect:** Reports the chronology and marks cause as undetermined. Result: A factual summary with an explicit evidence gap.
- **Reject:** Omitting the mechanism or instead doing this: Add what might have happened if a different operator acted.

## Negative Activation

- **Given:** the task explicitly requests scenarios, hypotheses, or counterfactual analysis
- **Expect:** Remain inactive; do not begin the package-specific first step: Confirm that the task contract excludes hypothetical reasoning.
- **Reject:** Activating Counterfactual Silence Scaffold solely because its name appears relevant

## Precedence Or Conflict

- **Given:** An explicit user request for counterfactual analysis deactivates this scaffold and activates counterfactual integrity instead.
- **Expect:** Honor the conflict rule and preserve this invariant: Tie activation to an explicit factual-only boundary.
- **Reject:** Silently violating the stated precedence for Counterfactual Silence Scaffold

## Failure Boundary

- **Given:** If factual and counterfactual propositions cannot be distinguished reliably, request review rather than deleting uncertain content wholesale.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: unauthorized hypothetical premises must not enter factual output
- **Reject:** Claiming a successful Counterfactual Silence Scaffold result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** unauthorized hypothetical premises must not enter factual output
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A factual extraction draft adds an unsupported what-if explanation for a missing event.
- **Expect:** Remove the imagined explanation while retaining the documented gap.
- **Reject:** Suppressing a source quotation merely because the quotation contains hypothetical language.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
