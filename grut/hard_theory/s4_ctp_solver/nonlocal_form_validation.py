"""Validate nonlocal form candidates without promoting claims."""

from typing import Dict, List


def validate_nonlocal_form_candidate(candidate: Dict[str, object]) -> Dict[str, object]:
    failures: List[str] = []

    nonlocal_form = candidate.get("nonlocal_form")
    if not isinstance(nonlocal_form, str) or not nonlocal_form.strip():
        failures.append("nonlocal_form_missing")

    if candidate.get("coefficient") != "symbolic_uncomputed":
        failures.append("coefficient_not_symbolic")

    if candidate.get("protected_source_claimed") is not False:
        failures.append("protected_source_claimed")

    if candidate.get("scaffold_only") is not False:
        failures.append("scaffold_only")

    if candidate.get("finite_extractability") is not False:
        failures.append("finite_extractability_claimed")

    return {
        "status": "pass" if not failures else "fail",
        "failures": failures,
        "promotes_claims": False,
    }
