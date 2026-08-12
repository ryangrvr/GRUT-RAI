"""test_merge_invariant: PINS the merge tool's cardinal invariant.

The tool validates DECLARATIONS; only ADJUDICATION decides mergers. Structural refusals are
verdicts the tool is entitled to reach; REDUCTION / TRADE / NO-REDUCTION are DECLARED READINGS --
arithmetic over analyst judgements -- and are never adjudications.

This file exists for the same reason test_harness.py pins admissible() having no `data` parameter:
the invariant is only real if something FAILS when it is violated. Without these tests a future
wave could quietly re-promote the tool to adjudicator by relabelling an output, and every downstream
reader would inherit a verdict that was only ever arithmetic.

WHY THE INVARIANT IS STRUCTURAL, not a disclaimer: three of the four judgements the test consumes
are declared non-mechanizable (derived-vs-posited, discharge-over-the-family, complete enumeration)
and the fourth requires an authored registry. Every input to the arithmetic is an analyst judgement.
Three versions each tried to close that gap and each merely MOVED where the judgement enters --
labels, then per-proposal integers, then a registry that broke its own pre-registration. A fixed
point of relocation, not convergence. Hence: IF A TOOL CANNOT BE CERTIFIED, DO NOT LET IT CERTIFY.
"""
import inspect
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import merge_criterion as MC
import merge_test as MT


def _proposal(**kw):
    base = {"relation_status_justification": "x", "discharge_at_observed_values": "x",
            "relation_axioms": "x",
            "input_enumeration_source": "x", "merge_class": "functional-relation",
            "relation": "x_B = R(x_A)", "relation_status": "derived",
            "relation_inputs": ["_ctl_xA", "_ctl_xB"],
            "inputs_sides": [["_ctl_xA"], ["_ctl_xB"]], "merged_inputs": ["_ctl_xA"],
            "new_inputs": [], "eliminates": ["_ctl_xB"]}
    base.update(kw)
    return base


class TestCardinalInvariant(unittest.TestCase):

    def test_the_two_output_kinds_are_declared_and_disjoint(self):
        self.assertTrue(MC.STRUCTURAL_VERDICTS.isdisjoint(MC.DECLARED_READINGS),
                        "the tool's two output kinds must be structurally separate -- merging them "
                        "rebuilds laundering at the scale of the ledger")
        self.assertEqual(MC.STRUCTURAL_VERDICTS, {"REFUSED-INCOMPLETE"},
                         "only the structural refusal is a verdict the tool may reach")
        self.assertEqual(MC.DECLARED_READINGS, {"REDUCTION", "TRADE", "NO-REDUCTION"})

    def test_every_scored_output_is_labelled_a_declared_reading(self):
        """A reading must announce itself as one. This is what a downstream consumer keys on."""
        r = MT.evaluate(_proposal())
        self.assertEqual(r["output_kind"], "declared-reading",
                         "a scored outcome must be labelled a DECLARED READING, never a verdict")
        self.assertIn(r["verdict"], MC.DECLARED_READINGS)

    def test_structural_refusals_are_labelled_verdicts(self):
        r = MT.evaluate(_proposal(relation_inputs=["_ctl_xA"]))   # unbound elimination
        self.assertEqual(r["verdict"], "REFUSED-INCOMPLETE")
        self.assertEqual(r["output_kind"], "structural-verdict",
                         "the structural refusal IS a verdict the tool is entitled to reach")

    def test_the_invariant_is_stated_in_the_criterion_itself(self):
        """Prose, but load-bearing prose: the next reader must meet the invariant before the API."""
        doc = MC.__doc__ or ""
        head = doc[:doc.find("merge_criterion:")] if "merge_criterion:" in doc else doc
        for phrase in ("CARDINAL INVARIANT", "NO MERGE IS BANKED FOR PASSING THIS TOOL",
                       "CANDIDATE FOR ADJUDICATION", "AUDITS THE REGISTRY BEFORE"):
            self.assertIn(phrase, head,
                          f"the criterion's header must state {phrase!r} -- the invariant is "
                          f"structural only if a reader meets it before the API")

    def test_the_tool_exposes_no_adjudication_entry_point(self):
        """A future wave must not add adjudicate()/decide()/rule() and have it look official."""
        for banned in ("adjudicate", "decide", "rule", "bank", "certify"):
            self.assertFalse(hasattr(MT, banned),
                             f"merge_test must expose no {banned}() -- the tool does bookkeeping "
                             f"on decisions already made; it does not make them")

    def test_evaluate_cannot_see_the_ledger(self):
        """The analogue of admissible() never receiving data: the scorer must not read the register.
        If it could, a reading could be tuned to the ledger it is about to move."""
        src = inspect.getsource(MT.evaluate) + inspect.getsource(MT._validate)
        for leak in ("claims.json", "ledger_delta", "open(", "json."):
            self.assertNotIn(leak, src,
                             f"evaluate/_validate must not reach the register ({leak!r} found) -- "
                             f"the scorer sees a DECLARATION, never the ledger it concerns")

    def test_registry_caveat_travels_with_the_freeze(self):
        with open(os.path.join(HERE, "FROZEN_MERGE.txt")) as f:
            frozen = f.read()
        self.assertIn("audit the REGISTRY", frozen.replace("audit the registry", "audit the REGISTRY"),
                      "the freeze record must carry the registry caveat -- the arithmetic is no "
                      "longer where the judgement lives")
        self.assertIn("NOT pre-registered", frozen,
                      "the freeze must state plainly that the registry is not pre-registered in "
                      "the full sense; v3's own fix broke that property")

    def test_every_registry_entry_carries_a_scope(self):
        """PART 1: the borrowed/GRUT separation must be a FIELD, not prose. A prose guard is the
        weak form this program has rejected three separate times."""
        for k, v in MC.ATOMIC.items():
            self.assertIn("scope", v, f"ATOMIC[{k!r}] has no scope")
            self.assertIn(v["scope"], MC.SCOPES, f"ATOMIC[{k!r}] scope {v['scope']!r} invalid")

    def test_a_borrowed_only_reduction_cannot_read_as_a_grut_ledger_move(self):
        """The exception that motivated this: born_rule is a real input to the PHYSICS at Delta 0,
        grut_standing 'borrowed'. Eliminating it is a legitimate reading and can NEVER be a GRUT
        ledger move. Structurally, not in a footnote."""
        borrowed = [k for k, v in MC.ATOMIC.items() if v["scope"] == "borrowed-physics"]
        self.assertTrue(borrowed, "the registry must carry at least one borrowed-physics entry")
        b, g = borrowed[0], "p_tt_ansatz"
        r = MT.evaluate(_proposal(relation_inputs=[g, b], inputs_sides=[[g], [b]],
                                  merged_inputs=[g], eliminates=[b]))
        self.assertEqual(r["ledger_scope_of_reduction"], "borrowed-only")
        self.assertFalse(r["can_move_grut_ledger"],
                         "a reduction eliminating only borrowed inputs must be structurally "
                         "incapable of reading as a GRUT ledger move")

    def test_a_grut_input_reduction_is_correctly_flagged_as_ledger_relevant(self):
        """The guard must DISCRIMINATE, not merely refuse everything."""
        r = MT.evaluate(_proposal(relation_inputs=["p_tt_ansatz", "born_rule"],
                                  inputs_sides=[["p_tt_ansatz"], ["born_rule"]],
                                  merged_inputs=["born_rule"], eliminates=["p_tt_ansatz"]))
        self.assertEqual(r["ledger_scope_of_reduction"], "grut")
        self.assertTrue(r["can_move_grut_ledger"])

    def test_a_reading_never_claims_to_bank_anything(self):
        for v in MC.VERDICTS.values():
            for word in ("banked", "proven", "adjudicat"):
                self.assertNotIn(word, v.lower(),
                                 f"a verdict string must not imply adjudication: {v!r}")


class TestRegistryIsTwoTables(unittest.TestCase):
    """PART 2: fixtures live in their own table and their own namespace. Structural, both ways --
    the point is that an auditor reading INPUTS is reading physics and nothing else."""

    def test_the_tables_are_disjoint_and_compose_to_the_view(self):
        self.assertFalse(set(MC.INPUTS) & set(MC.FIXTURES), "tables must not overlap")
        self.assertEqual(MC.ATOMIC, {**MC.INPUTS, **MC.FIXTURES})

    def test_no_test_data_in_the_audited_table(self):
        strays = [k for k, v in MC.INPUTS.items() if v["scope"] == "fixture"]
        self.assertEqual(strays, [], f"fixture-scoped entries in INPUTS: {strays} -- the audited "
                                     f"table must contain no test scaffolding")
        self.assertEqual([k for k, v in MC.FIXTURES.items() if v["scope"] != "fixture"], [],
                         "FIXTURES must contain nothing but fixtures")

    def test_the_namespace_boundary_holds_in_both_directions(self):
        self.assertEqual([k for k in MC.INPUTS if k.startswith("_ctl_")], [],
                         "a _ctl_ id in INPUTS means test data is being audited as physics")
        self.assertEqual([k for k in MC.FIXTURES if not k.startswith("_ctl_")], [],
                         "an unprefixed id in FIXTURES means physics is being hidden as test data")


class TestC1aAxiomBase(unittest.TestCase):
    """PART 5: 'derived relative to WHOSE axioms' is recorded per proposal, never resolved silently.
    A checklist item that does not REFUSE when absent is a comment, not a checklist item."""

    def test_the_field_is_required(self):
        self.assertIn("relation_axioms", MC.HUMAN_CHECKLIST)

    def test_a_proposal_without_an_axiom_base_is_REFUSED(self):
        r = MT.evaluate(_proposal(relation_axioms=""))
        self.assertEqual(r["verdict"], "REFUSED-INCOMPLETE",
                         "a 'derived' claim with no stated base must not be scorable -- that is "
                         "the silent resolution this field was promoted to prevent")
        self.assertTrue(any("relation_axioms" in b for b in r.get("refusals", [])),
                        f"refusal must name the missing field: {r.get('refusals')}")

    def test_the_convention_is_stated_in_the_criterion(self):
        for phrase in ("DERIVED RELATIVE TO WHOSE AXIOMS",
                       "A DERIVED-CONDITIONAL RELATION COUNTS AS POSITED"):
            self.assertIn(phrase, MC.__doc__ or "",
                          f"the criterion must state {phrase!r} where a reader meets it")


if __name__ == "__main__":
    unittest.main()
