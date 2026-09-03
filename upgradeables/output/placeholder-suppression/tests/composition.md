# Placeholder Suppression — Behavioral Expectations

## Positive Activation

- **Given:** README templates, manifests, and examples may retain setup prompts or dummy URLs.
- **Expect:** A release with no accidental placeholders and one documented intentional fixture.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the deliverable is explicitly a template whose placeholders are the product
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Never fabricate content to satisfy completion.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** false completion
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** lexical plus schema scan
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A final artifact contains TODO text, one empty required field, and a placeholder intentionally shown in an example.
- **Expect:** The skill catches lexical and structural defects, resolves or blocks them, and narrowly allowlists the instructional example.
- **Reject:** The skill only searches for TODO, deletes unknowns, invents values, or suppresses the intentional example.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
