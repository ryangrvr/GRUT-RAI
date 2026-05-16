"""Audit for convergence control repair attempt."""

from typing import Dict


def audit_convergence_repair(result: Dict[str, object]) -> Dict[str, object]:
    guard = result.get("guard", {})
    guard_ok = guard.get("guard") == "tensor_placeholder_guard"
    no_proof = result.get("convergence_proven") is False

    status = "valid" if guard_ok and no_proof else "invalid"

    return {
        "audit": "convergence_repair",
        "status": status,
        "blocker_closed": False,
        "can_compute_finite_parts": False,
        "promotes_claims": False,
    }
