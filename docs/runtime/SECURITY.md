# Runtime security and privacy

The safe default is local compilation only. Resolving a task, loading installed
runtime data, compiling a plan, and rendering text require no network and no API
key. Network activity begins only when application code explicitly invokes a
network adapter with a caller-selected endpoint.

## Trust boundaries

Treat these as separate trust decisions:

1. task and project data admitted to v0.3 resolution;
2. saved `TaskResolution` data admitted through `--resolution`;
3. runtime representations installed with the package;
4. host instructions and capabilities supplied by the application;
5. endpoint, model, credentials, and request body supplied to an adapter;
6. provider response and tool output;
7. run/evaluation artifacts written to disk.

A valid JSON shape is not proof that content is trustworthy. In particular,
`hard_restrictions` from a saved resolution become instruction text. Use
resolver-produced files from a trusted workspace and review externally supplied
resolutions before compilation.

## Endpoint choice and data movement

The Ollama and OpenAI-compatible helpers accept arbitrary endpoint strings.
They classify endpoint locality conservatively for reporting, but do not
enforce loopback, TLS, or an allowlist. The caller must verify the destination
before passing task or project data.

`upgradeables run ollama --dry-run` performs no network request and writes no
artifacts. A live `upgradeables run ollama` call contacts only the endpoint the
caller supplies; it performs no discovery, model pull, or automatic retry.

Live evaluation applies a narrower endpoint-origin policy: HTTP(S) only, no
embedded credentials, query, fragment, or arbitrary API path, and HTTPS for a
remote origin. Loopback/private HTTP remains available for local servers.
`upgradeables eval run --dry-run` performs no network request and writes no
experiment. A non-dry Ollama evaluation performs read-only exact-model
preflight before creating its experiment directory; OpenAI-compatible
evaluation performs no implicit discovery. Neither path retries or downloads.

The adapters do not upload a checkout automatically. They send only the strings
and options placed in the constructed request. Do not add source files,
`.upgradeables` history, environment data, or attachments unless the user has
explicitly selected that endpoint and task input.

No helper pulls models, edits a Modelfile, installs a provider, or retries a
partial streamed response automatically.

## Credentials

Pass credentials at execution time through provider-standard environment or
caller-owned secret management. Never store API keys in project config, lock
files, runtime plans, run manifests, evaluation reports, fixtures, or command
history.

The OpenAI-compatible executor can add a bearer header. It does not log that
header itself, but callers must prevent HTTP debugging, exception wrappers, or
custom openers from exposing it.

The eval CLI accepts only `--api-key-env ENVIRONMENT_VARIABLE`, never a literal
API-key argument. It reads the value at execution setup and does not place the
value or variable name in the manifest or dry-run output. Live result values
and unexpected exception messages are recursively redacted before persistence.
Public experiment manifests reject secret-bearing field names and endpoint
origins containing credentials.

`redact_secrets` masks common bearer, key/value, OpenAI-style, and GitHub-style
patterns. Redaction is defense in depth, not a guarantee: unusual credentials,
secrets embedded in arbitrary prose, and encoded values may survive. Inspect
artifacts before sharing them.

## Sensitive plans and hashes

A plan contains source paths, selection reasons, constraints, host capabilities,
and potentially sensitive task-derived material. `task_resolution_hash` and
`manifest_hash` are stable identifiers; hashing does not anonymize low-entropy
or guessable inputs.

Do not use global cross-project caches for sensitive plans. No runtime cache is
implemented today. If one is added, keep it project-local, restrict access, and
key it by every semantic compiler input described in [Versioning](VERSIONING.md).

## Run artifacts

`write_run_artifacts` creates a new directory and refuses to reuse an existing
one. It writes:

- redacted task text;
- full runtime plan;
- compiled instructions;
- raw model response;
- metrics and run manifest.

The full plan, compiled instructions, raw response, and arbitrary metrics may
still contain secrets or private source content. Choose an access-controlled
output location, apply retention rules, and redact before publication. Store
source IDs/hashes instead of copyrighted or confidential corpora when full text
is not needed.

## Prompt and tool safety

- Keep user/task content outside the managed instruction block.
- Treat retrieved files, web content, and tool output as untrusted data.
- Never ask a model to reveal private chain-of-thought; validate observable
  output and actions.
- Do not claim an unavailable tool, worker, or durable-state mechanism exists.
- Do not convert every validator into prose; use deterministic enforcement when
  possible.
- Surface conflicts and limitations before model execution.

## Evaluation safety

Core CI and dry-run use mock/fake transports only. A live eval requires an
explicit adapter/model/endpoint choice; it may use local compute or incur remote
provider cost. Keep generation and graders isolated, do not leak expected
answers into model input, sandbox any code grader, and retain failed/partial
attempts rather than silently replaying side effects. See
[Evaluation](EVALUATION.md).
