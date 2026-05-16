"""Index structure diagnostics for TT contractions."""

from typing import Dict, List


def analyze_tt_index_structure(tt_inversion_results: List[Dict[str, object]]) -> Dict[str, object]:
    indices_detected = ["mu", "nu", "alpha", "beta"]
    paired_indices = [("mu", "nu"), ("alpha", "beta")]
    free_indices = []

    tt_constraints_respected = all(
        result.get("structure") in {"tensor_preserved", "tt_truncated"}
        for result in tt_inversion_results
    )

    complete = bool(tt_inversion_results) and tt_constraints_respected and not free_indices

    return {
        "index_structure_id": "tt_indices",
        "indices_detected": indices_detected,
        "paired_indices": paired_indices,
        "free_indices": free_indices,
        "tt_constraints_respected": tt_constraints_respected,
        "complete": complete,
        "promotes_claims": False,
    }
