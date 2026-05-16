from grut.hard_theory.s4_ctp_solver.stage_p11_r3_selection_rule_audit import (
    run_stage_p11_r3_selection_rule_audit,
)


def _pair(left_source, right_source):
    return {
        "pair_id": f"{left_source}__{right_source}",
        "left": {
            "source_type": left_source,
            "source_family": "nonlocal_kernel",
            "scheme_protected": True,
        },
        "right": {
            "source_type": right_source,
            "source_family": "nonlocal_kernel",
            "scheme_protected": True,
        },
    }


def _ratio(left_source, right_source, ratio_id):
    return {
        "ratio_id": ratio_id,
        "pair": _pair(left_source, right_source),
        "symbolic_r": {"symbolic_ratio": "R_symbolic_protected"},
        "promotes_claims": False,
    }


def _p11_r2_report(ratios):
    return {
        "refreshed_ratios": ratios,
    }


def _stage_n2(assumptions=None):
    return {
        "protected_sources_found": 1,
        "assumptions": assumptions or {},
    }


def _install(monkeypatch, p11_r2_report, stage_n2_report):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p11_r3_selection_rule_audit.run_stage_p11_r2_equivalence_refresh",
        lambda: p11_r2_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p11_r3_selection_rule_audit.run_stageN2_imaginary_causal_sector_audit",
        lambda: stage_n2_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p11_r3_selection_rule_audit.run_stage_p5_counterterm_finite_readiness",
        lambda: {"status": "p5"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p11_r3_selection_rule_audit.run_stage_p7_protected_scheme_injection",
        lambda: {"status": "p7"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p11_r3_selection_rule_audit.run_stage_p8_r_legality_with_protected_kernels",
        lambda: {"status": "p8"},
    )


def test_no_manual_ratio_selection(monkeypatch):
    ratio = _ratio("Im_log_minus_box_i_epsilon", "R_log_box_R", "ratio_a")
    ratio["manual_equivalence_override"] = True
    _install(monkeypatch, _p11_r2_report([ratio]), _stage_n2({}))

    report = run_stage_p11_r3_selection_rule_audit()
    assert report["audit"]["status"] == "invalid"
    assert report["selection_rule_found"] is False


def test_detects_multiple_inequivalent_classes(monkeypatch):
    ratios = [
        _ratio("Im_log_minus_box_i_epsilon", "R_log_box_R", "ratio_a"),
        _ratio("Im_log_minus_box_i_epsilon", "Weyl_log_box_Weyl", "ratio_b"),
    ]
    _install(monkeypatch, _p11_r2_report(ratios), _stage_n2({}))

    report = run_stage_p11_r3_selection_rule_audit()
    assert report["selection_rule_found"] is False
    assert len(report["unresolved_ratio_ids"]) == 2


def test_ctp_priority_requires_r_definition(monkeypatch):
    ratios = [_ratio("Im_log_minus_box_i_epsilon", "R_log_box_R", "ratio_a")]
    assumptions = {"ctp_causal_priority": True}
    _install(monkeypatch, _p11_r2_report(ratios), _stage_n2(assumptions))

    report = run_stage_p11_r3_selection_rule_audit()
    assert report["selection_rule_found"] is False


def test_explicit_r_definition_selects_one_ratio(monkeypatch):
    ratios = [_ratio("Im_log_minus_box_i_epsilon", "R_log_box_R", "ratio_a")]
    assumptions = {
        "r_definition": {
            "numerator_source_type": "Im_log_minus_box_i_epsilon",
            "denominator_source_type": "R_log_box_R",
        }
    }
    _install(monkeypatch, _p11_r2_report(ratios), _stage_n2(assumptions))

    report = run_stage_p11_r3_selection_rule_audit()
    assert report["selection_rule_found"] is True
    assert report["selected_ratio_id"] == "ratio_a"


def test_conflicting_rules_block_selection(monkeypatch):
    ratios = [
        _ratio("Im_log_minus_box_i_epsilon", "R_log_box_R", "ratio_a"),
        _ratio("R_log_box_R", "Weyl_log_box_Weyl", "ratio_b"),
    ]
    assumptions = {
        "ctp_causal_priority": True,
        "r_definition": {
            "numerator_source_type": "R_log_box_R",
            "denominator_source_type": "Weyl_log_box_Weyl",
        },
    }
    _install(monkeypatch, _p11_r2_report(ratios), _stage_n2(assumptions))

    report = run_stage_p11_r3_selection_rule_audit()
    assert report["selection_rule_found"] is False


def test_no_coefficient_values_or_numeric_r(monkeypatch):
    ratio = _ratio("Im_log_minus_box_i_epsilon", "R_log_box_R", "ratio_a")
    ratio["pair"]["left"]["coefficient_value"] = "bad"
    ratio["symbolic_r"] = {"r_value": 1}
    _install(monkeypatch, _p11_r2_report([ratio]), _stage_n2({}))

    report = run_stage_p11_r3_selection_rule_audit()
    assert report["audit"]["status"] == "invalid"
    assert report["can_compute_numeric_r"] is False
    assert report["can_claim_r"] is False
