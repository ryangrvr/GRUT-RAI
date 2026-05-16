from grut.hard_theory.s4_ctp_solver.stage_or2_physical_interpretation_constraint import (
    run_stage_or2_physical_interpretation_constraint,
)


def _route(route_id, numerator, denominator):
    return {
        "ratio_id": route_id,
        "numerator_source_type": numerator,
        "denominator_source_type": denominator,
        "promotes_claims": False,
    }


def _or1_report(routes):
    return {"candidate_routes": routes}


def _or1_r1_report(mapped_routes=None):
    return {
        "mapped_routes": mapped_routes or [],
    }


def _intent_statements(classification, explicit_roles=True):
    return [
        {
            "source": "unit_test",
            "statement": "intent",
            "classification": classification,
            "explicit_roles": explicit_roles,
            "promotes_claims": False,
        }
    ]


def _install_common(monkeypatch, or1_report, or1_r1_report, statements):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or2_physical_interpretation_constraint.run_stage_or1_resolve_r_route",
        lambda: or1_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or2_physical_interpretation_constraint.run_stage_or1_r1_legacy_definition_mapping",
        lambda: or1_r1_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or2_physical_interpretation_constraint.load_physical_intent_sources",
        lambda: statements,
    )


def test_ambiguous_intent_blocks(monkeypatch):
    routes = [_route("r1", "Im_log_minus_box_i_epsilon", "R_log_box_R")]
    _install_common(
        monkeypatch,
        _or1_report(routes),
        _or1_r1_report(),
        _intent_statements("undefined_or_ambiguous", explicit_roles=False),
    )

    report = run_stage_or2_physical_interpretation_constraint()
    assert report["unique_route_selected"] is False
    assert report["next_required_action"] == "write_explicit_r_definition"


def test_c_cosmo_ratio_blocks_without_mapping(monkeypatch):
    routes = [_route("r1", "Im_log_minus_box_i_epsilon", "R_log_box_R")]
    statements = _intent_statements("anomaly_final_cosmological_ratio")

    _install_common(monkeypatch, _or1_report(routes), _or1_r1_report(), statements)
    report = run_stage_or2_physical_interpretation_constraint()

    evaluation = report["route_evaluations"][0]
    assert evaluation["blocking_reason"] == "c_cosmo_mapping_missing"
    assert report["unique_route_selected"] is False


def test_causal_intent_requires_explicit_roles(monkeypatch):
    routes = [_route("r1", "Im_log_minus_box_i_epsilon", "R_log_box_R")]
    statements = _intent_statements("causal_ctp_response_ratio", explicit_roles=False)

    _install_common(monkeypatch, _or1_report(routes), _or1_r1_report(), statements)
    report = run_stage_or2_physical_interpretation_constraint()
    evaluation = report["route_evaluations"][0]
    assert evaluation["blocking_reason"] == "explicit_roles_missing"


def test_curvature_intent_requires_explicit_roles(monkeypatch):
    routes = [_route("r1", "R_log_box_R", "Weyl_log_box_Weyl")]
    statements = _intent_statements("curvature_anomaly_ratio", explicit_roles=False)

    _install_common(monkeypatch, _or1_report(routes), _or1_r1_report(), statements)
    report = run_stage_or2_physical_interpretation_constraint()
    evaluation = report["route_evaluations"][0]
    assert evaluation["blocking_reason"] == "explicit_roles_missing"


def test_conflicting_sources_block(monkeypatch):
    routes = [_route("r1", "Im_log_minus_box_i_epsilon", "R_log_box_R")]
    statements = [
        {"classification": "anomaly_final_cosmological_ratio", "explicit_roles": True},
        {"classification": "curvature_anomaly_ratio", "explicit_roles": True},
    ]

    _install_common(monkeypatch, _or1_report(routes), _or1_r1_report(), statements)
    report = run_stage_or2_physical_interpretation_constraint()
    assert report["intent_classification"] == "conflicting"
    assert report["unique_route_selected"] is False


def test_unique_route_selected_when_mapping_matches(monkeypatch):
    routes = [_route("r1", "R_log_box_R", "Weyl_log_box_Weyl")]
    mapped_routes = [
        {
            "mapping_status": "complete",
            "mapped_numerator_candidates": [{"source_type": "R_log_box_R"}],
            "mapped_denominator_candidates": [{"source_type": "Weyl_log_box_Weyl"}],
        }
    ]
    statements = _intent_statements("curvature_anomaly_ratio", explicit_roles=True)

    _install_common(
        monkeypatch,
        _or1_report(routes),
        _or1_r1_report(mapped_routes),
        statements,
    )
    report = run_stage_or2_physical_interpretation_constraint()
    assert report["unique_route_selected"] is True
    assert report["selected_route"]["ratio_id"] == "r1"


def test_no_numeric_r_or_claims(monkeypatch):
    routes = [_route("r1", "R_log_box_R", "Weyl_log_box_Weyl")]
    statements = _intent_statements("curvature_anomaly_ratio", explicit_roles=True)

    _install_common(monkeypatch, _or1_report(routes), _or1_r1_report(), statements)
    report = run_stage_or2_physical_interpretation_constraint()
    assert report["can_compute_numeric_r"] is False
    assert report["can_claim_r"] is False
    assert report["promotes_claims"] is False
