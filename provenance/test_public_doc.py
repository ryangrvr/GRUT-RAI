"""test_public_doc: the one-number rule enforced on the public document itself.

Three properties: the rendered file matches a fresh render (no hand-edited numbers); the SOURCE
contains no typed register count (the prohibition is on the body, not the appendix); and the
front matter's load-bearing negatives track the register rather than being asserted.
"""
import os
import re
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "docs", "WHERE_IT_STOPS.src.md")
OUT = os.path.join(ROOT, "docs", "WHERE_IT_STOPS.md")

sys.path.insert(0, HERE)


class TestPublicDoc(unittest.TestCase):

    def test_rendered_matches_source_and_register(self):
        r = subprocess.run([sys.executable, os.path.join(HERE, "build_public_doc.py"), "--check"],
                           capture_output=True, text=True, timeout=300)
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_the_source_types_no_register_count(self):
        """THE RULE. Every register-derived count must be a placeholder in the source. Checked by
        looking for the CURRENT values as bare integers in the source prose -- if a number that
        the register currently emits appears typed, it would silently go stale."""
        import emit_public_numbers as E
        n = E.numbers()
        src = open(SRC).read()
        # strip fenced code, inline code, and DOIs/dates, where digits are legitimate
        stripped = re.sub(r"`[^`]*`", "", src)
        stripped = re.sub(r"\d{4}-\d{2}-\d{2}", "", stripped)
        stripped = re.sub(r"10\.5281/zenodo\.\d+", "", stripped)
        guarded = {"n_grut": n["n_grut"], "spec_total": n["spec_total"], "spec_B": n["spec_B"],
                   "spec_A": n["spec_A"], "n_tests": n["n_tests"], "total": n["total"]}
        offenders = []
        for name, val in guarded.items():
            if re.search(rf"(?<![\d.]){val}(?![\d.])", stripped):
                offenders.append(f"{name}={val}")
        self.assertFalse(offenders,
                         f"register counts typed into the source prose: {offenders}. "
                         f"Use the {{{{placeholder}}}} form -- a typed count goes stale silently, "
                         f"which is the failure the prior deposit made at scale.")

    def test_fixed_point_one_tracks_the_empty_derived_tier(self):
        import emit_public_numbers as E
        n = E.numbers()
        self.assertEqual(n["tiers"].get("derived", 0), 0,
                         "the `derived` tier is populated; fixed point 1 must be rewritten")
        self.assertIn("Zero novel positive predictions", open(SRC).read())

    def test_fixed_point_five_denies_being_the_final_deposit(self):
        src = open(SRC).read()
        self.assertIn("not the program's final deposit", src)
        self.assertIn("No stop condition has fired", src)

    def test_the_dispatch_is_described_as_unsent(self):
        src = open(SRC).read()
        self.assertTrue(re.search(r"never sent|held, and never sent|unsent", src),
                        "the document must not imply the dispatch was sent")
