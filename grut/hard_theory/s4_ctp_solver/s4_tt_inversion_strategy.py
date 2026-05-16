"""Spectral inversion strategy for TT propagator on S4 (formal only)."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.s4_tt_mode_decomposition import (
    define_tt_mode_decomposition,
)
from grut.hard_theory.s4_ctp_solver.s4_tt_eigenvalues import define_tt_eigenvalues
from grut.hard_theory.s4_ctp_solver.s4_tt_degeneracies import define_tt_degeneracies
from grut.hard_theory.s4_ctp_solver.s4_tt_zero_mode_handling import (
    define_zero_mode_strategy,
)


def define_spectral_inversion_strategy() -> Dict[str, object]:
    decomposition = define_tt_mode_decomposition()
    eigenvalues = define_tt_eigenvalues()
    degeneracies = define_tt_degeneracies()
    zero_modes = define_zero_mode_strategy()

    components: List[Dict[str, object]] = [
        decomposition,
        eigenvalues,
        degeneracies,
        zero_modes,
    ]

    return {
        "strategy_id": "s4_tt_spectral_inversion",
        "formula": "sum_over_l (deg_l / eigenvalue_l) * projector_l",
        "components": components,
        "convergence_requirements": [
            "large-l asymptotics",
            "regularization scheme",
            "mode cutoff handling",
        ],
        "regularization_placeholder": "dim_reg_or_zeta_placeholder",
        "status": "strategy_defined_not_executed",
        "promotes_claims": False,
    }
