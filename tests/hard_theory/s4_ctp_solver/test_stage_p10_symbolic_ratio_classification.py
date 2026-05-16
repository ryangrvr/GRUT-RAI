from grut.hard_theory.s4_ctp_solver.stage_p10_symbolic_ratio_classification import (
    run_stage_p10_symbolic_ratio_classification,
)


def _pair(
    left_overrides=None,
    right_overrides=None,
    pair_id="pair_a",
):
    left = {
        "candidate_id": "protected_Im_log_minus_box_i_epsilon_candidate",
        "scheme_protected": True,
        "nonlocal_form_present": True,
        "counterterm_nonmixing_verified": True,
        "finite_extractability": True,
        "regulator_class": "symbolic_regulator",
        "source_family": "nonlocal_kernel",
        "source_type": "Im_log_minus_box_i_epsilon",
        "kernel_id": "Im_log_minus_box_i_epsilon_kernel",
        "coefficient_value": None,
    }
    right = {
        "candidate_id": "protected_R_log_box_R_candidate",
        "scheme_protected": True,
        "nonlocal_form_present": True,
        "counterterm_nonmixing_verified": True,
        "finite_extractability": True,
        "regulator_class": "symbolic_regulator",
        "source_family": "nonlocal_kernel",
        "source_type": "R_log_box_R",
        "kernel_id": "R_log_box_R_kernel",
        "coefficient_value": None,
    }

    if left_overrides:
        left.update(left_overrides)
    if right_overrides:
        right.update(right_overrides)

    return {
        "pair_id": pair_id,
        "left": left,
        "right": right,
    }


def _symbolic(pair):
    return {
        "symbolic_ratio": "R_symbolic_protected",
        "numerator": {"candidate_id": pair["left"]["candidate_id"]},
        "denominator": {"candidate_id": pair["right"]["candidate_id"]},
        "promotes_claims": False,
    }


def _p9_report(entries, blocked=None):
    return {
        "symbolic_candidates": entries,
        "blocked_pairs": blocked or [],
    }


def _p7_report(candidate_ids):
    return {
        "scheme_protected_candidates": [
            {"candidate_id": candidate_id} for candidate_id in candidate_ids
        ]
    }


def _p5_report(source_types):
    return {
        "readiness_candidates": [{"source_type": value} for value in source_types]
    }


def _install(monkeypatch, p9_report, p7_report, p5_report):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p10_symbolic_ratio_classification.run_stage_p9_controlled_symbolic_r_attempt",
        lambda: p9_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p10_symbolic_ratio_classification.run_stage_p8_r_legality_with_protected_kernels",
        lambda: {"valid_pairs": []},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p10_symbolic_ratio_classification.run_stage_p7_protected_scheme_injection",
        lambda: p7_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p10_symbolic_ratio_classification.run_stage_p5_counterterm_finite_readiness",
        lambda: p5_report,
    )


def test_classifies_valid_symbolic_ratio(monkeypatch):
    pair = _pair()
    entry = {"pair": pair, "symbolic_r": _symbolic(pair), "promotes_claims": False}
    _install(
        monkeypatch,
        _p9_report([entry]),
        _p7_report(
            [
                "protected_Im_log_minus_box_i_epsilon_candidate",
                "protected_R_log_box_R_candidate",
            ]
        ),
        _p5_report(["Im_log_minus_box_i_epsilon", "R_log_box_R"]),
    )

    report = run_stage_p10_symbolic_ratio_classification()
    assert len(report["valid_symbolic_ratios"]) == 1
    assert report["unique_ratio_exists"] is True
    assert report["can_advance_to_coefficient_symbol_binding"] is True


def test_rejects_ratio_with_coefficient_value(monkeypatch):
    pair = _pair(left_overrides={"coefficient_value": "bad"})
    entry = {"pair": pair, "symbolic_r": _symbolic(pair), "promotes_claims": False}
    _install(
        monkeypatch,
        _p9_report([entry]),
        _p7_report(
            [
                "protected_Im_log_minus_box_i_epsilon_candidate",
                "protected_R_log_box_R_candidate",
            ]
        ),
        _p5_report(["Im_log_minus_box_i_epsilon", "R_log_box_R"]),
    )

    report = run_stage_p10_symbolic_ratio_classification()
    assert report["blocked_symbolic_ratios"]
    assert report["valid_symbolic_ratios"] == []


def test_rejects_regulator_mismatch(monkeypatch):
    pair = _pair(right_overrides={"regulator_class": "other_reg"})
    entry = {"pair": pair, "symbolic_r": _symbolic(pair), "promotes_claims": False}
    _install(
        monkeypatch,
        _p9_report([entry]),
        _p7_report(
            [
                "protected_Im_log_minus_box_i_epsilon_candidate",
                "protected_R_log_box_R_candidate",
            ]
        ),
        _p5_report(["Im_log_minus_box_i_epsilon", "R_log_box_R"]),
    )

    report = run_stage_p10_symbolic_ratio_classification()
    blocked = report["blocked_symbolic_ratios"][0]
    assert blocked["classification"] == "blocked_by_regulator_residual"


def test_rejects_cancellation_failure(monkeypatch):
    pair = _pair(left_overrides={"counterterm_nonmixing_verified": False})
    entry = {"pair": pair, "symbolic_r": _symbolic(pair), "promotes_claims": False}
    _install(
        monkeypatch,
        _p9_report([entry]),
        _p7_report(
            [
                "protected_Im_log_minus_box_i_epsilon_candidate",
                "protected_R_log_box_R_candidate",
            ]
        ),
        _p5_report(["Im_log_minus_box_i_epsilon", "R_log_box_R"]),
    )

    report = run_stage_p10_symbolic_ratio_classification()
    blocked = report["blocked_symbolic_ratios"][0]
    assert blocked["classification"] == "blocked_by_cancellation_failure"


def test_detects_multiple_inequivalent_ratios(monkeypatch):
    pair_a = _pair(pair_id="pair_a")
    pair_b = _pair(
        right_overrides={"source_type": "Weyl_log_box_Weyl", "kernel_id": "Weyl_log_box_Weyl_kernel"},
        pair_id="pair_b",
    )

    entry_a = {"pair": pair_a, "symbolic_r": _symbolic(pair_a), "promotes_claims": False}
    entry_b = {"pair": pair_b, "symbolic_r": _symbolic(pair_b), "promotes_claims": False}

    _install(
        monkeypatch,
        _p9_report([entry_a, entry_b]),
        _p7_report(
            [
                "protected_Im_log_minus_box_i_epsilon_candidate",
                "protected_R_log_box_R_candidate",
                "protected_Weyl_log_box_Weyl_candidate",
            ]
        ),
        _p5_report(
            ["Im_log_minus_box_i_epsilon", "R_log_box_R", "Weyl_log_box_Weyl"]
        ),
    )

    report = run_stage_p10_symbolic_ratio_classification()
    assert report["unique_ratio_exists"] is False
    assert report["can_advance_to_coefficient_symbol_binding"] is False


def test_no_numeric_r_or_claims(monkeypatch):
    pair = _pair()
    entry = {"pair": pair, "symbolic_r": _symbolic(pair), "promotes_claims": False}
    _install(
        monkeypatch,
        _p9_report([entry]),
        _p7_report(
            [
                "protected_Im_log_minus_box_i_epsilon_candidate",
                "protected_R_log_box_R_candidate",
            ]
        ),
        _p5_report(["Im_log_minus_box_i_epsilon", "R_log_box_R"]),
    )

    report = run_stage_p10_symbolic_ratio_classification()
    assert report["can_compute_numeric_r"] is False
    assert report["can_claim_r"] is False
    assert report["promotes_claims"] is False
