"""Audit protected quotient selection rule outcomes."""

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


def audit_selection_rules(
    ratios: List[Dict[str, object]],
    rule_reports: List[Dict[str, object]],
) -> Dict[str, object]:
    violations: List[str] = []

    for ratio in ratios:
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

    for rule in rule_reports:
        if rule.get("manual_choice") is True:
            violations.append("manual_choice")
        if rule.get("promotes_claims") is True:
            violations.append("rule_promotes_claims")

    status = "valid" if not violations else "invalid"

    return {
        "audit": "protected_quotient_selection_rule_audit",
        "status": status,
        "violations": sorted(set(violations)),
        "can_compute_numeric_r": False,
        "can_claim_r": False,
        "promotes_claims": False,
    }
