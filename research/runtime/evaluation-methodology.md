# Runtime evaluation methodology

Status: research and implementation guidance for v0.4
Sources checked: 2026-09-03

## Decision summary

The v0.4 harness should be a randomized, blocked, paired experiment over a
fixed task set. For each model and task, run the same ordinary host
instructions, task input, adapter, and generation parameters under four
conditions:

1. `baseline`: no Upgradeables runtime layer;
2. `static-full`: one useful, broad, non-adaptive Upgradeables-style layer;
3. `adaptive-fixed-resolution`: compile a saved, validated per-task
   `TaskResolution` so selection is held fixed;
4. `adaptive-end-to-end`: resolve the raw task with v0.3 and compile the
   task-specific `RuntimePlan` with v0.4.

Pre-declare comparisons according to the research question. Fixed-resolution
minus baseline estimates the directive/runtime association with saved selection;
end-to-end minus fixed-resolution describes the contribution associated with a
different TaskResolution source; end-to-end minus baseline describes the total
product association. These decompositions are descriptive, not proof of a causal
mechanism. Repeated generations measure response variability; they do not turn
one task into several independent tasks. Aggregate trials within each task,
compute task-level paired deltas, and report uncertainty across tasks.

Prefer deterministic task-specific graders. Preserve every request, response,
grader result, error, and provenance field before producing summaries. Human or
model judges are fallbacks, never silent substitutes for ground truth. CI uses
mocks only, and network/model execution is always an explicit user action.

This design follows several well-supported principles:

- OpenAI's current evaluation guidance recommends task-specific tests, logging,
  automation where possible, human calibration, and pairwise/pass-fail judgments
  rather than unconstrained grading when model graders are needed
  ([Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)).
- HELM emphasizes standardized conditions, multiple metrics, and public raw
  prompts/completions for transparent evaluation
  ([HELM paper](https://openreview.net/forum?id=iO4LZibEqW),
  [HELM project](https://crfm.stanford.edu/helm/)).
- NIST recommends blocking controllable nuisance factors and randomizing the
  rest; here the task is the main block and execution order is randomized within
  it
  ([NIST randomized-block design](https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm)).
- NIST's paired-observation guidance supports estimating within-unit differences
  rather than comparing unrelated aggregate means
  ([NIST paired confidence intervals](https://itl.nist.gov/div898/handbook/prc/section3/prc312.htm)).

## What the experiment can and cannot establish

The treatment is the Upgradeables runtime layer, not the whole host application.
The experiment can estimate whether a particular compiler/runtime version changes
measured performance or overhead for a named model snapshot on a named task
suite. It cannot by itself establish that:

- adaptive directives improve all models or all tasks;
- a smaller model has become equivalent to a larger model;
- observed benchmark performance transfers to production;
- a public benchmark was absent from model training data;
- a seed makes model inference deterministic;
- a model-judge score is ground truth.

NIST specifically cautions that laboratory benchmarks may not extrapolate to
real-world contexts and that prompt sensitivity increases this gap
([NIST AI 600-1, Appendix A.1.4](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)).
Reports therefore need scoped claims: model snapshot, suite version, conditions,
date, sample size, and observed uncertainty.

## Freeze the protocol before inference

The manifest's run-contract and configuration fields are immutable after the
first real response is accepted. The sole mutable progress field is
`request_count_completed`; the runner durably rewrites it after each recorded
adapter invocation and excludes it from the immutable manifest-hash scope.
Corrections to any run-contract field create a new manifest/version; they do
not rewrite the old run contract. At minimum, pre-declare:

- experiment ID and hypothesis;
- primary and secondary comparisons;
- suite slug/version and exact ordered task IDs;
- development, validation, or held-out status;
- included/excluded task rules;
- conditions and the version/hash of each condition constructor;
- adapter, endpoint type, model identifier, and model snapshot/digest when
  available;
- host/base instruction hash and user-input construction version;
- generation parameters, timeout, retry policy, and supported seed policy;
- trials per task and planned task count;
- deterministic order-schedule seed;
- primary metric, family-level metrics, and overhead metrics;
- grader slugs/versions/hashes and precedence;
- analysis version, confidence level, and multiplicity policy;
- failure and missing-data policy;
- output directory and data-retention policy;
- network/cost authorization mode.

Pre-declaration prevents results from silently changing the question. NIST notes
that contrasts chosen after inspecting results do not retain their nominal
confidence properties and that multiple comparisons alter overall confidence
([NIST multiple comparisons](https://www.itl.nist.gov/div898/handbook/prc/section4/prc47.htm)).

Do not stop early because a preferred condition is winning. A user may abort for
cost, time, or safety, but the report must mark the run incomplete and retain the
partial artifacts. Any data-dependent follow-up is exploratory and gets a new
manifest.

## Conditions and fairness invariants

### Canonical condition definitions

`baseline` contains only the host's normal base/safety instructions, the user
task, and its inputs. Do not weaken ordinary safety or remove host behavior to
make the baseline worse.

`static-full` adds a versioned, reasonable broad directive bundle. It must not
inspect the task, `TaskResolution`, selected components, failure modes, or
runtime plan. It should be genuinely usable, bounded, and frozen before
confirmatory testing—not an intentionally bloated straw comparator.

`adaptive-fixed-resolution` adds runtime channels compiled from the suite's
versioned, validated, hash-preserved fixed `TaskResolution`. A missing or stale
resolution is unsupported and must never silently fall back to live selection.

`adaptive-end-to-end` runs the v0.3 resolver on the raw user task, then passes
that resolution through the same v0.4 compiler, model profile, host-capability,
and budget path used by the fixed condition. Persist the resulting
`TaskResolution` hash, structured `RuntimePlan`, and exact instruction block.

`adaptive-runtime` is a compatibility alias for `adaptive-end-to-end`. New
manifests and reports use the canonical name; supplying both labels in one run
is an error because they are the same condition.

### Hold everything else equal

Within a model experiment, the following must match across conditions unless the
manifest explicitly defines an adapter-mandated exception:

- model snapshot/digest;
- host/base instructions;
- user content and attachments;
- tool declarations and tool implementation;
- generation parameters and output limits;
- context truncation policy;
- adapter version, chat template, and endpoint;
- timeout, retry, and error classification;
- grader and analysis version.

Runtime directive tokens are intentionally different and must be counted
separately. If adding directives causes different truncation, that is a treatment
effect worth reporting, but the record must expose it (`input_truncated`, token
counts, and effective-context hash).

Do not let one condition reuse another condition's model response. Request
caching may cache only exact, fully rendered request hashes and should be disabled
for confirmatory repeated-trial runs unless cache behavior itself is under test.

## Blocking, order, and repeated trials

Treat each task as a block. Each task receives every requested condition the same
number of times. Generate the order schedule before inference from a recorded
runner seed.

For the requested conditions, construct all condition-order permutations,
shuffle that permutation list with the recorded schedule seed, and cycle
through it across task/trial blocks. The standard four-condition experiment
therefore balances permutations of `baseline`, `static-full`,
`adaptive-fixed-resolution`, and `adaptive-end-to-end`; a complete cycle has 24
orders. Partial cycles remain deterministic and should be reported as such.
This balances warm caches, server load, thermal throttling, rate limits, and
temporal provider drift more fairly than running all baselines first. If
concurrency is enabled, assign all conditions the same concurrency policy and
record dispatch and completion timestamps.

Repeated trials are required when generation can vary. Five trials per
task/condition is a reasonable initial manifest default, not a universal sample
size claim. Even at temperature zero, preserve repeated-trial support because
provider internals and hardware kernels may vary. Record a generation seed only
when accepted by the endpoint, plus whether the provider claims to honor it. Do
not equate a recorded seed with byte-identical inference.

The independent unit for generalizing over a fixed suite is the task, not the
individual generation. Trials are nested within task and condition. For the
simple v0.4 analysis:

1. grade every trial;
2. average (or otherwise pre-declared aggregate) trials within task/condition;
3. subtract condition aggregates within the same task;
4. summarize those task-level paired deltas.

Also publish trial-level outcomes and within-task variability. This avoids
pseudo-replication while still showing model instability.

## Grader hierarchy

Use the most objective grader that captures the success criterion. Every grader
returns a typed result with `grader_kind` equal to `deterministic`,
`human-declared`, or `model-judge`.

### 1. Deterministic graders (default)

Examples by task family:

| Family | Preferred checks |
| --- | --- |
| Structured output | Parse success, JSON Schema validation, exact keys/types, forbidden text absent |
| Constraint following | Exact preservation of protected values, regex/AST predicates, word/count limits |
| Coding/editing | Tests, API invariants, expected defect repaired, forbidden paths unchanged, diff scope |
| Source grounding | Claim/reference mapping to supplied source IDs, exact quote spans, unsupported-fact sentinels |
| Citation fidelity | Citation IDs exist and point to the required source segment |
| Debugging | Reproducer fails before and passes after; regression tests pass |
| Stopping/overwork | No forbidden tool/edit, changed-file count, unnecessary step/tool counters |
| Alternative hypothesis | Final observable answer/action correct; rival hypothesis check present only if externally observable and rubric-required |

Deterministic does not mean infallible. Version grader code and fixtures, test it
with known passing/failing outputs, and preserve its stdout/stderr and exception.
Code execution must use a disposable, resource-limited sandbox with no network by
default. Never grade hidden chain of thought; grade final answers, tool events,
and externally visible artifacts.

### 2. Human grading (when semantics require it)

Write the rubric and examples before collecting judgments. Present outputs with
condition names, model identity, runtime text, task order, and filenames removed.
Randomize candidate labels. Give graders a `tie`/`both fail` path where suitable.
Use at least two graders for confirmatory subjective subsets when practical;
retain each raw judgment, adjudication, disagreement, and rubric version rather
than overwriting them with consensus.

Calibrate on a shared pilot subset and report agreement. Human labels should not
be treated as perfectly objective: the Chatbot Arena study used blind expert
review and found meaningful disagreement even among experts
([Chatbot Arena paper](https://arxiv.org/abs/2403.04132)).

### 3. Model judges (optional and non-authoritative)

Model judging is disabled in offline/default runs. If explicitly enabled:

- store the exact judge model snapshot, prompt, parameters, response, and parsed
  verdict;
- blind model/condition identities and remove treatment-revealing metadata;
- prefer pairwise or pass/fail decisions against a specific rubric;
- judge each pair in both A/B and B/A order;
- treat an order-dependent winner as `inconsistent` (normally a tie for the
  headline comparison) and report the inconsistency rate;
- allow ties and both-bad outcomes;
- validate judge agreement against a human-labeled sample;
- keep judge scores separate from deterministic and human-declared scores.

Pairwise model judges exhibit position bias, and the bias varies by judge and
task; swapped-order testing is therefore a required diagnostic, not polish
([systematic position-bias study](https://arxiv.org/abs/2406.07791)). OpenAI's
current guidance likewise identifies position and verbosity bias and recommends
pairwise/pass-fail grading plus human calibration
([Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)).

## Metrics

### Primary outcomes

Declare exactly one primary metric per suite. Prefer a task success value in
`[0, 1]` derived from the deterministic success contract. Keep component metrics
rather than collapsing away failure modes:

- exact/objective score;
- constraint adherence;
- unsupported-claim count/rate;
- citation fidelity;
- forbidden action rate;
- repair/test success;
- edit scope;
- tool error rate;
- appropriate abstention.

Report macro averages over tasks so tasks with more assertions or trials do not
silently dominate. A suite can also publish a pre-declared weighted aggregate,
but it must publish the weights and unweighted result.

### Overhead and efficiency

Capture per request where the adapter supplies it:

- host/base input tokens;
- runtime directive tokens;
- total input and output tokens;
- wall-clock latency and, when exposed, queue/prompt/eval durations;
- tool call count and tool error count;
- actual billed usage and currency;
- provider request ID.

Use `null` plus an availability reason for missing metrics. Never estimate a
provider's token usage from characters while labeling it actual. Never invent a
dollar cost for a local model. Optional local measurements may report elapsed
time, energy, or hardware utilization with the measurement method.

Two useful descriptive secondary metrics are:

```text
score_gain_per_1k_runtime_tokens =
    (score_treatment - score_comparator) /
    (runtime_tokens_treatment - runtime_tokens_comparator) * 1000

gap_closed_fraction =
    (adaptive_small - baseline_small) /
    (baseline_large - baseline_small)
```

Only compute the second for the identical suite, scoring protocol, and compatible
model conditions when the denominator is positive. Label both descriptive; do
not call either an intelligence gain.

## Statistical analysis

### Default report

For every predeclared contrast, including the standard
`adaptive-fixed-resolution - baseline`,
`adaptive-end-to-end - adaptive-fixed-resolution`, and
`adaptive-end-to-end - baseline` contrasts, publish:

- number of planned and completed tasks;
- trials requested/completed/failed per condition;
- condition success rates or mean objective scores;
- mean and median task-level paired delta;
- count of improved/tied/regressed tasks;
- a two-sided 95% confidence interval for the mean paired delta when justified;
- per-family paired deltas;
- raw per-task and per-trial values;
- error, timeout, refusal, and missing-result counts;
- token and latency deltas.

Use a task-level paired bootstrap for the default interval: resample tasks with
replacement, retaining all conditions and trials for a selected task as one
cluster, and recompute the complete statistic. Record bootstrap algorithm,
iterations, and RNG seed. For very small suites, emphasize the raw deltas and
label intervals unstable; do not present asymptotic precision as certainty.
NIST's confidence-interval guidance stresses that interval width reflects sample
size and uncertainty
([NIST confidence intervals](https://www.itl.nist.gov/div898/handbook/prc/section1/prc14.htm)).

For paired binary outcomes with one aggregate outcome per task, an exact paired
test may be added, but effect size and interval remain primary. With repeated
trials, do not apply a simple unpaired proportion test to all generations. A
future hierarchical model may explicitly model task/trial effects; v0.4 should
not pretend independence.

### Multiple comparisons and exploratory work

The manifest must name its confirmatory primary contrast before inference; the
methodology does not assign one implicitly. Other named contrasts, family
breakdowns, model-size comparisons, micro/standard/full, and component
ablations are secondary or exploratory unless the manifest predeclares them
otherwise. Publish all planned comparisons and negative results. If inferential
claims are made over many comparisons, apply a declared correction or clearly
label unadjusted intervals exploratory. Do not report only the winning family,
model, directive level, or seed.

### Missingness and failures

Define failure handling before the run:

- model/adapter error: failed trial, not a silently dropped observation;
- invalid output: grade as failure if validity is part of the task;
- grader crash: `ungraded` with error artifact, never zero by accident;
- task fixture failure across all conditions: mark task invalid and report its
  exclusion for every condition;
- user cancellation: incomplete experiment;
- provider outage/rate limit: retain attempt records and follow the fixed retry
  policy equally across conditions.

Publish both intent-to-evaluate counts (all scheduled tasks) and successfully
graded counts. A sensitivity table may show alternate treatment of infrastructure
errors, but it cannot replace the pre-declared primary policy.

## Leakage, contamination, and held-out evidence

Separate suites structurally:

- `development`: visible and reusable for compiler/grader iteration;
- `validation`: used for bounded selection among frozen candidates;
- `held-out-confirmatory`: not inspected or tuned against until compiler,
  static-full bundle, grader, and analysis are frozen.

After a held-out suite is used to change directives, it becomes development
evidence for later work. New confirmatory claims require a new held-out suite.
Public benchmark exposure cannot be ruled out for opaque models; label it
`contamination_unknown`. Research documents that benchmark test-set exposure can
invalidate classical evaluation assumptions
([contamination position paper](https://arxiv.org/abs/2310.18018),
[black-box contamination study](https://proceedings.iclr.cc/paper_files/paper/2024/file/46e624c244cff669223d488defd4e835-Paper-Conference.pdf)).

Prevent experiment-induced prompt leakage:

- never send reference answers, grader rules, condition labels, grader-only
  expected outcomes/failure annotations, or competing responses to the
  generation model;
- ensure task-visible source snippets are explicitly part of all conditions;
- scan compiled and static directives for task answers/canary strings;
- render each condition from the same immutable task input;
- keep grader execution and model generation in separate interfaces;
- hash the exact rendered request and store a redacted inspection form;
- never include previous conditions' output in later condition context.

Synthetic tasks should use generated fixtures and private/randomized instance
values where possible, with the generator version and seed recorded. Synthetic
does not automatically mean representative; report task-family coverage and what
the suite omits.

## Artifact and provenance contract

Store one append-only experiment directory:

```text
.evals/upgradeables/<experiment-id>/
|-- manifest.json
|-- schedule.json
|-- tasks/
|-- requests/
|-- responses/
|-- graders/
|-- results.jsonl
|-- summary.json
|-- report.md
`-- checksums.sha256
```

Write raw request/response/grader artifacts before summary generation. Never
overwrite a raw artifact; retries get distinct attempt IDs. Exclude credentials,
authorization headers, and unrelated private environment data. If task data
cannot safely be retained, record a stable task ID/hash and explicit retention
limitation rather than claiming full reproducibility.

Each trial record should contain at least:

```text
schema_version
experiment_id, run_id, task_id, task_family, task_version
condition, trial_index, schedule_index, attempt_index
repository_commit, harness_version, registry_version, compiler_version
task_definition_hash, task_resolution_hash
runtime_plan_hash, compiled_instruction_hash, static_bundle_hash
host_instruction_hash, rendered_request_hash
adapter_slug/version, endpoint_type
model_requested, model_reported, model_snapshot_or_digest
generation_parameters, requested_seed, seed_support
dispatch/start/end timestamps, latency_ms
token/usage fields with source and availability
actual cost fields or null, never inferred local dollar cost
raw request path/hash, raw response path/hash
finish status, retry/error classification
grader slug/version/kind/hash, grader artifact path/hash
objective score, component scores, valid/invalid/ungraded status
```

Use canonical UTF-8 JSON with sorted keys and normalized line endings for hashes.
Hash task definitions, runtime plans, rendered instruction blocks, model config,
and grader definitions separately so two runs can diagnose where they differ.
Checksums prove artifact identity, not semantic correctness or model determinism.
HELM's publication of raw prompts and completions is a useful transparency model
for this design ([HELM paper](https://openreview.net/forum?id=iO4LZibEqW)).

## Offline and no-surprise execution policy

The safe default is construction and inspection, not inference:

- core CI runs compiler/adapters/graders against fixtures and mocks only;
- `eval list-suites`, `inspect-suite`, manifest validation, report generation,
  and `--dry-run` make no network calls;
- `--dry-run` prints exact tasks, conditions, trials, total planned requests,
  adapters, and which actions would need network or a local model;
- an API run requires an explicit network adapter and affirmative cost/network
  acknowledgement; merely having an API key is not authorization;
- an Ollama/local run uses only an already-installed model and fails with a
  preparation command if absent; it never invokes pull/download;
- externally hosted benchmark data is never auto-fetched; manifests contain task
  IDs, source URL, license notes, and manual fetch instructions;
- model-as-judge is off unless separately requested;
- reports distinguish `not_run`, `dry_run`, `mock`, `local`, and `api` evidence.

No paid calls, model downloads, benchmark downloads, or external writes should
occur during installation, import, tests, CI, suite listing, or dry-run. A CLI
must show expected request count before an explicit run. Actual pricing should be
captured from provider billing/usage metadata when available; external reports
also record price source and date.

## Minimum implementation checks

The harness is ready for post-PR experiments when automated tests demonstrate:

1. baseline excludes the Upgradeables runtime layer;
2. static-full is fixed across tasks and has a stable version/hash;
3. fixed-resolution and end-to-end modes use the same compiler path and preserve
   the exact `TaskResolution`/`RuntimePlan`/rendered-block hashes;
4. all conditions retain identical base task/model settings;
5. schedule generation is deterministic and condition order is balanced;
6. repeated trials remain nested under task IDs;
7. objective grader fixtures include known pass/fail/error cases;
8. grader failure produces `ungraded`, not success or zero;
9. invalid structured output follows the manifest's failure policy;
10. model-judge order swapping detects inconsistent preferences;
11. summaries derive only from immutable raw records;
12. task-level paired deltas match hand-calculated fixtures;
13. bootstrap resampling keeps all records for one task together;
14. incomplete and tiny-sample runs are labeled honestly;
15. all pre-declared comparisons, including negative results, appear in reports;
16. hashes change when task, runtime plan, instruction, model config, or grader
    changes and remain stable across line-ending differences;
17. retry attempts remain visible and are not double-counted;
18. `--dry-run` performs zero inference calls and reports request count;
19. CI and default commands perform no network request, model pull, or paid call;
20. reports never label a model-judge result as objective ground truth.

## Recommended first experiments

After the v0.4 PR is reviewed, begin with small, bounded runs:

1. one already-installed small local model on `constraint-following-v1`,
   `baseline` versus `adaptive-fixed-resolution`;
2. the same model on a tiny debugging suite across baseline, static-full,
   fixed-resolution, and end-to-end conditions;
3. a small and larger local model on the same frozen suite;
4. only with explicit authorization, small and larger API snapshots on one
   held-out suite;
5. micro/standard/full and component ablations only after the primary pipeline is
   validated.

Treat these as measurements, not demonstrations. A strong report states where
adaptive controls helped, tied, or hurt; the added directive tokens and latency;
the remaining gap; every limitation; and the exact artifacts needed to reproduce
the claim.
