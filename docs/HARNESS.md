# Upgradeables Project Harness

The harness turns the repository's registry into a small, local project map. It detects shallow project signals, selects weak project-profile priors, and prepares task-family and agent-adapter files. It does not activate every recommended component.

## Local workflow

```bash
upgradeables inspect
upgradeables recommend
upgradeables init
upgradeables task "review this pull request for regressions"
upgradeables integrate codex --write
upgradeables doctor
```

`inspect`, `recommend`, and integration preview are read-only. `init` writes only under `.upgradeables/`. Agent host files change only through an explicit `integrate ... --write` or `--remove` request and only inside the marked managed block.

The default `standard` initialization creates portable project, configuration, lock, task-map, Skill-map, and agent-fragment artifacts. `--minimal` omits task/Skill maps and specialized fragments. `--full` additionally creates explicit local runtime state directories. Repeating initialization is byte-idempotent; differing existing harness files are preserved unless `--force` is supplied.

Project recommendations rank candidate recipes and cross-cutting controls. Current task wording, authority, failure risk, canonical triggers and non-triggers, and the smallest sufficient composition still decide what is used.

Run `upgradeables doctor --fix` to repair only deterministic harness-owned files. It never rewrites user-authored Skills or unmarked host-file content.

To turn a stable project workflow into a local, reviewable Skill, follow the
[Project Skill Factory](SKILL_FACTORY.md). Task-event recording remains off by
default and Skill suggestions never auto-create files.

## Release-candidate smoke test

On Windows, maintainers can validate a GitHub branch end to end with one command:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/test_v03_release_candidate.ps1
```

The script waits for PR checks, installs the branch through `pipx`, exercises a
temporary Python project, checks initialization and managed-block idempotency,
tests task resolution and the Skill factory, and requires `doctor` to pass. Use
`-KeepTemp` to retain the synthetic project for inspection.
