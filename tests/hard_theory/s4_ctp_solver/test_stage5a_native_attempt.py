from grut.hard_theory.s4_ctp_solver.native_attempt_topology import (
    select_native_attempt_topology,
)
from grut.hard_theory.s4_ctp_solver.native_attempt_pipeline import (
    run_native_attempt_pipeline,
)
from grut.hard_theory.s4_ctp_solver.native_attempt_evaluation import (
    evaluate_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.native_attempt_audit import (
    audit_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.stage5a_native_attempt import (
    run_stage5a_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_native_attempt_topology():
    topo = select_native_attempt_topology()
    assert topo.loop_order == 3
    assert topo.background == "S4"
    assert topo.native_attempt is True


def test_native_attempt_pipeline_steps():
    topo = select_native_attempt_topology()
    steps = run_native_attempt_pipeline(topo, {})
    names = {step["stage"] for step in steps}
    assert "spectral_setup" in names
    assert "scalar_subset_evaluation" in names
    assert "scheme_tagging" in names
    assert "divergence_tracking" in names
    assert "cross_check" in names


def test_native_attempt_evaluation_and_audit():
    topo = select_native_attempt_topology()
    result = evaluate_native_attempt(topo)
    assert result["finite_part"] == "not_computed"
    assert result["status"] == "native_attempt_internal"
    assert result["promotes_claims"] is False

    audit = audit_native_attempt(result)
    assert audit["promotion_blocked"] is True
    assert audit["can_promote_to_computed"] is False


def test_stage5a_audit_and_pipeline():
    report = run_stage5a_native_attempt()
    assert report["topologies_attempted"] == 1
    assert report["can_compute_full_3loop"] is False

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


def test_no_full_three_loop_claims_in_stage5a():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage5a_native_attempt()
    assert report["can_compute_full_3loop"] is False


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
