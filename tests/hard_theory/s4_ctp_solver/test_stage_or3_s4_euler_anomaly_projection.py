from grut.hard_theory.s4_ctp_solver.stage_or3_s4_euler_anomaly_projection import (
    run_stage_or3_s4_euler_anomaly_projection,
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


def _ratio(ratio_id, numerator, denominator):
    return {
        "ratio_id": ratio_id,
        "pair": {
            "left": {"source_type": numerator},
            "right": {"source_type": denominator},
        },
        "promotes_claims": False,
    }


def _install_common(monkeypatch, kernel_projections, ratios):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or3_s4_euler_anomaly_projection.S4CTPPipeline",
        lambda: type("Stage2", (), {"run_stage2_benchmarks": lambda self: {"stage": 2}})(),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or3_s4_euler_anomaly_projection.run_stage_p7_protected_scheme_injection",
        lambda: {"stage_p6": {"registered_candidates": []}},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or3_s4_euler_anomaly_projection.run_stage_p8_r_legality_with_protected_kernels",
        lambda: {"status": "p8"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or3_s4_euler_anomaly_projection.run_stage_p11_r2_equivalence_refresh",
        lambda: {"refreshed_ratios": ratios},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or3_s4_euler_anomaly_projection.run_stage_or1_resolve_r_route",
        lambda: {"stage": "or1"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or3_s4_euler_anomaly_projection.run_stage_or1_r1_legacy_definition_mapping",
        lambda: {"stage": "or1_r1"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or3_s4_euler_anomaly_projection.run_stage_or2_physical_interpretation_constraint",
        lambda: {"stage": "or2"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or3_s4_euler_anomaly_projection.build_kernel_projections",
        lambda _stage_p7, _identities: kernel_projections,
    )


def test_weyl_vanishes_on_s4(monkeypatch):
    kernel_projections = [_projection("Weyl_log_box_Weyl", projects_to_weyl=True, survives=False)]
    ratios = [_ratio("r1", "Weyl_log_box_Weyl", "Weyl_log_box_Weyl")]
    _install_common(monkeypatch, kernel_projections, ratios)

    report = run_stage_or3_s4_euler_anomaly_projection()
    assert report["s4_weyl_zero"] is True
    assert report["blocking_reason"] in {"no_euler_route_selected", "multiple_euler_routes"}


def test_euler_density_survives(monkeypatch):
    kernel_projections = [_projection("R_log_box_R", projects_to_euler=True, survives=True)]
    ratios = [_ratio("r1", "R_log_box_R", "R_log_box_R")]
    _install_common(monkeypatch, kernel_projections, ratios)

    report = run_stage_or3_s4_euler_anomaly_projection()
    assert report["euler_channel_available"] is True


def test_weyl_route_blocks_without_off_shell(monkeypatch):
    kernel_projections = [_projection("Weyl_log_box_Weyl", projects_to_weyl=True, survives=False)]
    ratios = [_ratio("r1", "Weyl_log_box_Weyl", "Weyl_log_box_Weyl")]
    _install_common(monkeypatch, kernel_projections, ratios)

    report = run_stage_or3_s4_euler_anomaly_projection()
    assert report["unique_route_selected"] is False


def test_r_log_maps_to_euler_candidate(monkeypatch):
    kernel_projections = [_projection("R_log_box_R", projects_to_euler=True, survives=True)]
    ratios = [_ratio("r1", "R_log_box_R", "R_log_box_R")]
    _install_common(monkeypatch, kernel_projections, ratios)

    report = run_stage_or3_s4_euler_anomaly_projection()
    assert report["euler_channel_available"] is True


def test_im_log_requires_ctp_bridge(monkeypatch):
    kernel_projections = [_projection("Im_log_minus_box_i_epsilon", survives=True)]
    ratios = [_ratio("r1", "Im_log_minus_box_i_epsilon", "Im_log_minus_box_i_epsilon")]
    _install_common(monkeypatch, kernel_projections, ratios)

    report = run_stage_or3_s4_euler_anomaly_projection()
    assert report["unique_route_selected"] is False


def test_no_numeric_r_or_claims(monkeypatch):
    kernel_projections = [_projection("R_log_box_R", projects_to_euler=True, survives=True)]
    ratios = [_ratio("r1", "R_log_box_R", "R_log_box_R")]
    _install_common(monkeypatch, kernel_projections, ratios)

    report = run_stage_or3_s4_euler_anomaly_projection()
    assert report["can_compute_numeric_r"] is False
    assert report["can_claim_r"] is False
    assert report["promotes_claims"] is False
