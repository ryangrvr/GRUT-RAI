from grut.hard_theory.s4_ctp_solver.kernel_counterterm_overlap import (
    evaluate_counterterm_overlap,
)
from grut.hard_theory.s4_ctp_solver.kernel_nonmixing_check import (
    check_counterterm_nonmixing,
)
from grut.hard_theory.s4_ctp_solver.kernel_finite_extractability import (
    evaluate_finite_extractability,
)
from grut.hard_theory.s4_ctp_solver.stage_p5_counterterm_finite_readiness import (
    run_stage_p5_counterterm_finite_readiness,
)


def _candidate(kernel_id: str, form: str) -> dict:
    return {
        "kernel_id": kernel_id,
        "nonlocal_form": form,
        "coefficient": "symbolic_uncomputed",
        "promotes_claims": False,
    }


def test_local_overlap_detection_runs():
    candidate = _candidate("r_log", "R log(Box) R")
    overlap = evaluate_counterterm_overlap(candidate)
    assert overlap["overlaps_local_counterterms"] is True
    assert "R_squared" in overlap["overlap_terms"]
    assert overlap["nonlocal_structure_preserved"] is True


def test_nonlocal_log_not_absorbed_by_local_basis():
    candidate = _candidate("weyl_log", "Weyl log(Box) Weyl")
    overlap = evaluate_counterterm_overlap(candidate)
    nonmixing = check_counterterm_nonmixing(
        candidate,
        overlap,
        {"plan": {"subtractions_planned": []}},
        {"counterterms_mapped": True},
        {"counterterms_registered": True},
    )
    assert nonmixing["counterterm_nonmixing_verified"] is True


def test_nonmixing_fails_without_log_structure():
    candidate = _candidate("plain_r", "R squared")
    overlap = evaluate_counterterm_overlap(candidate)
    nonmixing = check_counterterm_nonmixing(
        candidate,
        overlap,
        {"plan": {"subtractions_planned": []}},
        {"counterterms_mapped": True},
        {"counterterms_registered": True},
    )
    assert nonmixing["counterterm_nonmixing_verified"] is False


def test_finite_extractability_requires_benchmark_pass():
    candidate = _candidate("im_log", "Im log(-Box - i epsilon)")
    nonmixing = {"counterterm_nonmixing_verified": True}
    report = evaluate_finite_extractability(candidate, nonmixing, {"all_benchmarks_pass": False})
    assert report["finite_extractability"] is False
    assert report["coefficient_value"] is None


def test_stage_p5_no_r_or_claims(monkeypatch):
    p4_report = {
        "integrated_candidates": [
            {
                "source_type": "Im_log_minus_box_i_epsilon",
                "candidate": {
                    "kernel_id": "im_log",
                    "nonlocal_form": "Im log(-Box - i epsilon)",
                    "coefficient": "symbolic_uncomputed",
                    "promotes_claims": False,
                },
            }
        ]
    }

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p5_counterterm_finite_readiness.run_stage_p4_protected_kernel_integration",
        lambda: p4_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p5_counterterm_finite_readiness.run_stage11b_subtraction_dry_run",
        lambda: {"plan": {"subtractions_planned": []}},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p5_counterterm_finite_readiness.run_stage3d_scheme_audit",
        lambda: {"counterterms_registered": True},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p5_counterterm_finite_readiness.run_stage7f_tt_renormalization_dry_run",
        lambda: {"counterterms_mapped": True},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p5_counterterm_finite_readiness.run_stage11c_finite_part_benchmark_gate",
        lambda: {"all_benchmarks_pass": False},
    )

    report = run_stage_p5_counterterm_finite_readiness()
    assert report["protected_source_derived"] is False
    assert report["r_computation_allowed"] is False
    assert report["promotes_claims"] is False
    assert report["blocked_kernels"]
