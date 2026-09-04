# Runtime evaluation

The runtime evaluation harness compares instruction conditions under the same
task and model settings. Its purpose is to measure scoped behavior and overhead,
not to claim that middleware upgrades a model's intrinsic intelligence.

The implementation and bundled data live under
[evals/runtime](../../evals/runtime/). The research protocol is documented in
[evaluation methodology](../../research/runtime/evaluation-methodology.md).

## Current conditions and attribution

- `baseline`: task with no Upgradeables runtime instructions.
- `static-full`: task plus the fixed
  [static-full-v1](../../evals/runtime/static-full-v1.txt) bundle.
- `adaptive-fixed-resolution`: compile the checked-in, per-task v0.3
  `TaskResolution` without rerunning selection. A missing or stale fixed
  resolution fails before execution; it never falls back to live selection.
- `adaptive-end-to-end`: resolve the task with v0.3 and compile the v0.4 capsule
  during each observation.

`adaptive-runtime` remains a deprecated compatibility alias for
`adaptive-end-to-end`; manifests and observations record the canonical label.

An optional larger-model comparator is run as a separate baseline experiment;
`large-model-baseline` is not a core condition label accepted by the current
condition builder or CLI.

The fixed-resolution comparison isolates the runtime compiler more cleanly;
the end-to-end comparison also includes task-selection behavior. Differences
between those conditions are descriptive **Selection Attribution** evidence,
while fixed-resolution versus baseline/static-full is descriptive **Runtime
Attribution** evidence. Neither is causal without an appropriately powered,
predeclared design. A larger-model baseline, when separately integrated,
measures a remaining gap; it does not establish model equivalence.

## Bundled suite and graders

The bundled
[synthetic-runtime-v1 suite](../../evals/runtime/suites/synthetic-runtime-v1.json)
contains ten CC0 tasks covering constraint following, source grounding,
citation fidelity, local editing, debugging, review, state, alternative
hypotheses, structured output, and stopping.

Current objective graders support:

- exact text after trimming;
- case-insensitive contains-all and contains-any checks;
- excluded-string checks;
- exact expected JSON field values.

These tasks are useful for harness plumbing and small local experiments. They
are not a representative general capability benchmark.

## CLI

```bash
upgradeables eval list-suites
upgradeables eval inspect-suite synthetic-runtime-v1
upgradeables eval run synthetic-runtime-v1 --adapter mock --trials 1
upgradeables eval report .evals/upgradeables/synthetic-runtime-v1-mock
upgradeables eval compare .evals/upgradeables/run-a .evals/upgradeables/run-b
```

The mock remains the default and makes no network request. Preview a complete
Ollama experiment without contacting Ollama or creating an experiment:

```bash
upgradeables eval run synthetic-runtime-v1 \
  --adapter ollama \
  --model your-already-installed-model \
  --conditions baseline static-full adaptive-fixed-resolution adaptive-end-to-end \
  --trials 1 \
  --dry-run \
  --json
```

The preview validates the suite, conditions, model/endpoint configuration, and
fixed-resolution availability. It reports task IDs, trials, exact planned
request count, deterministic configuration hash, manifest preview, and
`estimated_cost` as unavailable rather than guessing.

Run that experiment only after reviewing the preview:

```bash
upgradeables eval run synthetic-runtime-v1 \
  --adapter ollama \
  --model your-already-installed-model \
  --endpoint http://127.0.0.1:11434 \
  --conditions baseline static-full adaptive-fixed-resolution adaptive-end-to-end \
  --trials 1 \
  --output-root .evals/upgradeables \
  --json
```

Before creating the experiment directory, a live Ollama run performs one
read-only model-availability preflight through the existing discovery helper.
It fails if the endpoint or exact model is unavailable. The preflight never
pulls or loads a missing model, and generation requests have no retry path.

For an explicitly selected OpenAI-compatible endpoint, put the credential in
an environment variable and pass only its name. For PowerShell:

```powershell
$env:UPGRADEABLES_EVAL_API_KEY = "your-key"
upgradeables eval run synthetic-runtime-v1 `
  --adapter openai-compatible `
  --model your-exact-model-id `
  --endpoint https://models.example/v1 `
  --api-key-env UPGRADEABLES_EVAL_API_KEY `
  --conditions baseline adaptive-fixed-resolution `
  --trials 1 `
  --dry-run `
  --json
```

Remove `--dry-run` only when the request count, endpoint, model, and possible
cost are accepted. OpenAI-compatible live evaluation performs no implicit
model discovery. `--timeout` controls each request; all live adapters are
non-streaming and make one attempt per scheduled observation.

`eval compare` returns the descriptive summaries for two experiment directories.
It does not claim the manifests are matched; verify model, task, and generation
settings before interpreting differences causally.

## Experiment execution

The runner requires an experiment ID, suite, conditions, model record, positive
trials per task, temperature, seed policy, and grader label. For each task and
trial it assigns a deterministic balanced condition permutation using
`order_seed`, builds the condition, invokes the selected adapter callback,
grades the raw string, and records hashes. Condition, adapter, and grader
failures remain typed ungraded observations rather than silently becoming task
failures or aborting later observations. Structured live-adapter observations
also preserve the redacted provider request/response, provider usage, measured
latency, response model ID, provider timing, finish reason, partial/truncated
flags, and normalized error.

The default CLI output root is `.evals/upgradeables/`. A new experiment directory
is created; an existing directory is not overwritten.

Current files are:

```text
manifest.json
raw-results.jsonl
summary.json
report.md
```

Each raw result records task/family, trial and condition order, the condition
request and request hash, approximate directive tokens, response text and its
hash, any redacted provider request and raw response, usage and latency,
observation status, attribution fields, and grader result. Results are appended
and flushed per observation. The manifest records the suite, configuration,
condition schedule, fixed-resolution, and immutable run-contract hashes.

## Reporting

The current summary reports observations, graded/ungraded counts, successes,
success rate, mean score, output size, directive overhead, status counts, and
task-level paired adaptive-minus-baseline/static-full deltas across repeated
trials. The report preserves limitations and points to raw results.

These are descriptive aggregate rates. Provider usage and latency are captured
per observation when available, but the current reporter does not yet compute
task-clustered confidence intervals, bootstrap uncertainty, verified monetary
cost, or every family-level paired statistic.
Use the fuller research protocol before making empirical claims.

## Protocol for real model experiments

An external adapter integration should freeze a manifest before inference and
hold model snapshot/digest, base instructions, user input, tools, generation
parameters, timeout/retry policy, grader, and truncation policy constant across
conditions. Repeat trials, balance condition order within task, and treat the
task—not each generation—as the independent unit for suite-level inference.

Prefer deterministic task-specific graders. When human grading is needed,
define the rubric first, blind condition/model identity where practical, retain
individual judgments and disagreement, and permit ties/both-fail. Model judges
are optional and non-authoritative; preserve their exact prompt/model/output and
test response-order bias.

Capture actual provider tokens, latency, and cost only when exposed. Use `null`
with an availability reason otherwise. Do not label the character-based runtime
estimate as provider token usage or invent local-model dollar cost.

## Leakage and tuning discipline

- Never send expected answers, grader rules, condition names, or competing
  outputs to the generation model.
- Keep development, validation, and held-out confirmatory suites separate.
- Once a held-out suite changes directives, treat it as development evidence.
- Version and hash changed tasks, graders, static bundles, and runtime wording.
- Report null, adverse, failed, refused, and incomplete results.
- Do not select only favorable models, task families, trials, or seeds.

## Safety and cost

Core tests and dry-runs use mocks/fake transports and make no network call, paid
request, or model download. Live local/remote evaluation requires an explicit
adapter, exact model, reviewed request count, and caller-selected endpoint.
Never pull a local model or spend API credits automatically.

The experiment schema is
[EXPERIMENT_SCHEMA.json](../../evals/runtime/schemas/EXPERIMENT_SCHEMA.json), and
the reporting starting point for small/large comparisons is the
[Capability Gap template](../../evals/runtime/reports/CAPABILITY_GAP_TEMPLATE.md).

## Claims

Acceptable conclusions name the exact model, snapshot/digest, suite, compiler,
conditions, task and trial counts, effect, overhead, and limitations. Also report
where adaptive runtime did nothing or hurt.

Do not use phrases such as “turns a small model into a frontier model,”
“intelligence boost,” or “model equivalence” unless a separately justified,
carefully scoped protocol actually supports that statement. The current mock
results never support it.
