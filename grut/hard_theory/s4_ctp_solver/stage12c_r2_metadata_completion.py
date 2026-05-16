"""Stage 12C-R2 candidate metadata completion."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage11e_cross_partition_finite_consistency import (
    run_stage11e_cross_partition_finite_consistency,
)
from grut.hard_theory.s4_ctp_solver.stage12a_coefficient_assembly_dry_run import (
    run_stage12a_coefficient_assembly_dry_run,
)
from grut.hard_theory.s4_ctp_solver.stage12c_r1_legality_repair import (
    run_stage12c_r1_legality_repair,
)
from grut.hard_theory.s4_ctp_solver.candidate_metadata_completion import (
    complete_candidate_metadata,
)
from grut.hard_theory.s4_ctp_solver.candidate_metadata_validation import (
    validate_candidate_metadata,
)


def run_stage12c_r2_metadata_completion() -> Dict[str, object]:
    stage11e = run_stage11e_cross_partition_finite_consistency()
    stage12a = run_stage12a_coefficient_assembly_dry_run()
    stage12c_r1 = run_stage12c_r1_legality_repair()

    completion = complete_candidate_metadata(
        stage12a.get("registry", {}), stage11e, stage12c_r1
    )
    validation = validate_candidate_metadata(completion.get("registry", {}))

    metadata_completed = validation.get("valid") is True
    missing_fields = validation.get("missing_fields", [])

    return {
        "stage": "12C-R2",
        "status": "candidate_metadata_completion",
        "metadata_completed": metadata_completed,
        "missing_fields": missing_fields,
        "r_computation_allowed": False,
        "rerun_12b_12c_recommended": metadata_completed,
        "promotes_claims": False,
        "stage11e": stage11e,
        "stage12a": stage12a,
        "stage12c_r1": stage12c_r1,
        "registry": completion.get("registry", {}),
        "completion": completion,
        "validation": validation,
    }
