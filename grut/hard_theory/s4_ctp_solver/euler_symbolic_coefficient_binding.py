"""Bind Euler-channel coefficient symbols to protected candidates."""

from typing import Dict, List, Optional

from grut.hard_theory.s4_ctp_solver.euler_coefficient_roles import (
    build_euler_coefficient_roles,
)

_BLOCKED_KERNEL_REASONS = {
    "Weyl_log_box_Weyl": "weyl_zero_on_s4",
    "Im_log_minus_box_i_epsilon": "ctp_to_euler_bridge_missing",
}


def _registered_map(stage_p7: Dict[str, object]) -> Dict[str, Dict[str, object]]:
    stage_p6 = stage_p7.get("stage_p6", {})
    return {
        entry.get("protected_source_candidate_id"): entry
        for entry in stage_p6.get("registered_candidates", [])
    }


def _protected_candidates(stage_p7: Dict[str, object]) -> List[Dict[str, object]]:
    protected = stage_p7.get("scheme_protected_candidates", [])
    registered = _registered_map(stage_p7)
    candidates: List[Dict[str, object]] = []

    for entry in protected:
        candidate_id = entry.get("candidate_id")
        registered_entry = registered.get(candidate_id)
        if registered_entry:
            candidates.append(registered_entry)

    return candidates


def _binding_entry(
    role_id: str,
    source_type: Optional[str],
    kernel_id: Optional[str],
    coefficient_symbol: Optional[str],
    status: str,
    blocking_reason: Optional[str],
) -> Dict[str, object]:
    return {
        "role_id": role_id,
        "source_type": source_type,
        "kernel_id": kernel_id,
        "coefficient_symbol": coefficient_symbol,
        "coefficient_value": None,
        "status": status,
        "blocking_reason": blocking_reason,
        "promotes_claims": False,
    }


def bind_euler_coefficient_symbols(
    or4_report: Dict[str, object],
    or3_report: Dict[str, object],
    stage_p7: Dict[str, object],
) -> Dict[str, object]:
    roles = build_euler_coefficient_roles()
    bindings: List[Dict[str, object]] = []
    binding_blockers: List[str] = []

    if or4_report.get("can_advance_to_euler_coefficient_symbol_binding") is not True:
        binding_blockers.append("or4_gate_blocked")
    if or3_report.get("euler_channel_available") is not True:
        binding_blockers.append("euler_channel_unavailable")

    allowed_kernels = {
        entry.get("source_type")
        for entry in or4_report.get("allowed_kernel_roles", [])
        if entry.get("source_type")
    }
    if not allowed_kernels:
        allowed_kernels = {role.get("allowed_kernel") for role in roles}

    candidates = _protected_candidates(stage_p7)

    for candidate in candidates:
        source_type = candidate.get("source_type")
        kernel_id = candidate.get("kernel_id")
        if candidate.get("coefficient_value") is not None:
            bindings.append(
                _binding_entry(
                    "disallowed_candidate",
                    source_type,
                    kernel_id,
                    None,
                    "blocked",
                    "coefficient_value_present",
                )
            )
            continue

        if source_type not in allowed_kernels:
            bindings.append(
                _binding_entry(
                    "disallowed_candidate",
                    source_type,
                    kernel_id,
                    None,
                    "blocked",
                    _BLOCKED_KERNEL_REASONS.get(source_type, "kernel_not_allowed"),
                )
            )

    role_bindings: List[Dict[str, object]] = []

    for role in roles:
        if binding_blockers:
            role_bindings.append(
                _binding_entry(
                    role.get("role_id"),
                    role.get("allowed_kernel"),
                    None,
                    role.get("coefficient_symbol"),
                    "unbound",
                    binding_blockers[0],
                )
            )
            continue

        target = None
        for candidate in candidates:
            if candidate.get("source_type") == role.get("allowed_kernel"):
                target = candidate
                break

        if target is None:
            role_bindings.append(
                _binding_entry(
                    role.get("role_id"),
                    role.get("allowed_kernel"),
                    None,
                    role.get("coefficient_symbol"),
                    "unbound",
                    "candidate_missing",
                )
            )
            continue

        role_bindings.append(
            _binding_entry(
                role.get("role_id"),
                target.get("source_type"),
                target.get("kernel_id"),
                role.get("coefficient_symbol"),
                "bound",
                None,
            )
        )

    bindings.extend(role_bindings)

    binding_complete = all(entry.get("status") == "bound" for entry in role_bindings)
    symbolic_ratio_form = "C_Euler_num / C_Euler_den" if binding_complete else None

    return {
        "bindings": bindings,
        "binding_complete": binding_complete,
        "symbolic_ratio_form": symbolic_ratio_form,
        "can_advance_to_symbolic_euler_extraction": binding_complete,
        "binding_blockers": binding_blockers,
        "promotes_claims": False,
    }
