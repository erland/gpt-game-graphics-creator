"""Regression guard for selective revision and explicitly unverified G16 contracts."""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "fixtures"

def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))

class AcceptanceContractTests(unittest.TestCase):
    def test_G12_only_ground_changes(self):
        original = load("prototype-manifest.json")
        revised = load("selective-revision-manifest.json")
        before = {a["id"]: a for a in original["assets"]}
        after = {a["id"]: a for a in revised["assets"]}
        self.assertEqual(set(before), set(after))
        self.assertEqual(revised["revision"]["changed_asset_ids"], ["ground-01"])
        self.assertEqual(revised["revision"]["unchanged_asset_ids"], ["prop-01"])
        for key in ("file", "sha256", "footprint", "projection", "anchor", "scale", "atlas_slot"):
            self.assertEqual(before["prop-01"][key], after["prop-01"][key], key)
        self.assertNotEqual(before["ground-01"]["sha256"], after["ground-01"]["sha256"])
        for a in revised["assets"]:
            self.assertEqual(hashlib.sha256((ROOT / a["file"]).read_bytes()).hexdigest(), a["sha256"])

    def test_G16_unknown_contracts_not_claimed_pass(self):
        contract = load("G16-verification-contract.json")
        self.assertEqual(contract["upgrade"]["target_maturity"], "productionCandidate")
        for name in ("animation", "localization"):
            self.assertEqual(contract[name]["preservation_status"], "NOT_VERIFIED")
        self.assertEqual(contract["visual_change_policy"]["status"], "NOT_VERIFIED")
        self.assertEqual(contract["external"]["independent_plugin_runtime"], "NOT_VERIFIED")

if __name__ == "__main__":
    unittest.main()
