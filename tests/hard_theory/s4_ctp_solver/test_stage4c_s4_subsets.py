import sympy as sp

from grut.hard_theory.s4_ctp_solver.three_loop_subset_s4_scalar import (
    s4_scalar_subset_topologies,
)
from grut.hard_theory.s4_ctp_solver.s4_subset_expansions import (
    evaluate_s4_subset_via_spectral,
    evaluate_s4_subset_via_curvature_expansion,
)
from grut.hard_theory.s4_ctp_solver.s4_spectral_basis import scalar_harmonic_degeneracy
from grut.hard_theory.s4_ctp_solver.s4_green_functions import scalar_green_denominator
from grut.hard_theory.s4_ctp_solver.s4_curvature_corrections import (
    check_flat_limit,
    check_small_curvature_limit,
)
from grut.hard_theory.s4_ctp_solver.stage4c_s4_subset_evaluation import (
    run_stage4c_s4_subset_evaluation,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_s4_scalar_subset_topologies():
    topologies = s4_scalar_subset_topologies(l_max=2)
    assert len(topologies) >= 3
    assert all(t.background == "S4" for t in topologies)


def test_spectral_evaluation_uses_degeneracy_and_denominator():
    a = sp.symbols("a", positive=True)
    topo = s4_scalar_subset_topologies(l_max=1)[0]
    result = evaluate_s4_subset_via_spectral(topo, l_max=1, radius=a)
    assert result["status"] == "partial_curved_subset"

    degeneracy = scalar_harmonic_degeneracy(0)
    denom = scalar_green_denominator(0, a, mass_sq=sp.symbols("m")**2, xi=sp.Rational(1, 6))
    assert result["expression"].has(degeneracy)
    assert result["expression"].has(denom)


def test_curvature_expansion_symbolic():
    a = sp.symbols("a", positive=True)
    topo = [t for t in s4_scalar_subset_topologies(l_max=1) if t.evaluation_type == "curvature_expansion"][0]
    result = evaluate_s4_subset_via_curvature_expansion(topo, order=2, radius=a)
    assert result["status"] == "curvature_expansion_partial"


def test_consistency_checks():
    a = sp.symbols("a", positive=True)
    topo = s4_scalar_subset_topologies(l_max=1)[0]
    result = evaluate_s4_subset_via_spectral(topo, l_max=1, radius=a)
    flat = check_flat_limit(result)
    small = check_small_curvature_limit(result)
    assert flat["status"] in {"consistent", "inconclusive"}
    assert small["status"] in {"consistent", "inconclusive"}


def test_stage4c_audit_and_pipeline():
    report = run_stage4c_s4_subset_evaluation()
    assert report["can_compute_full_3loop"] is False
    assert report["convergence_established"] is False

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


def test_no_full_three_loop_claims_in_stage4c():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage4c_s4_subset_evaluation()
    assert "computed" not in str(report).lower()


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
