"""Stage 6B multi-blocker closure harness."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.blocker_registry import register_blockers
from grut.hard_theory.s4_ctp_solver.blocker_dependency_graph import (
    build_blocker_dependency_graph,
    graph_is_acyclic,
)
from grut.hard_theory.s4_ctp_solver.blocker_closure_plan import (
    build_blocker_closure_plan,
)
from grut.hard_theory.s4_ctp_solver.blocker_progress_audit import (
    run_blocker_progress_audit,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage6b_multi_blocker_harness() -> Dict[str, object]:
    blockers = register_blockers()
    graph = build_blocker_dependency_graph()
    plan = build_blocker_closure_plan()
    audit = run_blocker_progress_audit()

    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())

    return {
        "stage": "6B",
        "status": "multi_blocker_closure_harness",
        "blockers_registered": len(blockers),
        "blockers_closed": 0,
        "can_extract": False,
        "can_compute_r": False,
        "can_promote_r_route": False,
        "promotes_claims": False,
        "dependency_graph": graph,
        "graph_is_acyclic": graph_is_acyclic(graph),
        "closure_plan": plan,
        "progress_audit": audit,
        "guard": guard,
    }
