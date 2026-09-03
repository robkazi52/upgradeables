# Behavioral Evaluation Framework

This directory separates two kinds of evidence:

- **Static validation** checks schemas, package completeness, forbidden
  boilerplate, metadata/document agreement, and case structure in CI.
- **Narrow deterministic checks** exercise only lexical or schema properties
  they can honestly decide; the six fixtures run through
  `scripts/run_deterministic_package_checks.py`.
- **Behavioral model evaluation** runs cases against a real model through an
  adapter. It is opt-in and never runs in CI without an explicitly configured
  command.

Every operational package contains `tests/cases.json` with six provider-neutral
behavior specifications. `scripts/validate_behavior_cases.py` proves only that
those cases are complete and structurally valid. It does not prove that any
model passes them.

Adapters:

- `adapters/base.py` defines the minimal interface.
- `adapters/mock.py` supports harness development with declared canned output;
  mock results are not model results.
- `adapters/command.py` sends a prompt to an explicit local command over stdin.

Providers can add adapters without changing canonical Upgradeable semantics.
Store generated evaluation output under `evals/reports/` and identify the actual
model, adapter, date, parameters, and case set. Do not commit credentials.
