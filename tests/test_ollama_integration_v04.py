import os
import shutil
import sys
import unittest
import uuid
from contextlib import contextmanager
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from upgradeables_harness.runtime.adapters.generic import AdapterRequestError, endpoint_type
from upgradeables_harness.runtime.adapters.ollama import discover, run_ollama


@contextmanager
def workspace_directory():
    path = ROOT / "tests" / f"tmp-ollama-integration-{uuid.uuid4().hex}"
    path.mkdir()
    try:
        yield str(path)
    finally:
        shutil.rmtree(path)


class OptionalOllamaIntegrationTests(unittest.TestCase):
    def test_installed_loopback_model_smoke(self):
        if os.environ.get("UPGRADEABLES_RUN_OLLAMA_INTEGRATION") != "1":
            self.skipTest("set UPGRADEABLES_RUN_OLLAMA_INTEGRATION=1 to enable")
        model = os.environ.get("UPGRADEABLES_OLLAMA_MODEL")
        if not model:
            self.skipTest("set UPGRADEABLES_OLLAMA_MODEL to an already installed model")
        endpoint = os.environ.get("UPGRADEABLES_OLLAMA_ENDPOINT", "http://127.0.0.1:11434")
        if endpoint_type(endpoint) != "loopback":
            self.skipTest("integration smoke permits only a loopback Ollama endpoint")
        try:
            discovered = discover(endpoint, model, timeout=3)
        except AdapterRequestError as error:
            self.skipTest(f"Ollama unavailable: {error.error['kind']}")
        if discovered["model_available"]["status"] != "supported":
            self.skipTest(f"model is not installed: {model}")

        with workspace_directory() as directory:
            result = run_ollama(
                endpoint=endpoint,
                model=model,
                task="Return exactly: OLLAMA_SMOKE_OK",
                model_profile="strong",
                max_directive_tokens=100,
                options={"temperature": 0},
                timeout=30,
                output_root=directory,
            )
            self.assertIsNone(result["response"]["error"])
            self.assertFalse(result["response"]["partial"])
            self.assertTrue(result["response"]["response_text"].strip())
            self.assertTrue(Path(result["artifact_directory"], "manifest.json").is_file())


if __name__ == "__main__":
    unittest.main()
