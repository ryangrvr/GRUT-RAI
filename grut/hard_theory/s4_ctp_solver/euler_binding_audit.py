"""Audit Euler-channel coefficient symbol bindings."""

from typing import Dict, List


def audit_euler_binding(binding_report: Dict[str, object]) -> Dict[str, object]:
    failures: List[str] = []
    bindings = binding_report.get("bindings", [])

    for entry in bindings:
        if entry.get("coefficient_value") is not None:
            failures.append("coefficient_value_present")
        if entry.get("promotes_claims") is True:
            failures.append("promotes_claims")

    return {
        "status": "pass" if not failures else "fail",
        "failures": sorted(set(failures)),
        "promotes_claims": False,
    }
