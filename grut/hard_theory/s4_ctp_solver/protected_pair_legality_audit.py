"""Audit protected pair legality guardrails."""

from __future__ import annotations

from typing import Dict, List


def audit_protected_pair_legality(
    pair: Dict[str, object],
    scheme_protected_candidates: List[Dict[str, object]],
) -> Dict[str, object]:
    failures: List[str] = []
    allowed_ids = {entry.get("candidate_id") for entry in scheme_protected_candidates}

    for side in ("left", "right"):
        candidate = pair.get(side, {})
        candidate_id = candidate.get("candidate_id")
        if candidate_id not in allowed_ids:
            failures.append("unprotected_candidate_used")
        if candidate.get("coefficient_value") is not None:
            failures.append("coefficient_value_present")

    return {
        "pair_id": pair.get("pair_id"),
        "status": "pass" if not failures else "fail",
        "failures": failures,
        "promotes_claims": False,
    }
