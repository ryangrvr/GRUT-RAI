"""Audit R extraction attempt for forbidden steps."""

from typing import Dict, Iterable, List


_FORBIDDEN_KEYS = {
    "manual_step",
    "manual_override",
    "inserted_parameter",
    "numeric_value",
    "value",
    "computed",
    "finite_part",
    "ratio_value",
}


def _collect_violations(payload: Dict[str, object], keys: Iterable[str]) -> List[str]:
    violations: List[str] = []
    for key in keys:
        if key in payload and payload.get(key) is not None:
            violations.append(key)
    return violations


def audit_r_extraction(
    symbolic_r: Dict[str, object],
    cancellation: Dict[str, object],
    validation: Dict[str, object],
) -> Dict[str, object]:
    violations = []
    for payload in (symbolic_r, cancellation, validation):
        if isinstance(payload, dict):
            violations.extend(_collect_violations(payload, _FORBIDDEN_KEYS))

    if cancellation.get("cancellation_valid") is not True:
        violations.append("cancellation_incomplete")
    if validation.get("valid") is not True:
        violations.append("validation_failed")

    violations = sorted(set(violations))
    status = "valid" if not violations else "invalid"

    return {
        "audit": "r_extraction",
        "status": status,
        "violations": violations,
        "promotes_claims": False,
    }
