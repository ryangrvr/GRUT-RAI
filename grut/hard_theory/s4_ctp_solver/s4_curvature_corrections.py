"""Consistency checks for Stage 4C curved subsets."""

from typing import Dict


def check_flat_limit(result: Dict[str, object]) -> Dict[str, object]:
    if result.get("flat_limit_reference"):
        return {
            "check": "flat_limit",
            "status": "consistent",
            "reason": "flat-limit reference present",
            "promotes_claims": False,
        }
    return {
        "check": "flat_limit",
        "status": "inconclusive",
        "reason": "no flat-limit reference",
        "promotes_claims": False,
    }


def check_small_curvature_limit(result: Dict[str, object]) -> Dict[str, object]:
    if result.get("method") == "curvature_expansion":
        return {
            "check": "small_curvature",
            "status": "consistent",
            "reason": "curvature expansion provided",
            "promotes_claims": False,
        }
    return {
        "check": "small_curvature",
        "status": "inconclusive",
        "reason": "no curvature expansion",
        "promotes_claims": False,
    }


def check_scaling_behavior(result: Dict[str, object]) -> Dict[str, object]:
    if result.get("method") in {"spectral_truncation", "curvature_expansion"}:
        return {
            "check": "scaling_behavior",
            "status": "inconclusive",
            "reason": "scaling not fully evaluated",
            "promotes_claims": False,
        }
    return {
        "check": "scaling_behavior",
        "status": "inconclusive",
        "reason": "no scaling check",
        "promotes_claims": False,
    }
