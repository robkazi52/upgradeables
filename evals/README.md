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

Run a selected case through a local model command and write a raw, initially
unscored report:

```bash
python scripts/run_behavioral_evals.py --adapter command \
  --command "your-model-cli --flag" --model "exact-model-build" \
  --package grounding-no-invention --max-cases 1 \
  --parameters '{"temperature": 0}' --output evals/reports/local-run.json
```

For harness development, `--adapter mock --allow-mock --model mock` is available.
Mock reports are labeled `mock-not-evidence`. Optional human judgments are a JSON
object keyed by case ID; each value must contain an `outcome` of `pass`, `fail`,
or `uncertain` and may include notes.

Providers can add adapters without changing canonical Upgradeable semantics.
Store generated evaluation output under `evals/reports/` and identify the actual
model, adapter, date, parameters, and case set. Do not commit credentials. The
runner records raw outputs and optional declared judgments; it does not infer a
pass from lexical overlap and does not make model-quality claims automatically.
