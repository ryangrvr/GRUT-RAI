"""Φ_μν derivation package — Priority 2 of the v2 deposit roadmap.

Submodules:
    linearized_ctp_action — Priority 2A. Symbolic CTP action setup
        on flat spacetime, variation δS_CTP/δh_a, Φ_μν kernel
        extraction, and structural verification at the linearized
        (flat-spacetime) level. Closes the original heuristic open
        question at one structural level.

    curved_background — Priority 2B SCAFFOLD. Covariant extension
        to curved backgrounds (FRW, S⁴) with explicit √-g measure,
        bitensor retarded kernel, and four structural verification
        targets: flat-limit recovery, covariant conservation,
        causality, FRW scalar-mode compatibility (Priority 3 bridge).

    frw_explicit — Priority 2C. Explicit construction of χ_FRW(k, η)
        and n_g²(k, η) on FRW spacetime. WKB / slow-H limit gives:
            χ_FRW^WKB(k, η) = 1 / [1 + (τ_0 k_phys)²]
            n_g²(k, η) = 1 + α / [1 + (τ_0 k_phys)²]
        with sub-horizon → 1 (GR), super-horizon → 4/3, transition
        at k_phys = 1/τ_0 (λ_* ≈ 80.7 Mpc today). Beyond-WKB
        corrections are O(10⁻⁶) for late-universe cosmology — the
        WKB result is operationally complete. This is the cosmology
        backbone for Priority 3 (n_g(ω) covariance).

    mg_eft_mapping — Priority 3 closure. Maps χ_FRW(k, η) onto the
        modified-gravity EFT-of-dark-energy parameterization
        μ(k, a) / γ(k, a) for direct comparison to Planck 2018 MG /
        DESI / Euclid observational constraints. Three closure gates:
            (1) ω → k_phys × c identification, gauge-invariant at WKB
            (2) gauge-invariance verification (CN/sync/comoving)
            (3) μ_GRUT = n_g², γ_GRUT = 1 (no slip)
        Sharp prediction: GRUT lives in the "μ ≠ 1, γ = 1" subclass
        of MG models with μ - 1 = 1/3 on the largest scales.
        Includes explicit SCOPE CLARIFICATION distinguishing the
        linear FRW perturbation regime from bound-system / nonlinear
        halo regimes (rotation curves, cluster-merger dynamics).

Scope:
    Priority 2A — flat-space derivation: COMPUTED.
    Priority 2B — curved-background scaffold: ANCHORED with four
        structural checks.
    Priority 2C — explicit FRW χ_FRW(k, η) and n_g²(k, η): COMPUTED
        at WKB level. Beyond-WKB (Phase 2D) deferred — corrections
        are negligibly small for post-equality cosmology.
    Priority 3 — n_g(ω) covariance: CLOSED. ω → k_phys × c, gauge-
        invariant at WKB, mapped to μ(k, a) / γ(k, a) MG-EFT
        parameterization. cmb_boltzmann_scoping now has a well-
        defined ω; Boltzmann-code implementation is downstream
        (not a theoretical gap).

Honest framing: the cosmology backbone produces n_g²(k, η)
explicitly and maps to the standard MG-EFT framework. Modified
growth equations and observational tests (CMB, P(k), σ_8) are
downstream computational tasks using the structural ingredients
this package provides.
"""

from grut.derivation.phi_munu.linearized_ctp_action import (
    constitutive_kernel_fourier,
    convention_declaration,
    derive_phi_munu_from_variation,
    extract_phi_munu_kernel_form,
    phi_munu_high_freq_limit,
    phi_munu_low_freq_limit,
    transverse_traceless_projector,
    verify,
)
from grut.derivation.phi_munu.curved_background import (
    causality_check_retarded_green_function,
    convention_declaration as curved_convention_declaration,
    covariant_conservation_check,
    curved_ctp_action_terms,
    flat_limit_check,
    frw_scalar_mode_compatibility,
    phi_munu_curved_integral_form,
    phi_munu_curved_operator_form,
    verify as curved_verify,
)
from grut.derivation.phi_munu.frw_explicit import (
    beyond_wkb_correction_magnitude_today,
    box_g_on_scalar_fourier_mode,
    chi_FRW_WKB,
    chi_FRW_WKB_in_physical_wavenumber,
    conformal_hubble,
    conformal_time_FRW_metric,
    convention_declaration as frw_convention_declaration,
    n_g_squared_FRW_WKB,
    n_g_squared_FRW_in_physical_wavenumber,
    n_g_squared_numeric,
    relaxation_operator_on_scalar_fourier,
    sub_horizon_limit,
    super_horizon_limit,
    transition_wavelength_today_Mpc,
    transition_wavenumber,
    transition_wavenumber_today_inverse_meters,
    verify as frw_verify,
)
from grut.derivation.phi_munu.mg_eft_mapping import (
    convention_declaration as mg_eft_convention_declaration,
    gamma_GRUT,
    gauge_invariance_check_three_gauges,
    mu_GRUT,
    mu_GRUT_numeric,
    mu_minus_one_GRUT_at_DC,
    mu_minus_one_at_super_horizon_today,
    mu_minus_one_at_transition_today,
    observational_constraints_today,
    omega_effective_for_cosmological_mode,
    omega_tau_0_dimensionless_argument,
    verify as mg_eft_verify,
)

__all__ = [
    # Linearized (Priority 2A)
    "constitutive_kernel_fourier",
    "convention_declaration",
    "derive_phi_munu_from_variation",
    "extract_phi_munu_kernel_form",
    "phi_munu_high_freq_limit",
    "phi_munu_low_freq_limit",
    "transverse_traceless_projector",
    "verify",
    # Curved-background scaffold (Priority 2B)
    "causality_check_retarded_green_function",
    "curved_convention_declaration",
    "covariant_conservation_check",
    "curved_ctp_action_terms",
    "flat_limit_check",
    "frw_scalar_mode_compatibility",
    "phi_munu_curved_integral_form",
    "phi_munu_curved_operator_form",
    "curved_verify",
    # FRW explicit (Priority 2C)
    "beyond_wkb_correction_magnitude_today",
    "box_g_on_scalar_fourier_mode",
    "chi_FRW_WKB",
    "chi_FRW_WKB_in_physical_wavenumber",
    "conformal_hubble",
    "conformal_time_FRW_metric",
    "frw_convention_declaration",
    "n_g_squared_FRW_WKB",
    "n_g_squared_FRW_in_physical_wavenumber",
    "n_g_squared_numeric",
    "relaxation_operator_on_scalar_fourier",
    "sub_horizon_limit",
    "super_horizon_limit",
    "transition_wavelength_today_Mpc",
    "transition_wavenumber",
    "transition_wavenumber_today_inverse_meters",
    "frw_verify",
    # Priority 3 closure — MG-EFT mapping
    "mg_eft_convention_declaration",
    "gamma_GRUT",
    "gauge_invariance_check_three_gauges",
    "mu_GRUT",
    "mu_GRUT_numeric",
    "mu_minus_one_GRUT_at_DC",
    "mu_minus_one_at_super_horizon_today",
    "mu_minus_one_at_transition_today",
    "observational_constraints_today",
    "omega_effective_for_cosmological_mode",
    "omega_tau_0_dimensionless_argument",
    "mg_eft_verify",
]
