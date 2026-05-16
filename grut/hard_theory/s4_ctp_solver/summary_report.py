"""Honesty Protocol summary report helper for external audits."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.audit_manifest import build_audit_manifest
from grut.hard_theory.s4_ctp_solver.capability_matrix import build_capability_matrix
from grut.hard_theory.s4_ctp_solver.refusal_report import generate_refusal_report
from grut.hard_theory.s4_ctp_solver.reproducibility_bundle import build_reproducibility_bundle
from grut.hard_theory.s4_ctp_solver.stage3f_external_audit import run_stage3f_external_audit


def build_summary_report() -> Dict[str, object]:
    manifest = build_audit_manifest()
    matrix = build_capability_matrix()
    bundle = build_reproducibility_bundle()
    refusal = generate_refusal_report("compute_full_3loop_s4_ctp")
    stage3f = run_stage3f_external_audit()

    stage_statuses = {stage: entry.status for stage, entry in manifest.items()}
    limitations: List[str] = []
    for entry in manifest.values():
        limitations.extend(entry.current_limitations)

    capability_snapshot = [
        {"capability": row.capability, "status": row.status} for row in matrix
    ]

    return {
        "report_id": "s4_ctp_solver_honesty_protocol",
        "stage_statuses": stage_statuses,
        "capability_snapshot": capability_snapshot,
        "refusal_example": refusal,
        "reproducibility_commands": bundle["test_commands"],
        "known_limitations": sorted(set(limitations)),
        "stage4_allowed_scope": stage3f["stage4_allowed_scope"],
        "can_compute_3loop": False,
        "promotes_claims": False,
    }
