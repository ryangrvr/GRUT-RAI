"""Stage P3 minimal nonlocal form construction pass."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_kernel_derivation import (
    run_stage_p2_nonlocal_kernel_derivation,
)
from grut.hard_theory.s4_ctp_solver.stageN2_imaginary_causal_sector_audit import (
    run_stageN2_imaginary_causal_sector_audit,
)
from grut.hard_theory.s4_ctp_solver.stage9c_regularized_integrand import (
    run_stage9c_regularized_integrand,
)
from grut.hard_theory.s4_ctp_solver.stage11b_subtraction_dry_run import (
    run_stage11b_subtraction_dry_run,
)
from grut.hard_theory.s4_ctp_solver.nonlocal_form_extractor import (
    extract_nonlocal_markers,
)
from grut.hard_theory.s4_ctp_solver.im_log_kernel_constructor import (
    build_im_log_kernel_candidate,
)
from grut.hard_theory.s4_ctp_solver.curvature_log_kernel_constructor import (
    build_curvature_log_candidates,
)
from grut.hard_theory.s4_ctp_solver.nonlocal_form_validation import (
    validate_nonlocal_form_candidate,
)


def run_stage_p3_nonlocal_form_construction() -> Dict[str, object]:
    stage_p2 = run_stage_p2_nonlocal_kernel_derivation()
    stageN2 = run_stageN2_imaginary_causal_sector_audit()
    stage9c = run_stage9c_regularized_integrand()
    stage11b = run_stage11b_subtraction_dry_run()

    extraction = extract_nonlocal_markers(stage_p2, stageN2, stage9c, stage11b)

    candidates_constructed: List[Dict[str, object]] = []
    blocked_targets: List[Dict[str, object]] = []

    im_result = build_im_log_kernel_candidate(extraction)
    if im_result.get("status") == "constructed":
        candidate = im_result.get("candidate", {})
        validation = validate_nonlocal_form_candidate(candidate)
        if validation["status"] == "pass":
            candidates_constructed.append(
                {
                    "target": im_result.get("target"),
                    "candidate": candidate,
                    "validation": validation,
                    "promotes_claims": False,
                }
            )
        else:
            blocked_targets.append(
                {
                    "target": im_result.get("target"),
                    "reason": "validation_failed",
                    "validation": validation,
                    "promotes_claims": False,
                }
            )
    else:
        blocked_targets.append(im_result)

    curvature_candidates, curvature_blocked = build_curvature_log_candidates(extraction)
    for entry in curvature_candidates:
        candidate = entry.get("candidate", {})
        validation = validate_nonlocal_form_candidate(candidate)
        if validation["status"] == "pass":
            candidates_constructed.append(
                {
                    "target": entry.get("target"),
                    "candidate": candidate,
                    "validation": validation,
                    "promotes_claims": False,
                }
            )
        else:
            blocked_targets.append(
                {
                    "target": entry.get("target"),
                    "reason": "validation_failed",
                    "validation": validation,
                    "promotes_claims": False,
                }
            )

    blocked_targets.extend(curvature_blocked)

    candidate_exists = bool(candidates_constructed)

    return {
        "stage": "P3",
        "status": "nonlocal_form_construction",
        "candidates_constructed": candidates_constructed,
        "blocked_targets": blocked_targets,
        "nonlocal_form_candidate_exists": candidate_exists,
        "protected_source_derived": False,
        "r_computation_allowed": False,
        "rerun_p2_recommended": candidate_exists,
        "promotes_claims": False,
        "stage_p2": stage_p2,
        "stageN2": stageN2,
        "stage9c": stage9c,
        "stage11b": stage11b,
        "extraction": extraction,
    }
