from grut.hard_theory.s4_ctp_solver.stage7f_tt_renormalization_dry_run import (
    run_stage7f_tt_renormalization_dry_run,
)
from grut.hard_theory.s4_ctp_solver.stage7e_tt_regularization import (
    run_stage7e_tt_regularization,
)
from grut.hard_theory.s4_ctp_solver.tt_divergence_to_counterterms import (
    map_tt_divergences_to_counterterms,
)
from grut.hard_theory.s4_ctp_solver.tt_renormalization_plan import (
    build_tt_renormalization_plan,
)
from grut.hard_theory.s4_ctp_solver.tt_scheme_alignment_check import (
    check_tt_scheme_alignment,
)
from grut.hard_theory.s4_ctp_solver.tt_renormalization_audit import (
    audit_tt_renormalization_dry_run,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_counterterms_mapped():
    stage7e = run_stage7e_tt_regularization()
    mapping = map_tt_divergences_to_counterterms(stage7e["regularized"])
    assert mapping["mapping_status"] == "mapped_structurally"
    assert mapping["counterterms_required"]


def test_unmapped_divergences_tracked_if_present():
    stage7e = run_stage7e_tt_regularization()
    mapping = map_tt_divergences_to_counterterms(stage7e["regularized"])
    assert isinstance(mapping["unmapped_divergences"], list)


def test_plan_no_finite_parts():
    stage7e = run_stage7e_tt_regularization()
    mapping = map_tt_divergences_to_counterterms(stage7e["regularized"])
    plan = build_tt_renormalization_plan(mapping)
    assert plan["finite_parts"] == "not_computed"
    assert plan["renormalization_performed"] is False


def test_scheme_alignment_runs():
    stage7e = run_stage7e_tt_regularization()
    mapping = map_tt_divergences_to_counterterms(stage7e["regularized"])
    plan = build_tt_renormalization_plan(mapping)
    scheme = check_tt_scheme_alignment(plan)
    assert scheme["can_extract"] is False


def test_audit_valid():
    stage7e = run_stage7e_tt_regularization()
    mapping = map_tt_divergences_to_counterterms(stage7e["regularized"])
    plan = build_tt_renormalization_plan(mapping)
    scheme = check_tt_scheme_alignment(plan)
    audit = audit_tt_renormalization_dry_run(plan, scheme)
    assert audit["status"] == "valid_dry_run"


def test_stage7f_flags_and_guard():
    report = run_stage7f_tt_renormalization_dry_run()
    assert report["status"] == "tt_renormalization_dry_run"
    assert report["renormalization_performed"] is False
    assert report["finite_parts_computed"] is False
    assert report["can_extract"] is False
    assert report["can_compute_r"] is False
    assert report["promotes_claims"] is False
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_stage7f_pipeline_statuses_unchanged():
    pipeline = S4CTPPipeline()
    stage7e_before = pipeline.run_stage7e_tt_regularization()
    _ = pipeline.run_stage7f_tt_renormalization_dry_run()
    stage7e_after = pipeline.run_stage7e_tt_regularization()
    assert stage7e_before["status"] == stage7e_after["status"]


def test_no_full_three_loop_claims_in_stage7f():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage7f_tt_renormalization_dry_run()
    assert report["can_compute_full_3loop"] is False


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
