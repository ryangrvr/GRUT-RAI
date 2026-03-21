"""Tests for grut.covariant_interior — Constitutive-to-Metric Lapse Obstruction.

Targeted tests for the Constitutive Lapse Insufficiency Theorem, lapse
direction failure, proxy classification, status ladder, self-healing
reconfirmation, Phase IV reconfirmation, parametric beta scan, effective
NEC analysis, T^Phi status, and serialization.

~130 tests across 14 test classes.
"""

from __future__ import annotations

import json
import math

import pytest

from grut.covariant_interior import (
    compute_covariant_interior_analysis,
    covariant_interior_result_to_dict,
    build_insufficiency_theorem,
    build_effective_nec,
    build_lapse_direction,
    build_tphi_status,
    build_proxy_classification,
    build_status_ladder_update,
    build_self_healing_reconfirmation,
    build_phase4_reconfirmation,
    scan_A_eff_vs_beta,
    _compactness,
    _h_of_x,
    _g_of_beta,
    _A_eff_from_constitutive,
    ALPHA_VAC,
    BETA_Q,
    EPSILON_Q,
    R_EQ_OVER_R_S,
    C_ENDPOINT,
    ALPHA_VAC_CRITICAL,
    LEVEL_EXACT,
    LEVEL_CONSTITUTIVE_DERIVED,
    LEVEL_UNRESOLVED,
    LEVEL_CONSTITUTIVE_LAPSE_PROMOTION_OBSTRUCTED,
    LEVEL_CONSTITUTIVE_SURROGATE,
    SCOPE_STATEMENT,
)


# ================================================================
# Module-scoped fixtures
# ================================================================

@pytest.fixture(scope="module")
def insufficiency():
    """Insufficiency theorem at canonical alpha_vac."""
    return build_insufficiency_theorem()


@pytest.fixture(scope="module")
def effective_nec():
    """Effective NEC analysis at canonical parameters."""
    return build_effective_nec()


@pytest.fixture(scope="module")
def lapse_direction():
    """Lapse direction analysis at canonical parameters."""
    return build_lapse_direction()


@pytest.fixture(scope="module")
def tphi_status():
    """T^Phi status."""
    return build_tphi_status()


@pytest.fixture(scope="module")
def proxy_class():
    """Proxy lapse classification at canonical parameters."""
    return build_proxy_classification()


@pytest.fixture(scope="module")
def status_ladder():
    """Status ladder update."""
    return build_status_ladder_update()


@pytest.fixture(scope="module")
def self_healing():
    """Self-healing reconfirmation."""
    return build_self_healing_reconfirmation()


@pytest.fixture(scope="module")
def phase4_reconf():
    """Phase IV reconfirmation."""
    return build_phase4_reconfirmation()


@pytest.fixture(scope="module")
def beta_scan():
    """Beta scan at canonical alpha_vac."""
    return scan_A_eff_vs_beta()


@pytest.fixture(scope="module")
def master_result():
    """Full Phase V analysis at canonical parameters."""
    return compute_covariant_interior_analysis()


# ================================================================
# Test classes
# ================================================================

class TestHelperFunctions:
    """Test helper functions and constants parity."""

    def test_alpha_vac_value(self):
        assert abs(ALPHA_VAC - 1.0 / 3.0) < 1e-15

    def test_beta_Q_value(self):
        assert abs(BETA_Q - 2.0) < 1e-15

    def test_epsilon_Q_value(self):
        assert abs(EPSILON_Q - 1.0 / 9.0) < 1e-15

    def test_epsilon_Q_equals_alpha_squared(self):
        assert abs(EPSILON_Q - ALPHA_VAC ** 2) < 1e-15

    def test_C_endpoint_value(self):
        assert abs(C_ENDPOINT - 3.0) < 1e-15

    def test_compactness_at_canon(self):
        C = _compactness(ALPHA_VAC, BETA_Q)
        assert abs(C - 3.0) < 1e-12

    def test_h_of_x_at_zero(self):
        assert _h_of_x(0.0) == 0.0

    def test_h_of_x_positive_for_various_x(self):
        for x in [0.001, 0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 100.0]:
            assert _h_of_x(x) > 0, f"h({x}) should be > 0"

    def test_g_positive_at_canon(self):
        L = abs(math.log(ALPHA_VAC))
        g = _g_of_beta(BETA_Q, L)
        assert g > 0

    def test_A_eff_at_canon(self):
        A = _A_eff_from_constitutive(ALPHA_VAC, BETA_Q)
        assert abs(A - (-1.0)) < 1e-12


class TestInsufficiencyProof:
    """Test the Constitutive Lapse Insufficiency Theorem."""

    def test_alpha_satisfies_bound(self, insufficiency):
        assert insufficiency.alpha_vac_satisfies_bound is True

    def test_alpha_vac_stored(self, insufficiency):
        assert abs(insufficiency.alpha_vac - ALPHA_VAC) < 1e-15

    def test_alpha_vac_critical_stored(self, insufficiency):
        assert abs(insufficiency.alpha_vac_critical - ALPHA_VAC_CRITICAL) < 1e-15

    def test_ln_alpha_abs(self, insufficiency):
        expected = abs(math.log(ALPHA_VAC))
        assert abs(insufficiency.ln_alpha_abs - expected) < 1e-12

    def test_two_L_value(self, insufficiency):
        expected = 2.0 * abs(math.log(ALPHA_VAC))
        assert abs(insufficiency.two_L - expected) < 1e-12

    def test_two_L_ge_one(self, insufficiency):
        assert insufficiency.two_L_ge_one is True

    def test_h_positive_for_all_x(self, insufficiency):
        assert insufficiency.h_positive_for_all_x is True

    def test_g_positive_for_all_beta(self, insufficiency):
        assert insufficiency.g_positive_for_all_beta is True

    def test_A_eff_negative_for_all_finite_beta(self, insufficiency):
        assert insufficiency.A_eff_negative_for_all_finite_beta is True

    def test_sample_A_eff_all_negative(self, insufficiency):
        assert len(insufficiency.sample_A_eff_values) > 0
        for i, A in enumerate(insufficiency.sample_A_eff_values):
            beta = insufficiency.sample_beta_values[i]
            assert A < 0, f"A_eff at beta={beta} should be < 0, got {A}"

    def test_sample_g_all_positive(self, insufficiency):
        for i, g in enumerate(insufficiency.sample_g_values):
            beta = insufficiency.sample_beta_values[i]
            assert g > 0, f"g at beta={beta} should be > 0, got {g}"

    def test_sample_h_all_positive(self, insufficiency):
        for i, h in enumerate(insufficiency.sample_h_values):
            beta = insufficiency.sample_beta_values[i]
            assert h > 0, f"h at beta={beta} should be > 0, got {h}"

    def test_proof_steps_count(self, insufficiency):
        assert len(insufficiency.proof_steps) == 9

    def test_proof_step_1_defines_A_eff(self, insufficiency):
        assert "A_eff" in insufficiency.proof_steps[0]

    def test_proof_step_qed(self, insufficiency):
        assert "QED" in insufficiency.proof_steps[7]

    def test_proof_step_scope(self, insufficiency):
        assert "constitutive" in insufficiency.proof_steps[8].lower()

    def test_theorem_status_proven(self, insufficiency):
        assert insufficiency.theorem_status == "proven"

    def test_scope_statement_is_verbatim(self, insufficiency):
        assert insufficiency.scope_statement == SCOPE_STATEMENT

    def test_edge_case_alpha_too_large(self):
        """Alpha > e^{-1/2}: theorem not applicable by this proof."""
        ip = build_insufficiency_theorem(alpha_vac=0.8)
        assert ip.alpha_vac_satisfies_bound is False
        assert ip.theorem_status == "not_applicable"


class TestThresholdBehavior:
    """Test the theorem at the critical alpha_vac = e^{-1/2} boundary."""

    def test_below_threshold_theorem_holds(self):
        """alpha = e^{-1/2} - epsilon: theorem proven."""
        alpha = ALPHA_VAC_CRITICAL - 0.01
        ip = build_insufficiency_theorem(alpha_vac=alpha)
        assert ip.alpha_vac_satisfies_bound is True
        assert ip.two_L_ge_one is True
        assert ip.theorem_status == "proven"

    def test_at_threshold_exact(self):
        """alpha = e^{-1/2}: boundary case, still satisfies bound (<=)."""
        ip = build_insufficiency_theorem(alpha_vac=ALPHA_VAC_CRITICAL)
        assert ip.alpha_vac_satisfies_bound is True
        # 2L = 2 * 0.5 = 1.0, so 2L >= 1 is satisfied (barely)
        assert ip.two_L_ge_one is True
        assert ip.theorem_status == "proven"

    def test_above_threshold_not_established(self):
        """alpha = e^{-1/2} + epsilon: beyond the universal proof."""
        alpha = ALPHA_VAC_CRITICAL + 0.01
        ip = build_insufficiency_theorem(alpha_vac=alpha)
        assert ip.alpha_vac_satisfies_bound is False
        assert ip.theorem_status == "not_applicable"

    def test_two_L_decreases_with_alpha(self):
        """2L = 2|ln alpha| decreases as alpha increases toward 1."""
        L_low = 2.0 * abs(math.log(0.2))
        L_mid = 2.0 * abs(math.log(0.5))
        L_high = 2.0 * abs(math.log(0.8))
        assert L_low > L_mid > L_high

    def test_canonical_well_below_threshold(self):
        """Canonical alpha = 1/3 ~ 0.333 is well below e^{-1/2} ~ 0.607."""
        assert ALPHA_VAC < ALPHA_VAC_CRITICAL

    def test_threshold_is_e_minus_half(self):
        assert abs(ALPHA_VAC_CRITICAL - math.exp(-0.5)) < 1e-15

    def test_at_threshold_A_eff_still_negative_numerically(self):
        """Even at the boundary, A_eff < 0 at canon beta."""
        A = _A_eff_from_constitutive(ALPHA_VAC_CRITICAL, BETA_Q)
        assert A < 0

    def test_slightly_above_threshold_A_eff_still_negative_at_canon(self):
        """A_eff can still be < 0 above the threshold for specific beta.
        The theorem just isn't universally proven above it."""
        alpha = ALPHA_VAC_CRITICAL + 0.01
        A = _A_eff_from_constitutive(alpha, BETA_Q)
        # The theorem doesn't universally guarantee this above threshold,
        # but numerically it's still negative at beta=2
        assert A < 0


class TestProofConsistency:
    """Verify the mathematical building blocks of the proof directly."""

    def test_h_at_x_0001(self):
        x = 0.001
        h = _h_of_x(x)
        expected = x - math.log(1.0 + x)
        assert abs(h - expected) < 1e-15
        assert h > 0

    def test_h_at_x_001(self):
        x = 0.01
        h = _h_of_x(x)
        assert h > 0
        # For small x, h ~ x^2/2
        assert abs(h - x * x / 2) < x * x * x  # cubic error

    def test_h_at_x_1(self):
        x = 1.0
        h = _h_of_x(x)
        assert abs(h - (1.0 - math.log(2.0))) < 1e-15

    def test_h_at_x_10(self):
        h = _h_of_x(10.0)
        assert h > 0

    def test_h_at_x_100(self):
        h = _h_of_x(100.0)
        assert h > 0

    def test_h_derivative_is_x_over_1_plus_x(self):
        """h'(x) = 1 - 1/(1+x) = x/(1+x) > 0 for x > 0.
        Verify numerically via finite difference."""
        dx = 1e-8
        for x in [0.1, 1.0, 5.0, 50.0]:
            h_prime_numerical = (_h_of_x(x + dx) - _h_of_x(x)) / dx
            h_prime_exact = x / (1.0 + x)
            assert abs(h_prime_numerical - h_prime_exact) < 1e-5

    def test_two_L_ge_one_implies_g_ge_h(self):
        """When 2L >= 1, g(beta) = 2Lx - ln(1+x) >= x - ln(1+x) = h(x)."""
        L = abs(math.log(ALPHA_VAC))
        assert 2.0 * L >= 1.0
        for beta in [0.5, 1.0, 2.0, 5.0, 10.0, 100.0]:
            x = 1.0 / beta
            g = _g_of_beta(beta, L)
            h = _h_of_x(x)
            assert g >= h - 1e-15, f"g({beta}) should be >= h({x})"


class TestEffectiveNEC:
    """Test effective NEC analysis (secondary, constitutive-level)."""

    def test_compactness(self, effective_nec):
        assert abs(effective_nec.compactness - 3.0) < 1e-12

    def test_is_sub_horizon(self, effective_nec):
        assert effective_nec.is_sub_horizon is True

    def test_A_eff_at_canon(self, effective_nec):
        assert abs(effective_nec.A_eff - (-1.0)) < 1e-12

    def test_derivation_level_is_constitutive(self, effective_nec):
        assert effective_nec.derivation_level == "constitutive"

    def test_nec_violating_support_indicated(self, effective_nec):
        assert effective_nec.nec_violating_support_indicated is True

    def test_rho_plus_P_sign_negative(self, effective_nec):
        assert effective_nec.rho_plus_P_sign_effective == "negative"

    def test_not_labeled_as_covariant_theorem(self, effective_nec):
        for note in effective_nec.notes:
            if "NOT a covariant theorem" in note:
                return
        pytest.fail("Must contain note about NOT being a covariant theorem")

    def test_no_gravastar_analogy_field(self, effective_nec):
        """gravastar_analogy should be in notes only, not as a field."""
        assert not hasattr(effective_nec, "gravastar_analogy")


class TestLapseDirection:
    """Test lapse direction failure analysis."""

    def test_compactness(self, lapse_direction):
        assert abs(lapse_direction.compactness - 3.0) < 1e-12

    def test_A_schw(self, lapse_direction):
        assert abs(lapse_direction.A_schw - (-2.0)) < 1e-12

    def test_g_tt_schw(self, lapse_direction):
        # g_tt_schw = -A_schw = 2.0 > 0 (spacelike!)
        assert abs(lapse_direction.g_tt_schw - 2.0) < 1e-12

    def test_t_is_spacelike_schw(self, lapse_direction):
        assert lapse_direction.t_is_spacelike_schw is True

    def test_r_is_timelike_schw(self, lapse_direction):
        assert lapse_direction.r_is_timelike_schw is True

    def test_A_eff(self, lapse_direction):
        assert abs(lapse_direction.A_eff - (-1.0)) < 1e-12

    def test_g_tt_eff_positive(self, lapse_direction):
        # g_tt_eff = -A_eff = 1.0 > 0 (still spacelike)
        assert lapse_direction.g_tt_eff > 0

    def test_constitutive_does_not_restore_timelike(self, lapse_direction):
        assert lapse_direction.constitutive_restores_timelike is False

    def test_naive_redshift_fails(self, lapse_direction):
        assert lapse_direction.naive_redshift_fails is True

    def test_requires_adapted_chart(self, lapse_direction):
        assert lapse_direction.requires_adapted_chart_or_covariant is True


class TestTPhiStatus:
    """Test T^Phi status result."""

    def test_not_lagrangian_derived(self, tphi_status):
        assert tphi_status.is_lagrangian_derived is False

    def test_is_schematic(self, tphi_status):
        assert tphi_status.is_schematic is True

    def test_not_uniquely_specified(self, tphi_status):
        assert tphi_status.is_uniquely_specified is False

    def test_mapping_underdetermined(self, tphi_status):
        assert tphi_status.mapping_underdetermined is True

    def test_underdetermination_reason_nonempty(self, tphi_status):
        assert len(tphi_status.underdetermination_reason) > 20

    def test_missing_for_metric_has_at_least_3(self, tphi_status):
        assert len(tphi_status.missing_for_metric) >= 3

    def test_missing_includes_action(self, tphi_status):
        found = any("action" in m.lower() for m in tphi_status.missing_for_metric)
        assert found, "Missing items should mention a covariant action"


class TestProxyClassification:
    """Test Psi_proxy classification."""

    def test_psi_value(self, proxy_class):
        assert abs(proxy_class.psi_proxy - 1.0 / 3.0) < 1e-12

    def test_level_1_exact(self, proxy_class):
        assert proxy_class.level_1_status == LEVEL_EXACT

    def test_level_2_constitutive_derived(self, proxy_class):
        assert proxy_class.level_2_status == LEVEL_CONSTITUTIVE_DERIVED

    def test_level_3_phase_iv_unresolved(self, proxy_class):
        assert proxy_class.level_3_status_phase_iv == LEVEL_UNRESOLVED

    def test_level_3_phase_v_obstructed(self, proxy_class):
        assert (proxy_class.level_3_status_phase_v
                == LEVEL_CONSTITUTIVE_LAPSE_PROMOTION_OBSTRUCTED)

    def test_is_exact_energy_ratio(self, proxy_class):
        assert proxy_class.is_exact_energy_ratio is True

    def test_is_constitutive_lapse_scale(self, proxy_class):
        assert proxy_class.is_constitutive_lapse_scale is True

    def test_cannot_promote(self, proxy_class):
        assert proxy_class.can_be_promoted_to_true_lapse is False

    def test_cannot_exclude(self, proxy_class):
        assert proxy_class.can_be_excluded is False

    def test_classification_is_surrogate(self, proxy_class):
        assert proxy_class.classification == LEVEL_CONSTITUTIVE_SURROGATE

    def test_scope_of_obstruction_populated(self, proxy_class):
        assert len(proxy_class.scope_of_obstruction) > 20

    def test_scope_mentions_constitutive(self, proxy_class):
        assert "constitutive" in proxy_class.scope_of_obstruction.lower()


class TestStatusLadder:
    """Test Phase IV → Phase V status ladder transition."""

    def test_level_1_unchanged(self, status_ladder):
        assert status_ladder.level_1_before == LEVEL_EXACT
        assert status_ladder.level_1_after == LEVEL_EXACT
        assert status_ladder.level_1_changed is False

    def test_level_2_unchanged(self, status_ladder):
        assert status_ladder.level_2_before == LEVEL_CONSTITUTIVE_DERIVED
        assert status_ladder.level_2_after == LEVEL_CONSTITUTIVE_DERIVED
        assert status_ladder.level_2_changed is False

    def test_level_3_before(self, status_ladder):
        assert status_ladder.level_3_before == LEVEL_UNRESOLVED

    def test_level_3_after(self, status_ladder):
        assert (status_ladder.level_3_after
                == LEVEL_CONSTITUTIVE_LAPSE_PROMOTION_OBSTRUCTED)

    def test_level_3_changed(self, status_ladder):
        assert status_ladder.level_3_changed is True

    def test_level_3_sharpening_reason_nonempty(self, status_ladder):
        assert len(status_ladder.level_3_sharpening_reason) > 20

    def test_no_level_weakened(self, status_ladder):
        assert status_ladder.no_level_weakened is True

    def test_obstruction_scope_populated(self, status_ladder):
        assert len(status_ladder.obstruction_scope) > 20

    def test_obstruction_scope_mentions_constitutive(self, status_ladder):
        assert "constitutive" in status_ladder.obstruction_scope.lower()

    def test_notes_present(self, status_ladder):
        assert len(status_ladder.notes) >= 3


class TestSelfHealing:
    """Test self-healing reconfirmation."""

    def test_source_vanishes(self, self_healing):
        assert self_healing.source_vanishes is True

    def test_source_at_eq_zero(self, self_healing):
        assert self_healing.source_at_eq == 0.0

    def test_independent_of_metric(self, self_healing):
        assert self_healing.independent_of_metric is True

    def test_independent_of_A_eff(self, self_healing):
        assert self_healing.independent_of_A_eff is True

    def test_independent_of_nec(self, self_healing):
        assert self_healing.independent_of_nec is True

    def test_preserved(self, self_healing):
        assert self_healing.preserved is True

    def test_reason_nonempty(self, self_healing):
        assert len(self_healing.reason) > 20


class TestPhase4Reconfirmation:
    """Test Phase IV reconfirmation."""

    def test_level_1_preserved(self, phase4_reconf):
        assert phase4_reconf.level_1_preserved is True

    def test_level_2_preserved(self, phase4_reconf):
        assert phase4_reconf.level_2_preserved is True

    def test_sensitivity_band_preserved(self, phase4_reconf):
        assert phase4_reconf.sensitivity_band_preserved is True

    def test_self_healing_preserved(self, phase4_reconf):
        assert phase4_reconf.self_healing_preserved is True

    def test_shift_estimates_preserved(self, phase4_reconf):
        assert phase4_reconf.shift_estimates_preserved is True

    def test_coincidence_explanation_preserved(self, phase4_reconf):
        assert phase4_reconf.coincidence_explanation_preserved is True

    def test_all_preserved(self, phase4_reconf):
        assert phase4_reconf.all_preserved is True


class TestBetaScan:
    """Test the beta_Q parametric scan."""

    def test_default_scan_length(self, beta_scan):
        assert len(beta_scan) == 8

    def test_all_A_eff_negative(self, beta_scan):
        for entry in beta_scan:
            assert entry.A_eff_is_negative, (
                f"A_eff at beta={entry.beta_Q} should be negative"
            )

    def test_all_A_eff_values_negative(self, beta_scan):
        for entry in beta_scan:
            assert entry.A_eff < 0, (
                f"A_eff at beta={entry.beta_Q} = {entry.A_eff} should be < 0"
            )

    def test_all_g_positive(self, beta_scan):
        for entry in beta_scan:
            assert entry.g_of_beta > 0, (
                f"g at beta={entry.beta_Q} should be > 0"
            )

    def test_all_h_positive(self, beta_scan):
        for entry in beta_scan:
            assert entry.h_of_x > 0, (
                f"h at beta={entry.beta_Q} should be > 0"
            )

    def test_canon_A_eff_is_minus_one(self, beta_scan):
        canon_entries = [e for e in beta_scan if abs(e.beta_Q - 2.0) < 1e-10]
        assert len(canon_entries) == 1
        assert abs(canon_entries[0].A_eff - (-1.0)) < 1e-12

    def test_g_of_beta_decreasing_with_beta(self, beta_scan):
        """g(beta) should decrease as beta increases (x = 1/beta decreases)."""
        for i in range(len(beta_scan) - 1):
            assert beta_scan[i].g_of_beta > beta_scan[i + 1].g_of_beta, (
                f"g should decrease: g({beta_scan[i].beta_Q}) = "
                f"{beta_scan[i].g_of_beta} should be > "
                f"g({beta_scan[i+1].beta_Q}) = {beta_scan[i+1].g_of_beta}"
            )

    def test_A_eff_increasing_toward_zero_with_beta(self, beta_scan):
        """A_eff(beta) should increase toward 0⁻ as beta increases."""
        for i in range(len(beta_scan) - 1):
            assert beta_scan[i].A_eff < beta_scan[i + 1].A_eff, (
                f"A_eff should increase: A_eff({beta_scan[i].beta_Q}) = "
                f"{beta_scan[i].A_eff} should be < "
                f"A_eff({beta_scan[i+1].beta_Q}) = {beta_scan[i+1].A_eff}"
            )

    def test_A_eff_approaches_zero_at_large_beta(self, beta_scan):
        """At beta=500, A_eff should be negative but close to 0."""
        last = beta_scan[-1]
        assert last.beta_Q == 500.0
        assert last.A_eff < 0
        assert last.A_eff > -0.1  # close to zero

    def test_compactness_values(self, beta_scan):
        """Each C = alpha^{-2/beta} should match the helper."""
        for entry in beta_scan:
            expected_C = _compactness(ALPHA_VAC, entry.beta_Q)
            assert abs(entry.C - expected_C) < 1e-12


class TestMasterResult:
    """Test the master CovariantInteriorResult."""

    def test_valid(self, master_result):
        assert master_result.valid is True

    def test_has_insufficiency_theorem(self, master_result):
        assert master_result.insufficiency_theorem is not None
        assert master_result.insufficiency_theorem.theorem_status == "proven"

    def test_has_effective_nec(self, master_result):
        assert master_result.effective_nec is not None

    def test_has_lapse_direction(self, master_result):
        assert master_result.lapse_direction is not None

    def test_has_tphi_status(self, master_result):
        assert master_result.tphi_status is not None

    def test_has_proxy_classification(self, master_result):
        assert master_result.proxy_classification is not None

    def test_has_status_ladder(self, master_result):
        assert master_result.status_ladder is not None

    def test_has_self_healing(self, master_result):
        assert master_result.self_healing is not None

    def test_has_phase4_reconfirmation(self, master_result):
        assert master_result.phase4_reconfirmation is not None

    def test_nonclaims_at_least_12(self, master_result):
        assert len(master_result.nonclaims) >= 12

    def test_obstruction_is_about_constitutive_ansatz(self, master_result):
        assert master_result.obstruction_is_about_constitutive_ansatz is True

    def test_scope_statement_in_theorem(self, master_result):
        assert (master_result.insufficiency_theorem.scope_statement
                == SCOPE_STATEMENT)

    def test_scope_mentions_naive_constitutive(self, master_result):
        found = any("naive constitutive" in nc.lower()
                     for nc in master_result.nonclaims)
        assert found

    def test_diagnostics_populated(self, master_result):
        d = master_result.diagnostics
        assert d["theorem_proven"] is True
        assert d["self_healing_preserved"] is True
        assert d["phase4_preserved"] is True
        assert d["obstruction_is_about_constitutive_ansatz"] is True
        assert d["n_nonclaims"] >= 12

    def test_beta_scan_present(self, master_result):
        assert len(master_result.beta_scan) == 8

    def test_remaining_obstructions(self, master_result):
        assert len(master_result.remaining_obstructions) >= 2

    def test_approx_status_nonempty(self, master_result):
        assert len(master_result.approx_status) > 20


class TestSerialization:
    """Test serialization to dict and JSON roundtrip."""

    def test_to_dict_is_dict(self, master_result):
        d = covariant_interior_result_to_dict(master_result)
        assert isinstance(d, dict)

    def test_to_dict_valid(self, master_result):
        d = covariant_interior_result_to_dict(master_result)
        assert d["valid"] is True

    def test_json_roundtrip(self, master_result):
        d = covariant_interior_result_to_dict(master_result)
        s = json.dumps(d)
        d2 = json.loads(s)
        assert d2["valid"] is True

    def test_scope_preserved_in_dict(self, master_result):
        d = covariant_interior_result_to_dict(master_result)
        assert d["insufficiency_theorem"]["scope_statement"] == SCOPE_STATEMENT

    def test_nonclaims_in_dict(self, master_result):
        d = covariant_interior_result_to_dict(master_result)
        assert len(d["nonclaims"]) >= 12

    def test_beta_scan_in_dict(self, master_result):
        d = covariant_interior_result_to_dict(master_result)
        assert len(d["beta_scan"]) == 8

    def test_obstruction_flag_in_dict(self, master_result):
        d = covariant_interior_result_to_dict(master_result)
        assert d["obstruction_is_about_constitutive_ansatz"] is True
