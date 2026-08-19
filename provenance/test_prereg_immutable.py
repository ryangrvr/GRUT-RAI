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

    # ------------------------------------------------------------------------------------------
    # THE ONE NAMED, DELIBERATE EXCEPTION (ruled 2026-08-18, recorded here rather than repaired).
    #
    # A blind-safe pre-registration may state, IN WORDS AND WITHOUT FIGURES OR SOURCES, that its
    # own threshold is AS YET UNMET. The in-force DESI threshold seal (v3) does exactly this:
    # "no published result has met the threshold below by a model-independent route, and the
    # framework is not falsified by present data."
    #
    # WHY IT IS EXEMPT RATHER THAN A DEFECT: a pre-registration that could not say its threshold
    # is as yet unmet would have NO PROSPECTIVE CONTENT -- it would be indistinguishable from a
    # post-hoc reading. The statement is near-tautological, since a threshold already met would
    # not be worth freezing, and it hands a blinded reader nothing: no significance, no
    # comparison, no direction of the current preference, no route to any of them.
    #
    # RECORDED, NOT REPAIRED, ON PURPOSE. This file has already been superseded three times in one
    # day; a fourth supersession for a residual both parties agree is defensible would be
    # over-correction with a credibility cost of its own, and a seal should not have to carry its
    # own exception list. The exception lives here, in the guard's documentation, where anyone
    # auditing the guard meets it.
    #
    # SCOPE, STATED SO IT CANNOT BE STRETCHED: the exemption covers the BARE UNMET-NESS of the
    # frozen threshold. It does NOT cover which parametrizations are favoured, which re-analyses
    # moved which figure, how close any result came, any identifier, or any pointer to a file
    # carrying those. The leak patterns below remain in force against all of it.
    # ------------------------------------------------------------------------------------------

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
        # COLLECTS EVERY CASE, does not stop at the first. A set-valued guard that fails fast
        # reports one member even when three are broken -- and once that one member is declared
        # expected-red, the other two are invisible. See numeric_leak_cases() and expected_red.py.
        # (The green path is exercised by test_the_sealed_v3_predicate_survives_its_own_guard: an
        # earlier draft of this test built its failure f-string eagerly and crashed when nothing
        # matched -- a guard untested on its passing path.)
        cases = sorted(numeric_leak_cases())
        if cases:
            self.fail("blind-safe pre-registrations carrying result-adjacent numerics "
                      f"({len(cases)}): " + "; ".join(cases) +
                      " -- motive quantities go in a separate citing file; a blinded reader of "
                      "such a prereg has been unblinded by the seal itself.")
        # No assertion on non-emptiness of the blind-safe set: the flag is opt-in.

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
        # COLLECTS EVERY CASE. Same reason as above, and this test is the one that proved it:
        # it is one set-valued test over every sealed blind-safe prereg, so declaring it red once
        # declared it red for every file that would ever join the set.
        cases = sorted(pointer_leak_cases())
        if cases:
            self.fail(f"blind-safe pre-registrations naming a companion that leaks "
                      f"({len(cases)}): " + "; ".join(cases) +
                      " -- the pointer IS the leak. Citation runs COMPANION -> SEAL only.")


# ---------------------------------------------------------------------------------------------
# CASE ENUMERATORS -- the single implementation of each blind-safe check.
#
# WHY THESE EXIST, AND WHY THE TESTS ARE THIN WRAPPERS AROUND THEM. A declared expected-red is
# declared at (test, CASE) granularity, not at test granularity, because DECLARING A SET-VALUED
# TEST RED SILENCES IT FOR EVERY FUTURE MEMBER OF THE SET. That is a property of
# classification-at-test-granularity, not of any one test -- see SCREEN_RECORD, "Declaring a
# set-valued test red silences it for every future member of the set."
#
# Three consumers, one implementation:
#   the tests            assert the case set is empty;
#   expected_red.py      diffs the case set against what is declared, so a NEW member is a NEW red
#                        even while the test is a declared failure;
#   seal.py              runs the SINGLE-FILE forms against a candidate BEFORE it is hashed, which
#                        is the only moment at which the answer can still change.

def blind_safe_preregs():
    """Every sealed pre-registration that OPTS IN to the blind-safe rule."""
    out = []
    for path in sorted(glob.glob(os.path.join(PREREG, "PREREG_*.txt"))):
        if "BLIND-SAFE: yes" in open(path).read():
            out.append(path)
    return out


def numeric_leaks_in(path):
    """Result-adjacent numerics in ONE file. Returns a description per matching pattern."""
    body = open(path).read()
    return [what for pat, what in TestBlindSafe.LEAK_PATTERNS if pat.search(body) is not None]


# THE CHARACTER CLASS, AND WHY IT IS NOT WIDER. The first form of this pattern was
# `(?:RESULT|CITES)_[A-Za-z0-9_]+\.txt` -- NO HYPHEN. Every dated artifact in this repository is
# named `NAME_YYYY-MM-DD.txt`, so the pattern could only ever match the handful of UNDATED targets,
# and the pointer defect it was written for -- a dated companion -- was invisible to it. Measured
# consequence, not a hunch: with the hyphen, three further live cases appear, including the one
# this guard's own declaration had claimed it was catching.
# Widening further was TESTED AND REJECTED. Following every `*.txt|md|json|py` token flags a
# blind-safe prereg for naming `claims.json` -- naming the register unblinds nobody -- and rakes in
# calculation scripts and dispatch memos. The `RESULT_`/`CITES_` convention IS the defect class:
# what unblinds a reader is a pointer at a file of RESULTS.
_POINTER = re.compile(r"\b(?:RESULT|CITES)_[A-Za-z0-9_-]+\.txt")


def pointer_leaks_in(path):
    """Outbound pointers from ONE file that LAND on leaking material.

    Follows the pointer rather than matching the name: a blind-safe prereg may legitimately name a
    companion whose content cannot unblind anyone. What makes a pointer a leak is where it lands.
    Returns (companion, description) pairs."""
    body = open(path).read()
    out = []
    for m in re.finditer(_POINTER, body):
        target = os.path.join(PREREG, m.group(0))
        if not os.path.exists(target):
            # NOT SILENTLY SKIPPED. A pointer at a file that does not exist yet is still a route:
            # the seal is immutable and the target can be written tomorrow. Reported as its own
            # case so it is visible and declarable rather than invisible.
            out.append((m.group(0), "an unresolved pointer -- target not on disk"))
            continue
        for what in numeric_leaks_in(target):
            out.append((m.group(0), what))
    return out


def numeric_leak_cases():
    return {f"{os.path.basename(p)} :: {what}"
            for p in blind_safe_preregs() for what in numeric_leaks_in(p)}


def pointer_leak_cases():
    return {f"{os.path.basename(p)} -> {tgt} :: {what}"
            for p in blind_safe_preregs() for tgt, what in pointer_leaks_in(p)}
