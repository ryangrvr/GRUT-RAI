from grut.hard_theory.s4_ctp_solver.stage7g_finite_part_audit import (
    run_stage7g_finite_part_audit,
)
from grut.hard_theory.s4_ctp_solver.finite_part_requirements import (
    define_finite_part_requirements,
)
from grut.hard_theory.s4_ctp_solver.finite_part_readiness_checks import (
    evaluate_finite_part_readiness,
)
from grut.hard_theory.s4_ctp_solver.finite_part_blockers import (
    identify_finite_part_blockers,
)
from grut.hard_theory.s4_ctp_solver.finite_part_eligibility_decision import (
    decide_finite_part_eligibility,
)
from grut.hard_theory.s4_ctp_solver.stage7d_tt_diagnostics import (
    run_stage7d_tt_diagnostics,
)
from grut.hard_theory.s4_ctp_solver.stage7e_tt_regularization import (
    run_stage7e_tt_regularization,
)
from grut.hard_theory.s4_ctp_solver.stage7f_tt_renormalization_dry_run import (
    run_stage7f_tt_renormalization_dry_run,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_requirements_defined():
    requirements = define_finite_part_requirements()
    assert requirements["status"] == "defined"
    assert requirements["requirements"]


def test_readiness_checks_run():
    stage7d = run_stage7d_tt_diagnostics()
    stage7e = run_stage7e_tt_regularization()
    stage7f = run_stage7f_tt_renormalization_dry_run()
    readiness = evaluate_finite_part_readiness(stage7d, stage7e, stage7f)
    assert 0.0 <= readiness["readiness_score"] <= 1.0


def test_blockers_identified():
    readiness = {
        "divergence_complete": False,
        "scheme_alignment_ok": False,
        "stability_ok": False,
        "structure_ok": False,
        "readiness_score": 0.0,
    }
    blockers = identify_finite_part_blockers(readiness)
    assert "unmapped_divergence" in blockers["blockers"]
    assert blockers["blocking_severity"] in {"low", "medium", "high"}


def test_eligibility_false_when_blockers_exist():
    readiness = {
        "scheme_alignment_ok": False,
        "readiness_score": 0.2,
    }
    blockers = {"blockers": ["scheme_incomplete"]}
    decision = decide_finite_part_eligibility(readiness, blockers)
    assert decision["eligible"] is False


def test_eligibility_true_only_when_conditions_met():
    readiness = {
        "scheme_alignment_ok": True,
        "readiness_score": 0.95,
    }
    blockers = {"blockers": []}
    decision = decide_finite_part_eligibility(readiness, blockers)
    assert decision["eligible"] is True


def test_stage7g_flags_and_guard():
    report = run_stage7g_finite_part_audit()
    assert report["status"] == "finite_part_eligibility_audit"
    assert report["can_extract"] is False
    assert report["can_compute_r"] is False
    assert report["promotes_claims"] is False
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_stage7g_pipeline_statuses_unchanged():
    pipeline = S4CTPPipeline()
    stage7f_before = pipeline.run_stage7f_tt_renormalization_dry_run()
    _ = pipeline.run_stage7g_finite_part_audit()
    stage7f_after = pipeline.run_stage7f_tt_renormalization_dry_run()
    assert stage7f_before["status"] == stage7f_after["status"]


def test_no_full_three_loop_claims_in_stage7g():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage7g_finite_part_audit()
    assert report["can_compute_full_3loop"] is False


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
