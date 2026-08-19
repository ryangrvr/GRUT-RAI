"""test_mutation_battery: ENFORCES the calc-layer floor (provenance/mutation_registry.py).

The standing rule: every calc producing a load-bearing number ships a mutation battery whose
mutants make its own selftest FAIL. This test is the enforcement -- the calc-layer equivalent of
the bank-gate.

What it checks:
  1. CONTROL       -- each battery calc passes UNMUTATED (otherwise "the mutant failed" proves
                      nothing).
  2. THE BATTERY   -- each mutant makes the calc FAIL. A surviving mutant is a test failure.
  3. ANCHORS       -- every mutant's `find` string still exists in its calc (so a refactor cannot
                      silently turn a battery into a no-op -- the isw_tt_auto lesson in a new form).
  4. THE RATCHET   -- OWED may only shrink; a load-bearing calc cannot be added without a battery.
  5. COVERAGE      -- every calc cited by claims.json is either batteried or explicitly OWED.

Slow batteries (declared `slow: True`) have their DECLARATION and ANCHORS enforced always, and
their mutants executed only under GRUT_FULL_MUTATION=1 (keeps the default suite fast without
letting the requirement lapse).
"""
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
CALC = os.path.join(os.path.dirname(HERE), "calc")
sys.path.insert(0, HERE)

import mutation_registry as MR

FULL = os.environ.get("GRUT_FULL_MUTATION") == "1"


def _dir_for(spec):
    """Batteries may live outside calc/ -- the rule is about load-bearing NUMBERS, not folders."""
    return os.path.join(os.path.dirname(HERE), spec.get("dir", "calc")) \
        if spec.get("dir", "calc") != "provenance" else HERE


def _run(path, timeout=900, cwd=None):
    """Run a calc; return (ok, mechanism, tail).

    MECHANISM matters (firewall 2026-08-04): a mutant that dies on an incidental TypeError is not
    evidence that the calc's CHECKS caught a wrong answer -- it is evidence the program broke. The
    battery only proves something when a CHECK rejects the answer, so the mechanism is classified
    and asserted, not conflated into a boolean.
      'selftest'  -- the calc's own selftest reported FAIL   (strongest)
      'assertion' -- an assert in the calc's body rejected it (strong: a check fired)
      'crash'     -- anything else nonzero                    (does NOT count as caught)
    """
    try:
        r = subprocess.run([sys.executable, path], capture_output=True, text=True,
                           timeout=timeout, cwd=cwd or CALC)
    except subprocess.TimeoutExpired:
        return False, "crash", "TIMEOUT"
    out = r.stdout + r.stderr
    if "SELFTEST: FAIL" in out:
        return False, "selftest", out[-400:]
    if r.returncode != 0:
        mech = "assertion" if "AssertionError" in out else "crash"
        return False, mech, out[-400:]
    return True, "passed", out[-400:]


def _write_mutant(name, src, into=None):
    """Write a mutant INTO the calc dir so its sibling imports resolve; caller removes it.
    Unique per-process (firewall 2026-08-04: deterministic names made two concurrent runs collide
    by construction, and an interrupted run left a deliberately-broken .py in the source tree)."""
    p = os.path.join(into or CALC, f"_mutant_{os.getpid()}_{name}.py")
    with open(p, "w") as f:
        f.write(src)
    return p


class TestMutationBattery(unittest.TestCase):

    def test_anchors_still_present(self):
        """A refactor must not silently turn a battery into a no-op (always enforced, incl. slow)."""
        for calc, spec in MR.BATTERIES.items():
            src = open(os.path.join(_dir_for(spec), calc)).read()
            for name, find, _repl, _why in spec["mutants"]:
                self.assertIn(find, src,
                              f"{calc}: mutant '{name}' anchor no longer exists -- the battery is "
                              f"a NO-OP. Repair the anchor or the mutant is not testing anything.")
                self.assertEqual(src.count(find), 1,
                                 f"{calc}: mutant '{name}' anchor is ambiguous ({src.count(find)}x)")

    def test_every_mutant_is_caught(self):
        """The rule itself: a pre-registered wrong answer must make the selftest FAIL."""
        for calc, spec in MR.BATTERIES.items():
            if spec.get("slow") and not FULL:
                continue
            d = _dir_for(spec)
            path = os.path.join(d, calc)
            src = open(path).read()
            ok, _mech, tail = _run(path, cwd=d)
            self.assertTrue(ok, f"CONTROL FAILED: {calc} does not pass unmutated -- the battery "
                                f"proves nothing until this is fixed.\n{tail}")
            for name, find, repl, why in spec["mutants"]:
                mpath = _write_mutant(f"{calc[:-3]}_{name}", src.replace(find, repl), into=d)
                try:
                    mok, mech, mtail = _run(mpath, cwd=d)
                finally:
                    if os.path.exists(mpath):
                        os.remove(mpath)
                self.assertFalse(mok,
                                 f"MUTANT SURVIVED: {calc} :: {name}\n  installs: {why}\n"
                                 f"  The selftest passed with a pre-registered WRONG answer in "
                                 f"place. No number from this calc may bank until the selftest "
                                 f"catches it.\n{mtail}")
                self.assertNotEqual(mech, "crash",
                                    f"MUTANT CAUGHT FOR THE WRONG REASON: {calc} :: {name} died "
                                    f"incidentally (not via a check). A battery only proves "
                                    f"something when a CHECK rejects the answer -- re-anchor the "
                                    f"mutant so the calc's own guards fire.\n{mtail}")

    def test_owed_list_only_shrinks(self):
        """The ratchet: a load-bearing calc cannot be introduced without a battery."""
        self.assertTrue(set(MR.OWED).issubset(MR.OWED_CEILING),
                        f"OWED GREW: {sorted(set(MR.OWED) - set(MR.OWED_CEILING))} -- a calc was "
                        f"added to the owed list. The rule is that OWED only shrinks; give the "
                        f"calc a battery instead.")
        self.assertFalse(set(MR.OWED) & set(MR.BATTERIES),
                         "a calc is listed both OWED and batteried")

    def test_every_register_cited_calc_is_accounted_for(self):
        """Coverage: no calc cited by the register is silently uncovered."""
        blob = open(os.path.join(HERE, "claims.json")).read()
        cited = set(re.findall(r"calc/([A-Za-z0-9_]+\.py)", blob))   # case-sensitivity hole
                                                                     # fixed 2026-08-04 (firewall)
        # calcs named as OWED-to-be-built (they do not exist yet) are not coverage failures
        cited = {c for c in cited if os.path.exists(os.path.join(CALC, c))}
        accounted = set(MR.BATTERIES) | set(MR.OWED)
        missing = cited - accounted
        self.assertFalse(missing,
                         f"UNACCOUNTED load-bearing calcs (cited by claims.json, neither batteried "
                         f"nor OWED): {sorted(missing)}. Add a battery, or add to OWED with a "
                         f"reason -- silence is not an option.")

    def test_batteries_declare_their_reason(self):
        """A battery is a PRE-REGISTRATION of failure modes, not a coverage exercise."""
        for calc, spec in MR.BATTERIES.items():
            self.assertTrue(spec["mutants"], f"{calc}: empty battery")
            for name, _f, _r, why in spec["mutants"]:
                self.assertGreater(len(why), 40,
                                   f"{calc}::{name}: the mutant must state WHAT WRONG ANSWER it "
                                   f"installs, in words.")


if __name__ == "__main__":
    unittest.main()


class TestComparisonRule(unittest.TestCase):
    """THE COMPARISON RULE (2026-08-05): agreement without discriminating power is not evidence."""

    def test_every_comparison_calc_exposes_both_numbers(self):
        import importlib.util
        from mutation_registry import COMPARISON_CALCS
        root = os.path.dirname(HERE)
        for fname, why in COMPARISON_CALCS.items():
            path = os.path.join(root, "calc", fname)
            self.assertTrue(os.path.exists(path), f"{fname} listed but missing")
            spec = importlib.util.spec_from_file_location(fname[:-3], path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            r = mod.report()
            for key in ("agreement_sigma", "discrimination_sigma"):
                self.assertIn(key, r["lock"],
                              f"{fname} compares a prediction to a measurement but does not report "
                              f"{key!r} -- agreement alone is the match temptation in numbers")

    def test_a_low_discrimination_comparison_says_so(self):
        """If the instrument cannot adjudicate, the calc must SAY it cannot -- silence would let a
        0.4-sigma 'fit' read as support, which is exactly what happened."""
        import importlib.util
        from mutation_registry import COMPARISON_CALCS
        root = os.path.dirname(HERE)
        for fname in COMPARISON_CALCS:
            path = os.path.join(root, "calc", fname)
            spec = importlib.util.spec_from_file_location(fname[:-3], path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            r = mod.report()
            if r["lock"]["discrimination_sigma"] < 2.0:
                src = open(path).read().upper()
                self.assertTrue("CANNOT ADJUDICATE" in src or "NOT EVIDENCE" in src,
                                f"{fname} has discrimination "
                                f"{r['lock']['discrimination_sigma']:.2f} sigma but nowhere states "
                                f"that the comparison cannot adjudicate")


class TestSelftestMarker(unittest.TestCase):
    """A battery can only prove something if the harness can tell a CHECK from a CRASH.

    _run() classifies a mutant as caught-by-a-check on the exact string "SELFTEST: FAIL". Two
    calcs shipped "SELFTEST FAILED:" instead -- no colon -- so their checks fired and were
    recorded as crashes: a working guard reading as proving nothing, the mirror of a broken guard
    reading as managed. Calcs that fail via assertions are fine (mech == "assertion"); this pins
    only the calcs that PRINT a verdict.

    THIS TEST WAS WRONG TWICE BEFORE IT WAS RIGHT, and the attempts are recorded rather than
    quietly rewritten, because the pattern is the finding. (1) It first required the literal
    "SELFTEST: FAIL" in the SOURCE -- nine false alarms, because those calcs build the marker with
    an f-string, f"SELFTEST: {'PASS' if ok else 'FAIL'}". (2) It then required the substring
    "SELFTEST: " -- one more false alarm, because print("  SELFTEST:", "FAIL") emits the right
    text from source in which the colon is followed by a quote, not a space. A guard checking the
    string instead of the behaviour, written to catch a guard checking the string instead of the
    behaviour, twice. (3) It now NORMALISES the line -- strips the punctuation that separates
    string literals -- and then asks for the colon form, which is what the emitted text actually
    depends on. Verified against all three idioms and against the real defect.

    THE STANDING LIMIT, since two wrong versions is enough evidence for it: a static read of a
    print statement cannot in general determine what it emits. The authoritative discriminator is
    the runtime one that already exists -- _run()'s crash-versus-check classification -- and this
    test is only a cheap early warning for it, not a replacement."""

    @staticmethod
    def _normalise(line):
        """Drop the punctuation that separates string literals, so that the three idioms
        print("SELFTEST: FAIL") / print(f"SELFTEST: {...}") / print("SELFTEST:", "FAIL")
        all reduce to text containing 'SELFTEST:' followed by whitespace."""
        return line.replace('"', ' ').replace("'", ' ').replace(",", " ")

    def test_batteried_calcs_use_the_marker_the_harness_matches(self):
        for calc, spec in MR.BATTERIES.items():
            path = os.path.join(_dir_for(spec), calc)
            if not os.path.exists(path):
                continue
            emitters = [ln for ln in open(path).read().splitlines()
                        if "SELFTEST" in ln and "print(" in ln]
            if not emitters:
                continue          # fails by assertion instead; _run() classifies that correctly
            self.assertTrue(any("SELFTEST:" in self._normalise(ln) for ln in emitters),
                            f"{calc} prints a selftest verdict but no emitter uses the COLON form "
                            f"that test_mutation_battery._run() matches. Its checks would be "
                            f"classified as CRASHES and its battery would prove nothing while "
                            f"looking maintained. Emitters seen: {emitters}")

    def test_this_guard_still_catches_the_real_defect(self):
        """The green path plus the biting path -- a guard that has been wrong twice must show it
        can still fail on the thing it exists for."""
        n = self._normalise
        self.assertNotIn("SELFTEST:", n('print("SELFTEST FAILED:")'),
                         "the guard must still reject the missing-colon form that caused this")
        for good in ('print("SELFTEST: FAIL")',
                     'print(f"SELFTEST: {\'PASS\' if ok else \'FAIL\'}")',
                     'print("  SELFTEST:", "FAIL")'):
            self.assertIn("SELFTEST:", n(good), f"false alarm on a valid idiom: {good}")
