"""Assess R-route legality based on scheme-stability audit."""

from typing import Dict


def assess_r_route_legality(audit: Dict[str, object]) -> Dict[str, object]:
    all_stable = audit.get("all_r_inputs_stable") is True

    if all_stable:
        status = "conditionally_allowed_future"
        reason = "all_r_inputs_stable"
    else:
        status = "blocked"
        reason = "scheme_inputs_unstable"

    return {
        "r_route_status": status,
        "reason": reason,
        "can_compute_r_now": False,
        "can_extract": False,
        "promotes_claims": False,
    }
