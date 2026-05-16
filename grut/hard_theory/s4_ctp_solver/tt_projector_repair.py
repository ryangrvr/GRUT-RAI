"""Projector placement repair proposals for TT contractions."""

from typing import Dict


def repair_tt_projector_placement(readiness_output: Dict[str, object]) -> Dict[str, object]:
    projector_check = readiness_output.get("projector_check", {})
    projector_positions_repaired = not projector_check.get("projector_consistency", False)

    return {
        "repair": "tt_projector_placement",
        "canonical_form": "P_TT * inverse_operator_placeholder * P_TT",
        "projector_positions_repaired": projector_positions_repaired,
        "projector_evaluated": False,
        "status": "repair_proposed",
        "promotes_claims": False,
    }
