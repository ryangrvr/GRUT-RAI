"""Stage 12F R attempt status report."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage12c_r_legality_gate import (
    run_stage12c_r_legality_gate,
)
from grut.hard_theory.s4_ctp_solver.stage12d_r_extraction_attempt import (
    run_stage12d_r_extraction_attempt,
)
from grut.hard_theory.s4_ctp_solver.stage12e_r_result_classification import (
    run_stage12e_r_result_classification,
)
from grut.hard_theory.s4_ctp_solver.r_attempt_status_report import (
    build_r_attempt_status_report,
)


def run_stage12f_r_status_report() -> Dict[str, object]:
    stage12c = run_stage12c_r_legality_gate()
    stage12d = run_stage12d_r_extraction_attempt()
    stage12e = run_stage12e_r_result_classification()

    report = build_r_attempt_status_report(stage12c, stage12d, stage12e)

    return {
        **report,
        "stage12c": stage12c,
        "stage12d": stage12d,
        "stage12e": stage12e,
        "promotes_claims": False,
    }
