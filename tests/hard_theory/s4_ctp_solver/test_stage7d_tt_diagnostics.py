from grut.hard_theory.s4_ctp_solver.stage7d_tt_diagnostics import (
    run_stage7d_tt_diagnostics,
)
from grut.hard_theory.s4_ctp_solver.stage7c_tt_inversion import run_stage7c_tt_inversion
from grut.hard_theory.s4_ctp_solver.tt_inversion_stability import analyze_tt_stability
from grut.hard_theory.s4_ctp_solver.tt_mode_behavior_analysis import (
    analyze_mode_behavior,
)
from grut.hard_theory.s4_ctp_solver.tt_divergence_diagnostics import (
    diagnose_tt_divergence,
)
from grut.hard_theory.s4_ctp_solver.tt_inversion_failure_modes import (
    classify_tt_failure_modes,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_stability_analysis_runs():
    stage7c = run_stage7c_tt_inversion()
    stability = analyze_tt_stability(stage7c["inversion"]["results"])
    assert stability["stability"] in {"stable", "unstable", "inconclusive"}


def test_mode_analysis_runs():
    stage7c = run_stage7c_tt_inversion()
    analysis = analyze_mode_behavior(stage7c["inversion"]["results"])
    assert "mode_behavior" in analysis


def test_divergence_diagnostics_runs():
    stage7c = run_stage7c_tt_inversion()
    diag = diagnose_tt_divergence(stage7c["inversion"]["results"])
    assert diag["divergence"] in {"none", "mild", "severe", "inconclusive"}


def test_failure_mode_classification():
    stage7c = run_stage7c_tt_inversion()
    stability = analyze_tt_stability(stage7c["inversion"]["results"])
    divergence = diagnose_tt_divergence(stage7c["inversion"]["results"])
    failure = classify_tt_failure_modes(
        {
            "stability": stability,
            "divergence": divergence,
            "comparison": stage7c["comparison"],
        }
    )
    assert failure["failure_mode"] in {
        "no_failure",
        "divergence_ladder",
        "tensor_structure_breakdown",
        "projector_inconsistency",
        "spectral_instability",
    }


def test_no_convergence_claims():
    report = run_stage7d_tt_diagnostics()
    assert report["stage7c"]["convergence_observed"] is False


def test_stage7d_flags_and_guard():
    report = run_stage7d_tt_diagnostics()
    assert report["status"] == "tt_inversion_diagnostics"
    assert report["can_extract"] is False
    assert report["can_compute_r"] is False
    assert report["promotes_claims"] is False
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_stage7d_pipeline_statuses_unchanged():
    pipeline = S4CTPPipeline()
    stage7c_before = pipeline.run_stage7c_tt_inversion()
    _ = pipeline.run_stage7d_tt_diagnostics()
    stage7c_after = pipeline.run_stage7c_tt_inversion()
    assert stage7c_before["status"] == stage7c_after["status"]


def test_no_full_three_loop_claims_in_stage7d():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage7d_tt_diagnostics()
    assert report["can_compute_full_3loop"] is False
