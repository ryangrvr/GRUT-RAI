"""Regression tests for Priority 4 — neutrino hierarchy via Z_3 / Koide.

Pins the framework's Standard-Model-sector predictions for the
neutrino mass spectrum:

  - Canonical Z_3 (a = √2 from charged leptons) DOES NOT extend to
    neutrinos (minimum Δm²_atm/Δm²_sol = 194.7, vs observed 33.9)
  - Generalized Z_3 with a_ν = 1 admits NH interior solution
  - IH at a_ν = 1 sits at m_3 → 0 boundary (degenerate, fine-tuned)
  - GRUT predicts: NORMAL HIERARCHY, m_1 ≈ 0.8 meV, Σm_ν ≈ 60 meV
  - Cosmologically consistent with Planck Σm_ν < 0.12 eV
  - Falsifiable by JUNO/DUNE/Hyper-K hierarchy + DESI/Euclid Σm_ν

The deliverable is a SHARP PREDICTION conditional on the postulate
a_ν = 1 (whose derivation from GRUT primitives is open). The
precision of the Σm_ν prediction (60 meV) is well within reach of
near-future cosmological surveys.
"""

from __future__ import annotations

import numpy as np


# ─────────────────────────────────────────────────────────────────────
# Module imports
# ─────────────────────────────────────────────────────────────────────


class TestModuleImports:
    def test_module_importable(self):
        from grut.derived.koide import neutrino_hierarchy  # noqa
        assert hasattr(neutrino_hierarchy, "verify")

    def test_API_exports(self):
        from grut.derived.koide.neutrino_hierarchy import (
            convention_declaration,
            s_values,
            koide_K,
            all_positive,
            minimum_ratio_canonical_z3,
            canonical_z3_fits_neutrinos,
            neutrino_solution,
            grut_prediction_NH,
            grut_prediction_IH,
            hierarchy_preference,
            consistency_with_planck,
            observational_tests_summary,
            verify,
            A_CHARGED_LEPTON,
            A_NEUTRINO_POSTULATE,
            DELTA_M_SQ_SOL_EV2,
            DELTA_M_SQ_ATM_NH_EV2,
            DELTA_M_SQ_ATM_IH_EV2,
            SIGMA_M_NU_PLANCK_BOUND_EV,
        )
        # Constants
        assert abs(A_CHARGED_LEPTON - np.sqrt(2)) < 1e-12
        assert A_NEUTRINO_POSTULATE == 1.0
        assert DELTA_M_SQ_SOL_EV2 == 7.42e-5
        assert SIGMA_M_NU_PLANCK_BOUND_EV == 0.12


class TestVerifyHarness:
    def test_verify_all_legs_pass(self):
        """Priority 4 + 4B verify() now has 11 legs (8 original + 3 uniqueness)."""
        from grut.derived.koide.neutrino_hierarchy import verify
        v = verify()
        for k, val in v.items():
            assert val is True, f"Priority 4/4B verify() leg failed: {k} = {val}"

    def test_verify_includes_uniqueness_theorem_legs(self):
        """The Priority 4B uniqueness theorem must be exercised in verify()."""
        from grut.derived.koide.neutrino_hierarchy import verify
        v = verify()
        assert "boundary_gap_vanishes_at_a_1" in v
        assert "boundary_gap_positive_for_a_above_1" in v
        assert "boundary_inaccessible_for_a_below_1" in v


# ─────────────────────────────────────────────────────────────────────
# Convention declaration
# ─────────────────────────────────────────────────────────────────────


class TestConventionDeclaration:
    def test_C1n_z3_ansatz_form(self):
        from grut.derived.koide.neutrino_hierarchy import (
            convention_declaration,
        )
        d = convention_declaration()
        c1 = d["C1n_z3_ansatz"]
        assert "1 + a cos" in c1 or "(1+a" in c1
        assert "2π" in c1 or "2pi" in c1.lower()

    def test_C2n_K_value_formula(self):
        from grut.derived.koide.neutrino_hierarchy import (
            convention_declaration,
        )
        d = convention_declaration()
        c2 = d["C2n_K_value_from_a"]
        assert "K_ν" in c2
        assert "a²" in c2 or "a^2" in c2

    def test_C3n_canonical_a_fails_documented(self):
        from grut.derived.koide.neutrino_hierarchy import (
            convention_declaration,
        )
        d = convention_declaration()
        c3 = d["C3n_canonical_a_fails"]
        assert "194.7" in c3
        assert "NO solution" in c3 or "no solution" in c3.lower()

    def test_C4n_neutrino_postulate(self):
        from grut.derived.koide.neutrino_hierarchy import (
            convention_declaration,
        )
        d = convention_declaration()
        c4 = d["C4n_neutrino_postulate_a_equals_1"]
        assert "a_ν = 1" in c4 or "a_nu = 1" in c4
        assert "K_ν = 1/2" in c4 or "K = 1/2" in c4
        assert "NH" in c4 or "Normal" in c4

    def test_C5n_derivation_status_derived(self):
        """Post Priority 4B (Correction #29), a_ν = 1 is DERIVED via
        boundary-degenerate uniqueness theorem, not postulated."""
        from grut.derived.koide.neutrino_hierarchy import (
            convention_declaration,
        )
        d = convention_declaration()
        c5 = d["C5n_derivation_status"]
        assert "DERIVED" in c5 or "derived" in c5.lower()
        # boundary-degenerate / uniqueness theorem must be named
        assert "uniqueness" in c5.lower() or "boundary-degenerate" in c5.lower()

    def test_priority_4_status_marked(self):
        from grut.derived.koide.neutrino_hierarchy import (
            convention_declaration,
        )
        d = convention_declaration()
        s = d["priority_4_status"]
        assert "NORMAL HIERARCHY" in s or "Normal Hierarchy" in s


# ─────────────────────────────────────────────────────────────────────
# Z_3 ansatz machinery
# ─────────────────────────────────────────────────────────────────────


class TestZ3AnsatzMachinery:
    def test_charged_lepton_K_is_two_thirds(self):
        from grut.derived.koide.neutrino_hierarchy import (
            koide_K, A_CHARGED_LEPTON,
        )
        assert abs(koide_K(A_CHARGED_LEPTON) - 2 / 3) < 1e-12

    def test_neutrino_postulate_K_is_one_half(self):
        from grut.derived.koide.neutrino_hierarchy import (
            koide_K, A_NEUTRINO_POSTULATE,
        )
        assert abs(koide_K(A_NEUTRINO_POSTULATE) - 1 / 2) < 1e-12

    def test_K_formula_general_a(self):
        """K(a) = (1 + a²/2)/3"""
        from grut.derived.koide.neutrino_hierarchy import koide_K
        for a in [0.5, 0.7, 1.0, 1.2, np.sqrt(2)]:
            expected = (1 + a**2 / 2) / 3
            assert abs(koide_K(a) - expected) < 1e-12

    def test_s_values_sum_to_three(self):
        """For Z_3 ansatz with any a and any θ, Σ s_k = 3 + a × Σ cos(θ + 2πk/3)
        = 3 + 0 = 3 (the trig sum vanishes)."""
        from grut.derived.koide.neutrino_hierarchy import s_values
        for theta in np.linspace(0, 2 * np.pi, 50):
            for a in [0.5, 1.0, np.sqrt(2)]:
                s = s_values(theta, a)
                assert abs(np.sum(s) - 3) < 1e-12

    def test_s_squared_sum_invariant(self):
        """Σ s_k² = 3 + 0 + 2 × (3a²/4) = 3 + 3a²/2 (independent of θ)."""
        from grut.derived.koide.neutrino_hierarchy import s_values
        for theta in np.linspace(0, 2 * np.pi, 30):
            for a in [0.5, 1.0, np.sqrt(2)]:
                s = s_values(theta, a)
                expected = 3 + 3 * a**2 / 2
                assert abs(np.sum(s**2) - expected) < 1e-10

    def test_all_positive_at_known_theta_range(self):
        """The all-positive θ range is non-empty for a < 2 (since
        min cosine is -1, requiring 1 - a > 0 → a < 2)."""
        from grut.derived.koide.neutrino_hierarchy import all_positive
        # For a = 1, all-positive at θ = 0
        assert all_positive(0.0, a=1.0)


# ─────────────────────────────────────────────────────────────────────
# Canonical Z_3 fails for neutrinos — load-bearing
# ─────────────────────────────────────────────────────────────────────


class TestCanonicalZ3FailsForNeutrinos:
    """The framework's charged-lepton Z_3 (a = √2, K = 2/3) does NOT
    admit any neutrino solution. This is a sharp structural finding."""

    def test_minimum_ratio_at_a_sqrt2_is_194_7(self):
        from grut.derived.koide.neutrino_hierarchy import (
            minimum_ratio_canonical_z3,
        )
        min_r = minimum_ratio_canonical_z3()
        # Should be ~194.07 (from boundary computation)
        assert 190 < min_r < 200

    def test_observed_ratio_below_minimum(self):
        """Observed Δm²_atm/Δm²_sol ≈ 33.9 (NH) is well below the
        Z_3 minimum 194.7 → canonical ansatz cannot fit."""
        from grut.derived.koide.neutrino_hierarchy import (
            DELTA_M_SQ_ATM_NH_EV2,
            DELTA_M_SQ_SOL_EV2,
            minimum_ratio_canonical_z3,
        )
        observed = DELTA_M_SQ_ATM_NH_EV2 / DELTA_M_SQ_SOL_EV2
        min_z3 = minimum_ratio_canonical_z3()
        assert observed < min_z3, (
            f"Expected observed ({observed:.2f}) < min_z3 ({min_z3:.2f})"
        )

    def test_canonical_z3_does_not_fit_NH(self):
        from grut.derived.koide.neutrino_hierarchy import (
            canonical_z3_fits_neutrinos,
        )
        assert not canonical_z3_fits_neutrinos()

    def test_no_NH_solution_at_a_sqrt2(self):
        """Confirm at the API level: neutrino_solution returns None
        for a = √2 in either hierarchy."""
        from grut.derived.koide.neutrino_hierarchy import (
            neutrino_solution, A_CHARGED_LEPTON,
        )
        for hier in ["NH", "IH"]:
            sol = neutrino_solution(a=A_CHARGED_LEPTON, hierarchy=hier)
            assert sol is None, (
                f"Unexpected solution for a={A_CHARGED_LEPTON}, hier={hier}"
            )


# ─────────────────────────────────────────────────────────────────────
# GRUT NH prediction at a_ν = 1
# ─────────────────────────────────────────────────────────────────────


class TestGRUTNHPrediction:
    """The framework's neutrino prediction conditional on a_ν = 1."""

    def test_NH_solution_exists(self):
        from grut.derived.koide.neutrino_hierarchy import grut_prediction_NH
        sol = grut_prediction_NH()
        assert sol is not None

    def test_NH_m1_is_sub_meV(self):
        """m_1 ≈ 0.8 meV, the GRUT prediction for the lightest mass."""
        from grut.derived.koide.neutrino_hierarchy import grut_prediction_NH
        sol = grut_prediction_NH()
        # Roughly 0.5–5 meV
        assert 5e-4 < sol["m_1"] < 5e-3

    def test_NH_m3_close_to_sqrt_atm(self):
        """m_3 ≈ √Δm²_atm ≈ 50 meV"""
        from grut.derived.koide.neutrino_hierarchy import (
            grut_prediction_NH, DELTA_M_SQ_ATM_NH_EV2,
        )
        sol = grut_prediction_NH()
        m3_expected = np.sqrt(DELTA_M_SQ_ATM_NH_EV2)
        # Within 5%
        assert abs(sol["m_3"] - m3_expected) / m3_expected < 0.05

    def test_NH_mass_ordering(self):
        from grut.derived.koide.neutrino_hierarchy import grut_prediction_NH
        sol = grut_prediction_NH()
        assert sol["m_1"] < sol["m_2"] < sol["m_3"]

    def test_NH_delta_m_sq_sol_recovered(self):
        from grut.derived.koide.neutrino_hierarchy import (
            grut_prediction_NH, DELTA_M_SQ_SOL_EV2,
        )
        sol = grut_prediction_NH()
        delta_sol = sol["m_2"]**2 - sol["m_1"]**2
        assert abs(delta_sol - DELTA_M_SQ_SOL_EV2) / DELTA_M_SQ_SOL_EV2 < 1e-6

    def test_NH_delta_m_sq_atm_recovered(self):
        from grut.derived.koide.neutrino_hierarchy import (
            grut_prediction_NH, DELTA_M_SQ_ATM_NH_EV2,
        )
        sol = grut_prediction_NH()
        delta_atm = sol["m_3"]**2 - sol["m_1"]**2
        assert abs(delta_atm - DELTA_M_SQ_ATM_NH_EV2) / DELTA_M_SQ_ATM_NH_EV2 < 1e-3

    def test_NH_K_is_one_half(self):
        from grut.derived.koide.neutrino_hierarchy import grut_prediction_NH
        sol = grut_prediction_NH()
        assert abs(sol["K_implied"] - 0.5) < 1e-12

    def test_NH_sum_m_nu_around_60_meV(self):
        """GRUT predicts Σm_ν ≈ 60 meV. Pin within ±10 meV."""
        from grut.derived.koide.neutrino_hierarchy import grut_prediction_NH
        sol = grut_prediction_NH()
        sum_m = sol["sum_m_nu"]
        assert 50e-3 < sum_m < 70e-3, (
            f"Expected Σm_ν ≈ 60 meV, got {sum_m * 1000:.1f} meV"
        )


# ─────────────────────────────────────────────────────────────────────
# IH at a = 1: boundary case
# ─────────────────────────────────────────────────────────────────────


class TestIHBoundaryCase:
    """IH at a_ν = 1 sits at m_3 → 0 boundary, NOT a generic interior
    solution. GRUT's preference is NH because of this asymmetry."""

    def test_IH_solution_exists_but_at_boundary(self):
        from grut.derived.koide.neutrino_hierarchy import grut_prediction_IH
        sol = grut_prediction_IH()
        assert sol is not None
        # m_3 should be essentially zero (numerical noise)
        assert sol["m_3"] < 1e-6

    def test_IH_m1_close_to_sqrt_atm(self):
        from grut.derived.koide.neutrino_hierarchy import (
            grut_prediction_IH, DELTA_M_SQ_ATM_IH_EV2, DELTA_M_SQ_SOL_EV2,
        )
        sol = grut_prediction_IH()
        # In IH with m_3 → 0: m_1² ≈ |Δm²_atm| - Δm²_sol
        m1_expected = np.sqrt(DELTA_M_SQ_ATM_IH_EV2 - DELTA_M_SQ_SOL_EV2)
        assert abs(sol["m_1"] - m1_expected) / m1_expected < 0.01

    def test_IH_theta_at_60_degrees(self):
        """IH boundary at a=1 corresponds to θ = 60° (where one cos = -1)."""
        from grut.derived.koide.neutrino_hierarchy import grut_prediction_IH
        sol = grut_prediction_IH()
        # Should be at 60° within numerical tolerance
        assert abs(sol["theta_deg"] - 60.0) < 1.0


# ─────────────────────────────────────────────────────────────────────
# Hierarchy preference
# ─────────────────────────────────────────────────────────────────────


class TestHierarchyPreference:
    def test_GRUT_prefers_NH(self):
        from grut.derived.koide.neutrino_hierarchy import hierarchy_preference
        pref = hierarchy_preference()
        assert pref["preferred"] == "NH"

    def test_IH_marked_as_boundary(self):
        from grut.derived.koide.neutrino_hierarchy import hierarchy_preference
        pref = hierarchy_preference()
        assert pref["IH_at_boundary"] is True

    def test_NH_m_lightest_nonzero(self):
        from grut.derived.koide.neutrino_hierarchy import hierarchy_preference
        pref = hierarchy_preference()
        assert pref["NH_m_lightest"] > 1e-5  # > 10 μeV

    def test_rationale_explains_interior_vs_boundary(self):
        from grut.derived.koide.neutrino_hierarchy import hierarchy_preference
        pref = hierarchy_preference()
        rat = pref["rationale"]
        assert "interior" in rat.lower()
        assert "boundary" in rat.lower() or "degenerate" in rat.lower()


# ─────────────────────────────────────────────────────────────────────
# Cosmological consistency
# ─────────────────────────────────────────────────────────────────────


class TestCosmologicalConsistency:
    def test_sum_m_nu_below_planck_bound(self):
        from grut.derived.koide.neutrino_hierarchy import consistency_with_planck
        c = consistency_with_planck()
        assert c["consistent"] is True
        assert c["GRUT_sum_m_nu_eV"] < c["Planck_2018_BAO_bound_eV"]

    def test_headroom_above_30_meV(self):
        """Σm_ν ≈ 60 meV with bound 120 meV → ~60 meV headroom."""
        from grut.derived.koide.neutrino_hierarchy import consistency_with_planck
        c = consistency_with_planck()
        assert c["headroom_eV"] > 0.030  # > 30 meV

    def test_observational_tests_summary_present(self):
        from grut.derived.koide.neutrino_hierarchy import (
            observational_tests_summary,
        )
        s = observational_tests_summary()
        assert "hierarchy_NH_preference" in s
        assert "sum_m_nu" in s
        assert "m_beta_kinematic" in s
        assert "neutrinoless_double_beta_decay" in s


# ─────────────────────────────────────────────────────────────────────
# Cross-consistency with charged-lepton Koide
# ─────────────────────────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────────────────
# Priority 4B — uniqueness theorem for a_ν = 1
# ─────────────────────────────────────────────────────────────────────


class TestUniquenessTheoremPriority4B:
    """The boundary-degenerate uniqueness theorem: a_ν = 1 is the
    UNIQUE Z_3 coupling at which (i) boundary access is admissible
    AND (ii) the two non-zero s values are exactly degenerate.

    Closes the open question `neutrino_z3_coupling_derivation_open
    _question` by deriving a_ν = 1 from structural primitives.
    """

    def test_boundary_gap_at_a_1_is_exactly_zero(self):
        """Gap = √3 × √(a² - 1) = 0 at a = 1."""
        from grut.derived.koide.neutrino_hierarchy import boundary_gap
        gap = boundary_gap(1.0)
        assert gap is not None
        assert abs(gap) < 1e-12

    def test_boundary_gap_strictly_positive_for_a_above_1(self):
        """Gap > 0 for a > 1 — boundary configuration has 3 distinct s values."""
        from grut.derived.koide.neutrino_hierarchy import boundary_gap
        for a in [1.001, 1.1, 1.2, np.sqrt(2), 1.5, 2.0]:
            gap = boundary_gap(a)
            assert gap is not None
            assert gap > 0, f"Expected gap > 0 at a={a}, got {gap}"

    def test_boundary_inaccessible_for_a_below_1(self):
        """Gap returns None for a < 1 (no boundary access)."""
        from grut.derived.koide.neutrino_hierarchy import boundary_gap
        for a in [0.5, 0.9, 0.95, 0.999]:
            gap = boundary_gap(a)
            assert gap is None, f"Expected None at a={a}, got {gap}"

    def test_boundary_gap_analytic_formula(self):
        """Gap matches √3 × √(a² - 1) analytically."""
        from grut.derived.koide.neutrino_hierarchy import boundary_gap
        for a in [1.001, 1.1, 1.4142, 1.5, 2.0]:
            gap = boundary_gap(a)
            expected = np.sqrt(3) * np.sqrt(a**2 - 1)
            assert abs(gap - expected) < 1e-12

    def test_boundary_s_values_at_a_1_is_0_1p5_1p5(self):
        """At a = 1, boundary s values are exactly (0, 3/2, 3/2)."""
        from grut.derived.koide.neutrino_hierarchy import boundary_s_values
        s = boundary_s_values(1.0)
        assert s is not None
        s_min, s_minus, s_plus = s
        assert abs(s_min - 0.0) < 1e-12
        assert abs(s_minus - 1.5) < 1e-12
        assert abs(s_plus - 1.5) < 1e-12

    def test_boundary_s_values_at_a_above_1_split(self):
        """For a > 1, boundary s values split symmetrically around 3/2."""
        from grut.derived.koide.neutrino_hierarchy import boundary_s_values
        for a in [1.001, 1.1, 1.4142]:
            s_min, s_minus, s_plus = boundary_s_values(a)
            assert s_min == 0.0
            # s_- and s_+ symmetric around 3/2
            assert abs((s_minus + s_plus) / 2 - 1.5) < 1e-10
            assert s_minus < 1.5 < s_plus

    def test_uniqueness_theorem_returns_unique_value_one(self):
        from grut.derived.koide.neutrino_hierarchy import (
            uniqueness_theorem_a_equals_1,
        )
        t = uniqueness_theorem_a_equals_1()
        assert t["unique_value"] == 1.0
        assert t["boundary_admissibility_threshold"] == 1.0
        assert t["boundary_degenerate_at"] == 1.0
        assert t["boundary_gap_at_a_1"] == 0.0

    def test_channel_counting_a_squared_values(self):
        """Route 4 interpretation: a²_e = 2 (EM+weak), a²_ν = 1 (weak only)."""
        from grut.derived.koide.neutrino_hierarchy import (
            uniqueness_theorem_a_equals_1,
        )
        t = uniqueness_theorem_a_equals_1()
        assert t["channel_counting_a_e_squared"] == 2
        assert t["channel_counting_a_nu_squared"] == 1
        # K values
        assert abs(t["channel_counting_K_e"] - 2 / 3) < 1e-12
        assert abs(t["channel_counting_K_nu"] - 1 / 2) < 1e-12
        # Σs²
        assert t["channel_counting_sigma_s_sq_e"] == 6
        assert abs(t["channel_counting_sigma_s_sq_nu"] - 4.5) < 1e-12

    def test_uniqueness_theorem_status_marked_derived(self):
        """The status string must indicate that a_ν = 1 is no longer
        a postulate but a structural derivation."""
        from grut.derived.koide.neutrino_hierarchy import (
            uniqueness_theorem_a_equals_1,
        )
        t = uniqueness_theorem_a_equals_1()
        s = t["status"]
        assert "DERIVED" in s
        assert "Priority 4B" in s or "uniqueness" in s.lower()

    def test_verify_uniqueness_at_grid(self):
        """Multi-point verification across a grid of a values."""
        from grut.derived.koide.neutrino_hierarchy import (
            verify_uniqueness_theorem,
        )
        results = verify_uniqueness_theorem()
        # a = 1.0 should be the unique degenerate point
        assert "a=1.0" in results
        r1 = results["a=1.0"]
        assert r1["boundary_access"] is True
        assert r1["degenerate"] is True
        # a = 0.5 (below 1) — no access
        r_low = results["a=0.5"]
        assert r_low["boundary_access"] is False
        # a = 1.1 — access but not degenerate
        r_high = results["a=1.1"]
        assert r_high["boundary_access"] is True
        assert r_high["degenerate"] is False

    def test_canonical_lepton_a_sqrt2_at_boundary_is_distinct_split(self):
        """At a = √2 (charged-lepton coupling), the boundary s values
        are (0, 0.634, 2.366) — distinct, NOT degenerate. Confirms
        charged leptons are NOT at the degenerate-boundary point."""
        from grut.derived.koide.neutrino_hierarchy import (
            boundary_s_values, A_CHARGED_LEPTON,
        )
        s = boundary_s_values(A_CHARGED_LEPTON)
        s_min, s_minus, s_plus = s
        assert abs(s_min - 0.0) < 1e-12
        # The two non-zero values are distinct (gap = √3)
        assert abs(s_plus - s_minus - np.sqrt(3)) < 1e-10
        # And s_- < 3/2 < s_+
        assert s_minus < 1.5 < s_plus


class TestCrossConsistencyWithChargedLeptonKoide:
    def test_charged_lepton_Koide_K_matches_existing_module(self):
        """The K = 2/3 from this module's koide_K(√2) should match the
        existing `grut/derived/koide/identity.py` charged-lepton K."""
        from grut.derived.koide.neutrino_hierarchy import (
            koide_K, A_CHARGED_LEPTON,
        )
        from grut.derived.koide.identity import koide_check
        # Charged-lepton experimental check
        existing = koide_check()
        # K from existing module
        K_existing = existing["K"]
        # K from our formula
        K_ours = koide_K(A_CHARGED_LEPTON)
        # Both should be close to 2/3 (existing tests pass exactly,
        # this is the conceptual identity)
        assert abs(K_existing - K_ours) < 1e-3

    def test_a_neutrino_differs_from_a_charged_lepton(self):
        """The framework explicitly states a_ν ≠ a_charged. Charged
        leptons have a = √2 (proven); neutrinos require a different
        a (postulate: a = 1)."""
        from grut.derived.koide.neutrino_hierarchy import (
            A_CHARGED_LEPTON, A_NEUTRINO_POSTULATE,
        )
        assert A_NEUTRINO_POSTULATE != A_CHARGED_LEPTON
        assert abs(A_NEUTRINO_POSTULATE - A_CHARGED_LEPTON) > 0.4
