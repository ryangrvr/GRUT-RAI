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


class TestDocSync(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(HERE, "claims.json")) as f:
            claims = json.load(f)["claims"]
        # SCOPED 2026-08-04: the REGISTER-SYNC markers in the standing docs describe GRUT's
        # register. Out-of-scope nodes (the vacuum-cluster map) have their own deliverable and
        # their own gate, and must not silently move GRUT's doc markers.
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


if __name__ == "__main__":
    unittest.main()
