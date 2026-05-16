"""Define regulator handling strategy for the dry-run plan."""

from typing import Dict


def define_regulator_handling() -> Dict[str, object]:
    return {
        "regulator_strategy": "attach_symbolic_regulator_then_limit",
        "limit_process": "symbolic_only",
        "scheme_dependent": True,
        "status": "regulator_strategy_defined",
        "promotes_claims": False,
    }
