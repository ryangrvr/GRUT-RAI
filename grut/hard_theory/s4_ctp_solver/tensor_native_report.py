"""Report renderer for Stage 5C tensor-native attempts."""

from typing import Dict


def render_tensor_native_report(result: Dict[str, object]) -> Dict[str, object]:
    return {
        "topology_id": result.get("topology_id"),
        "tensor_flow_map": result.get("tensor_flow", {}).get("flow_map"),
        "constraints_applied": result.get("constraint_status", {}).get("constraints_applied", []),
        "checks_run": [
            "tensor_flow",
            "tensor_scalar_alignment",
            "tensor_ward",
            "tensor_scheme",
        ],
        "limitations": result.get("limitations", []),
        "promotion_blocked": True,
        "can_proceed": result.get("can_attempt_candidate_extraction", False),
        "cannot_proceed": not result.get("can_attempt_candidate_extraction", False),
    }
