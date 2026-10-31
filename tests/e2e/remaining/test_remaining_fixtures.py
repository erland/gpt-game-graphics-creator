"""Validate synthetic G03-G10/G13-G15 scenario coverage, not host runtime functionality."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DOCS = ROOT / "tests"
FIXTURE = Path(__file__).with_name("remaining-test-cases.json")
EXPECTED = {"G03","G04","G05","G06","G07","G08","G09","G10","G13","G14","G15"}

class RemainingFixtureContract(unittest.TestCase):
    def test_unique_complete_case_ids_and_sources(self):
        data = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(data["status"], "NOT_RUN")
        cases = data["cases"]
        self.assertEqual(len(cases),len(EXPECTED))
        self.assertEqual({c["id"] for c in cases}, EXPECTED)
        for case in cases:
            with self.subTest(case=case["id"]):
                self.assertTrue((DOCS / (case["id"]+".md")).is_file())
                self.assertIn(case["priority"],(1,2,3))
                self.assertEqual(case["result"],"NOT_RUN")
                for field in ("prompt","expected_behavior","automation_scope","manual_or_external_check"):
                    self.assertTrue(case[field])
                self.assertTrue(case["assertion_tags"])
    def test_no_claimed_runtime_pass(self):
        data=json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertNotIn("PASS",[c["result"] for c in data["cases"]])

if __name__=="__main__":
    unittest.main()
