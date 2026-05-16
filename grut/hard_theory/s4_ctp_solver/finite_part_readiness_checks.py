"""Readiness checks for finite-part eligibility."""

from typing import Dict


def evaluate_finite_part_readiness(
    stage7d: Dict[str, object],
    stage7e: Dict[str, object],
    stage7f: Dict[str, object],
) -> Dict[str, object]:
    divergence_complete = not stage7f.get("mapping", {}).get("unmapped_divergences")
    scheme_alignment = stage7f.get("scheme_check", {}).get("scheme_alignment")
    scheme_alignment_ok = scheme_alignment in {"partial", "consistent"}

    stability_ok = stage7d.get("stability") == "stable"
    structure_ok = stage7e.get("structure_preserved") is True
    convergence_control = stage7e.get("comparison", {}).get("convergence_observed") is False

    score_components = [
        divergence_complete,
        scheme_alignment_ok,
        stability_ok,
        structure_ok,
        convergence_control,
    ]
    readiness_score = sum(bool(item) for item in score_components) / len(score_components)

    return {
        "divergence_complete": divergence_complete,
        "scheme_alignment_ok": scheme_alignment_ok,
        "stability_ok": stability_ok,
        "structure_ok": structure_ok,
        "readiness_score": readiness_score,
        "promotes_claims": False,
    }
