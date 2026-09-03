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
