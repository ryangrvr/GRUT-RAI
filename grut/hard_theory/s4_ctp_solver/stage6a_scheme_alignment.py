"""Stage 6A targeted closure: scheme alignment."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.native_attempt_topology_set import (
    get_native_attempt_topology_set,
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
from grut.hard_theory.s4_ctp_solver.scheme_definition import define_reference_scheme
from grut.hard_theory.s4_ctp_solver.scheme_alignment_engine import align_to_scheme
from grut.hard_theory.s4_ctp_solver.scheme_consistency_checks import (
    check_scheme_consistency,
)
from grut.hard_theory.s4_ctp_solver.scheme_alignment_report import (
    generate_scheme_alignment_report,
)


def _gather_stage5_results() -> List[Dict[str, object]]:
    stage5b_topologies = get_native_attempt_topology_set()
    stage5b_pipeline = run_native_attempt_multi_pipeline(stage5b_topologies)
    stage5c_result = evaluate_tensor_native_attempt()

    combined: List[Dict[str, object]] = []
    combined.extend(stage5b_pipeline["results"])
    combined.append(stage5c_result)
    return combined


def run_stage6a_scheme_alignment() -> Dict[str, object]:
    scheme = define_reference_scheme()
    results = _gather_stage5_results()

    aligned_results = [align_to_scheme(result, scheme) for result in results]
    consistency = check_scheme_consistency(aligned_results)
    report = generate_scheme_alignment_report(scheme, aligned_results, consistency)

    guard = enforce_tensor_placeholder_guard(results[-1]) if results else None

    return {
        "stage": "6A",
        "status": "scheme_alignment_partial",
        "scheme_defined": True,
        "alignment_performed": True,
        "consistency_status": consistency.get("status"),
        "scheme_stable_structures": len(report.get("stable_structures", [])),
        "scheme_fragile_structures": len(report.get("fragile_structures", [])),
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "guard": guard,
        "report": report,
    }
