from grut.hard_theory.s4_ctp_solver.s4_ghost_vector_spectral_inversion import (
    perform_ghost_vector_spectral_inversion,
)
from grut.hard_theory.s4_ctp_solver.ghost_vector_inversion_engine import (
    run_ghost_vector_inversion_engine,
)
from grut.hard_theory.s4_ctp_solver.ghost_vector_inversion_comparison import (
    compare_ghost_vector_structure,
)
from grut.hard_theory.s4_ctp_solver.ghost_vector_inversion_audit import (
    audit_ghost_vector_inversion,
)
from grut.hard_theory.s4_ctp_solver.stage7b_ghost_vector_inversion import (
    run_stage7b_ghost_vector_inversion,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_ghost_vector_inversion_runs_multiple_cutoffs():
    engine = run_ghost_vector_inversion_engine([5, 10, 20, 50])
    l_values = [result["l_max"] for result in engine["results"]]
    assert l_values == [5, 10, 20, 50]


def test_partial_vector_sum_representation():
    import sympy as sp

    radius = sp.symbols("a", positive=True)
    result = perform_ghost_vector_spectral_inversion(5, radius)
    assert result["status"] == "partial_vector_sum"
    assert result["expression"] is not None


def test_ghost_operator_and_vector_harmonics_used():
    import sympy as sp

    radius = sp.symbols("a", positive=True)
    result = perform_ghost_vector_spectral_inversion(5, radius)
    assert result["ghost_operator"]["operator_id"] == "s4_fp_ghost_operator"
    assert result["vector_harmonics"]["structure"] == "vector_harmonics"


def test_no_tt_or_graviton_inversion():
    engine = run_ghost_vector_inversion_engine([5])
    assert all(result["sector"] == "ghost_vector" for result in engine["results"])


def test_no_scalar_only_collapse():
    engine = run_ghost_vector_inversion_engine([5])
    comparison = compare_ghost_vector_structure(engine["results"])
    assert comparison["scalar_collapse_detected"] is False


def test_comparison_detects_scalar_collapse_if_injected():
    comparison = compare_ghost_vector_structure(
        [
            {
                "expression": 1,
                "ghost_operator": {"structure": "bad"},
                "vector_harmonics": {"structure": "scalar_only"},
                "status": "partial_vector_sum",
            }
        ]
    )
    assert comparison["scalar_collapse_detected"] is True
    assert comparison["status"] == "fail"


def test_convergence_observed_not_proven():
    engine = run_ghost_vector_inversion_engine([5, 10])
    comparison = compare_ghost_vector_structure(engine["results"])
    assert comparison["convergence_observed"] is True
    assert comparison["convergence_proven"] is False


def test_inversion_audit_passes():
    engine = run_ghost_vector_inversion_engine([5])
    comparison = compare_ghost_vector_structure(engine["results"])
    audit = audit_ghost_vector_inversion({**engine, "comparison": comparison})
    assert audit["status"] == "valid_benchmark"


def test_stage7b_flags_and_guard():
    report = run_stage7b_ghost_vector_inversion()
    assert report["inversion_performed"] is True
    assert report["tt_inversion_performed"] is False
    assert report["can_extract"] is False
    assert report["can_compute_r"] is False
    assert report["promotes_claims"] is False
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_stage7b_pipeline_statuses_unchanged():
    pipeline = S4CTPPipeline()
    stage7a_before = pipeline.run_stage7a_scalar_inversion()
    _ = pipeline.run_stage7b_ghost_vector_inversion()
    stage7a_after = pipeline.run_stage7a_scalar_inversion()
    assert stage7a_before["status"] == stage7a_after["status"]


def test_no_full_three_loop_claims_in_stage7b():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage7b_ghost_vector_inversion()
    assert report["can_compute_full_3loop"] is False


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
