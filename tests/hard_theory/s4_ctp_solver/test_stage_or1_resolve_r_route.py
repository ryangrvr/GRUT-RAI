from grut.hard_theory.s4_ctp_solver.stage_or1_resolve_r_route import (
    run_stage_or1_resolve_r_route,
)


def _ratio(ratio_id, left_source, right_source):
    return {
        "ratio_id": ratio_id,
        "pair": {
            "left": {
                "source_type": left_source,
                "source_family": "nonlocal_kernel",
                "scheme_protected": True,
                "regulator_class": "dim_reg",
            },
            "right": {
                "source_type": right_source,
                "source_family": "nonlocal_kernel",
                "scheme_protected": True,
                "regulator_class": "dim_reg",
            },
        },
        "symbolic_r": {"regulator_class": "dim_reg"},
        "promotes_claims": False,
    }


def _stage_p11_r3_report(ratios, selected_ratio_id=None, selection_rule_found=False):
    return {
        "selection_rule_found": selection_rule_found,
        "selected_ratio_id": selected_ratio_id,
        "stage_p11_r2": {
            "refreshed_ratios": ratios,
            "unique_equivalence_class_exists": False,
        },
    }


def _install_common(monkeypatch, stage_p11_r3_report):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or1_resolve_r_route.run_stage12g_r_route_terminal_audit",
        lambda: {"stage": "12G"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or1_resolve_r_route.run_stage12c_r1_legality_repair",
        lambda: {"stage": "12C-R1"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or1_resolve_r_route.run_stage12c_r2_metadata_completion",
        lambda: {"stage": "12C-R2"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or1_resolve_r_route.run_stage12c_r3_complete_missing_metadata",
        lambda: {"stage": "12C-R3"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or1_resolve_r_route.run_stage12c_r4_rerun_legality_after_metadata",
        lambda: {"stage": "12C-R4"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or1_resolve_r_route.run_stage12c_r5_protected_source_audit",
        lambda: {"stage": "12C-R5"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or1_resolve_r_route.run_stage_p1_nonlocal_anomaly_source_plan",
        lambda: {"stage": "P1"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or1_resolve_r_route.run_stage_p2_nonlocal_anomaly_kernel_attempt",
        lambda: {"stage": "P2-attempt"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or1_resolve_r_route.run_stage_p2_nonlocal_kernel_derivation",
        lambda: {"stage": "P2-derivation"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or1_resolve_r_route.run_stage_p3_nonlocal_form_construction",
        lambda: {"stage": "P3"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or1_resolve_r_route.run_stage_p4_protected_kernel_integration",
        lambda: {"stage": "P4"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or1_resolve_r_route.run_stage_p11_r3_selection_rule_audit",
        lambda: stage_p11_r3_report,
    )


def test_missing_definition_blocks(monkeypatch):
    ratios = [_ratio("ratio_a", "Im_log_minus_box_i_epsilon", "R_log_box_R")]
    _install_common(monkeypatch, _stage_p11_r3_report(ratios))

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or1_resolve_r_route.build_r_definition_history",
        lambda: {
            "r_definition_found": False,
            "definition_status": "missing",
            "definitions": [],
            "r_definition_source": None,
        },
    )

    report = run_stage_or1_resolve_r_route()
    assert report["status"] == "r_definition_missing"
    assert report["can_advance_to_symbol_binding"] is False


def test_multiple_valid_routes_no_selection(monkeypatch):
    ratios = [
        _ratio("ratio_a", "Im_log_minus_box_i_epsilon", "R_log_box_R"),
        _ratio("ratio_b", "Im_log_minus_box_i_epsilon", "Weyl_log_box_Weyl"),
    ]
    _install_common(monkeypatch, _stage_p11_r3_report(ratios))

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or1_resolve_r_route.build_r_definition_history",
        lambda: {
            "r_definition_found": True,
            "definition_status": "ok",
            "definitions": [
                {
                    "definition_id": "explicit_mapping",
                    "source_type_mapping": {
                        "numerator_source_type": "Im_log_minus_box_i_epsilon",
                        "denominator_source_type": "R_log_box_R",
                    },
                }
            ],
            "r_definition_source": "unit_test",
        },
    )

    report = run_stage_or1_resolve_r_route()
    assert report["status"] == "multiple_valid_routes_no_selection_principle"
    assert report["can_advance_to_symbol_binding"] is False


def test_selected_route_with_rule(monkeypatch):
    ratios = [_ratio("ratio_a", "Im_log_minus_box_i_epsilon", "R_log_box_R")]
    _install_common(
        monkeypatch,
        _stage_p11_r3_report(ratios, selected_ratio_id="ratio_a", selection_rule_found=True),
    )

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or1_resolve_r_route.build_r_definition_history",
        lambda: {
            "r_definition_found": True,
            "definition_status": "ok",
            "definitions": [],
            "r_definition_source": "unit_test",
        },
    )

    report = run_stage_or1_resolve_r_route()
    assert report["status"] == "unique_r_route_selected"
    assert report["selected_route"]["ratio_id"] == "ratio_a"
    assert report["can_advance_to_symbol_binding"] is True


def test_no_numeric_r_or_claims(monkeypatch):
    ratios = [_ratio("ratio_a", "Im_log_minus_box_i_epsilon", "R_log_box_R")]
    _install_common(monkeypatch, _stage_p11_r3_report(ratios))

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or1_resolve_r_route.build_r_definition_history",
        lambda: {
            "r_definition_found": False,
            "definition_status": "missing",
            "definitions": [],
            "r_definition_source": None,
        },
    )

    report = run_stage_or1_resolve_r_route()
    assert report["can_compute_numeric_r"] is False
    assert report["can_claim_r"] is False
    assert report["promotes_claims"] is False
