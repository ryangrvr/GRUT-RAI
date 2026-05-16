"""Construct curvature log(Box) kernel candidates."""

from typing import Dict, List, Tuple


def _build_candidate(
    kernel_id: str,
    nonlocal_form: str,
    target: str,
) -> Dict[str, object]:
    return {
        "kernel_id": kernel_id,
        "nonlocal_form": nonlocal_form,
        "coefficient": "symbolic_uncomputed",
        "source": "curvature_sector",
        "scaffold_only": False,
        "finite_extractability": False,
        "protected_source_claimed": False,
        "promotes_claims": False,
    }


def build_curvature_log_candidates(
    extraction_report: Dict[str, object]
) -> Tuple[List[Dict[str, object]], List[Dict[str, object]]]:
    marker_map = extraction_report.get("marker_map", {})

    candidates: List[Dict[str, object]] = []
    blocked: List[Dict[str, object]] = []

    if marker_map.get("R_log_box_R"):
        candidates.append(
            {
                "target": "R_log_box_R",
                "candidate": _build_candidate(
                    "r_log_box_r_candidate",
                    "R log(Box) R",
                    "R_log_box_R",
                ),
                "promotes_claims": False,
            }
        )
    else:
        blocked.append(
            {
                "status": "blocked",
                "reason": "marker_missing",
                "target": "R_log_box_R",
                "promotes_claims": False,
            }
        )

    if marker_map.get("Weyl_log_box_Weyl"):
        candidates.append(
            {
                "target": "Weyl_log_box_Weyl",
                "candidate": _build_candidate(
                    "weyl_log_box_weyl_candidate",
                    "Weyl log(Box) Weyl",
                    "Weyl_log_box_Weyl",
                ),
                "promotes_claims": False,
            }
        )
    else:
        blocked.append(
            {
                "status": "blocked",
                "reason": "marker_missing",
                "target": "Weyl_log_box_Weyl",
                "promotes_claims": False,
            }
        )

    return candidates, blocked
