# Harness Security and Privacy

Normal `init`, `inspect`, `recommend`, task resolution, integration preview, and `doctor` operations require no network connection, telemetry, API key, or model call.

Project detection is intentionally shallow. It checks recognized file and directory names but does not execute builds or tests, import project packages, traverse `.git/objects`, recursively ingest a repository, or read `.env`, credential, token, key, or private-key contents. Agent instruction files are project signals, not proof of model or tool capabilities.

`.upgradeables/project.json` records portable paths and observable signals. Runtime capability values remain `unknown` unless explicitly declared; only project-file durable state is identified locally.

`init` writes under `.upgradeables/` only. Host instruction integration is preview-only unless `--write` is explicit. Managed-block insertion, update, and removal preserve bytes outside the two Upgradeables markers and fail closed on missing, doubled, nested, or out-of-order markers. Symlinked write targets are rejected.

`doctor --fix` may recreate missing deterministic harness files and refresh generated adapter fragments. It does not rewrite user-authored Skill content, repair malformed user host files, execute project code, or contact a remote registry.
