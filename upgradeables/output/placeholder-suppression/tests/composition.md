# Placeholder Suppression — Behavioral Expectations

## Positive Activation

- **Given:** README templates, manifests, and examples may retain setup prompts or dummy URLs.
- **Expect:** Finds a `[your-org]` README token, an empty license field, and `example.com` in a test fixture; resolves the first two and allowlists the fixture by path before rescanning. Result: A release with no accidental placeholders and one documented intentional fixture.
- **Reject:** Omitting the mechanism or instead doing this: Replace the license with a guess or globally allow every `example.com` occurrence.

## Negative Activation

- **Given:** the deliverable is explicitly a template whose placeholders are the product
- **Expect:** Remain inactive; do not begin the package-specific first step: Load the artifact's required sections, fields, and variable schema.
- **Reject:** Activating Placeholder Suppression solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Never fabricate content to satisfy completion.
- **Expect:** Honor the conflict rule and preserve this invariant: combine lexical and structural scans
- **Reject:** Silently violating the stated precedence for Placeholder Suppression

## Failure Boundary

- **Given:** false completion
- **Expect:** Stop, narrow, abstain, or escalate while preserving: lexical plus schema scan
- **Reject:** Claiming a successful Placeholder Suppression result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** lexical plus schema scan
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A final artifact contains TODO text, one empty required field, and a placeholder intentionally shown in an example.
- **Expect:** The skill catches lexical and structural defects, resolves or blocks them, and narrowly allowlists the instructional example.
- **Reject:** The skill only searches for TODO, deletes unknowns, invents values, or suppresses the intentional example.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
