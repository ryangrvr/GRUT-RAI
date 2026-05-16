"""Audit scheme injection for protected source candidates."""

from __future__ import annotations

from typing import Dict, List


def audit_protected_source_scheme_injection(
    injected: List[Dict[str, object]],
    stage_p6: Dict[str, object],
) -> Dict[str, object]:
    failures: List[str] = []

    registered_ids = {
        entry.get("protected_source_candidate_id")
        for entry in stage_p6.get("registered_candidates", [])
    }

    for entry in injected:
        candidate_id = entry.get("candidate_id")
        if candidate_id not in registered_ids:
            failures.append("unregistered_candidate_injected")
        if entry.get("coefficient_value") is not None:
            failures.append("coefficient_value_present")
        if entry.get("physical_coefficient_computed") is True:
            failures.append("physical_coefficient_computed")

    return {
        "status": "pass" if not failures else "fail",
        "failures": failures,
        "promotes_claims": False,
    }
