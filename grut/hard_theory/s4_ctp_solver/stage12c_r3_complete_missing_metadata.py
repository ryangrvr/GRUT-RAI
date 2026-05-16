"""Stage 12C-R3 completion of tensor-origin and regulator metadata."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage9c_regularized_integrand import (
    run_stage9c_regularized_integrand,
)
from grut.hard_theory.s4_ctp_solver.stage9d_integration_dry_run import (
    run_stage9d_integration_dry_run,
)
from grut.hard_theory.s4_ctp_solver.stage12c_r2_metadata_completion import (
    run_stage12c_r2_metadata_completion,
)
from grut.hard_theory.s4_ctp_solver.candidate_tensor_origin_resolver import (
    apply_tensor_origin_metadata,
)
from grut.hard_theory.s4_ctp_solver.candidate_regulator_dependence_resolver import (
    apply_regulator_dependence_metadata,
)
from grut.hard_theory.s4_ctp_solver.candidate_metadata_r3_validation import (
    validate_candidate_metadata_r3,
)


def run_stage12c_r3_complete_missing_metadata() -> Dict[str, object]:
    stage9c = run_stage9c_regularized_integrand()
    stage9d = run_stage9d_integration_dry_run()
    stage12c_r2 = run_stage12c_r2_metadata_completion()

    registry = stage12c_r2.get("registry", {})
    registry = apply_tensor_origin_metadata(registry)
    registry = apply_regulator_dependence_metadata(registry, stage9c, stage9d)

    validation = validate_candidate_metadata_r3(registry)
    metadata_completed = validation.get("valid") is True

    return {
        "stage": "12C-R3",
        "status": "complete_missing_metadata",
        "metadata_completed": metadata_completed,
        "remaining_missing_fields": validation.get("missing_fields", []),
        "r_computation_allowed": False,
        "rerun_12b_12c_recommended": metadata_completed,
        "promotes_claims": False,
        "stage9c": stage9c,
        "stage9d": stage9d,
        "stage12c_r2": stage12c_r2,
        "registry": registry,
        "validation": validation,
    }
