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

    frw_gaussian_path_integral — Phase 2D. FRW Gaussian path integral
        deriving G^R(k, η) from first principles. Closes
        `constitutive_growth_poisson_closure_gap`. Key result:
            G^R(k, η) = 1 / [1 + (τ_0 k_phys(η))²]
        Exact in QSA on FRW — a⁴ volume factors cancel in the Gaussian
        integration; no a(η)-dependent corrections. Confirms Phase 2C
        WKB result via independent route. 26 tests passing.

    modified_growth — Priority 3.1. Modified linear growth equation
        δ'' + [2 - (3/2)Ω_m] δ' - (3/2) Ω_m μ_GRUT(k, N) δ = 0.
        Numerical integration for canonical k modes, growth-factor
        enhancement f_GRUT(k) = D_GRUT(z=0, k) / D_ΛCDM(z=0).
        Key results: σ_8 scale (k = 0.5 Mpc⁻¹) gets 0.09% enhancement
        — does NOT break σ_8 measurements. BAO scale gets ~8.5%, CMB
        horizon ~135% — testable with DESI Y3+ / Euclid. Honest
        verdict: "GRUT survives the σ_8-scale sanity check; predicts
        a definite testable signal at large scales."

Scope:
    Priority 2A — flat-space derivation: COMPUTED.
    Priority 2B — curved-background scaffold: ANCHORED with four
        structural checks.
    Priority 2C — explicit FRW χ_FRW(k, η) and n_g²(k, η): COMPUTED
        at WKB level.
    Phase 2D — FRW Gaussian path integral: DERIVED. G^R = 1/(1+(τ₀k_phys)²)
        exact in QSA on FRW. a⁴ factors cancel in Gaussian integration.
        Closes `constitutive_growth_poisson_closure_gap`. 26 tests passing.
    Priority 3 — n_g(ω) covariance: CLOSED. ω → k_phys × c, gauge-
        invariant at WKB, mapped to μ(k, a) / γ(k, a) MG-EFT
        parameterization. cmb_boltzmann_scoping now has a well-
        defined ω; Boltzmann-code implementation is downstream
        (not a theoretical gap).
    Priority 3.1 — modified linear growth equation: COMPUTED.
        Numerical D(z, k) integration with μ_GRUT(k, a). σ_8 scale
        unchanged at 0.1% level (does not break S_8 tension); large
        scales enhanced (~135% at CMB horizon, testable but not yet
        ruled out).

Honest framing: the cosmology backbone produces n_g²(k, η)
explicitly, maps to the standard MG-EFT framework, and the linear
growth-factor analysis lands the first-look verdict that GRUT
survives the σ_8 sanity check while predicting a definite signal
at large scales. Full Boltzmann pipeline (CAMB/CLASS modification)
remains the downstream observational-comparison task.
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
from grut.derivation.phi_munu.frw_gaussian_path_integral import (
    G_R_agrees_with_wkb,
    G_R_qsa,
    a_cancellation_check,
    beyond_qsa_correction_estimate,
    convention_declaration as phase2d_convention_declaration,
    coupling_source_per_mode,
    coupling_vertex,
    gaussian_completion_on_shell_sigma,
    modified_poisson_from_path_integral,
    mu_GRUT_from_path_integral,
    quadratic_kernel,
    quadratic_kernel_factored,
    s_gradient_kinetic_per_mode,
    s_relaxation_mass_per_mode,
    verify as phase2d_verify,
)
from grut.derivation.phi_munu.modified_growth import (
    convention_declaration as modified_growth_convention_declaration,
    growing_mode_enhancement_per_efold,
    growing_mode_exponent,
    growing_mode_exponent_numeric,
    growth_enhancement_survey,
    growth_factor_enhancement,
    honest_assessment_summary,
    integrate_growth_factor,
    modified_growth_equation_symbolic,
    verify as modified_growth_verify,
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
    # Phase 2D — FRW Gaussian path integral (G^R derived, June 2026)
    "G_R_agrees_with_wkb",
    "G_R_qsa",
    "a_cancellation_check",
    "beyond_qsa_correction_estimate",
    "phase2d_convention_declaration",
    "coupling_source_per_mode",
    "coupling_vertex",
    "gaussian_completion_on_shell_sigma",
    "modified_poisson_from_path_integral",
    "mu_GRUT_from_path_integral",
    "quadratic_kernel",
    "quadratic_kernel_factored",
    "s_gradient_kinetic_per_mode",
    "s_relaxation_mass_per_mode",
    "phase2d_verify",
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
    # Priority 3.1 — modified linear growth
    "modified_growth_convention_declaration",
    "growing_mode_enhancement_per_efold",
    "growing_mode_exponent",
    "growing_mode_exponent_numeric",
    "growth_enhancement_survey",
    "growth_factor_enhancement",
    "honest_assessment_summary",
    "integrate_growth_factor",
    "modified_growth_equation_symbolic",
    "modified_growth_verify",
]
