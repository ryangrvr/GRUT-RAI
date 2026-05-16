from grut.hard_theory.s4_ctp_solver.s4_tt_operator import define_tt_operator
from grut.hard_theory.s4_ctp_solver.s4_tt_projector_extended import extend_tt_projector
from grut.hard_theory.s4_ctp_solver.s4_tt_propagator_scaffold import (
    build_tt_propagator_scaffold,
)
from grut.hard_theory.s4_ctp_solver.tt_propagator_validation import (
    validate_tt_scaffold,
)
from grut.hard_theory.s4_ctp_solver.tt_propagator_blocker_update import (
    update_tt_blocker_status,
)
from grut.hard_theory.s4_ctp_solver.stage6f_tt_propagator import (
    run_stage6f_tt_propagator,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_tt_operator_definition():
    operator = define_tt_operator()
    assert operator["operator_id"] == "s4_tt_operator"
    assert operator["type"] == "rank_2_tensor"
    assert operator["background"] == "S4"


def test_tt_projector_extension():
    projector = extend_tt_projector()
    assert "transverse" in projector["properties"]
    assert "traceless" in projector["properties"]
    assert projector["status"] == "structural_only"


def test_tt_propagator_scaffold_built():
    operator = define_tt_operator()
    projector = extend_tt_projector()
    scaffold = build_tt_propagator_scaffold(operator, projector)
    assert scaffold["propagator_id"] == "s4_tt_propagator_scaffold"
    assert scaffold["inverse_operator"] == "inverse_operator_placeholder"
    assert "spectral_sum_not_performed" in scaffold["limitations"]


def test_tt_validation_runs():
    operator = define_tt_operator()
    projector = extend_tt_projector()
    scaffold = build_tt_propagator_scaffold(operator, projector)
    validation = validate_tt_scaffold(scaffold, operator, projector)
    assert validation["status"] == "structural_validated"
    assert validation["checks"]["no_scalar_reduction"] is True


def test_tt_blocker_update_status():
    update = update_tt_blocker_status()
    assert update["tt_propagator_scaffold"] == "constructed"
    assert update["tt_propagator_inverted"] == "open"
    assert update["overall_blocker_closed"] is False


def test_stage6f_flags_and_guard():
    report = run_stage6f_tt_propagator()
    assert report["can_extract"] is False
    assert report["can_compute_r"] is False
    assert report["promotes_claims"] is False
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_stage6f_pipeline_statuses_unchanged():
    pipeline = S4CTPPipeline()
    stage6e_before = pipeline.run_stage6e_harmonic_benchmark()
    _ = pipeline.run_stage6f_tt_propagator()
    stage6e_after = pipeline.run_stage6e_harmonic_benchmark()
    assert stage6e_before["status"] == stage6e_after["status"]


def test_no_full_three_loop_claims_in_stage6f():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage6f_tt_propagator()
    assert report["can_compute_full_3loop"] is False


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
