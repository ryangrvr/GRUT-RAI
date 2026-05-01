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

Scope:
    Priority 2A — flat-space derivation: COMPUTED.
    Priority 2B — curved-background scaffold: ANCHORED with four
        structural checks.
    Priority 2C — explicit FRW χ_FRW(k, η) and n_g²(k, η): COMPUTED
        at WKB level. Beyond-WKB (Phase 2D) deferred — corrections
        are negligibly small for post-equality cosmology.

Honest framing: the cosmology backbone now produces n_g²(k, η)
explicitly. Priority 3 inserts this into the linearized Einstein
equations on FRW to derive observable consequences (CMB, structure
formation, primordial spectrum amplitudes).
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
]
