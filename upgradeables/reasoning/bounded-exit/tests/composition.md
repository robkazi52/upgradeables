# Bounded ExIt — Behavioral Expectations

## Positive Activation

- **Given:** The memo is sound but can absorb an unknown number of polish passes.
- **Expect:** Repairs the unclear paragraph, rechecks the criteria, and exits because the remaining style gain is below its review cost. Result: A publishable memo and an explicit diminishing-return exit.
- **Reject:** Omitting the mechanism or instead doing this: Rewrite the whole memo or continue polishing synonyms after acceptance.

## Negative Activation

- **Given:** a mandatory validator has not yet passed
- **Expect:** Remain inactive; do not begin the package-specific first step: Lock acceptance criteria and a maximum pass or cost budget.
- **Reject:** Activating Bounded ExIt solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Mandatory acceptance checks outrank a pass budget; if budget expires first, return blocked rather than pass.
- **Expect:** Honor the conflict rule and preserve this invariant: define the exit condition before iterating
- **Reject:** Silently violating the stated precedence for Bounded ExIt

## Failure Boundary

- **Given:** endless recursive polishing
- **Expect:** Stop, narrow, abstain, or escalate while preserving: predeclared exit rule
- **Reject:** Claiming a successful Bounded ExIt result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** predeclared exit rule
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** An artifact can always be improved a little more.
- **Expect:** The skill selects the highest-value next repair and emits a reasoned stop decision tied to threshold, budget, or marginal value.
- **Reject:** The skill says iterate until good without a measurable exit.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
