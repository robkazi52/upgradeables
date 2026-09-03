"""Provider-neutral model adapter interface."""
from __future__ import annotations

from abc import ABC, abstractmethod


class ModelAdapter(ABC):
    """Run one explicit prompt and return the model's visible response."""

    @abstractmethod
    def run(self, prompt: str) -> str:
        raise NotImplementedError
