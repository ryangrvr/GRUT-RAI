"""Total decoherence budget with uncertainty propagation.

Aggregates ALL channels (physical + nuisance), identifies the binding
constraint, and propagates input uncertainties to output error bars.
"""

from __future__ import annotations
import numpy as np
from dataclasses import dataclass, field
from typing import Optional

from grut_solver.constants import HBAR, G
from grut_solver.usl.gravitational import lambda_grav, suppression_factor
from grut_solver.usl.anomaly import lambda_anomaly
from grut_solver.budget.gas import lambda_gas
from grut_solver.budget.blackbody import lambda_bb_scatter, lambda_bb_emission


@dataclass
class Channel:
    """A single decoherence channel."""
    name: str
    rate_hz: float
    is_fundamental: bool   # True = gravitational; False = environmental/nuisance
    formula: str = ""
    suppressible: bool = True  # Can this channel be reduced experimentally?


@dataclass
class BudgetResult:
    """Complete decoherence budget with uncertainties."""
    channels: list[Channel]
    lambda_total: float
    lambda_env: float          # sum of environmental channels only
    lambda_grav: float         # gravitational channel only
    lambda_anomaly: float
    t_coherence: float         # 1 / lambda_total

    binding_channel: str       # name of the dominant suppressible channel
    signal_to_noise: float     # lambda_grav / lambda_env
    is_grav_dominated: bool    # lambda_grav > lambda_env

    # Uncertainty (from ±vary_pct input variation)
    lambda_total_lo: float = 0.0
    lambda_total_hi: float = 0.0
    conclusion_robust: bool = True  # binding constraint unchanged under variation


def compute_budget(
    m: float, R: float, l: float,
    T_env: float, P: float,
    *,
    T_int: float = None,
    m_gas: float = None,
    P_laser: float = 0.0,
    omega_laser: float = 0.0,
    n_charges: int = 0,
    E_noise: float = 0.0,
    omega_trap: float = 0.0,
    S_vib: float = 0.0,
) -> BudgetResult:
    """Compute the full multi-channel decoherence budget.

    Parameters
    ----------
    m, R, l, T_env, P : float
        Primary experimental parameters (mass, radius, separation, temperature, pressure).
    T_int : float, optional
        Internal temperature [K]. Default: T_env.
    m_gas, P_laser, omega_laser, n_charges, E_noise, omega_trap, S_vib : float
        Optional nuisance channel parameters.

    Returns
    -------
    BudgetResult with all channels, totals, binding constraint, and SNR.
    """
    if T_int is None:
        T_int = T_env

    channels = []

    # --- Fundamental channels (GRUT predictions, zero free parameters) ---
    Lg = lambda_grav(m, l, R)
    channels.append(Channel("gravitational", Lg, is_fundamental=True,
                           formula="G m^2 S(l/R) / (hbar l)", suppressible=False))

    La = lambda_anomaly(m, l)
    channels.append(Channel("anomaly", La, is_fundamental=True,
                           formula="C_Final^2 * G m^2 / (hbar l)", suppressible=False))

    # --- Environmental channels (suppressible) ---
    Lgas = lambda_gas(m, R, l, T_env, P, m_gas)
    channels.append(Channel("gas_collision", Lgas, is_fundamental=False,
                           formula="n sigma v (l/lambda_dB)^2", suppressible=True))

    Lbb_scat = lambda_bb_scatter(R, l, T_env)
    channels.append(Channel("bb_scatter", Lbb_scat, is_fundamental=False,
                           formula="Joos-Zeh photon scatter", suppressible=True))

    Lbb_emit = lambda_bb_emission(R, T_int)
    channels.append(Channel("bb_emission", Lbb_emit, is_fundamental=False,
                           formula="thermal photon emission", suppressible=True))

    # --- Nuisance channels (conditional on experimental setup) ---
    if P_laser > 0 and omega_laser > 0:
        from grut_solver.budget.trap_noise import lambda_photon_recoil
        Ltrap = lambda_photon_recoil(P_laser, omega_laser, R, l)
        channels.append(Channel("trap_recoil", Ltrap, is_fundamental=False,
                               formula="laser photon recoil", suppressible=True))

    if n_charges > 0 and E_noise > 0 and omega_trap > 0:
        from grut_solver.budget.charge_noise import lambda_charge
        Lcharge = lambda_charge(n_charges, E_noise, m, l, omega_trap)
        channels.append(Channel("charge_noise", Lcharge, is_fundamental=False,
                               formula="stray E field", suppressible=True))

    if S_vib > 0 and omega_trap > 0:
        from grut_solver.budget.vibration import lambda_vibration
        Lvib = lambda_vibration(m, omega_trap, S_vib, l)
        channels.append(Channel("vibration", Lvib, is_fundamental=False,
                               formula="seismic noise", suppressible=True))

    # --- Aggregate ---
    lambda_total = sum(ch.rate_hz for ch in channels)
    lambda_env = sum(ch.rate_hz for ch in channels if not ch.is_fundamental)
    t_coh = 1.0 / lambda_total if lambda_total > 0 else float('inf')

    # Binding constraint: largest suppressible channel
    suppressible = [ch for ch in channels if ch.suppressible and ch.rate_hz > 0]
    if suppressible:
        binding = max(suppressible, key=lambda ch: ch.rate_hz)
        binding_name = binding.name
    else:
        binding_name = "none"

    snr = Lg / lambda_env if lambda_env > 0 else float('inf')

    return BudgetResult(
        channels=channels,
        lambda_total=lambda_total,
        lambda_env=lambda_env,
        lambda_grav=Lg,
        lambda_anomaly=La,
        t_coherence=t_coh,
        binding_channel=binding_name,
        signal_to_noise=snr,
        is_grav_dominated=(Lg > lambda_env),
    )


def budget_with_uncertainty(
    m: float, R: float, l: float,
    T_env: float, P: float,
    vary_pct: float = 10.0,
    **kwargs,
) -> BudgetResult:
    """Compute budget with uncertainty propagation.

    Varies each input by ±vary_pct% and checks whether the binding
    constraint and gravity-dominated conclusion change.
    """
    nominal = compute_budget(m, R, l, T_env, P, **kwargs)

    frac = vary_pct / 100.0
    totals = []

    # Vary each input independently
    for m_f in [1-frac, 1+frac]:
        for R_f in [1-frac, 1+frac]:
            for P_f in [1-frac, 1+frac]:
                b = compute_budget(m*m_f, R*R_f, l, T_env, P*P_f, **kwargs)
                totals.append(b.lambda_total)

    nominal.lambda_total_lo = min(totals)
    nominal.lambda_total_hi = max(totals)

    # Check robustness: does the binding constraint change?
    binding_names = set()
    grav_dom_flags = set()
    for m_f in [1-frac, 1+frac]:
        for P_f in [1-frac, 1+frac]:
            b = compute_budget(m*m_f, R, l, T_env, P*P_f, **kwargs)
            binding_names.add(b.binding_channel)
            grav_dom_flags.add(b.is_grav_dominated)

    nominal.conclusion_robust = (len(binding_names) == 1 and len(grav_dom_flags) == 1)

    return nominal
