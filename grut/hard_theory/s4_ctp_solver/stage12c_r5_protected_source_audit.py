"""Stage 12C-R5 protected candidate source audit."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage12a_coefficient_assembly_dry_run import (
    run_stage12a_coefficient_assembly_dry_run,
)
from grut.hard_theory.s4_ctp_solver.stage12b_scheme_stability_audit import (
    run_stage12b_scheme_stability_audit,
)
from grut.hard_theory.s4_ctp_solver.stage11e_cross_partition_finite_consistency import (
    run_stage11e_cross_partition_finite_consistency,
)
from grut.hard_theory.s4_ctp_solver.stage12c_r3_complete_missing_metadata import (
    run_stage12c_r3_complete_missing_metadata,
)
from grut.hard_theory.s4_ctp_solver.c_final_reclassification_check import (
    evaluate_c_final_reclassification,
)
from grut.hard_theory.s4_ctp_solver.c_final_source_metadata_report import (
    build_c_final_source_metadata_report,
)


def run_stage12c_r5_protected_source_audit() -> Dict[str, object]:
    stage12a = run_stage12a_coefficient_assembly_dry_run()
    stage12b = run_stage12b_scheme_stability_audit()
    stage11e = run_stage11e_cross_partition_finite_consistency()
    stage12c_r3 = run_stage12c_r3_complete_missing_metadata()

    check = evaluate_c_final_reclassification(stage12a, stage12b, stage11e, stage12c_r3)
    source_metadata_report = build_c_final_source_metadata_report(
        stage12c_r3.get("registry", {}), stage11e
    )

    return {
        "stage": "12C-R5",
        "status": "protected_candidate_source_audit",
        "c_final_reclassification_eligible": check.get(
            "c_final_reclassification_eligible"
        ),
        "disqualifying_sources": check.get("disqualifying_sources"),
        "can_rerun_12b": check.get("c_final_reclassification_eligible") is True,
        "r_computation_allowed": False,
        "promotes_claims": False,
        "source_metadata_report": source_metadata_report,
        "stage12a": stage12a,
        "stage12b": stage12b,
        "stage11e": stage11e,
        "stage12c_r3": stage12c_r3,
        "check": check,
    }
