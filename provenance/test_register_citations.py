"""test_register_citations: any artifact asserting what a register field SAYS must quote it
verbatim with the node id and field name, and the quote must VERIFY against claims.json.

WHY THIS EXISTS (2026-08-10) -- THE PHYSICS THIS GUARD PROTECTS, named per the growth policy:
the sealed termination pre-registration v2 asserted the register's rung7 overturning clauses
were "structural (a passive single-pole kernel exhibited to cross)". The actual
rung7_wz.overturning_computation is a wa-sign / parameter-count condition -- something else
entirely. The misquote ran in the FLATTERING direction (it made the kill channel harder to
fire than the source supports) and was INVISIBLE TO SEVEN ROUNDS OF INTERNAL REVIEW (P1-P7),
because every internal check audited the document's structure -- buckets, triggers, thresholds,
ranking -- and none audited its citations of the register. An outside reviewer caught it by
direct comparison. The program audits the register against itself and audits documents against
the register; it had NEVER audited a document's claims ABOUT the register. Same shape as
layer-5 ("a falsifier that cannot be run is a falsifiability claim the register cannot back"):
a register claim that is not quoted verbatim cannot be "inherited".

MATCHING RULE: whitespace runs are collapsed to single spaces on both sides before comparing
(a wrapped text document cannot carry a one-line JSON field byte-exactly), and that is the ONLY
normalization -- no case folding, no punctuation loosening, no ellipsis stitching. The first
run of this very test caught its own v3 target on a line-wrap; the normalization is the fix,
the strictness is the point.

CITATIONS is the coverage list: (artifact_path relative to repo root, claim_id, field,
verbatim_quote). The test asserts BOTH directions:
  (1) the quote appears verbatim in the artifact (the artifact actually says what is
      registered here), and
  (2) the quote is a verbatim substring of the named register field (the register actually
      says what the artifact claims).
A register edit that breaks a sealed document's citation FIRES here -- the resolution is a new
sealed version or an explicit staleness record, never silence. The list may GROW (adding
citations is adding coverage); removing an entry requires removing or superseding the artifact.
"""
import json
import os
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

CITATIONS = [
    # The termination condition v3: every register assertion it makes, quoted and pinned.
    ("provenance/prereg/PREREG_TERMINATION_V3_2026-08-10.txt",
     "rung7_wz", "overturning_computation",
     "if the full in-in (Calzetta-Hu) stress tensor of a horizon-relaxing vacuum gives wa>0 "
     "(not DESI's wa<0), or needs as many params as CPL, rung7 FAILS as the second "
     "differentiator"),
    ("provenance/prereg/PREREG_TERMINATION_V3_2026-08-10.txt",
     "method_novelty", "overturning_computation",
     "GRADUATES toward a banked contribution ONLY on independent EXTERNAL validation -- a "
     "DIFFERENT team, on a DIFFERENT problem, where the method's discipline catches a REAL "
     "error (not its own)"),
    ("provenance/prereg/PREREG_TERMINATION_V3_2026-08-10.txt",
     "mu_linear", "boundary_condition",
     "if rung3 resolves AGAINST the trace-correlator route (Pi_0 != 0 established)"),
    # Added at the pre-seal stress pass (U5 delivery check): every register assertion v3
    # makes is quoted and covered, not only the three the reviewer flagged.
    ("provenance/prereg/PREREG_TERMINATION_V3_2026-08-10.txt",
     "method_novelty", "overturning_computation",
     "Absent that it stays to-derive (a promising in-house discipline, not a banked "
     "contribution)"),
    ("provenance/prereg/PREREG_TERMINATION_V3_2026-08-10.txt",
     "rung7_w3_nocrossing_export", "statement",
     "RUNG7-SIGN sub-claim W3 (the consequence, open, default-BROKEN): IF W2's no-crossing "
     "graduates"),
    ("provenance/prereg/PREREG_TERMINATION_V3_2026-08-10.txt",
     "rung3_single_pole", "sub_status",
     "SPINE TEST RUN 2026-07-04: earned-under-determined, externally reviewed"),
    ("provenance/prereg/PREREG_TERMINATION_V3_2026-08-10.txt",
     "zeta_interior_family", "boundary_condition",
     "The family ALLOWS up to the edge; it predicts nothing (x has no floor)"),
    # Added at the second pre-seal stress pass (five uncovered assertions found).
    ("provenance/prereg/PREREG_TERMINATION_V3_2026-08-10.txt",
     "mu_linear", "overturning_computation",
     "graduation now runs ONLY through the rung3 dynamical route (Pi_0 = 0 forced, costing "
     "a new +1 at rung3)"),
    ("provenance/prereg/PREREG_TERMINATION_V3_2026-08-10.txt",
     "rung7_w3_nocrossing_export", "tier",
     "to-derive"),
    ("provenance/prereg/PREREG_TERMINATION_V3_2026-08-10.txt",
     "method_novelty", "boundary_condition",
     "this is the 'different problem' half of the falsifier's graduation condition ONLY"),
    ("provenance/prereg/PREREG_TERMINATION_V3_2026-08-10.txt",
     "x_no_pin_theorem", "statement",
     "the floor restates as x_diss(omega) >= 0 pointwise"),
    ("provenance/prereg/PREREG_TERMINATION_V3_2026-08-10.txt",
     "zeta_interior_family", "boundary_condition",
     "conditional on the vacuum kernel's chi_inf >= 0 (rung3's domain), the quasi-static x "
     "inherits the floor -- never unconditionally"),
    # v4 (the one-page rebuild): its Q1-Q3 are the ONLY register text it uses, per its R4.
    ("provenance/prereg/PREREG_TERMINATION_V4_2026-08-10.txt",
     "rung7_wz", "overturning_computation",
     "if the full in-in (Calzetta-Hu) stress tensor of a horizon-relaxing vacuum gives wa>0 "
     "(not DESI's wa<0), or needs as many params as CPL, rung7 FAILS as the second "
     "differentiator"),
    ("provenance/prereg/PREREG_TERMINATION_V4_2026-08-10.txt",
     "zeta_interior_family", "boundary_condition",
     "The family ALLOWS up to the edge; it predicts nothing (x has no floor)"),
    ("provenance/prereg/PREREG_TERMINATION_V4_2026-08-10.txt",
     "method_novelty", "overturning_computation",
     "GRADUATES toward a banked contribution ONLY on independent EXTERNAL validation -- a "
     "DIFFERENT team, on a DIFFERENT problem, where the method's discipline catches a REAL "
     "error (not its own)"),
]


def _register():
    with open(os.path.join(HERE, "claims.json")) as f:
        return {c["id"]: c for c in json.load(f)["claims"]}


def _norm(text):
    """Collapse whitespace runs to single spaces -- the only permitted normalization."""
    return " ".join(text.split())


class TestRegisterCitations(unittest.TestCase):

    def test_every_registered_citation_verifies_both_ways(self):
        by = _register()
        for path, cid, field, quote in CITATIONS:
            full = os.path.join(ROOT, path)
            self.assertTrue(os.path.exists(full),
                            f"{path}: cited artifact missing on disk")
            body = _norm(open(full).read())
            q = _norm(quote)
            self.assertIn(q, body,
                          f"{path}: does not contain the registered verbatim quote of "
                          f"{cid}.{field} -- the citation list and the artifact have drifted")
            self.assertIn(cid, by, f"{path} cites unknown claim id {cid!r}")
            src = _norm(by[cid].get(field) or "")
            self.assertIn(q, src,
                          f"{path}: quotes {cid}.{field} as saying something the field does "
                          f"NOT say verbatim. A document may not 'inherit' register text it "
                          f"does not quote exactly -- this is the v2/C2 defect class.")

    def test_the_v2_misquote_would_have_failed(self):
        """The check must BITE on the defect that motivated it (the blind-safe precedent:
        a guard that cannot catch the failure that actually happened certifies nothing).
        Sealed v2 asserts the rung7 clause is 'a passive single-pole kernel exhibited to
        cross'; verify that assertion is present in sealed v2 (immutable history) and that it
        does NOT verify against the actual register field."""
        v2 = open(os.path.join(HERE, "prereg", "PREREG_TERMINATION_2026-08-10.txt")).read()
        bad = "a passive single-pole kernel exhibited to cross"
        self.assertIn(bad, v2, "the sealed v2 defect text is the calibration case; if v2 was "
                               "edited, the seal is broken (see test_prereg_immutable)")
        actual = _register()["rung7_wz"].get("overturning_computation") or ""
        self.assertNotIn(bad, actual,
                         "rung7_wz.overturning_computation now contains the phrase v2 "
                         "misattributed to it -- if the register changed, re-adjudicate; "
                         "as sealed, this phrase was a misquote")


if __name__ == "__main__":
    unittest.main()
