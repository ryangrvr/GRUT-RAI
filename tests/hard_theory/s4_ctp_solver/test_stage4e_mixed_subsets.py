from grut.hard_theory.s4_ctp_solver.three_loop_subset_s4_mixed import (
    s4_mixed_subset_topologies,
)
from grut.hard_theory.s4_ctp_solver.mixed_subset_structures import (
    build_mixed_structure,
)
from grut.hard_theory.s4_ctp_solver.mixed_contraction_scaffold import (
    symbolic_mixed_contraction,
)
from grut.hard_theory.s4_ctp_solver.mixed_subset_checks import (
    check_mixed_scalar_reduction,
    check_mixed_tensor_consistency,
    check_mixed_scheme_integrity,
)
from grut.hard_theory.s4_ctp_solver.stage4e_mixed_subset_evaluation import (
    run_stage4e_mixed_subset_evaluation,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_mixed_subset_topologies():
    topologies = s4_mixed_subset_topologies()
    assert len(topologies) >= 3
    assert all(t.scalar_component for t in topologies)
    assert all(t.tensor_component for t in topologies)


def test_mixed_structures_and_contraction():
    topo = s4_mixed_subset_topologies()[0]
    structure = build_mixed_structure(topo)
    assert structure.scalar_part_reference
    assert structure.tensor_structure_reference

    record = symbolic_mixed_contraction(topo, structure.__dict__, structure.__dict__)
    assert record["contraction_status"] == "not_evaluated"
    assert record["status"] == "mixed_structure_only"


def test_mixed_reduction_checks():
    topo = s4_mixed_subset_topologies()[0]
    structure = build_mixed_structure(topo)
    record = symbolic_mixed_contraction(topo, structure.__dict__, structure.__dict__)

    scalar = check_mixed_scalar_reduction(record)
    tensor = check_mixed_tensor_consistency(record)
    scheme = check_mixed_scheme_integrity(record)

    assert scalar["status"] in {"consistent", "inconclusive"}
    assert tensor["status"] in {"consistent", "inconclusive"}
    assert scheme["status"] in {"consistent", "inconclusive"}


def test_stage4e_audit_and_pipeline():
    report = run_stage4e_mixed_subset_evaluation()
    assert report["can_compute_full_3loop"] is False
    assert report["any_evaluated_components"] is False

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


def test_no_full_three_loop_claims_in_stage4e():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage4e_mixed_subset_evaluation()
    assert "computed" not in str(report).lower()


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
