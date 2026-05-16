"""Define scheme-stability rules for coefficient candidates."""

from typing import Dict


def define_scheme_stability_rules() -> Dict[str, object]:
    return {
        "rules_id": "scheme_stability_rules_v1",
        "r_route_allowed_only_if": [
            "numerator_scheme_protected",
            "denominator_scheme_protected",
            "same_scheme_family",
            "no_unresolved_local_fragile_terms",
        ],
        "promotes_claims": False,
    }
