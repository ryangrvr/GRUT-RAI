"""Tests for grut/fermionic_emergence_audit.py — Fermionic Emergence / Topological Obstruction Audit.

Covers:
  TestConstants               — PI2_REAL_SCALAR, PI2_S2, PI3_S2, HOPF_THETA_FOR_FERMION
  TestHomotopyLayers          — three layers; canonical (pi2=0); O(3) (pi2=Z, bosonic); Hopf (absent)
  TestHopfAnalysis            — hopf_term_present=False; berry phases; theta=pi
  TestSpinorContent           — all fields False; verdict contains "no_fermionic_structure"
  TestObstructionLayers       — three layers; hard/structural_gap/absent_extension types
  TestVerdict                 — computed from Booleans; mentions "obstructed" and "hopf"
  TestNonclaims               — not ruling out forever; Hopf path coherent; not claiming impossible
  TestForbiddenClaims         — o3_hedgehog_is_a_fermion not allowed; pi2_Z not fermionic
  TestMasterAudit             — end-to-end run_fermionic_emergence_audit()
  TestCrossConsistency        — pi2 gives bosonic; pi3 would give fermionic; Hopf theta=pi
"""

from __future__ import annotations

import math
import pytest

from grut.fermionic_emergence_audit import (
    PI2_REAL_SCALAR,
    PI2_S2,
    PI3_S2,
    HOPF_THETA_FOR_FERMION,
    N_MIN_HEDGEHOG,
    build_homotopy_layers,
    build_hopf_analysis,
    build_spinor_content,
    build_obstruction_layers,
    assign_verdict,
    run_fermionic_emergence_audit,
)


class TestConstants:
    def test_pi2_real_scalar_is_zero(self):
        assert PI2_REAL_SCALAR == 0

    def test_pi2_s2_is_integer_group(self):
        assert PI2_S2 == "Z"

    def test_pi3_s2_is_integer_group(self):
        assert PI3_S2 == "Z"

    def test_hopf_theta_for_fermion_is_pi(self):
        assert abs(HOPF_THETA_FOR_FERMION - math.pi) < 1e-10

    def test_hopf_theta_berry_phase(self):
        """e^{iθ} at θ=π should give -1 (fermionic)."""
        berry = math.cos(HOPF_THETA_FOR_FERMION)
        assert abs(berry - (-1.0)) < 1e-10

    def test_n_min_hedgehog(self):
        assert N_MIN_HEDGEHOG == 1


class TestHomotopyLayers:
    def setup_method(self):
        self.layers = build_homotopy_layers()

    def test_three_layers(self):
        assert len(self.layers) == 3

    def test_layer_names(self):
        names = {l.name for l in self.layers}
        assert "canonical_scalar" in names
        assert "o3_extension" in names
        assert "hopf_term" in names

    # --- canonical_scalar layer ---

    def test_canonical_pi2_is_zero(self):
        canonical = next(l for l in self.layers if l.name == "canonical_scalar")
        assert canonical.pi2 == "0"

    def test_canonical_statistics_none(self):
        canonical = next(l for l in self.layers if l.name == "canonical_scalar")
        assert canonical.statistics == "none"

    def test_canonical_present_in_grut(self):
        canonical = next(l for l in self.layers if l.name == "canonical_scalar")
        assert canonical.present_in_grut is True

    def test_canonical_vacuum_manifold_is_real_line(self):
        canonical = next(l for l in self.layers if l.name == "canonical_scalar")
        assert "R" in canonical.vacuum_manifold or "real" in canonical.vacuum_manifold.lower()

    def test_canonical_topological_charge_none(self):
        canonical = next(l for l in self.layers if l.name == "canonical_scalar")
        assert "none" in canonical.topological_charge.lower()

    def test_canonical_notes_mention_hard_obstruction(self):
        canonical = next(l for l in self.layers if l.name == "canonical_scalar")
        combined = " ".join(canonical.notes).lower()
        assert "hard" in combined or "obstruction" in combined

    # --- o3_extension layer ---

    def test_o3_pi2_is_Z(self):
        o3 = next(l for l in self.layers if l.name == "o3_extension")
        assert o3.pi2 == "Z"

    def test_o3_statistics_bosonic(self):
        o3 = next(l for l in self.layers if l.name == "o3_extension")
        assert o3.statistics == "bosonic"

    def test_o3_present_in_grut(self):
        o3 = next(l for l in self.layers if l.name == "o3_extension")
        assert o3.present_in_grut is True

    def test_o3_vacuum_manifold_s2(self):
        o3 = next(l for l in self.layers if l.name == "o3_extension")
        assert "S^2" in o3.vacuum_manifold or "S2" in o3.vacuum_manifold or "sphere" in o3.vacuum_manifold.lower()

    def test_o3_topological_charge_integer(self):
        o3 = next(l for l in self.layers if l.name == "o3_extension")
        charge = o3.topological_charge.lower()
        assert "integer" in charge or "winding" in charge

    def test_o3_notes_mention_hopf_absent(self):
        o3 = next(l for l in self.layers if l.name == "o3_extension")
        combined = " ".join(o3.notes).lower()
        assert "hopf" in combined

    def test_o3_notes_mention_bosonic(self):
        o3 = next(l for l in self.layers if l.name == "o3_extension")
        combined = " ".join(o3.notes).lower()
        assert "bosonic" in combined or "boson" in combined

    # --- hopf_term layer ---

    def test_hopf_layer_not_present_in_grut(self):
        hopf_layer = next(l for l in self.layers if l.name == "hopf_term")
        assert hopf_layer.present_in_grut is False

    def test_hopf_layer_statistics_fermionic(self):
        hopf_layer = next(l for l in self.layers if l.name == "hopf_term")
        assert "fermionic" in hopf_layer.statistics.lower()

    def test_hopf_layer_pi3_is_Z(self):
        hopf_layer = next(l for l in self.layers if l.name == "hopf_term")
        assert hopf_layer.pi3 == "Z"

    def test_hopf_layer_topological_charge_mentions_hopf(self):
        hopf_layer = next(l for l in self.layers if l.name == "hopf_term")
        assert "hopf" in hopf_layer.topological_charge.lower() or "H" in hopf_layer.topological_charge

    def test_hopf_layer_notes_mention_wilczek_zee(self):
        hopf_layer = next(l for l in self.layers if l.name == "hopf_term")
        combined = " ".join(hopf_layer.notes).lower()
        assert "wilczek" in combined or "1983" in combined

    def test_hopf_layer_notes_mention_absent(self):
        hopf_layer = next(l for l in self.layers if l.name == "hopf_term")
        combined = " ".join(hopf_layer.notes).lower()
        assert "absent" in combined

    # --- only canonical and o3 are present ---

    def test_only_two_layers_present(self):
        present = [l for l in self.layers if l.present_in_grut]
        assert len(present) == 2

    def test_hopf_is_the_absent_layer(self):
        absent = [l for l in self.layers if not l.present_in_grut]
        assert len(absent) == 1
        assert absent[0].name == "hopf_term"


class TestHopfAnalysis:
    def setup_method(self):
        self.h = build_hopf_analysis()

    def test_hopf_term_not_present(self):
        assert self.h.hopf_term_present is False

    def test_hopf_invariant_not_available(self):
        assert self.h.hopf_invariant_available is False

    def test_theta_value_required_is_pi(self):
        assert abs(self.h.theta_value_required - math.pi) < 1e-10

    def test_berry_phase_without_hopf_is_plus_one(self):
        """Without Hopf term: e^{i×0} = +1 (bosonic)."""
        assert abs(self.h.berry_phase_without_hopf - 1.0) < 1e-10

    def test_berry_phase_with_hopf_is_minus_one(self):
        """With Hopf term at θ=π: e^{iπ} = −1 (fermionic)."""
        assert abs(self.h.berry_phase_with_hopf - (-1.0)) < 1e-10

    def test_berry_phases_differ_by_sign(self):
        assert self.h.berry_phase_with_hopf == -self.h.berry_phase_without_hopf

    def test_mechanism_reference_mentions_wilczek(self):
        assert "Wilczek" in self.h.mechanism_reference or "wilczek" in self.h.mechanism_reference.lower()

    def test_mechanism_reference_mentions_1983(self):
        assert "1983" in self.h.mechanism_reference

    def test_obstruction_nonempty(self):
        assert len(self.h.obstruction) > 50

    def test_obstruction_mentions_hopf_term(self):
        assert "Hopf" in self.h.obstruction or "hopf" in self.h.obstruction.lower()

    def test_obstruction_mentions_theta(self):
        assert "theta" in self.h.obstruction.lower() or "θ" in self.h.obstruction

    def test_notes_nonempty(self):
        assert len(self.h.notes) >= 3

    def test_notes_mention_theta_pi(self):
        combined = " ".join(self.h.notes).lower()
        assert "pi" in combined or "π" in combined


class TestSpinorContent:
    def setup_method(self):
        self.s = build_spinor_content()

    def test_spin_connection_absent(self):
        assert self.s.spin_connection_present is False

    def test_clifford_algebra_absent(self):
        assert self.s.clifford_algebra_present is False

    def test_dirac_operator_absent(self):
        assert self.s.dirac_operator_present is False

    def test_anticommuting_fields_absent(self):
        assert self.s.anticommuting_fields is False

    def test_zero_mode_analysis_absent(self):
        assert self.s.zero_mode_analysis is False

    def test_index_theorem_not_invoked(self):
        assert self.s.index_theorem_invoked is False

    def test_verdict_mentions_no_fermionic_structure(self):
        assert "no_fermionic_structure" in self.s.verdict

    def test_all_fields_false(self):
        """Every structural element is absent."""
        all_false = (
            not self.s.spin_connection_present
            and not self.s.clifford_algebra_present
            and not self.s.dirac_operator_present
            and not self.s.anticommuting_fields
            and not self.s.zero_mode_analysis
            and not self.s.index_theorem_invoked
        )
        assert all_false


class TestObstructionLayers:
    def setup_method(self):
        self.obs = build_obstruction_layers()

    def test_three_obstruction_layers(self):
        assert len(self.obs) == 3

    def test_layer_numbers(self):
        nums = {o.layer for o in self.obs}
        assert nums == {1, 2, 3}

    def test_layer1_is_hard(self):
        l1 = next(o for o in self.obs if o.layer == 1)
        assert l1.obstruction_type == "hard"

    def test_layer2_is_structural_gap(self):
        l2 = next(o for o in self.obs if o.layer == 2)
        assert l2.obstruction_type == "structural_gap"

    def test_layer3_is_absent_extension(self):
        l3 = next(o for o in self.obs if o.layer == 3)
        assert l3.obstruction_type == "absent_extension"

    def test_layer1_mentions_pi2_zero(self):
        l1 = next(o for o in self.obs if o.layer == 1)
        combined = (l1.what_is_missing + " " + " ".join(l1.notes)).lower()
        assert "π₂" in combined or "pi2" in combined or "pi_2" in combined or "= 0" in combined or "=0" in combined

    def test_layer2_mentions_bosonic(self):
        l2 = next(o for o in self.obs if o.layer == 2)
        combined = (l2.what_is_missing + " " + " ".join(l2.notes)).lower()
        assert "bosonic" in combined or "boson" in combined

    def test_layer3_mentions_hopf(self):
        l3 = next(o for o in self.obs if o.layer == 3)
        combined = (l3.what_is_missing + " " + " ".join(l3.notes)).lower()
        assert "hopf" in combined

    def test_all_fixable_in_principle(self):
        for o in self.obs:
            assert o.fixable_in_principle is True, f"Layer {o.layer} should be fixable in principle"

    def test_all_have_what_would_fix(self):
        for o in self.obs:
            assert len(o.what_would_fix_it) > 20, f"Layer {o.layer} needs a fix description"

    def test_layer3_fix_requires_three_steps(self):
        l3 = next(o for o in self.obs if o.layer == 3)
        fix = l3.what_would_fix_it.lower()
        # The fix requires three things: canonical O(3), derive theta, verify Hopf
        assert "derive" in fix or "canonical" in fix or "establish" in fix


class TestVerdict:
    def setup_method(self):
        self.r = run_fermionic_emergence_audit()

    def test_verdict_nonempty(self):
        assert len(self.r.verdict) > 30

    def test_verdict_mentions_obstructed(self):
        assert "obstructed" in self.r.verdict.lower()

    def test_verdict_mentions_hopf(self):
        assert "hopf" in self.r.verdict.lower()

    def test_verdict_mentions_pi3_or_hopf_term(self):
        assert "pi3" in self.r.verdict.lower() or "hopf_term" in self.r.verdict.lower()

    def test_verdict_does_not_claim_fermionic_possible(self):
        assert "fermionic_possible" not in self.r.verdict.lower()

    def test_canonical_fermion_not_possible(self):
        assert self.r.canonical_fermion_possible is False

    def test_o3_fermion_not_possible(self):
        assert self.r.o3_fermion_possible is False

    def test_hopf_term_not_present(self):
        assert self.r.hopf_term_present is False

    def test_spinor_fields_not_present(self):
        assert self.r.spinor_fields_present is False

    def test_obstruction_type_mentions_pi2_and_hopf(self):
        ot = self.r.obstruction_type.lower()
        assert "pi2" in ot or "bosonic" in ot or "pi_2" in ot
        assert "hopf" in ot or "pi3" in ot

    def test_verdict_computed_not_hardcoded(self):
        """Verdict is computed by assign_verdict — verify it matches direct call."""
        layers = build_homotopy_layers()
        hopf = build_hopf_analysis()
        spinor = build_spinor_content()
        expected = assign_verdict(spinor, hopf, layers)
        assert self.r.verdict == expected


class TestNonclaims:
    def setup_method(self):
        self.r = run_fermionic_emergence_audit()

    def test_nonclaims_nonempty(self):
        assert len(self.r.nonclaims) >= 4

    def test_not_ruling_out_forever(self):
        combined = " ".join(self.r.nonclaims).lower()
        assert "forever" in combined or "current" in combined

    def test_hopf_path_is_coherent_extension(self):
        combined = " ".join(self.r.nonclaims).lower()
        assert "coherent" in combined or "extension" in combined

    def test_not_claiming_hopf_impossible(self):
        combined = " ".join(self.r.nonclaims).lower()
        assert "impossible" not in combined or "not" in combined

    def test_nonclaim_about_composite_fermions(self):
        """Not assessing composite fermion routes."""
        combined = " ".join(self.r.nonclaims).lower()
        assert "composite" in combined or "collective" in combined

    def test_nonclaim_about_other_mechanisms(self):
        """Zero-mode / Atiyah-Singer route is unanalysed, not closed."""
        combined = " ".join(self.r.nonclaims).lower()
        assert "zero" in combined or "atiyah" in combined or "unanalys" in combined or "other mechanism" in combined


class TestForbiddenClaims:
    def setup_method(self):
        self.r = run_fermionic_emergence_audit()

    def test_forbidden_claims_nonempty(self):
        assert len(self.r.forbidden_claims) >= 4

    def test_o3_hedgehog_is_fermion_forbidden(self):
        assert "o3_hedgehog_is_a_fermion" in self.r.forbidden_claims

    def test_pi2_Z_implies_fermionic_forbidden(self):
        assert "pi2_Z_implies_fermionic_statistics" in self.r.forbidden_claims

    def test_grut_has_spinors_forbidden(self):
        assert "grut_architecture_contains_spinor_fields" in self.r.forbidden_claims

    def test_hopf_present_forbidden(self):
        assert "hopf_term_is_present_in_o3_sector" in self.r.forbidden_claims

    def test_fermions_from_current_content_forbidden(self):
        assert "fermions_emerge_from_current_grut_field_content" in self.r.forbidden_claims


class TestMasterAudit:
    def setup_method(self):
        self.r = run_fermionic_emergence_audit()

    def test_three_homotopy_layers(self):
        assert len(self.r.homotopy_layers) == 3

    def test_three_obstruction_layers(self):
        assert len(self.r.obstruction_layers) == 3

    def test_hopf_analysis_present(self):
        assert self.r.hopf_analysis is not None

    def test_spinor_content_present(self):
        assert self.r.spinor_content is not None

    def test_diagnostics_pi2_real_scalar(self):
        assert self.r.diagnostics["PI2_REAL_SCALAR"] == 0

    def test_diagnostics_pi2_s2(self):
        assert self.r.diagnostics["PI2_S2"] == "Z"

    def test_diagnostics_pi3_s2(self):
        assert self.r.diagnostics["PI3_S2"] == "Z"

    def test_diagnostics_hopf_theta(self):
        assert abs(self.r.diagnostics["HOPF_THETA_FOR_FERMION"] - math.pi) < 1e-10

    def test_diagnostics_hopf_term_false(self):
        assert self.r.diagnostics["hopf_term_present"] is False

    def test_diagnostics_spinor_false(self):
        assert self.r.diagnostics["spinor_fields_present"] is False

    def test_diagnostics_canonical_fermion_false(self):
        assert self.r.diagnostics["canonical_fermion_possible"] is False

    def test_diagnostics_o3_fermion_false(self):
        assert self.r.diagnostics["o3_fermion_possible"] is False

    def test_diagnostics_berry_without_hopf(self):
        assert abs(self.r.diagnostics["berry_phase_without_hopf"] - 1.0) < 1e-10

    def test_diagnostics_berry_with_hopf(self):
        assert abs(self.r.diagnostics["berry_phase_with_hopf"] - (-1.0)) < 1e-10

    def test_diagnostics_o3_winding_type(self):
        assert self.r.diagnostics["o3_winding_type"] == "integer_Z"

    def test_diagnostics_o3_statistics_bosonic(self):
        assert self.r.diagnostics["o3_statistics"] == "bosonic"

    def test_diagnostics_three_obstruction_layers(self):
        assert self.r.diagnostics["num_obstruction_layers"] == 3

    def test_diagnostics_all_fixable(self):
        assert self.r.diagnostics["all_layers_fixable_in_principle"] is True

    def test_diagnostics_verdict_matches(self):
        assert self.r.diagnostics["verdict"] == self.r.verdict


class TestCrossConsistency:
    def test_pi2_gives_bosonic_pi3_gives_fermionic(self):
        """π₂(S²) = ℤ gives integer (bosonic) charge; π₃ needed for fermionic."""
        layers = build_homotopy_layers()
        o3 = next(l for l in layers if l.name == "o3_extension")
        hopf_layer = next(l for l in layers if l.name == "hopf_term")
        assert o3.pi2 == "Z"
        assert o3.statistics == "bosonic"
        assert hopf_layer.pi3 == "Z"
        assert "fermionic" in hopf_layer.statistics.lower()

    def test_hopf_absent_means_bosonic_only(self):
        """Without Hopf term, no layer provides fermionic statistics."""
        layers = build_homotopy_layers()
        present_layers = [l for l in layers if l.present_in_grut]
        for l in present_layers:
            assert "fermionic" not in l.statistics.lower(), (
                f"Layer {l.name} claims fermionic statistics but Hopf is absent"
            )

    def test_hopf_theta_pi_gives_minus_one_berry(self):
        """Berry phase e^{iπ} = −1 at θ=π."""
        hopf = build_hopf_analysis()
        assert abs(hopf.theta_value_required - math.pi) < 1e-10
        assert abs(math.cos(hopf.theta_value_required) - hopf.berry_phase_with_hopf) < 1e-10

    def test_without_hopf_berry_phase_is_even(self):
        """Without Hopf: Berry phase +1 (even, bosonic)."""
        hopf = build_hopf_analysis()
        assert hopf.berry_phase_without_hopf == +1.0

    def test_spinor_analysis_consistent_with_verdict(self):
        """No spinors → spinor_fields_present=False → verdict says obstructed."""
        spinor = build_spinor_content()
        assert spinor.anticommuting_fields is False
        r = run_fermionic_emergence_audit()
        assert r.spinor_fields_present is False
        assert "obstructed" in r.verdict.lower()

    def test_obstruction_layer_count_matches_homotopy_layers(self):
        """Three homotopy layers correspond to three obstruction layers."""
        layers = build_homotopy_layers()
        obstructions = build_obstruction_layers()
        assert len(layers) == len(obstructions) == 3

    def test_pi2_real_scalar_zero_implies_hard_obstruction(self):
        """π₂(ℝ) = 0 → layer 1 obstruction is 'hard'."""
        assert PI2_REAL_SCALAR == 0
        obstructions = build_obstruction_layers()
        l1 = next(o for o in obstructions if o.layer == 1)
        assert l1.obstruction_type == "hard"

    def test_no_pi2_zero_no_topological_charge(self):
        """Canonical scalar: π₂=0 ↔ topological_charge='none'."""
        layers = build_homotopy_layers()
        canonical = next(l for l in layers if l.name == "canonical_scalar")
        assert canonical.pi2 == "0"
        assert "none" in canonical.topological_charge.lower()

    def test_o3_present_not_hopf(self):
        """O(3) is present; Hopf layer is not. Exactly one absent."""
        layers = build_homotopy_layers()
        o3 = next(l for l in layers if l.name == "o3_extension")
        hopf_layer = next(l for l in layers if l.name == "hopf_term")
        assert o3.present_in_grut is True
        assert hopf_layer.present_in_grut is False
