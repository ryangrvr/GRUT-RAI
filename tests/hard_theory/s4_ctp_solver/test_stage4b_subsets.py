import sympy as sp

from grut.hard_theory.s4_ctp_solver.three_loop_subset_flat import flat_subset_topologies
from grut.hard_theory.s4_ctp_solver.symmetry_factors import compute_symmetry_factor
from grut.hard_theory.s4_ctp_solver.subset_evaluation_engine import (
    evaluate_3loop_subset,
    compare_subset_to_known_structure,
)
from grut.hard_theory.s4_ctp_solver.stage4b_subset_evaluation import (
    run_stage4b_subset_evaluation,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_subset_topologies_present():
    topologies = flat_subset_topologies()
    assert len(topologies) >= 3
    assert all(t.loop_order == 3 for t in topologies)


def test_symmetry_factors_known_and_unknown():
    topology = flat_subset_topologies()[0]
    factor = compute_symmetry_factor(topology)
    assert factor["status"] == "structural_verified"
    assert factor["symmetry_factor"] is not None

    class Dummy:
        topology_id = "unknown"

    unknown = compute_symmetry_factor(Dummy())
    assert unknown["status"] == "unknown_topology"


def test_subset_evaluation_factorized_and_partial():
    topologies = flat_subset_topologies()
    factorized = [t for t in topologies if t.factorization_possible]
    partial = [t for t in topologies if not t.factorization_possible]

    for topo in factorized:
        result = evaluate_3loop_subset(topo, {})
        assert result["evaluation_type"] == "factorized"
        assert result["status"] == "partial_benchmark"
        assert result["finite_part"] == "not_evaluated"

    for topo in partial:
        result = evaluate_3loop_subset(topo, {})
        assert result["evaluation_type"] == "partial"
        assert result["status"] == "exploratory"


def test_divergence_patterns_and_comparisons():
    topo = flat_subset_topologies()[0]
    result = evaluate_3loop_subset(topo, {})
    assert result["divergence_structure"] == topo.expected_divergence_pattern

    comparison = compare_subset_to_known_structure(result, topo)
    assert comparison["status"] == "consistent"

    bad = {**result, "divergence_structure": "1/epsilon"}
    comparison_bad = compare_subset_to_known_structure(bad, topo)
    assert comparison_bad["status"] == "inconsistent"


def test_stage4b_audit_gate_and_pipeline():
    report = run_stage4b_subset_evaluation()
    assert report["can_compute_full_3loop"] is False
    assert report["can_attempt_curved_subsets"] is True

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

    assert stage2["status"] == "benchmarked"
    assert stage3["status"] == "speculative_internal"
    assert stage3b["status"] == "ingredient_benchmarked_scaffold"
    assert stage3c["status"] == "tensor_structural_audit"
    assert stage3d["status"] == "renormalization_scheme_audit"
    assert stage3e["status"] == "crosscheck_audit"
    assert stage3f["status"] == "external_audit_ready"
    assert stage4a["status"] == "benchmark_evaluation"
    assert stage4b["status"] == "subset_evaluation"


def test_no_full_three_loop_claims_in_stage4b():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage4b_subset_evaluation()
    assert "computed" not in str(report).lower()


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
