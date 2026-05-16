"""Gate 3 coefficient landing interface with strict provenance checks."""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, Optional

import sympy as sp

from grut.hard_theory.s4_ctp_solver.gate3_euler_coefficient_extraction import (
    EulerCoefficientResult,
)


def _is_resolved_scalar(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return False
    if isinstance(value, (int, float)):
        return True
    if isinstance(value, sp.Basic):
        return bool(value.is_number) and not value.has(sp.Integral, sp.Derivative)
    return False


def _is_resolved_pole_term(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return False
    if isinstance(value, (int, float)):
        return True
    if isinstance(value, sp.Basic):
        epsilon = sp.Symbol("epsilon")
        return value.free_symbols <= {epsilon} and not value.has(sp.Integral, sp.Derivative)
    return False


def _validate_result(result: EulerCoefficientResult) -> Optional[str]:
    if result.channel != "Euler":
        return "non_euler_channel_rejected"
    if result.scheme is None or str(result.scheme).strip() == "":
        return "missing_scheme_metadata"
    if result.regulator is None or str(result.regulator).strip() == "":
        return "missing_regulator_metadata"
    if result.status == "scheme_fragile":
        return "scheme_fragile_rejected"
    if result.manual_target_matched:
        return "manual_target_matching_rejected"
    if not result.round_s4_projection or not result.euler_only_condition_w2_zero:
        return "round_s4_euler_projection_required"
    if result.status == "computed":
        if not _is_resolved_scalar(result.value):
            return "computed_value_not_resolved_scalar"
        if not _is_resolved_scalar(result.finite_part):
            return "computed_finite_part_not_resolved_scalar"
        if result.epsilon_pole is not None and not _is_resolved_pole_term(result.epsilon_pole):
            return "computed_epsilon_pole_not_resolved_scalar"
    return None


def land_gate3_coefficients(
    *,
    cosmo: EulerCoefficientResult,
    final: EulerCoefficientResult,
    raw_r_value: Optional[float] = None,
) -> Dict[str, Any]:
    """Accept only structured coefficient objects with valid provenance metadata."""
    if raw_r_value is not None:
        return {
            "accepted": False,
            "status": "rejected",
            "reason": "raw_hard_coded_r_rejected",
            "promotes_claims": False,
        }

    cosmo_error = _validate_result(cosmo)
    if cosmo_error:
        return {
            "accepted": False,
            "status": "rejected",
            "reason": cosmo_error,
            "coefficient": "C_Euler_cosmo",
            "promotes_claims": False,
        }

    final_error = _validate_result(final)
    if final_error:
        return {
            "accepted": False,
            "status": "rejected",
            "reason": final_error,
            "coefficient": "C_Euler_final",
            "promotes_claims": False,
        }

    if cosmo.status == "blocked" or final.status == "blocked":
        return {
            "accepted": True,
            "status": "blocked",
            "reason": "blocked_result_accepted_with_provenance",
            "coefficients": {
                "C_Euler_cosmo": asdict(cosmo),
                "C_Euler_final": asdict(final),
            },
            "promotes_claims": False,
        }

    return {
        "accepted": True,
        "status": "accepted",
        "reason": "structured_provenance_valid",
        "coefficients": {
            "C_Euler_cosmo": asdict(cosmo),
            "C_Euler_final": asdict(final),
        },
        "promotes_claims": False,
    }
