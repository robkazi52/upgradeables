# Runtime Evaluation Harness

This harness compares `baseline`, `static-full`, and `adaptive-runtime` under
matched task, model, and generation settings. Core tests use only the built-in
mock adapter: no API key, paid call, model download, or network access is
performed automatically.

Run `upgradeables eval list-suites`, inspect a suite, then use
`upgradeables eval run synthetic-runtime-v1 --adapter mock`. Raw responses,
requests, condition labels, grader outputs, hashes, summaries, and the report
are written below `.evals/upgradeables/` unless another output root is supplied.

The mock output is plumbing evidence only. It is not evidence that runtime
middleware improves model behavior. See
[`docs/runtime/EVALUATION.md`](../../docs/runtime/EVALUATION.md) for the
experimental protocol.
