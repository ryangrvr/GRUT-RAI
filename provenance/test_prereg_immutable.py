"""test_prereg_immutable: PINS the rule that a pre-registration is immutable once hashed.

Third instance of one shape in this program: a record that describes itself, a guard that bounds
itself, and an artifact that grows after being sealed. The response is the same each time -- make
the property structural, and make something FAIL when it is violated.
"""
import glob
import hashlib
import os
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
PREREG = os.path.join(HERE, "prereg")

# Words that mean a result has been written into a file that should hold only expectations.
RESULT_MARKERS = ("=> PASS", "=> FAIL", "RESULT, scored", "SELFTEST:", "actual:")


class TestPreregImmutable(unittest.TestCase):

    def test_every_prereg_matches_its_recorded_hash(self):
        """The seal. If a prereg is edited after the manifest records it, this fails."""
        manifest = {}
        with open(os.path.join(PREREG, "MANIFEST.txt")) as f:
            for line in f:
                parts = line.split()
                if len(parts) == 2 and len(parts[0]) == 64:
                    manifest[parts[1]] = parts[0]
        self.assertTrue(manifest, "the manifest records no pre-registration")
        for name, want in manifest.items():
            path = os.path.join(PREREG, name)
            self.assertTrue(os.path.exists(path), f"{name} is in the manifest but missing on disk")
            got = hashlib.sha256(open(path, "rb").read()).hexdigest()
            self.assertEqual(got, want,
                             f"{name}: SEAL BROKEN. A pre-registration is IMMUTABLE once hashed -- "
                             f"results cite it, they never join it. Recorded {want[:16]}, "
                             f"found {got[:16]}.")

    def test_no_prereg_contains_a_result(self):
        """Belt and braces: a prereg holds expectations. A result inside one is the failure mode
        even when the hash happens to have been re-recorded afterwards."""
        for path in glob.glob(os.path.join(PREREG, "PREREG_*.txt")):
            body = open(path).read()
            for marker in RESULT_MARKERS:
                self.assertNotIn(marker, body,
                                 f"{os.path.basename(path)} contains {marker!r} -- a result has "
                                 f"been written into a pre-registration")

    def test_every_result_cites_a_prereg_hash(self):
        for path in glob.glob(os.path.join(PREREG, "RESULT_*.txt")):
            body = open(path).read()
            self.assertIn("CITES PRE-REGISTRATION", body,
                          f"{os.path.basename(path)} does not cite the prereg it answers")
            self.assertRegex(body, r"sha256 = [0-9a-f]{64}",
                             f"{os.path.basename(path)} cites no verifiable hash")


if __name__ == "__main__":
    unittest.main()


class TestBlindSafe(unittest.TestCase):
    """THE LEAK RULE (O4, ruled 2026-08-09). The kappa wave's blinding failed through its own seal:
    PREREG_KAPPA's motive paragraph carried the tension sigmas and the arXiv id, and the blinding
    text pointed every blinded agent at that file. Sixth instance of certifier-inside-certified,
    roles inverted -- THE SEAL WAS THE LEAK. The rule: motive quantities go in a SEPARATE CITING
    file; a prereg that declares itself BLIND-SAFE must contain no result-adjacent numerics.

    The sealed kappa prereg would FAIL this check -- which is the point, and why the flag is
    opt-in: sealed history is immutable and stays as the recorded defect; every FUTURE
    observation-adjacent prereg must carry the flag and pass."""

    # Result-adjacent numerics: sigma values, tension ranges, and arXiv ids. A blind-safe prereg
    # states the QUESTION and the EXPECTATIONS; the motive's numbers live in a separate citing file.
    import re as _re
    LEAK_PATTERNS = (
        (_re.compile(r"[-+]?\d+\.\d+\s*(?:sigma|σ)"), "a sigma value"),
        (_re.compile(r"[-+]\d+\.\d+\s*(?:to|-)\s*[-+]?\d+\.\d+"), "a signed numeric range"),
        (_re.compile(r"arXiv:\s*\d{4}\.\d{4,5}", _re.I), "an arXiv id"),
    )

    def _preregs(self):
        return sorted(glob.glob(os.path.join(PREREG, "PREREG_*.txt")))

    def test_blind_safe_preregs_carry_no_result_adjacent_numerics(self):
        checked = 0
        for path in self._preregs():
            body = open(path).read()
            if "BLIND-SAFE: yes" not in body:
                continue
            checked += 1
            for pat, what in self.LEAK_PATTERNS:
                m = pat.search(body)
                # NB: build the message only on failure -- an f-string evaluates eagerly, and the
                # first draft crashed on the PASSING path (m is None), a path that could not fire
                # until the first blind-safe prereg existed. A guard untested on its green path.
                if m is not None:
                    self.fail(f"{os.path.basename(path)} declares BLIND-SAFE but contains {what} "
                              f"({m.group(0)!r}). Motive quantities go in a separate citing file; "
                              f"a blinded reader of this prereg has been unblinded by the seal "
                              f"itself.")
        # No assertion on checked>0: the flag is opt-in and no blind-safe prereg exists yet.

    def test_the_kappa_prereg_would_have_failed(self):
        """The check must BITE on the real defect, not merely exist. Run the leak patterns against
        the sealed kappa prereg (unflagged, so exempt in the live check) and require a hit --
        if the patterns cannot catch the leak that actually happened, they are decorative."""
        path = os.path.join(PREREG, "PREREG_KAPPA_2026-08-05.txt")
        body = open(path).read()
        hits = [what for pat, what in self.LEAK_PATTERNS if pat.search(body)]
        self.assertTrue(hits, "the sealed kappa prereg contains the leak that motivated this rule; "
                              "patterns that cannot find it would certify nothing")
