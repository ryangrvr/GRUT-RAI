"""Structural contraction rules for TT sector."""

from typing import Dict, List


def define_tt_contraction_rules() -> Dict[str, object]:
    allowed: List[str] = [
        "metric_contraction",
        "projector_contraction",
        "index_pairing_mu_nu",
        "index_pairing_alpha_beta",
    ]
    forbidden: List[str] = [
        "trace_with_non_tt",
        "drop_projector",
        "cross_sector_contraction",
    ]

    return {
        "rules_id": "tt_contraction_rules",
        "allowed": allowed,
        "forbidden": forbidden,
        "requires_projector": True,
        "status": "defined_structural",
        "promotes_claims": False,
    }
