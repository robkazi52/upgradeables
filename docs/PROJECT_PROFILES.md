# Project Profiles

Project profiles are weak, versioned preselection priors. They map shallow project signals to likely recipe families, candidate cross-cutting components, and likely exclusions. They never override current-task wording, permissions, triggers, non-triggers, or complexity limits.

Built-in profiles:

- `general`
- `software-development`
- `research`
- `long-context`
- `authoring`
- `data-analysis`
- `medical-evidence`
- `legal-evidence`
- `agent-development`
- `documentation`

Automatic inspection uses recognizable manifests and top-level directories. Use `upgradeables init --profile <slug>` for an explicit profile or `--no-detect` to avoid signal detection. Numeric probability or confidence claims are not produced.

Host capability is separate from project profile. An `AGENTS.md` file can suggest an agent-development profile, but it cannot prove that shell, web, persistent memory, or parallel workers are available.
