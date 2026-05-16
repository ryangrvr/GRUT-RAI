from __future__ import annotations

import pytest
import sympy as sp

from grut.derivation.tji.aj_parameter_branches import (
    allowed_branch_ids,
    allen_jacobson_kernel,
    branch_table_rows,
    build_branch_table,
    conformal_closed_form_kernel,
    dimension_from_epsilon,
    h_pm_conformal_scalar,
    h_pm_massive,
    h_pm_massless_minimal,
    select_branch,
    validate_m2_over_h2,
    verify_conformal_kernel_reduction,
)


def test_dimension_from_epsilon_definition() -> None:
    eps = sp.Symbol("epsilon")
    assert dimension_from_epsilon(eps) == 4 - 2 * eps


def test_h_pm_conformal_branch() -> None:
    D = sp.Symbol("D")
    hp, hm = h_pm_conformal_scalar(D)
    assert hp == D / 2
    assert hm == (D - 2) / 2


def test_h_pm_massless_minimal_branch() -> None:
    D = sp.Symbol("D")
    hp, hm = h_pm_massless_minimal(D)
    assert hp == D - 1
    assert hm == 0


def test_h_pm_massive_formula() -> None:
    D = sp.Symbol("D")
    mu2 = sp.Symbol("m2_over_h2")
    hp, hm = h_pm_massive(D, mu2)
    expected_nu = sp.sqrt((D - 1) ** 2 / 4 - mu2)
    assert sp.simplify(hp - ((D - 1) / 2 + expected_nu)) == 0
    assert sp.simplify(hm - ((D - 1) / 2 - expected_nu)) == 0


def test_conformal_kernel_reduction_is_exact() -> None:
    u = sp.Symbol("u")
    D = sp.Symbol("D")
    mismatch = verify_conformal_kernel_reduction(u=u, D=D)
    assert mismatch == 0


def test_kernel_functions_match_for_conformal_branch() -> None:
    u = sp.Symbol("u")
    D = sp.Symbol("D")
    hp, hm = h_pm_conformal_scalar(D)
    aj = allen_jacobson_kernel(u, D, hp, hm)
    closed = conformal_closed_form_kernel(u, D)
    assert sp.simplify(sp.expand_func(aj) - closed) == 0


def test_branch_status_table_matches_gate3_spec() -> None:
    rows = branch_table_rows()
    status_by_branch = {row["branch"]: row["status"] for row in rows}
    assert status_by_branch["conformal_closed_form"] == "benchmark"
    assert status_by_branch["massive_regulated"] == "candidate"
    assert status_by_branch["hminus_direct_limit"] == "blocked until validated"
    assert status_by_branch["hminus_derivative_regularized"] == "investigate"
    assert status_by_branch["mmc_massless"] == "likely blocked"


def test_branch_promotion_status_table_matches_gate3_spec() -> None:
    rows = branch_table_rows()
    promotion_by_branch = {row["branch"]: row["promotion_status"] for row in rows}
    assert promotion_by_branch["conformal_closed_form"] == "not target"
    assert promotion_by_branch["massive_regulated"] == "possible"
    assert promotion_by_branch["hminus_direct_limit"] == "blocked until validated"
    assert promotion_by_branch["hminus_derivative_regularized"] == "investigate"
    assert promotion_by_branch["mmc_massless"] == "blocked"


def test_allowed_branch_ids_exact_set() -> None:
    assert allowed_branch_ids() == [
        "conformal_closed_form",
        "hminus_derivative_regularized",
        "hminus_direct_limit",
        "massive_regulated",
        "mmc_massless",
    ]


def test_select_branch_returns_concrete_object() -> None:
    selected = select_branch("hminus_derivative_regularized")
    assert selected.branch_id == "hminus_derivative_regularized"
    assert selected.promotion_status == "investigate"


def test_select_branch_rejects_invalid_id() -> None:
    with pytest.raises(ValueError) as exc_info:
        select_branch("invalid_branch")
    assert "invalid branch_id" in str(exc_info.value)


def test_build_branch_table_contains_five_branches() -> None:
    table = build_branch_table()
    assert len(table) == 5


def test_validate_m2_over_h2_accepts_positive_decimal() -> None:
    is_valid, msg = validate_m2_over_h2("0.5")
    assert is_valid
    assert msg == ""


def test_validate_m2_over_h2_accepts_positive_integer() -> None:
    is_valid, msg = validate_m2_over_h2("1")
    assert is_valid
    assert msg == ""


def test_validate_m2_over_h2_rejects_zero() -> None:
    is_valid, msg = validate_m2_over_h2("0")
    assert not is_valid
    assert "must be positive" in msg


def test_validate_m2_over_h2_rejects_negative() -> None:
    is_valid, msg = validate_m2_over_h2("-0.5")
    assert not is_valid
    assert "must be positive" in msg


def test_validate_m2_over_h2_rejects_empty() -> None:
    is_valid, msg = validate_m2_over_h2("")
    assert not is_valid
    assert "empty" in msg.lower()


def test_validate_m2_over_h2_rejects_non_numeric() -> None:
    is_valid, msg = validate_m2_over_h2("abc")
    assert not is_valid
    assert "not numeric" in msg
