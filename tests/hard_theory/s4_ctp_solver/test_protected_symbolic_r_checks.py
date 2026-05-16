from grut.hard_theory.s4_ctp_solver.protected_symbolic_r_checks import (
    check_protected_symbolic_ratio_topology,
    check_protected_symbolic_cancellation,
    check_protected_symbolic_regulator_independence,
    check_protected_symbolic_pair_consistency,
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


def test_ratio_topology_passes():
    report = check_protected_symbolic_ratio_topology(_pair())
    assert report["status"] == "pass"


def test_cancellation_requires_nonmixing():
    report = check_protected_symbolic_cancellation(
        _pair(left_overrides={"counterterm_nonmixing_verified": False})
    )
    assert report["status"] == "fail"


def test_regulator_independence_warns_on_unknown():
    report = check_protected_symbolic_regulator_independence(
        _pair(left_overrides={"regulator_class": "unknown"}, right_overrides={"regulator_class": "unknown"})
    )
    assert report["status"] == "pass"
    assert "regulator_class_unknown" in report["warnings"]


def test_pair_consistency_rejects_identical_sources():
    report = check_protected_symbolic_pair_consistency(
        _pair(right_overrides={"source_type": "Im_log_minus_box_i_epsilon"})
    )
    assert report["status"] == "fail"
