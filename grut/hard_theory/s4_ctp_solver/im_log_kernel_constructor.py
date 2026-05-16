"""Construct Im log(-Box - i epsilon) nonlocal kernel candidates."""

from typing import Dict


def build_im_log_kernel_candidate(extraction_report: Dict[str, object]) -> Dict[str, object]:
    marker_map = extraction_report.get("marker_map", {})
    marker_present = bool(marker_map.get("log_minus_box_i_epsilon_placeholder"))

    if not marker_present:
        return {
            "status": "blocked",
            "reason": "marker_missing",
            "target": "Im_log_minus_box_i_epsilon",
            "promotes_claims": False,
        }

    candidate = {
        "kernel_id": "im_log_minus_box_i_epsilon_candidate",
        "nonlocal_form": "Im log(-Box - i epsilon)",
        "coefficient": "symbolic_uncomputed",
        "source": "ctp_imaginary_sector",
        "scaffold_only": False,
        "finite_extractability": False,
        "protected_source_claimed": False,
        "promotes_claims": False,
    }

    return {
        "status": "constructed",
        "target": "Im_log_minus_box_i_epsilon",
        "candidate": candidate,
        "promotes_claims": False,
    }
