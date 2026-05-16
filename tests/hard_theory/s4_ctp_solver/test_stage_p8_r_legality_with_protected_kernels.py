from grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels import (
    run_stage_p8_r_legality_with_protected_kernels,
)


def _p6_candidate(source_type: str, kernel_id: str) -> dict:
    return {
        "protected_source_candidate_id": f"protected_{source_type}_candidate",
        "source_type": source_type,
        "kernel_id": kernel_id,
        "nonlocal_form_present": True,
        "counterterm_nonmixing_verified": True,
        "finite_extractability": True,
        "coefficient_value": None,
    }


def _p7_report() -> dict:
    return {
        "scheme_protected_candidates": [
            {
                "candidate_id": "protected_Im_log_minus_box_i_epsilon_candidate",
                "classification": "scheme_protected",
            },
            {
                "candidate_id": "protected_R_log_box_R_candidate",
                "classification": "scheme_protected",
            },
        ],
        "stage_p6": {
            "registered_candidates": [
                _p6_candidate("Im_log_minus_box_i_epsilon", "im_log"),
                _p6_candidate("R_log_box_R", "r_log"),
            ]
        },
    }


def test_only_protected_candidates_used(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels.run_stage_p7_protected_scheme_injection",
        _p7_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels.run_stage_p5_counterterm_finite_readiness",
        lambda: {"readiness_candidates": []},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels.run_stage_p4_protected_kernel_integration",
        lambda: {"integrated_candidates": []},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels.run_stage12b_scheme_stability_audit",
        lambda: {"status": "scheme_stability_audit"},
    )

    report = run_stage_p8_r_legality_with_protected_kernels()
    assert report["candidate_pairs_examined"] == 1


def test_invalid_fragile_candidate_rejected(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels.run_stage_p7_protected_scheme_injection",
        lambda: {
            "scheme_protected_candidates": [],
            "stage_p6": {"registered_candidates": []},
        },
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels.run_stage_p5_counterterm_finite_readiness",
        lambda: {"readiness_candidates": []},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels.run_stage_p4_protected_kernel_integration",
        lambda: {"integrated_candidates": []},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels.run_stage12b_scheme_stability_audit",
        lambda: {"status": "scheme_stability_audit"},
    )

    report = run_stage_p8_r_legality_with_protected_kernels()
    assert report["r_legal"] is False


def test_valid_protected_pair_passes_legality(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels.run_stage_p7_protected_scheme_injection",
        _p7_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels.run_stage_p5_counterterm_finite_readiness",
        lambda: {"readiness_candidates": []},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels.run_stage_p4_protected_kernel_integration",
        lambda: {"integrated_candidates": []},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels.run_stage12b_scheme_stability_audit",
        lambda: {"status": "scheme_stability_audit"},
    )

    report = run_stage_p8_r_legality_with_protected_kernels()
    assert report["r_legal"] is True
    assert report["next_required_action"] == "run_controlled_symbolic_r_attempt"


def test_no_coefficients_or_r(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels.run_stage_p7_protected_scheme_injection",
        _p7_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels.run_stage_p5_counterterm_finite_readiness",
        lambda: {"readiness_candidates": []},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels.run_stage_p4_protected_kernel_integration",
        lambda: {"integrated_candidates": []},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels.run_stage12b_scheme_stability_audit",
        lambda: {"status": "scheme_stability_audit"},
    )

    report = run_stage_p8_r_legality_with_protected_kernels()
    assert report["r_computation_allowed"] is False
    assert report["promotes_claims"] is False
