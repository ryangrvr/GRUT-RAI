from pathlib import Path

from grut.hard_theory.s4_ctp_solver.stage_or4_formal_r_definition_gate import (
    run_stage_or4_formal_r_definition_gate,
)


def _projection(source_type, projects_to_euler=False, projects_to_weyl=False, survives=True):
    return {
        "kernel_id": source_type,
        "source_type": source_type,
        "projects_to_euler_channel": projects_to_euler,
        "projects_to_weyl_channel": projects_to_weyl,
        "survives_on_s4": survives,
        "promotes_claims": False,
    }


def _install_common(monkeypatch, kernel_projections, euler_available=True):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or4_formal_r_definition_gate.run_stage_or3_s4_euler_anomaly_projection",
        lambda: {
            "kernel_projections": kernel_projections,
            "euler_channel_available": euler_available,
            "promotes_claims": False,
        },
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or4_formal_r_definition_gate.run_stage_or1_resolve_r_route",
        lambda: {"stage": "OR1"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or4_formal_r_definition_gate.run_stage_or1_r1_legacy_definition_mapping",
        lambda: {"stage": "OR1-R1"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or4_formal_r_definition_gate.run_stage_or2_physical_interpretation_constraint",
        lambda: {"stage": "OR2"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or4_formal_r_definition_gate.run_stage_p11_r2_equivalence_refresh",
        lambda: {"stage": "P11-R2"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or4_formal_r_definition_gate.run_stage_p7_protected_scheme_injection",
        lambda: {"stage": "P7"},
    )


def test_r_definition_document_exists():
    doc_path = Path("theory/hard_theory/R_DEFINITION.md")
    assert doc_path.exists() is True
    content = doc_path.read_text(encoding="utf-8")
    assert "R_log_box_R" in content
    assert "Weyl_log_box_Weyl" in content


def test_weyl_route_blocked_on_round_s4(monkeypatch):
    kernel_projections = [
        _projection("Weyl_log_box_Weyl", projects_to_weyl=True, survives=False)
    ]
    _install_common(monkeypatch, kernel_projections)

    report = run_stage_or4_formal_r_definition_gate()
    blocked = {entry["source_type"]: entry for entry in report["blocked_kernel_roles"]}
    assert blocked["Weyl_log_box_Weyl"]["blocking_reason"] == "weyl_zero_on_s4"


def test_im_log_blocked_without_ctp_bridge(monkeypatch):
    kernel_projections = [_projection("Im_log_minus_box_i_epsilon", survives=True)]
    _install_common(monkeypatch, kernel_projections)

    report = run_stage_or4_formal_r_definition_gate()
    blocked = {entry["source_type"]: entry for entry in report["blocked_kernel_roles"]}
    assert (
        blocked["Im_log_minus_box_i_epsilon"]["blocking_reason"]
        == "ctp_to_euler_bridge_missing"
    )


def test_r_log_maps_to_euler_role(monkeypatch):
    kernel_projections = [
        _projection("R_log_box_R", projects_to_euler=True, survives=True)
    ]
    _install_common(monkeypatch, kernel_projections, euler_available=True)

    report = run_stage_or4_formal_r_definition_gate()
    allowed = {entry["source_type"]: entry for entry in report["allowed_kernel_roles"]}
    assert allowed["R_log_box_R"]["role"] == "euler_channel_anomaly_quotient"
    assert report["can_advance_to_euler_coefficient_symbol_binding"] is True


def test_no_numeric_r_or_claims(monkeypatch):
    kernel_projections = [
        _projection("R_log_box_R", projects_to_euler=True, survives=True)
    ]
    _install_common(monkeypatch, kernel_projections, euler_available=True)

    report = run_stage_or4_formal_r_definition_gate()
    assert report["can_compute_numeric_r"] is False
    assert report["can_claim_r"] is False
    assert report["promotes_claims"] is False
