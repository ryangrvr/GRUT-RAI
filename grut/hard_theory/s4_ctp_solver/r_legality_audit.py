"""Audit R legality inputs to enforce no computation."""

from typing import Dict, Iterable, List


_FORBIDDEN_KEYS = {
    "ratio_value",
    "r_value",
    "numeric_value",
    "computed_value",
    "finite_part",
    "computed",
    "value",
}


def _collect_values(payload: Dict[str, object], keys: Iterable[str]) -> List[str]:
    violations: List[str] = []
    for key in keys:
        if key in payload and payload.get(key) is not None:
            violations.append(key)
    return violations


def audit_r_legality_inputs(
    pair: Dict[str, object],
    structural: Dict[str, object],
    cancellation: Dict[str, object],
) -> Dict[str, object]:
    violations = []
    for payload in (pair, pair.get("numerator", {}), pair.get("denominator", {})):
        if isinstance(payload, dict):
            violations.extend(_collect_values(payload, _FORBIDDEN_KEYS))

    for payload in (structural, cancellation):
        if isinstance(payload, dict):
            violations.extend(_collect_values(payload, _FORBIDDEN_KEYS))

    violations = sorted(set(violations))
    status = "valid" if not violations else "invalid"

    return {
        "audit": "r_legality",
        "status": status,
        "violations": violations,
        "promotes_claims": False,
    }
