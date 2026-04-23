"""Tests for the Z₃ circulant Koide mass operator and the
Track II Phase 1 derivation attempt.

Required (must-pass):
    - Z₃ parameterization reconstructs (m_e, m_μ, m_τ) at (M₀, θ) to 0.01%
    - K = 2/3 is algebraic (machine precision for any nonzero M₀, any θ)
    - Circulant operator is Hermitian in flavor basis with eigenvalues
      equal to the three lepton masses
    - verify() returns all-true

Expected status (per V7 honesty protocol):
    - Derivation is HONEST NEGATIVE (underdetermined)
    - V7 §29 label: still "MAPPED"
    - V7 Conjecture F1 label: still "HYPOTHESIS"
    - Canonical constants (R, S, α_vac, τ_0) unmodified
    - One CANDIDATE IDENTITY surfaced: θ = K·α_vac = 2/9
"""

from __future__ import annotations

import numpy as np
import pytest


class TestZ3Parameterization:
    """The canonical (M₀, θ) must reconstruct the three charged-lepton
    masses to 0.01% — this is the regression constraint that any
    future derivation must preserve."""

    def test_imports(self):
        from grut.derived.flavor import koide_operator  # noqa: F401

    def test_canonical_reconstruction_0p01pct(self):
        from grut.derived.flavor.koide_operator import verify_reconstruction
        r = verify_reconstruction()
        assert r["reproduces_to_0p01pct"], (
            f"Z₃ circulant at (M₀, θ) = "
            f"({r['M0_input_GeV_half']}, {r['theta_input_rad']}) "
            f"missed 0.01% reconstruction: max frac err = "
            f"{r['max_frac_err_pct']}%"
        )

    def test_K_equals_two_thirds_machine_precision(self):
        from grut.derived.flavor.koide_operator import (
            koide_K_from_operator,
            M0_FIT_GEV_HALF, THETA_FIT_RAD,
        )
        K = koide_K_from_operator(M0_FIT_GEV_HALF, THETA_FIT_RAD)
        assert abs(K - 2.0/3.0) < 1e-12

    def test_K_is_theta_independent_algebraic_identity(self):
        """The whole point of the Z₃ circulant at N=3 is that K=2/3
        regardless of θ. Sample across the full angle range."""
        from grut.derived.flavor.koide_operator import koide_K_from_operator
        for theta in np.linspace(0.05, 2*np.pi - 0.05, 50):
            K = koide_K_from_operator(1.0, float(theta))
            assert abs(K - 2.0/3.0) < 1e-12, (
                f"K=2/3 identity failed at θ={theta}: K={K}"
            )

    def test_K_is_M0_independent_algebraic_identity(self):
        """K is scale-invariant under M₀."""
        from grut.derived.flavor.koide_operator import (
            koide_K_from_operator, THETA_FIT_RAD,
        )
        for M0 in (0.1, 0.5, 1.0, 10.0, 100.0):
            K = koide_K_from_operator(M0, THETA_FIT_RAD)
            assert abs(K - 2.0/3.0) < 1e-12

    def test_three_masses_are_distinct_and_positive(self):
        from grut.derived.flavor.koide_operator import (
            lepton_masses_from_koide, M0_FIT_GEV_HALF, THETA_FIT_RAD,
        )
        m = lepton_masses_from_koide(M0_FIT_GEV_HALF, THETA_FIT_RAD)
        assert np.all(m > 0)
        assert len(np.unique(np.round(m, 10))) == 3


class TestCirculantOperator:
    """The 3×3 flavor-space circulant built from the mass triplet
    must have the three masses as its eigenvalues."""

    def test_eigenvalues_are_the_three_masses(self):
        from grut.derived.flavor.koide_operator import (
            circulant_mass_operator, lepton_masses_from_koide,
            M0_FIT_GEV_HALF, THETA_FIT_RAD,
        )
        M = circulant_mass_operator(M0_FIT_GEV_HALF, THETA_FIT_RAD)
        eigs = np.sort(np.real(np.linalg.eigvals(M)))
        expected = np.sort(lepton_masses_from_koide(M0_FIT_GEV_HALF, THETA_FIT_RAD))
        assert np.allclose(eigs, expected, rtol=1e-10)

    def test_operator_is_3x3(self):
        from grut.derived.flavor.koide_operator import (
            circulant_mass_operator, M0_FIT_GEV_HALF, THETA_FIT_RAD,
        )
        M = circulant_mass_operator(M0_FIT_GEV_HALF, THETA_FIT_RAD)
        assert M.shape == (3, 3)

    def test_operator_is_circulant(self):
        """First row is (c_0, c_1, c_2); each subsequent row is a
        cyclic shift: M[i,j] = c[(i−j) mod 3]."""
        from grut.derived.flavor.koide_operator import (
            circulant_mass_operator, M0_FIT_GEV_HALF, THETA_FIT_RAD,
        )
        M = circulant_mass_operator(M0_FIT_GEV_HALF, THETA_FIT_RAD)
        c = M[0]  # (c_0, c_{-1} mod 3 = c_2, c_{-2} mod 3 = c_1)
        # Check row 1 is c shifted by 1
        for j in range(3):
            assert np.isclose(M[1, j], M[0, (j - 1) % 3], rtol=1e-12)
            assert np.isclose(M[2, j], M[0, (j - 2) % 3], rtol=1e-12)


class TestTrackIIPhase1Attempt:
    """Honest-negative regression: the derivation attempt must stay
    labeled 'HONEST NEGATIVE' until a full derivation from S_CTP is
    provided. V7 §29 must remain MAPPED; Conjecture F1 must remain
    HYPOTHESIS."""

    def test_verify_all_checks_pass(self):
        from grut.derived.flavor.koide_operator import verify
        v = verify()
        for key, val in v.items():
            assert val is True, f"verify() check failed: {key}"

    def test_status_is_honest_negative(self):
        from grut.derived.flavor.koide_operator import derivation_attempt
        d = derivation_attempt()
        assert "HONEST NEGATIVE" in d["status"]

    def test_V7_section_29_still_mapped(self):
        from grut.derived.flavor.koide_operator import derivation_attempt
        d = derivation_attempt()
        assert "MAPPED" in d["status_after_attempt"]["V7_section_29"]

    def test_V7_conjecture_F1_still_hypothesis(self):
        from grut.derived.flavor.koide_operator import derivation_attempt
        d = derivation_attempt()
        assert "HYPOTHESIS" in d["status_after_attempt"]["V7_conjecture_F1"]

    def test_K_and_N_uniqueness_still_proven(self):
        """These are algebraic; Track II Phase 1 does NOT touch them."""
        from grut.derived.flavor.koide_operator import derivation_attempt
        d = derivation_attempt()
        assert "PROVEN" in d["status_after_attempt"]["Koide_identity_K"]
        assert "PROVEN" in d["status_after_attempt"]["N_3_uniqueness"]

    def test_canonical_constants_unmodified(self):
        from grut.derived.flavor.koide_operator import derivation_attempt
        d = derivation_attempt()
        assert d["cross_sector_consistency"]["canonical_constants_not_modified"] is True

    def test_M0_dimensional_gap_documented(self):
        """The 20-order-of-magnitude gap between √(ℏ/τ_0) and the
        required M₀ must be explicitly surfaced."""
        from grut.derived.flavor.koide_operator import derivation_attempt
        d = derivation_attempt()
        gap = d["what_failed"]["M0_dimensional"]["orders_of_magnitude_gap_log10"]
        assert gap > 15, f"M₀ dimensional gap should be ~20 decades, got {gap}"

    def test_what_would_close_it_has_three_items(self):
        from grut.derived.flavor.koide_operator import derivation_attempt
        d = derivation_attempt()
        assert len(d["what_would_close_it"]) == 3

    def test_summary_paragraph_is_present(self):
        from grut.derived.flavor.koide_operator import derivation_attempt
        d = derivation_attempt()
        s = d["V8_track_II_summary_paragraph"]
        assert isinstance(s, str)
        assert "HONEST NEGATIVE" in s
        assert "MAPPED" in s
        assert "HYPOTHESIS" in s


class TestThetaCandidateIdentity:
    """θ = K·α_vac = 2/9 is a CANDIDATE IDENTITY (not DERIVED).
    It must be (a) surfaced by the survey, (b) inside the
    experimental window, and (c) labeled correctly."""

    def test_candidate_surfaced_in_survey(self):
        from grut.derived.flavor.koide_operator import survey_candidate_relations
        s = survey_candidate_relations()
        tight = [r for r in s["theta_tight_matches"]
                 if "K · α_vac" in r["expression"] or "2/9" in r["expression"]]
        assert len(tight) >= 1, "θ = K·α_vac should be the leading tight match"

    def test_candidate_deviation_under_ten_ppm(self):
        from grut.derived.flavor.koide_operator import derivation_attempt
        d = derivation_attempt()
        c = d["candidate_identity_theta"]
        assert c["deviation_ppm"] < 10.0

    def test_candidate_inside_experimental_window(self):
        from grut.derived.flavor.koide_operator import derivation_attempt
        d = derivation_attempt()
        c = d["candidate_identity_theta"]
        assert c["inside_experimental_window"] is True
        assert c["deviation_ppm"] < c["experimental_window_ppm_from_m_tau"]

    def test_candidate_is_labeled_candidate_not_derived(self):
        from grut.derived.flavor.koide_operator import derivation_attempt
        d = derivation_attempt()
        c = d["candidate_identity_theta"]
        assert "CANDIDATE" in c["status_tier"]
        assert "DERIVED" not in c["status_tier"]
        assert "COMPUTED" not in c["status_tier"]

    def test_candidate_has_falsifier(self):
        from grut.derived.flavor.koide_operator import derivation_attempt
        d = derivation_attempt()
        c = d["candidate_identity_theta"]
        assert isinstance(c["falsifier"], str)
        assert len(c["falsifier"]) > 0

    def test_candidate_value_equals_two_over_nine(self):
        from grut.derived.flavor.koide_operator import derivation_attempt
        d = derivation_attempt()
        c = d["candidate_identity_theta"]
        assert abs(c["value_rad"] - 2.0/9.0) < 1e-15


class TestPhase2MassAnchorMechanisms:
    """Track II Phase 2: evaluate three candidate dimensional-anchor
    mechanisms for M₀. Evaluation is mechanism-based, not numerical.
    Expected finding: v_EW Yukawa is the sole viable anchor; Λ_QCD
    and v_dark both FAIL because no Lagrangian operator in the SM
    or V7 couples them to the charged-lepton sector."""

    def test_evaluate_returns_three_mechanisms(self):
        from grut.derived.flavor.koide_operator import evaluate_mass_anchor_mechanisms
        m = evaluate_mass_anchor_mechanisms()
        assert "mechanism_1_v_EW" in m
        assert "mechanism_2_Lambda_QCD" in m
        assert "mechanism_3_v_dark" in m

    def test_v_EW_is_HYPOTHESIS_not_DERIVED(self):
        """v_EW Yukawa is SM-native; M₀ reduces to Σy_i but the three
        eigenvalues themselves are not yet derived from S_CTP."""
        from grut.derived.flavor.koide_operator import evaluate_mass_anchor_mechanisms
        m = evaluate_mass_anchor_mechanisms()
        assert m["mechanism_1_v_EW"]["status"] == "HYPOTHESIS"
        assert m["mechanism_1_v_EW"]["coupling_present_in_V7"] is True

    def test_v_EW_arithmetic_matches_fit_to_ppm(self):
        """Numerical sanity check on the Koide→Yukawa translation."""
        from grut.derived.flavor.koide_operator import evaluate_mass_anchor_mechanisms
        m = evaluate_mass_anchor_mechanisms()
        v = m["mechanism_1_v_EW"]
        # M₀² reconstructed from (Y_E, Y_MU, Y_TAU) · v_EW/√2 / 6
        # should match the fit within rounding of the Yukawa values.
        assert v["match_to_fit_fractional"] < 1e-4

    def test_Lambda_QCD_FAILED(self):
        from grut.derived.flavor.koide_operator import evaluate_mass_anchor_mechanisms
        m = evaluate_mass_anchor_mechanisms()
        assert m["mechanism_2_Lambda_QCD"]["status"] == "FAILED"
        assert m["mechanism_2_Lambda_QCD"]["coupling_present_in_V7"] is False

    def test_v_dark_FAILED(self):
        from grut.derived.flavor.koide_operator import evaluate_mass_anchor_mechanisms
        m = evaluate_mass_anchor_mechanisms()
        assert m["mechanism_3_v_dark"]["status"] == "FAILED"
        assert m["mechanism_3_v_dark"]["coupling_between_v_dark_and_charged_leptons_in_V7"] is False

    def test_only_v_EW_is_viable(self):
        from grut.derived.flavor.koide_operator import evaluate_mass_anchor_mechanisms
        m = evaluate_mass_anchor_mechanisms()
        assert m["viable_mechanisms"] == ["v_EW Yukawa (SM-native)"]

    def test_phase_3_redirect_is_posed(self):
        from grut.derived.flavor.koide_operator import evaluate_mass_anchor_mechanisms
        m = evaluate_mass_anchor_mechanisms()
        p3 = m["phase_3_redirect"]
        assert "Yukawa" in p3["new_goal"]
        assert "v_EW as an input" in p3["new_goal"]
        # The anti-curve-fitting warning must be explicitly present.
        assert "curve-fitting" in p3["what_v8_MUST_NOT_do"] or \
               "numerology" in p3["what_v8_MUST_NOT_do"]

    def test_phase_2_does_not_upgrade_status(self):
        from grut.derived.flavor.koide_operator import evaluate_mass_anchor_mechanisms
        m = evaluate_mass_anchor_mechanisms()
        assert "MAPPED" in m["status_change"]["V7_section_29"]
        assert "HYPOTHESIS" in m["status_change"]["V7_conjecture_F1"]

    def test_rejects_numerical_coincidence_Lambda_QCD(self):
        """The module must explicitly document that M₀²/Λ_QCD ≈ 1.26
        is rejected as a coincidence."""
        from grut.derived.flavor.koide_operator import evaluate_mass_anchor_mechanisms
        m = evaluate_mass_anchor_mechanisms()
        s = m["mechanism_2_Lambda_QCD"]["reject_numerical_fit"]
        assert "coincidence" in s.lower()

    def test_rejects_numerical_coincidence_v_dark(self):
        """The module must explicitly document that v_dark ≈ R²·M₀²
        is rejected as a coincidence (the Gemini failure mode)."""
        from grut.derived.flavor.koide_operator import evaluate_mass_anchor_mechanisms
        m = evaluate_mass_anchor_mechanisms()
        s = m["mechanism_3_v_dark"]["reject_numerical_fit"]
        assert "coincidence" in s.lower()

    def test_verify_phase_2_booleans_all_true(self):
        from grut.derived.flavor.koide_operator import verify
        v = verify()
        assert v["v_EW_mechanism_is_HYPOTHESIS"] is True
        assert v["Lambda_QCD_mechanism_FAILED"] is True
        assert v["v_dark_mechanism_FAILED"] is True
        assert v["sole_viable_mechanism_is_v_EW"] is True


class TestPhase3YukawaDerivation:
    """Track II Phase 3: attempt to derive (y_e, y_μ, y_τ) from the
    multi-generation CTP fixed-point at v_EW with θ = K·α_vac = 2/9.
    Expected: HONEST NEGATIVE — the CTP fixed point does not
    constrain the Yukawa couplings, which are SM Lagrangian inputs."""

    def test_empirical_targets_match_PDG(self):
        """y_i = m_i √2 / v_EW reproduces PDG values."""
        from grut.derived.flavor.koide_operator import yukawa_empirical_targets
        e = yukawa_empirical_targets()
        assert abs(e["y_e"]   - 2.94e-6) / 2.94e-6 < 0.01
        assert abs(e["y_mu"]  - 6.07e-4) / 6.07e-4 < 0.01
        assert abs(e["y_tau"] - 1.02e-2) / 1.02e-2 < 0.01
        assert abs(e["trace_y_over_3"] - 3.605e-3) / 3.605e-3 < 0.01

    def test_theta_input_matches_fit_within_percent(self):
        """θ = 2π/3 + 2/9 matches fitted θ at ≲ 0.05%."""
        from grut.derived.flavor.koide_operator import yukawa_empirical_targets
        e = yukawa_empirical_targets()
        assert e["theta_matches_fit_at_pct"] < 0.05

    def test_ctp_fixed_point_does_not_fix_yukawas(self):
        from grut.derived.flavor.koide_operator import ctp_fixed_point_at_EW_scale
        c = ctp_fixed_point_at_EW_scale()
        not_fixed = " ".join(c["what_is_NOT_fixed_by_CTP"]).lower()
        assert "y_e" in not_fixed
        assert "hierarchy" in not_fixed

    def test_no_candidate_under_5_pct(self):
        """No dimensionless combination matches ⟨y⟩ at derivation-level
        precision. This is the quantitative honest-negative claim."""
        from grut.derived.flavor.koide_operator import yukawa_trace_candidate_survey
        s = yukawa_trace_candidate_survey()
        assert len(s["tight_matches_under_5_pct"]) == 0

    def test_closest_candidate_is_mechanism_free(self):
        """The closest match (α_vac · α_s/(4π)) requires α_s to
        couple to leptons, which fails on SM mechanism grounds."""
        from grut.derived.flavor.koide_operator import yukawa_trace_candidate_survey
        s = yukawa_trace_candidate_survey()
        issue = s["closest_match_issue"].lower()
        assert "color singlet" in issue or "color" in issue
        assert "α_s" in s["closest_match_issue"] or "a_s" in s["closest_match_issue"].lower()

    def test_phase_3_status_is_HN(self):
        from grut.derived.flavor.koide_operator import phase_3_yukawa_derivation_attempt
        p3 = phase_3_yukawa_derivation_attempt()
        assert "HONEST NEGATIVE" in p3["status"]

    def test_phase_3_does_NOT_falsify_phase_1_candidate(self):
        """θ = K·α_vac = 2/9 survives. Phase 3's failure is at the
        trace-scale level; θ distributes eigenvalues within the trace."""
        from grut.derived.flavor.koide_operator import phase_3_yukawa_derivation_attempt
        p3 = phase_3_yukawa_derivation_attempt()
        status = p3["status_after_attempt"]["Phase_1_candidate_theta_2_over_9"]
        assert "CANDIDATE IDENTITY" in status
        assert "unchanged" in status

    def test_phase_3_preserves_phase_2_v_EW_HYPOTHESIS(self):
        from grut.derived.flavor.koide_operator import phase_3_yukawa_derivation_attempt
        p3 = phase_3_yukawa_derivation_attempt()
        status = p3["status_after_attempt"]["Phase_2_viable_anchor_v_EW"]
        assert "HYPOTHESIS" in status

    def test_phase_3_preserves_V7_section_29_MAPPED(self):
        from grut.derived.flavor.koide_operator import phase_3_yukawa_derivation_attempt
        p3 = phase_3_yukawa_derivation_attempt()
        assert "MAPPED" in p3["status_after_attempt"]["V7_section_29"]

    def test_phase_3_preserves_Conjecture_F1(self):
        from grut.derived.flavor.koide_operator import phase_3_yukawa_derivation_attempt
        p3 = phase_3_yukawa_derivation_attempt()
        assert "HYPOTHESIS" in p3["status_after_attempt"]["V7_conjecture_F1"]

    def test_phase_3_canonical_constants_intact(self):
        from grut.derived.flavor.koide_operator import phase_3_yukawa_derivation_attempt
        p3 = phase_3_yukawa_derivation_attempt()
        assert p3["cross_sector_consistency"]["canonical_constants_not_modified"] is True
        assert p3["cross_sector_consistency"]["SM_imports_not_modified"] is True

    def test_phase_4_direction_mentions_hierarchy(self):
        """Phase 4 = Yukawa hierarchy problem. This must be explicit."""
        from grut.derived.flavor.koide_operator import phase_3_yukawa_derivation_attempt
        p3 = phase_3_yukawa_derivation_attempt()
        p4 = " ".join(p3["what_would_close_it_phase_4"]).lower()
        assert "hierarchy" in p4 or "flavor-selection" in p4 or "flavor selection" in p4

    def test_phase_3_summary_paragraph_present(self):
        from grut.derived.flavor.koide_operator import phase_3_yukawa_derivation_attempt
        p3 = phase_3_yukawa_derivation_attempt()
        s = p3["V8_track_II_phase_3_paragraph"]
        assert isinstance(s, str) and len(s) > 500
        assert "HONEST NEGATIVE" in s
        assert "MAPPED" in s
        assert "HYPOTHESIS" in s
        assert "CANDIDATE IDENTITY" in s

    def test_verify_phase_3_booleans_true(self):
        from grut.derived.flavor.koide_operator import verify
        v = verify()
        assert v["phase_3_status_is_HN"] is True
        assert v["phase_3_no_tight_match"] is True
        assert v["phase_3_preserves_phase_1"] is True
        assert v["phase_3_preserves_phase_2"] is True


class TestPhase4FlavorMechanism:
    """Track II Phase 4: evaluate three candidate flavor-selection
    mechanisms (A anomaly-weighted, B dielectric, C flavor-anomaly)
    against four mechanism requirements (C1–C4). Expected outcome:
    HONEST NEGATIVE on full closure; Phase 4.0 scope document
    becomes the deliverable."""

    def test_hypercharge_accounting_matches_V7_correction_16(self):
        """ΣY²_total per 3 generations = 10; (ΣY²)² = 100, per V7 §26.2.6."""
        from grut.derived.flavor.koide_operator import direction_A_anomaly_weighted_ctp
        a = direction_A_anomaly_weighted_ctp()
        assert abs(a["hypercharge_accounting_per_gen"]["Y2_total"] - 10.0/3.0) < 1e-12
        assert a["3gen_sums"]["correction_16_integer"] == 100
        assert abs(a["3gen_sums"]["Y2_total_3gen_squared"] - 100.0) < 1e-12

    def test_charged_lepton_hypercharge_is_five_quarter_per_gen(self):
        from grut.derived.flavor.koide_operator import direction_A_anomaly_weighted_ctp
        a = direction_A_anomaly_weighted_ctp()
        assert abs(a["hypercharge_accounting_per_gen"]["Y2_charged_lepton_subset"] - 5.0/4.0) < 1e-12

    def test_direction_A_satisfies_C1_and_C4_but_fails_C2(self):
        """Direction A's verdict pattern: hypercharge distinction is
        real and SM-native, but the scale doesn't land under 5%."""
        from grut.derived.flavor.koide_operator import direction_A_anomaly_weighted_ctp
        a = direction_A_anomaly_weighted_ctp()
        assert "PASS" in a["C1_status"]
        assert "PASS" in a["C4_status"]
        assert "FAIL" in a["C2_status"]
        assert a["any_candidate_closes_C2"] is False

    def test_direction_B_fails_all_primary_criteria(self):
        """Dielectric α_eff at lab frequencies is ~10⁻⁷³ — too small
        by 70 decades for any Yukawa mechanism."""
        from grut.derived.flavor.koide_operator import direction_B_dielectric_flavor_mixing
        b = direction_B_dielectric_flavor_mixing()
        assert "FAIL" in b["C1_status"]
        assert "FAIL" in b["C2_status"]
        assert "FAIL" in b["C4_status"]
        assert b["suppression_gap_log10"] > 60  # ~70 decades
        assert b["lagrangian_audit"]["flavor_dependent_kinetic_mixing"] is False
        assert b["lagrangian_audit"]["lepton_dark_Yukawa_H_dark_L_e_R"] is False

    def test_direction_C_inherits_underdetermination(self):
        """Direction C reaches the right order of magnitude but
        inherits Phase 3's underdetermination — one trace equation,
        three unknowns."""
        from grut.derived.flavor.koide_operator import direction_C_flavor_anomaly_analog
        c = direction_C_flavor_anomaly_analog()
        assert "FAIL" in c["C2_status"]
        assert c["any_candidate_closes_C2"] is False
        assert "underdetermination" in c["underdetermination_note"].lower() or \
               "underdetermined" in c["verdict"].lower()

    def test_phase_4_no_direction_passes_all_four_criteria(self):
        from grut.derived.flavor.koide_operator import phase_4_mechanism_evaluation
        p4 = phase_4_mechanism_evaluation()
        assert p4["any_direction_passes_all"] is False

    def test_phase_4_status_is_HN(self):
        from grut.derived.flavor.koide_operator import phase_4_mechanism_evaluation
        p4 = phase_4_mechanism_evaluation()
        assert "HONEST NEGATIVE" in p4["status"]

    def test_phase_4_preserves_all_prior_phases(self):
        from grut.derived.flavor.koide_operator import phase_4_mechanism_evaluation
        p4 = phase_4_mechanism_evaluation()
        assert "MAPPED" in p4["status_after_attempt"]["V7_section_29"]
        assert "HYPOTHESIS" in p4["status_after_attempt"]["V7_conjecture_F1"]
        assert "CANDIDATE IDENTITY" in p4["status_after_attempt"]["Phase_1_candidate"]
        assert "HYPOTHESIS" in p4["status_after_attempt"]["Phase_2_anchor"]
        assert "HONEST NEGATIVE" in p4["status_after_attempt"]["Phase_3_outcome"]

    def test_phase_4_direction_A_PARTIAL_not_full_PASS(self):
        """Direction A is partial — must not be marked as FULL PASS
        or DERIVED under the honesty protocol."""
        from grut.derived.flavor.koide_operator import phase_4_mechanism_evaluation
        p4 = phase_4_mechanism_evaluation()
        a_verdict = p4["status_after_attempt"]["Phase_4_A"]
        assert "PARTIAL" in a_verdict
        assert "DERIVED" not in a_verdict
        assert "RESULT" not in a_verdict

    def test_phase_4_direction_B_FAILED(self):
        from grut.derived.flavor.koide_operator import phase_4_mechanism_evaluation
        p4 = phase_4_mechanism_evaluation()
        assert "FAILED" in p4["status_after_attempt"]["Phase_4_B"]

    def test_phase_4_0_scope_document_has_required_sections(self):
        from grut.derived.flavor.koide_operator import phase_4_scope_document
        s = phase_4_scope_document()
        # Must contain the four requirements explicitly
        req = s["four_requirements_for_any_candidate_mechanism"]
        for key in ("C1_flavor_distinction", "C2_trace_scale",
                    "C3_Z3_compatibility", "C4_mechanism_grade"):
            assert key in req
        # Must document the three attempted directions
        attempted = s["three_directions_attempted_in_phase_4"]
        for key in ("A_anomaly_weighted_ctp", "B_dielectric_flavor_mixing",
                    "C_flavor_anomaly_analog"):
            assert key in attempted
        # Must articulate candidate Phase 5 directions
        assert len(s["candidate_phase_5_directions"]) >= 3

    def test_phase_4_0_scope_states_underdetermination_theorem(self):
        from grut.derived.flavor.koide_operator import phase_4_scope_document
        s = phase_4_scope_document()
        thm = s["phase_3_underdetermination_theorem"].lower()
        # The theorem must state either that the CTP doesn't constrain
        # the Yukawas (underdetermination) or that it's satisfied for
        # any choice (equivalent phrasing).
        assert ("not constrain" in thm) or ("underdetermin" in thm) or ("any choice" in thm)
        assert "yukawa" in thm

    def test_phase_4_0_recommends_deferring_to_phase_5(self):
        from grut.derived.flavor.koide_operator import phase_4_scope_document
        s = phase_4_scope_document()
        rp = s["recommended_posture"].lower()
        assert "deferred" in rp or "defer" in rp or "4.1" in rp

    def test_verify_phase_4_booleans_true(self):
        from grut.derived.flavor.koide_operator import verify
        v = verify()
        assert v["phase_4_status_is_HN"] is True
        assert v["phase_4_no_direction_passes_C2"] is True
        assert v["phase_4_scope_document_available"] is True

    def test_direction_A_rejects_cubed_hypercharge_numerology(self):
        """1/(ΣY²)³ = 10⁻³ is a numerology pattern (Gemini's
        suggestion). It must be explicitly REJECTED in Direction A."""
        from grut.derived.flavor.koide_operator import direction_A_anomaly_weighted_ctp
        a = direction_A_anomaly_weighted_ctp()
        rejected = [c for c in a["candidates_ranked"]
                    if c.get("REJECTED_per_C4", False)]
        assert len(rejected) >= 1
        r = rejected[0]
        assert "REJECTED" in r["expression"] or "NUMEROLOGY" in r["expression"].upper() \
               or "10⁻³" in r["expression"] or "numerology" in r["justification"].lower()

    def test_direction_C_includes_temporal_correlator_C2(self):
        """Direction C must include the C.2 temporal-correlator
        sub-direction, which evaluates the FDT at three-flavor level
        and confirms it is flavor-diagonal (no extra constraint)."""
        from grut.derived.flavor.koide_operator import direction_C_flavor_anomaly_analog
        c = direction_C_flavor_anomaly_analog()
        assert "C_2_temporal_correlator" in c
        c2 = c["C_2_temporal_correlator"]
        assert c2["flavor_dependent_tau_in_V7"] is False
        assert c2["flavor_dependent_temperature_in_V7"] is False
        assert "FAILED" in c2["verdict"]

    def test_phase_4_0_scope_explicitly_rules_out_4th_generation(self):
        """Adding a 4th fermion generation breaks V7 §9's PROVEN
        N=3 uniqueness. Must be explicitly off-limits."""
        from grut.derived.flavor.koide_operator import phase_4_scope_document
        s = phase_4_scope_document()
        ruled_out = s["explicitly_ruled_out_framings"]
        assert "four_generation_extension" in ruled_out
        text = ruled_out["four_generation_extension"].lower()
        assert "proven" in text or "n = 3" in text or "n=3" in text
        assert "off-limits" in text or "invalidates" in text

    def test_phase_4_0_scope_rules_out_tau_0_as_new_dimension(self):
        """τ_0 is a CTP response parameter, not a dimension. Must be
        explicitly off-limits as a 'reframe' direction."""
        from grut.derived.flavor.koide_operator import phase_4_scope_document
        s = phase_4_scope_document()
        ruled_out = s["explicitly_ruled_out_framings"]
        assert "tau_0_as_a_new_dimension" in ruled_out
        text = ruled_out["tau_0_as_a_new_dimension"].lower()
        assert "response kernel" in text or "parameter" in text
        assert "4d" in text or "narrative" in text

    def test_phase_4_0_scope_rules_out_S4_to_4_generations_confusion(self):
        """The '4' in S^4 is spacetime dimension, not generation count.
        Pattern-matching S^4 to 4-generation must be off-limits."""
        from grut.derived.flavor.koide_operator import phase_4_scope_document
        s = phase_4_scope_document()
        ruled_out = s["explicitly_ruled_out_framings"]
        assert "S4_to_4_generations_pattern_match" in ruled_out
        text = ruled_out["S4_to_4_generations_pattern_match"].lower()
        assert "spacetime" in text or "euclidean" in text
        assert "generation" in text

    def test_phase_4_0_scope_rules_out_cubed_ratio_numerology(self):
        from grut.derived.flavor.koide_operator import phase_4_scope_document
        s = phase_4_scope_document()
        ruled_out = s["explicitly_ruled_out_framings"]
        assert "cubed_hypercharge_ratio_numerology" in ruled_out

    def test_phase_4_0_scope_lists_legitimate_extensions(self):
        """Explicit positive list of where the missing constraint
        might legitimately live (higher-loop, non-perturbative,
        explicit temporal correlator refinement)."""
        from grut.derived.flavor.koide_operator import phase_4_scope_document
        s = phase_4_scope_document()
        legit = s["legitimate_places_to_look_for_the_missing_constraint"]
        assert len(legit) >= 3
        joined = " ".join(legit).lower()
        assert "higher-loop" in joined or "4-loop" in joined or "higher loop" in joined
        assert "non-perturbative" in joined or "nonperturbative" in joined or "instanton" in joined
        assert "temporal" in joined or "time" in joined


class TestNoDerivationClaim:
    """Double-checks that nothing in the module claims COMPUTED or
    DERIVED status for (M₀, θ). The honesty protocol forbids
    upgrading without an S_CTP-level proof."""

    def test_status_tier_is_not_computed_or_derived(self):
        from grut.derived.flavor.koide_operator import derivation_attempt
        d = derivation_attempt()
        assert d["status"] != "COMPUTED"
        assert d["status"] != "DERIVED"

    def test_derived_keys_not_present(self):
        """The 'succeeds' branch of derivation_attempt exposes 'theta_derivation'
        and 'M0_derivation' keys. They must be ABSENT until a real derivation
        lands."""
        from grut.derived.flavor.koide_operator import derivation_attempt
        d = derivation_attempt()
        assert "theta_derivation" not in d
        assert "M0_derivation" not in d
