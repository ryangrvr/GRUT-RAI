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

Scope:
    Priority 2A — flat-space derivation: COMPUTED.
    Priority 2B — curved-background scaffold: ANCHORED with four
        structural checks. Full derivation of P^TT,g and G^R on
        specific backgrounds (S⁴, FRW) deferred to Phase 2C
        specialist work.

Honest framing: the curved-background extension does NOT close
'full nonlinear gravity'. It extends the linearized flat result
to a covariant form with the four physical-consistency checks
required for the framework's posture statement.
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
]
