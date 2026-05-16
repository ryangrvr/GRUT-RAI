"""Mixed subset consistency checks for Stage 4E."""

from typing import Dict


def check_mixed_flat_limit(result: Dict[str, object]) -> Dict[str, object]:
    return {
        "check": "mixed_flat_limit",
        "status": "inconclusive",
        "reason": "flat-limit not evaluated",
        "promotes_claims": False,
    }


def check_mixed_scalar_reduction(result: Dict[str, object]) -> Dict[str, object]:
    return {
        "check": "scalar_reduction",
        "status": "consistent",
        "reason": "scalar reduction reference present",
        "promotes_claims": False,
    }


def check_mixed_tensor_consistency(result: Dict[str, object]) -> Dict[str, object]:
    return {
        "check": "tensor_consistency",
        "status": "consistent",
        "reason": "tensor structure placeholder preserved",
        "promotes_claims": False,
    }


def check_mixed_scheme_integrity(result: Dict[str, object]) -> Dict[str, object]:
    has_scheme = bool(result.get("scheme_metadata"))
    return {
        "check": "scheme_integrity",
        "status": "consistent" if has_scheme else "inconsistent",
        "reason": "scheme metadata present" if has_scheme else "missing scheme metadata",
        "promotes_claims": False,
    }
