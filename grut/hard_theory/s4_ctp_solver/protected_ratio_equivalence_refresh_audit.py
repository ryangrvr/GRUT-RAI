"""Audit protected ratio equivalence refresh."""

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


def audit_equivalence_refresh(
    refreshed_ratios: List[Dict[str, object]],
    equivalence_report: Dict[str, object],
    unique_equivalence_class_exists: bool,
) -> Dict[str, object]:
    violations: List[str] = []

    for ratio in refreshed_ratios:
        violations.extend(_collect_nonnull(ratio, _FORBIDDEN_KEYS))
        if ratio.get("manual_equivalence_override") is True:
            violations.append("manual_equivalence_override")
        if ratio.get("promotes_claims") is True:
            violations.append("promotes_claims")
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
        "audit": "equivalence_refresh",
        "status": status,
        "violations": sorted(set(violations)),
        "can_advance_to_coefficient_symbol_binding": bool(unique_equivalence_class_exists)
        and status == "valid",
        "can_compute_numeric_r": False,
        "can_claim_r": False,
        "promotes_claims": False,
    }
