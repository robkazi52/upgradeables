"""Typed provider-neutral runtime compiler inputs."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class HostCapabilities:
    instruction_channel: str = "system-or-developer"
    tools: tuple[str, ...] = ()
    state_support: str = "none"
    parallelism: bool = False

    @classmethod
    def from_value(cls, value: "HostCapabilities | dict[str, Any] | None") -> "HostCapabilities":
        if value is None:
            return cls()
        if isinstance(value, cls):
            return value
        return cls(
            instruction_channel=str(value.get("instruction_channel", "system-or-developer")),
            tools=tuple(sorted(set(value.get("tools", ())))),
            state_support=str(value.get("state_support", "none")),
            parallelism=bool(value.get("parallelism", False)),
        )

    def as_dict(self) -> dict[str, Any]:
        return {
            "instruction_channel": self.instruction_channel,
            "tools": list(self.tools),
            "state_support": self.state_support,
            "parallelism": self.parallelism,
        }


@dataclass(frozen=True)
class RuntimeContext:
    model_profile: str = "medium"
    max_directive_tokens: int = 500
    host: HostCapabilities = field(default_factory=HostCapabilities)
    base_instructions_present: bool = True

    @classmethod
    def from_value(cls, value: "RuntimeContext | dict[str, Any] | None") -> "RuntimeContext":
        if value is None:
            return cls()
        if isinstance(value, cls):
            return value
        budget = value.get("budget", {})
        return cls(
            model_profile=str(value.get("model_profile", "medium")),
            max_directive_tokens=int(value.get("max_directive_tokens", budget.get("max_directive_tokens", 500))),
            host=HostCapabilities.from_value(value.get("host")),
            base_instructions_present=bool(value.get("base_instructions_present", True)),
        )


@dataclass(frozen=True)
class RuntimeCompileRequest:
    """Serializable provider-neutral compiler request."""

    task_resolution: dict[str, Any]
    model_profile: str = "medium"
    host: HostCapabilities = field(default_factory=HostCapabilities)
    max_directive_tokens: int = 500
    base_instructions_present: bool = True

    @classmethod
    def from_value(cls, value: "RuntimeCompileRequest | dict[str, Any]") -> "RuntimeCompileRequest":
        if isinstance(value, cls):
            return value
        return cls(
            task_resolution=value["task_resolution"],
            model_profile=str(value.get("model_profile", "medium")),
            host=HostCapabilities.from_value(value.get("host")),
            max_directive_tokens=int(value.get("budget", {}).get("max_directive_tokens", 500)),
            base_instructions_present=bool(value.get("base_instructions_present", True)),
        )

    def context(self) -> RuntimeContext:
        return RuntimeContext(
            model_profile=self.model_profile,
            max_directive_tokens=self.max_directive_tokens,
            host=self.host,
            base_instructions_present=self.base_instructions_present,
        )

    def as_dict(self) -> dict[str, Any]:
        return {
            "task_resolution": self.task_resolution,
            "model_profile": self.model_profile,
            "host": self.host.as_dict(),
            "budget": {"max_directive_tokens": self.max_directive_tokens},
            "base_instructions_present": self.base_instructions_present,
        }
