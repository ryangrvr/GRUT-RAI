from grut.hard_theory.s4_ctp_solver.gate3_euler_coefficient_extraction import (
    EulerCoefficientResult,
)
from grut.hard_theory.s4_ctp_solver.gate3_r_quotient_classifier import (
    classify_gate3_r_quotient,
)


def _result(
    *,
    name: str,
    status: str,
    value,
    channel: str = "Euler",
    scheme: str = "OR4-approved",
    regulator: str = "D=4-2epsilon",
    protected: bool = True,
    manual_target_matched: bool = False,
) -> EulerCoefficientResult:
    return EulerCoefficientResult(
        coefficient_name=name,
        channel=channel,
        value=value,
        epsilon_pole=None,
        finite_part=value,
        scheme=scheme,
        regulator=regulator,
        protected=protected,
        status=status,
        blocker=None if status != "blocked" else "blocked",
        local_vs_nonlocal_role="protected_nonlocal_R_log_box_R",
        round_s4_projection=True,
        euler_only_condition_w2_zero=True,
        massless_or_conformal_limit="massless-minimal",
        manual_target_matched=manual_target_matched,
        provenance="test",
    )


def test_blocked_when_coefficients_are_blocked() -> None:
    out = classify_gate3_r_quotient(
        cosmo=_result(name="C_Euler_cosmo", status="blocked", value=None),
        final=_result(name="C_Euler_final", status="blocked", value=None),
    )
    assert out["classification"] == "blocked"
    assert out["R_3loop"] is None


def test_scheme_illegal_on_mismatch() -> None:
    out = classify_gate3_r_quotient(
        cosmo=_result(name="C_Euler_cosmo", status="computed", value=1.0, scheme="A"),
        final=_result(name="C_Euler_final", status="computed", value=1.0, scheme="B"),
    )
    assert out["classification"] == "scheme_illegal"


def test_computed_candidate_only_when_valid_and_replicated() -> None:
    out = classify_gate3_r_quotient(
        cosmo=_result(name="C_Euler_cosmo", status="computed", value=1.154700538),
        final=_result(name="C_Euler_final", status="computed", value=1.0),
        replicated=True,
    )
    assert out["classification"] == "computed_candidate"
    assert out["R_3loop"] is not None


def test_needs_replication_when_single_route_number_exists() -> None:
    out = classify_gate3_r_quotient(
        cosmo=_result(name="C_Euler_cosmo", status="computed", value=1.154700538),
        final=_result(name="C_Euler_final", status="computed", value=1.0),
        replicated=False,
    )
    assert out["classification"] == "needs_replication"


def test_honest_negative_for_undefined_ratio() -> None:
    out = classify_gate3_r_quotient(
        cosmo=_result(name="C_Euler_cosmo", status="computed", value=0.0),
        final=_result(name="C_Euler_final", status="computed", value=0.0),
        replicated=True,
    )
    assert out["classification"] == "honest_negative"
