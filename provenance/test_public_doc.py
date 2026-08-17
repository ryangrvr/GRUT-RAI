"""test_public_doc: the one-number rule enforced on the public document itself.

Three properties: the rendered file matches a fresh render (no hand-edited numbers); the SOURCE
contains no typed register count (the prohibition is on the body, not the appendix); and the
front matter's load-bearing negatives track the register rather than being asserted.
"""
import os
import re
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "docs", "WHERE_IT_STOPS.src.md")
OUT = os.path.join(ROOT, "docs", "WHERE_IT_STOPS.md")

sys.path.insert(0, HERE)


class TestPublicDoc(unittest.TestCase):

    def test_rendered_matches_source_and_register(self):
        r = subprocess.run([sys.executable, os.path.join(HERE, "build_public_doc.py"), "--check"],
                           capture_output=True, text=True, timeout=300)
        self.assertEqual(r.returncode, 0, r.stdout)

    # Number-words the guard must see. The first version checked BARE INTEGERS ONLY, so
    # "six, across", "seven versions", "1-of-18", "0-of-7", "four occasions" and "roughly 2 sigma"
    # all walked past it -- inside the paragraph advertising the rule. A guard that cannot read the
    # way the prose is written is not guarding the prose.
    WORDS = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",
             9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",
             16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty"}

    def test_the_source_types_no_register_count(self):
        """THE RULE. Every register-derived count must be a placeholder in the source. Checked by
        looking for the CURRENT values as bare integers in the source prose -- if a number that
        the register currently emits appears typed, it would silently go stale."""
        import emit_public_numbers as E
        n = E.numbers()
        src = open(SRC).read()
        # strip fenced code, inline code, and DOIs/dates, where digits are legitimate
        # PLACEHOLDERS FIRST: {{token}} is the rule's own mechanism; a digit inside a token
        # NAME (e.g. sigma0) is not a typed count. Found the hard way when {{desi_sigma0}}'s
        # trailing 0 tripped the integer scan (2026-08-17).
        stripped = re.sub(r"\{\{[A-Za-z_0-9]+\}\}", "", src)
        stripped = re.sub(r"`[^`]*`", "", stripped)                  # inline code
        stripped = re.sub(r"\d{4}-\d{2}-\d{2}", "", stripped)        # dates
        stripped = re.sub(r"10\.5281/zenodo\.\d+", "", stripped)      # DOIs
        stripped = re.sub(r"arXiv:\s*\d{4}\.\d{4,5}", "", stripped)  # arXiv ids
        stripped = re.sub(r"\[?\d{4}\.\d{4,5}\]?", "", stripped)     # bare arXiv ids in links
        stripped = re.sub(r"https?://\S+", "", stripped)              # urls
        # physics notation: superscripts, and the literal formulae this document quotes.
        # WHY THIS STRIPPING IS NOT A LOOPHOLE: the guard's job is to catch a REGISTER COUNT typed
        # as prose. "2 Im G_R^TT" and "P^(0s)/P^(2) = -2" are physics, and a guard that cannot tell
        # them from a count will either cry wolf or be switched off -- which is how guards die.
        # POWERS OF TEN are physics magnitudes, never register counts -- and they must go
        # BEFORE the bare-superscript strip, which would otherwise decapitate "10⁷" into a
        # bare "10" (found 2026-08-17 when tier_shown=10 fired on exactly that residue).
        stripped = re.sub(r"~?10[⁰¹²³⁴⁵⁶⁷⁸⁹]+[×x]?", "", stripped)
        stripped = re.sub(r"[⁰¹²³⁴⁵⁶⁷⁸⁹½]", "", stripped)
        # LIMIT NOTATION is physics, not a count: rho_TT(omega->0), lim as x -> 0, etc.
        stripped = re.sub(r"[ωx]\s*[→>-]+\s*0", "", stripped)
        # PHYSICS-STRUCTURAL NUMERALS (new class, introduced by Part I): spin labels, tensor ranks
        # and dimension compounds. "spin-2", "rank-2", "six-dimensional", "four-dimensionally" are
        # properties of the mathematics; none can go stale when the register changes, which is the
        # only failure this guard exists to prevent. Stripped, and then PROVEN not to blind the
        # guard: test_the_guard_still_bites_inside_part_I mutates a register count into Part I's
        # own prose and requires it caught.
        stripped = re.sub(r"\b(?:spin|rank|helicity)-\d+", "", stripped, flags=re.I)
        stripped = re.sub(r"\b(?:one|two|three|four|five|six|seven|eight|nine|ten|\d+)[- ]"
                          r"dimensions?(?:al(?:ly)?)?", "", stripped, flags=re.I)
        for formula in ("2 Im G_R^TT", "= -2", "= −2", "P⁽⁰ˢ⁾/P⁽²⁾", "2P", "ratio −2", "ratio -2",
                        "(i/2)", "≥ 0", ">= 0", "x = 0", "x = 1"):
            stripped = stripped.replace(formula, "")
        # BLOCKQUOTES are exception 1 by construction -- this document only block-quotes the prior
        # deposit and the literature, both of which the rule exempts and both of which are marked
        # at the quote. Stripping them here is the same exemption, mechanized.
        stripped = re.sub(r"^\s*>.*$", "", stripped, flags=re.M)
        # MARKDOWN HEADINGS and SECTION NUMBERS are document structure, not register counts:
        # "## Six fixed points", "**5 — This is not...**", "fixed point 2 requires".
        stripped = re.sub(r"^#{1,6}\s.*$", "", stripped, flags=re.M)
        stripped = re.sub(r"\*\*\d+\s*[—–-]", "", stripped)
        stripped = re.sub(r"[Ff]ixed point \d+", "", stripped)
        guarded = {"n_grut": n["n_grut"], "spec_total": n["spec_total"], "spec_B": n["spec_B"],
                   "spec_A": n["spec_A"], "spec_C": n["spec_C"], "spec_D": n["spec_D"],
                   "n_tests": n["n_tests"], "total": n["total"],
                   "n_spec_2026_06_25_nodes": n["n_spec_2026_06_25_nodes"],
                   "n_spec_2026_06_25_occurrences": n["n_spec_2026_06_25_occurrences"],
                   "tier_derived": n["tiers"].get("derived", 0),
                   "tier_derived_pending": n["tiers"].get("derived-pending", 0),
                   "tier_shown": n["tiers"].get("shown", 0),
                   "tier_assumed": n["tiers"].get("assumed", 0),
                   "tier_to_derive": n["tiers"].get("to-derive", 0)}
        # Hyphenated ratios are handled by their own check below; strip them here so their
        # component digits are not ALSO reported as bare integers (the "0" in "0-of-7").
        int_scan = re.sub(r"\b\d+-of-\d+\b", "", stripped)
        # Sigma-values are check (c)'s jurisdiction, with its clause-level attribution rule;
        # strip them here so a guarded integer inside "~4σ-class" is not ALSO reported bare.
        int_scan = re.sub(r"~?\d+(?:\.\d+)?\s*(?:sigma|σ)", "", int_scan)
        offenders = []
        for name, val in guarded.items():
            # (a) as a bare integer
            # A NEGATIVE number is never one of the guarded register counts (they are all
            # non-negative tallies), so a preceding minus excludes it -- which is what lets the
            # physics ratio "exactly -2" coexist with the guard on spec_C = 2.
            if re.search(rf"(?<![\d.\-−]){val}(?![\d.])", int_scan):
                offenders.append(f"{name}={val} (as a digit)")
            # (b) as a spelled-out numeral -- the class that falsified the rule in its own paragraph
            # Word-forms are checked only for values > 3. Below that the numeral collides with
            # ordinary English ("two inflations are refused", "the two halves") too often to
            # discriminate, and a guard that fires on English is a guard that gets disabled.
            # DECLARED LIMITATION, not a silent carve-out: values 0-3 are placeholder-disciplined
            # but not machine-enforced in word form. Stated here so the limit is auditable.
            w = self.WORDS.get(val)
            if w and val > 3 and re.search(rf"\b{w}\b", stripped, re.I):
                offenders.append(f"{name}={val} (as the word {w!r})")
        # (c) hyphenated ratios and sigma-values sourced from THIS register (not quoted, not cited)
        for pat, what in ((r"\b\d+-of-\d+\b", "a hyphenated ratio"),
                          (r"(?<!\{)\b\d+(?:\.\d+)?\s*(?:sigma|σ)", "a sigma value")):
            for m in re.finditer(pat, stripped, re.I):
                # THE EXCEPTION MARKER MUST BE IN THE SAME SENTENCE, not merely nearby. A ±200-char
                # window let a neighbouring "(quoted)" -- attached to a DIFFERENT number -- exempt
                # this one, and a mutation test caught it: an unmarked sigma sailed through because
                # the quoted 32-sigma sat two clauses away. Proximity is not attribution.
                # SEMICOLON AND COLON ARE BOUNDARIES TOO. Without them, "advertises a 32-sigma
                # exclusion *(quoted)*; this register's own recomputation returned 2.0 sigma" is
                # ONE sentence, and the quoted-marker on the first number exempts the second --
                # which a mutation test caught. Clause-level attribution, not sentence-level.
                DELIMS = ".!?;:\n"
                lo = max((stripped.rfind(c, 0, m.start()) for c in DELIMS), default=-1) + 1
                hi = min((x for x in (stripped.find(c, m.end()) for c in DELIMS) if x != -1),
                         default=len(stripped))
                sentence = stripped[lo:hi + 1]
                if not re.search(r"quoted|cited|that pass|attributed|prior deposit|literature",
                                 sentence, re.I):
                    offenders.append(f"{what} typed unmarked: {m.group(0)!r}")
        # (d) bare register-derived decimals (the Part III.2 class: the interior-family edge
        # and its neighbours). No exception machinery: these are THIS register's computed
        # values, never quotable from elsewhere.
        for name in ("x_upper", "mu_allowance", "desi_sigma0", "isw_sigma", "isw_central", "x_gate"):
            val = n.get(name)
            if not val:
                continue
            if re.search(rf"(?<![\d.{{]){re.escape(str(val))}(?![\d}}])", stripped):
                offenders.append(f"{name}={val} (as a bare decimal)")
        self.assertFalse(offenders,
                         f"register counts typed into the source prose: {offenders}. "
                         f"Use the {{{{placeholder}}}} form -- a typed count goes stale silently, "
                         f"which is the failure the prior deposit made at scale.")

    def test_the_guard_still_bites_inside_part_III(self):
        """The decimal guard (check d) must bite in the section that introduced the class.
        Mutate III.2's ceiling sentence to type the register's own decimal and require it
        caught."""
        import emit_public_numbers as E
        n = E.numbers()
        src = open(SRC).read()
        target = "admits the interior below a ceiling of roughly {{x_upper}} in x"
        self.assertIn(target, src, "III.2's ceiling sentence moved; re-anchor this mutant")
        mutated = src.replace(
            target, f"admits the interior below a ceiling of roughly {n['x_upper']} in x", 1)
        import shutil
        bak = SRC + ".bak"
        shutil.copy(SRC, bak)
        try:
            open(SRC, "w").write(mutated)
            with self.assertRaises(AssertionError):
                self.test_the_source_types_no_register_count()
        finally:
            shutil.move(bak, SRC)

    def test_the_guard_still_bites_inside_part_I(self):
        """The physics-notation strippers must not blind the guard in the section that motivated
        them. Mutate a register count into Part I's own prose and require it caught."""
        import emit_public_numbers as E
        n = E.numbers()
        src = open(SRC).read()
        i = src.find("# Part I —")
        self.assertGreater(i, 0, "Part I not found")
        mutated = (src[:i] +
                   src[i:].replace("the physical spectrum is exactly two helicities.",
                                   f"the physical spectrum is exactly two helicities, checked in "
                                   f"{n['spec_B']} configurations.", 1))
        self.assertNotEqual(mutated, src, "mutation anchor missing")
        # re-run the same scan the real test uses, on the mutated text
        import tempfile, shutil, os as _os
        bak = SRC + ".bak"
        shutil.copy(SRC, bak)
        try:
            open(SRC, "w").write(mutated)
            with self.assertRaises(AssertionError):
                self.test_the_source_types_no_register_count()
        finally:
            shutil.move(bak, SRC)

    def test_fixed_point_one_tracks_the_empty_derived_tier(self):
        import emit_public_numbers as E
        n = E.numbers()
        self.assertEqual(n["tiers"].get("derived", 0), 0,
                         "the `derived` tier is populated; fixed point 1 must be rewritten")
        self.assertIn("Zero novel positive predictions", open(SRC).read())

    def test_fixed_point_five_denies_being_the_final_deposit(self):
        src = open(SRC).read()
        self.assertIn("not the program's final deposit", src)
        self.assertIn("No stop condition has fired", src)

    def test_the_dispatch_is_described_as_unsent(self):
        src = open(SRC).read()
        self.assertTrue(re.search(r"never sent|held, and never sent|unsent", src),
                        "the document must not imply the dispatch was sent")
