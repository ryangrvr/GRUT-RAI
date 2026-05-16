"""Refusal report generator for external audit requests."""

from typing import Dict, List


def generate_refusal_report(requested_task: str) -> Dict[str, object]:
    blocked = {
        "compute_full_3loop_s4_ctp": (
            "Full 3-loop S4 CTP evaluation is not available.",
            ["run Stage 3E cross-checks", "review Stage 3D scheme audit"],
            ["explicit loop integrals", "explicit subtraction", "independent replication"],
        ),
        "promote_r_route": (
            "R-route promotion is forbidden in Stage 3F.",
            ["review ladder limitations", "await Stage 4 scope"],
            ["independent replication", "full 3-loop evaluation"],
        ),
        "derive_r_native": (
            "Native R derivation is out of scope for Stage 3F.",
            ["audit current R posture", "maintain scheme alignment"],
            ["explicit TT propagator", "renormalized finite parts"],
        ),
        "evaluate_tensor_harmonic_spectrum": (
            "Tensor harmonic spectrum is not benchmarked.",
            ["use structural placeholders", "document limits"],
            ["explicit TT spectrum benchmark"],
        ),
    }
    reason, alternatives, required = blocked.get(
        requested_task,
        (
            "Requested task is outside current audit scope.",
            ["use scaffolded reports"],
            ["stage-gated promotion requirements"],
        ),
    )
    return {
        "requested_task": requested_task,
        "can_do": False,
        "current_status": "refused",
        "reason_for_refusal": reason,
        "available_alternatives": alternatives,
        "required_before_allowed": required,
        "promotes_claims": False,
    }
