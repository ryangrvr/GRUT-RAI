"""Classify the Stage 12D R extraction attempt."""

from typing import Dict


def classify_r_result(stage12c: Dict[str, object], stage12d: Dict[str, object]) -> Dict[str, object]:
    r_legal = stage12c.get("r_legal") is True
    validation = stage12d.get("validation", {})
    audit = stage12d.get("audit", {})
    cancellation = stage12d.get("cancellation", {})
    finite = stage12d.get("finite", {})

    validation_pass = validation.get("valid") is True
    audit_pass = audit.get("status") == "valid"
    r_value = stage12d.get("r_value")
    symbolic_exists = (
        r_value is not None
        or finite.get("finite_structure") is not None
        or stage12d.get("symbolic_r") is not None
    )
    cancellation_ok = cancellation.get("cancellation_valid") is True
    isolation_ok = finite.get("isolation_ok") is True

    if not r_legal:
        classification = "blocked_by_legality"
    elif not validation_pass:
        classification = "blocked_by_validation"
    elif not audit_pass:
        classification = "blocked_by_audit"
    elif symbolic_exists and (not cancellation_ok or not isolation_ok):
        classification = "ambiguous_symbolic_result"
    elif validation_pass and audit_pass and r_value is not None:
        classification = "valid_symbolic_candidate"
    else:
        classification = "failed_extraction"

    return {
        "classification": classification,
        "promotes_claims": False,
    }
