"""test_layer5_overturning: WIRES LAYER 5 -- every overturning_computation that names a calc must
name one that EXISTS and EXITS 0.

resident.py's own docstring listed this as "LATER" from the beginning; the external review
(2026-08-09) called it: a falsifier path that doesn't exist, or crashes, is a falsifiability claim
the register cannot back. EXISTENCE is enforced always; EXECUTION is gated behind GRUT_RUN_SLOW=1
(same contract as the slow mutation batteries -- several cited calcs run minutes each), and the
gating is DECLARED here rather than silent.
"""
import json
import os
import re
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FULL = os.environ.get("GRUT_RUN_SLOW") == "1"
PAT = re.compile(r"(calc/[A-Za-z0-9_]+\.py)")


def _cited():
    claims = json.load(open(os.path.join(HERE, "claims.json")))["claims"]
    out = {}
    for c in claims:
        for m in PAT.finditer(c.get("overturning_computation") or ""):
            out.setdefault(m.group(1), []).append(c["id"])
    return out


class TestLayer5(unittest.TestCase):

    def test_every_cited_falsifier_path_exists(self):
        missing = {p: ids for p, ids in _cited().items()
                   if not os.path.exists(os.path.join(ROOT, p))}
        self.assertFalse(missing,
                         f"overturning_computation cites calc paths that DO NOT EXIST: {missing}. "
                         f"A falsifier that cannot be run is a falsifiability claim the register "
                         f"cannot back.")

    def test_the_register_actually_cites_calcs(self):
        """Guard the guard: if the regex ever rots, this fails rather than existence passing
        vacuously over an empty set."""
        self.assertGreater(len(_cited()), 3)

    def test_every_cited_falsifier_exits_zero(self):
        if not FULL:
            self.skipTest("execution gated: set GRUT_RUN_SLOW=1 (several cited calcs run minutes "
                          "each); existence is enforced unconditionally above")
        for p in sorted(_cited()):
            r = subprocess.run([sys.executable, os.path.join(ROOT, p)],
                               capture_output=True, text=True, timeout=1800)
            self.assertEqual(r.returncode, 0,
                             f"{p} exits {r.returncode}:\n{r.stdout[-800:]}\n{r.stderr[-800:]}")


if __name__ == "__main__":
    unittest.main()
