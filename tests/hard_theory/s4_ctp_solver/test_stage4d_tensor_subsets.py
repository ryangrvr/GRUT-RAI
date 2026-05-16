from grut.hard_theory.s4_ctp_solver.three_loop_subset_s4_tensor import (
    s4_tensor_subset_topologies,
)
from grut.hard_theory.s4_ctp_solver.tensor_subset_structures import (
    tt_propagator_placeholder,
    graviton_vertex_structure,
    index_contraction_structure,
)
from grut.hard_theory.s4_ctp_solver.tensor_contraction_scaffold import (
    symbolic_tensor_contraction,
)
from grut.hard_theory.s4_ctp_solver.tensor_subset_checks import (
    check_tt_constraints,
    check_ward_tensor_consistency,
    check_ctp_tensor_branch_structure,
)
from grut.hard_theory.s4_ctp_solver.stage4d_tensor_subset_evaluation import (
    run_stage4d_tensor_subset_evaluation,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_tensor_subset_topologies():
    topologies = s4_tensor_subset_topologies()
    assert len(topologies) >= 3
    assert all(t.includes_tensor for t in topologies)


def test_tensor_structures_symbolic():
    for record in (
        tt_propagator_placeholder(),
        graviton_vertex_structure(),
        index_contraction_structure(),
    ):
        assert record.status == "symbolic_tensor_structure"
        assert "transverse" in record.tt_constraints
        assert "traceless" in record.tt_constraints


def test_contraction_scaffold_and_checks():
    topo = s4_tensor_subset_topologies()[0]
    structures = [tt_propagator_placeholder(), graviton_vertex_structure(), index_contraction_structure()]
    record = symbolic_tensor_contraction(topo, structures)
    assert record["contraction_status"] == "not_evaluated"
    assert record["tensor_indices"]
    assert record["status"] == "tensor_structure_only"

    tt = check_tt_constraints(record)
    ward = check_ward_tensor_consistency(record)
    ctp = check_ctp_tensor_branch_structure(record)
    assert tt["status"] in {"structural_pass", "incomplete"}
    assert ward["status"] in {"structural_pass", "incomplete"}
    assert ctp["status"] in {"structural_pass", "incomplete"}


def test_stage4d_audit_and_pipeline():
    report = run_stage4d_tensor_subset_evaluation()
    assert report["any_tensor_evaluated"] is False
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


def test_no_full_three_loop_claims_in_stage4d():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage4d_tensor_subset_evaluation()
    assert "computed" not in str(report).lower()


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
