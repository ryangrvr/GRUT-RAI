"""Audit protected quotient equivalence resolution outputs."""

from typing import Dict, Iterable, List


_FORBIDDEN_KEYS = {
    "numeric_value",
    "ratio_value",
    "r_value",
    "coefficient_value",
    "computed_value",
}


def _collect_nonnull(payload: Dict[str, object], keys: Iterable[str]) -> List[str]:
    violations: List[str] = []
    for key in keys:
        if key in payload and payload.get(key) is not None:
            violations.append(key)
    return violations


def audit_ratio_equivalence_resolution(
    ratios: List[Dict[str, object]],
    equivalence_report: Dict[str, object],
    unique_ratio_exists: bool,
) -> Dict[str, object]:
    violations: List[str] = []

    for ratio in ratios:
        violations.extend(_collect_nonnull(ratio, _FORBIDDEN_KEYS))
        pair = ratio.get("pair", {})
        if isinstance(pair, dict):
            for side in (pair.get("left", {}), pair.get("right", {})):
                if isinstance(side, dict):
                    violations.extend(_collect_nonnull(side, _FORBIDDEN_KEYS))
        symbolic_r = ratio.get("symbolic_r", {})
        if isinstance(symbolic_r, dict):
            violations.extend(_collect_nonnull(symbolic_r, _FORBIDDEN_KEYS))

    status = "valid" if not violations else "invalid"

    return {
        "audit": "protected_quotient_equivalence_resolution",
        "status": status,
        "violations": sorted(set(violations)),
        "can_advance_to_coefficient_symbol_binding": bool(unique_ratio_exists) and status == "valid",
        "can_compute_numeric_r": False,
        "can_claim_r": False,
        "promotes_claims": False,
    }
