"""Gate 3 R quotient classifier for protected Euler-channel extraction."""

from __future__ import annotations

import math
from typing import Any, Dict, Optional

from grut.hard_theory.s4_ctp_solver.gate3_euler_coefficient_extraction import (
    EulerCoefficientResult,
)


def _compatible_scheme_and_regulator(
    cosmo: EulerCoefficientResult,
    final: EulerCoefficientResult,
) -> bool:
    return cosmo.scheme == final.scheme and cosmo.regulator == final.regulator


def classify_gate3_r_quotient(
    *,
    cosmo: EulerCoefficientResult,
    final: EulerCoefficientResult,
    replicated: bool = False,
    osborn_local_rg: Optional[float] = 1.15367,
) -> Dict[str, Any]:
    """Classify Gate 3 quotient status under strict legality gates."""
    canonical = math.sqrt(4.0 / 3.0)
    loop_target = 1.15428

    # Blocked path
    if cosmo.status == "blocked" or final.status == "blocked":
        return {
            "classification": "blocked",
            "R_3loop": None,
            "comparison": {
                "sqrt_4_over_3": canonical,
                "loop_target_1_15428": loop_target,
                "osborn_local_rg": osborn_local_rg,
            },
            "legal_for_promotion": False,
            "promotes_claims": False,
            "reason": "integral_still_blocked_or_coefficients_unavailable",
        }

    # Scheme legality path
    if (
        cosmo.status == "scheme_fragile"
        or final.status == "scheme_fragile"
        or not _compatible_scheme_and_regulator(cosmo, final)
        or not cosmo.protected
        or not final.protected
    ):
        return {
            "classification": "scheme_illegal",
            "R_3loop": None,
            "comparison": {
                "sqrt_4_over_3": canonical,
                "loop_target_1_15428": loop_target,
                "osborn_local_rg": osborn_local_rg,
            },
            "legal_for_promotion": False,
            "promotes_claims": False,
            "reason": "scheme_or_protection_incompatibility",
        }

    # Null / invalid quotient path
    if cosmo.value is None or final.value is None:
        return {
            "classification": "honest_negative",
            "R_3loop": None,
            "comparison": {
                "sqrt_4_over_3": canonical,
                "loop_target_1_15428": loop_target,
                "osborn_local_rg": osborn_local_rg,
            },
            "legal_for_promotion": False,
            "promotes_claims": False,
            "reason": "undefined_or_null_coefficient_value",
        }

    try:
        ratio = float(cosmo.value) / float(final.value)
        if not math.isfinite(ratio) or ratio <= 0.0:
            raise ValueError("non-positive quotient")
        r_3loop = ratio
    except Exception:
        return {
            "classification": "honest_negative",
            "R_3loop": None,
            "comparison": {
                "sqrt_4_over_3": canonical,
                "loop_target_1_15428": loop_target,
                "osborn_local_rg": osborn_local_rg,
            },
            "legal_for_promotion": False,
            "promotes_claims": False,
            "reason": "quotient_failed",
        }

    comparison = {
        "sqrt_4_over_3": canonical,
        "loop_target_1_15428": loop_target,
        "osborn_local_rg": osborn_local_rg,
        "delta_vs_sqrt_4_over_3": r_3loop - canonical,
        "delta_vs_loop_target": r_3loop - loop_target,
        "delta_vs_osborn": None if osborn_local_rg is None else (r_3loop - osborn_local_rg),
    }

    if not replicated:
        return {
            "classification": "needs_replication",
            "R_3loop": r_3loop,
            "comparison": comparison,
            "legal_for_promotion": False,
            "promotes_claims": False,
            "reason": "single_route_only",
        }

    return {
        "classification": "computed_candidate",
        "R_3loop": r_3loop,
        "comparison": comparison,
        "legal_for_promotion": True,
        "promotes_claims": False,
        "reason": "both_protected_coefficients_valid_and_compatible",
    }
