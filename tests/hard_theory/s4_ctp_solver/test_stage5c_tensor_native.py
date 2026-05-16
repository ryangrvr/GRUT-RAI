from grut.hard_theory.s4_ctp_solver.native_attempt_tensor_deep import (
    select_tensor_native_topology,
)
from grut.hard_theory.s4_ctp_solver.tensor_flow_tracking import track_tensor_index_flow
from grut.hard_theory.s4_ctp_solver.tensor_constraint_engine import apply_tensor_constraints
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
    run_stage5c_tensor_native,
)
from grut.hard_theory.s4_ctp_solver.tensor_native_checks import (
    check_tensor_flow_consistency,
    check_tensor_scalar_alignment,
    check_tensor_ward_consistency,
    check_tensor_scheme_integrity,
)
from grut.hard_theory.s4_ctp_solver.tensor_native_report import render_tensor_native_report
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_single_tensor_topology():
    topo = select_tensor_native_topology()
    assert topo.loop_order == 3
    assert topo.background == "S4"


def test_tensor_flow_and_constraints():
    topo = select_tensor_native_topology()
    flow = track_tensor_index_flow(topo)
    assert flow["indices"]
    assert flow["status"] == "tracked_not_contracted"

    constraints = apply_tensor_constraints(flow)
    assert constraints["status"] == "constraint_applied_structural"
    assert constraints["promotes_claims"] is False


def test_tensor_native_evaluation():
    result = evaluate_tensor_native_attempt()
    assert result["status"] == "native_attempt_internal_tensor"
    assert result["finite_part"] == "not_computed"
    assert result["divergence_structure"]


def test_tensor_checks_and_audit():
    result = evaluate_tensor_native_attempt()
    flow = check_tensor_flow_consistency(result)
    scalar = check_tensor_scalar_alignment(result)
    ward = check_tensor_ward_consistency(result)
    scheme = check_tensor_scheme_integrity(result)

    assert flow["promotes_claims"] is False
    assert scalar["promotes_claims"] is False
    assert ward["promotes_claims"] is False
    assert scheme["promotes_claims"] is False

    report = run_stage5c_tensor_native()
    assert report["can_compute_full_3loop"] is False
    assert report["guard"]["status"] == "pass"
    assert report["report"]["topology_id"]


def test_stage5c_pipeline_statuses():
    pipeline = S4CTPPipeline()
    stage2 = pipeline.run_stage2_benchmarks()
    stage3 = pipeline.run_stage3_partials()
    stage3b = pipeline.run_stage3b_s4_ingredients()
    stage3c = pipeline.run_stage3c_tensor_audit()
    stage3d = pipeline.run_stage3d_scheme_audit()
    stage3e = pipeline.run_stage3e_crosscheck_audit()
    stage3f = pipeline.run_stage3f_external_audit()
    stage4a = pipeline.run_stage4a_benchmark_evaluation()
    stage4b = pipeline.run_stage4b_subset_evaluation()
    stage4c = pipeline.run_stage4c_s4_subset_evaluation()
    stage4d = pipeline.run_stage4d_tensor_subset_evaluation()
    stage4e = pipeline.run_stage4e_mixed_subset_evaluation()
    stage5a = pipeline.run_stage5a_native_attempt()
    stage5b = pipeline.run_stage5b_native_multi()
    stage5c = pipeline.run_stage5c_tensor_native()

    assert stage2["status"] == "benchmarked"
    assert stage3["status"] == "speculative_internal"
    assert stage3b["status"] == "ingredient_benchmarked_scaffold"
    assert stage3c["status"] == "tensor_structural_audit"
    assert stage3d["status"] == "renormalization_scheme_audit"
    assert stage3e["status"] == "crosscheck_audit"
    assert stage3f["status"] == "external_audit_ready"
    assert stage4a["status"] == "benchmark_evaluation"
    assert stage4b["status"] == "subset_evaluation"
    assert stage4c["status"] == "curved_subset_evaluation"
    assert stage4d["status"] == "tensor_subset_structural"
    assert stage4e["status"] == "mixed_subset_evaluation"
    assert stage5a["status"] == "native_attempt"
    assert stage5b["status"] == "multi_native_attempt"
    assert stage5c["status"] == "tensor_native_attempt"


def test_no_full_three_loop_claims_in_stage5c():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage5c_tensor_native()
    assert report["can_compute_full_3loop"] is False


def test_tensor_report_and_guard_renderer():
    result = evaluate_tensor_native_attempt()
    guard = enforce_tensor_placeholder_guard(result)
    report = render_tensor_native_report({**result, "can_attempt_candidate_extraction": True})
    assert guard["promotes_claims"] is False
    assert report["constraints_applied"]


def test_tensor_guard_recursive_scan_forbidden_markers():
    result = evaluate_tensor_native_attempt()
    bad = {
        **result,
        "nested": {
            "value": "full_contraction",
            "more": ["tensor_propagator_evaluated"],
        },
    }
    guard = enforce_tensor_placeholder_guard(bad)
    assert guard["status"] == "fail"
    assert guard["issues"]


def test_tensor_guard_allows_exceptions():
    result = evaluate_tensor_native_attempt()
    ok = {
        **result,
        "flags": {
            "evaluated": False,
            "can_compute_full_3loop": False,
            "note": "not_computed",
        },
    }
    guard = enforce_tensor_placeholder_guard(ok)
    assert guard["status"] == "pass"


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
