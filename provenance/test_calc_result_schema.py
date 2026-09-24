#!/usr/bin/env python3
"""Shared schema test for the calc/ result artifacts.

Walks every calc/*RESULT*.json / calc/RESULTS*.json file and asserts the COMMON
shape the downstream manifest builders rely on (schema inferred from the frozen
artifacts themselves, 2026 vintage):

  - the file parses as JSON and is a single JSON object;
  - it carries at least one IDENTITY key (instrument / purpose / auditor /
    battery / manifest / charter / question) saying what produced it;
  - any `checks` list entries are objects carrying a NAME-like key
    (name / check / label / id) and a PASS-like key (pass / ok / status /
    passed / holds) so failing checks are machine-readable.

It does NOT adjudicate pass/fail counts -- only the schema. Run:
    python3 provenance/test_calc_result_schema.py
(pure stdlib, unittest)
"""
import glob
import json
import os
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
CALC = os.path.join(HERE, os.pardir, "calc")

IDENTITY_KEYS = {"instrument", "purpose", "auditor", "battery", "manifest", "charter", "question"}
NAME_KEYS = {"name", "check", "label", "id"}
PASS_KEYS = {"pass", "ok", "status", "passed", "holds"}


def result_files():
    pats = [os.path.join(CALC, "*RESULT*.json"), os.path.join(CALC, "RESULTS_*.json")]
    seen = set()
    for pat in pats:
        for p in sorted(glob.glob(pat)):
            if p not in seen:
                seen.add(p)
                yield p


class TestCalcResultSchema(unittest.TestCase):
    def _load(self, path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)

    def test_every_result_parses_as_json_object(self):
        files = list(result_files())
        self.assertGreater(len(files), 0, "no calc result artifacts found")
        for p in files:
            with self.subTest(file=os.path.basename(p)):
                d = self._load(p)
                self.assertIsInstance(d, dict)

    def test_every_result_carries_identity_key(self):
        for p in result_files():
            with self.subTest(file=os.path.basename(p)):
                d = self._load(p)
                self.assertTrue(IDENTITY_KEYS & set(d),
                                f"{p}: no identity key (any of {sorted(IDENTITY_KEYS)})")

    def test_checks_entries_are_well_formed(self):
        for p in result_files():
            d = self._load(p)
            checks = d.get("checks")
            if checks is None:
                continue
            with self.subTest(file=os.path.basename(p)):
                self.assertIsInstance(checks, list, f"{p}: checks must be a list")
                for i, c in enumerate(checks):
                    self.assertIsInstance(c, dict,
                                          f"{p}: checks[{i}] is not an object")
                    self.assertTrue(NAME_KEYS & set(c),
                                    f"{p}: checks[{i}] has no name-like key")
                    self.assertTrue(PASS_KEYS & set(c),
                                    f"{p}: checks[{i}] has no pass-like key")

    def test_summary_when_present_is_object_or_string(self):
        for p in result_files():
            d = self._load(p)
            if "summary" in d:
                with self.subTest(file=os.path.basename(p)):
                    self.assertIsInstance(d["summary"], (dict, str),
                                          f"{p}: summary must be object or string")


if __name__ == "__main__":
    unittest.main(verbosity=2)
