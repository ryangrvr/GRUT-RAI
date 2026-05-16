"""
Coefficient landing interface for the Euler-channel 3-loop R extraction.

This is the ONLY place in the codebase where C_Euler_cosmo and C_Euler_final
may be injected.  All other coefficient_value fields remain None until this
module has been called with validated, OR4-compliant inputs.

Usage
-----
from grut.hard_theory.s4_ctp_solver.euler_coefficient_landing import (
    land_euler_coefficients,
)

report = land_euler_coefficients(
    C_Euler_cosmo = <float or Fraction>,
    C_Euler_final = <float or Fraction>,
    source        = "Mathematica/HypExp v2 — TJI_PHASE_1_CALCULATION_PLAN.md §3",
    scheme        = "OR4-approved",
    regulator     = "dimreg D=4-2eps",
    projection    = "round-S4 Euler channel",
)
"""

from __future__ import annotations

import math
from typing import Optional, Union

# ---------------------------------------------------------------------------
# OR4 validation constants
# ---------------------------------------------------------------------------
_REQUIRED_SCHEME     = "OR4-approved"
_REQUIRED_REGULATOR  = "dimreg D=4-2eps"
_REQUIRED_PROJECTION = "round-S4 Euler channel"

_R_PROTECTED         = math.sqrt(4.0 / 3.0)   # ≈ 1.15470
_R_TOLERANCE         = 0.001                   # 0.1 % — agreement required for promotion

# Type alias
_Coeff = Optional[Union[float, int]]


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _validate_provenance(source, scheme, regulator, projection):
    """Return a list of error strings.  Empty list = valid."""
    errors = []
    if scheme != _REQUIRED_SCHEME:
        errors.append(
            f"scheme '{scheme}' is not OR4-approved "
            f"(required: '{_REQUIRED_SCHEME}')."
        )
    if regulator != _REQUIRED_REGULATOR:
        errors.append(
            f"regulator '{regulator}' is not accepted "
            f"(required: '{_REQUIRED_REGULATOR}')."
        )
    if projection != _REQUIRED_PROJECTION:
        errors.append(
            f"projection '{projection}' is not accepted "
            f"(required: '{_REQUIRED_PROJECTION}')."
        )
    if source is None or str(source).strip() == "":
        errors.append("source must be a non-empty string identifying the Mathematica notebook.")
    return errors


def _apply_decision_table(C_cosmo: _Coeff, C_final: _Coeff, validation_errors):
    """
    Apply the hard decision table.

    Returns (decision, route_status, promotes_claims, note).
    """
    if validation_errors:
        return (
            "r_illegal",
            "scheme_contaminated_or_bad_provenance",
            False,
            "FAIL: " + "; ".join(validation_errors),
        )

    if C_cosmo is None or C_final is None:
        return (
            "deferred",
            "open_symbolic_only",
            False,
            "DEFERRED: coefficient values are null. Pipeline remains symbolic-only.",
        )

    if C_final == 0:
        return (
            "honest_negative",
            "3loop_route_honest_negative",
            False,
            "HONEST NEGATIVE: C_Euler_final = 0 — quotient undefined.",
        )

    try:
        r_ratio = math.sqrt(float(C_cosmo) / float(C_final))
    except (ValueError, ZeroDivisionError, TypeError) as exc:
        return (
            "honest_negative",
            "3loop_route_honest_negative",
            False,
            f"HONEST NEGATIVE: quotient formation failed ({exc}).",
        )

    rel_diff = abs(r_ratio - _R_PROTECTED) / _R_PROTECTED

    if rel_diff <= _R_TOLERANCE:
        return (
            "computed_candidate",
            "3loop_route_computed_candidate",
            True,
            (
                f"PASS: R_ratio = sqrt({C_cosmo}/{C_final}) = {r_ratio:.8f} agrees with "
                f"sqrt(4/3) = {_R_PROTECTED:.8f} to {rel_diff * 100:.4f} %. "
                "3-loop route promoted to computed-candidate."
            ),
        )
    else:
        return (
            "update_r_route",
            "different_protected_coefficients",
            False,
            (
                f"UNEXPECTED: R_ratio = {r_ratio:.8f} differs from sqrt(4/3) by "
                f"{rel_diff * 100:.4f} %. Update R route — no cherry-picking."
            ),
        )


# ---------------------------------------------------------------------------
# Public interface
# ---------------------------------------------------------------------------

def land_euler_coefficients(
    C_Euler_cosmo: _Coeff = None,
    C_Euler_final: _Coeff = None,
    *,
    source: Optional[str] = None,
    scheme: str = _REQUIRED_SCHEME,
    regulator: str = _REQUIRED_REGULATOR,
    projection: str = _REQUIRED_PROJECTION,
) -> dict:
    """
    Accept Euler-channel coefficients from an OR4-compliant external computation
    and apply the hard pass/fail decision table.

    Parameters
    ----------
    C_Euler_cosmo : float | int | None
        Finite-part (ε⁰) coefficient for the cosmological-constant Euler-anomaly term.
        Leave as None if the computation is incomplete or failed.
    C_Euler_final : float | int | None
        Finite-part (ε⁰) coefficient for the C_Final Euler-anomaly term.
        Leave as None if the computation is incomplete or failed.
    source : str | None
        Human-readable identifier of the Mathematica/HypExp notebook and version.
    scheme : str
        Must be "OR4-approved" (or an explicit OR4-registered dim-reg scheme name).
    regulator : str
        Must be "dimreg D=4-2eps".
    projection : str
        Must be "round-S4 Euler channel".

    Returns
    -------
    dict with keys:
        C_Euler_cosmo       — value passed in (or None)
        C_Euler_final       — value passed in (or None)
        R_ratio             — float if computable, else None
        decision            — one of: deferred / r_illegal / honest_negative /
                              update_r_route / computed_candidate
        route_status        — string label for the current 3-loop route state
        promotes_claims     — bool; True ONLY for "computed_candidate"
        audit_record        — human-readable decision note
        provenance          — dict of the metadata fields used
        validation_errors   — list[str]; empty if provenance is valid
    """
    # Null shortcut: if both coefficients are absent no provenance is needed yet
    if C_Euler_cosmo is None and C_Euler_final is None:
        return {
            "C_Euler_cosmo": None,
            "C_Euler_final": None,
            "R_ratio": None,
            "decision": "deferred",
            "route_status": "open_symbolic_only",
            "promotes_claims": False,
            "audit_record": (
                "DEFERRED: coefficient values are null. "
                "Pipeline remains symbolic-only. "
                "Populate C_Euler_cosmo and C_Euler_final to proceed."
            ),
            "provenance": {
                "source": source,
                "scheme": scheme,
                "regulator": regulator,
                "projection": projection,
            },
            "validation_errors": [],
            "two_loop_separation": {
                "two_loop_result": 1.1498,
                "two_loop_tag": "independent-2-loop-anomaly-ratio",
                "may_fill_C_Euler_cosmo": False,
                "may_fill_C_Euler_final": False,
                "note": (
                    "Independent 2-loop extraction / nearby anomaly-ratio result. "
                    "Not proof of the 3-loop value. Do not merge."
                ),
            },
        }

    validation_errors = _validate_provenance(source, scheme, regulator, projection)

    # Compute R_ratio only if both coefficients are present and provenance is valid
    r_ratio = None
    if not validation_errors and C_Euler_cosmo is not None and C_Euler_final is not None:
        if C_Euler_final != 0:
            try:
                r_ratio = math.sqrt(float(C_Euler_cosmo) / float(C_Euler_final))
            except Exception:
                pass

    decision, route_status, promotes_claims, audit_record = _apply_decision_table(
        C_Euler_cosmo, C_Euler_final, validation_errors
    )

    return {
        "C_Euler_cosmo": C_Euler_cosmo,
        "C_Euler_final": C_Euler_final,
        "R_ratio": r_ratio,
        "decision": decision,
        "route_status": route_status,
        "promotes_claims": promotes_claims,
        "audit_record": audit_record,
        "provenance": {
            "source": source,
            "scheme": scheme,
            "regulator": regulator,
            "projection": projection,
        },
        "validation_errors": validation_errors,
        # Two-loop separation guard — never filled from this module
        "two_loop_separation": {
            "two_loop_result": 1.1498,
            "two_loop_tag": "independent-2-loop-anomaly-ratio",
            "may_fill_C_Euler_cosmo": False,
            "may_fill_C_Euler_final": False,
            "note": (
                "Independent 2-loop extraction / nearby anomaly-ratio result. "
                "Not proof of the 3-loop value. Do not merge."
            ),
        },
    }
