"""Projection-domain rules for OR6 symbolic Euler extraction."""

from typing import Dict, List

_ALLOWED_KERNEL = "R_log_box_R"
_BLOCKED_KERNELS = {"Weyl_log_box_Weyl", "Im_log_minus_box_i_epsilon"}


def evaluate_projection_guard(
    or4_report: Dict[str, object],
    or3_report: Dict[str, object],
) -> Dict[str, object]:
    failures: List[str] = []

    if or4_report.get("definition_domain") != "round_s4_euler_anomaly_channel":
        failures.append("definition_domain_mismatch")

    if or3_report.get("euler_channel_available") is not True:
        failures.append("euler_channel_unavailable")

    allowed_roles = or4_report.get("allowed_kernel_roles", [])
    allowed_sources = {
        entry.get("source_type") for entry in allowed_roles if entry.get("source_type")
    }
    if _ALLOWED_KERNEL not in allowed_sources:
        failures.append("allowed_kernel_missing")

    blocked_roles = or4_report.get("blocked_kernel_roles", [])
    blocked_sources = {
        entry.get("source_type") for entry in blocked_roles if entry.get("source_type")
    }
    if not _BLOCKED_KERNELS.issubset(blocked_sources):
        failures.append("blocked_kernel_missing")

    return {
        "projection_guard_passed": not failures,
        "projection_failures": failures,
        "projection_domain": "round_s4_euler_channel",
        "allowed_kernel": _ALLOWED_KERNEL,
        "blocked_kernels": sorted(_BLOCKED_KERNELS),
        "promotes_claims": False,
    }
