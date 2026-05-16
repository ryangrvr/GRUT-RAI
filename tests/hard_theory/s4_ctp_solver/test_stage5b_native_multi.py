from grut.hard_theory.s4_ctp_solver.native_attempt_topology_set import (
    get_native_attempt_topology_set,
)
from grut.hard_theory.s4_ctp_solver.native_attempt_multi_pipeline import (
    run_native_attempt_multi_pipeline,
)
from grut.hard_theory.s4_ctp_solver.native_attempt_comparison import (
    compare_native_attempts,
)
from grut.hard_theory.s4_ctp_solver.native_attempt_multi_audit import (
    audit_native_multi,
)
from grut.hard_theory.s4_ctp_solver.stage5b_native_multi import (
    run_stage5b_native_multi,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_topology_set_size_and_validity():
    topologies = get_native_attempt_topology_set()
    assert 2 <= len(topologies) <= 3
    assert all(t.loop_order == 3 for t in topologies)
    assert all(t.background == "S4" for t in topologies)


def test_multi_pipeline_and_results():
    topologies = get_native_attempt_topology_set()
    pipeline = run_native_attempt_multi_pipeline(topologies)
    assert pipeline["status"] == "multi_native_attempt"
    assert len(pipeline["results"]) == len(topologies)

    for result in pipeline["results"]:
        assert result["status"] == "native_attempt_internal"
        assert result["finite_part"] == "not_computed"
        assert result["divergence_structure"]
        assert result["evaluation_steps"]


def test_comparison_and_audit():
    topologies = get_native_attempt_topology_set()
    pipeline = run_native_attempt_multi_pipeline(topologies)
    comparison = compare_native_attempts(pipeline["results"])
    assert comparison["promotes_claims"] is False

    audit = audit_native_multi(pipeline["results"], pipeline["audits"], comparison)
    assert audit["promotes_claims"] is False
    assert audit["can_compute_full_3loop"] is False


def test_stage5b_audit_and_pipeline():
    report = run_stage5b_native_multi()
    assert report["topologies_attempted"] in {2, 3}
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
    stage5b = pipeline.run_stage5b_native_multi()

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


def test_no_full_three_loop_claims_in_stage5b():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage5b_native_multi()
    assert report["can_compute_full_3loop"] is False


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
