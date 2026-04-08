"""
GRUT Solver — The Main API

Given (m, R, l, T, P), compute ALL decoherence channels, compare models,
run adversarial kill tests, and assess experimental testability.

Zero free parameters in the gravitational prediction.
"""

from __future__ import annotations
import numpy as np
from dataclasses import dataclass
from typing import Optional

from grut_solver.constants import G, HBAR, AMU
from grut_solver.usl.gravitational import lambda_grav, lambda_grav_point, boundary_mass, suppression_factor
from grut_solver.usl.anomaly import lambda_anomaly
from grut_solver.usl.scaling import crossover_pressure
from grut_solver.budget.total import compute_budget, budget_with_uncertainty, BudgetResult
from grut_solver.kill.model_comparison import run_all_kill_tests, kill_summary, KillResult


@dataclass
class DecoherenceResult:
    """Complete decoherence analysis for a physical system."""
    # Inputs
    m: float; R: float; l: float; T_env: float; P: float

    # Budget
    budget: BudgetResult

    # Key rates
    lambda_grav: float
    lambda_total: float
    t_coherence: float
    binding_channel: str
    signal_to_noise: float
    is_grav_dominated: bool

    # Competing models
    lambda_dp_point: float
    lambda_csl_grw: float
    lambda_csl_adler: float

    # Extended body
    S_extended: float
    suppression_x: float  # 1/S = how much point-mass overestimates

    # Testability
    is_testable: bool  # SNR > 1 means grav signal exceeds environment


class GRUTSolver:
    """The monster physics solver."""

    def decoherence(
        self,
        m: float,
        R: float,
        l: float,
        T_env: float = 4.0,
        P: float = 1e-10,
        **kwargs,
    ) -> DecoherenceResult:
        """Compute ALL decoherence channels for given parameters.

        Parameters
        ----------
        m : float       Mass [kg].
        R : float       Radius [m].
        l : float       Superposition separation [m].
        T_env : float   Environment temperature [K].
        P : float       Gas pressure [Pa].
        **kwargs        Passed to compute_budget (T_int, P_laser, etc.)

        Returns
        -------
        DecoherenceResult with every channel, comparisons, and testability.
        """
        budget = compute_budget(m, R, l, T_env, P, **kwargs)

        S = suppression_factor(l, R)
        Lg = budget.lambda_grav
        Ldp = lambda_grav_point(m, l)

        # CSL competing models
        from grut_solver.experiments.competing_models import lambda_csl
        Lcsl_grw = lambda_csl(m, l, R, lambda_CSL=1e-16, r_CSL=1e-7)
        Lcsl_adler = lambda_csl(m, l, R, lambda_CSL=1e-8, r_CSL=1e-7)

        return DecoherenceResult(
            m=m, R=R, l=l, T_env=T_env, P=P,
            budget=budget,
            lambda_grav=Lg,
            lambda_total=budget.lambda_total,
            t_coherence=budget.t_coherence,
            binding_channel=budget.binding_channel,
            signal_to_noise=budget.signal_to_noise,
            is_grav_dominated=budget.is_grav_dominated,
            lambda_dp_point=Ldp,
            lambda_csl_grw=Lcsl_grw,
            lambda_csl_adler=Lcsl_adler,
            S_extended=S,
            suppression_x=1.0/S if S > 0 else float('inf'),
            is_testable=budget.signal_to_noise > 1.0,
        )

    def pressure_scan(
        self, m: float, R: float, l: float, T_env: float,
        P_min: float = 1e-14, P_max: float = 1e-6,
        n_points: int = 50, **kwargs,
    ) -> list[DecoherenceResult]:
        """F3 test: scan pressure to find plateau."""
        pressures = np.logspace(np.log10(P_min), np.log10(P_max), n_points)
        return [self.decoherence(m, R, l, T_env, P, **kwargs) for P in pressures]

    def mass_scan(
        self, l: float, rho: float, T_env: float, P: float,
        m_min: float = 1e-18, m_max: float = 1e-10,
        n_points: int = 30, **kwargs,
    ) -> list[DecoherenceResult]:
        """F1 test: scan mass to verify m^2 scaling."""
        masses = np.logspace(np.log10(m_min), np.log10(m_max), n_points)
        results = []
        for m in masses:
            R = (3*m/(4*np.pi*rho))**(1/3)
            results.append(self.decoherence(m, R, l, T_env, P, **kwargs))
        return results

    def radius_scan(
        self, m: float, l: float, T_env: float, P: float,
        densities: dict[str, float] = None, **kwargs,
    ) -> list[DecoherenceResult]:
        """F2 test: scan radius at fixed mass (different densities)."""
        if densities is None:
            from grut_solver.constants import RHO_GOLD, RHO_SILICA, RHO_DIAMOND
            densities = {"aerogel": 100, "polymer": 1000, "silica": 2200,
                         "diamond": 3510, "gold": 19300}
        results = []
        for name, rho in densities.items():
            R = (3*m/(4*np.pi*rho))**(1/3)
            results.append(self.decoherence(m, R, l, T_env, P, **kwargs))
        return results

    def boundary_mass(self, l: float, t_obs: float) -> float:
        """Quantum-classical boundary mass [kg]."""
        return boundary_mass(l, t_obs)

    def crossover_pressure(self, m: float, R: float, l: float, T: float,
                           m_gas: float = None) -> float:
        """Pressure where gas decoherence = gravitational decoherence [Pa]."""
        return crossover_pressure(m, R, l, T, m_gas)

    def compare_models(self, result: DecoherenceResult) -> str:
        """Human-readable comparison of GRUT vs competing models."""
        lines = [
            f"MODEL COMPARISON at m={result.m:.2e} kg, R={result.R*1e9:.0f} nm, l={result.l*1e9:.0f} nm",
            f"  GRUT (0 params):     Lambda = {result.lambda_grav:.2e} Hz  (S = {result.S_extended:.2e})",
            f"  DP point-mass:       Lambda = {result.lambda_dp_point:.2e} Hz  (overestimates by {result.suppression_x:.0f}x)",
            f"  CSL (GRW, 2 params): Lambda = {result.lambda_csl_grw:.2e} Hz",
            f"  CSL (Adler, 2 par):  Lambda = {result.lambda_csl_adler:.2e} Hz",
            f"  Standard QM:         Lambda = 0",
            f"  Environment total:   Lambda = {result.budget.lambda_env:.2e} Hz",
            f"  GRUT SNR:            {result.signal_to_noise:.2f}",
            f"  Testable:            {result.is_testable}",
        ]
        return "\n".join(lines)

    def try_kill(self, model: str = "all", **kwargs) -> list[KillResult] | KillResult:
        """Run adversarial kill tests against GRUT.

        Parameters
        ----------
        model : str
            "all", "constant_floor", "power_law_floor", or "CSL".

        Returns
        -------
        KillResult or list of KillResult.
        """
        from grut_solver.kill.model_comparison import (
            try_kill_constant_floor, try_kill_power_law_floor, try_kill_csl
        )
        l = kwargs.get("l", 100e-9)
        rho = kwargs.get("rho", 2200.0)

        if model == "all":
            return run_all_kill_tests(l, rho)
        elif model == "constant_floor":
            return try_kill_constant_floor(l, rho)
        elif model == "power_law_floor":
            return try_kill_power_law_floor(l, rho)
        elif model == "CSL":
            return try_kill_csl(l, rho)
        else:
            raise ValueError(f"Unknown model: {model}")

    def sensitivity(self, result: DecoherenceResult, vary_pct: float = 10.0) -> BudgetResult:
        """Check robustness: vary inputs by ±vary_pct%, see if conclusions hold."""
        return budget_with_uncertainty(
            result.m, result.R, result.l, result.T_env, result.P,
            vary_pct=vary_pct,
        )

    # =================================================================
    # MANY-BODY / ENTANGLEMENT EXTENSION
    # =================================================================

    def bell_vs_product(self, m: float, l: float, d_AB: float,
                        R: float = None) -> dict:
        """Compare Bell and product state decoherence rates.

        The core many-body prediction: anti-correlated entanglement
        REDUCES gravitational decoherence.

        Parameters
        ----------
        m : float     Mass of each particle [kg].
        l : float     Superposition separation per particle [m].
        d_AB : float  Distance between the two particles [m].
        R : float     Particle radius [m] (optional).

        Returns
        -------
        dict with lambda_product, lambda_bell, percent_difference,
        and three-way discriminant (GRUT vs QM vs CSL).
        """
        from grut_solver.usl.many_body import entanglement_discriminant
        disc = entanglement_discriminant(m, l, d_AB, R)

        disc["three_way_discriminant"] = {
            "standard_QM": "both rates = 0",
            "CSL": "product = Bell (mass-only dependence)",
            "GRUT": f"product > Bell by {abs(disc['percent_difference']):.1f}%",
            "unique_to_GRUT": True,
        }
        return disc

    def entanglement_scan(self, m: float, l: float, R: float = None,
                           d_min: float = None, d_max: float = None,
                           n_points: int = 50) -> list[dict]:
        """Scan the entanglement protection as a function of inter-particle distance.

        Returns the Bell/product fractional difference at each d_AB.
        """
        from grut_solver.usl.many_body import cross_term_scan
        return cross_term_scan(m, l, R, d_min, d_max, n_points)

    def ghz_scaling(self, m: float, l: float, d: float,
                     N_max: int = 20) -> list[dict]:
        """Compute GHZ state suppression as a function of particle number N.

        Returns the GHZ/product ratio for N = 2, 3, ..., N_max.
        """
        from grut_solver.usl.many_body import lambda_n_particle
        from grut_solver.usl.gravitational import lambda_grav

        Lambda_single = lambda_grav(m, l)
        results = []

        for N in range(2, N_max + 1):
            positions_L = [np.array([(i * d) - l/2, 0, 0]) for i in range(N)]
            positions_R = [np.array([(i * d) + l/2, 0, 0]) for i in range(N)]
            L_ghz = lambda_n_particle([m]*N, positions_L, positions_R)
            L_prod = N * Lambda_single

            results.append({
                "N": N,
                "lambda_ghz": L_ghz,
                "lambda_product": L_prod,
                "ratio": L_ghz / L_prod if L_prod > 0 else 0,
                "suppression_pct": (1 - L_ghz / L_prod) * 100 if L_prod > 0 else 0,
            })

        return results
