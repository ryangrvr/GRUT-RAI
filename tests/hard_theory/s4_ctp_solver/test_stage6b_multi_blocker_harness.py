from grut.hard_theory.s4_ctp_solver.blocker_registry import register_blockers
from grut.hard_theory.s4_ctp_solver.blocker_dependency_graph import (
    build_blocker_dependency_graph,
    graph_is_acyclic,
)
from grut.hard_theory.s4_ctp_solver.stage6b_multi_blocker_harness import (
    run_stage6b_multi_blocker_harness,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_blockers_registered():
    blockers = register_blockers()
    assert len(blockers) == 6
    assert all(blocker["closure_status"] == "open" for blocker in blockers)


def test_dependency_graph_acyclic():
    graph = build_blocker_dependency_graph()
    assert graph_is_acyclic(graph) is True


def test_stage6b_flags_and_guard():
    report = run_stage6b_multi_blocker_harness()
    assert report["blockers_registered"] == 6
    assert report["blockers_closed"] == 0
    assert report["can_extract"] is False
    assert report["can_compute_r"] is False
    assert report["can_promote_r_route"] is False
    assert report["promotes_claims"] is False
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_stage6b_pipeline_statuses_unchanged():
    pipeline = S4CTPPipeline()
    stage6a_before = pipeline.run_stage6a_scheme_alignment()
    _ = pipeline.run_stage6b_multi_blocker_harness()
    stage6a_after = pipeline.run_stage6a_scheme_alignment()
    assert stage6a_before["status"] == stage6a_after["status"]


def test_no_full_three_loop_claims_in_stage6b():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage6b_multi_blocker_harness()
    assert report["can_compute_full_3loop"] is False


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
