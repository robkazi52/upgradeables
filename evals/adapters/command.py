"""Adapter for an explicitly supplied local model CLI command."""
from __future__ import annotations

import subprocess
from collections.abc import Sequence

from .base import ModelAdapter


class CommandAdapter(ModelAdapter):
    def __init__(self, command: Sequence[str], timeout_seconds: int = 120):
        if not command:
            raise ValueError("command must contain an executable")
        self.command = list(command)
        self.timeout_seconds = timeout_seconds

    def run(self, prompt: str) -> str:
        if not prompt.strip():
            raise ValueError("prompt must be non-empty text")
        result = subprocess.run(
            self.command,
            input=prompt,
            text=True,
            capture_output=True,
            timeout=self.timeout_seconds,
            check=False,
            shell=False,
        )
        if result.returncode:
            raise RuntimeError(
                f"model command failed with {result.returncode}: {result.stderr.strip()}"
            )
        return result.stdout
