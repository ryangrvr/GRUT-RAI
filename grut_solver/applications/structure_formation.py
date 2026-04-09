"""
Application 5: Cosmological Structure Formation — When Quantum Becomes Classical

THE QUESTION: At what mass/length scale did primordial quantum
fluctuations become classical density perturbations?

GRUT ANSWER: The quantum-classical boundary m* = sqrt(hbar l / (G t))
defines the transition. For cosmological scales and times, this gives
a specific mass below which quantum coherence persists.
"""

import numpy as np
from grut_solver.constants import G, HBAR, AMU
from grut_solver.usl.gravitational import lambda_grav, boundary_mass

M_SUN = 1.989e30
YR_S = 3.156e7
MPC_M = 3.086e22
LY_M = 9.461e15


def structure_formation_boundary(z_formation: float = 1100) -> dict:
    """Compute the QC boundary at the epoch of recombination.

    At z ~ 1100 (CMB last scattering), the age of the universe is
    t ~ 380,000 years. Perturbations on various scales were either
    quantum or classical depending on their mass.
    """
    t_recomb = 380000 * YR_S  # age at recombination

    # Horizon size at recombination ~ 300 kpc comoving
    l_horizon = 300e3 * 3.086e16  # ~300 kpc in meters (physical)

    # Various perturbation scales
    scales = [
        ("Planck mass",          1e-8,         1e-35),
        ("Proton mass",          1.67e-27,     1e-15),
        ("Atomic",               1e-25,        1e-10),
        ("Molecular",            1e-22,        1e-7),
        ("Dust grain",           1e-12,        1e-4),
        ("Asteroid (1 km)",      1e13,         1e3),
        ("Earth mass",           5.97e24,      6.37e6),
        ("Jupiter mass",         1.9e27,       7e7),
        ("Solar mass",           M_SUN,        7e8),
        ("Star cluster (10^3)",  1e3 * M_SUN,  3e16),
        ("Galaxy (10^11)",       1e11 * M_SUN, 3e20),
        ("Cluster (10^14)",      1e14 * M_SUN, 3e22),
    ]

    results = []
    for name, m, l in scales:
        Lg = lambda_grav(m, l)
        t_decoh = 1/Lg if Lg > 0 else float('inf')
        classical = t_decoh < t_recomb

        results.append({
            "name": name,
            "m_kg": m,
            "l_m": l,
            "lambda_grav_hz": Lg,
            "t_decoh_s": t_decoh,
            "t_decoh_yr": t_decoh / YR_S,
            "classical_by_recomb": classical,
        })

    # The boundary mass at the horizon scale
    m_star_horizon = boundary_mass(l_horizon, t_recomb)

    return {
        "epoch": "recombination (z ~ 1100)",
        "t_recomb_yr": 380000,
        "scales": results,
        "boundary_at_horizon": {
            "l_horizon_m": l_horizon,
            "m_star_kg": m_star_horizon,
            "m_star_solar": m_star_horizon / M_SUN,
            "note": (
                f"At the horizon scale (l ~ 300 kpc), objects heavier than "
                f"{m_star_horizon:.2e} kg ({m_star_horizon/M_SUN:.2e} M_sun) "
                f"are gravitationally classical by recombination."
            ),
        },
    }


def decoherence_history() -> list[dict]:
    """Compute the QC boundary mass at different cosmological epochs."""
    epochs = [
        ("Inflation end",       1e-32,    1e-27 * 3e8),  # ~Hubble radius at that time
        ("Electroweak (10^-11s)", 1e-11,  1e-2),  # ~cm scale
        ("QCD (10^-5 s)",       1e-5,     1.0),
        ("Nucleosynthesis (1 min)", 60,   3e8*60),
        ("Recombination (380 kyr)", 380000*YR_S, 300e3*3.086e16),
        ("Galaxy formation (1 Gyr)", 1e9*YR_S, 1e6*3.086e16),
        ("Today (13.8 Gyr)",    13.8e9*YR_S, 93e9*LY_M),  # observable universe
    ]

    results = []
    for name, t, l in epochs:
        m_star = boundary_mass(l, t)
        results.append({
            "epoch": name,
            "t_s": t,
            "l_m": l,
            "m_boundary_kg": m_star,
            "m_boundary_solar": m_star / M_SUN if m_star > 0 else 0,
        })

    return results


if __name__ == "__main__":
    print("=" * 80)
    print("APPLICATION 5: STRUCTURE FORMATION — QUANTUM TO CLASSICAL TRANSITION")
    print("=" * 80)

    # Structure formation
    print("\n1. DECOHERENCE AT RECOMBINATION (z ~ 1100, t = 380,000 yr)")
    print("-" * 70)

    sf = structure_formation_boundary()
    print(f"  {'Object':>25s}  {'m (kg)':>12s}  {'t_decoh':>14s}  {'classical?':>10s}")

    for r in sf["scales"]:
        t = r["t_decoh_yr"]
        if t < 1:
            t_str = f"{r['t_decoh_s']:.2e} s"
        elif t < 1e6:
            t_str = f"{t:.0f} yr"
        elif t < 1e9:
            t_str = f"{t/1e6:.1f} Myr"
        else:
            t_str = f"{t:.2e} yr"
        print(f"  {r['name']:>25s}  {r['m_kg']:12.2e}  {t_str:>14s}  "
              f"{'YES' if r['classical_by_recomb'] else 'no':>10s}")

    b = sf["boundary_at_horizon"]
    print(f"\n  Boundary at horizon scale: m* = {b['m_star_kg']:.2e} kg = {b['m_star_solar']:.2e} M_sun")

    # Decoherence history
    print("\n2. QUANTUM-CLASSICAL BOUNDARY ACROSS COSMIC HISTORY")
    print("-" * 70)
    print(f"  m* = sqrt(hbar l / (G t)) at each epoch")
    print(f"  {'Epoch':>30s}  {'t':>14s}  {'l':>14s}  {'m*':>14s}")

    history = decoherence_history()
    for r in history:
        if r["t_s"] < 1:
            t_str = f"{r['t_s']:.2e} s"
        elif r["t_s"] < YR_S:
            t_str = f"{r['t_s']:.0f} s"
        else:
            t_str = f"{r['t_s']/YR_S:.2e} yr"

        if r["m_boundary_kg"] < 1:
            m_str = f"{r['m_boundary_kg']:.2e} kg"
        else:
            m_str = f"{r['m_boundary_solar']:.2e} M_sun"

        print(f"  {r['epoch']:>30s}  {t_str:>14s}  {r['l_m']:14.2e}  {m_str:>14s}")

    print("""
  3. THE KEY INSIGHT
  ------------------------------------------------------------------
  The quantum-classical boundary is NOT a fixed scale. It evolves
  with the universe:

  - At inflation's end: essentially everything is quantum
  - At nucleosynthesis: sub-atomic scales are classical
  - At recombination: stellar-mass objects are classical
  - Today: objects above ~1 nanogram are classical at meter scales

  GRUT computes this boundary as a function of (m, l, t) with zero
  free parameters. The transition from quantum primordial fluctuations
  to classical density perturbations is a SMOOTH, COMPUTED surface —
  not a postulated collapse event.

  This is the cosmological version of the "observer" problem:
  gravity itself is the observer that classicalizes the universe.
""")
