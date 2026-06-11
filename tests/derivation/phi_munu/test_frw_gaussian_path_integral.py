"""Tests for Phase 2D — FRW Gaussian path integral derivation of G^R.

Verifies:
  - QSA action terms (gradient kinetic, relaxation mass, matter coupling)
  - Quadratic kernel structure K = (a⁴/2)(1+(τ₀k_phys)²)
  - a(η)-cancellation in Gaussian integration
  - G^R = 1/(1+(τ₀k_phys)²) — no a(η) corrections
  - Agreement with Correction #25 WKB result
  - Coupling vertex = −α_vac = −1/3
  - μ_GRUT from path integral result
  - Beyond-QSA correction is negligible

Pattern matches tests/derivation/phi_munu/test_frw_explicit.py.
"""

from __future__ import annotations

from fractions import Fraction

import sympy as sp


# ─────────────────────────────────────────────────────────────────────
# Module imports & verify()
# ─────────────────────────────────────────────────────────────────────


class TestModuleImports:
    def test_module_importable(self):
        from grut.derivation.phi_munu import frw_gaussian_path_integral  # noqa
        assert hasattr(frw_gaussian_path_integral, "verify")

    def test_key_functions_present(self):
        from grut.derivation.phi_munu.frw_gaussian_path_integral import (
            quadratic_kernel,
            quadratic_kernel_factored,
            G_R_qsa,
            G_R_agrees_with_wkb,
            a_cancellation_check,
            coupling_vertex,
            mu_GRUT_from_path_integral,
            convention_declaration,
            verify,
        )
        assert all([
            quadratic_kernel, quadratic_kernel_factored, G_R_qsa,
            G_R_agrees_with_wkb, a_cancellation_check, coupling_vertex,
            mu_GRUT_from_path_integral, convention_declaration, verify,
        ])


class TestVerifyPassesAllLegs:
    def test_verify_returns_dict(self):
        from grut.derivation.phi_munu.frw_gaussian_path_integral import verify
        result = verify()
        assert isinstance(result, dict)
        assert len(result) == 10

    def test_all_legs_pass(self):
        from grut.derivation.phi_munu.frw_gaussian_path_integral import verify
        result = verify()
        failed = [k for k, v in result.items() if not v]
        assert failed == [], f"Failed legs: {failed}"


# ─────────────────────────────────────────────────────────────────────
# Section 1 — QSA action terms
# ─────────────────────────────────────────────────────────────────────


class TestQSAActionTerms:
    def test_gradient_kinetic_has_a_squared(self):
        """Gradient kinetic term scales as a² (not a⁴)."""
        import sympy as sp
        from grut.derivation.phi_munu.frw_gaussian_path_integral import (
            s_gradient_kinetic_per_mode, A, K_COMOVING, TAU_0,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0
        term = s_gradient_kinetic_per_mode(K_COMOVING, A, TAU_0)
        # Must contain A**2 (not A**4)
        expanded = sp.expand(term)
        assert sp.degree(expanded, A) == 2

    def test_relaxation_mass_has_a_fourth(self):
        """Relaxation mass term scales as a⁴."""
        import sympy as sp
        from grut.derivation.phi_munu.frw_gaussian_path_integral import (
            s_relaxation_mass_per_mode, A,
        )
        term = s_relaxation_mass_per_mode(A)
        expanded = sp.expand(term)
        assert sp.degree(expanded, A) == 4

    def test_coupling_source_has_a_fourth(self):
        """Matter coupling source scales as a⁴ — same as kernel."""
        import sympy as sp
        from grut.derivation.phi_munu.frw_gaussian_path_integral import (
            coupling_source_per_mode, A,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import ALPHA
        source = coupling_source_per_mode(A, ALPHA)
        expanded = sp.expand(source)
        assert sp.degree(expanded, A) == 4

    def test_coupling_vertex_equals_minus_alpha(self):
        """Coupling vertex ∂²S_IF/∂σ_a∂δρ_m = −α_vac; α_vac = 1/3."""
        from grut.derivation.phi_munu.frw_gaussian_path_integral import coupling_vertex
        from grut.derivation.phi_munu.linearized_ctp_action import (
            ALPHA, alpha_vac_from_conformal_mode,
        )
        vertex = coupling_vertex(ALPHA)
        # Symbolic equality: vertex = −α_vac symbol
        assert vertex == -ALPHA
        # Numerical value: α_vac = 1/3
        alpha_val = alpha_vac_from_conformal_mode()  # Fraction(1, 3)
        assert alpha_val.numerator == 1
        assert alpha_val.denominator == 3


# ─────────────────────────────────────────────────────────────────────
# Section 2 — Quadratic kernel
# ─────────────────────────────────────────────────────────────────────


class TestQuadraticKernel:
    def test_kernel_factored_form(self):
        """K = (a⁴/2)(1+(τ₀k_phys)²) in factored form."""
        import sympy as sp
        from grut.derivation.phi_munu.frw_gaussian_path_integral import (
            quadratic_kernel_factored, A, K_COMOVING,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0
        K = quadratic_kernel_factored(K_COMOVING, A, TAU_0)
        expected = sp.Rational(1, 2) * A**4 * (1 + TAU_0**2 * (K_COMOVING / A)**2)
        assert sp.simplify(K - expected) == 0

    def test_kernel_unfactored_equals_factored(self):
        """Unfactored kernel equals factored kernel (algebraic consistency)."""
        import sympy as sp
        from grut.derivation.phi_munu.frw_gaussian_path_integral import (
            quadratic_kernel, quadratic_kernel_factored, A, K_COMOVING,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0
        K_unfact = quadratic_kernel(K_COMOVING, A, TAU_0)
        K_fact = quadratic_kernel_factored(K_COMOVING, A, TAU_0)
        diff = sp.simplify(sp.expand(K_unfact) - sp.expand(K_fact))
        assert diff == 0

    def test_kernel_a_fourth_at_k_zero(self):
        """At k=0 (DC limit), kernel reduces to a⁴/2."""
        import sympy as sp
        from grut.derivation.phi_munu.frw_gaussian_path_integral import (
            quadratic_kernel_factored, A,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0
        K_at_k0 = sp.limit(
            quadratic_kernel_factored(sp.Symbol("k", positive=True), A, TAU_0),
            sp.Symbol("k", positive=True), 0,
        )
        assert sp.simplify(K_at_k0 - A**4 / 2) == 0


# ─────────────────────────────────────────────────────────────────────
# Section 3 — Gaussian integration and a-cancellation
# ─────────────────────────────────────────────────────────────────────


class TestGaussianIntegration:
    def test_a_cancels_in_kphys_coordinates(self):
        """The a⁴ factor cancels when action is written in physical-wavenumber coordinates.

        Source = a⁴ α_vac, kernel = a⁴(1+(τ₀k_phys)²) → ratio is a-independent.
        This is the key structural result: G^R depends on k_phys ONLY.
        """
        from grut.derivation.phi_munu.frw_gaussian_path_integral import (
            a_cancellation_check, K_PHYS,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0, ALPHA
        result = a_cancellation_check(K_PHYS, TAU_0, ALPHA)
        assert result["a_cancels_exactly"], (
            "a⁴ does NOT cancel in the Gaussian integration. "
            "G^R would have a(η)-dependent corrections."
        )
        assert result["ratio_equals_alpha_GR"], (
            "ratio (source/kernel) does not equal α_vac × G^R"
        )

    def test_on_shell_sigma_form_in_kphys(self):
        """σ_a^{on-shell}/δρ_m = α_vac × G^R = α_vac/(1+(τ₀k_phys)²)."""
        import sympy as sp
        from grut.derivation.phi_munu.frw_gaussian_path_integral import (
            a_cancellation_check, K_PHYS,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0, ALPHA
        result = a_cancellation_check(K_PHYS, TAU_0, ALPHA)
        expected = ALPHA / (1 + TAU_0**2 * K_PHYS**2)
        assert sp.simplify(result["ratio_in_kphys"] - expected) == 0

    def test_on_shell_sigma_a_independent_in_kphys(self):
        """σ_a^{on-shell}/δρ_m is independent of a when expressed in k_phys."""
        from grut.derivation.phi_munu.frw_gaussian_path_integral import (
            a_cancellation_check, K_PHYS,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0, ALPHA
        result = a_cancellation_check(K_PHYS, TAU_0, ALPHA)
        assert result["a_cancels_exactly"], (
            f"σ_a^{{on-shell}} has a-dependent correction: "
            f"{result['d_ratio_da_sym']}"
        )


# ─────────────────────────────────────────────────────────────────────
# Section 4 — G^R structure
# ─────────────────────────────────────────────────────────────────────


class TestRetardedGreenFunction:
    def test_G_R_form(self):
        """G^R(k_phys) = 1/(1+(τ₀k_phys)²)."""
        import sympy as sp
        from grut.derivation.phi_munu.frw_gaussian_path_integral import (
            G_R_qsa, K_PHYS,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0
        g_r = G_R_qsa(K_PHYS, TAU_0)
        expected = 1 / (1 + TAU_0**2 * K_PHYS**2)
        assert sp.simplify(g_r - expected) == 0

    def test_G_R_agrees_with_phase2C_WKB(self):
        """G^R from path integral matches χ_FRW^WKB from Phase 2C."""
        from grut.derivation.phi_munu.frw_gaussian_path_integral import (
            G_R_agrees_with_wkb, K_PHYS,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0
        assert G_R_agrees_with_wkb(K_PHYS, TAU_0)

    def test_G_R_sub_horizon_limit(self):
        """Sub-horizon limit: k_phys → ∞, G^R → 0 (GR recovery)."""
        import sympy as sp
        from grut.derivation.phi_munu.frw_gaussian_path_integral import G_R_qsa
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0
        k = sp.Symbol("k", positive=True)
        lim = sp.limit(G_R_qsa(k, TAU_0), k, sp.oo)
        assert lim == 0

    def test_G_R_super_horizon_limit(self):
        """Super-horizon limit: k_phys → 0, G^R → 1 (full constitutive)."""
        import sympy as sp
        from grut.derivation.phi_munu.frw_gaussian_path_integral import G_R_qsa
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0
        k = sp.Symbol("k", positive=True)
        lim = sp.limit(G_R_qsa(k, TAU_0), k, 0)
        assert lim == 1

    def test_G_R_transition_scale(self):
        """At k_phys = 1/τ₀, G^R = 1/2."""
        import sympy as sp
        from grut.derivation.phi_munu.frw_gaussian_path_integral import G_R_qsa
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0
        g_r_at_transition = G_R_qsa(1 / TAU_0, TAU_0)
        assert sp.simplify(g_r_at_transition - sp.Rational(1, 2)) == 0

    def test_beyond_qsa_correction_negligible(self):
        """Beyond-QSA correction O((τ₀H)²) is < 10⁻⁴ today."""
        from grut.derivation.phi_munu.frw_gaussian_path_integral import (
            beyond_qsa_correction_estimate,
        )
        result = beyond_qsa_correction_estimate()
        assert result["beyond_qsa_negligible"], (
            f"Beyond-QSA correction = {result['(tau_0_H_0)_squared']:.2e} — "
            f"not negligible!"
        )


# ─────────────────────────────────────────────────────────────────────
# Section 5 — Modified Poisson equation
# ─────────────────────────────────────────────────────────────────────


class TestModifiedPoisson:
    def test_mu_GRUT_sub_hubble(self):
        """μ_GRUT = 1 + α_vac/(1+(τ₀k_phys)²) in sub-Hubble limit."""
        import sympy as sp
        from grut.derivation.phi_munu.frw_gaussian_path_integral import (
            mu_GRUT_from_path_integral, K_PHYS,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0, ALPHA
        mu = mu_GRUT_from_path_integral(K_PHYS, TAU_0, ALPHA)
        expected = 1 + ALPHA / (1 + TAU_0**2 * K_PHYS**2)
        assert sp.simplify(mu - expected) == 0

    def test_mu_GRUT_sub_horizon_is_one(self):
        """μ_GRUT → 1 as k_phys → ∞ (GR recovery)."""
        import sympy as sp
        from grut.derivation.phi_munu.frw_gaussian_path_integral import (
            mu_GRUT_from_path_integral,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0, ALPHA
        k = sp.Symbol("k", positive=True)
        mu_high_k = sp.limit(
            mu_GRUT_from_path_integral(k, TAU_0, ALPHA), k, sp.oo,
        )
        assert mu_high_k == 1

    def test_mu_GRUT_super_horizon_is_one_plus_alpha(self):
        """μ_GRUT → 1 + α_vac as k_phys → 0 (full constitutive; = 4/3 numerically)."""
        import sympy as sp
        from grut.derivation.phi_munu.frw_gaussian_path_integral import (
            mu_GRUT_from_path_integral,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import (
            TAU_0, ALPHA, alpha_vac_from_conformal_mode,
        )
        k = sp.Symbol("k", positive=True)
        mu_low_k = sp.limit(
            mu_GRUT_from_path_integral(k, TAU_0, ALPHA), k, 0,
        )
        # Symbolic: μ → 1 + α_vac
        assert sp.simplify(mu_low_k - (1 + ALPHA)) == 0
        # Numerical: α_vac = 1/3 → μ = 4/3
        alpha_frac = alpha_vac_from_conformal_mode()  # Fraction(1, 3)
        mu_numeric = float(mu_low_k.subs(ALPHA, float(alpha_frac)))
        assert abs(mu_numeric - 4.0 / 3.0) < 1e-12

    def test_modified_poisson_structure(self):
        """modified_poisson_from_path_integral returns expected keys."""
        from grut.derivation.phi_munu.frw_gaussian_path_integral import (
            modified_poisson_from_path_integral, K_PHYS,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0, ALPHA
        result = modified_poisson_from_path_integral(K_PHYS, TAU_0, ALPHA)
        assert set(result.keys()) == {
            "G_R", "coupling_vertex", "mu_GRUT", "poisson_rhs_form", "sigma_a_on_shell"
        }
        # coupling vertex = −α_vac (symbolically)
        assert result["coupling_vertex"] == -ALPHA


# ─────────────────────────────────────────────────────────────────────
# Section 6 — Conventions and gap-closure claims
# ─────────────────────────────────────────────────────────────────────


class TestConventionDeclaration:
    def test_convention_declaration_complete(self):
        """All Phase 2D conventions declared."""
        from grut.derivation.phi_munu.frw_gaussian_path_integral import (
            convention_declaration,
        )
        conv = convention_declaration()
        required = [
            "C1d_FRW_metric", "C2d_fourier", "C3d_k_phys",
            "C4d_qsa_regime", "C5d_minimal_coupling",
            "C6d_alpha_vac", "C7d_cdm_coupling", "phase_2D_status",
        ]
        missing = [k for k in required if k not in conv]
        assert missing == [], f"Missing conventions: {missing}"

    def test_phase_2D_status_mentions_gap_closure(self):
        """Phase 2D status string references the gap registry entry."""
        from grut.derivation.phi_munu.frw_gaussian_path_integral import (
            convention_declaration,
        )
        status = convention_declaration()["phase_2D_status"]
        assert "constitutive_growth_poisson_closure_gap" in status
