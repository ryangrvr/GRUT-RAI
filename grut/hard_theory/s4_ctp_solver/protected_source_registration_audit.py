"""Audit protected source registrations for guardrails."""

from __future__ import annotations

from typing import Dict, List


def audit_protected_source_registration(
    registered: List[Dict[str, object]]
) -> Dict[str, object]:
    failures: List[str] = []

    for entry in registered:
        if entry.get("coefficient_value") is not None:
            failures.append("coefficient_value_present")
        if entry.get("physical_coefficient_claimed") is True:
            failures.append("physical_coefficient_claimed")
        if entry.get("nonlocal_form_present") is not True:
            failures.append("nonlocal_form_missing")
        if entry.get("counterterm_nonmixing_verified") is not True:
            failures.append("nonmixing_missing")
        if entry.get("finite_extractability") is not True:
            failures.append("finite_extractability_missing")

    return {
        "status": "pass" if not failures else "fail",
        "failures": failures,
        "promotes_claims": False,
    }
