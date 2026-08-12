"""Tests for the coverage-map substrate (B0): every node domained + validly-standing, buckets sum,
and the structural honesty guard -- a BORROWED node carries ZERO GRUT-derivation credit, so growing
the map (borrowed/silent scaffold) can never read as GRUT reach.
"""
import json
import os
import re
import unittest

from coverage import coverage_map, VALID_STANDINGS

# Claim-verbs that, applied to GRUT AFFIRMATIVELY, would over-claim a borrowed/silent node.
_VERB = re.compile(r"\b(derives?|derived|covers?|reproduces?|explains?)\b", re.I)
_NEG = re.compile(r"\b(no|not|nothing|neither|never|n't)\b", re.I)

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    with open(os.path.join(HERE, "claims.json")) as f:
        return json.load(f)["claims"]


class TestCoverage(unittest.TestCase):
    def setUp(self):
        self.claims = load()

    def test_every_node_has_domain_and_valid_standing(self):
        for c in self.claims:
            self.assertIn("domain", c, f"{c['id']} missing domain")
            self.assertTrue(c.get("domain"), f"{c['id']} empty domain")
            self.assertIn(c.get("grut_standing"), VALID_STANDINGS,
                          f"{c['id']} grut_standing {c.get('grut_standing')!r} not in {VALID_STANDINGS}")

    def test_no_unknown_standing(self):
        m = coverage_map(self.claims)
        self.assertEqual(m["unknown_standing"], [])

    def test_buckets_sum_to_all_nodes(self):
        m = coverage_map(self.claims)
        self.assertEqual(sum(m["totals"].values()), len(self.claims))

    def test_borrowed_nodes_carry_zero_credit(self):
        # THE honesty guard: a borrowed import must never carry GRUT-derivation credit, so a borrowed
        # scaffold node can never inflate the ledger / read as GRUT reach.
        for c in self.claims:
            if c.get("grut_standing") == "borrowed":
                self.assertEqual(c.get("ledger_delta"), 0,
                                 f"borrowed node {c['id']} carries non-zero credit {c.get('ledger_delta')}")

    def test_open_field_nodes_carry_zero_credit(self):
        for c in self.claims:
            if c.get("grut_standing") == "open field":
                self.assertEqual(c.get("ledger_delta"), 0,
                                 f"open-field node {c['id']} carries non-zero credit {c.get('ledger_delta')}")

    def test_absent_bucket_present(self):
        m = coverage_map(self.claims)
        self.assertTrue(m["absent"], "the map must name its known-physics gaps (absent), not hide them")

    def test_no_borrowed_or_silent_node_over_claims(self):
        # LAUNDERING-BY-ADJACENCY guard (permanent): no borrowed/silent node's claim-bearing text may
        # affirmatively say GRUT derives/covers/reproduces/explains -- a claim-verb near 'GRUT' MUST carry
        # a negation ("GRUT derives NOTHING", "does NOT derive", "not a GRUT-derived medium").
        for c in self.claims:
            if c.get("grut_standing") not in ("borrowed", "silent"):
                continue
            blob = " ".join(str(c.get(f, "")) for f in
                            ("statement", "match_verdict", "boundary_condition", "sub_status"))
            for m in _VERB.finditer(blob):
                window = blob[max(0, m.start() - 30):m.end() + 15]
                if "grut" in window.lower():
                    self.assertTrue(_NEG.search(window),
                                    f"{c['id']} affirmative over-claim near: '...{window.strip()}...'")

    def test_attaches_to_resolves_and_media_are_borrowed(self):
        # B1: every real-medium scaffold node carries an attaches_to edge that resolves to a real claim,
        # and is grut_standing 'borrowed' -- the firewall-critical guard that a real medium in the graph
        # can NEVER read as 'GRUT covers it'.
        by_id = {c["id"]: c for c in self.claims}
        media = [c for c in self.claims if "attaches_to" in c]
        self.assertTrue(media, "B1 media scaffold nodes must be present")
        for c in media:
            self.assertIn(c["attaches_to"], by_id, f"{c['id']} attaches_to '{c['attaches_to']}' does not resolve")
            self.assertEqual(c.get("grut_standing"), "borrowed",
                             f"media node {c['id']} must be 'borrowed', never 'covered'")
            self.assertEqual(c.get("ledger_delta"), 0, f"media node {c['id']} must carry zero credit")
            self.assertIn("match_verdict", c, f"{c['id']} missing the sanity-check payload (match_verdict)")


if __name__ == "__main__":
    unittest.main()
