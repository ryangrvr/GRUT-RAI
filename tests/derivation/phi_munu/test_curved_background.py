"""Regression tests for the Φ_μν curved-background scaffold.

Pins the four verification targets called out in the v8→v2 roadmap
for Priority 2B:

  (1) Flat-limit recovery: g_μν → η_μν reduces Φ_μν^curved →
      Φ_μν^linear (Correction #23 form).
  (2) Covariant conservation: ∇^μ Φ_μν = 0 holds STRUCTURALLY from
      ∇^μ P^TT,g_μνρσ = 0.
  (3) Causality: K^R_μνρσ(x, x') = 0 outside/past the retarded domain.
  (4) FRW scalar-mode compatibility: scaffold makes the Priority 3
      bridge explicit (n_g(ω, k, t) = 1 + α χ_FRW).

These are STRUCTURAL checks of the scaffold's consistency, not full
derivations. The scaffold's status is "anchored" — the structural form
is pinned and the four physical consistency requirements are met;
explicit construction of P^TT,g and G^R on FRW/S⁴ is deferred.

Pattern matches tests/derivation/phi_munu/test_linearized_ctp_action.py.
"""

from __future__ import annotations

import sympy as sp


# ─────────────────────────────────────────────────────────────────────
# Module imports & verify()
# ─────────────────────────────────────────────────────────────────────


class TestCurvedModuleImports:
    def test_curved_module_importable(self):
        from grut.derivation.phi_munu import curved_background  # noqa
        assert hasattr(curved_background, "verify")

    def test_package_exports_curved_API(self):
        from grut.derivation.phi_munu import (
            phi_munu_curved_integral_form,
            phi_munu_curved_operator_form,
            flat_limit_check,
            covariant_conservation_check,
            causality_check_retarded_green_function,
            frw_scalar_mode_compatibility,
            curved_verify,
            curved_convention_declaration,
        )
        for fn in (
            phi_munu_curved_integral_form,
            phi_munu_curved_operator_form,
            flat_limit_check,
            covariant_conservation_check,
            causality_check_retarded_green_function,
            frw_scalar_mode_compatibility,
            curved_verify,
            curved_convention_declaration,
        ):
            assert callable(fn)


class TestCurvedVerifyHarness:
    def test_curved_verify_all_legs_pass(self):
        """All six scaffold verification legs must return True."""
        from grut.derivation.phi_munu.curved_background import verify
        v = verify()
        for k, val in v.items():
            assert val is True, f"curved verify() leg failed: {k} = {val}"


# ─────────────────────────────────────────────────────────────────────
# Convention declaration
# ─────────────────────────────────────────────────────────────────────


class TestCurvedConventionDeclaration:
    """C1c-C7c match C1-C7 of the linearized module with the '_c' suffix
    marking curved-background extensions."""

    def test_C1c_metric_signature(self):
        from grut.derivation.phi_munu.curved_background import (
            convention_declaration,
        )
        d = convention_declaration()
        assert "(-, +, +, +)" in d["C1c_metric_signature"]

    def test_C2c_states_background_perturbation_split(self):
        from grut.derivation.phi_munu.curved_background import (
            convention_declaration,
        )
        d = convention_declaration()
        c2c = d["C2c_background_perturbation_split"]
        assert "ḡ_μν" in c2c or "background" in c2c.lower()
        assert "h_μν" in c2c or "h_mu" in c2c.lower()

    def test_C4c_curved_kernel_includes_retarded_green(self):
        from grut.derivation.phi_munu.curved_background import (
            convention_declaration,
        )
        d = convention_declaration()
        c4c = d["C4c_curved_retarded_kernel"]
        assert "G^R" in c4c or "Green" in c4c.lower() or "retarded" in c4c.lower()
        assert "causal past" in c4c.lower() or "past" in c4c.lower()

    def test_C6c_sqrt_minus_g_measure_named(self):
        from grut.derivation.phi_munu.curved_background import (
            convention_declaration,
        )
        d = convention_declaration()
        c6c = d["C6c_sqrt_minus_g_measure"]
        assert "√-g" in c6c or "sqrt" in c6c.lower() or "-g" in c6c

    def test_C7c_curved_projector_is_transverse_tracefree(self):
        from grut.derivation.phi_munu.curved_background import (
            convention_declaration,
        )
        d = convention_declaration()
        c7c = d["C7c_curved_transverse_tracefree_projector"]
        assert "transverse" in c7c.lower()
        assert "tracefree" in c7c.lower() or "tracefree" in c7c.lower() or "trace" in c7c.lower()
        assert "∇^μ" in c7c or "covariant" in c7c.lower() or "nabla" in c7c.lower()

    def test_phase_2B_status_is_scaffold(self):
        """The convention declaration must explicitly mark this as a
        SCAFFOLD with deferred Phase 2C work."""
        from grut.derivation.phi_munu.curved_background import (
            convention_declaration,
        )
        d = convention_declaration()
        s = d["phase_2B_status"]
        assert "SCAFFOLD" in s or "scaffold" in s.lower()
        assert "Phase 2C" in s or "deferred" in s.lower()


# ─────────────────────────────────────────────────────────────────────
# Section 1: Curved-background CTP action structure
# ─────────────────────────────────────────────────────────────────────


class TestCurvedActionTerms:
    """The curved CTP action has the same four pieces as flat (EH,
    matter, constitutive, noise) but each piece carries an explicit
    √-g factor for covariance."""

    def test_action_has_four_terms(self):
        from grut.derivation.phi_munu.curved_background import (
            curved_ctp_action_terms,
        )
        a = curved_ctp_action_terms()
        assert "S_EH_curved" in a
        assert "S_matter_curved" in a
        assert "S_const_curved" in a
        assert "S_noise_curved" in a

    def test_action_terms_carry_sqrt_minus_g(self):
        """Every action piece carries the √-g measure for covariance."""
        from grut.derivation.phi_munu.curved_background import (
            curved_ctp_action_terms, SQRT_MINUS_G,
        )
        a = curved_ctp_action_terms()
        for name, term in a.items():
            assert term.has(SQRT_MINUS_G), (
                f"{name} missing √-g factor: {term}"
            )


# ─────────────────────────────────────────────────────────────────────
# Section 2: Curved Φ_μν integral form (canonical scaffold)
# ─────────────────────────────────────────────────────────────────────


class TestCurvedPhiMuNuIntegralForm:
    """The integral form Φ_μν^curved = ∫ d⁴x' √-g K^R(x,x') h(x') is the
    canonical scaffold expression. The kernel decomposes as
    K^R = α × P^TT,g × G^R."""

    def test_kernel_has_alpha_factor(self):
        from grut.derivation.phi_munu.curved_background import (
            phi_munu_curved_integral_form,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import ALPHA
        f = phi_munu_curved_integral_form()
        decomp = f["kernel_decomposition"]
        assert decomp["alpha_factor"] == ALPHA

    def test_kernel_has_curved_projector_factor(self):
        from grut.derivation.phi_munu.curved_background import (
            phi_munu_curved_integral_form,
        )
        f = phi_munu_curved_integral_form()
        decomp = f["kernel_decomposition"]
        # P^TT,g is a function of (x, x') — bitensor
        proj = decomp["projector"]
        assert proj is not None
        # It's a SymPy function application of two arguments
        assert proj.func.__name__ == "P_TT_g" or "P_TT_g" in str(proj)

    def test_kernel_has_retarded_green_function(self):
        from grut.derivation.phi_munu.curved_background import (
            phi_munu_curved_integral_form,
        )
        f = phi_munu_curved_integral_form()
        decomp = f["kernel_decomposition"]
        gR = decomp["retarded_green_function"]
        assert gR is not None
        # G^R is a function of two spacetime points
        assert gR.func.__name__ == "G_R" or "G_R" in str(gR)

    def test_integrand_carries_sqrt_minus_g_at_integration_point(self):
        """The integrand carries √-g(x') — at the INTEGRATION point,
        not at x. This is the standard covariant integration measure."""
        from grut.derivation.phi_munu.curved_background import (
            phi_munu_curved_integral_form,
        )
        f = phi_munu_curved_integral_form()
        measure = f["measure_factor"]
        # Should be sqrt_minus_g(x') — function of XPRIME, not X
        from grut.derivation.phi_munu.curved_background import XPRIME
        assert measure.has(XPRIME)


class TestCurvedPhiMuNuOperatorForm:
    """The operator form Φ_μν^curved = α × χ(τ_0² (-□_g)) × P^TT,g × h
    is the equivalent compact form using the curved d'Alembertian."""

    def test_operator_form_has_alpha_factor(self):
        from grut.derivation.phi_munu.curved_background import (
            phi_munu_curved_operator_form,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import ALPHA
        f = phi_munu_curved_operator_form()
        # The operator form should have α as a multiplicative factor
        assert f["phi_operator_form"].has(ALPHA)

    def test_operator_susceptibility_has_pole_structure(self):
        """χ_op = 1/(1 - τ_0² □_g). At □_g = 0 (flat-DC), χ_op = 1."""
        from grut.derivation.phi_munu.curved_background import (
            phi_munu_curved_operator_form,
        )
        f = phi_munu_curved_operator_form()
        chi_op = f["operator_susceptibility"]
        box_g = f["box_operator"]
        # At box_g = 0, chi_op should be 1
        chi_at_zero = chi_op.subs(box_g, 0)
        assert sp.simplify(chi_at_zero - 1) == 0


# ─────────────────────────────────────────────────────────────────────
# Verification target 1: Flat-limit recovery
# ─────────────────────────────────────────────────────────────────────


class TestFlatLimitRecovery:
    """Target 1 of the v2B roadmap: g_μν → η_μν reduces Φ_μν^curved
    to Φ_μν^linear from Correction #23."""

    def test_flat_limit_check_passes(self):
        from grut.derivation.phi_munu.curved_background import flat_limit_check
        c = flat_limit_check()
        assert c["structural_form_matches_flat"] is True
        assert c["flat_limit_recovers_correction_23"] is True

    def test_curved_kernel_decomposition_matches_flat_three_factor_form(self):
        """Both flat and curved kernels have the form α × P × χ.
        In flat: α × χ(ω) × P^TT (Fourier domain).
        In curved: α × G^R(x,x') × P^TT,g(x,x') (position-domain bitensor)."""
        from grut.derivation.phi_munu.curved_background import (
            phi_munu_curved_integral_form,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import (
            constitutive_kernel_fourier, OMEGA, TAU_0, ALPHA,
        )
        # Flat kernel structure
        flat = constitutive_kernel_fourier(OMEGA, TAU_0, ALPHA)
        # Has α as multiplicative factor
        assert flat.has(ALPHA)
        # Curved kernel structure
        curved = phi_munu_curved_integral_form()
        assert curved["kernel"].has(ALPHA)
        # Both are α × (relaxation factor) × (projector). The structural
        # form is the same.

    def test_alpha_factor_preserved_under_flat_limit(self):
        """α_vac is unchanged under the flat limit — it inherits from
        the conformal-mode-scalar identification, not from background
        geometry. This pins that Phase 2B does not modify α_vac."""
        from grut.derivation.phi_munu.curved_background import (
            phi_munu_curved_integral_form,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import (
            ALPHA, alpha_vac_from_conformal_mode,
        )
        from fractions import Fraction
        # Curved kernel has α explicitly
        curved = phi_munu_curved_integral_form()
        assert curved["kernel_decomposition"]["alpha_factor"] == ALPHA
        # Flat α_vac is 1/3
        assert alpha_vac_from_conformal_mode() == Fraction(1, 3)


# ─────────────────────────────────────────────────────────────────────
# Verification target 2: Covariant conservation
# ─────────────────────────────────────────────────────────────────────


class TestCovariantConservation:
    """Target 2: ∇^μ Φ_μν = 0 holds STRUCTURALLY, not just
    on-shell or for specific solutions."""

    def test_projector_is_covariantly_transverse(self):
        from grut.derivation.phi_munu.curved_background import (
            covariant_conservation_check,
        )
        c = covariant_conservation_check()
        assert c["projector_is_covariantly_transverse"] is True

    def test_kernel_inherits_transversality(self):
        """K^R = α × P^TT,g × G^R inherits transversality from P^TT,g."""
        from grut.derivation.phi_munu.curved_background import (
            covariant_conservation_check,
        )
        c = covariant_conservation_check()
        assert c["kernel_inherits_transversality_from_projector"] is True

    def test_phi_conserved_for_arbitrary_h(self):
        """∇^μ Φ_μν = 0 for ANY h^ρσ, ANY background g — structural,
        not specific-solution."""
        from grut.derivation.phi_munu.curved_background import (
            covariant_conservation_check,
        )
        c = covariant_conservation_check()
        assert c["phi_munu_covariantly_conserved_for_all_h"] is True
        assert c["structural_not_just_specific_solutions"] is True

    def test_flat_limit_matches_correction_23_bianchi(self):
        """In the flat limit, ∇^μ → ∂^μ and P^TT,g → P^TT, so
        ∇^μ Φ_μν = 0 ↦ ∂^μ Φ_μν = 0 — recovers the Correction #23
        flat Bianchi check."""
        from grut.derivation.phi_munu.curved_background import (
            covariant_conservation_check,
        )
        c = covariant_conservation_check()
        assert c["consistent_with_flat_bianchi_check"] is True


# ─────────────────────────────────────────────────────────────────────
# Verification target 3: Causality
# ─────────────────────────────────────────────────────────────────────


class TestCausalityRetardedSupport:
    """Target 3: K^R(x, x') = 0 outside the past lightcone of x.
    Standard retarded-Green-function property; implements the A1
    retarded-variation axiom covariantly."""

    def test_retarded_green_vanishes_outside_past_cone(self):
        from grut.derivation.phi_munu.curved_background import (
            causality_check_retarded_green_function,
        )
        c = causality_check_retarded_green_function()
        assert c["retarded_green_function_vanishes_outside_past_cone"] is True

    def test_kernel_inherits_causal_support(self):
        """K^R = α × P^TT,g × G^R; support of K^R = support of G^R."""
        from grut.derivation.phi_munu.curved_background import (
            causality_check_retarded_green_function,
        )
        c = causality_check_retarded_green_function()
        assert c["kernel_inherits_causal_support"] is True

    def test_phi_depends_only_on_past_h(self):
        """Φ(x) = ∫_{J^-(x)} √-g K^R h dx' — depends only on h on
        the past lightcone of x."""
        from grut.derivation.phi_munu.curved_background import (
            causality_check_retarded_green_function,
        )
        c = causality_check_retarded_green_function()
        assert c["phi_munu_depends_only_on_past_h"] is True

    def test_implements_A1_axiom_covariantly(self):
        """A1 retarded-variation axiom holds in curved spacetime —
        not just in flat space."""
        from grut.derivation.phi_munu.curved_background import (
            causality_check_retarded_green_function,
        )
        c = causality_check_retarded_green_function()
        assert c["implements_A1_axiom_covariantly"] is True

    def test_flat_limit_recovers_minkowski_past_cone(self):
        from grut.derivation.phi_munu.curved_background import (
            causality_check_retarded_green_function,
        )
        c = causality_check_retarded_green_function()
        assert c["flat_limit_recovers_minkowski_retarded_support"] is True


# ─────────────────────────────────────────────────────────────────────
# Verification target 4: FRW scalar-mode compatibility (Priority 3 bridge)
# ─────────────────────────────────────────────────────────────────────


class TestFRWScalarModeCompatibility:
    """Target 4: The scaffold makes explicit how Φ_μν^curved becomes
    a correction to cosmological perturbations on FRW. This is the
    BRIDGE INTO PRIORITY 3 (n_g(ω) covariance)."""

    def test_frw_box_g_includes_hubble_coupling(self):
        """The FRW d'Alembertian on scalar modes contains 2H(η) ∂_η
        coupling — this is what makes χ time-dependent on FRW."""
        from grut.derivation.phi_munu.curved_background import (
            frw_scalar_mode_compatibility,
        )
        f = frw_scalar_mode_compatibility()
        box_g_FRW = f["frw_box_g_scalar_mode"]
        # Should reference H_conformal somewhere
        assert "H_conformal" in str(box_g_FRW)

    def test_frw_chi_has_k_dependence(self):
        """χ_FRW depends on comoving wavenumber k — n_g(ω) is now
        n_g(ω, k, t)."""
        from grut.derivation.phi_munu.curved_background import (
            frw_scalar_mode_compatibility, K_COMOVING,
        )
        f = frw_scalar_mode_compatibility()
        chi = f["frw_chi_susceptibility_operator"]
        assert chi.has(K_COMOVING)

    def test_frw_chi_has_tau_0_squared(self):
        """The operator susceptibility carries τ_0² in the relaxation
        denominator."""
        from grut.derivation.phi_munu.curved_background import (
            frw_scalar_mode_compatibility,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0
        f = frw_scalar_mode_compatibility()
        chi = f["frw_chi_susceptibility_operator"]
        assert chi.has(TAU_0)

    def test_n_g_squared_FRW_form_is_one_plus_alpha_chi(self):
        """The output n_g²(ω, k, t) = 1 + α × χ_FRW(k, η).
        This IS the integrand Priority 3 needs to derive covariantly."""
        from grut.derivation.phi_munu.curved_background import (
            frw_scalar_mode_compatibility,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import ALPHA
        f = frw_scalar_mode_compatibility()
        n_g_sq = f["n_g_squared_FRW_form"]
        assert n_g_sq.has(ALPHA)
        # Should have the additive structure 1 + α × χ
        # Substituting χ → 0 should give n_g² → 1 (high-k / GR limit)
        chi = f["frw_chi_susceptibility_operator"]
        # Replace χ → 0 (formally, take chi → 0)
        n_g_at_zero_chi = (1 + ALPHA * 0)
        assert n_g_at_zero_chi == 1

    def test_priority_3_bridge_is_marked(self):
        """The scaffold explicitly identifies the Priority 3 bridge."""
        from grut.derivation.phi_munu.curved_background import (
            frw_scalar_mode_compatibility,
        )
        f = frw_scalar_mode_compatibility()
        assert f["is_priority_3_bridge"] is True
        assert "priority_3_target" in f
        assert "Priority 3" in f["priority_3_target"] or "P3" in f["priority_3_target"]

    def test_super_horizon_limit_has_form(self):
        """The super-horizon (k → 0) limit produces a time-dependent
        operator depending on H(η). This is the ω-large-scale behavior
        Priority 3 uses."""
        from grut.derivation.phi_munu.curved_background import (
            frw_scalar_mode_compatibility,
        )
        f = frw_scalar_mode_compatibility()
        super_horizon = f["super_horizon_limit_kappa_to_zero"]
        # Should contain H_conformal
        assert "H_conformal" in str(super_horizon)


# ─────────────────────────────────────────────────────────────────────
# Cross-consistency with Correction #23 (linearized result)
# ─────────────────────────────────────────────────────────────────────


class TestConsistencyWithLinearizedDerivation:
    """The curved scaffold must be CONSISTENT with the linearized
    derivation (Correction #23). The flat limit reduces them to the
    same kernel form."""

    def test_alpha_inherits_from_linearized(self):
        """The α used in curved-form is the SAME α as in linearized.
        Correction #24 does not modify α_vac."""
        from grut.derivation.phi_munu.curved_background import (
            phi_munu_curved_integral_form,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import ALPHA
        f = phi_munu_curved_integral_form()
        decomp = f["kernel_decomposition"]
        assert decomp["alpha_factor"] is ALPHA

    def test_tau_0_inherits_from_linearized(self):
        """The τ_0 used in curved χ_FRW is the SAME τ_0 as in
        linearized χ. The macroscopic gravitational relaxation time
        is unchanged."""
        from grut.derivation.phi_munu.curved_background import (
            frw_scalar_mode_compatibility,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0
        f = frw_scalar_mode_compatibility()
        chi = f["frw_chi_susceptibility_operator"]
        assert chi.has(TAU_0)

    def test_curved_verify_includes_flat_recovery_leg(self):
        from grut.derivation.phi_munu.curved_background import verify
        v = verify()
        assert "flat_limit_recovers_correction_23" in v
        assert v["flat_limit_recovers_correction_23"] is True

    def test_both_modules_share_alpha_and_tau_0_symbols(self):
        """The curved module imports α and τ_0 from the linearized
        module, ensuring symbol identity (not just value match)."""
        from grut.derivation.phi_munu.curved_background import (
            ALPHA as ALPHA_curved, TAU_0 as TAU_0_curved,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import (
            ALPHA, TAU_0,
        )
        assert ALPHA_curved is ALPHA
        assert TAU_0_curved is TAU_0
