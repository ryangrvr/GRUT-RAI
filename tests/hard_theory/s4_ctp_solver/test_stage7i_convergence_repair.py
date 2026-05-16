from grut.hard_theory.s4_ctp_solver.stage7i_convergence_repair import (
    run_stage7i_convergence_repair,
)
from grut.hard_theory.s4_ctp_solver.tt_convergence_metrics import (
    compute_tt_convergence_metrics,
)
from grut.hard_theory.s4_ctp_solver.tt_convergence_thresholds import (
    define_convergence_thresholds,
)
from grut.hard_theory.s4_ctp_solver.tt_convergence_repair import (
    evaluate_convergence_repair,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_metrics_computed():
    metrics = compute_tt_convergence_metrics(
        [
            {"scheme": "cutoff", "l_max": 5, "regularized_sum": 1, "structure_preserved": True},
            {"scheme": "exponential_damping", "l_max": 10, "regularized_sum": 0.9, "structure_preserved": True},
        ]
    )
    assert metrics["metrics_id"] == "tt_convergence_metrics"


def test_successive_differences_exist():
    metrics = compute_tt_convergence_metrics(
        [
            {"scheme": "cutoff", "l_max": 5, "regularized_sum": 1, "structure_preserved": True},
            {"scheme": "cutoff", "l_max": 10, "regularized_sum": 0.9, "structure_preserved": True},
        ]
    )
    assert metrics["successive_differences"]


def test_relative_changes_exist():
    metrics = compute_tt_convergence_metrics(
        [
            {"scheme": "cutoff", "l_max": 5, "regularized_sum": 1, "structure_preserved": True},
            {"scheme": "cutoff", "l_max": 10, "regularized_sum": 0.9, "structure_preserved": True},
        ]
    )
    assert metrics["relative_changes"]


def test_thresholds_defined():
    thresholds = define_convergence_thresholds()
    assert thresholds["relative_change_threshold"] == 0.05


def test_threshold_passing_only_partial_repair():
    metrics = {
        "relative_changes": [0.01],
        "scheme_sensitivity": "low",
        "structure_preserved": True,
    }
    thresholds = define_convergence_thresholds()
    result = evaluate_convergence_repair(metrics, thresholds)
    assert result["repair_status"] == "partial_repair"
    assert result["blocker_closed"] is False


def test_threshold_failure_keeps_blocker_open():
    metrics = {
        "relative_changes": [0.2],
        "scheme_sensitivity": "high",
        "structure_preserved": True,
    }
    thresholds = define_convergence_thresholds()
    result = evaluate_convergence_repair(metrics, thresholds)
    assert result["repair_status"] == "open"


def test_structure_breakdown_fails_repair():
    metrics = {
        "relative_changes": [0.01],
        "scheme_sensitivity": "low",
        "structure_preserved": False,
    }
    thresholds = define_convergence_thresholds()
    result = evaluate_convergence_repair(metrics, thresholds)
    assert result["repair_status"] == "failed"


def test_convergence_proven_always_false():
    report = run_stage7i_convergence_repair()
    assert report["convergence_proven"] is False


def test_blocker_closed_false():
    report = run_stage7i_convergence_repair()
    assert report["blocker_closed"] is False


def test_flags_disallow_finite_parts_and_extraction():
    report = run_stage7i_convergence_repair()
    assert report["can_compute_finite_parts"] is False
    assert report["can_extract"] is False
    assert report["can_compute_r"] is False
    assert report["promotes_claims"] is False


def test_guard_invoked():
    report = run_stage7i_convergence_repair()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_stage7i_pipeline_statuses_unchanged():
    pipeline = S4CTPPipeline()
    stage7h_before = pipeline.run_stage7h_finite_part_repair_plan()
    _ = pipeline.run_stage7i_convergence_repair()
    stage7h_after = pipeline.run_stage7h_finite_part_repair_plan()
    assert stage7h_before["status"] == stage7h_after["status"]


def test_no_full_three_loop_claims_in_stage7i():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage7i_convergence_repair()
    assert report["can_compute_full_3loop"] is False


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
