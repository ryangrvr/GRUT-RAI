"""Dry-run extraction simulation without computing coefficients."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.extraction_criteria import CRITERIA_ITEMS


def perform_extraction_dry_run(candidate: Dict[str, object]) -> Dict[str, object]:
    required_inputs: List[str] = list(CRITERIA_ITEMS)
    missing_inputs: List[str] = list(CRITERIA_ITEMS)

    return {
        "candidate_id": candidate.get("candidate_id", "unknown_candidate"),
        "status": "extraction_not_permitted_dry_run",
        "required_inputs": required_inputs,
        "missing_inputs": missing_inputs,
        "simulated_output": {
            "coefficient": "UNDEFINED",
            "reason": "blocked_by_missing_requirements",
        },
        "promotes_claims": False,
    }
