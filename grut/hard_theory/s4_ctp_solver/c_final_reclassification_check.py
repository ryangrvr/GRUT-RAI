"""Evaluate whether c_final_candidate can be reclassified based on sources."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.c_final_source_audit import audit_c_final_sources


def evaluate_c_final_reclassification(
    stage12a: Dict[str, object],
    stage12b: Dict[str, object],
    stage11e: Dict[str, object],
    stage12c_r3: Dict[str, object],
) -> Dict[str, object]:
    registry = stage12c_r3.get("registry") or stage12a.get("registry", {})
    audit = audit_c_final_sources(registry, stage11e)

    disqualifying_sources = audit.get("disqualifying_sources", [])
    eligible = audit.get("source_count", 0) > 0 and not disqualifying_sources

    return {
        "c_final_reclassification_eligible": eligible,
        "disqualifying_sources": disqualifying_sources,
        "audit": audit,
        "r_computation_allowed": False,
        "promotes_claims": False,
        "stage12a": stage12a,
        "stage12b": stage12b,
        "stage11e": stage11e,
        "stage12c_r3": stage12c_r3,
    }
