"""Projector consistency checks for TT contractions."""

from typing import Dict, List


def check_tt_projector_consistency(tt_results: List[Dict[str, object]]) -> Dict[str, object]:
    projector_ids = [
        result.get("projector", {}).get("projector_id") for result in tt_results
    ]
    projector_present = all(pid == "tt_projector_extended" for pid in projector_ids)
    projector_positions_valid = projector_present and bool(tt_results)

    return {
        "projector_consistency": projector_positions_valid,
        "projector_positions_valid": projector_positions_valid,
        "projector_required": True,
        "promotes_claims": False,
    }
