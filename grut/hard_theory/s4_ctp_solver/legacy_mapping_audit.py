"""Audit legacy definition mapping for guardrails."""

from typing import Dict, Iterable, List


_FORBIDDEN_VALUE_KEYS = {
    "coefficient_value",
    "numeric_r",
    "r_value",
    "ratio_value",
}


def _has_forbidden_values(entries: Iterable[Dict[str, object]]) -> List[str]:
    failures: List[str] = []
    for entry in entries:
        for key in _FORBIDDEN_VALUE_KEYS:
            if entry.get(key) is not None:
                failures.append(f"forbidden_value:{key}")
    return failures


def audit_legacy_definition_mapping(
    mapped_routes: List[Dict[str, object]],
    blocked_routes: List[Dict[str, object]],
    role_assignments: Dict[str, object],
) -> Dict[str, object]:
    failures: List[str] = []

    failures.extend(_has_forbidden_values(mapped_routes))
    failures.extend(_has_forbidden_values(blocked_routes))

    for route in mapped_routes:
        if route.get("manual_selection") is True:
            failures.append("manual_selection_present")

        if route.get("numerator_role") == "C_Cosmo" or route.get("denominator_role") == "C_Cosmo":
            if role_assignments.get("explicit_cosmo_kernel_present") is not True:
                failures.append("c_cosmo_mapping_without_kernel")

    status = "pass" if not failures else "fail"
    return {
        "status": status,
        "failures": failures,
        "promotes_claims": False,
    }
