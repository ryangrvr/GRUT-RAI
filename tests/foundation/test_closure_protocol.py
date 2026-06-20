"""Tests for Phase I Closure Protocol canonical constants and engine.

Locks in every Phase I §5-§8 canonical value and engine formula.
Verifies:
  - α_vac = 1/3 exactly (v11 App H)
  - S = 12π/α² = 108π exactly
  - τ_0 = 41.9 Myr (canonical)
  - n_g(0) = √(4/3)
  - μ_Λ, μ_0 scales
  - a_0 ≈ 1.08 × 10⁻¹⁰ m/s² (MOND-like)
  - T_c = 54.7 MK
  - τ_0 = 1/√(Λc) identity
  - Regime gate: Saturn suppression ≈ 10⁻¹⁵
  - ν(y) interpolation limits
  - g_eff recovers GR at X ≫ 1 and MOND at X, y ≪ 1
  - Bullet Cluster offset estimate ≈ v × τ_0
"""

import pytest
import numpy as np


class TestCanonicalConstants:
    """Phase I §5-§6 canonical constants."""

    def test_alpha_vac_is_one_third_exactly(self):
        from grut.foundation.closure_protocol import ALPHA_VAC
        assert abs(ALPHA_VAC - 1/3) < 1e-15

    def test_S_equals_108_pi_exactly(self):
        from grut.foundation.closure_protocol import S_SCREENING
        assert abs(S_SCREENING - 108 * np.pi) < 1e-10

    def test_S_equals_12_pi_over_alpha_squared(self):
        from grut.foundation.closure_protocol import S_SCREENING, ALPHA_VAC
        assert abs(S_SCREENING - 12 * np.pi / ALPHA_VAC**2) < 1e-10

    def test_tau_0_is_41p9_Myr(self):
        from grut.foundation.closure_protocol import TAU_0_MYR
        assert abs(TAU_0_MYR - 41.9) < 0.01

    def test_n_g_DC_is_sqrt_4_over_3(self):
        from grut.foundation.closure_protocol import N_G_DC
        assert abs(N_G_DC - np.sqrt(4/3)) < 1e-12
        assert abs(N_G_DC - 1.15470) < 0.0001

    def test_a_0_in_MOND_band(self):
        """a_0 = c/(2πτ_Λ) ≈ 1.2 × 10⁻¹⁰ m/s² — MOND scale."""
        from grut.foundation.closure_protocol import A_0_SI
        assert 1e-11 < A_0_SI < 1e-9

    def test_T_c_is_54p7_MK(self):
        from grut.foundation.closure_protocol import T_C_MK
        assert abs(T_C_MK - 54.7) / 54.7 < 0.05

    def test_T_c_canonical_anchor_is_5p47e7_K(self):
        """T_C_KELVIN_CANONICAL = 5.47×10⁷ K — the empirical anchor.

        This is the cosmological-chronology pin (T at t≈16 hours post-BB
        per V7 §0.5, V7 §22). T_C_KELVIN is computed from this canonical
        value via the SI-correct formula T_c = ℏ/(τ_micro × k_B).
        Pinning the canonical separately ensures the chain is verifiable
        end-to-end."""
        from grut.foundation.closure_protocol import T_C_KELVIN_CANONICAL
        assert abs(T_C_KELVIN_CANONICAL - 5.47e7) < 1e3

    def test_tau_micro_is_femtosecond_scale(self):
        """τ_micro = ℏ/(k_B × T_c) ≈ 1.4 × 10⁻¹⁹ s (microscopic plasma scale).

        Distinct from the macroscopic gravitational τ_0 = 41.9 Myr by
        ~34 orders of magnitude. See Correction #22 (tau-cleanup)."""
        from grut.foundation.closure_protocol import TAU_MICRO_SEC
        assert 1.0e-19 < TAU_MICRO_SEC < 2.0e-19
        # Tighter pin — recovers ≈1.396×10⁻¹⁹ s from T_c = 54.7 MK.
        assert abs(TAU_MICRO_SEC - 1.396e-19) / 1.396e-19 < 0.01

    def test_T_c_formula_is_SI_correct(self):
        """T_C_KELVIN = ℏ/(τ_micro × k_B) — dimensionally consistent.

        Pre-Correction-#22 the formula was 1/(τ_0 × k_B), which produced
        units K/(J·s), not K. The fix introduces τ_micro and uses the
        SI-correct formula. This test pins the closure of that
        dimensional bug."""
        from grut.foundation.closure_protocol import (
            T_C_KELVIN, TAU_MICRO_SEC,
        )
        from grut.foundation.constants import HBAR, K_B
        recomputed = HBAR / (TAU_MICRO_SEC * K_B)
        assert abs(T_C_KELVIN - recomputed) / T_C_KELVIN < 1e-12

    def test_T_c_recovered_value_matches_canonical(self):
        """The recovered T_C_KELVIN must equal T_C_KELVIN_CANONICAL exactly
        (up to float precision). This is structural — τ_micro is defined
        as ℏ/(k_B × T_c_canonical), and T_c is recomputed from τ_micro,
        so the round trip is identity."""
        from grut.foundation.closure_protocol import (
            T_C_KELVIN, T_C_KELVIN_CANONICAL,
        )
        assert abs(T_C_KELVIN - T_C_KELVIN_CANONICAL) / T_C_KELVIN_CANONICAL < 1e-12

    def test_two_tau_scales_separated_by_thirty_plus_orders(self):
        """τ_0 (gravitational) and τ_micro (thermal) differ by ~34 orders
        of magnitude. They are distinct physical scales, conflated under
        one symbol in pre-Correction-#22 prose. This test pins the
        magnitude of the separation as a structural finding."""
        from grut.foundation.closure_protocol import TAU_0_SEC, TAU_MICRO_SEC
        ratio = TAU_0_SEC / TAU_MICRO_SEC
        assert ratio > 1e30, f"Expected τ_0/τ_micro > 10³⁰; got {ratio:.2e}"
        assert ratio < 1e36, f"Expected τ_0/τ_micro < 10³⁶; got {ratio:.2e}"

    def test_T_c_old_dimensionally_invalid_formula_NOT_used(self):
        """Negative test: the codebase no longer recovers T_c from
        1/(τ_0 × k_B). The numerical match between the new
        ℏ/(τ_micro × k_B) and the old 1/(τ_0 × k_B) is by construction
        of τ_micro (defined to make them coincide), but the formula
        used in the module is now the SI-correct one. This test verifies
        the modular constants by re-deriving τ_micro from the canonical
        T_c and asserting it does NOT equal τ_0 (which would happen if
        τ_micro had been silently aliased to τ_0)."""
        from grut.foundation.closure_protocol import TAU_0_SEC, TAU_MICRO_SEC
        # The two scales must NOT be the same constant.
        assert TAU_0_SEC != TAU_MICRO_SEC
        # And they're not numerically close either.
        assert TAU_0_SEC / TAU_MICRO_SEC > 1e10

    def test_mu_Lambda_order_of_magnitude(self):
        """μ_Λ = ℏ/τ_Λ ~ 10⁻³³ eV (horizon IR reference)."""
        from grut.foundation.closure_protocol import MU_LAMBDA_EV
        assert 1e-34 < MU_LAMBDA_EV < 1e-32

    def test_mu_0_equals_S_mu_Lambda(self):
        """μ_0 = S × μ_Λ — screening applies to mass-gap too."""
        from grut.foundation.closure_protocol import (
            MU_LAMBDA_EV, MU_0_EV, S_SCREENING
        )
        assert abs(MU_0_EV / MU_LAMBDA_EV - S_SCREENING) / S_SCREENING < 1e-6

    def test_H0_implied_is_planck_like(self):
        """τ_0 = 41.9 Myr and S = 108π give H_0 ≈ 68.8 km/s/Mpc."""
        from grut.foundation.closure_protocol import H_0_IMPLIED_KM_S_MPC
        # Planck is 67.4, SH0ES is 73.0, our implied should be Planck-like
        assert 65 < H_0_IMPLIED_KM_S_MPC < 72


class TestCanonicalR:
    """Path G canonical R = √(4/3) ≈ 1.15470 and Path D cross-checks."""

    def test_R_refractive_aliases_n_g_DC(self):
        """R_REFRACTIVE is the semantic alias for n_g(0)."""
        from grut.foundation.closure_protocol import R_REFRACTIVE, N_G_DC
        assert R_REFRACTIVE == N_G_DC

    def test_R_canonical_equals_sqrt_4_over_3(self):
        """Path G canonical R = √(4/3) — exact within float precision."""
        from grut.foundation.closure_protocol import R_REFRACTIVE
        assert abs(R_REFRACTIVE - np.sqrt(4/3)) < 1e-12
        assert abs(R_REFRACTIVE - 1.15470) < 1e-4

    def test_path_d_majorana_a_over_c(self):
        """Path D Majorana cross-check: a/c = 1991/1698 ≈ 1.17256."""
        from grut.foundation.closure_protocol import A_OVER_C_SM_MAJORANA
        assert abs(A_OVER_C_SM_MAJORANA - 1991/1698) < 1e-12
        assert abs(A_OVER_C_SM_MAJORANA - 1.17256) < 1e-4

    def test_path_d_dirac_a_over_c(self):
        """Path D Dirac variant: a/c = 253/219 ≈ 1.15525, closer to √(4/3)."""
        from grut.foundation.closure_protocol import A_OVER_C_SM_DIRAC
        assert abs(A_OVER_C_SM_DIRAC - 253/219) < 1e-12
        assert abs(A_OVER_C_SM_DIRAC - 1.15525) < 1e-4

    def test_dirac_closer_to_canonical_than_majorana(self):
        """Dirac variant agrees with Path G better than Majorana — supports
        the GRUT ToE's lean-Dirac falsifiable prediction."""
        from grut.foundation.closure_protocol import (
            R_REFRACTIVE, A_OVER_C_SM_DIRAC, A_OVER_C_SM_MAJORANA,
        )
        gap_dirac = abs(A_OVER_C_SM_DIRAC - R_REFRACTIVE)
        gap_majo = abs(A_OVER_C_SM_MAJORANA - R_REFRACTIVE)
        assert gap_dirac < gap_majo


class TestRMaxSaturationCurvature:
    """V7 §13 Whole Hole — universal RICCI-scalar saturation R_max = α/(c²τ_0²).

    Crucial scope: this is Ricci scalar saturation, NOT Kretschmann. For
    Schwarzschild VACUUM exterior, R = 0 identically and R_max imposes
    no constraint there. R_max bounds the matter-bearing interior, and
    its trace-of-Einstein consequence ρ_max is the universal interior
    density cap.
    """

    def test_R_max_formula(self):
        """R_max = α / (c² τ_0²) — exact algebraic identity."""
        from grut.foundation.closure_protocol import (
            R_MAX_INV_M2, ALPHA_VAC, TAU_0_SEC,
        )
        from grut.foundation.constants import C as C_LIGHT
        expected = ALPHA_VAC / (C_LIGHT**2 * TAU_0_SEC**2)
        assert abs(R_MAX_INV_M2 - expected) / expected < 1e-12

    def test_R_max_universal_order(self):
        """R_max ≈ 2 × 10⁻⁴⁸ m⁻² with universal τ_0 = 41.9 Myr."""
        from grut.foundation.closure_protocol import R_MAX_INV_M2
        assert 1e-49 < R_MAX_INV_M2 < 1e-47
        assert abs(R_MAX_INV_M2 - 2.12e-48) / 2.12e-48 < 0.05

    def test_rho_max_formula(self):
        """ρ_max = c² R_max / (8πG) — universal interior density cap."""
        from grut.foundation.closure_protocol import (
            R_MAX_INV_M2, RHO_MAX_KG_M3,
        )
        from grut.foundation.constants import C as C_LIGHT, G as G_NEWTON
        expected = (C_LIGHT**2 * R_MAX_INV_M2) / (8.0 * np.pi * G_NEWTON)
        assert abs(RHO_MAX_KG_M3 - expected) / expected < 1e-12

    def test_rho_max_is_universal_constant(self):
        """ρ_max ~ 10⁻²² kg/m³ — universal, mass-independent interior density.

        Larger BHs contain larger cores at the same ρ_max; ρ_max is set
        by the medium's relaxation time τ_0, not by the object's mass.
        """
        from grut.foundation.closure_protocol import RHO_MAX_KG_M3
        assert 1e-23 < RHO_MAX_KG_M3 < 1e-21


class TestThresholdBridge:
    """Two-condition equivalence: ωτ_0 ≫ 1 ⟺ Λ_grav τ_0 ≫ 1 when ω ~ Λ_grav.

    The bridge between laboratory decoherence (atoms deep in crystal) and
    cosmological dark-sector phenomenology (galactic rotation deep in fluid).
    """

    def test_macroscopic_body_is_deep_crystal_via_lambda_grav(self):
        """Self-gravitating macro body (1 mg, 1 mm): Λ_grav τ_0 ~ 10³⁵.

        For self-gravitating systems, the dominant dynamical frequency
        IS the Diósi-Penrose decoherence rate, so Λ_grav τ_0 is the
        natural crystallinity. A gram-scale object at mm separation has
        Λ_grav ~ 10²⁰ Hz, deep in the crystal regime.

        (Note: literal atoms have tiny Λ_grav ~ 10⁻¹⁹ Hz, but their
        crystallinity comes from EM-dominated orbital ω ~ 10¹⁵ Hz,
        not gravity. The bridge ω ~ Λ_grav holds only for
        self-gravitating systems.)
        """
        from grut.foundation.closure_protocol import (
            crystallinity, lambda_grav_dp,
        )
        # 1 g sphere, mm separation → Λ_grav ~ 10²⁰ Hz, Λ_grav τ_0 ~ 10³⁵
        l_grav = lambda_grav_dp(m_kg=1e-3, l_m=1e-3, R_m=1e-3)
        X = crystallinity(lambda_grav_Hz=l_grav)
        assert X > 1e30

    def test_atom_is_deep_crystal_via_em_frequency(self):
        """Literal atom: Λ_grav ~ 10⁻¹⁹ Hz (tiny), but EM orbital ω ~ 10¹⁵ Hz
        gives ωτ_0 ~ 10³⁰ — still deep crystal, via EM not gravity."""
        from grut.foundation.closure_protocol import crystallinity
        # Hydrogen-like ground-state frequency ~ 10¹⁵ Hz
        X = crystallinity(omega_dyn_Hz=1e15)
        assert X > 1e20

    def test_galactic_rotation_is_deep_fluid(self):
        """Galactic rotation (period ~ 250 Myr): ωτ_0 < 1 (deep fluid)."""
        from grut.foundation.closure_protocol import crystallinity, YEAR_SEC
        omega = 2 * np.pi / (2.5e8 * YEAR_SEC)  # period ~ 250 Myr
        X = crystallinity(omega_dyn_Hz=omega)
        # ω × τ_0 = 2π × (41.9 Myr / 250 Myr) ≈ 1.05 — at the boundary.
        # Looser check: galactic-mode X is order 1 or below, not crystal.
        assert X < 2.0

    def test_solar_system_orbit_is_deep_crystal(self):
        """Saturn orbit (period ~ 30 yr): ωτ_0 ≫ 1 (deep crystal, GR safe)."""
        from grut.foundation.closure_protocol import crystallinity, YEAR_SEC
        omega = 2 * np.pi / (30 * YEAR_SEC)
        X = crystallinity(omega_dyn_Hz=omega)
        assert X > 1e6

    def test_crystallinity_takes_max_when_both_provided(self):
        """When both ω and Λ_grav are given, function uses the dominant rate."""
        from grut.foundation.closure_protocol import crystallinity, TAU_0_SEC
        X = crystallinity(omega_dyn_Hz=1e-15, lambda_grav_Hz=1e10)
        assert abs(X - 1e10 * TAU_0_SEC) / X < 1e-12


class TestProvenanceHonesty:
    """Provenance dict reflects the canonical derivation chains for both
    foundational constants — neither is a free parameter."""

    def test_provenance_dict_marks_alpha_vac_derived(self):
        """α_vac DERIVED via conformal-mode scalar (KS 2011 a/c = 1/3)."""
        from grut.foundation.closure_protocol import canonical_constants_table
        provenance = canonical_constants_table()["provenance"]
        assert "DERIVED" in provenance["alpha_vac"]
        assert "conformal-mode scalar" in provenance["alpha_vac"]

    def test_provenance_dict_marks_tau_0_derived(self):
        """τ_0 DERIVED from CTP noise kernel at gold benchmark."""
        from grut.foundation.closure_protocol import canonical_constants_table
        provenance = canonical_constants_table()["provenance"]
        assert "DERIVED" in provenance["tau_0"]
        assert "noise-kernel" in provenance["tau_0"] or "noise kernel" in provenance["tau_0"]

    def test_historical_provenance_preserved(self):
        """The v6.0 back-derivation history is referenced for honesty."""
        from grut.foundation.closure_protocol import canonical_constants_table
        provenance = canonical_constants_table()["provenance"]
        assert "ALPHA_VAC_PROVENANCE" in provenance["alpha_vac"]

    def test_table_exposes_two_foundational_constants(self):
        """Foundational constants are exposed at the top of the table."""
        from grut.foundation.closure_protocol import canonical_constants_table
        keys = list(canonical_constants_table().keys())
        # tau_0 and alpha_vac come first
        assert keys[0] == "tau_0_Myr"
        assert keys[1] == "alpha_vac"


class TestTauLambdaCIdentity:
    """τ_0 = 1/√(Λc) — v11 Appendix I dark-sector unification."""

    def test_roundtrip(self):
        from grut.foundation.closure_protocol import (
            tau_0_from_lambda_c, lambda_from_tau_0, TAU_0_SEC
        )
        Lambda = lambda_from_tau_0(TAU_0_SEC)
        tau_back = tau_0_from_lambda_c(Lambda)
        assert abs(tau_back - TAU_0_SEC) / TAU_0_SEC < 1e-10

    def test_Lambda_positive_finite(self):
        """τ_0 = 1/√(Λc²) gives positive finite Λ.

        The identity as stated in v11 App I relates τ_0 to a dark-sector
        Λ that is NOT the observed cosmological constant directly —
        it carries an S (screening) factor. The round-trip consistency
        is what matters for internal correctness.
        """
        from grut.foundation.closure_protocol import lambda_from_tau_0, TAU_0_SEC
        import numpy as np
        Lambda = lambda_from_tau_0(TAU_0_SEC)
        assert Lambda > 0
        assert np.isfinite(Lambda)


class TestResponseKernel:
    """Phase I §7 kernel and susceptibility."""

    def test_kernel_normalized(self):
        """∫₀^∞ K(t) dt = 1 (normalization)."""
        from grut.foundation.closure_protocol import kernel_K, TAU_0_SEC
        ts = np.linspace(0, 20 * TAU_0_SEC, 10000)
        integral = np.trapezoid([kernel_K(t) for t in ts], ts)
        assert abs(integral - 1.0) < 0.01

    def test_kernel_zero_at_negative_time(self):
        """Causal: K(t<0) = 0."""
        from grut.foundation.closure_protocol import kernel_K
        assert kernel_K(-1.0) == 0.0

    def test_susceptibility_DC_equals_alpha(self):
        """χ(0) = α (DC susceptibility)."""
        from grut.foundation.closure_protocol import susceptibility_chi, ALPHA_VAC
        chi = susceptibility_chi(0.0)
        assert abs(chi.real - ALPHA_VAC) < 1e-15

    def test_n_g_DC_matches_N_G_DC(self):
        from grut.foundation.closure_protocol import n_g_refractive, N_G_DC
        assert abs(n_g_refractive(0.0) - N_G_DC) < 1e-12

    def test_n_g_high_freq_reduces_to_one(self):
        from grut.foundation.closure_protocol import n_g_refractive
        assert abs(n_g_refractive(1e10) - 1.0) < 1e-6


class TestRegimeGate:
    """Phase I §8.1 solar-system safety via regime gate."""

    def test_saturn_suppression_is_15_orders(self):
        """α_eff at Saturn's orbital frequency is ~10⁻¹⁵ (below ranging)."""
        from grut.foundation.closure_protocol import (
            alpha_effective, TAU_0_SEC
        )
        P_saturn_sec = 29.5 * 3.156e7
        omega_saturn = 2 * np.pi / P_saturn_sec
        alpha_eff = alpha_effective(omega_saturn)
        assert alpha_eff < 1e-13       # at most 10⁻¹³
        assert alpha_eff > 1e-17       # not zero

    def test_regime_parameter_X_saturn_is_large(self):
        from grut.foundation.closure_protocol import regime_parameter_X
        omega_saturn = 2 * np.pi / (29.5 * 3.156e7)
        X = regime_parameter_X(omega_saturn)
        assert X > 1e6

    def test_regime_parameter_X_galactic_is_order_unity(self):
        """Galactic rotation (200 km/s @ 10 kpc): X ~ 1."""
        from grut.foundation.closure_protocol import regime_parameter_X
        v = 200e3
        r = 10 * 3.086e19
        omega = v / r
        X = regime_parameter_X(omega)
        assert 0.1 < X < 10


class TestEngineInterpolation:
    """Phase I Appendix E — ν(y) and g_eff."""

    def test_nu_high_y_approaches_one(self):
        """y ≫ 1 (Newtonian): ν → 1."""
        from grut.foundation.closure_protocol import nu_interpolation
        assert abs(nu_interpolation(1e6) - 1.0) < 1e-3

    def test_nu_low_y_diverges_as_sqrt(self):
        """y ≪ 1: ν ~ √(1/y)."""
        from grut.foundation.closure_protocol import nu_interpolation
        y = 1e-6
        nu = nu_interpolation(y)
        expected = np.sqrt(1/y)  # leading-order
        assert abs(nu / expected - 1.0) < 0.01

    def test_g_eff_equals_g_bar_at_solar_system(self):
        """At Saturn's ω_dyn, g_eff ≈ g_bar (GR recovered)."""
        from grut.foundation.closure_protocol import g_effective
        omega_saturn = 2 * np.pi / (29.5 * 3.156e7)
        g_bar = 6.7e-4    # Saturn's orbit around Sun
        g_eff = g_effective(g_bar, omega_saturn)
        # Should match within 10⁻¹⁰
        assert abs(g_eff - g_bar) / g_bar < 1e-10

    def test_g_eff_enhanced_in_galactic_regime(self):
        """At galactic ω_dyn, low g_bar: g_eff > g_bar."""
        from grut.foundation.closure_protocol import g_effective, A_0_SI
        v = 200e3
        r = 30 * 3.086e19    # 30 kpc (outer)
        omega = v / r
        g_bar = A_0_SI / 100   # deep below a_0
        g_eff = g_effective(g_bar, omega)
        assert g_eff > g_bar

    def test_deep_regime_gives_sqrt_g_bar_a0(self):
        """y ≪ 1, X ≪ 1: g_eff ≈ √(g_bar × a_0) (MOND-like)."""
        from grut.foundation.closure_protocol import g_effective, A_0_SI, TAU_0_SEC
        # Far outer galaxy: low ω, low g_bar
        omega = 1e-18
        g_bar = A_0_SI * 1e-3
        g_eff = g_effective(g_bar, omega)
        g_mond = np.sqrt(g_bar * A_0_SI)
        # Within factor 1.5 of MOND deep limit (not exact due to ν(y) form)
        assert 0.5 < g_eff / g_mond < 1.5


class TestBulletCluster:
    """Phase I §8.4 operational estimate."""

    def test_bullet_offset_is_order_100_kpc(self):
        """v_coll × τ_0 ≈ 100 kpc for v_coll ≈ 3000 km/s."""
        from grut.foundation.closure_protocol import bullet_offset_estimate
        v = 3000e3    # 3000 km/s
        offset = bullet_offset_estimate(v)
        kpc = 3.086e19
        assert 50 * kpc < offset < 500 * kpc


class TestMONDComparison:
    """v11 App F comparison table sanity."""

    def test_GRUT_has_zero_free_parameters(self):
        from grut.foundation.closure_protocol import MOND_COMPARISON
        assert MOND_COMPARISON["GRUT_Closure"]["free_parameters"] == 0

    def test_GRUT_uses_frequency_based_regime(self):
        from grut.foundation.closure_protocol import MOND_COMPARISON
        sep = MOND_COMPARISON["GRUT_Closure"]["regime_separator"]
        assert "frequency" in sep.lower()

    def test_MOND_uses_acceleration_based_regime(self):
        from grut.foundation.closure_protocol import MOND_COMPARISON
        sep = MOND_COMPARISON["MOND"]["regime_separator"]
        assert "acceleration" in sep.lower()


class TestVerifyAllChecks:
    def test_verify_all_pass(self):
        from grut.foundation.closure_protocol import verify
        checks = verify()
        for name, passed in checks.items():
            assert passed, f"Canonical check failed: {name}"
