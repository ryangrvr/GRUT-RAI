"""Decide legality of constructing R from candidate pairs."""

from typing import Dict


def decide_r_legality(
    pair: Dict[str, object],
    structural: Dict[str, object],
    cancellation: Dict[str, object],
    audit: Dict[str, object],
) -> Dict[str, object]:
    if not pair.get("scheme_stable"):
        return {
            "r_legal": False,
            "reason": "scheme_stability_failed",
            "promotes_claims": False,
        }
    if not pair.get("nonlocal_or_anomaly_protected"):
        return {
            "r_legal": False,
            "reason": "nonlocal_or_anomaly_required",
            "promotes_claims": False,
        }
    if not pair.get("renorm_structure_shared"):
        return {
            "r_legal": False,
            "reason": "renorm_structure_mismatch",
            "promotes_claims": False,
        }
    if not structural.get("compatible"):
        return {
            "r_legal": False,
            "reason": structural.get("reason"),
            "promotes_claims": False,
        }
    if not cancellation.get("cancellation_valid"):
        return {
            "r_legal": False,
            "reason": cancellation.get("reason"),
            "promotes_claims": False,
        }
    if audit.get("status") != "valid":
        return {
            "r_legal": False,
            "reason": "audit_violation",
            "promotes_claims": False,
        }

    return {
        "r_legal": True,
        "reason": "r_legality_conditions_met",
        "promotes_claims": False,
    }
