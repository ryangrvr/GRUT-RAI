"""Blocker identification for finite-part eligibility."""

from typing import Dict, List


def identify_finite_part_blockers(readiness: Dict[str, object]) -> Dict[str, object]:
    blockers: List[str] = []
    if not readiness.get("divergence_complete", False):
        blockers.append("unmapped_divergence")
    if not readiness.get("scheme_alignment_ok", False):
        blockers.append("scheme_incomplete")
    if not readiness.get("stability_ok", False):
        blockers.append("instability_detected")
    if not readiness.get("structure_ok", False):
        blockers.append("structure_breakdown")
    if readiness.get("readiness_score", 0.0) < 0.9:
        blockers.append("insufficient_convergence_control")

    if not blockers:
        severity = "low"
    elif len(blockers) >= 3:
        severity = "high"
    else:
        severity = "medium"

    return {
        "blockers": blockers,
        "blocking_severity": severity,
        "promotes_claims": False,
    }
