"""Audit regulator class resolution for protected ratios."""

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


def audit_regulator_class_resolution(
    kernel_regulator_classes: List[Dict[str, object]],
    ratio_regulator_classes: List[Dict[str, object]],
    symbolic_entries: List[Dict[str, object]],
) -> Dict[str, object]:
    violations: List[str] = []

    for entry in kernel_regulator_classes:
        if entry.get("regulator_class") == "regulator_class_unresolved":
            violations.append("kernel_regulator_unresolved")
        if entry.get("promotes_claims") is True:
            violations.append("kernel_promotes_claims")

    for entry in ratio_regulator_classes:
        if entry.get("ratio_regulator_class") != "matched_dimensional_symbolic_preserved":
            violations.append("ratio_regulator_unresolved")
        if entry.get("promotes_claims") is True:
            violations.append("ratio_promotes_claims")

    for entry in symbolic_entries:
        violations.extend(_collect_nonnull(entry, _FORBIDDEN_KEYS))
        pair = entry.get("pair", {})
        if isinstance(pair, dict):
            for side in (pair.get("left", {}), pair.get("right", {})):
                if isinstance(side, dict):
                    violations.extend(_collect_nonnull(side, _FORBIDDEN_KEYS))
        symbolic_r = entry.get("symbolic_r", {})
        if isinstance(symbolic_r, dict):
            violations.extend(_collect_nonnull(symbolic_r, _FORBIDDEN_KEYS))

        if entry.get("promotes_claims") is True:
            violations.append("symbolic_entry_promotes_claims")

    status = "valid" if not violations else "invalid"
    regulator_classes_resolved = status == "valid"

    return {
        "audit": "regulator_class_resolution",
        "status": status,
        "violations": sorted(set(violations)),
        "regulator_classes_resolved": regulator_classes_resolved,
        "can_advance_to_coefficient_symbol_binding": regulator_classes_resolved,
        "can_compute_numeric_r": False,
        "can_claim_r": False,
        "promotes_claims": False,
    }
