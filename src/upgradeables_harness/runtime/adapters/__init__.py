"""Provider adapters for v0.4 RuntimePlan values."""

from .generic import AdapterRequestError, capability, compose_instructions, endpoint_type
from .openai_agents import apply_runtime_plan, describe_capabilities as describe_openai_agents_capabilities
from .ollama import (
    build_ollama_request,
    discover as discover_ollama,
    normalize_discovery as normalize_ollama_discovery,
    normalize_response as normalize_ollama_response,
    normalize_stream as normalize_ollama_stream,
    run_ollama,
)
from .openai_compatible import (
    build_chat_completions_request,
    discover_models,
    normalize_discovery as normalize_models_discovery,
    normalize_response as normalize_chat_completions_response,
    normalize_stream as normalize_chat_completions_stream,
)

__all__ = [
    "AdapterRequestError",
    "apply_runtime_plan",
    "build_chat_completions_request",
    "build_ollama_request",
    "capability",
    "compose_instructions",
    "discover_models",
    "discover_ollama",
    "describe_openai_agents_capabilities",
    "endpoint_type",
    "normalize_chat_completions_response",
    "normalize_chat_completions_stream",
    "normalize_models_discovery",
    "normalize_ollama_discovery",
    "normalize_ollama_response",
    "normalize_ollama_stream",
    "run_ollama",
]
