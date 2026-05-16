from grut.hard_theory.s4_ctp_solver.stage_p6_protected_source_registration import (
    run_stage_p6_protected_source_registration,
)


def _ready_record(source_type: str, kernel_id: str) -> dict:
    return {
        "source_type": source_type,
        "candidate": {
            "kernel_id": kernel_id,
            "nonlocal_form": "Im log(-Box - i epsilon)",
        },
        "nonmixing": {"counterterm_nonmixing_verified": True},
        "finite_extractability": {"finite_extractability": True},
    }


def test_registers_all_p5_ready(monkeypatch):
    p5_report = {
        "readiness_candidates": [
            _ready_record("Im_log_minus_box_i_epsilon", "im_log"),
            _ready_record("R_log_box_R", "r_log"),
        ],
        "blocked_kernels": [],
    }
    p4_report = {
        "integrated_candidates": [
            {
                "source_type": "Im_log_minus_box_i_epsilon",
                "candidate": {"nonlocal_form_present": True},
            },
            {
                "source_type": "R_log_box_R",
                "candidate": {"nonlocal_form_present": True},
            },
        ]
    }

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p6_protected_source_registration.run_stage_p5_counterterm_finite_readiness",
        lambda: p5_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p6_protected_source_registration.run_stage_p4_protected_kernel_integration",
        lambda: p4_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p6_protected_source_registration.run_stage12b_scheme_stability_audit",
        lambda: {"status": "scheme_stability_audit"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p6_protected_source_registration.run_stage12c_r_legality_gate",
        lambda: {"status": "r_legality_gate"},
    )

    report = run_stage_p6_protected_source_registration()
    assert report["registered_count"] == 2


def test_rejects_nonmixing_or_finite_failures(monkeypatch):
    p5_report = {
        "readiness_candidates": [],
        "blocked_kernels": [
            {
                "source_type": "Im_log_minus_box_i_epsilon",
                "candidate": {"kernel_id": "im_log"},
                "nonmixing": {"counterterm_nonmixing_verified": False},
                "finite_extractability": {"finite_extractability": False},
            }
        ],
    }
    p4_report = {"integrated_candidates": []}

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p6_protected_source_registration.run_stage_p5_counterterm_finite_readiness",
        lambda: p5_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p6_protected_source_registration.run_stage_p4_protected_kernel_integration",
        lambda: p4_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p6_protected_source_registration.run_stage12b_scheme_stability_audit",
        lambda: {"status": "scheme_stability_audit"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p6_protected_source_registration.run_stage12c_r_legality_gate",
        lambda: {"status": "r_legality_gate"},
    )

    report = run_stage_p6_protected_source_registration()
    assert report["registered_count"] == 0


def test_no_coefficients_or_claims(monkeypatch):
    p5_report = {
        "readiness_candidates": [_ready_record("Im_log_minus_box_i_epsilon", "im_log")],
        "blocked_kernels": [],
    }
    p4_report = {
        "integrated_candidates": [
            {
                "source_type": "Im_log_minus_box_i_epsilon",
                "candidate": {"nonlocal_form_present": True},
            }
        ]
    }

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p6_protected_source_registration.run_stage_p5_counterterm_finite_readiness",
        lambda: p5_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p6_protected_source_registration.run_stage_p4_protected_kernel_integration",
        lambda: p4_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p6_protected_source_registration.run_stage12b_scheme_stability_audit",
        lambda: {"status": "scheme_stability_audit"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p6_protected_source_registration.run_stage12c_r_legality_gate",
        lambda: {"status": "r_legality_gate"},
    )

    report = run_stage_p6_protected_source_registration()
    assert report["r_computation_allowed"] is False
    for entry in report["registered_candidates"]:
        assert entry["coefficient_value"] is None
        assert entry["physical_coefficient_claimed"] is False
        assert entry["promotes_claims"] is False
