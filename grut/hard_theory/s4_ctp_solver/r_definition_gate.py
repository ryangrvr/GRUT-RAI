"""Gate the formal OR4 R definition against OR3 S4 Euler projections."""

from typing import Dict, List


def _projection_map(kernel_projections: List[Dict[str, object]]) -> Dict[str, Dict[str, object]]:
    mapping: Dict[str, Dict[str, object]] = {}
    for entry in kernel_projections:
        source_type = entry.get("source_type")
        if source_type:
            mapping[source_type] = entry
    return mapping


def _role_entry(source_type: str, role: str, status: str, reason: str | None) -> Dict[str, object]:
    return {
        "source_type": source_type,
        "role": role,
        "status": status,
        "blocking_reason": reason,
        "promotes_claims": False,
    }


def evaluate_formal_r_definition_gate(
    formal_definition: Dict[str, object],
    or3_report: Dict[str, object],
) -> Dict[str, object]:
    kernel_projections = list(or3_report.get("kernel_projections", []))
    euler_channel_available = or3_report.get("euler_channel_available") is True

    projections = _projection_map(kernel_projections)
    r_projection = projections.get("R_log_box_R", {})
    r_projects_to_euler = r_projection.get("projects_to_euler_channel") is True
    r_survives = r_projection.get("survives_on_s4") is True
    r_available = r_projects_to_euler and r_survives

    allowed_kernel_roles: List[Dict[str, object]] = []
    blocked_kernel_roles: List[Dict[str, object]] = []

    if r_available:
        allowed_kernel_roles.append(
            _role_entry(
                "R_log_box_R",
                "euler_channel_anomaly_quotient",
                "allowed",
                None,
            )
        )
    else:
        blocked_kernel_roles.append(
            _role_entry(
                "R_log_box_R",
                "euler_channel_anomaly_quotient",
                "blocked",
                "r_log_box_r_unavailable",
            )
        )

    blocked_kernel_roles.append(
        _role_entry(
            "Weyl_log_box_Weyl",
            "weyl_channel_blocked_on_s4",
            "blocked",
            "weyl_zero_on_s4",
        )
    )

    blocked_kernel_roles.append(
        _role_entry(
            "Im_log_minus_box_i_epsilon",
            "ctp_causal_kernel_blocked",
            "blocked",
            "ctp_to_euler_bridge_missing",
        )
    )

    can_advance = r_available and euler_channel_available

    return {
        "definition_domain": formal_definition.get("definition_domain"),
        "allowed_kernel_roles": allowed_kernel_roles,
        "blocked_kernel_roles": blocked_kernel_roles,
        "can_advance_to_euler_coefficient_symbol_binding": can_advance,
        "can_compute_numeric_r": False,
        "can_claim_r": False,
        "promotes_claims": False,
    }
