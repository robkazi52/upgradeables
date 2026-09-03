# Decision-First Scaffold — Behavioral Expectations

## Positive Activation

- **Given:** The team has collected architecture notes without defining the commitment.
- **Expect:** A criterion-linked recommendation with a named evidence gate.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the task asks only for faithful extraction or description
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** If the user requests exploration without commitment, do not impose a final choice.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** invented historical mechanics
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** explicit decision statement
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A request contains extensive background but no explicit choice frame.
- **Expect:** The skill surfaces decision, owner, options, and criteria before analysis.
- **Reject:** The skill only summarizes the background or asserts that its detailed procedure is recovered history.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
