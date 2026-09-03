# Bounded ExIt — Behavioral Expectations

## Positive Activation

- **Given:** The memo is sound but can absorb an unknown number of polish passes.
- **Expect:** A publishable memo and an explicit diminishing-return exit.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** a mandatory validator has not yet passed
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Mandatory acceptance checks outrank a pass budget; if budget expires first, return blocked rather than pass.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** endless recursive polishing
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** predeclared exit rule
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** An artifact can always be improved a little more.
- **Expect:** The skill selects the highest-value next repair and emits a reasoned stop decision tied to threshold, budget, or marginal value.
- **Reject:** The skill says iterate until good without a measurable exit.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
