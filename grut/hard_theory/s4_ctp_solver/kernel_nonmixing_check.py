"""Check whether nonlocal kernels can avoid counterterm mixing."""

from __future__ import annotations

from typing import Dict


def check_counterterm_nonmixing(
    candidate: Dict[str, object],
    overlap_report: Dict[str, object],
    stage11b: Dict[str, object],
    stage7f: Dict[str, object],
    stage3d: Dict[str, object],
) -> Dict[str, object]:
    nonlocal_preserved = overlap_report.get("nonlocal_structure_preserved")
    if not nonlocal_preserved:
        return {
            "kernel_id": candidate.get("kernel_id"),
            "counterterm_nonmixing_verified": False,
            "reason": "nonlocal_structure_missing",
            "promotes_claims": False,
        }

    plan = stage11b.get("plan", {})
    subtractions = plan.get("subtractions_planned", [])
    if any("nonlocal" in item for item in subtractions):
        return {
            "kernel_id": candidate.get("kernel_id"),
            "counterterm_nonmixing_verified": False,
            "reason": "subtraction_plan_removes_nonlocal",
            "promotes_claims": False,
        }

    if not stage3d.get("counterterms_registered", False):
        return {
            "kernel_id": candidate.get("kernel_id"),
            "counterterm_nonmixing_verified": False,
            "reason": "counterterm_registry_missing",
            "promotes_claims": False,
        }

    if stage7f.get("counterterms_mapped") is False:
        return {
            "kernel_id": candidate.get("kernel_id"),
            "counterterm_nonmixing_verified": False,
            "reason": "renormalization_mapping_missing",
            "promotes_claims": False,
        }

    return {
        "kernel_id": candidate.get("kernel_id"),
        "counterterm_nonmixing_verified": True,
        "reason": "nonlocal_structure_preserved",
        "promotes_claims": False,
    }
