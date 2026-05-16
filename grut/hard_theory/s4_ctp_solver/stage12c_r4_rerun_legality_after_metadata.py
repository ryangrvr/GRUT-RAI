"""Stage 12C-R4 rerun legality after metadata completion."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage12c_r3_complete_missing_metadata import (
    run_stage12c_r3_complete_missing_metadata,
)
from grut.hard_theory.s4_ctp_solver.stage12a_coefficient_assembly_dry_run import (
    run_stage12a_coefficient_assembly_dry_run,
)
from grut.hard_theory.s4_ctp_solver.r_legality_rerun_after_metadata import (
    rerun_legality_after_metadata,
)


def run_stage12c_r4_rerun_legality_after_metadata() -> Dict[str, object]:
    stage12c_r3 = run_stage12c_r3_complete_missing_metadata()
    stage12a = run_stage12a_coefficient_assembly_dry_run()

    rerun = rerun_legality_after_metadata(stage12c_r3)

    return {
        "stage": "12C-R4",
        "status": "rerun_legality_after_metadata",
        "metadata_completed": rerun.get("metadata_completed"),
        "candidate_pairs_examined": rerun.get("candidate_pairs_examined"),
        "valid_pairs": rerun.get("valid_pairs"),
        "blocked_pairs": rerun.get("blocked_pairs"),
        "r_legal": rerun.get("r_legal"),
        "remaining_blockers": rerun.get("remaining_blockers"),
        "r_computation_allowed": False,
        "next_required_action": rerun.get("next_required_action"),
        "promotes_claims": False,
        "stage12c_r3": stage12c_r3,
        "stage12a": stage12a,
        "rerun": rerun,
    }
