"""test_emergence_chain: the chain regenerates from the register, or it is stale.

The design rule under test: the stage->claims mapping is authored, EVERY STATUS IS GENERATED.
A narrative that can drift from its register is the doc-sync failure in a new costume; a generated
one cannot drift without this failing."""
import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))


class TestEmergenceChain(unittest.TestCase):

    def test_no_drift(self):
        r = subprocess.run([sys.executable, os.path.join(HERE, "emergence_chain.py"), "--check"],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, f"chain drifted from the register:\n{r.stdout}")

    def test_coverage_guard_fires(self):
        """THE MUTATION: a generator whose coverage guard cannot fire would let a GRUT node vanish
        from the story silently -- the exact 'gap you cannot see' the chain exists to prevent."""
        import emergence_chain as EC
        popped = EC.OFF_CHAIN.pop("rung8_falsifier")
        try:
            with self.assertRaises(SystemExit) as cm:
                EC.generate()
            self.assertIn("neither in the chain nor declared off-chain", str(cm.exception))
        finally:
            EC.OFF_CHAIN["rung8_falsifier"] = popped

    def test_chain_node_banked_at_zero(self):
        import json
        by = {c["id"]: c for c in json.load(open(os.path.join(HERE, "claims.json")))["claims"]}
        n = by["emergence_chain"]
        self.assertEqual(n["ledger_delta"], 0, "the chain asserts no new physics; delta must be 0")
        self.assertEqual(n["tier"], "to-derive")
