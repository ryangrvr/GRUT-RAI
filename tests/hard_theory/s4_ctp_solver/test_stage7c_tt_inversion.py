from grut.hard_theory.s4_ctp_solver.s4_tt_truncated_inversion import (
    perform_tt_truncated_inversion,
)
from grut.hard_theory.s4_ctp_solver.tt_inversion_engine import run_tt_inversion_engine
from grut.hard_theory.s4_ctp_solver.tt_inversion_comparison import (
    compare_tt_truncated_structure,
)
from grut.hard_theory.s4_ctp_solver.tt_inversion_audit import audit_tt_inversion
from grut.hard_theory.s4_ctp_solver.stage7c_tt_inversion import run_stage7c_tt_inversion
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_tt_truncated_inversion_runs_multiple_cutoffs():
    engine = run_tt_inversion_engine([3, 5, 10])
    l_values = [result["l_max"] for result in engine["results"]]
    assert l_values == [3, 5, 10]


def test_truncated_inversion_structure():
    import sympy as sp

    radius = sp.symbols("a", positive=True)
    result = perform_tt_truncated_inversion(3, radius)
    assert result["status"] == "partial_attempt"
    assert result["structure"] == "tensor_preserved"


def test_comparison_structure_valid():
    engine = run_tt_inversion_engine([3])
    comparison = compare_tt_truncated_structure(engine["results"])
    assert comparison["structure_valid"] is True
    assert comparison["collapse_detected"] is False


def test_comparison_detects_scalar_collapse():
    comparison = compare_tt_truncated_structure(
        [
            {
                "expression": 1,
                "projector": {"projector_id": "tt_projector_extended"},
            }
        ]
    )
    assert comparison["collapse_detected"] is True


def test_no_convergence_claims():
    engine = run_tt_inversion_engine([3, 5])
    comparison = compare_tt_truncated_structure(engine["results"])
    assert comparison["convergence_observed"] is False


def test_inversion_audit_passes():
    engine = run_tt_inversion_engine([3])
    comparison = compare_tt_truncated_structure(engine["results"])
    audit = audit_tt_inversion(
        {**engine, "comparison": comparison, "guard": {"status": "pass"}}
    )
    assert audit["status"] == "valid_benchmark"


def test_stage7c_flags_and_guard():
    report = run_stage7c_tt_inversion()
    assert report["status"] == "tt_truncated_inversion_attempt"
    assert report["inversion_performed"] is True
    assert report["convergence_observed"] is False
    assert report["can_extract"] is False
    assert report["can_compute_r"] is False
    assert report["promotes_claims"] is False
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_stage7c_pipeline_statuses_unchanged():
    pipeline = S4CTPPipeline()
    stage7b_before = pipeline.run_stage7b_ghost_vector_inversion()
    _ = pipeline.run_stage7c_tt_inversion()
    stage7b_after = pipeline.run_stage7b_ghost_vector_inversion()
    assert stage7b_before["status"] == stage7b_after["status"]


def test_no_full_three_loop_claims_in_stage7c():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage7c_tt_inversion()
    assert report["can_compute_full_3loop"] is False


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
