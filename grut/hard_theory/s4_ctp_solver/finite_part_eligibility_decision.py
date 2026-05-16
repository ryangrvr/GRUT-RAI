"""Eligibility decision logic for finite-part computation."""

from typing import Dict, List


def decide_finite_part_eligibility(
    readiness: Dict[str, object],
    blockers: Dict[str, object],
    threshold: float = 0.95,
) -> Dict[str, object]:
    scheme_alignment = readiness.get("scheme_alignment_ok", False)
    readiness_score = readiness.get("readiness_score", 0.0)
    blocker_list: List[str] = blockers.get("blockers", [])

    eligible = (
        not blocker_list
        and readiness_score >= threshold
        and scheme_alignment
    )

    if eligible:
        reason = "All prerequisites satisfied for finite-part attempt."
        conditions_required: List[str] = []
    else:
        reason = "Prerequisites not satisfied for finite-part attempt."
        conditions_required = blocker_list

    return {
        "eligible": eligible,
        "reason": reason,
        "conditions_required": conditions_required,
        "can_proceed_to_stage8": eligible,
        "promotes_claims": False,
    }
