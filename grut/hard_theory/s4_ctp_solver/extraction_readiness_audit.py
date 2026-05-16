"""Audit extraction readiness against the legal criteria."""

from typing import Dict, List


def audit_extraction_readiness(candidate: Dict[str, object], criteria: Dict[str, object]) -> Dict[str, object]:
    criteria_list: List[str] = list(criteria.get("criteria", []))
    criteria_satisfied: List[str] = []
    criteria_missing: List[str] = list(criteria_list)

    return {
        "candidate_id": candidate.get("candidate_id", "unknown_candidate"),
        "criteria_satisfied": criteria_satisfied,
        "criteria_missing": criteria_missing,
        "extraction_allowed": False,
        "reason": "insufficient_conditions",
        "promotes_claims": False,
    }
