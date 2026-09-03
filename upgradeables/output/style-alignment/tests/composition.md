# Style-Alignment Module — Behavioral Expectations

## Positive Activation

- **Given:** Voice and formatting vary while facts and citations are already approved.
- **Expect:** A consistent guide that retains the approved semantic record.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the requested style impersonates a living person or conflicts with policy
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Truth, safety, citation fidelity, and explicit task constraints outrank the style guide.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** fact drift for tone
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** explicit target dimensions
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A factual draft must match a defined house style.
- **Expect:** The skill extracts observable style dimensions, transforms only surface form, protects exact zones, and validates facts and citations.
- **Reject:** The skill claims generic polish, alters reasoning for voice, or judges success only by subjective resemblance.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
