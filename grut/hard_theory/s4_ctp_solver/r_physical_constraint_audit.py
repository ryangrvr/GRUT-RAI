"""Audit OR2 physical interpretation constraint outputs."""

from typing import Dict, Iterable, List


_FORBIDDEN_KEYS = {
    "numeric_r",
    "r_value",
    "ratio_value",
    "coefficient_value",
}


def _check_forbidden(entries: Iterable[Dict[str, object]]) -> List[str]:
    failures: List[str] = []
    for entry in entries:
        for key in _FORBIDDEN_KEYS:
            if entry.get(key) is not None:
                failures.append(f"forbidden_value:{key}")
    return failures


def audit_physical_constraint(
    route_evaluations: List[Dict[str, object]],
    intent: Dict[str, object],
) -> Dict[str, object]:
    failures: List[str] = []

    failures.extend(_check_forbidden(route_evaluations))
    if intent.get("intent_classification") == "conflicting":
        failures.append("intent_conflicting")

    status = "pass" if not failures else "fail"
    return {
        "status": status,
        "failures": failures,
        "promotes_claims": False,
    }
