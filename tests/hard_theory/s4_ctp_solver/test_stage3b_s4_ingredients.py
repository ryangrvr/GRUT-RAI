import sympy as sp

from grut.hard_theory.s4_ctp_solver.s4_spectral_basis import (
    scalar_laplacian_eigenvalue,
    scalar_harmonic_degeneracy,
)
from grut.hard_theory.s4_ctp_solver.s4_green_functions import (
    scalar_green_truncated,
    scalar_green_denominator,
)
from grut.hard_theory.s4_ctp_solver.tensor_harmonics import (
    scalar_harmonic_placeholder,
    transverse_vector_harmonic_placeholder,
    transverse_traceless_tensor_harmonic_placeholder,
)
from grut.hard_theory.s4_ctp_solver.propagator_benchmarks import (
    benchmark_scalar_conformal_s4,
    benchmark_scalar_minimal_zero_mode_warning,
    benchmark_flat_large_radius_limit_structure,
)
from grut.hard_theory.s4_ctp_solver.contraction_engine import (
    symbolic_contract_topology_with_propagators,
)
from grut.hard_theory.s4_ctp_solver.diagram_topologies import stage3_topologies
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_scalar_eigenvalue_formula_and_monotonic():
    a = sp.symbols("a", positive=True)
    assert scalar_laplacian_eigenvalue(0, a) == 0
    assert scalar_laplacian_eigenvalue(1, a) > scalar_laplacian_eigenvalue(0, a)
    assert scalar_laplacian_eigenvalue(2, a) > scalar_laplacian_eigenvalue(1, a)


def test_scalar_degeneracy_values():
    assert scalar_harmonic_degeneracy(0) == 1
    assert scalar_harmonic_degeneracy(1) == 5
    assert scalar_harmonic_degeneracy(2) == 14


def test_conformal_scalar_denominator_l0():
    a = sp.symbols("a", positive=True)
    denom = scalar_green_denominator(0, a, mass_sq=0, xi=sp.Rational(1, 6))
    assert sp.simplify(denom - 2 / a**2) == 0


def test_conformal_scalar_has_no_zero_mode_singularity():
    a = sp.symbols("a", positive=True)
    denom = scalar_green_denominator(0, a, mass_sq=0, xi=sp.Rational(1, 6))
    assert sp.simplify(denom) != 0


def test_minimal_massless_scalar_zero_mode_warning():
    a = sp.symbols("a", positive=True)
    report = benchmark_scalar_minimal_zero_mode_warning(a)
    assert report["status"] == "warning"


def test_green_truncation_status_and_error():
    a = sp.symbols("a", positive=True)
    trunc = scalar_green_truncated(max_l=3, radius=a)
    assert trunc.status == "truncated_spectral_representation"
    assert trunc.truncation_error_status == "not_bounded"


def test_tensor_harmonics_are_placeholders():
    for record in (
        scalar_harmonic_placeholder(),
        transverse_vector_harmonic_placeholder(),
        transverse_traceless_tensor_harmonic_placeholder(),
    ):
        assert record.status == "structural_placeholder"
        assert record.evaluated is False


def test_propagator_benchmarks():
    a = sp.symbols("a", positive=True)
    assert benchmark_scalar_conformal_s4(a)["status"] == "benchmarked"
    assert benchmark_scalar_minimal_zero_mode_warning(a)["status"] == "warning"
    assert (
        benchmark_flat_large_radius_limit_structure()["status"]
        in {"structural_only", "benchmarked"}
    )


def test_contraction_engine_scaffold():
    topo = stage3_topologies()[0]
    record = symbolic_contract_topology_with_propagators(topo, ("scalar",))
    assert record.result_status == "scaffold_only"
    assert record.omitted_terms


def test_pipeline_stage3b_status_and_flags():
    pipeline = S4CTPPipeline()
    stage2 = pipeline.run_stage2_benchmarks()
    stage3 = pipeline.run_stage3_partials()
    stage3b = pipeline.run_stage3b_s4_ingredients()
    assert stage2["status"] == "benchmarked"
    assert stage3["status"] == "speculative_internal"
    assert stage3b["can_compute_3loop"] is False
    assert stage3b["promotes_claims"] is False


def test_no_full_three_loop_claims_in_stage3b():
    pipeline = S4CTPPipeline()
    stage3b = pipeline.run_stage3b_s4_ingredients()
    assert "computed" not in str(stage3b).lower()
