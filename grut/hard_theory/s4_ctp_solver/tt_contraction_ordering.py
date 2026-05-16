"""Ordering protocol for TT contraction readiness."""

from typing import Dict, List


def define_contraction_ordering_protocol() -> Dict[str, object]:
    steps: List[str] = [
        "apply_tt_projector_structurally",
        "remove_gauge_zero_modes",
        "pair_tensor_indices",
        "check_ward_constraints",
        "allow_future_sandbox_contraction",
    ]

    return {
        "protocol_id": "tt_contraction_ordering_v1",
        "steps": steps,
        "allows_contraction_now": False,
        "status": "protocol_defined",
        "promotes_claims": False,
    }
