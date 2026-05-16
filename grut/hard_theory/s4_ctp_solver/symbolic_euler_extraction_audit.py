"""Audit OR6 symbolic Euler extraction output."""

from typing import Dict, List, Optional


def audit_symbolic_euler_extraction(
    symbolic_ratio: Dict[str, object],
    guard: Optional[Dict[str, object]] = None,
) -> Dict[str, object]:
    failures: List[str] = []

    if symbolic_ratio.get("numeric_value") is not None:
        failures.append("numeric_value_present")
    if symbolic_ratio.get("physical_value_claimed") is True:
        failures.append("physical_value_claimed")
    if symbolic_ratio.get("promotes_claims") is True:
        failures.append("promotes_claims")

    if guard and guard.get("scheme_guard_passed") is False:
        failures.append("scheme_guard_failed")

    return {
        "status": "pass" if not failures else "fail",
        "failures": sorted(set(failures)),
        "promotes_claims": False,
    }
