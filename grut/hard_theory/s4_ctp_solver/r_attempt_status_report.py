"""Build a human-readable status report for the R attempt."""

from typing import Dict


def _publishable_reason(classification: str) -> str:
    if classification == "valid_symbolic_candidate":
        return "symbolic_candidate_only"
    if classification == "blocked_by_legality":
        return "legality_blocked"
    if classification == "blocked_by_validation":
        return "validation_failed"
    if classification == "blocked_by_audit":
        return "audit_failed"
    if classification == "ambiguous_symbolic_result":
        return "cancellation_or_isolation_incomplete"
    return "extraction_failed"


def _blocking_reason(
    classification: str, stage12c: Dict[str, object], stage12d: Dict[str, object]
) -> str:
    if classification == "blocked_by_legality":
        return stage12c.get("blocking_reason", "legality_blocked")
    if classification == "blocked_by_validation":
        return "validation_failed"
    if classification == "blocked_by_audit":
        return "audit_failed"
    if classification == "ambiguous_symbolic_result":
        return "cancellation_or_isolation_incomplete"
    if classification == "valid_symbolic_candidate":
        return "symbolic_candidate_not_physical"
    failure_reason = stage12d.get("failure_reason")
    return failure_reason if isinstance(failure_reason, str) else "failed_extraction"


def build_r_attempt_status_report(
    stage12c: Dict[str, object],
    stage12d: Dict[str, object],
    stage12e: Dict[str, object],
) -> Dict[str, object]:
    classification = stage12e.get("classification")
    next_required_action = stage12e.get("next_required_action")

    report = {
        "stage": "12F",
        "status": "r_attempt_status_report",
        "r_physical_result": False,
        "can_publish_r": False,
        "can_claim_r": False,
        "classification": classification,
        "next_required_action": next_required_action,
        "promotes_claims": False,
        "r_legal": stage12c.get("r_legal") is True,
        "r_attempted": stage12d.get("r_attempted") is True,
        "publishable_reason": _publishable_reason(classification),
        "blocking_reason": _blocking_reason(classification, stage12c, stage12d),
    }

    return report
