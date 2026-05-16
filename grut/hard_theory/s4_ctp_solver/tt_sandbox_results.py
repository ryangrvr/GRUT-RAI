"""Validation for sandbox tensor contractions."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.tt_sandbox_rules import (
    define_sandbox_contraction_rules,
)


def validate_sandbox_results(results: Dict[str, object]) -> Dict[str, object]:
    rules = define_sandbox_contraction_rules()
    allowed = set(rules.get("allowed", []))
    forbidden = set(rules.get("forbidden", []))
    issues: List[str] = []

    contractions = results.get("contractions_run", [])
    for entry in contractions:
        rule = entry.get("rule", "")
        expression = entry.get("expression", "")
        if rule not in allowed:
            issues.append(f"rule_not_allowed:{rule}")
        lowered = f"{rule} {expression}".lower()
        for marker in forbidden:
            if marker in lowered:
                issues.append(f"forbidden_marker:{marker}")

    if results.get("unresolved_free_indices"):
        issues.append("unresolved_free_indices")

    if results.get("propagators_evaluated") is not False:
        issues.append("propagators_evaluated")

    if results.get("full_contractions_performed") is not False:
        issues.append("full_contractions_performed")

    if results.get("finite_parts_computed") is not False:
        issues.append("finite_parts_computed")

    if results.get("extraction_performed") is not False:
        issues.append("extraction_performed")

    status = "valid_sandbox" if not issues else "invalid_sandbox"

    return {
        "validation": "tt_sandbox_results",
        "status": status,
        "issues": issues,
        "promotes_claims": False,
    }
