#!/usr/bin/env python3
"""test_expected_red: the mutation battery for the CLASSIFICATION layer.

This layer decides which failures are allowed to be red, so a defect in it is worse than a defect
in any single guard: it can silence guards wholesale. Its first version did exactly that -- it
matched failures by TEST NAME, so declaring one set-valued guard red silenced it for every member
that set would ever acquire, permanently, since declarations of sealed defects cannot be withdrawn.

Every mutant below must be REFUSED. A classifier that cannot fail on its own defect is decorative,
and this one certifies the others.

pytest is stubbed with the true failing set: the battery is testing the classifier, not the suite,
and running the suite from inside the suite would recurse.
"""
import contextlib
import io
import types
import unittest

import expected_red as X

POINTER = ("test_prereg_immutable.py::TestBlindSafe::"
           "test_no_sealed_prereg_points_outward_at_its_own_context")


class TestExpectedRed(unittest.TestCase):

    def setUp(self):
        self._subprocess = X.subprocess
        self._passes = X.open_passes
        failing = "\n".join("FAILED " + t for t in X.DECLARED)
        X.subprocess = types.SimpleNamespace(
            run=lambda *a, **k: types.SimpleNamespace(returncode=1, stdout=failing))

    def tearDown(self):
        X.subprocess = self._subprocess
        X.open_passes = self._passes

    def _run(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = X.main()
        return rc, buf.getvalue()

    def test_the_declared_state_is_accepted(self):
        """The green path. A classifier that cannot pass its own valid input gets switched off."""
        rc, out = self._run()
        self.assertEqual(rc, 0, out)

    def test_a_declaration_citing_a_closed_pass_is_refused(self):
        """The adjudication closes, the test keeps failing for an unrelated reason, and the runner
        would otherwise print green while citing a ruling that already happened. Staleness cannot
        catch it -- stale fires only when a test starts PASSING."""
        base = X.open_passes()
        X.open_passes = lambda: {**base, "P1-RUNG1-TIER": "CLOSED"}
        rc, out = self._run()
        self.assertEqual(rc, 1)
        self.assertIn("CLOSED PASS", out)

    def test_a_declaration_citing_an_unknown_pass_is_refused(self):
        base = X.open_passes()
        X.open_passes = lambda: {k: v for k, v in base.items()
                                 if k != "P4-TERMINATION-KAPPA-RESULT"}
        rc, out = self._run()
        self.assertEqual(rc, 1)
        self.assertIn("UNKNOWN PASS", out)

    def test_a_new_member_of_a_declared_set_is_a_new_red(self):
        """THE HOLE THIS LAYER WAS REBUILT FOR. A third file with a defect already on the books
        must not inherit that defect's declaration."""
        real = X.DECLARED[POINTER]["enumerate"]
        try:
            X.DECLARED[POINTER]["enumerate"] = lambda: set(real()) | {"PREREG_THIRD.txt -> x"}
            rc, out = self._run()
        finally:
            X.DECLARED[POINTER]["enumerate"] = real
        self.assertEqual(rc, 1)
        self.assertIn("NEW RED (case)", out)

    def test_a_case_that_is_no_longer_produced_is_refused(self):
        cases = X.DECLARED[POINTER]["cases"]
        try:
            cases["PREREG_GHOST.txt -> gone"] = "P2-TERMINATION-EVENTLOG"
            rc, out = self._run()
        finally:
            del cases["PREREG_GHOST.txt -> gone"]
        self.assertEqual(rc, 1)
        self.assertIn("STALE CASE", out)

    def test_a_declared_test_failing_for_an_unmodelled_reason_is_refused(self):
        """The declaration's enumerator finds nothing, yet the test fails: it is failing for a
        reason this declaration does not model -- a new red wearing an old declaration's name."""
        real = X.DECLARED[POINTER]["enumerate"]
        try:
            X.DECLARED[POINTER]["enumerate"] = lambda: set()
            rc, out = self._run()
        finally:
            X.DECLARED[POINTER]["enumerate"] = real
        self.assertEqual(rc, 1)
        self.assertIn("UNMODELLED FAILURE", out)

    def test_every_declaration_supplies_an_enumerator(self):
        """Structural: a declaration without an enumerator would be a test-granularity declaration
        smuggled back in, and would carry the blind spot this file exists to prevent."""
        for test, d in X.DECLARED.items():
            self.assertTrue(callable(d.get("enumerate")),
                            f"{test} declares no enumerator -- its case set cannot be diffed")
            self.assertTrue(d.get("cases"), f"{test} declares no cases")


if __name__ == "__main__":
    unittest.main()
