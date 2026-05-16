from grut.hard_theory.s4_ctp_solver.stage_p11_r2_equivalence_refresh import (
    run_stage_p11_r2_equivalence_refresh,
)


def _pair(left_overrides=None, right_overrides=None, pair_id="pair_a"):
    left = {
        "candidate_id": "protected_Im_log_minus_box_i_epsilon_candidate",
        "scheme_protected": True,
        "nonlocal_form_present": True,
        "regulator_class": "unknown",
        "source_family": "nonlocal_kernel",
        "source_type": "Im_log_minus_box_i_epsilon",
        "kernel_id": "Im_log_minus_box_i_epsilon_kernel",
        "coefficient_value": None,
    }
    right = {
        "candidate_id": "protected_R_log_box_R_candidate",
        "scheme_protected": True,
        "nonlocal_form_present": True,
        "regulator_class": "unknown",
        "source_family": "nonlocal_kernel",
        "source_type": "R_log_box_R",
        "kernel_id": "R_log_box_R_kernel",
        "coefficient_value": None,
    }
    if left_overrides:
        left.update(left_overrides)
    if right_overrides:
        right.update(right_overrides)
    return {"pair_id": pair_id, "left": left, "right": right}


def _ratio(pair, ratio_id):
    return {
        "ratio_id": ratio_id,
        "pair": pair,
        "symbolic_r": {"symbolic_ratio": "R_symbolic_protected"},
        "classification": "valid_symbolic_ratio_candidate",
        "promotes_claims": False,
    }


def _p10_report(ratios):
    return {"valid_symbolic_ratios": ratios, "blocked_symbolic_ratios": []}


def _p11_r1_report(ratio_regulator_classes):
    return {"ratio_regulator_classes": ratio_regulator_classes}


def _install(monkeypatch, p11_r1_report, p10_report):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p11_r2_equivalence_refresh.run_stage_p11_r1_regulator_class_resolution",
        lambda: p11_r1_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p11_r2_equivalence_refresh.run_stage_p10_symbolic_ratio_classification",
        lambda: p10_report,
    )


def test_propagates_resolved_regulator_classes(monkeypatch):
    pair = _pair()
    ratio = _ratio(pair, "pair_a")
    ratio_classes = [
        {
            "ratio_id": "pair_a",
            "numerator_regulator_class": "dimensional_regularization_symbolic_preserved",
            "denominator_regulator_class": "dimensional_regularization_symbolic_preserved",
            "ratio_regulator_class": "matched_dimensional_symbolic_preserved",
        }
    ]

    _install(monkeypatch, _p11_r1_report(ratio_classes), _p10_report([ratio]))
    report = run_stage_p11_r2_equivalence_refresh()
    refreshed = report["refreshed_ratios"][0]
    assert refreshed["pair"]["left"]["regulator_class"] == "dimensional_regularization_symbolic_preserved"
    assert refreshed["pair"]["right"]["regulator_class"] == "dimensional_regularization_symbolic_preserved"


def test_removes_regulator_unknown_blockers(monkeypatch):
    pair = _pair()
    ratio = _ratio(pair, "pair_a")
    ratio_classes = [
        {
            "ratio_id": "pair_a",
            "numerator_regulator_class": "dimensional_regularization_symbolic_preserved",
            "denominator_regulator_class": "dimensional_regularization_symbolic_preserved",
            "ratio_regulator_class": "matched_dimensional_symbolic_preserved",
        }
    ]

    _install(monkeypatch, _p11_r1_report(ratio_classes), _p10_report([ratio]))
    report = run_stage_p11_r2_equivalence_refresh()
    comparisons = report["equivalence_report"]["comparisons"]
    assert all(item["reason"] != "regulator_class_unknown" for item in comparisons)


def test_preserves_symbolic_only_status(monkeypatch):
    pair = _pair()
    ratio = _ratio(pair, "pair_a")
    ratio_classes = [
        {
            "ratio_id": "pair_a",
            "numerator_regulator_class": "dimensional_regularization_symbolic_preserved",
            "denominator_regulator_class": "dimensional_regularization_symbolic_preserved",
            "ratio_regulator_class": "matched_dimensional_symbolic_preserved",
        }
    ]

    _install(monkeypatch, _p11_r1_report(ratio_classes), _p10_report([ratio]))
    report = run_stage_p11_r2_equivalence_refresh()
    assert report["can_compute_numeric_r"] is False
    assert report["can_claim_r"] is False
    assert report["promotes_claims"] is False


def test_rejects_manual_equivalence_override(monkeypatch):
    pair = _pair()
    ratio = _ratio(pair, "pair_a")
    ratio["manual_equivalence_override"] = True
    ratio_classes = [
        {
            "ratio_id": "pair_a",
            "numerator_regulator_class": "dimensional_regularization_symbolic_preserved",
            "denominator_regulator_class": "dimensional_regularization_symbolic_preserved",
            "ratio_regulator_class": "matched_dimensional_symbolic_preserved",
        }
    ]

    _install(monkeypatch, _p11_r1_report(ratio_classes), _p10_report([ratio]))
    report = run_stage_p11_r2_equivalence_refresh()
    assert report["audit"]["status"] == "invalid"


def test_no_coefficient_values_or_numeric_r(monkeypatch):
    pair = _pair(left_overrides={"coefficient_value": "bad"})
    ratio = _ratio(pair, "pair_a")
    ratio_classes = [
        {
            "ratio_id": "pair_a",
            "numerator_regulator_class": "dimensional_regularization_symbolic_preserved",
            "denominator_regulator_class": "dimensional_regularization_symbolic_preserved",
            "ratio_regulator_class": "matched_dimensional_symbolic_preserved",
        }
    ]

    _install(monkeypatch, _p11_r1_report(ratio_classes), _p10_report([ratio]))
    report = run_stage_p11_r2_equivalence_refresh()
    assert report["audit"]["status"] == "invalid"
    assert report["can_compute_numeric_r"] is False
    assert report["can_claim_r"] is False
