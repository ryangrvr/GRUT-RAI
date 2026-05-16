"""Build a blocker ledger for the R route terminal audit."""

from typing import Dict, List


def build_r_route_blocker_ledger(
    stage12c: Dict[str, object],
    stage12d: Dict[str, object],
    stage12e: Dict[str, object],
    stage12f: Dict[str, object],
) -> Dict[str, object]:
    blockers: List[Dict[str, object]] = []

    if stage12c.get("r_legal") is not True:
        blockers.append(
            {
                "blocker_id": "r_legality_blocked",
                "reason": stage12c.get("blocking_reason", "r_legality_blocked"),
                "stage": "12C",
            }
        )

    validation = stage12d.get("validation", {})
    if validation.get("valid") is False:
        blockers.append(
            {
                "blocker_id": "validation_failed",
                "reason": validation.get("reason", "validation_failed"),
                "stage": "12D",
            }
        )

    audit = stage12d.get("audit", {})
    if audit.get("status") == "invalid":
        blockers.append(
            {
                "blocker_id": "audit_failed",
                "reason": audit.get("violations", "audit_failed"),
                "stage": "12D",
            }
        )

    failure_reason = stage12d.get("failure_reason")
    if failure_reason:
        blockers.append(
            {
                "blocker_id": "extraction_failed",
                "reason": failure_reason,
                "stage": "12D",
            }
        )

    classification = stage12e.get("classification")
    if classification in {
        "blocked_by_legality",
        "blocked_by_validation",
        "blocked_by_audit",
        "ambiguous_symbolic_result",
        "failed_extraction",
    }:
        blockers.append(
            {
                "blocker_id": "classification_blocker",
                "reason": classification,
                "stage": "12E",
            }
        )

    blocking_reason = stage12f.get("blocking_reason")
    if blocking_reason:
        blockers.append(
            {
                "blocker_id": "terminal_blocker",
                "reason": blocking_reason,
                "stage": "12F",
            }
        )

    return {
        "blockers": blockers,
        "promotes_claims": False,
    }
