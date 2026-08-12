"""Doc-sync standing test (3e): the four standing docs carry a REGISTER-SYNC marker that must match
the live register. Converts count/net drift (the class the 2026-08 review caught: three docs saying
'32 claims' against a 43-node register) from a manual sweep into a standing test.

Marker format, one per doc:  <!-- REGISTER-SYNC: <N> nodes, net +<NET> -->
"""
import json
import os
import re
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

DOCS = ["STATE.md", "POSTULATE_MAP.md", "GRUT_II_Agenda.md", "GRUT_I_What_Survived.md", "GRUT_ToE.md", "README.md",
    "GRUT_II_What_Survived.md",   # added 2026-08-04: it carries a REGISTER-SYNC
    "X_FLOOR_MAP.md",            # marker that nothing was enforcing (firewall finding)
]
MARKER = re.compile(r"<!-- REGISTER-SYNC: (\d+) nodes, net \+(\d+) -->")
# B1 (2026-08-10): the sync marker's count is GRUT-scope and readers running len(claims) got 70 --
# so every marker now travels with a TOTAL stamp naming BOTH counts and BOTH nets. Machine-checked
# here so the stamps derive from the register rather than being hand-maintained prose.
TOTAL = re.compile(r"<!-- REGISTER-TOTAL: (\d+) = (\d+) grut \+ (\d+) vacuum-cluster; "
                   r"nets \+(\d+) grut, \+(\d+) cluster -->")


class TestDocSync(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(HERE, "claims.json")) as f:
            claims = json.load(f)["claims"]
        # SCOPED 2026-08-04: the REGISTER-SYNC markers in the standing docs describe GRUT's
        # register. Out-of-scope nodes (the vacuum-cluster map) have their own deliverable and
        # their own gate, and must not silently move GRUT's doc markers.
        self.total = len(claims)
        cluster = [c for c in claims if c.get("ledger_scope") == "vacuum-cluster"]
        self.n_cluster = len(cluster)
        self.net_cluster = sum(c.get("ledger_delta", 0) for c in cluster
                               if isinstance(c.get("ledger_delta"), int)
                               and not isinstance(c.get("ledger_delta"), bool))
        claims = [c for c in claims if c.get("ledger_scope", "grut") == "grut"]
        self.n = len(claims)
        self.net = sum(c.get("ledger_delta", 0) for c in claims
                       if isinstance(c.get("ledger_delta"), int) and not isinstance(c.get("ledger_delta"), bool))

    def test_every_standing_doc_matches_live_register(self):
        for doc in DOCS:
            with open(os.path.join(ROOT, doc)) as f:
                text = f.read()
            markers = list(MARKER.finditer(text))
            self.assertTrue(markers, f"{doc}: missing REGISTER-SYNC marker")
            for m in markers:  # ALL markers in a doc must match, not just the first
                self.assertEqual(int(m.group(1)), self.n,
                                 f"{doc}: marker says {m.group(1)} nodes, register has {self.n}")
                self.assertEqual(int(m.group(2)), self.net,
                                 f"{doc}: marker says net +{m.group(2)}, register nets +{self.net}")
            totals = list(TOTAL.finditer(text))
            self.assertEqual(len(totals), len(markers),
                             f"{doc}: every REGISTER-SYNC marker must travel with a REGISTER-TOTAL "
                             f"stamp (found {len(markers)} sync, {len(totals)} total) -- the "
                             f"GRUT-count/full-count ambiguity is what let '49 nodes' read as "
                             f"falsified against a 70-claim file")
            for t in totals:
                got = tuple(int(t.group(i)) for i in range(1, 6))
                want = (self.total, self.n, self.n_cluster, self.net, self.net_cluster)
                self.assertEqual(got, want,
                                 f"{doc}: REGISTER-TOTAL stamp {got} != register {want}")


if __name__ == "__main__":
    unittest.main()


class TestAnchorConditionalityTravels(unittest.TestCase):
    """ENFORCEMENT HOOK (2026-08-10c, overseer-found). The four-boundaries anchor claim was
    corrected in STATE.md and NOT in GRUT_I_What_Survived.md -- which STATE.md itself calls
    "the label-for-label deposit", i.e. the document written for external readers. The
    correction landed in the internal snapshot and skipped the public one.

    That is the RELOCATION pattern, not a new error class: fixing an inconsistency in one of two
    documents MOVES it instead of closing it. A claim this load-bearing must not depend on
    someone remembering both sites, so it is carried here the way the register stamps are.

    THE AUTHORITY IS THE LEDGER: NO_GO_LEDGER.md holds the no-crossing "conditional on the open
    `rung3` (a no-go cannot outrank its anchor) -- held `to-derive`." Any document asserting the
    boundaries are clean of the anchor must carry that conditionality in the same breath."""

    PHRASE = "clean of the open anchor"
    # the qualifier that must accompany it -- any of these forms
    QUALIFIERS = ("anchor-conditional", "anchor-CONDITIONAL", "conditional on the open",
                  "THREE of the four", "three are clean")
    WINDOW = 1200   # chars after the phrase within which the qualifier must appear

    def test_the_ledger_still_states_the_conditionality(self):
        """Guard the authority itself: if the ledger's own line is ever softened, this fires
        first -- otherwise the docs below could be 'corrected' toward a claim nobody holds."""
        with open(os.path.join(ROOT, "NO_GO_LEDGER.md")) as f:
            led = f.read()
        self.assertIn("conditional on the open", led,
                      "NO_GO_LEDGER is the authority on boundary strength grades; its "
                      "anchor-conditionality line is missing")
        self.assertIn("a no-go cannot outrank its anchor", led)

    def test_no_doc_asserts_anchor_cleanliness_unqualified(self):
        import glob
        offenders = []
        for path in sorted(glob.glob(os.path.join(ROOT, "*.md"))):
            with open(path) as f:
                text = f.read()
            for m in re.finditer(re.escape(self.PHRASE), text):
                window = text[m.start():m.start() + self.WINDOW]
                if not any(q in window for q in self.QUALIFIERS):
                    offenders.append(f"{os.path.basename(path)} @ char {m.start()}")
        self.assertFalse(offenders,
                         f"unqualified anchor-cleanliness assertion at: {offenders}. "
                         f"NO_GO_LEDGER.md holds the no-crossing conditional on the open rung3; "
                         f"three of the four boundaries are anchor-clean, the fourth is not. "
                         f"Carry the conditionality in the same passage, or the correction has "
                         f"merely RELOCATED to whichever document you did not edit.")
