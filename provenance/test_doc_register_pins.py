"""test_doc_register_pins: the book must not go stale when the register moves.

The counts in the public document are emitted, the tables generated, the figures regenerated --
all three drift-checked. PROSE was the unguarded leg: a tier change, a demotion, a retirement or a
price change would leave every sentence describing it stale with nothing failing. This test is
that leg. A failure here is not a defect to be repaired by editing this file -- it is the prompt
to re-read the prose citing the moved node and then re-pin (doc_register_pins.py --accept), which
is a human act asserting the prose was reconciled.
"""
import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))


class TestDocRegisterPins(unittest.TestCase):
    def test_the_document_is_current_with_the_register(self):
        r = subprocess.run([sys.executable, os.path.join(HERE, "doc_register_pins.py")],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0,
                         "the register moved under the document's prose:\n" + r.stdout)

    def test_the_pin_check_actually_fires(self):
        """Proven to bite, in-test, against a copied register: a node the document cites, moved
        in a field the prose depends on, MUST fail the check. A guard nothing can fail is
        decoration -- this program's own recurring finding."""
        import json
        import shutil
        import tempfile
        claims_p = os.path.join(HERE, "claims.json")
        with open(claims_p) as f:
            d = json.load(f)
        cited = json.load(open(os.path.join(HERE, "doc_register_pins.json")))["nodes"]
        target = sorted(cited)[0]
        for c in d["claims"]:
            if c["id"] == target:
                c["tier"] = "shown" if c["tier"] != "shown" else "to-derive"
                break
        bak = claims_p + ".pintest"
        shutil.copy(claims_p, bak)
        try:
            with open(claims_p, "w") as f:
                json.dump(d, f, indent=1)
            r = subprocess.run([sys.executable, os.path.join(HERE, "doc_register_pins.py")],
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 1,
                             "a cited node changed tier and the pin check passed -- it is blind")
            self.assertIn(target, r.stdout)
        finally:
            shutil.move(bak, claims_p)


if __name__ == "__main__":
    unittest.main()
