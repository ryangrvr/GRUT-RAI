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
        # In-prose section references ("Part 0", "Part IV.6") and data-release identifiers
        # ("DESI DR2") are document structure and proper names, not register counts.
        stripped = re.sub(r"\bPart \d+", "", stripped)
        stripped = re.sub(r"\bFigure \d+", "", stripped)          # figure references
        stripped = re.sub(r"\]\([^)]*\)", "", stripped)            # markdown link/image targets
        stripped = re.sub(r"\bR\d\b", "", stripped)               # sealed-file rule labels
        stripped = re.sub(r"\bDR\d+\b", "", stripped)
        # THE GUARDED SET IS DERIVED, NEVER HAND-LISTED. It was hand-listed until 2026-08-18,
        # when a whole-document screen typed three emitted values into the source and the ENTIRE
        # suite stayed green -- among them n_overseer_register, the token introduced days earlier
        # precisely to stop a typed count from going stale. A hand-maintained coverage list is an
        # enforcement instrument claiming coverage it does not have, which is the defect class
        # this program keeps finding in itself. Coverage now derives from what the emitter emits,
        # so a new number cannot enter the document outside the guard.
        guarded = {k: v for k, v in n.items() if isinstance(v, int) and not isinstance(v, bool)}
        guarded.update({f"tier_{k.replace('-', '_')}": v for k, v in n["tiers"].items()})
        # Hyphenated ratios are handled by their own check below; strip them here so their
        # component digits are not ALSO reported as bare integers (the "0" in "0-of-7").
        int_scan = re.sub(r"\b\d+-of-\d+\b", "", stripped)
        # Sigma-values are check (c)'s jurisdiction, with its clause-level attribution rule;
        # strip them here so a guarded integer inside "~4σ-class" is not ALSO reported bare.
        int_scan = re.sub(r"~?\d+(?:\.\d+)?\s*(?:sigma|σ)", "", int_scan)
        # THE FOUR DECLARED EXCEPTION CLASSES, enforced rather than banned. The rule permits
        # quoted, cited, verification-pass and dated-audit-record figures WHEN MARKED at the
        # occurrence; checks (a)/(b) previously ignored the marking and so would have banned a
        # correctly-attributed historical figure that happened to equal a live register count.
        # Clause-level, like check (c) -- proximity is not attribution.
        DELIMS_AB = ".!?;:\n"
        MARKERS = (r"quoted|cited|that pass|attributed|prior deposit|literature|"
                   r"dated disclosure|dated record|the audit's|audit correction|"
                   r"its own heading records|the record's|the log's")

        def _marked(hay, start, end):
            lo = max((hay.rfind(c, 0, start) for c in DELIMS_AB), default=-1) + 1
            hi = min((x for x in (hay.find(c, end) for c in DELIMS_AB) if x != -1),
                     default=len(hay))
            return re.search(MARKERS, hay[lo:hi + 1], re.I) is not None

        offenders = []
        for name, val in guarded.items():
            # (a) as a bare integer
            # A NEGATIVE number is never one of the guarded register counts (they are all
            # non-negative tallies), so a preceding minus excludes it -- which is what lets the
            # physics ratio "exactly -2" coexist with the guard on spec_C = 2.
            m = re.search(rf"(?<![\d.\-−]){val}(?![\d.])", int_scan)
            if m and not _marked(int_scan, m.start(), m.end()):
                offenders.append(f"{name}={val} (as a digit)")
            # (b) as a spelled-out numeral -- the class that falsified the rule in its own paragraph
            # Word-forms are checked only for values > 3. Below that the numeral collides with
            # ordinary English ("two inflations are refused", "the two halves") too often to
            # discriminate, and a guard that fires on English is a guard that gets disabled.
            # DECLARED LIMITATION, not a silent carve-out: values 0-3 are placeholder-disciplined
            # but not machine-enforced in word form. Stated here so the limit is auditable.
            w = self.WORDS.get(val)
            mw = re.search(rf"\b{w}\b", stripped, re.I) if (w and val > 3) else None
            if mw and not _marked(stripped, mw.start(), mw.end()):
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

    def test_vii3_is_handed_over_unwritten(self):
        """The one section reserved for the human author must stay unwritten, and the frame must
        stay the frame. The first version of this test filtered out every blockquoted line -- but
        the frame IS a blockquote, so it was blind to the exact defect it answered (ghost-writing
        by negation, inside the quote). It now pins the frame's own content: the declared shape
        must be intact and nothing may be added to it."""
        src = open(SRC).read()
        i = src.find("## VII.3")
        self.assertGreater(i, 0, "VII.3 is missing")
        body = src[i:src.find("\n---", i)]
        lines = [ln.strip() for ln in body.split("\n")[1:] if ln.strip()]
        prose = [ln for ln in lines if not ln.startswith(">")]
        self.assertEqual(prose, [], f"VII.3 has body text outside its handover frame: {prose}")
        quoted = " ".join(ln.lstrip("> ").strip() for ln in lines)
        # the frame's declared shape, pinned sentence by sentence
        for required in [
                "must not be produced that way",
                "so it is not drafted",
                "it must not re-argue the physics",
                "must not promise future work",
                "must not thank the machinery",
                "is the author's to say and is not specified here",
                "To be written by D. Ryan Grover",
        ]:
            self.assertIn(required, quoted, f"the handover frame lost: {required!r}")
        # AND NOTHING BEYOND IT. A length cap is not enough: one added sentence slipped a
        # mutation test under a generous bound. The frame's paragraph count is pinned exactly,
        # so any inserted line inside the blockquote fails here -- which is the only form of
        # ghost-writing this section can suffer.
        paras = [ln.lstrip("> ").strip() for ln in lines if ln.lstrip("> ").strip()]
        self.assertEqual(len(paras), 4,
                         f"the handover frame is {len(paras)} paragraphs, not its declared 4 -- "
                         f"prose added inside the blockquote is ghost-writing by another route: "
                         f"{paras}")
        self.assertRegex(src, r"\*\*Outstanding:\*\* VII\.3",
                         "the completeness line must still report VII.3 outstanding")

    def test_every_generated_figure_is_placed_in_the_document(self):
        """A generated figure nobody reads is not a figure. The drift test checks
        file-versus-generator; this checks figure-versus-document -- the gap that let two of
        three figures ship unreferenced while the completeness line called them complete."""
        import build_figures
        src = open(SRC).read()
        for name in build_figures.FIGS:
            self.assertIn(f"]({name})", src, f"{name} is generated but never placed in the document")
        self.assertNotIn("enters with the figures wave", src,
                         "a figure-deferral marker survived the wave it defers to")

    def test_figure_two_tracks_the_postulate_map(self):
        """Figure 2 claims its membership is transcribed from POSTULATE_MAP.md. Bind BOTH
        directions, with explicit per-member anchors rather than any-word matching: the first
        version of this test passed a bogus member on the single word 'framework' and could not
        see a dropped member at all -- while three of Bin 4's members were in fact missing
        (re-screen mutation, 2026-08-17). Bin 4 is the results-never-inputs bin, so a dropped
        member is exactly a result the figure stops protecting."""
        import build_figures
        mp = open(os.path.join(ROOT, "POSTULATE_MAP.md")).read()
        # forward: every drawn member names a phrase the map actually contains
        for _title, members in build_figures.BINS:
            for label, anchor in members:
                self.assertIn(anchor, mp,
                              f"figure 2 draws {label!r} whose anchor {anchor!r} is not in the map")
        # backward: every member the map lists is drawn -- counted per bin section
        sections = re.split(r"^### Bin \d+", mp, flags=re.M)[1:]
        self.assertEqual(len(sections), len(build_figures.BINS),
                         "the map's bin count and the figure's disagree")
        for i, (sec, (_t, members)) in enumerate(zip(sections, build_figures.BINS), start=1):
            body = re.split(r"^#{2,3} ", sec, flags=re.M)[0].split("> ")[0]
            listed = re.findall(r"^(?:\d+\.|-)\s+\*\*", body, flags=re.M)
            self.assertEqual(len(listed), len(members),
                             f"Bin {i}: the map lists {len(listed)} members, figure 2 draws "
                             f"{len(members)} -- a member was added or dropped without the figure")

    def test_the_address_block_names_the_public_repository_and_its_hash(self):
        """The address block is this document's single pointer to its own evidence. It was
        emptied once by a check run against the wrong repository (the subtree SOURCE cannot
        resolve objects the subtree ADD created in the destination), and the correction published
        a confession to an error that had not occurred. Pins: the hash is present, and the
        wrong-repository trap is stated where a reader would otherwise repeat it."""
        src = open(SRC).read()
        self.assertRegex(src, r"commit `[0-9a-f]{12}`",
                         "the address block must carry the public repository's commit hash")
        self.assertIn("not against a working tree", src,
                      "the subtree trap must be stated where the hash is claimed")
        self.assertNotIn("named one that does not resolve", src,
                         "the manufactured-defect confession must not return")

    def test_every_source_token_is_guarded_or_declared_nonnumeric(self):
        """The guard's coverage derives from the emitter, but a token could still be added that
        the emitter exposes as a non-int (a string figure, say) and so escape check (a)/(b).
        Every placeholder the source uses must therefore be either an int the guard covers, or
        named here as deliberately non-numeric. Closes the class rather than the instance."""
        import build_public_doc as B
        import emit_public_numbers as E
        n = E.numbers()
        NON_NUMERIC = {"STAMP_DATE", "CORRECTION_DATE", "WAVE_DATE", "register_table",
                       "calc_index", "net_grut", "net_cluster", "waived_total"}
        DECIMAL_GUARDED = {"x_upper", "mu_allowance", "desi_sigma0", "isw_sigma", "isw_central",
                           "x_gate"}
        src = open(SRC).read()
        used = set(re.findall(r"\{\{([A-Za-z_0-9]+)\}\}", src))
        vals = B.values()
        for tok in sorted(used):
            self.assertIn(tok, vals, f"source uses undefined placeholder {tok!r}")
            if tok in NON_NUMERIC or tok in DECIMAL_GUARDED:
                continue
            # a tier key is ABSENT from n["tiers"] exactly when the tier is empty -- which is
            # the document's headline case -- so check the canonical vocabulary, not the
            # observed keys.
            TIERS = ("shown", "derived", "derived-pending", "assumed", "to-derive")
            base = tok[5:].replace("_", "-") if tok.startswith("tier_") else tok
            covered = isinstance(n.get(tok), int) or base in TIERS
            self.assertTrue(covered,
                            f"placeholder {tok!r} is neither an int the guard covers nor declared "
                            f"non-numeric -- it could be typed into the source undetected")

    def test_the_calc_index_and_the_calc_count_are_the_same_set(self):
        """A GENERATED TABLE AND AN EMITTED COUNT OVER THE SAME DIRECTORY MUST AGREE.

        They did not. The Appendix E table listed every `*.py` in `calc/`; the emitted `n_calcs`
        listed every `*.py` not starting with `_`. Two rules, one directory, nothing comparing
        them -- so the published table could carry a row the published count did not count. Found
        2026-08-18 when a gitignored mutant, left behind by a mutation battery, inserted itself as
        a row in the calculation index of a document that gets committed.

        The second half of that defect is pinned by test_the_calc_index_ignores_the_working_tree:
        the set is now taken from the REPOSITORY, not from the working directory, because a count
        another clone cannot reproduce is not a verifiable number."""
        import emit_public_numbers as E
        rows = [r for r in E.calc_index().splitlines() if r.startswith("| `calc/")]
        self.assertEqual(len(rows), E.numbers()["n_calcs"],
                         "Appendix E's row count and the emitted n_calcs disagree -- two rules "
                         "over one directory")

    def test_the_calc_manifest_matches_the_repository(self):
        """The published calculation set must be a property of the REPOSITORY, not of whatever is
        sitting in calc/ when the document is built -- a gitignored mutant reached Appendix E that
        way. The emitter may not shell out, so it reads a committed manifest; THIS test is what
        keeps that manifest from becoming the hand-maintained list Wave 7 found in the one-number
        guard. The truth is derived from git here and compared."""
        r = subprocess.run([sys.executable, os.path.join(HERE, "build_calc_manifest.py"),
                            "--check"], capture_output=True, text=True, timeout=120)
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_the_calc_index_ignores_the_working_tree(self):
        """Belt and braces on the same defect, at the emitter rather than the manifest: plant an
        untracked file in calc/ and require the published set to be unchanged."""
        import emit_public_numbers as E
        before = E.calc_files()
        planted = os.path.join(ROOT, "calc", "zz_untracked_probe.py")
        try:
            with open(planted, "w") as f:
                f.write("# planted by the guard suite; must not reach the published index\n")
            self.assertEqual(E.calc_files(), before,
                             "an untracked file in calc/ changed the published calculation set")
        finally:
            if os.path.exists(planted):
                os.remove(planted)
