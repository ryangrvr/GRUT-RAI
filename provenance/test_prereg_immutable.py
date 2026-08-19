"""test_prereg_immutable: PINS the rule that a pre-registration is immutable once hashed.

Third instance of one shape in this program: a record that describes itself, a guard that bounds
itself, and an artifact that grows after being sealed. The response is the same each time -- make
the property structural, and make something FAIL when it is violated.
"""
import glob
import re
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
    # THE DECIMAL CONVENTION, WRITTEN DOWN BECAUSE THE GUARD DEPENDED ON IT SILENTLY.
    # The original sigma pattern required a decimal point, so it caught a cited result ("3.2 sigma")
    # and missed a frozen threshold ("5 sigma"). That discrimination was doing real work and nothing
    # recorded that it was deliberate -- one edit from a threshold written "5.0 sigma"
    # false-positiving, or a cited result written "4 sigma" walking through. Both halves are now
    # taken: the convention is stated HERE (thresholds are written round, results decimal), AND the
    # pattern no longer relies on it -- it catches any sigma value and exempts only the BOUND FORM
    # (">= N sigma", "at least N sigma"), which is what a threshold looks like and what a reported
    # result does not.
    # Variable-width look-behind is unsupported, so the bound form is matched POSITIVELY and
    # skipped, rather than excluded by look-behind.
    _BOUND_FORM = re.compile(r"(?:>=|≥|at least|no less than)\s*\d+(?:\.\d+)?\s*(?:sigma|σ)",
                             re.I)

    class _SigmaQuantity:
        """Any sigma value that is NOT stated as a bound. A threshold reads '>= 5 sigma'; a
        reported result reads '3.2 sigma' or '4 sigma'. Only the second unblinds a reader."""
        def __init__(self, bound):
            self._all = re.compile(r"\d+(?:\.\d+)?\s*(?:sigma|σ)", re.I)
            self._bound = bound

        def search(self, body):
            skip = [(m.start(), m.end()) for m in self._bound.finditer(body)]
            for m in self._all.finditer(body):
                if not any(s <= m.start() and m.end() <= e for s, e in skip):
                    return m
            return None

    LEAK_PATTERNS = (
        (_SigmaQuantity(_BOUND_FORM),
         "a sigma value stated as a quantity rather than as a bound"),
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

    def test_the_desi_v1_prereg_would_have_failed(self):
        """Twin of the kappa test, on the second real defect in the record. DESI DR3 v1 is sealed,
        immutable, and violates its own BLIND-SAFE declaration -- which makes it the ideal fixture:
        a pattern that cannot find the defect that motivated it certifies nothing. If a future edit
        loosens the patterns, this fails."""
        path = os.path.join(PREREG, "PREREG_DESI_DR3_2026-08-18.txt")
        self.assertTrue(os.path.exists(path), "the v1 fixture is missing")
        body = open(path).read()
        self.assertIn("BLIND-SAFE: yes", body, "the fixture no longer declares blind-safe")
        hits = [what for pat, what in self.LEAK_PATTERNS if pat.search(body)]
        self.assertTrue(hits, "the leak patterns no longer catch the DESI v1 defect they were "
                              "re-verified against")

    def test_the_sealed_v3_predicate_survives_its_own_guard(self):
        """The green path, tested -- the lesson from the f-string note above, applied. The frozen
        predicate states a BOUND ('>= 5 sigma'); that is a threshold, not a reported result, and
        the guard must not fire on it. A guard that cannot pass its own legitimate input gets
        switched off."""
        path = os.path.join(PREREG, "PREREG_DESI_DR3_2026-08-18_v3.txt")
        self.assertTrue(os.path.exists(path), "v3 is missing")
        body = open(path).read()
        self.assertIn("BLIND-SAFE: yes", body)
        for pat, what in self.LEAK_PATTERNS:
            m = pat.search(body)
            self.assertIsNone(m, f"v3's clean predicate false-positives on {what}: {m.group(0)!r}"
                                 if m else "")

    def test_no_sealed_prereg_points_outward_at_its_own_context(self):
        """THE KAPPA DEFECT, PINNED. Removing motive figures from a blind-safe prereg accomplishes
        nothing if the prereg still NAMES the file they moved to -- a blinded reader follows the
        name and arrives at exactly what the blinding was for. The guard's own docstring records
        this ('the blinding text pointed every blinded agent at that file'), and the repair for the
        v1 violation reproduced it one hop out. Citation runs COMPANION -> SEAL only: a citing file
        binds itself to a sealed predicate by hash; the seal never reaches back."""
        for path in self._preregs():
            body = open(path).read()
            if "BLIND-SAFE: yes" not in body:
                continue
            # FOLLOW THE POINTER, do not match the name. A blind-safe prereg may legitimately
            # name a companion whose content cannot unblind anyone -- the termination condition
            # names its own event log by architecture, and that log holds events, not motive
            # figures. What makes a pointer a leak is where it LANDS. So the target is fetched and
            # run through the same leak patterns: a pointer to a file that leaks, leaks.
            # (Over-firing here would be its own defect -- over-demotion is a defect too, and this
            # test found a false positive on its first run before this was added.)
            for m in re.finditer(r"\b(?:RESULT|CITES)_[A-Za-z0-9_]+\.txt", body):
                target = os.path.join(PREREG, m.group(0))
                if not os.path.exists(target):
                    continue
                tbody = open(target).read()
                leaks = [what for pat, what in self.LEAK_PATTERNS if pat.search(tbody)]
                if leaks:
                    self.fail(f"{os.path.basename(path)} is blind-safe and names "
                              f"{m.group(0)!r}, which contains {leaks[0]} -- the pointer is the "
                              f"leak. Citation runs COMPANION -> SEAL only.")
