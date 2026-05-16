from grut.hard_theory.s4_ctp_solver.s4_ghost_operator import define_ghost_operator
from grut.hard_theory.s4_ctp_solver.s4_ghost_propagator import (
    build_ghost_propagator_structure,
)
from grut.hard_theory.s4_ctp_solver.ghost_propagator_validation import (
    validate_ghost_propagator,
)
from grut.hard_theory.s4_ctp_solver.ghost_propagator_blocker_update import (
    update_ghost_blocker_status,
)
from grut.hard_theory.s4_ctp_solver.stage6d_ghost_propagator import (
    run_stage6d_ghost_propagator,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_ghost_operator_definition():
    operator = define_ghost_operator()
    assert operator["operator_id"] == "s4_fp_ghost_operator"
    assert operator["type"] == "vector_ghost"
    assert operator["background"] == "S4"
    assert "R" in str(operator["structure"])


def test_ghost_propagator_structure():
    operator = define_ghost_operator()
    propagator = build_ghost_propagator_structure(operator)
    assert propagator["propagator_id"] == "s4_ghost_propagator_structural"
    assert propagator["index_structure"] == "vector"
    assert propagator["representation"] != "full_evaluated"


def test_ghost_propagator_validation():
    operator = define_ghost_operator()
    propagator = build_ghost_propagator_structure(operator)
    validation = validate_ghost_propagator(propagator, operator)
    assert validation["status"] == "structural_validated"
    assert validation["checks"]["no_scalar_reduction"] is True


def test_blocker_update_partial_closure():
    update = update_ghost_blocker_status()
    assert update["ghost_subproblem"] == "partially_closed"
    assert update["tt_graviton_propagator"] == "open"
    assert update["overall_blocker_closed"] is False


def test_stage6d_flags_and_guard():
    report = run_stage6d_ghost_propagator()
    assert report["can_extract"] is False
    assert report["can_compute_r"] is False
    assert report["promotes_claims"] is False
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_stage6d_pipeline_statuses_unchanged():
    pipeline = S4CTPPipeline()
    stage6c_before = pipeline.run_stage6c_scalar_propagator()
    _ = pipeline.run_stage6d_ghost_propagator()
    stage6c_after = pipeline.run_stage6c_scalar_propagator()
    assert stage6c_before["status"] == stage6c_after["status"]


def test_no_full_three_loop_claims_in_stage6d():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage6d_ghost_propagator()
    assert report["can_compute_full_3loop"] is False


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
