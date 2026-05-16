from grut.hard_theory.s4_ctp_solver.gate3_euler_coefficient_extraction import (
    run_gate3_euler_coefficient_extraction,
)


def test_sympy_blocked_integral_returns_blocked_not_fake() -> None:
    report = run_gate3_euler_coefficient_extraction()
    cosmo = report["results"]["C_Euler_cosmo"]
    final = report["results"]["C_Euler_final"]

    assert cosmo["status"] == "blocked"
    assert final["status"] == "blocked"
    assert cosmo["value"] is None
    assert final["value"] is None
    assert cosmo["finite_part"] is None
    assert final["finite_part"] is None
    assert "Mathematica+HypExp" in cosmo["blocker"]


def test_target_values_not_used_to_construct_coefficients() -> None:
    report = run_gate3_euler_coefficient_extraction()
    cosmo = report["results"]["C_Euler_cosmo"]
    final = report["results"]["C_Euler_final"]

    assert cosmo["manual_target_matched"] is False
    assert final["manual_target_matched"] is False
