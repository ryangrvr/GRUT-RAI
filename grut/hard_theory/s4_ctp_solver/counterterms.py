"""Counterterm registry for Stage 3D renormalization audits."""

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class CountertermRecord:
    counterterm_id: str
    invariant: str
    coupling_symbol: str
    mass_dimension: int
    scheme_dependence: str
    status: str


def counterterm_registry() -> Dict[str, CountertermRecord]:
    return {
        "cosmological_constant_counterterm": CountertermRecord(
            counterterm_id="cosmological_constant_counterterm",
            invariant="1",
            coupling_symbol="delta_Lambda",
            mass_dimension=4,
            scheme_dependence="scheme_dependent",
            status="registered_not_evaluated",
        ),
        "einstein_hilbert_counterterm": CountertermRecord(
            counterterm_id="einstein_hilbert_counterterm",
            invariant="R",
            coupling_symbol="delta_1_over_G",
            mass_dimension=2,
            scheme_dependence="scheme_dependent",
            status="registered_not_evaluated",
        ),
        "R_squared_counterterm": CountertermRecord(
            counterterm_id="R_squared_counterterm",
            invariant="R^2",
            coupling_symbol="delta_alpha_R2",
            mass_dimension=0,
            scheme_dependence="scheme_dependent",
            status="registered_not_evaluated",
        ),
        "Ricci_squared_counterterm": CountertermRecord(
            counterterm_id="Ricci_squared_counterterm",
            invariant="R_{μν}R^{μν}",
            coupling_symbol="delta_alpha_Ricci2",
            mass_dimension=0,
            scheme_dependence="scheme_dependent",
            status="registered_not_evaluated",
        ),
        "Riemann_squared_counterterm": CountertermRecord(
            counterterm_id="Riemann_squared_counterterm",
            invariant="R_{μνρσ}R^{μνρσ}",
            coupling_symbol="delta_alpha_Riemann2",
            mass_dimension=0,
            scheme_dependence="scheme_dependent",
            status="registered_not_evaluated",
        ),
        "Euler_density_counterterm": CountertermRecord(
            counterterm_id="Euler_density_counterterm",
            invariant="E4",
            coupling_symbol="delta_alpha_E4",
            mass_dimension=0,
            scheme_dependence="topological_or_scheme_invariant_candidate",
            status="registered_not_evaluated",
        ),
        "Weyl_squared_counterterm": CountertermRecord(
            counterterm_id="Weyl_squared_counterterm",
            invariant="W^2",
            coupling_symbol="delta_alpha_W2",
            mass_dimension=0,
            scheme_dependence="topological_or_scheme_invariant_candidate",
            status="registered_not_evaluated",
        ),
        "box_R_counterterm": CountertermRecord(
            counterterm_id="box_R_counterterm",
            invariant="□R",
            coupling_symbol="delta_alpha_boxR",
            mass_dimension=0,
            scheme_dependence="total_derivative_scheme_dependent",
            status="registered_not_evaluated",
        ),
    }
