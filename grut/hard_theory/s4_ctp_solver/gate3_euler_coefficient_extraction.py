"""Gate 3 protected Euler-channel coefficient extraction driver.

This module attempts only what can be honestly done in Python/SymPy.
If extraction is not tractable, it returns structured BLOCKED results.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Dict, Optional

import sympy as sp

from grut.derivation.tji.allen_jacobson import (
    S4CurvatureObstacle,
    s4_propagator,
    tji_on_s4,
)


@dataclass(frozen=True)
class EulerCoefficientResult:
    coefficient_name: str
    channel: str
    value: Optional[Any]
    epsilon_pole: Optional[Any]
    finite_part: Optional[Any]
    scheme: str
    regulator: str
    protected: bool
    status: str  # computed | blocked | scheme_fragile | invalid
    blocker: Optional[str]
    local_vs_nonlocal_role: str
    round_s4_projection: bool
    euler_only_condition_w2_zero: bool
    massless_or_conformal_limit: str
    manual_target_matched: bool
    provenance: str


def define_euler_channel_integral() -> Dict[str, Any]:
    """Define the symbolic Gate 3 integral target and metadata."""
    eps = sp.Symbol("epsilon", positive=True)
    D = 4 - 2 * eps
    Z = sp.Symbol("Z", real=True)

    h_plus, h_minus = sp.symbols("h_plus h_minus")
    z_arg = (1 + Z) / 2
    hyper = sp.hyper([h_plus, h_minus], [D / 2], z_arg)
    integrand = hyper**3 * (1 - Z**2) ** ((D - 3) / 2)

    return {
        "integral_name": "I_Euler_round_S4",
        "integrand": integrand,
        "integration_variable": Z,
        "integration_domain": (-1, 1),
        "D": D,
        "epsilon": eps,
        "h_plus": h_plus,
        "h_minus": h_minus,
        "z_argument": z_arg,
        "regulator": "D=4-2epsilon",
        "round_s4_projection": True,
        "euler_only_condition_w2_zero": True,
        "local_vs_nonlocal_role": "Euler-channel protected quotient input",
    }


def _blocked_result(coefficient_name: str, blocker: str) -> EulerCoefficientResult:
    return EulerCoefficientResult(
        coefficient_name=coefficient_name,
        channel="Euler",
        value=None,
        epsilon_pole=None,
        finite_part=None,
        scheme="OR4-approved",
        regulator="D=4-2epsilon",
        protected=True,
        status="blocked",
        blocker=blocker,
        local_vs_nonlocal_role="protected_nonlocal_R_log_box_R",
        round_s4_projection=True,
        euler_only_condition_w2_zero=True,
        massless_or_conformal_limit="massless-minimal (requested); conformal sanity path exists",
        manual_target_matched=False,
        provenance="python_sympy_attempt",
    )


def attempt_euler_coefficient_extraction(coefficient_name: str) -> EulerCoefficientResult:
    """Attempt extraction in Python/SymPy and return honest structured status."""
    try:
        # This call is expected to raise the known obstacle for minimal coupling.
        _ = tji_on_s4(
            D=sp.Symbol("D"),
            k_squared=0,
            indices=((1, 0), (1, 0), (1, 0)),
            H_inf=1.0,
        )
    except S4CurvatureObstacle as exc:
        return _blocked_result(
            coefficient_name,
            (
                "Allen-Jacobson hypergeometric cube integral and Laurent extraction "
                "around D=4-2epsilon remain blocked in SymPy; Mathematica+HypExp required. "
                f"Details: {exc}"
            ),
        )
    except Exception as exc:  # pragma: no cover
        return _blocked_result(
            coefficient_name,
            f"Unexpected symbolic failure during extraction attempt: {exc}",
        )

    # Defensive fallback: if no obstacle occurred, still avoid inventing values.
    return EulerCoefficientResult(
        coefficient_name=coefficient_name,
        channel="Euler",
        value=None,
        epsilon_pole=None,
        finite_part=None,
        scheme="OR4-approved",
        regulator="D=4-2epsilon",
        protected=True,
        status="blocked",
        blocker="No validated finite-part extraction pipeline available in SymPy.",
        local_vs_nonlocal_role="protected_nonlocal_R_log_box_R",
        round_s4_projection=True,
        euler_only_condition_w2_zero=True,
        massless_or_conformal_limit="massless-minimal",
        manual_target_matched=False,
        provenance="python_sympy_attempt",
    )


def run_gate3_euler_coefficient_extraction() -> Dict[str, Any]:
    """Run Gate 3 extraction attempts for cosmo/final Euler coefficients."""
    integral_spec = define_euler_channel_integral()

    # Touch existing propagator interface to ensure dependency alignment.
    Z = sp.Symbol("Z", real=True)
    _aj_expr = s4_propagator(Z=Z, D=4 - 2 * sp.Symbol("epsilon", positive=True), m_squared=0, H_inf=1)

    cosmo = attempt_euler_coefficient_extraction("C_Euler_cosmo")
    final = attempt_euler_coefficient_extraction("C_Euler_final")

    return {
        "stage": "gate3_euler_coefficient_extraction",
        "integral_spec": integral_spec,
        "allen_jacobson_symbolic_expression": _aj_expr,
        "results": {
            "C_Euler_cosmo": asdict(cosmo),
            "C_Euler_final": asdict(final),
        },
        "coefficients_computed": (
            cosmo.status == "computed"
            and final.status == "computed"
            and cosmo.value is not None
            and final.value is not None
        ),
        "promotes_claims": False,
    }
