"""Canned adapter for harness development; never evidence of model behavior."""
from __future__ import annotations

from .base import ModelAdapter


class MockAdapter(ModelAdapter):
    def __init__(self, response: str = "MOCK RESPONSE — NOT A MODEL RESULT"):
        self.response = response

    def run(self, prompt: str) -> str:
        if not isinstance(prompt, str) or not prompt.strip():
            raise ValueError("prompt must be non-empty text")
        return self.response
