"""TT graviton propagator scaffold on S4 (structural)."""

from typing import Dict, List


def build_tt_propagator_scaffold(
    operator: Dict[str, object],
    projector: Dict[str, object],
) -> Dict[str, object]:
    limitations: List[str] = [
        "operator_not_inverted",
        "spectral_sum_not_performed",
        "no_mode_by_mode_solution",
    ]
    mode_labels = {
        "spectra_id": "s4_harmonic_spectra",
        "mode": "TT_placeholder",
        "status": "structural_only",
    }
    projector_labels = {
        "projector_id": "P_TT_l",
        "harmonic_mode": "TT_placeholder",
        "summation_performed": False,
        "inversion_performed": False,
        "status": "projector_label_structural",
    }

    return {
        "propagator_id": "s4_tt_propagator_scaffold",
        "structure": "P_TT * inverse_operator_placeholder * P_TT",
        "operator": operator.get("operator_id"),
        "projector": projector.get("projector_id"),
        "inverse_operator": "inverse_operator_placeholder",
        "mode_labels": mode_labels,
        "projector_labels": projector_labels,
        "status": "scaffold_not_evaluated",
        "limitations": limitations,
        "promotes_claims": False,
    }
