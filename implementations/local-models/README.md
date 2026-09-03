# Local-Model Adapter

Local runtimes vary, so begin with an explicit capability manifest rather than a
presumed feature set.

## Mapping

| Concern | Mapping |
|---|---|
| Task Skill / behavior | Render the workflow and package rules into the runtime's prompt template. |
| Core loading | Resolve paths through a bounded loader with size and trust limits. |
| State | Store explicit JSON only when the integration supplies a real store. |
| Validators / scripts | Use an allowlisted command interface and capture exit status. |
| Tools / orchestration | Declare every tool and process boundary; validate returned data. |
| Persistence / parallelism | Document stores, processes, isolation, cleanup, and recovery. |

## Capability matrix

- **Supported:** file-based instruction assembly, explicit JSON schemas, local
  references, and deterministic scripts when the integrator wires them in.
- **Unsupported by specification alone:** reliable tools, durable memory,
  isolation, parallel workers, and permission enforcement.
- **Unknown / version-dependent:** prompt format, context limits, structured
  output, tools, retrieval, concurrency, and persistence.

Complete [the shared contract](../ADAPTER_CONTRACT.md) against the exact runtime and build.
