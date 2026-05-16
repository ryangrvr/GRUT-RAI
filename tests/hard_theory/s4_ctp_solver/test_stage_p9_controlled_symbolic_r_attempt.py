from grut.hard_theory.s4_ctp_solver.stage_p9_controlled_symbolic_r_attempt import (
    run_stage_p9_controlled_symbolic_r_attempt,
)


def _pair(left_overrides=None, right_overrides=None):
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
        "pair_id": "left__right",
        "left": left,
        "right": right,
    }


def test_no_valid_pairs(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p9_controlled_symbolic_r_attempt.run_stage_p8_r_legality_with_protected_kernels",
        lambda: {"valid_pairs": []},
    )

    report = run_stage_p9_controlled_symbolic_r_attempt()
    assert report["r_symbolic_ready"] is False
    assert report["symbolic_pairs_examined"] == 0
    assert report["next_required_action"] == "repair_symbolic_r_topology"


def test_symbolic_pair_success(monkeypatch):
    pair = _pair()
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p9_controlled_symbolic_r_attempt.run_stage_p8_r_legality_with_protected_kernels",
        lambda: {"valid_pairs": [{"pair": pair}]},
    )

    report = run_stage_p9_controlled_symbolic_r_attempt()
    assert report["r_symbolic_ready"] is True
    assert report["r_computation_allowed"] is False
    assert report["promotes_claims"] is False
    assert len(report["symbolic_candidates"]) == 1


def test_pair_blocked_by_coefficient(monkeypatch):
    pair = _pair(left_overrides={"coefficient_value": "not_allowed"})
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p9_controlled_symbolic_r_attempt.run_stage_p8_r_legality_with_protected_kernels",
        lambda: {"valid_pairs": [{"pair": pair}]},
    )

    report = run_stage_p9_controlled_symbolic_r_attempt()
    assert report["r_symbolic_ready"] is False
    assert report["blocked_pairs"]


def test_pair_blocked_by_regulator_mismatch(monkeypatch):
    pair = _pair(right_overrides={"regulator_class": "other_reg"})
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p9_controlled_symbolic_r_attempt.run_stage_p8_r_legality_with_protected_kernels",
        lambda: {"valid_pairs": [{"pair": pair}]},
    )

    report = run_stage_p9_controlled_symbolic_r_attempt()
    assert report["r_symbolic_ready"] is False
    assert report["blocked_pairs"]
