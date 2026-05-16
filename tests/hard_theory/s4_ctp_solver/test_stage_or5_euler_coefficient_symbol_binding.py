from pathlib import Path

from grut.hard_theory.s4_ctp_solver.stage_or5_euler_coefficient_symbol_binding import (
    run_stage_or5_euler_coefficient_symbol_binding,
)


def _registered_candidate(candidate_id, source_type, coefficient_value=None):
    return {
        "protected_source_candidate_id": candidate_id,
        "source_type": source_type,
        "kernel_id": source_type,
        "nonlocal_form_present": True,
        "counterterm_nonmixing_verified": True,
        "finite_extractability": True,
        "coefficient_value": coefficient_value,
        "promotes_claims": False,
    }


def _stage_p7(registered_candidates):
    return {
        "scheme_protected_candidates": [
            {"candidate_id": entry["protected_source_candidate_id"]}
            for entry in registered_candidates
        ],
        "stage_p6": {"registered_candidates": registered_candidates},
    }


def _stage_or4(stage_p7, can_advance=True, allowed_kernel="R_log_box_R"):
    return {
        "can_advance_to_euler_coefficient_symbol_binding": can_advance,
        "allowed_kernel_roles": [{"source_type": allowed_kernel}],
        "stage_or3": {"euler_channel_available": True},
        "stage_p7": stage_p7,
    }


def _install_common(monkeypatch, or4_report):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or5_euler_coefficient_symbol_binding.run_stage_or4_formal_r_definition_gate",
        lambda: or4_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or5_euler_coefficient_symbol_binding.run_stage_or3_s4_euler_anomaly_projection",
        lambda: {"euler_channel_available": True},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or5_euler_coefficient_symbol_binding.run_stage_p7_protected_scheme_injection",
        lambda: or4_report.get("stage_p7", {}),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or5_euler_coefficient_symbol_binding.run_stage_p8_r_legality_with_protected_kernels",
        lambda: {"stage": "P8"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or5_euler_coefficient_symbol_binding.run_stage_p11_r2_equivalence_refresh",
        lambda: {"stage": "P11-R2"},
    )


def test_or4_ladder_entry_exists():
    ladder_path = Path("theory/hard_theory/GRUT_RAI_V3_S4_CTP_SOLVER_LADDER.md")
    assert ladder_path.exists() is True
    content = ladder_path.read_text(encoding="utf-8")
    assert "Stage OR4 — Formal R Definition Gate" in content


def test_r_log_box_r_binds_to_euler_roles(monkeypatch):
    stage_p7 = _stage_p7(
        [_registered_candidate("protected_R_log_box_R_candidate", "R_log_box_R")]
    )
    or4_report = _stage_or4(stage_p7)
    _install_common(monkeypatch, or4_report)

    report = run_stage_or5_euler_coefficient_symbol_binding()
    assert report["binding_complete"] is True
    assert report["symbolic_ratio_form"] == "C_Euler_num / C_Euler_den"
    assert report["can_advance_to_symbolic_euler_extraction"] is True


def test_weyl_log_rejected(monkeypatch):
    stage_p7 = _stage_p7(
        [_registered_candidate("protected_weyl_candidate", "Weyl_log_box_Weyl")]
    )
    or4_report = _stage_or4(stage_p7)
    _install_common(monkeypatch, or4_report)

    report = run_stage_or5_euler_coefficient_symbol_binding()
    blocked = [
        entry
        for entry in report["bindings"]
        if entry.get("source_type") == "Weyl_log_box_Weyl"
    ]
    assert blocked
    assert blocked[0]["status"] == "blocked"


def test_im_log_rejected(monkeypatch):
    stage_p7 = _stage_p7(
        [_registered_candidate("protected_im_log_candidate", "Im_log_minus_box_i_epsilon")]
    )
    or4_report = _stage_or4(stage_p7)
    _install_common(monkeypatch, or4_report)

    report = run_stage_or5_euler_coefficient_symbol_binding()
    blocked = [
        entry
        for entry in report["bindings"]
        if entry.get("source_type") == "Im_log_minus_box_i_epsilon"
    ]
    assert blocked
    assert blocked[0]["status"] == "blocked"


def test_coefficient_values_remain_null(monkeypatch):
    stage_p7 = _stage_p7(
        [_registered_candidate("protected_R_log_box_R_candidate", "R_log_box_R")]
    )
    or4_report = _stage_or4(stage_p7)
    _install_common(monkeypatch, or4_report)

    report = run_stage_or5_euler_coefficient_symbol_binding()
    assert all(entry.get("coefficient_value") is None for entry in report["bindings"])


def test_symbolic_ratio_requires_two_bindings(monkeypatch):
    stage_p7 = _stage_p7([])
    or4_report = _stage_or4(stage_p7)
    _install_common(monkeypatch, or4_report)

    report = run_stage_or5_euler_coefficient_symbol_binding()
    assert report["binding_complete"] is False
    assert report["symbolic_ratio_form"] is None


def test_no_numeric_r_or_claims(monkeypatch):
    stage_p7 = _stage_p7(
        [_registered_candidate("protected_R_log_box_R_candidate", "R_log_box_R")]
    )
    or4_report = _stage_or4(stage_p7)
    _install_common(monkeypatch, or4_report)

    report = run_stage_or5_euler_coefficient_symbol_binding()
    assert report["can_compute_numeric_r"] is False
    assert report["can_claim_r"] is False
    assert report["promotes_claims"] is False
