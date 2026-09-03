import itertools
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = (
    "coding-debugging",
    "long-context-corpus-analysis",
    "creative-ideation",
    "high-stakes-evidence-analysis",
    "architecture-skill-building",
)
SECTIONS = (
    "Procedure",
    "Validators and Failure Handling",
    "Output Contract",
    "Tests",
)
TASK_ANCHORS = {
    "coding-debugging": {"reproduction", "patch", "test"},
    "long-context-corpus-analysis": {"corpus", "coverage", "source"},
    "creative-ideation": {"concept", "candidate", "brief"},
    "high-stakes-evidence-analysis": {"claim", "evidence", "abstain"},
    "architecture-skill-building": {"skill", "component", "validation"},
}


def section(text, heading):
    match = re.search(
        rf"^## {re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    return match.group(1).strip() if match else ""


class CommunitySkillSpecificityTests(unittest.TestCase):
    def test_generator_and_five_skills_validate(self):
        check = subprocess.run(
            [sys.executable, "scripts/build_ecosystem_reviews.py", "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(check.returncode, 0, check.stderr)
        paths = [f"implementations/community/{slug}" for slug in SKILLS]
        validation = subprocess.run(
            [sys.executable, "scripts/validate_skill.py", *paths],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(validation.returncode, 0, validation.stderr)

    def test_contract_sections_are_substantive_and_task_specific(self):
        contracts = {}
        minimum_words = {
            "Procedure": 120,
            "Validators and Failure Handling": 90,
            "Output Contract": 65,
            "Tests": 140,
        }
        for slug in SKILLS:
            text = (ROOT / "implementations" / "community" / slug / "SKILL.md").read_text(encoding="utf-8")
            bodies = []
            for heading in SECTIONS:
                body = section(text, heading)
                self.assertGreaterEqual(len(re.findall(r"[A-Za-z0-9'-]+", body)), minimum_words[heading], f"{slug}: {heading}")
                bodies.append(body)
            contract = " ".join(bodies).casefold()
            contracts[slug] = set(re.findall(r"[a-z]{4,}", contract))
            for anchor in TASK_ANCHORS[slug]:
                self.assertIn(anchor, contract, f"{slug}: missing task anchor {anchor}")

        for left, right in itertools.combinations(SKILLS, 2):
            union = contracts[left] | contracts[right]
            similarity = len(contracts[left] & contracts[right]) / len(union)
            self.assertLess(similarity, 0.40, f"generic-shell similarity: {left} / {right} = {similarity:.2f}")

    def test_selected_component_rationales_are_not_registry_purposes(self):
        catalog = json.loads((ROOT / "registry" / "catalog.json").read_text(encoding="utf-8"))
        purposes = {item["slug"]: item["purpose"] for item in catalog["upgradeables"]}
        row_pattern = re.compile(r"^\| `([a-z0-9-]+)@\d+\.\d+\.\d+` \| (.+) \|$", re.MULTILINE)
        seen_rationales = set()
        for skill_slug in SKILLS:
            text = (ROOT / "implementations" / "community" / skill_slug / "SKILL.md").read_text(encoding="utf-8")
            rows = row_pattern.findall(section(text, "Selected Upgradeables"))
            self.assertGreaterEqual(len(rows), 4, skill_slug)
            for component, rationale in rows:
                self.assertNotEqual(rationale.strip(), purposes[component].strip(), f"{skill_slug}: {component}")
                self.assertGreaterEqual(len(rationale.split()), 10, f"{skill_slug}: {component}")
                identity = rationale.casefold()
                self.assertNotIn(identity, seen_rationales)
                seen_rationales.add(identity)


if __name__ == "__main__":
    unittest.main()
