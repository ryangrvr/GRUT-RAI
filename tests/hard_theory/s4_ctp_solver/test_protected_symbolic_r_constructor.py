from grut.hard_theory.s4_ctp_solver.protected_symbolic_r_constructor import (
    build_protected_symbolic_r,
)


def test_symbolic_constructor_shape():
    pair = {
        "pair_id": "left__right",
        "left": {
            "candidate_id": "protected_Im_log_minus_box_i_epsilon_candidate",
            "source_type": "Im_log_minus_box_i_epsilon",
            "kernel_id": "Im_log_minus_box_i_epsilon_kernel",
            "regulator_class": "symbolic_regulator",
            "nonlocal_form_present": True,
            "counterterm_nonmixing_verified": True,
            "finite_extractability": True,
        },
        "right": {
            "candidate_id": "protected_R_log_box_R_candidate",
            "source_type": "R_log_box_R",
            "kernel_id": "R_log_box_R_kernel",
            "regulator_class": "symbolic_regulator",
            "nonlocal_form_present": True,
            "counterterm_nonmixing_verified": True,
            "finite_extractability": True,
        },
    }

    report = build_protected_symbolic_r(pair)
    assert report["symbolic_ratio"] == "R_symbolic_protected"
    assert report["numerator"]["candidate_id"] == "protected_Im_log_minus_box_i_epsilon_candidate"
    assert report["denominator"]["candidate_id"] == "protected_R_log_box_R_candidate"
    assert report["promotes_claims"] is False
