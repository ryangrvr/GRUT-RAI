from grut.hard_theory.s4_ctp_solver.stage_p11_protected_quotient_equivalence_resolution import (
    run_stage_p11_protected_quotient_equivalence_resolution,
)


def _pair(left_overrides=None, right_overrides=None, pair_id="pair_a"):
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


def _ratio(pair, ratio_id):
    return {
        "ratio_id": ratio_id,
        "pair": pair,
        "symbolic_r": {"symbolic_ratio": "R_symbolic_protected"},
        "classification": "valid_symbolic_ratio_candidate",
        "promotes_claims": False,
    }


def _install(monkeypatch, ratios):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p11_protected_quotient_equivalence_resolution.run_stage_p10_symbolic_ratio_classification",
        lambda: {"valid_symbolic_ratios": ratios, "blocked_symbolic_ratios": []},
    )


def test_unique_equivalence_class(monkeypatch):
    ratio = _ratio(_pair(pair_id="pair_a"), "pair_a")
    _install(monkeypatch, [ratio])

    report = run_stage_p11_protected_quotient_equivalence_resolution()
    assert report["unique_ratio_exists"] is True
    assert report["can_advance_to_coefficient_symbol_binding"] is True


def test_multiple_inequivalent_classes(monkeypatch):
    ratio_a = _ratio(_pair(pair_id="pair_a"), "pair_a")
    ratio_b = _ratio(
        _pair(
            right_overrides={"source_type": "Weyl_log_box_Weyl", "kernel_id": "Weyl_log_box_Weyl_kernel"},
            pair_id="pair_b",
        ),
        "pair_b",
    )
    _install(monkeypatch, [ratio_a, ratio_b])

    report = run_stage_p11_protected_quotient_equivalence_resolution()
    assert report["unique_ratio_exists"] is False
    assert report["can_advance_to_coefficient_symbol_binding"] is False


def test_undetermined_when_regulator_unknown(monkeypatch):
    ratio = _ratio(
        _pair(left_overrides={"regulator_class": "unknown"}, right_overrides={"regulator_class": "unknown"}),
        "pair_a",
    )
    _install(monkeypatch, [ratio])

    report = run_stage_p11_protected_quotient_equivalence_resolution()
    assert report["unique_ratio_exists"] is False
    assert report["can_advance_to_coefficient_symbol_binding"] is False
    assert report["equivalence_report"]["unresolved"]


def test_guardrails(monkeypatch):
    ratio = _ratio(_pair(), "pair_a")
    _install(monkeypatch, [ratio])

    report = run_stage_p11_protected_quotient_equivalence_resolution()
    assert report["can_compute_numeric_r"] is False
    assert report["can_claim_r"] is False
    assert report["promotes_claims"] is False
