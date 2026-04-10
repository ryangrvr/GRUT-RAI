"""
Sector 13 — Resonance Condition for the 38,000-Neuron Number

Application 9 found that ~33,000-38,000 neurons produce a collective
gravitational decoherence rate of 40 Hz (the gamma oscillation).
This module asks: is this just a linear scaling coincidence, or can
it be understood as a resonance condition?

STATUS: Computed (linear scaling from existing USL).
Network resonance interpretation is model-dependent.
"""

import numpy as np
from grut_solver.constants import G, HBAR, AMU
from grut_solver.usl.gravitational import lambda_grav

# Tubulin parameters (from Application 9)
M_TUBULIN_DA = 110000
M_TUBULIN_KG = M_TUBULIN_DA * AMU
L_CONFORMATIONAL = 0.7e-9    # nm
R_TUBULIN = 4e-9             # nm

# Microtubule parameters
DIMERS_PER_MT = 1625
MT_PER_NEURON = 2.4e7
DIMERS_PER_NEURON = DIMERS_PER_MT * MT_PER_NEURON

# Brain parameters
NEURONS_IN_BRAIN = 8.6e10

# Target frequency
GAMMA_HZ = 40.0


def linear_resonance_condition(target_freq: float = GAMMA_HZ) -> dict:
    """Linear scaling: N_neurons = freq / (Lambda_single * dimers_per_neuron).

    This recapitulates Application 9 with added sensitivity analysis.
    """
    Lg_single = lambda_grav(M_TUBULIN_KG, L_CONFORMATIONAL, R_TUBULIN)
    rate_per_neuron = Lg_single * DIMERS_PER_NEURON
    N_neurons = target_freq / rate_per_neuron

    # Sensitivity: dN/d(parameter) for key parameters
    # dN/df = 1 / rate_per_neuron
    dN_df = 1.0 / rate_per_neuron

    # dN/dm (mass sensitivity): Lambda ~ m^2, so N ~ 1/m^2
    # dN/dm = -2 * N / m
    dN_dm = -2 * N_neurons / M_TUBULIN_KG

    # dN/dl (separation sensitivity): Lambda ~ 1/l * S(l/R)
    # In near-field: Lambda ~ l^2, so N ~ 1/l^2, dN/dl = -2*N/l
    dN_dl = -2 * N_neurons / L_CONFORMATIONAL

    # Biological context
    brain_fraction = N_neurons / NEURONS_IN_BRAIN
    cortical_column_neurons = 80000  # typical cortical column

    return {
        "target_freq_hz": target_freq,
        "lambda_single_hz": Lg_single,
        "rate_per_neuron_hz": rate_per_neuron,
        "N_neurons": N_neurons,
        "brain_fraction": brain_fraction,
        "cortical_columns_equivalent": N_neurons / cortical_column_neurons,
        "sensitivity": {
            "dN_dfreq": dN_df,
            "dN_dmass_per_kg": dN_dm,
            "dN_dseparation_per_m": dN_dl,
            "pct_change_N_per_pct_mass": -2.0,  # N ~ m^{-2}
            "pct_change_N_per_pct_sep": -2.0,   # N ~ l^{-2} in near-field
        },
        "note": (
            f"N = {N_neurons:.0f} neurons for {target_freq} Hz. "
            f"This is {brain_fraction:.2e} of the brain, or "
            f"~{N_neurons/cortical_column_neurons:.1f} cortical columns. "
            f"Biologically: a localized network of realistic size."
        ),
    }


def network_resonance_condition(n_neurons: int = 38000,
                                connectivity: float = 0.01) -> dict:
    """Network correction to the linear scaling.

    In a network of N neurons with connectivity k (fraction of all-to-all),
    the effective rate depends on phase coherence between neurons:
      Lambda_eff = N * Lambda_1 * [1 + (N-1) * k * <cos(phi_ij)>]

    - Random phases: <cos> = 0, recover linear scaling
    - Phase-locked: <cos> = 1, super-linear: Lambda_eff ~ N^2 * k
    - Anti-correlated: <cos> = -1/(N-1), sub-linear

    Parameters
    ----------
    n_neurons : int        Number of neurons in network.
    connectivity : float   Fraction of all-to-all connections [0, 1].
    """
    Lg_single = lambda_grav(M_TUBULIN_KG, L_CONFORMATIONAL, R_TUBULIN)
    rate_per_neuron = Lg_single * DIMERS_PER_NEURON

    # Three regimes
    rate_random = n_neurons * rate_per_neuron  # <cos> = 0
    rate_locked = n_neurons * rate_per_neuron * (1 + (n_neurons - 1) * connectivity)
    rate_anti = n_neurons * rate_per_neuron * (1 - connectivity)

    # For phase-locked case: what N gives 40 Hz?
    # N * rate_1 * (1 + (N-1)*k) = 40
    # Approximate: N^2 * k * rate_1 = 40 for large N
    N_locked = np.sqrt(GAMMA_HZ / (connectivity * rate_per_neuron))

    # Cortical connectivity in literature: ~0.01-0.1 locally
    k_for_resonance = GAMMA_HZ / (n_neurons**2 * rate_per_neuron)

    return {
        "n_neurons": n_neurons,
        "connectivity": connectivity,
        "rate_per_neuron_hz": rate_per_neuron,
        "rate_random_hz": rate_random,
        "rate_locked_hz": rate_locked,
        "rate_anti_hz": rate_anti,
        "N_for_40hz_locked": N_locked,
        "k_for_resonance": k_for_resonance,
        "note": (
            f"Random phases: {rate_random:.1f} Hz (linear, matches App 9). "
            f"Phase-locked (k={connectivity}): {rate_locked:.1f} Hz. "
            f"For phase-locked 40 Hz: need {N_locked:.0f} neurons "
            f"(vs {n_neurons} for random). "
            f"Connectivity for resonance at N={n_neurons}: k={k_for_resonance:.2e}."
        ),
    }


def gravitational_biological_matching(
    mass_range_kg: tuple = (1e-25, 1e-20),
    freq_range_hz: tuple = (1, 100),
    n_mass_points: int = 50,
    n_freq_points: int = 20
) -> dict:
    """Map the full resonance surface: (mass, frequency, N_neurons).

    Scans over tubulin-like masses and biologically relevant frequencies
    to find ALL combinations that produce resonance.

    Returns the resonance surface and identifies special points.
    """
    masses = np.logspace(np.log10(mass_range_kg[0]),
                         np.log10(mass_range_kg[1]), n_mass_points)
    freqs = np.logspace(np.log10(freq_range_hz[0]),
                        np.log10(freq_range_hz[1]), n_freq_points)

    surface = []
    for m in masses:
        R = (3 * m / (4 * np.pi * 1400)) ** (1.0 / 3.0)  # protein density
        Lg = lambda_grav(m, L_CONFORMATIONAL, R)
        # Assume similar dimers_per_neuron scaling
        rate_per_neuron = Lg * DIMERS_PER_NEURON

        for f in freqs:
            if rate_per_neuron > 0:
                N = f / rate_per_neuron
            else:
                N = float('inf')

            surface.append({
                "m_kg": float(m),
                "m_amu": float(m / AMU),
                "freq_hz": float(f),
                "N_neurons": float(N),
                "feasible": 100 < N < NEURONS_IN_BRAIN,
            })

    # Find the biologically interesting region
    feasible = [s for s in surface if s["feasible"]]

    # Special points
    special = {
        "gamma_40hz_tubulin": linear_resonance_condition(40.0),
        "alpha_10hz_tubulin": linear_resonance_condition(10.0),
        "theta_6hz_tubulin": linear_resonance_condition(6.0),
        "beta_20hz_tubulin": linear_resonance_condition(20.0),
    }

    return {
        "surface": surface,
        "n_feasible_points": len(feasible),
        "mass_range_amu": (mass_range_kg[0] / AMU, mass_range_kg[1] / AMU),
        "freq_range_hz": freq_range_hz,
        "special_points": {k: {
            "N_neurons": v["N_neurons"],
            "freq": v["target_freq_hz"],
        } for k, v in special.items()},
        "note": (
            f"Resonance surface: {len(feasible)} points have "
            f"biologically feasible neuron counts (100 - {NEURONS_IN_BRAIN:.0e}). "
            f"At tubulin mass: gamma (40 Hz) needs ~{special['gamma_40hz_tubulin']['N_neurons']:.0f} neurons, "
            f"alpha (10 Hz) needs ~{special['alpha_10hz_tubulin']['N_neurons']:.0f} neurons."
        ),
    }
