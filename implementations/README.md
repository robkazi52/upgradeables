# Implementation Adapters

The specification is model-agnostic. These folders map it to host instructions,
state schemas, validators, scripts, references, agent graphs, and Skill packages.
Adapter behavior may evolve without rewriting canonical Upgradeable identity.
Implement only capabilities the host actually provides.

All adapters follow the [provider adapter contract](ADAPTER_CONTRACT.md). Its
capability matrix prevents prompt approximations from being represented as real
persistence, tool execution, parallelism, or evaluator independence.

- Start with [community Skills](community/) for portable implementations.
- Use a provider folder only when packaging or host capabilities require it.
- Follow the separate contribution routes in [CONTRIBUTING.md](../CONTRIBUTING.md).
