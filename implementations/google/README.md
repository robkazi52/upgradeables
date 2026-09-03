# Google Adapter

Map the task Skill to the actual Google model or agent surface selected by the
deployer. Do not transfer provider assumptions into the canonical library.

## Mapping

| Concern | Mapping |
|---|---|
| Task Skill / behavior | Use the host instruction artifact and keep activation selective. |
| Core loading | Map bounded references to a verified file, retrieval, or context mechanism. |
| State | Document request, session, and external lifetimes separately. |
| Validators / scripts | Attach scripts only through real execution; model judgments remain behavioral evals. |
| Orchestration | Preserve authority and validate outputs returned by verified agents/tools. |
| Persistence / parallelism | Require and name an actual backing feature. |

## Capability matrix

- **Supported:** portable instruction mapping, explicit state serialization,
  bounded-reference planning, and local checks.
- **Unsupported by specification alone:** implicit memory, automatic tool access,
  evaluator independence, and background execution.
- **Unknown / version-dependent:** packaging, context/file limits, retrieval,
  tools, stores, and parallelism. Verify the selected host and date the result.

Follow [the shared contract](../ADAPTER_CONTRACT.md); host policy retains precedence.
