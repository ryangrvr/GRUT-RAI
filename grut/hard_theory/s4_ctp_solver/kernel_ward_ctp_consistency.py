"""Ward/CTP consistency checks for nonlocal kernel attempts."""

from typing import Dict, List


def _has_ctp_markers(stageN2: Dict[str, object]) -> bool:
    for candidate in stageN2.get("candidate_sources", []):
        indicators = candidate.get("indicators", {})
        if indicators.get("keldysh_ctp") or indicators.get("imaginary_log"):
            return True
    return False


def check_ward_ctp_consistency(
    stage12g: Dict[str, object],
    stageN2: Dict[str, object],
    causal_required: bool,
) -> Dict[str, object]:
    ward_present = bool(stage12g.get("terminal_package"))
    causal_present = _has_ctp_markers(stageN2)

    if not ward_present:
        return {
            "status": "fail",
            "reason": "ward_markers_missing",
            "promotes_claims": False,
        }

    if causal_required and not causal_present:
        return {
            "status": "fail",
            "reason": "ctp_causal_markers_missing",
            "promotes_claims": False,
        }

    return {
        "status": "pass",
        "reason": "ward_ctp_markers_present",
        "promotes_claims": False,
    }
