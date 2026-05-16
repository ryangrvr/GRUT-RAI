"""Finite-part eligibility requirements (structural)."""

from typing import Dict, List


def define_finite_part_requirements() -> Dict[str, object]:
    requirements: List[str] = [
        "all divergences mapped to known counterterms",
        "no unmapped divergence structures",
        "scheme alignment at least partial with invariant coverage",
        "regularization produces stable behavior",
        "inversion preserves tensor structure",
        "no unresolved failure modes from Stage 7D",
    ]

    return {
        "requirements": requirements,
        "status": "defined",
        "promotes_claims": False,
    }
