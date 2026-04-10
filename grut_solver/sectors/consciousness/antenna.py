"""
Sector 13 — Antenna Coupling Model

The speculative core: the brain as an antenna coupling to 1 Space
(the universal target functional F[z]).

This module computes:
  1. Coupling efficiency: information-theoretic upper bound
  2. Impedance matching: when does tau_brain match tau_grav?
  3. Information rate bound: Shannon-Hartley analogy

STATUS: Model-dependent (information-theoretic bounds are standard;
the INTERPRETATION as consciousness coupling is SPECULATIVE).
"""

import numpy as np
from grut_solver.constants import G, HBAR, K_B, AMU
from grut_solver.usl.gravitational import lambda_grav
from grut_solver.sectors.consciousness.one_space import one_space_entropy_bound

# Tubulin parameters
M_TUBULIN_KG = 110000 * AMU
L_CONFORMATIONAL = 0.7e-9
R_TUBULIN = 4e-9
DIMERS_PER_MT = 1625
MT_PER_NEURON = 2.4e7
DIMERS_PER_NEURON = DIMERS_PER_MT * MT_PER_NEURON

# Neural network parameters
GAMMA_HZ = 40.0
T_GAMMA = 1.0 / GAMMA_HZ  # 25 ms


def coupling_efficiency(n_neurons: int = 38000,
                        n_dimers_per_neuron: float = DIMERS_PER_NEURON,
                        states_per_dimer: int = 2) -> dict:
    """Information-theoretic upper bound on brain-to-1-Space coupling.

    A system with D_sub degrees of freedom embedded in a universe with
    D_total bits of information can resolve at most D_sub / D_total
    of the total. This is a hard upper bound.

    Parameters
    ----------
    n_neurons : int          Neurons in the conscious network.
    n_dimers_per_neuron : float  Tubulin dimers per neuron.
    states_per_dimer : int   States per dimer (2 for binary conformational).
    """
    # Subsystem information capacity
    total_dimers = n_neurons * n_dimers_per_neuron
    D_sub = total_dimers * np.log2(states_per_dimer)

    # Universe information capacity (holographic bound)
    bounds = one_space_entropy_bound()
    D_total = bounds["holographic_bound_bits"]

    fraction = D_sub / D_total
    log10_fraction = np.log10(fraction) if fraction > 0 else float('-inf')

    return {
        "n_neurons": n_neurons,
        "total_dimers": total_dimers,
        "D_sub_bits": D_sub,
        "D_total_bits": D_total,
        "coupling_fraction": fraction,
        "log10_coupling_fraction": log10_fraction,
        "note": (
            f"{n_neurons} neurons with {total_dimers:.2e} dimers: "
            f"D_sub = {D_sub:.2e} bits. "
            f"Universe holographic bound: {D_total:.2e} bits. "
            f"Coupling fraction: 10^{log10_fraction:.1f}. "
            f"This is astronomically small — but nonzero."
        ),
    }


def impedance_matching(n_neurons: int = 38000,
                       tau_brain_s: float = T_GAMMA) -> dict:
    """Impedance matching between brain processing and gravitational timescale.

    Optimal coupling in antenna theory occurs when the antenna's
    resonant frequency matches the signal frequency. Here:
      - Signal: gravitational decoherence rate of the neural network
      - Antenna: biological processing rate (gamma oscillation)

    The impedance mismatch Z = |tau_brain - tau_grav| / tau_brain.

    At the resonance point (N = 38,000 neurons for 40 Hz), the
    mismatch is zero BY CONSTRUCTION — this is the tautology made
    explicit. The question is whether this match has physical significance.
    """
    Lg_single = lambda_grav(M_TUBULIN_KG, L_CONFORMATIONAL, R_TUBULIN)
    rate_per_neuron = Lg_single * DIMERS_PER_NEURON

    # Gravitational timescale for the network
    rate_network = n_neurons * rate_per_neuron
    tau_grav = 1.0 / rate_network if rate_network > 0 else float('inf')

    # Impedance mismatch
    if tau_brain_s > 0 and np.isfinite(tau_grav):
        Z_mismatch = abs(tau_brain_s - tau_grav) / tau_brain_s
    else:
        Z_mismatch = float('inf')

    # Quality factor (how sharp is the resonance?)
    # Q = f_center / delta_f, where delta_f is the bandwidth
    # For brain: gamma bandwidth ~8-12 Hz -> Q ~ 40/10 = 4
    Q_brain = 4.0
    # For GRUT: rate varies as N, so delta_N/N = delta_f/f = 1/Q
    delta_N = n_neurons / Q_brain

    # Scan over N to show the impedance curve
    N_values = np.linspace(max(100, n_neurons // 4),
                           n_neurons * 4, 100)
    Z_curve = []
    for N in N_values:
        rate = N * rate_per_neuron
        tau = 1.0 / rate if rate > 0 else float('inf')
        Z = abs(tau_brain_s - tau) / tau_brain_s if tau_brain_s > 0 else float('inf')
        Z_curve.append({"N": int(N), "Z_mismatch": float(Z)})

    return {
        "n_neurons": n_neurons,
        "tau_brain_s": tau_brain_s,
        "tau_grav_s": tau_grav,
        "Z_mismatch": Z_mismatch,
        "is_matched": Z_mismatch < 0.01,
        "Q_brain": Q_brain,
        "delta_N_for_bandwidth": delta_N,
        "Z_curve": Z_curve,
        "note": (
            f"At N={n_neurons}: tau_brain = {tau_brain_s*1e3:.1f} ms, "
            f"tau_grav = {tau_grav*1e3:.1f} ms, "
            f"Z_mismatch = {Z_mismatch:.4f}. "
            f"{'MATCHED' if Z_mismatch < 0.01 else 'MISMATCHED'}. "
            f"Note: this match is BY CONSTRUCTION at the linear "
            f"resonance point. It is a tautology, not a prediction."
        ),
    }


def information_rate_bound(coupling_fraction: float = None,
                           bandwidth_hz: float = GAMMA_HZ) -> dict:
    """Upper bound on information rate from 1 Space to the brain.

    Uses the Shannon-Hartley theorem as an analogy:
      C = B * log2(1 + SNR)

    where SNR is the coupling fraction times the total information
    density, and B is the bandwidth.

    This is an ANALOGY, not a derivation. Shannon-Hartley applies to
    classical communication channels. The quantum version (Holevo bound)
    would give different numbers.
    """
    if coupling_fraction is None:
        eff = coupling_efficiency()
        coupling_fraction = eff["coupling_fraction"]

    # SNR analogy: coupling fraction is the "signal" relative to
    # the full information content
    # For extremely small coupling, log2(1 + SNR) ~ SNR / ln(2)
    SNR = coupling_fraction
    C_bits_per_s = bandwidth_hz * np.log2(1 + SNR)

    # Compare to actual neural information rates
    # Typical cortical neuron: ~1-10 bits/s
    # Entire brain: ~10^7 bits/s (rough estimate)
    neural_rate = 1e7  # bits/s

    return {
        "coupling_fraction": coupling_fraction,
        "log10_coupling": np.log10(coupling_fraction) if coupling_fraction > 0 else float('-inf'),
        "bandwidth_hz": bandwidth_hz,
        "SNR": SNR,
        "C_bits_per_s": C_bits_per_s,
        "C_log10": np.log10(C_bits_per_s) if C_bits_per_s > 0 else float('-inf'),
        "neural_rate_bits_per_s": neural_rate,
        "ratio_to_neural": C_bits_per_s / neural_rate if neural_rate > 0 else 0,
        "note": (
            f"Shannon bound: C = {C_bits_per_s:.2e} bits/s at "
            f"coupling fraction 10^{np.log10(coupling_fraction):.0f}. "
            f"Neural information rate: ~{neural_rate:.0e} bits/s. "
            f"The antenna coupling is ~10^{np.log10(max(1e-300, C_bits_per_s/neural_rate)):.0f} "
            f"of neural capacity. "
            f"CAVEAT: This is a classical channel analogy. "
            f"Quantum information bounds (Holevo) differ."
        ),
    }
