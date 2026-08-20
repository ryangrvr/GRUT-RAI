#!/usr/bin/env python3
"""test_exemption_of_one: mechanising one of this week's prose rules -- PARTIALLY, and saying so.

    "An exemption carved for a single member is not a rule, it is a hole."
    (adopted 2026-08-19, after TestSelftestMarker skipped calcs with no SELFTEST emitter on an
     assumption never checked; the exemption covered a set of size ONE, and that one was the
     defect it was meant to be exempt from.)

The standing rule this file exists under: a recorded principle protects only where it has been
converted into something that runs. Prose principles govern the next thing you NOTICE; instruments
govern the next thing you DO. So each of this week's rules gets converted, or gets counted as
unprotected.

*** THE BLIND SPOT, DECLARED UP FRONT BECAUSE IT IS THE MOTIVATING CASE ***
This test scans for NAMED COLLECTIONS that act as exemption lists. The exemption that generated
the rule was NOT one: it was control flow --

        if not emitters:
            continue          # fails by assertion instead

-- and no static scan of named collections would have caught it. Detecting "this skip path covers
exactly one member" in general requires running the loop and counting, which would mean routing
every exemption through a shared helper; that is a refactor, not minutes, and it is not done here.

SO THIS RULE IS HALF-MECHANISED, and the halves are counted separately:
    named exemption lists  -> ENFORCED here
    control-flow skips     -> STILL PROSE, therefore STILL UNPROTECTED
Recording it as "mechanised" would reproduce, in the ledger of rules, the exact overstatement the
rule is about.
"""
import ast
import glob
import os
import re
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))

# Names that mark a collection as carving something OUT of a check.
EXEMPTION_NAME = re.compile(
    r"EXEMPT|ALLOW|SKIP|IGNORE|WAIV|EXCEPT|EXCLU|OWED|WHITELIST|PERMIT|NON_|_OK$|OPT_OUT", re.I)

# Declared, with a reason. An entry here is a promise that the singleton is principled rather than
# fitted -- and it must say why, in words, so the next reader can disagree with it.
KNOWN_SINGLETONS = {
    # (file, name): reason
}


def _literal_len(value):
    if isinstance(value, (ast.Set, ast.List, ast.Tuple)):
        return len(value.elts)
    if isinstance(value, ast.Dict):
        return len(value.keys)
    if isinstance(value, ast.Call) and value.args and isinstance(
            value.args[0], (ast.Set, ast.List, ast.Tuple)):
        return len(value.args[0].elts)
    return None


def exemption_lists():
    """Every named exemption-like literal collection in provenance/, with its size."""
    out = []
    for path in sorted(glob.glob(os.path.join(HERE, "*.py"))):
        try:
            tree = ast.parse(open(path).read())
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for t in targets:
                if not isinstance(t, ast.Name) or not EXEMPTION_NAME.search(t.id):
                    continue
                n = _literal_len(node.value)
                if n is not None:
                    out.append((os.path.basename(path), t.id, n))
    return out


class TestExemptionOfOne(unittest.TestCase):

    def test_no_exemption_list_has_exactly_one_member(self):
        """A one-member exemption is a scope fitted to a case rather than a rule with a case in it.
        Either it generalises -- and then it has a second member or a stated criterion -- or it is
        a hole with a name."""
        offenders = [(f, n, k) for f, n, k in exemption_lists()
                     if k == 1 and (f, n) not in KNOWN_SINGLETONS]
        self.assertFalse(
            offenders,
            "exemption list(s) of size ONE: " + "; ".join(f"{f}:{n}" for f, n, _ in offenders) +
            ". Either generalise the criterion, remove the exemption, or declare it in "
            "KNOWN_SINGLETONS with a reason a reader can disagree with.")

    def test_the_scan_finds_the_lists_it_claims_to_cover(self):
        """A scan that matched nothing would pass this file forever while checking nothing --
        the green-vacuous failure this repository has now hit three times."""
        found = exemption_lists()
        self.assertGreaterEqual(len(found), 4,
                                f"the exemption scan found only {len(found)} named collections; "
                                f"it has probably stopped matching. Found: {found}")

    def test_the_scan_would_bite_on_a_planted_singleton(self):
        """The biting path, since a guard that cannot fail proves nothing."""
        src = "ALLOWED_THINGS = {'only_me'}\n"
        tree = ast.parse(src)
        sizes = [_literal_len(nd.value) for nd in ast.walk(tree) if isinstance(nd, ast.Assign)]
        self.assertEqual(sizes, [1])
        self.assertTrue(EXEMPTION_NAME.search("ALLOWED_THINGS"))


if __name__ == "__main__":
    unittest.main()
