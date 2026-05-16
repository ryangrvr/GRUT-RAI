"""Stage 5D candidate extraction readiness audit."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.native_attempt_topology import (
    select_native_attempt_topology,
)
from grut.hard_theory.s4_ctp_solver.native_attempt_topology_set import (
    get_native_attempt_topology_set,
)
from grut.hard_theory.s4_ctp_solver.native_attempt_evaluation import (
    evaluate_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.native_attempt_multi_pipeline import (
    run_native_attempt_multi_pipeline,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)
from grut.hard_theory.s4_ctp_solver.candidate_structure_detection import (
    detect_candidate_structures,
)
from grut.hard_theory.s4_ctp_solver.candidate_scheme_assessment import (
    assess_candidate_scheme_safety,
)
from grut.hard_theory.s4_ctp_solver.candidate_extraction_blockers import (
    identify_extraction_blockers,
)


def _gather_stage5_results() -> Dict[str, object]:
    stage5a_topology = select_native_attempt_topology()
    stage5a_result = evaluate_native_attempt(stage5a_topology)

    stage5b_topologies = get_native_attempt_topology_set()
    stage5b_pipeline = run_native_attempt_multi_pipeline(stage5b_topologies)

    stage5c_result = evaluate_tensor_native_attempt()
    guard = enforce_tensor_placeholder_guard(stage5c_result)

    combined_results: List[Dict[str, object]] = [stage5a_result]
    combined_results.extend(stage5b_pipeline["results"])
    combined_results.append(stage5c_result)

    return {
        "results": combined_results,
        "guard": guard,
    }


def run_stage5d_candidate_readiness() -> Dict[str, object]:
    gathered = _gather_stage5_results()
    guard = gathered["guard"]

    detection = detect_candidate_structures(gathered["results"])
    raw_candidates = detection["candidates"]

    assessed_candidates: List[Dict[str, object]] = []
    scheme_assessments: List[Dict[str, object]] = []
    blockers: List[Dict[str, object]] = []

    for candidate in raw_candidates:
        assessment = assess_candidate_scheme_safety(candidate)
        updated = {**candidate, "scheme_sensitivity": assessment["scheme_sensitivity"]}
        assessed_candidates.append(updated)
        scheme_assessments.append(assessment)
        blockers.append(identify_extraction_blockers(updated))

    scheme_protected_candidates = sum(
        1
        for candidate in assessed_candidates
        if candidate["scheme_sensitivity"] == "scheme_protected_candidate"
    )
    scheme_fragile_candidates = sum(
        1
        for candidate in assessed_candidates
        if candidate["scheme_sensitivity"] == "scheme_fragile"
    )

    next_required_for_extraction = [
        "finite parts",
        "convergence proof",
        "explicit tensor contractions",
        "scheme-aligned definitions",
        "Ward verification",
        "independent replication",
    ]

    return {
        "stage": "5D",
        "status": "candidate_extraction_readiness",
        "candidate_count": len(assessed_candidates),
        "scheme_protected_candidates": scheme_protected_candidates,
        "scheme_fragile_candidates": scheme_fragile_candidates,
        "can_extract_any_candidate": False,
        "can_compute_r": False,
        "can_promote_r_route": False,
        "promotes_claims": False,
        "guard": guard,
        "detection": detection,
        "candidates": assessed_candidates,
        "scheme_assessments": scheme_assessments,
        "blockers": blockers,
        "next_required_for_extraction": next_required_for_extraction,
    }
