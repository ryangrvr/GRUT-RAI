"""Φ_μν derivation package — Priority 2 of the v2 deposit roadmap.

Closes constitutive_projection_gravity_heuristic_open_question by
deriving the gravitational constitutive correction Φ_μν explicitly
from the variation of the linearized Schwinger-Keldysh action,
δS_CTP / δh_a^μν |_{h_a = 0}.

Submodules:
    linearized_ctp_action — symbolic CTP action setup, variation,
        kernel extraction, and limit verification at the linearized
        (flat-spacetime) level.

Scope: linearized gravity (h_μν perturbations on η_μν Minkowski
background). Curved-background extension to S⁴ / FRW is research-
tier work tracked by phi_munu_curved_background_extension_open_question.
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

__all__ = [
    "constitutive_kernel_fourier",
    "convention_declaration",
    "derive_phi_munu_from_variation",
    "extract_phi_munu_kernel_form",
    "phi_munu_high_freq_limit",
    "phi_munu_low_freq_limit",
    "transverse_traceless_projector",
    "verify",
]
