"""Regression tests for Priority 3 closure (MG-EFT mapping).

Pins the three closure gates of `n_g_omega_cosmological_covariance_open_question`:

  Gate 1: ω → k_phys × c identification with gauge-invariance argument
  Gate 2: gauge-invariance under conformal-Newtonian / synchronous /
          comoving (manifest at WKB level since χ_FRW depends only on
          gauge-invariant background quantities)
  Gate 3: μ_GRUT(k, a) = n_g²(k, a), γ_GRUT(k, a) = 1 — explicit map
          to the modified-gravity EFT-of-dark-energy framework

Plus the SCOPE CLARIFICATION (FRW linear perturbations ≠ bound-
system / nonlinear halo regimes), preserved at code level via the
convention declaration.
"""

from __future__ import annotations

import math
from fractions import Fraction

import sympy as sp


# ─────────────────────────────────────────────────────────────────────
# Module imports & verify()
# ─────────────────────────────────────────────────────────────────────


class TestModuleImports:
    def test_module_importable(self):
        from grut.derivation.phi_munu import mg_eft_mapping  # noqa
        assert hasattr(mg_eft_mapping, "verify")

    def test_module_exports_priority_3_API(self):
        from grut.derivation.phi_munu.mg_eft_mapping import (
            convention_declaration,
            omega_effective_for_cosmological_mode,
            omega_tau_0_dimensionless_argument,
            gauge_invariance_check_three_gauges,
            mu_GRUT,
            gamma_GRUT,
            mu_minus_one_GRUT_at_DC,
            mu_GRUT_numeric,
            mu_minus_one_at_super_horizon_today,
            mu_minus_one_at_transition_today,
            observational_constraints_today,
            verify,
        )
        for fn in (
            convention_declaration,
            omega_effective_for_cosmological_mode,
            omega_tau_0_dimensionless_argument,
            gauge_invariance_check_three_gauges,
            mu_GRUT,
            gamma_GRUT,
            mu_minus_one_GRUT_at_DC,
            mu_GRUT_numeric,
            mu_minus_one_at_super_horizon_today,
            mu_minus_one_at_transition_today,
            observational_constraints_today,
            verify,
        ):
            assert callable(fn)


class TestVerifyHarness:
    def test_verify_all_eight_legs_pass(self):
        from grut.derivation.phi_munu.mg_eft_mapping import verify
        v = verify()
        for k, val in v.items():
            assert val is True, f"Priority 3 verify() leg failed: {k} = {val}"


# ─────────────────────────────────────────────────────────────────────
# Convention declaration (Priority 3)
# ─────────────────────────────────────────────────────────────────────


class TestConventionDeclaration:
    """C1p3-C6p3 close the three gates with explicit statements."""

    def test_C1p3_omega_identification_states_k_phys_times_c(self):
        from grut.derivation.phi_munu.mg_eft_mapping import (
            convention_declaration,
        )
        d = convention_declaration()
        c1p3 = d["C1p3_omega_identification"]
        assert "k_phys" in c1p3
        assert "c" in c1p3.lower() or "speed of light" in c1p3.lower()
        assert "gauge-invariant" in c1p3.lower() or "gauge invariant" in c1p3.lower()

    def test_C2p3_states_WKB_regime_for_gauge_invariance(self):
        from grut.derivation.phi_munu.mg_eft_mapping import (
            convention_declaration,
        )
        d = convention_declaration()
        c2p3 = d["C2p3_gauge_invariance_regime"]
        assert "WKB" in c2p3
        assert "(Hτ_0)" in c2p3 or "10⁻⁶" in c2p3 or "subleading" in c2p3.lower()

    def test_C3p3_states_eft_mg_dictionary(self):
        from grut.derivation.phi_munu.mg_eft_mapping import (
            convention_declaration,
        )
        d = convention_declaration()
        c3p3 = d["C3p3_eft_mg_dictionary"]
        # Must reference the standard MG framework
        assert "Pogosian-Silvestri" in c3p3 or "Bertschinger" in c3p3 or "EFT" in c3p3

    def test_C4p3_states_mu_and_gamma(self):
        from grut.derivation.phi_munu.mg_eft_mapping import (
            convention_declaration,
        )
        d = convention_declaration()
        c4p3 = d["C4p3_mu_gamma_GRUT"]
        assert "μ_GRUT" in c4p3
        assert "γ_GRUT" in c4p3
        assert "n_g²" in c4p3 or "n_g^2" in c4p3
        assert "1" in c4p3  # γ = 1

    def test_C5p3_observational_baseline(self):
        from grut.derivation.phi_munu.mg_eft_mapping import (
            convention_declaration,
        )
        d = convention_declaration()
        c5p3 = d["C5p3_observational_baseline"]
        assert "Planck" in c5p3
        assert "DESI" in c5p3 or "Euclid" in c5p3

    def test_C6p3_scope_clarification_present(self):
        """The scope clarification (linear FRW perturbations ONLY) must
        be explicitly named in the convention declaration. This prevents
        misreading the result as 'GRUT recovers GR at galactic scales'
        — a confusion the user flagged and that the docstring addresses."""
        from grut.derivation.phi_munu.mg_eft_mapping import (
            convention_declaration,
        )
        d = convention_declaration()
        c6p3 = d["C6p3_scope_linear_FRW_perturbations_only"]
        assert "LINEAR" in c6p3 or "linear" in c6p3
        assert "FRW" in c6p3
        assert ("bound" in c6p3.lower() or "nonlinear" in c6p3.lower()
                or "galaxies" in c6p3.lower() or "clusters" in c6p3.lower())

    def test_phase_3_status_marked_closed(self):
        from grut.derivation.phi_munu.mg_eft_mapping import (
            convention_declaration,
        )
        d = convention_declaration()
        s = d["phase_3_status"]
        assert "PRIORITY 3 CLOSED" in s or "CLOSED" in s


# ─────────────────────────────────────────────────────────────────────
# Gate 1 — ω → k_phys × c identification
# ─────────────────────────────────────────────────────────────────────


class TestGate1OmegaIdentification:
    def test_omega_eff_equals_k_phys_times_c(self):
        from grut.derivation.phi_munu.mg_eft_mapping import (
            omega_effective_for_cosmological_mode, K_PHYS,
        )
        c = sp.Symbol("c", positive=True)
        omega = omega_effective_for_cosmological_mode(K_PHYS, c)
        assert sp.simplify(omega - K_PHYS * c) == 0

    def test_dimensionless_argument_is_k_phys_c_tau_0_squared(self):
        """(ω τ_0)² = (k_phys c τ_0)² when ω = k_phys c."""
        from grut.derivation.phi_munu.mg_eft_mapping import (
            omega_tau_0_dimensionless_argument, K_PHYS,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0
        c = sp.Symbol("c", positive=True)
        arg = omega_tau_0_dimensionless_argument(K_PHYS, TAU_0, c)
        expected = (K_PHYS * c * TAU_0)**2
        assert sp.simplify(arg - expected) == 0


# ─────────────────────────────────────────────────────────────────────
# Gate 2 — gauge-invariance verification
# ─────────────────────────────────────────────────────────────────────


class TestGate2GaugeInvariance:
    def test_conformal_newtonian_gauge_invariant(self):
        from grut.derivation.phi_munu.mg_eft_mapping import (
            gauge_invariance_check_three_gauges,
        )
        g = gauge_invariance_check_three_gauges()
        assert g["conformal_newtonian_gauge_invariant"] is True

    def test_synchronous_gauge_invariant(self):
        from grut.derivation.phi_munu.mg_eft_mapping import (
            gauge_invariance_check_three_gauges,
        )
        g = gauge_invariance_check_three_gauges()
        assert g["synchronous_gauge_invariant"] is True

    def test_comoving_gauge_invariant(self):
        from grut.derivation.phi_munu.mg_eft_mapping import (
            gauge_invariance_check_three_gauges,
        )
        g = gauge_invariance_check_three_gauges()
        assert g["comoving_gauge_invariant"] is True

    def test_invariance_exact_at_WKB_level(self):
        from grut.derivation.phi_munu.mg_eft_mapping import (
            gauge_invariance_check_three_gauges,
        )
        g = gauge_invariance_check_three_gauges()
        assert g["exact_at_wkb_level"] is True
        assert g["wkb_regime_required"] is True


# ─────────────────────────────────────────────────────────────────────
# Gate 3 — μ(k, a) and γ(k, a) — the MG-EFT mapping
# ─────────────────────────────────────────────────────────────────────


class TestGate3MuGammaMapping:
    def test_mu_GRUT_equals_n_g_squared(self):
        """μ_GRUT(k, a) ≡ n_g²(k, a) — the load-bearing identification."""
        from grut.derivation.phi_munu.mg_eft_mapping import mu_GRUT
        from grut.derivation.phi_munu.frw_explicit import (
            n_g_squared_FRW_in_physical_wavenumber, K_PHYS,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import (
            TAU_0, ALPHA,
        )
        mu = mu_GRUT(K_PHYS, TAU_0, ALPHA)
        n_g_sq = n_g_squared_FRW_in_physical_wavenumber(K_PHYS, TAU_0, ALPHA)
        assert sp.simplify(mu - n_g_sq) == 0

    def test_gamma_GRUT_equals_one(self):
        """γ_GRUT(k, a) = 1 — no gravitational slip in GRUT.

        The TT-projector P^TT,g acts symmetrically on Φ and Ψ, so in
        the absence of matter anisotropic stress (radiation/matter
        epochs), Φ = Ψ and γ = 1. SHARP PREDICTION distinguishing
        GRUT from Brans-Dicke, f(R), DGP."""
        from grut.derivation.phi_munu.mg_eft_mapping import gamma_GRUT
        gamma = gamma_GRUT()
        assert gamma == 1

    def test_mu_at_DC_is_one_plus_alpha(self):
        """Super-horizon limit: μ → 1 + α (full constitutive enhancement)."""
        from grut.derivation.phi_munu.mg_eft_mapping import mu_GRUT
        from grut.derivation.phi_munu.linearized_ctp_action import (
            TAU_0, ALPHA,
        )
        from grut.derivation.phi_munu.frw_explicit import K_PHYS
        mu = mu_GRUT(K_PHYS, TAU_0, ALPHA)
        mu_at_DC = mu.subs(K_PHYS, 0)
        assert sp.simplify(mu_at_DC - (1 + ALPHA)) == 0

    def test_mu_at_high_k_is_one_LambdaCDM(self):
        """Sub-horizon limit: μ → 1 (ΛCDM recovery)."""
        from grut.derivation.phi_munu.mg_eft_mapping import mu_GRUT
        from grut.derivation.phi_munu.linearized_ctp_action import (
            TAU_0, ALPHA,
        )
        from grut.derivation.phi_munu.frw_explicit import K_PHYS
        mu = mu_GRUT(K_PHYS, TAU_0, ALPHA)
        assert sp.limit(mu, K_PHYS, sp.oo) == 1

    def test_mu_at_transition_is_one_plus_alpha_over_two(self):
        """At k_phys τ_0 = 1: μ = 1 + α/2."""
        from grut.derivation.phi_munu.mg_eft_mapping import mu_GRUT
        from grut.derivation.phi_munu.linearized_ctp_action import (
            TAU_0, ALPHA,
        )
        from grut.derivation.phi_munu.frw_explicit import K_PHYS
        mu = mu_GRUT(K_PHYS, TAU_0, ALPHA)
        mu_at_transition = mu.subs(K_PHYS, 1 / TAU_0)
        assert sp.simplify(mu_at_transition - (1 + ALPHA / 2)) == 0

    def test_mu_minus_one_at_DC_with_alpha_third_is_one_third(self):
        """The cosmological-scale modified-gravity signal: μ - 1 = 1/3
        on the largest scales (with α_vac = 1/3 from KS 2011)."""
        from grut.derivation.phi_munu.mg_eft_mapping import (
            mu_minus_one_GRUT_at_DC,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import ALPHA
        mu_m1_DC = mu_minus_one_GRUT_at_DC(ALPHA)
        # With α = 1/3, mu_minus_one_GRUT_at_DC = α = 1/3
        result = mu_m1_DC.subs(ALPHA, sp.Rational(1, 3))
        assert sp.simplify(result - sp.Rational(1, 3)) == 0


# ─────────────────────────────────────────────────────────────────────
# Numerical evaluation
# ─────────────────────────────────────────────────────────────────────


class TestNumericalEvaluation:
    def test_mu_minus_one_at_super_horizon_today_is_one_third(self):
        from grut.derivation.phi_munu.mg_eft_mapping import (
            mu_minus_one_at_super_horizon_today,
        )
        result = mu_minus_one_at_super_horizon_today()
        assert abs(result - 1 / 3) < 1e-10

    def test_mu_minus_one_at_transition_is_one_sixth(self):
        from grut.derivation.phi_munu.mg_eft_mapping import (
            mu_minus_one_at_transition_today,
        )
        result = mu_minus_one_at_transition_today()
        assert abs(result - 1 / 6) < 1e-10

    def test_mu_GRUT_numeric_super_horizon_is_4_over_3(self):
        from grut.derivation.phi_munu.mg_eft_mapping import mu_GRUT_numeric
        # k → 0 limit (very low k_phys)
        result = mu_GRUT_numeric(1e-30)
        assert abs(result - 4 / 3) < 1e-6

    def test_mu_GRUT_numeric_sub_horizon_is_one(self):
        from grut.derivation.phi_munu.mg_eft_mapping import mu_GRUT_numeric
        # k → ∞ limit (very high k_phys)
        result = mu_GRUT_numeric(1e30)
        assert abs(result - 1.0) < 1e-12


# ─────────────────────────────────────────────────────────────────────
# Observational constraints
# ─────────────────────────────────────────────────────────────────────


class TestObservationalConstraints:
    def test_constraints_dict_includes_planck_DESI_euclid(self):
        from grut.derivation.phi_munu.mg_eft_mapping import (
            observational_constraints_today,
        )
        c = observational_constraints_today()
        assert "Planck_2018_paper_VI" in c
        assert "DESI_Y1_2024" in c
        assert "Euclid_2027_forecast" in c

    def test_GRUT_prediction_is_one_third_in_each_constraint(self):
        from grut.derivation.phi_munu.mg_eft_mapping import (
            observational_constraints_today,
        )
        c = observational_constraints_today()
        for survey, data in c.items():
            assert "GRUT_predicts_mu_minus_1" in data
            assert abs(data["GRUT_predicts_mu_minus_1"] - 1 / 3) < 1e-3

    def test_GRUT_within_2_sigma_of_planck(self):
        """GRUT's μ - 1 = 1/3 ≈ 0.333 sits ~2σ above Planck central
        0.07 (with σ = 0.13). Within current bounds; targets next-
        generation surveys."""
        from grut.derivation.phi_munu.mg_eft_mapping import (
            observational_constraints_today,
        )
        c = observational_constraints_today()
        planck = c["Planck_2018_paper_VI"]
        sigma_distance = (planck["GRUT_predicts_mu_minus_1"]
                          - planck["mu_minus_1_central"]
                          ) / planck["mu_minus_1_one_sigma"]
        assert sigma_distance > 1.5  # ~2σ above central
        assert sigma_distance < 3.0   # but not yet ruled out
        assert planck["GRUT_within_2_sigma"] is True

    def test_DESI_predicts_significant_tension(self):
        """DESI Y1+ at 5% precision should resolve GRUT's μ - 1 = 1/3
        prediction at >3σ confidence (relative to current Planck
        central)."""
        from grut.derivation.phi_munu.mg_eft_mapping import (
            observational_constraints_today,
        )
        c = observational_constraints_today()
        desi = c["DESI_Y1_2024"]
        assert desi["tension_at_DESI_precision"] > 3.0  # >3σ test

    def test_euclid_definitive_at_3_sigma_or_more(self):
        from grut.derivation.phi_munu.mg_eft_mapping import (
            observational_constraints_today,
        )
        c = observational_constraints_today()
        euclid = c["Euclid_2027_forecast"]
        assert "definitive" in euclid["discriminating_power"].lower()


# ─────────────────────────────────────────────────────────────────────
# Scope clarification — FRW linear ≠ bound systems
# ─────────────────────────────────────────────────────────────────────


class TestScopeClarification:
    """The user explicitly flagged that 'galactic and cluster scales
    recover GR' from Phase 2C must NOT be misread as GRUT losing dark-
    sector phenomenology in those regimes. The bound-system / nonlinear
    halo physics (rotation curves, cluster-merger offsets, BH interior)
    operates with different operating variables. This is now explicitly
    documented in the convention declaration."""

    def test_module_docstring_includes_scope_clarification(self):
        import grut.derivation.phi_munu.mg_eft_mapping as mod
        doc = mod.__doc__
        assert "SCOPE CLARIFICATION" in doc or "Scope Clarification" in doc
        assert "bound-system" in doc.lower() or "nonlinear" in doc.lower()
        assert "galactic" in doc.lower() or "rotation" in doc.lower()

    def test_module_docstring_distinguishes_linear_FRW_from_bound(self):
        import grut.derivation.phi_munu.mg_eft_mapping as mod
        doc = mod.__doc__
        # The two regimes must be distinguished
        assert "Linear FRW" in doc or "linear FRW" in doc
        assert ("bound" in doc.lower()
                or "halo" in doc.lower()
                or "merger" in doc.lower())

    def test_convention_C6p3_explicitly_names_scope(self):
        from grut.derivation.phi_munu.mg_eft_mapping import (
            convention_declaration,
        )
        d = convention_declaration()
        c6p3 = d["C6p3_scope_linear_FRW_perturbations_only"]
        # Names the linear-FRW regime AND the contrasting bound-system
        # regime
        assert "LINEAR" in c6p3 or "linear" in c6p3
        assert "FRW" in c6p3
        assert ("bound" in c6p3.lower() or "galaxies" in c6p3.lower()
                or "clusters" in c6p3.lower() or "different" in c6p3.lower())


# ─────────────────────────────────────────────────────────────────────
# Cross-consistency with Phase 2C
# ─────────────────────────────────────────────────────────────────────


class TestCrossConsistencyWithPhase2C:
    def test_mu_GRUT_inherits_chi_FRW_form(self):
        """μ_GRUT IS the n_g² of Phase 2C, structurally identical."""
        from grut.derivation.phi_munu.mg_eft_mapping import mu_GRUT
        from grut.derivation.phi_munu.frw_explicit import (
            n_g_squared_FRW_in_physical_wavenumber, K_PHYS,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import (
            TAU_0, ALPHA,
        )
        mu = mu_GRUT(K_PHYS, TAU_0, ALPHA)
        n_g_sq = n_g_squared_FRW_in_physical_wavenumber(K_PHYS, TAU_0, ALPHA)
        # Identity at the symbolic level
        assert sp.simplify(mu - n_g_sq) == 0

    def test_alpha_inherits_from_linearized_module(self):
        from grut.derivation.phi_munu.mg_eft_mapping import (
            ALPHA as ALPHA_p3,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import ALPHA
        assert ALPHA_p3 is ALPHA

    def test_tau_0_inherits_from_linearized_module(self):
        from grut.derivation.phi_munu.mg_eft_mapping import (
            TAU_0 as TAU_0_p3,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0
        assert TAU_0_p3 is TAU_0

    def test_alpha_vac_value_one_third(self):
        from grut.derivation.phi_munu.linearized_ctp_action import (
            alpha_vac_from_conformal_mode,
        )
        # The α_vac that enters μ_GRUT is the canonical 1/3
        assert alpha_vac_from_conformal_mode() == Fraction(1, 3)
