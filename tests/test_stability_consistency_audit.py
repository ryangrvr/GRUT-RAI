"""Tests for Appendix E Pass 2: Stability and Consistency Audit.

These tests verify that the four deterministic checks produce the
correct classifications and numerical results, and that no unsupported
"full consistency" claim appears anywhere in the audit output.

WHAT THESE TESTS DO NOT VERIFY:
- They do NOT verify global consistency of GRUT
- They do NOT verify that root failures are resolved
- They do NOT upgrade the Appendix E classification
- They do NOT run simulations

TEST STRUCTURE:
  test_check1_* — τ_eff self-consistency ratio per sector
  test_check2_* — Q from three independent routes
  test_check3_* — Φ boundary condition at endpoint
  test_check4_* — T_Q2 extraction vs thermodynamic candidates
  test_guard_*  — Guard tests: no unsupported claims
"""

import math
import pytest

from grut.stability_consistency_audit import (
    M_REF_KG,
    TAU_0_S,
    ALPHA_VAC,
    BETA_Q,
    EPSILON_Q,
    R_EQ_OVER_RS,
    Q_CANONICAL,
    G_SI,
    C_SI,
    HBAR_SI,
    K_B,
    _FORBIDDEN_PASS2_CLASSIFICATIONS,
    run_check1,
    run_check2,
    run_check3,
    run_check4,
    run_pass2_audit,
    Pass2AuditResult,
)


# ================================================================
# Check 1: τ_eff self-consistency
# ================================================================

class TestCheck1TauEffConsistency:

    def test_tau_collapse_at_equilibrium_equals_tau0(self):
        """At V=0, the collapse formula gives τ_eff = τ₀."""
        r = run_check1()
        assert abs(r.tau_collapse_at_equilibrium_s - TAU_0_S) < 1e-6 * TAU_0_S

    def test_tau_local_pde_is_dynamical_scale(self):
        """τ_local (interior PDE) should be much smaller than τ₀ at astrophysical masses."""
        r = run_check1()
        assert r.tau_local_pde_s < TAU_0_S * 1e-10, (
            f"tau_local = {r.tau_local_pde_s:.2e} should be astrophysical scale, "
            f"not cosmological (tau_0 = {TAU_0_S:.2e})"
        )

    def test_tau_ratio_is_large(self):
        """τ ratio at equilibrium should be ~10^19 for a 30 M_sun BH."""
        r = run_check1()
        # ratio ≈ omega_0 * tau_0 ~ 1.76e4 * 1.32e15 ≈ 2.3e19
        assert r.tau_ratio > 1e18, (
            f"tau ratio should be >10^18 for astrophysical BH, got {r.tau_ratio:.2e}"
        )
        assert r.tau_ratio < 1e21, (
            f"tau ratio should be <10^21, got {r.tau_ratio:.2e}"
        )

    def test_tau_ratio_equals_omega0_tau0(self):
        """The tau ratio should equal ω₀·τ₀ (the structural mismatch factor)."""
        r = run_check1()
        assert abs(r.tau_ratio - r.omega_0_tau_0) / r.omega_0_tau_0 < 0.01

    def test_structural_identity_holds_for_tau_local(self):
        """ω₀·τ_local ≈ 1 (gravitational scaling relation)."""
        r = run_check1()
        assert r.structural_identity_holds, (
            f"omega_0 * tau_local = {r.omega_0_tau_local:.4f}, "
            f"should be ≈ 1"
        )

    def test_q2_resonance_does_not_hold_numerically(self):
        """ω₀ ≠ Ω = 1/τ₀ numerically — Q2 resonance claim is false."""
        r = run_check1()
        assert not r.resonance_holds_numerically, (
            f"Q2 resonance condition omega_0 = 1/tau_0 should NOT hold numerically. "
            f"omega_0 = {r.omega_0_actual_rad_s:.2e} rad/s, "
            f"Omega = {r.omega_bath_cutoff_rad_s:.2e} rad/s, "
            f"ratio = {r.resonance_ratio:.2e}"
        )

    def test_check1_classification(self):
        """Check 1 must classify as tau_eff_tensioned_across_sectors."""
        r = run_check1()
        assert r.classification == "tau_eff_tensioned_across_sectors", (
            f"Expected 'tau_eff_tensioned_across_sectors', got '{r.classification}'"
        )

    def test_check1_structural_identity_uses_correct_tau(self):
        """The structural identity must document using tau_local, not tau_0."""
        r = run_check1()
        assert "tau_local" in r.structural_identity_uses_tau.lower() or \
               "gravitational" in r.structural_identity_uses_tau.lower(), (
            "Structural identity must document it uses tau_local (gravitational scaling), "
            f"not tau_eff from constitutive law. Got: {r.structural_identity_uses_tau}"
        )


# ================================================================
# Check 2: Q from three routes
# ================================================================

class TestCheck2QRoutes:

    def test_all_routes_give_q_near_6(self):
        """All three Q routes should give approximately 6 at canonical parameters."""
        r = run_check2()
        for label, q in [("A", r.q_route_a), ("B", r.q_route_b), ("C", r.q_route_c)]:
            assert 5.0 < q < 8.0, (
                f"Route {label}: Q = {q:.3f}, expected in range [5, 8]"
            )

    def test_route_a_formula(self):
        """Route A: Q = β_Q/α_vac = 6."""
        r = run_check2()
        expected = BETA_Q / ALPHA_VAC
        assert abs(r.q_route_a - expected) < 1e-10

    def test_route_b_reduces_to_route_a(self):
        """Routes A and B must be algebraically identical at canonical parameters."""
        r = run_check2()
        assert r.route_b_reduces_to_a, (
            f"Route B (Q={r.q_route_b:.6f}) should equal Route A (Q={r.q_route_a:.6f}) "
            f"algebraically at omega_0*tau_local = 1"
        )

    def test_route_c_is_beta_q_independent(self):
        """Route C must be documented as β_Q-independent."""
        r = run_check2()
        assert r.route_c_beta_q_independent, (
            "Route C (interior waves) should be independent of beta_Q. "
            "It derives Q = 2/alpha_vac, not beta_Q/alpha_vac."
        )

    def test_routes_b_c_disagree_at_noncanonical_beta_q(self):
        """At β_Q = 1.5, Routes B and C should diverge."""
        r = run_check2()
        # Route B at β_Q = 1.5 gives Q ≠ 6, Route C tracking may also change
        # The key result is that they are NOT equal at non-canonical β_Q
        assert not r.routes_b_c_agree_at_noncanonical_beta_q, (
            f"At beta_Q = 1.5: Route B gives Q = {r.q_route_b_at_beta_q_15:.3f}, "
            f"Route C gives Q = {r.q_route_c_at_beta_q_15:.3f}. "
            f"These should differ if routes are not both fully beta_Q-dependent."
        )

    def test_beta_q_assumed_not_derived(self):
        """The module must document β_Q = 2 as assumed, not derived."""
        r = run_check2()
        assert r.beta_q_is_assumed_not_derived
        assert r.beta_q_controls_routes_a_and_b
        assert r.beta_q_does_not_control_route_c

    def test_check2_classification(self):
        """Check 2 must classify as q_numerically_aligned_but_not_independent."""
        r = run_check2()
        assert r.classification == "q_numerically_aligned_but_not_independent", (
            f"Expected 'q_numerically_aligned_but_not_independent', got '{r.classification}'"
        )

    def test_shared_assumptions_documented(self):
        """Check 2 must list shared assumptions preventing independence."""
        r = run_check2()
        assert len(r.shared_assumptions) >= 3, (
            f"Expected ≥3 shared assumptions documented, got {len(r.shared_assumptions)}"
        )


# ================================================================
# Check 3: Φ boundary condition
# ================================================================

class TestCheck3PhiBoundary:

    def test_phi_barrier_at_req_equals_one(self):
        """Φ_barrier at R_eq should equal 1: ε_Q × 3^β_Q = (1/9) × 9 = 1."""
        r = run_check3()
        assert abs(r.phi_barrier_at_req - 1.0) < 1e-10, (
            f"Phi_barrier at R_eq = {r.phi_barrier_at_req:.8f}, expected 1.0"
        )

    def test_phi_constitutive_at_req_equals_one(self):
        """Φ_constitutive at steady state equals 1 (M_drive/a_grav at equilibrium)."""
        r = run_check3()
        assert abs(r.phi_constitutive_at_req - 1.0) < 1e-10, (
            f"Phi_constitutive at equilibrium = {r.phi_constitutive_at_req}, expected 1.0"
        )

    def test_phi_values_equal_at_endpoint(self):
        """Both Φ objects must be equal at R_eq (formal consistency)."""
        r = run_check3()
        assert r.phi_values_equal_at_req, (
            f"Phi_barrier = {r.phi_barrier_at_req}, "
            f"Phi_constitutive = {r.phi_constitutive_at_req}. "
            f"Should be equal at endpoint."
        )

    def test_endpoint_agreement_is_by_construction(self):
        """The module must document that endpoint agreement is by construction."""
        r = run_check3()
        assert r.phi_agreement_is_by_construction, (
            "Endpoint agreement must be documented as a consequence of the "
            "endpoint law derivation, not as independent verification."
        )

    def test_off_equilibrium_tracking_not_same(self):
        """The two Φ objects must be documented as NOT tracking the same off-R_eq."""
        r = run_check3()
        assert not r.off_equilibrium_tracking_is_same, (
            "Off-equilibrium: Phi_barrier is R-dependent only; "
            "Phi_constitutive is a history-dependent ODE solution. "
            "They should NOT be flagged as tracking the same quantity."
        )

    def test_check3_endpoint_classification(self):
        """Check 3 must classify endpoint relation as phi_endpoint_relation_viable."""
        r = run_check3()
        assert r.classification == "phi_endpoint_relation_viable", (
            f"Expected 'phi_endpoint_relation_viable', got '{r.classification}'"
        )

    def test_check3_off_equilibrium_classification(self):
        """Check 3 must classify off-equilibrium relation as underdetermined."""
        r = run_check3()
        assert r.classification_off_equilibrium == "phi_relation_underdetermined", (
            f"Expected 'phi_relation_underdetermined', "
            f"got '{r.classification_off_equilibrium}'"
        )

    def test_epsilon_q_arithmetic(self):
        """Verify: ε_Q × 3^β_Q = (1/9) × 9 = 1 exactly."""
        phi_check = EPSILON_Q * (3.0 ** BETA_Q)
        assert abs(phi_check - 1.0) < 1e-12, (
            f"epsilon_Q * 3^beta_Q = {phi_check:.12f}, should be exactly 1.0"
        )


# ================================================================
# Check 4: T_Q2
# ================================================================

class TestCheck4TQ2:

    def test_t_q2_is_flagged_as_category_error(self):
        """T_Q2 = ℏΩ/k_B must be flagged as a category error."""
        r = run_check4()
        assert r.t_q2_is_category_error, (
            "T_Q2 = hbar/(k_B*tau_0) is a category error — it conflates the "
            "bath cutoff energy with the bath temperature."
        )

    def test_q2_does_not_constrain_temperature(self):
        """Q2 must be flagged as NOT constraining the bath temperature."""
        r = run_check4()
        assert not r.q2_constrains_bath_temperature, (
            "Q2 identifies bath spectral shape and cutoff, but NOT temperature. "
            "Temperature enters the FDT as an independent parameter."
        )

    def test_t_q2_far_below_all_candidates(self):
        """T_Q2 should be many orders of magnitude below the lowest Appendix D candidate."""
        r = run_check4()
        assert r.t_q2_orders_of_magnitude_below_lowest_candidate > 15, (
            f"T_Q2 should be >15 orders of magnitude below lowest candidate. "
            f"Got: {r.t_q2_orders_of_magnitude_below_lowest_candidate:.1f} OOM"
        )

    def test_t_q2_does_not_match_any_candidate(self):
        """T_Q2 must NOT match any Appendix D candidate within factor of 2."""
        r = run_check4()
        assert not r.t_q2_matches_any_candidate_within_factor_2, (
            "T_Q2 should not match any temperature candidate — it is ~10^18+ times smaller."
        )

    def test_four_candidates_defined(self):
        """The module must define exactly 4 temperature candidates (not 6)."""
        r = run_check4()
        assert r.n_candidates == 4, (
            f"Expected 4 temperature candidates (not 6 as in Pass 1 overcount). "
            f"Got: {r.n_candidates}"
        )

    def test_two_grut_native_candidates(self):
        """Exactly 2 temperature candidates should be GRUT-native."""
        r = run_check4()
        n_native = sum(1 for c in r.candidates if c.grut_native)
        assert n_native == 2, (
            f"Expected 2 GRUT-native candidates (T_dissipation, T_structural). "
            f"Got: {n_native}"
        )

    def test_q2_resonance_does_not_hold(self):
        """The Q2 resonance condition ω₀ = Ω should NOT hold numerically."""
        r = run_check4()
        assert not r.q2_resonance_condition_holds_numerically, (
            "Q2 resonance condition omega_0 = 1/tau_0 should not hold numerically "
            "for astrophysical masses."
        )

    def test_check4_classification(self):
        """Check 4 must classify as q2_temperature_noninformative."""
        r = run_check4()
        assert r.classification == "q2_temperature_noninformative", (
            f"Expected 'q2_temperature_noninformative', got '{r.classification}'"
        )

    def test_q4_deficit_unchanged(self):
        """Q4 temperature deficit must be reported as unchanged."""
        r = run_check4()
        assert r.q4_temperature_deficit_unchanged, (
            "Q4 temperature deficit (temperature as missing ingredient) "
            "must remain unchanged after Check 4."
        )

    def test_t_q2_value(self):
        """T_Q2 = ℏ/(k_B·τ₀) should be approximately 5.78 × 10^-27 K."""
        r = run_check4()
        expected = HBAR_SI / (K_B * TAU_0_S)
        assert abs(r.t_q2_category_error_kelvin - expected) < 0.01 * expected, (
            f"T_Q2 = {r.t_q2_category_error_kelvin:.2e} K, "
            f"expected {expected:.2e} K"
        )


# ================================================================
# Guard tests: no unsupported claims
# ================================================================

class TestGuardNoUnsupportedClaims:

    def test_overall_determination_is_not_fully_coherent(self):
        """The overall Pass 2 determination must NOT claim full coherence."""
        result = run_pass2_audit()
        for forbidden in _FORBIDDEN_PASS2_CLASSIFICATIONS:
            assert forbidden not in result.pass2_overall_determination, (
                f"FORBIDDEN CLAIM in overall determination: '{forbidden}'"
            )

    def test_classification_unchanged_from_pass1(self):
        """The Appendix E classification must remain unchanged from Pass 1."""
        result = run_pass2_audit()
        assert result.classification_unchanged
        assert result.pass2_overall_determination == "locally_consistent_globally_underdetermined"

    def test_assert_no_unsupported_claims_passes(self):
        """The guard method must not raise for a valid audit result."""
        result = run_pass2_audit()
        result.assert_no_unsupported_claims()  # Should not raise

    def test_module_is_valid(self):
        """run_pass2_audit() must return a valid result."""
        result = run_pass2_audit()
        assert result.valid

    def test_all_four_checks_present(self):
        """All four checks must be present in the result."""
        result = run_pass2_audit()
        assert result.check1.classification != "", "Check 1 must have a classification"
        assert result.check2.classification != "", "Check 2 must have a classification"
        assert result.check3.classification != "", "Check 3 must have a classification"
        assert result.check4.classification != "", "Check 4 must have a classification"

    def test_forbidden_claim_guard_raises_on_bad_input(self):
        """The guard must raise AssertionError if a forbidden claim is injected."""
        result = run_pass2_audit()
        original = result.pass2_overall_determination
        # Inject a forbidden classification
        result.pass2_overall_determination = "appears_coherent_in_claimed_regimes"
        with pytest.raises(AssertionError):
            result.assert_no_unsupported_claims()
        # Restore
        result.pass2_overall_determination = original

    def test_to_dict_serializes_without_error(self):
        """The full result must serialize to dict without error."""
        result = run_pass2_audit()
        d = result.to_dict()
        assert isinstance(d, dict)
        assert "check1" in d
        assert "check2" in d
        assert "check3" in d
        assert "check4" in d
        assert d["pass2_overall_determination"] == "locally_consistent_globally_underdetermined"


# ================================================================
# Numerical cross-checks
# ================================================================

class TestNumericalCrossChecks:

    def test_canonical_q_equals_beta_q_over_alpha_vac(self):
        """Verify Q_CANONICAL = β_Q/α_vac = 6."""
        assert abs(Q_CANONICAL - BETA_Q / ALPHA_VAC) < 1e-12
        assert abs(Q_CANONICAL - 6.0) < 1e-12

    def test_r_eq_over_rs_equals_one_third(self):
        """Verify R_eq/r_s = ε_Q^(1/β_Q) = (1/9)^(1/2) = 1/3."""
        assert abs(R_EQ_OVER_RS - 1.0 / 3.0) < 1e-12

    def test_epsilon_q_equals_alpha_vac_squared(self):
        """Verify ε_Q = α_vac² = 1/9."""
        assert abs(EPSILON_Q - ALPHA_VAC**2) < 1e-12
        assert abs(EPSILON_Q - 1.0 / 9.0) < 1e-12

    def test_omega_0_tau_local_approximately_one(self):
        """ω₀·τ_local ≈ 1 at equilibrium (structural identity)."""
        r = run_check1()
        assert abs(r.omega_0_tau_local - 1.0) < 0.05, (
            f"omega_0 * tau_local = {r.omega_0_tau_local:.4f}, should be ≈ 1.0"
        )

    def test_tau_ratio_equals_omega0_times_tau0(self):
        """The tau ratio should be ω₀·τ₀ (same factor appears in Q2 resonance)."""
        r = run_check1()
        # tau_collapse / tau_local ≈ tau_0 / t_dyn ≈ omega_0 * tau_0
        assert abs(math.log10(r.tau_ratio) - math.log10(r.omega_0_tau_0)) < 0.1, (
            f"tau_ratio = {r.tau_ratio:.2e}, omega_0_tau_0 = {r.omega_0_tau_0:.2e}. "
            f"Should agree within 10% on log scale."
        )
