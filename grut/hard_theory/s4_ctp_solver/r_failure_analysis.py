"""Provide next-action hints for R result classification."""

from typing import Dict


_ACTIONS = {
    "valid_symbolic_candidate": "retain_symbolic_candidate_only",
    "blocked_by_legality": "resolve_stage12c_legality",
    "blocked_by_validation": "address_validation_failures",
    "blocked_by_audit": "resolve_audit_violations",
    "ambiguous_symbolic_result": "complete_cancellation_and_isolation",
    "failed_extraction": "recheck_symbolic_pipeline_inputs",
}


def analyze_r_failure(classification: str) -> Dict[str, object]:
    return {
        "next_required_action": _ACTIONS.get(classification, "review_stage12d_inputs"),
        "promotes_claims": False,
    }
