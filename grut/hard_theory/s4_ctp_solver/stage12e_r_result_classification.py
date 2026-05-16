"""Stage 12E R extraction result classification."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage12c_r_legality_gate import (
    run_stage12c_r_legality_gate,
)
from grut.hard_theory.s4_ctp_solver.stage12d_r_extraction_attempt import (
    run_stage12d_r_extraction_attempt,
)
from grut.hard_theory.s4_ctp_solver.r_result_classifier import classify_r_result
from grut.hard_theory.s4_ctp_solver.r_failure_analysis import analyze_r_failure
from grut.hard_theory.s4_ctp_solver.r_result_report import build_r_result_report


def run_stage12e_r_result_classification() -> Dict[str, object]:
    stage12c = run_stage12c_r_legality_gate()
    stage12d = run_stage12d_r_extraction_attempt()

    classification = classify_r_result(stage12c, stage12d)
    analysis = analyze_r_failure(classification.get("classification"))
    report = build_r_result_report(classification, analysis)

    return {
        **report,
        "stage12c": stage12c,
        "stage12d": stage12d,
        "classification_detail": classification,
        "analysis": analysis,
        "promotes_claims": False,
    }
