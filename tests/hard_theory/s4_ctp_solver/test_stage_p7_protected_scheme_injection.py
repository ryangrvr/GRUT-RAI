from grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection import (
    run_stage_p7_protected_scheme_injection,
)


def _registered_candidate(source_type: str, kernel_id: str) -> dict:
    return {
        "protected_source_candidate_id": f"protected_{source_type}_candidate",
        "source_type": source_type,
        "kernel_id": kernel_id,
        "nonlocal_form_present": True,
        "counterterm_nonmixing_verified": True,
        "finite_extractability": True,
        "coefficient_value": None,
        "scheme_protection_status": "eligible_for_scheme_stability_audit",
        "physical_coefficient_claimed": False,
        "promotes_claims": False,
    }


def test_injects_only_p6_registered(monkeypatch):
    p6_report = {
        "registered_candidates": [
            _registered_candidate("Im_log_minus_box_i_epsilon", "im_log"),
            _registered_candidate("R_log_box_R", "r_log"),
        ]
    }

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection.run_stage_p6_protected_source_registration",
        lambda: p6_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection.run_stage12b_scheme_stability_audit",
        lambda: {"status": "scheme_stability_audit"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection.run_stage12a_coefficient_assembly_dry_run",
        lambda: {"physical_coefficients_computed": False},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection.run_stage12c_r_legality_gate",
        lambda: {"status": "r_legality_gate"},
    )

    report = run_stage_p7_protected_scheme_injection()
    assert report["injected_count"] == 2
    assert report["scheme_protected_count"] == 2


def test_rejects_unregistered_kernel(monkeypatch):
    p6_report = {"registered_candidates": []}

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection.run_stage_p6_protected_source_registration",
        lambda: p6_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection.inject_protected_sources",
        lambda _stage_p6: [
            {
                "candidate_id": "unregistered",
                "source_type": "Im_log_minus_box_i_epsilon",
                "kernel_id": "im_log",
                "locality_class": "nonlocal",
                "invariant_class": "anomaly_protected_nonlocal_kernel",
                "counterterm_nonmixing_verified": True,
                "finite_extractability": True,
                "coefficient_value": None,
                "physical_coefficient_computed": False,
                "promotes_claims": False,
            }
        ],
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection.run_stage12b_scheme_stability_audit",
        lambda: {"status": "scheme_stability_audit"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection.run_stage12a_coefficient_assembly_dry_run",
        lambda: {"physical_coefficients_computed": False},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection.run_stage12c_r_legality_gate",
        lambda: {"status": "r_legality_gate"},
    )

    report = run_stage_p7_protected_scheme_injection()
    assert report["injection_audit"]["status"] == "fail"


def test_no_coefficients_or_r(monkeypatch):
    p6_report = {
        "registered_candidates": [
            _registered_candidate("Im_log_minus_box_i_epsilon", "im_log")
        ]
    }

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection.run_stage_p6_protected_source_registration",
        lambda: p6_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection.run_stage12b_scheme_stability_audit",
        lambda: {"status": "scheme_stability_audit"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection.run_stage12a_coefficient_assembly_dry_run",
        lambda: {"physical_coefficients_computed": False},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection.run_stage12c_r_legality_gate",
        lambda: {"status": "r_legality_gate"},
    )

    report = run_stage_p7_protected_scheme_injection()
    assert report["r_computation_allowed"] is False
    assert report["promotes_claims"] is False
    for entry in report["scheme_protected_candidates"]:
        assert entry["classification"] == "scheme_protected"
