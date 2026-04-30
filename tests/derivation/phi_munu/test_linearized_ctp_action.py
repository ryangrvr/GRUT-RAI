"""Regression tests for the linearized Φ_μν derivation.

These pin the structural derivation that closes
`constitutive_projection_gravity_heuristic_open_question` (Ch 12).

Pattern matches tests/derivation/tji/test_ms_bar_reconciliation.py:
exact-equality assertions on symbolic SymPy expressions, no
float approximations for structural identities.

Coverage:
  - The variation δS_CTP/δh_a produces Φ_μν as kernel × h_r
  - The kernel form K(ω) = α_vac × χ(ω) emerges from the
    constitutive cross term, NOT postulated
  - The high-frequency limit is exactly 0 (GR recovery)
  - The low-frequency limit is exactly α_vac (full constitutive)
  - The Bianchi structural property holds for ALL h_r and ALL kernel
    time structures (not just single-mode plane wave)
  - α_vac = 1/3 from conformal-mode-scalar identification
  - Convention declaration is present and complete
  - The susceptibility's pole is at ω = -i/τ_0 (lower half-plane,
    causal)
  - The derivation is consistent with gr_recovery.py's existing
    susceptibility-based postulate (the postulate is now derived)
"""

from __future__ import annotations

from fractions import Fraction

import sympy as sp


# ─────────────────────────────────────────────────────────────────────
# Module imports & verify() block
# ─────────────────────────────────────────────────────────────────────


class TestModuleImports:
    def test_module_importable(self):
        from grut.derivation.phi_munu import linearized_ctp_action  # noqa
        assert hasattr(linearized_ctp_action, "verify")

    def test_package_init_exports(self):
        from grut.derivation.phi_munu import (
            constitutive_kernel_fourier,
            convention_declaration,
            derive_phi_munu_from_variation,
            extract_phi_munu_kernel_form,
            phi_munu_high_freq_limit,
            phi_munu_low_freq_limit,
            transverse_traceless_projector,
            verify,
        )
        # Exercise — they should all be callable.
        for fn in (
            constitutive_kernel_fourier,
            convention_declaration,
            derive_phi_munu_from_variation,
            extract_phi_munu_kernel_form,
            phi_munu_high_freq_limit,
            phi_munu_low_freq_limit,
            transverse_traceless_projector,
            verify,
        ):
            assert callable(fn)


class TestVerifyHarness:
    def test_verify_all_legs_pass(self):
        """The seven structural-derivation legs must all return True."""
        from grut.derivation.phi_munu.linearized_ctp_action import verify
        v = verify()
        for k, val in v.items():
            assert val is True, f"verify() leg failed: {k} = {val}"


# ─────────────────────────────────────────────────────────────────────
# Convention declaration (NIS discipline — same pattern as TJI)
# ─────────────────────────────────────────────────────────────────────


class TestConventionDeclaration:
    """Every Fraction equality in this module is asserted under
    these conventions; if any change, all downstream pinned values
    must be re-derived. Mirrors discipline of TJI Phase-0.5."""

    def test_C1_metric_signature(self):
        from grut.derivation.phi_munu.linearized_ctp_action import (
            convention_declaration,
        )
        d = convention_declaration()
        assert "(-, +, +, +)" in d["C1_metric_signature"]

    def test_C2_metric_perturbation(self):
        from grut.derivation.phi_munu.linearized_ctp_action import (
            convention_declaration,
        )
        d = convention_declaration()
        c2 = d["C2_metric_perturbation"]
        assert "g_μν" in c2 or "g_munu" in c2.lower()
        assert "η_μν" in c2 or "eta" in c2.lower()
        assert "h_μν" in c2 or "h_mu" in c2.lower()

    def test_C3_keldysh_basis_matches_axioms(self):
        from grut.derivation.phi_munu.linearized_ctp_action import (
            convention_declaration,
        )
        d = convention_declaration()
        c3 = d["C3_keldysh_basis"]
        assert "h_r" in c3
        assert "h_a" in c3
        assert "(h+ + h-)/2" in c3 or "(h_+ + h_-)/2" in c3.lower() or "h+" in c3.lower()

    def test_C4_memory_kernel_form_states_retarded(self):
        from grut.derivation.phi_munu.linearized_ctp_action import (
            convention_declaration,
        )
        d = convention_declaration()
        c4 = d["C4_memory_kernel_form"]
        assert "Θ" in c4 or "Heaviside" in c4 or "Retarded" in c4 or "retarded" in c4

    def test_C7_projector_is_transverse_tracefree(self):
        from grut.derivation.phi_munu.linearized_ctp_action import (
            convention_declaration,
        )
        d = convention_declaration()
        c7 = d["C7_projector"]
        assert "transverse" in c7.lower() or "tracefree" in c7.lower() or "TT" in c7

    def test_phase_2_status_named(self):
        """The convention declaration must explicitly mark what's
        derived (linearized) vs research-tier (curved background)."""
        from grut.derivation.phi_munu.linearized_ctp_action import (
            convention_declaration,
        )
        d = convention_declaration()
        s = d["phase_2_status"]
        assert "Linearized" in s or "linearized" in s
        assert "curved" in s.lower() or "Curved" in s


# ─────────────────────────────────────────────────────────────────────
# Susceptibility & kernel structure
# ─────────────────────────────────────────────────────────────────────


class TestSusceptibilityForm:
    """χ(ω) = 1/(1 - iωτ_0) is the structural form. Pin its
    properties: single pole, lower-half-plane (causal), correct
    DC and UV limits."""

    def test_chi_DC_is_one(self):
        from grut.derivation.phi_munu.linearized_ctp_action import (
            susceptibility_chi, OMEGA, TAU_0,
        )
        chi = susceptibility_chi(OMEGA, TAU_0)
        assert sp.simplify(chi.subs(OMEGA, 0) - 1) == 0

    def test_chi_high_freq_decays_to_zero(self):
        from grut.derivation.phi_munu.linearized_ctp_action import (
            susceptibility_chi, OMEGA, TAU_0,
        )
        chi = susceptibility_chi(OMEGA, TAU_0)
        assert sp.limit(chi, OMEGA, sp.oo) == 0

    def test_chi_pole_in_lower_half_plane(self):
        """The denominator (1 - iωτ_0) vanishes at ω = -i/τ_0,
        which is in the LOWER half-plane (Im(ω) < 0). This is the
        framework's causality structure (single-pole, KK-compatible).

        OMEGA is declared real in the module (a physical-frequency
        symbol), so we verify the pole by direct evaluation: substitute
        ω → -i/τ_0 (a complex symbol) into the denominator and
        confirm it vanishes."""
        from grut.derivation.phi_munu.linearized_ctp_action import (
            susceptibility_chi, TAU_0,
        )
        # Use a fresh complex symbol to evaluate the pole.
        omega_c = sp.Symbol("omega_complex")
        chi = susceptibility_chi(omega_c, TAU_0)
        denom = sp.fraction(chi)[1]
        # Substitute the expected pole and verify denom → 0
        expected_pole = -sp.I / TAU_0
        denom_at_pole = sp.simplify(denom.subs(omega_c, expected_pole))
        assert denom_at_pole == 0
        # The pole is in the lower half-plane: Im(-i/τ_0) = -1/τ_0 < 0
        assert sp.im(expected_pole) == -1 / TAU_0


class TestConstitutiveKernelForm:
    """The kernel K^R(ω) = α × χ(ω) — structural, not postulated."""

    def test_kernel_factors_alpha_times_chi(self):
        from grut.derivation.phi_munu.linearized_ctp_action import (
            constitutive_kernel_fourier, susceptibility_chi,
            OMEGA, TAU_0, ALPHA,
        )
        k = constitutive_kernel_fourier(OMEGA, TAU_0, ALPHA)
        chi = susceptibility_chi(OMEGA, TAU_0)
        expected = ALPHA * chi
        assert sp.simplify(k - expected) == 0

    def test_kernel_DC_is_alpha(self):
        from grut.derivation.phi_munu.linearized_ctp_action import (
            constitutive_kernel_fourier, OMEGA, TAU_0, ALPHA,
        )
        k = constitutive_kernel_fourier(OMEGA, TAU_0, ALPHA)
        assert sp.simplify(k.subs(OMEGA, 0) - ALPHA) == 0

    def test_kernel_high_freq_vanishes(self):
        from grut.derivation.phi_munu.linearized_ctp_action import (
            constitutive_kernel_fourier, OMEGA, TAU_0, ALPHA,
        )
        k = constitutive_kernel_fourier(OMEGA, TAU_0, ALPHA)
        assert sp.limit(k, OMEGA, sp.oo) == 0


# ─────────────────────────────────────────────────────────────────────
# Variation — the LOAD-BEARING derivation
# ─────────────────────────────────────────────────────────────────────


class TestVariationProducesPhiMuNu:
    """δS_CTP/δh_a |_{h_a=0} produces Φ_μν as a kernel × h_r term.
    This is the structural derivation that lifts Φ_μν from postulate
    to derived form."""

    def test_variation_produces_einstein_matter_phi_terms(self):
        """The variation has exactly four contributions: Einstein,
        matter, Φ_μν (constitutive), noise. Noise must vanish at
        h_a = 0 (it's quadratic in h_a)."""
        from grut.derivation.phi_munu.linearized_ctp_action import (
            derive_phi_munu_from_variation,
        )
        d = derive_phi_munu_from_variation()
        # All four expected keys present
        assert "einstein_term" in d
        assert "matter_term" in d
        assert "phi_munu_term" in d
        assert "noise_term" in d

    def test_noise_term_vanishes_at_h_a_zero(self):
        """S_noise is quadratic in h_a; its derivative at h_a = 0
        must be exactly 0. Required for the classical EOM to be
        deterministic at the variational level."""
        from grut.derivation.phi_munu.linearized_ctp_action import (
            derive_phi_munu_from_variation,
        )
        d = derive_phi_munu_from_variation()
        assert d["noise_term"] == 0

    def test_phi_munu_term_has_kernel_h_r_structure(self):
        """The Φ_μν term, divided by h_r, equals (1/2) × α × χ(ω) —
        the kernel coefficient in the variation rule. This is the
        STRUCTURAL output: Φ_μν ∝ kernel × h_r, not Φ_μν postulated."""
        from grut.derivation.phi_munu.linearized_ctp_action import (
            derive_phi_munu_from_variation, susceptibility_chi,
            H_R, OMEGA, TAU_0, ALPHA,
        )
        d = derive_phi_munu_from_variation()
        per_h_r = sp.simplify(d["phi_munu_term"] / H_R)
        expected = sp.Rational(1, 2) * ALPHA * susceptibility_chi(OMEGA, TAU_0)
        assert sp.simplify(per_h_r - expected) == 0

    def test_einstein_term_proportional_to_h_r(self):
        """The Einstein-Hilbert variation gives a term proportional
        to h_r, with coefficient a_EH/(16πG). Identifies G^(1)_μν
        in the equation of motion."""
        from grut.derivation.phi_munu.linearized_ctp_action import (
            derive_phi_munu_from_variation, H_R,
        )
        d = derive_phi_munu_from_variation()
        # Einstein term has h_r structure
        einstein = d["einstein_term"]
        assert einstein.has(H_R)

    def test_matter_term_is_T_munu_over_2(self):
        """Matter coupling (1/2) h_a T → variation gives T/2.
        Standard linearized matter source."""
        from grut.derivation.phi_munu.linearized_ctp_action import (
            derive_phi_munu_from_variation, T_MUNU,
        )
        d = derive_phi_munu_from_variation()
        matter = d["matter_term"]
        assert sp.simplify(matter - sp.Rational(1, 2) * T_MUNU) == 0


# ─────────────────────────────────────────────────────────────────────
# Extracted kernel form (the deliverable)
# ─────────────────────────────────────────────────────────────────────


class TestExtractedKernelForm:
    """The Φ_μν / h_r extraction — the structural form that
    closes the open question."""

    def test_extracted_form_is_alpha_times_chi(self):
        from grut.derivation.phi_munu.linearized_ctp_action import (
            extract_phi_munu_kernel_form, susceptibility_chi,
            OMEGA, TAU_0, ALPHA,
        )
        k = extract_phi_munu_kernel_form()
        expected = ALPHA * susceptibility_chi(OMEGA, TAU_0)
        assert sp.simplify(k - expected) == 0

    def test_extracted_form_at_DC_is_alpha(self):
        from grut.derivation.phi_munu.linearized_ctp_action import (
            extract_phi_munu_kernel_form, OMEGA, ALPHA,
        )
        k = extract_phi_munu_kernel_form()
        assert sp.simplify(k.subs(OMEGA, 0) - ALPHA) == 0

    def test_extracted_form_pole_structure(self):
        """The extracted Φ_μν/h_r has the same pole as χ(ω) — at
        ω = -i/τ_0 in the lower half-plane. Causality structure
        inherited."""
        from grut.derivation.phi_munu.linearized_ctp_action import (
            extract_phi_munu_kernel_form, OMEGA, TAU_0,
        )
        k = extract_phi_munu_kernel_form()
        denom = sp.fraction(k)[1]
        # Direct evaluation (OMEGA is real-only; pole is imaginary).
        expected_pole = -sp.I / TAU_0
        # Substitute via the abstract OMEGA — we treat it as a symbolic
        # placeholder for the pole position here.
        denom_at_pole = sp.simplify(denom.subs(OMEGA, expected_pole))
        assert denom_at_pole == 0


# ─────────────────────────────────────────────────────────────────────
# Limits — GR recovery and full-constitutive
# ─────────────────────────────────────────────────────────────────────


class TestPhiMuNuLimits:
    def test_high_freq_limit_is_exactly_zero(self):
        """Φ_μν → 0 as ωτ_0 → ∞. GR-recovery limit, V7 §22-§25."""
        from grut.derivation.phi_munu.linearized_ctp_action import (
            phi_munu_high_freq_limit,
        )
        assert phi_munu_high_freq_limit() == 0

    def test_low_freq_limit_is_exactly_alpha(self):
        """Φ_μν → α at ω → 0. Full-constitutive limit, gives n_g(0) = √(1+α)."""
        from grut.derivation.phi_munu.linearized_ctp_action import (
            phi_munu_low_freq_limit, ALPHA,
        )
        assert phi_munu_low_freq_limit() == ALPHA

    def test_low_freq_limit_with_alpha_one_third_gives_one_third(self):
        """Substituting α = 1/3 into the low-frequency limit gives 1/3 —
        the framework's α_vac value from conformal-mode-scalar identification."""
        from grut.derivation.phi_munu.linearized_ctp_action import (
            phi_munu_low_freq_limit, ALPHA,
        )
        limit = phi_munu_low_freq_limit()
        with_alpha = limit.subs(ALPHA, sp.Rational(1, 3))
        assert with_alpha == sp.Rational(1, 3)


# ─────────────────────────────────────────────────────────────────────
# Bianchi structural preservation
# ─────────────────────────────────────────────────────────────────────


class TestBianchiStructural:
    """∂^μ Φ_μν = 0 — derived structurally from ∂^μ P^TT = 0,
    not just verified on a single-mode plane wave (gr_recovery.py's
    existing weaker check)."""

    def test_projector_is_transverse(self):
        from grut.derivation.phi_munu.linearized_ctp_action import (
            transverse_traceless_projector,
        )
        P = transverse_traceless_projector()
        assert P["is_transverse"] is True

    def test_projector_is_idempotent(self):
        """P × P = P required for genuine projection."""
        from grut.derivation.phi_munu.linearized_ctp_action import (
            transverse_traceless_projector,
        )
        P = transverse_traceless_projector()
        assert P["is_idempotent"] is True

    def test_projector_trace_is_five(self):
        """5 propagating tensor modes in 4D linearized gravity (graviton's
        2 polarizations + 3 Goldstones in decoupling limit)."""
        from grut.derivation.phi_munu.linearized_ctp_action import (
            transverse_traceless_projector,
        )
        P = transverse_traceless_projector()
        assert P["trace"] == 5

    def test_bianchi_structural_for_all_h_r(self):
        """Bianchi is preserved STRUCTURALLY — for any h_r, any kernel
        time structure, any spacetime point. This is the upgrade over
        gr_recovery.py's single-mode plane-wave check."""
        from grut.derivation.phi_munu.linearized_ctp_action import (
            phi_munu_bianchi_structural,
        )
        b = phi_munu_bianchi_structural()
        assert b["bianchi_holds_for_all_h_r"] is True
        assert b["bianchi_holds_for_all_kernel"] is True
        assert b["structural_not_just_single_mode"] is True


# ─────────────────────────────────────────────────────────────────────
# α_vac = 1/3 — conformal-mode-scalar identification
# ─────────────────────────────────────────────────────────────────────


class TestAlphaVacConformalMode:
    """The α_vac coefficient in K^R = α × χ × P^TT comes from the
    conformal-mode-scalar identification (Komargodski-Schwimmer 2011
    a/c = 1/3 for a real scalar). This derivation INHERITS the value;
    Correction #23 does not modify α_vac."""

    def test_alpha_vac_from_conformal_mode_is_one_third(self):
        from grut.derivation.phi_munu.linearized_ctp_action import (
            alpha_vac_from_conformal_mode,
        )
        assert alpha_vac_from_conformal_mode() == Fraction(1, 3)

    def test_consistency_with_existing_alpha_vac_in_closure_protocol(self):
        """The derivation's α_vac value MUST equal the framework's
        canonical α_vac in closure_protocol.py. Correction #23 doesn't
        modify α_vac — it derives Φ_μν using α_vac as already given."""
        from grut.derivation.phi_munu.linearized_ctp_action import (
            alpha_vac_from_conformal_mode,
        )
        from grut.foundation.closure_protocol import ALPHA_VAC
        assert abs(float(alpha_vac_from_conformal_mode()) - ALPHA_VAC) < 1e-15


# ─────────────────────────────────────────────────────────────────────
# Consistency with existing gr_recovery.py (the postulate is now derived)
# ─────────────────────────────────────────────────────────────────────


class TestConsistencyWithGRRecoveryPostulate:
    """gr_recovery.py used Φ_μν ∝ susceptibility × T_μν as a
    POSTULATE. Correction #23 derives the same structural form from
    δS_CTP/δh_a. The kernel function in the derivation must be
    consistent with the susceptibility used in gr_recovery."""

    def test_derivation_susceptibility_matches_closure_protocol(self):
        """The derivation's χ(ω) = 1/(1 - iωτ) at α=1/3, τ=τ_0
        must produce the same numerical values as
        closure_protocol.susceptibility_chi over a range of frequencies."""
        from grut.derivation.phi_munu.linearized_ctp_action import (
            susceptibility_chi as derivation_chi, OMEGA, TAU_0,
        )
        from grut.foundation.closure_protocol import (
            susceptibility_chi as closure_chi, TAU_0_SEC, ALPHA_VAC,
        )

        chi_sym = derivation_chi(OMEGA, TAU_0)

        # closure_protocol returns α/(1-iωτ); derivation returns 1/(1-iωτ)
        # so closure_chi = α × derivation_chi for the same (ω, τ).
        for omega_val in [1e-20, 1e-10, 1.0, 1e10]:
            sym_val = complex(
                chi_sym.subs([(OMEGA, omega_val), (TAU_0, TAU_0_SEC)])
            )
            closure_val = closure_chi(omega_val, ALPHA_VAC, TAU_0_SEC)
            # Multiply derivation's χ by α to match closure's convention
            expected_match = ALPHA_VAC * sym_val
            relative_error = abs(closure_val - expected_match) / abs(expected_match)
            assert relative_error < 1e-12, (
                f"Mismatch at ω={omega_val}: derivation×α gives "
                f"{expected_match}, closure gives {closure_val}"
            )

    def test_phi_munu_DC_amplitude_gives_n_g_squared_4_over_3(self):
        """At DC: Φ_μν = α_vac × P × h_r. Per the conformal-mode
        identification, this gives the n_g²(0) = 1 + α_vac = 4/3
        refractive enhancement that is closure_protocol.N_G_DC²."""
        from grut.derivation.phi_munu.linearized_ctp_action import (
            phi_munu_low_freq_limit, ALPHA,
        )
        from grut.foundation.closure_protocol import N_G_DC
        DC_amp = phi_munu_low_freq_limit().subs(ALPHA, sp.Rational(1, 3))
        # n_g² = 1 + Φ at DC:
        n_g_sq_predicted = 1 + DC_amp
        # closure_protocol.N_G_DC = √(4/3); square it
        n_g_sq_canonical = N_G_DC ** 2
        assert abs(float(n_g_sq_predicted) - n_g_sq_canonical) < 1e-12
