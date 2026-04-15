"""
Entanglement Protection Test — F5

GRUT and Diosi-Penrose predict that entangled states decohere SLOWER
than separable states of the same total mass. CSL predicts the SAME rate
regardless of quantum state (state-independent collapse).

This is a yes/no discriminator between state-dependent (GRUT, DP) and
state-independent (CSL) decoherence models.

The physics: an entangled Bell pair |ψ⟩ = (|LR⟩ + |RL⟩)/√2 has a
different effective mass distribution than a separable state
|φ⟩ = |L⟩⊗|L⟩. The gravitational self-energy (and therefore Λ_grav)
differs because the noise kernel integrates over the JOINT mass distribution.
"""

import numpy as np
from grut.foundation.constants import G, HBAR, AMU


def lambda_grav_single(m_kg, l_m, rho=19300):
    """Decoherence rate for a single particle in superposition |L⟩ + |R⟩."""
    R = (3 * m_kg / (4 * np.pi * rho))**(1/3)
    ratio = l_m / R
    S = min(1.0, ratio**3 / 6.0)
    return G * m_kg**2 * S / (HBAR * l_m)


def lambda_grav_separable(m_kg, l_m, rho=19300):
    """Decoherence rate for a separable two-particle state |L⟩|L⟩ + |R⟩|R⟩.
    
    Both particles move together. Total mass = 2m.
    The self-energy involves the TOTAL mass distribution.
    """
    m_total = 2 * m_kg
    R = (3 * m_total / (4 * np.pi * rho))**(1/3)
    ratio = l_m / R
    S = min(1.0, ratio**3 / 6.0)
    return G * m_total**2 * S / (HBAR * l_m)


def lambda_grav_bell(m_kg, l_m, d_separation, rho=19300):
    """Decoherence rate for a Bell-entangled pair |LR⟩ + |RL⟩.
    
    The two particles are at DIFFERENT positions in each branch:
    Branch 1: particle A at L, particle B at R
    Branch 2: particle A at R, particle B at L
    
    The noise kernel integrates over the DIFFERENCE in mass distribution
    between branches. For the Bell state, particle A moves by l but
    particle B moves by -l (opposite direction). The effective mass
    distribution difference is partially cancelled by the anti-correlation.
    
    For well-separated particles (d >> l):
    Λ_Bell ≈ 2 × Λ_single (each particle contributes independently)
    
    For co-located particles (d << l):
    Λ_Bell ≈ Λ_single × (1 - overlap_correction)
    The overlap correction reduces the rate because the anti-correlated
    motion partially cancels the gravitational self-energy difference.
    """
    R = (3 * m_kg / (4 * np.pi * rho))**(1/3)
    ratio = l_m / R
    S = min(1.0, ratio**3 / 6.0)
    L_single = G * m_kg**2 * S / (HBAR * l_m)
    
    # For two particles separated by d:
    # The cross-term in the self-energy depends on d/l
    # When d >> l: independent → Λ_Bell = 2 × Λ_single
    # When d << l: anti-correlated → Λ_Bell < 2 × Λ_single
    # When d = 0 (co-located): maximum protection
    
    # Cross-term: the gravitational interaction between the two mass
    # distributions reduces the effective self-energy for the Bell state
    if d_separation > 0:
        cross_factor = 1.0 - np.exp(-d_separation / l_m)
    else:
        cross_factor = 0.0  # maximum protection when co-located
    
    # Bell state: each particle contributes Λ_single, but cross-term reduces total
    L_bell = 2 * L_single * (1 - 0.5 * (1 - cross_factor))
    
    return L_bell


def lambda_csl(m_kg, l_m):
    """CSL decoherence rate — state-independent.
    
    Λ_CSL = λ × (m/m_0)^2 × (1 - sinc(ql/ℏ))
    
    CSL does NOT depend on whether the state is separable or entangled.
    It depends only on the total mass.
    """
    lambda_csl_param = 1e-16  # s^-1
    r_c = 1e-7                # m
    N = m_kg / AMU
    sinc_arg = l_m / r_c
    sinc_val = np.sin(sinc_arg) / sinc_arg if sinc_arg > 1e-10 else 1.0
    return lambda_csl_param * N**2 * (1 - sinc_val)


def entanglement_experiment(m_amu=1e6, l_m=1e-7, d_m=1e-7, rho=19300):
    """Full entanglement protection experiment.
    
    Compare three configurations at the same total mass:
    1. Single particle (mass 2m) in superposition
    2. Separable pair (mass m each, correlated)
    3. Bell pair (mass m each, anti-correlated)
    """
    m_single = m_amu * AMU
    m_per_particle = m_single / 2  # each particle in the pair
    
    # GRUT predictions
    L_single = lambda_grav_single(m_single, l_m, rho)
    L_separable = lambda_grav_separable(m_per_particle, l_m, rho)
    L_bell = lambda_grav_bell(m_per_particle, l_m, d_m, rho)
    
    # CSL predictions (state-independent)
    L_csl_single = lambda_csl(m_single, l_m)
    L_csl_separable = lambda_csl(m_single, l_m)  # same! mass-only
    L_csl_bell = lambda_csl(m_single, l_m)       # same! state-independent
    
    # The discriminator ratios
    grut_protection = L_bell / L_separable if L_separable > 0 else 1
    csl_protection = L_csl_bell / L_csl_separable if L_csl_separable > 0 else 1
    
    return {
        "parameters": {
            "total_mass_amu": m_amu, "mass_per_particle_amu": m_amu / 2,
            "separation_m": l_m, "particle_distance_m": d_m,
            "material_rho": rho,
        },
        "grut_predictions": {
            "Lambda_single_Hz": L_single,
            "Lambda_separable_Hz": L_separable,
            "Lambda_bell_Hz": L_bell,
            "bell_to_separable_ratio": grut_protection,
            "protection_pct": (1 - grut_protection) * 100,
            "state_dependent": True,
        },
        "csl_predictions": {
            "Lambda_single_Hz": L_csl_single,
            "Lambda_separable_Hz": L_csl_separable,
            "Lambda_bell_Hz": L_csl_bell,
            "bell_to_separable_ratio": csl_protection,
            "protection_pct": 0.0,
            "state_dependent": False,
        },
        "discrimination": {
            "grut_ratio": grut_protection,
            "csl_ratio": csl_protection,
            "ratio_difference": abs(grut_protection - csl_protection),
            "distinguishable": abs(grut_protection - csl_protection) > 0.01,
            "test": "Measure Λ(Bell) / Λ(separable). GRUT < 1, CSL = 1.",
            "confirmation": f"Ratio < {grut_protection:.3f} (Bell slower than separable)",
            "falsification": "Ratio = 1.000 within error (state-independent → CSL wins)",
        },
        "dp_comparison": {
            "note": "Diosi-Penrose (point mass) also predicts state-dependent decoherence",
            "dp_agrees_with_grut": True,
            "to_distinguish_grut_from_dp": "Use F6 (kink test) — DP has no extended-body kink",
        },
    }


def protection_vs_distance(m_amu=1e6, l_m=1e-7, rho=19300, n=100):
    """Scan the Bell protection factor as a function of particle separation d.
    
    At d = 0: maximum protection (anti-correlated motion fully cancels)
    At d >> l: no protection (particles independent)
    """
    m_per = m_amu * AMU / 2
    d_vals = np.logspace(-10, -4, n)
    
    data = []
    for d in d_vals:
        L_sep = lambda_grav_separable(m_per, l_m, rho)
        L_bell = lambda_grav_bell(m_per, l_m, d, rho)
        ratio = L_bell / L_sep if L_sep > 0 else 1
        data.append({"d_m": float(d), "log_d": float(np.log10(d)),
                      "ratio": float(ratio), "protection_pct": float((1-ratio)*100)})
    
    return {
        "mass_amu": m_amu, "separation_m": l_m,
        "data": data,
        "max_protection_pct": max(p["protection_pct"] for p in data),
        "note": "Protection decreases as particles move apart (d → large)",
    }


def full_entanglement_analysis(m_amu=1e6):
    """Complete F5 analysis."""
    l_m = 1e-7  # 100 nm
    d_m = 1e-7  # particle distance = separation
    
    experiment = entanglement_experiment(m_amu, l_m, d_m)
    distance_scan = protection_vs_distance(m_amu, l_m)
    
    return {
        "experiment": experiment,
        "distance_scan": distance_scan,
        "combined_verdict": (
            f"At {m_amu:.0e} amu, l=100nm: GRUT predicts Bell/separable ratio = "
            f"{experiment['grut_predictions']['bell_to_separable_ratio']:.3f} "
            f"({experiment['grut_predictions']['protection_pct']:.1f}% protection). "
            f"CSL predicts ratio = 1.000 (0% protection). "
            f"This is a {'YES/NO' if experiment['discrimination']['distinguishable'] else 'marginal'} "
            f"discriminator between state-dependent (GRUT) and state-independent (CSL) decoherence."
        ),
    }
