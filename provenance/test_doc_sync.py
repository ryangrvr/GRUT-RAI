"""Doc-sync standing test (3e): the four standing docs carry a REGISTER-SYNC marker that must match
the live register. Converts count/net drift (the class the 2026-08 review caught: three docs saying
'32 claims' against a 43-node register) from a manual sweep into a standing test.

Marker format, one per doc:  <!-- REGISTER-SYNC: <N> nodes, net +<NET> -->
"""
import json
import os
import re
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

DOCS = ["STATE.md", "POSTULATE_MAP.md", "GRUT_II_Agenda.md", "GRUT_I_What_Survived.md", "GRUT_ToE.md", "README.md",
    "GRUT_II_What_Survived.md",   # added 2026-08-04: it carries a REGISTER-SYNC
    "X_FLOOR_MAP.md",            # marker that nothing was enforcing (firewall finding)
]
MARKER = re.compile(r"<!-- REGISTER-SYNC: (\d+) nodes, net \+(\d+) -->")
# B1 (2026-08-10): the sync marker's count is GRUT-scope and readers running len(claims) got 70 --
# so every marker now travels with a TOTAL stamp naming BOTH counts and BOTH nets. Machine-checked
# here so the stamps derive from the register rather than being hand-maintained prose.
TOTAL = re.compile(r"<!-- REGISTER-TOTAL: (\d+) = (\d+) grut \+ (\d+) vacuum-cluster; "
                   r"nets \+(\d+) grut, \+(\d+) cluster -->")


class TestDocSync(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(HERE, "claims.json")) as f:
            claims = json.load(f)["claims"]
        # SCOPED 2026-08-04: the REGISTER-SYNC markers in the standing docs describe GRUT's
        # register. Out-of-scope nodes (the vacuum-cluster map) have their own deliverable and
        # their own gate, and must not silently move GRUT's doc markers.
        self.total = len(claims)
        cluster = [c for c in claims if c.get("ledger_scope") == "vacuum-cluster"]
        self.n_cluster = len(cluster)
        self.net_cluster = sum(c.get("ledger_delta", 0) for c in cluster
                               if isinstance(c.get("ledger_delta"), int)
                               and not isinstance(c.get("ledger_delta"), bool))
        claims = [c for c in claims if c.get("ledger_scope", "grut") == "grut"]
        self.n = len(claims)
        self.net = sum(c.get("ledger_delta", 0) for c in claims
                       if isinstance(c.get("ledger_delta"), int) and not isinstance(c.get("ledger_delta"), bool))

    def test_every_standing_doc_matches_live_register(self):
        for doc in DOCS:
            with open(os.path.join(ROOT, doc)) as f:
                text = f.read()
            markers = list(MARKER.finditer(text))
            self.assertTrue(markers, f"{doc}: missing REGISTER-SYNC marker")
            for m in markers:  # ALL markers in a doc must match, not just the first
                self.assertEqual(int(m.group(1)), self.n,
                                 f"{doc}: marker says {m.group(1)} nodes, register has {self.n}")
                self.assertEqual(int(m.group(2)), self.net,
                                 f"{doc}: marker says net +{m.group(2)}, register nets +{self.net}")
            totals = list(TOTAL.finditer(text))
            self.assertEqual(len(totals), len(markers),
                             f"{doc}: every REGISTER-SYNC marker must travel with a REGISTER-TOTAL "
                             f"stamp (found {len(markers)} sync, {len(totals)} total) -- the "
                             f"GRUT-count/full-count ambiguity is what let '49 nodes' read as "
                             f"falsified against a 70-claim file")
            for t in totals:
                got = tuple(int(t.group(i)) for i in range(1, 6))
                want = (self.total, self.n, self.n_cluster, self.net, self.net_cluster)
                self.assertEqual(got, want,
                                 f"{doc}: REGISTER-TOTAL stamp {got} != register {want}")


if __name__ == "__main__":
    unittest.main()


class TestAnchorConditionalityTravels(unittest.TestCase):
    """ENFORCEMENT HOOK (2026-08-10c, overseer-found). The four-boundaries anchor claim was
    corrected in STATE.md and NOT in GRUT_I_What_Survived.md -- which STATE.md itself calls
    "the label-for-label deposit", i.e. the document written for external readers. The
    correction landed in the internal snapshot and skipped the public one.

    That is the RELOCATION pattern, not a new error class: fixing an inconsistency in one of two
    documents MOVES it instead of closing it. A claim this load-bearing must not depend on
    someone remembering both sites, so it is carried here the way the register stamps are.

    THE AUTHORITY IS THE LEDGER: NO_GO_LEDGER.md holds the no-crossing "conditional on the open
    `rung3` (a no-go cannot outrank its anchor) -- held `to-derive`." Any document asserting the
    boundaries are clean of the anchor must carry that conditionality in the same breath."""

    PHRASE = "clean of the open anchor"
    # the qualifier that must accompany it -- any of these forms
    QUALIFIERS = ("anchor-conditional", "anchor-CONDITIONAL", "conditional on the open",
                  "THREE of the four", "three are clean")
    WINDOW = 1200   # chars after the phrase within which the qualifier must appear

    def test_the_ledger_still_states_the_conditionality(self):
        """Guard the authority itself: if the ledger's own line is ever softened, this fires
        first -- otherwise the docs below could be 'corrected' toward a claim nobody holds."""
        with open(os.path.join(ROOT, "NO_GO_LEDGER.md")) as f:
            led = f.read()
        self.assertIn("conditional on the open", led,
                      "NO_GO_LEDGER is the authority on boundary strength grades; its "
                      "anchor-conditionality line is missing")
        self.assertIn("a no-go cannot outrank its anchor", led)

    def test_no_doc_asserts_anchor_cleanliness_unqualified(self):
        import glob
        offenders = []
        for path in sorted(glob.glob(os.path.join(ROOT, "*.md"))):
            with open(path) as f:
                text = f.read()
            for m in re.finditer(re.escape(self.PHRASE), text):
                window = text[max(0, m.start() - self.WINDOW):m.start() + self.WINDOW]
                if not any(q in window for q in self.QUALIFIERS):
                    offenders.append(f"{os.path.basename(path)} @ char {m.start()}")
        self.assertFalse(offenders,
                         f"unqualified anchor-cleanliness assertion at: {offenders}. "
                         f"NO_GO_LEDGER.md holds the no-crossing conditional on the open rung3; "
                         f"three of the four boundaries are anchor-clean, the fourth is not. "
                         f"Carry the conditionality in the same passage, or the correction has "
                         f"merely RELOCATED to whichever document you did not edit.")


class TestSpecialistNeverUnqualifiedInPublicDocs(unittest.TestCase):
    """B0.2 ENFORCEMENT (2026-08-12). In this register "specialist" denotes, 22 times out of 41,
    a pass that was RUN and banked -- with the modality never recorded, and no logged transmission
    to any outside human at any date. In a public document the word says "human expert" to every
    reader. The register keeps its historical text; PUBLIC-FACING documents may not use the word
    without naming the modality in the same sentence.

    Scoped to public documents by an explicit list, so adding a public doc is a deliberate act
    that opts into the rule."""

    PUBLIC_DOCS = ["GRUT_V1_PLAIN.md", "DISPATCH_ONE_PAGE.md", "README.md", "HOW_TO_VERIFY.md"]
    # A public doc may use the word only if the qualification appears NEAR it -- in EITHER
    # direction. The first draft looked forward only, and immediately mis-flagged the correction
    # notes it had just caused to be written (where the qualifier precedes the quoted word). A
    # one-directional window is the wrong shape for a rule about a word travelling with its
    # qualifier.
    WINDOW = 400
    QUALIFIERS = ("AI-relayed", "AI relayed", "in-house", "no outside", "unsent", "drafted",
                  "never answered", "no human", "AI-assisted", "would be", "outside experts",
                  "prospective", "owner-run", "outside human",
                  # A mention that POINTS THE READER AT THE AUDIT is qualified by construction --
                  # that is what the glossary entry is for. Without this the rule mis-flags its
                  # own correction notes, which is the guard eating its own remedy.
                  "GLOSSARY")

    def test_no_public_doc_uses_specialist_unqualified(self):
        import glob
        offenders = []
        for name in self.PUBLIC_DOCS:
            path = os.path.join(ROOT, name)
            if not os.path.exists(path):
                continue
            text = open(path).read()
            # CASE-INSENSITIVE, and the reason is recorded because this exact defect recurred:
            # the B0.2 audit's own pattern was r"[Ss]pecialists?" -- a character class on the FIRST
            # LETTER ONLY -- which silently dropped every ALL-CAPS "SPECIALIST" (8 of 49 in the
            # register, 6 of them the dangerous class). This guard was written with the same bug
            # and missed 2 public-doc occurrences. Third recorded instance of case-sensitive-audit-
            # regex in this program (the coverage regex that let two calcs escape was the prior).
            for m in re.finditer(r"specialists?", text, re.I):
                # NARROW, NAMED EXEMPTION: the literal filename token SPECIALIST_BRIEF*. A path is
                # a path -- it makes no assertion about who did what. Kept deliberately narrow
                # (exact token, not "any uppercase use") because carve-outs are how guards rot;
                # the filename's own misleading-ness is recorded in GLOSSARY.md instead.
                if text[m.start():m.start() + 16].upper().startswith("SPECIALIST_BRIE"):
                    continue
                window = text[max(0, m.start() - self.WINDOW):m.start() + self.WINDOW]
                if not any(q in window for q in self.QUALIFIERS):
                    offenders.append(f"{name} @ char {m.start()}: "
                                     f"...{text[max(0, m.start()-90):m.start()+90]}...")
        self.assertFalse(offenders,
                         "unqualified use of 'specialist' in a public document:\n  " +
                         "\n  ".join(offenders) +
                         "\n\nIn this register the word denotes an owner-run pass 22 times out of "
                         "41, modality never recorded, with NO logged transmission to any outside "
                         "human at any date. Name the modality in the same sentence or drop the "
                         "word. See GLOSSARY.md, the 2026-08-12 B0.2 audit entry.")

    def test_the_glossary_carries_the_audit(self):
        with open(os.path.join(ROOT, "GLOSSARY.md")) as f:
            g = f.read()
        # NB: this list first pinned "41 occurrences" -- the WRONG count -- so when the glossary
        # was corrected to 49 the test FAILED, defending the error it was written alongside. A
        # guard that hard-codes a figure inherits that figure's mistakes. The count is now checked
        # AGAINST THE REGISTER below instead of being hard-coded here.
        for phrase in ("what the register has actually meant",
                       "never records the modality", "No transmission to any external human"):
            self.assertIn(phrase.lower(), g.lower(),
                          f"GLOSSARY.md is missing the B0.2 audit element: {phrase!r}")
        # The stated count must equal a live count -- taken from THE EMITTER, not re-derived here.
        # Re-deriving is exactly how these two drifted apart: the emitter learned to exclude the
        # dated annotation blocks (which necessarily contain the audited words, so annotating
        # inflated the count 49 -> 58) and this test did not, so it demanded the inflated figure.
        # One source of truth, or the guard and the thing it guards disagree.
        import emit_public_numbers as EPN
        _n = EPN.numbers()
        live, nodes = _n["spec_total"], _n["spec_nodes"]
        self.assertIn(f"{live} occurrences", g,
                      f"GLOSSARY.md must state the LIVE count ({live}); a hard-coded audit figure "
                      f"is how the first run's undercount survived review")
        self.assertIn(f"across {nodes} of {_n['total']} claims", g)


class TestProseMatchesTheMarker(unittest.TestCase):
    """THE MARKER WAS CHECKED AND THE SENTENCES BESIDE IT WERE NOT.

    On 2026-08-19 STATE.md -- the standing snapshot -- opened with "net +13, all seals verify"
    while its own machine-emitted REGISTER-SYNC marker two lines below said net +15, and 49 nodes
    against the marker's 50. test_doc_sync verified the COMMENT and never read the PROSE, so a
    public-facing headline could contradict the instrument sitting in the same file.

    THE RULE, stated as a criterion rather than an exemption list (an exemption carved for a
    single member is a hole): every "net +N" in a standing doc must either be the register's
    CURRENT net, or sit on a line carrying an explicit HISTORICAL cue. A sentence that asserts a
    net with no cue is asserting the present."""

    HIST = ("->", "→", "stayed", "was ", "at that adjudication", "deposit", "History",
            "as of", "superseded", "Version I", "earlier", "then **+", "first net-ledger move")
    NET = re.compile(r"net \*{0,2}\+(\d+)")

    def _current_net(self):
        with open(os.path.join(HERE, "claims.json")) as f:
            claims = json.load(f)["claims"]
        return sum(c.get("ledger_delta", 0) for c in claims
                   if c.get("ledger_scope", "grut") == "grut"
                   and isinstance(c.get("ledger_delta"), int)
                   and not isinstance(c.get("ledger_delta"), bool))

    def test_no_standing_doc_asserts_a_stale_net(self):
        cur = self._current_net()
        for doc in DOCS:
            path = os.path.join(ROOT, doc)
            if not os.path.exists(path):
                continue
            for i, line in enumerate(open(path, encoding="utf-8").read().splitlines(), 1):
                for m in self.NET.finditer(line):
                    if int(m.group(1)) == cur:
                        continue
                    if any(cue in line for cue in self.HIST):
                        continue
                    self.fail(f"{doc}:{i} asserts {m.group(0)!r} with no historical cue, but the "
                              f"register's current net is +{cur}. Either correct the figure or "
                              f"mark the sentence as history.\n    {line.strip()[:160]}")

    def test_the_rule_would_have_caught_the_2026_08_19_defect(self):
        """Biting path: the exact sentence that stood in STATE.md for a fortnight."""
        stale = "The register below is held, not growing: gates green, bank-gate CLEAN, net +13, all seals verify."
        m = self.NET.search(stale)
        self.assertIsNotNone(m, "the pattern must match the real sentence")
        self.assertNotEqual(int(m.group(1)), self._current_net())
        self.assertFalse(any(cue in stale for cue in self.HIST),
                         "the offending sentence carries no historical cue, so the rule fires")
