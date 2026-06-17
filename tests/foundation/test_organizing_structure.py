"""Tests for the recorded V2->V3 organizing-structure result.

These lock the adversarially-verified dilatation theorem (outcome B):
the adiabatic spatial dilatation is a redundancy of the full CTP action
only at strict k=0 / in the memoryless limit; finite memory L0 breaks it
for k != 0; the breaking is non-anomalous (alpha absent); mu_linear = 1.
"""

import sympy as sp

from grut.foundation.organizing_structure import (
    verify,
    chi_eq_breaking,
    kphys_dilatation_factor,
    OUTCOME,
    MU_LINEAR,
    L0_MPC,
)


def test_all_verify_legs_pass():
    results = verify()
    failed = [k for k, v in results.items() if not v]
    assert not failed, f"organizing_structure verify legs failed: {failed}"


def test_invariant_at_strict_k0_broken_otherwise():
    br = chi_eq_breaking()
    assert br["invariant_at_k0"], "chi_eq must be invariant under T_lambda at strict k=0"
    assert br["broken_for_k_nonzero"], "chi_eq must break for k != 0 (finite-L0 obstruction)"


def test_kphys_exponent_is_minus_lambda():
    lam = sp.Symbol("lambda", real=True)
    assert sp.simplify(kphys_dilatation_factor() - sp.exp(-lam)) == 0


def test_squared_argument_exponent_is_minus_2lambda():
    lam = sp.Symbol("lambda", real=True)
    br = chi_eq_breaking()
    assert sp.simplify(br["squared_arg_factor"] - sp.exp(-2 * lam)) == 0


def test_outcome_is_B_not_A_or_C():
    assert OUTCOME == "B_broken_by_kernel"


def test_mu_linear_is_one():
    assert MU_LINEAR == 1


def test_L0_is_about_12p85_Mpc():
    assert abs(L0_MPC - 12.85) < 0.5
