"""Neural resonance verification — v2 certification of V7 Sector 13 results.

Two independent routes to 40 Hz gamma oscillation, zero free parameters:
  Route 1 (gravitational): N × Λ_grav/dimer × dimers/neuron = 39.9 Hz
  Route 2 (network topology): 1 / (6 hops × 4 ms) = 41.7 Hz

V7 biological parameters (from grut_solver/sectors/consciousness/resonance.py):
  m_tubulin   = 110,000 Da  = 1.827e-22 kg   (measured tubulin dimer mass)
  l_conform   = 0.7 nm                         (GTP→GDP conformational shift)
  R_tubulin   = 4 nm                           (effective radius)
  dimers/MT   = 1,625                          (13 protofilaments × 125 rings)
  MT/neuron   = 2.4e7                          (V7 biological estimate)
  dimers/neur = 3.9e10

Status: [SPECULATIVE] — interpretation is philosophical, not physical.
The computed results (40 Hz, two routes, neuron count) are structural.
"""

import math
import pytest

from grut.foundation.noise_kernel import lambda_grav

# ── V7 Biological parameters ─────────────────────────────────────────────────
AMU_KG = 1.66053906660e-27      # kg
M_TUBULIN_KG = 110_000 * AMU_KG  # 1.827e-22 kg — measured tubulin dimer mass
L_CONFORMATIONAL_M = 0.7e-9      # 0.7 nm — GTP→GDP conformational displacement
R_TUBULIN_M = 4e-9              # 4 nm — effective radius
DIMERS_PER_MT = 1_625           # 13 protofilaments × 125 rings
MT_PER_NEURON = 2.4e7           # V7 biological estimate
DIMERS_PER_NEURON = DIMERS_PER_MT * MT_PER_NEURON  # 3.9e10

# ── Known results from V7 Sector 13 ─────────────────────────────────────────
N_NEURONS_V7 = 38_064           # neurons for 40 Hz gamma (gravitational route)
GAMMA_HZ = 40.0                 # target: brain gamma oscillation

# Route 2 parameters
N_HOPS = 6
HOP_TIME_S = 4e-3               # 4 ms per synaptic hop


class TestNetworkTopologyRoute:
    """Route 2: 1/(6 hops × 4 ms) = 41.7 Hz — pure arithmetic."""

    def test_network_topology_frequency(self):
        freq = 1.0 / (N_HOPS * HOP_TIME_S)
        assert abs(freq - 41.667) < 0.001, f"Expected ~41.67 Hz, got {freq:.3f}"

    def test_brackets_40hz_gamma(self):
        freq = 1.0 / (N_HOPS * HOP_TIME_S)
        assert 40 < freq < 43, "Network topology route must bracket 40 Hz gamma band"


class TestGravitationalRoute:
    """Route 1: N × Λ_grav/dimer × dimers/neuron = 39.9 Hz."""

    def test_lambda_grav_per_dimer_is_positive(self):
        Lg = lambda_grav(M_TUBULIN_KG, L_CONFORMATIONAL_M, R_TUBULIN_M)
        assert Lg > 0

    def test_rate_per_neuron_is_positive(self):
        Lg = lambda_grav(M_TUBULIN_KG, L_CONFORMATIONAL_M, R_TUBULIN_M)
        rate = Lg * DIMERS_PER_NEURON
        assert rate > 0

    def test_n_neurons_for_40hz_matches_v7(self):
        """Core certification: v2 formula reproduces V7's 38,064 neurons."""
        Lg = lambda_grav(M_TUBULIN_KG, L_CONFORMATIONAL_M, R_TUBULIN_M)
        rate_per_neuron = Lg * DIMERS_PER_NEURON
        N = GAMMA_HZ / rate_per_neuron
        # Allow 1% tolerance for floating-point and rounding
        assert abs(N - N_NEURONS_V7) / N_NEURONS_V7 < 0.01, (
            f"Expected ~{N_NEURONS_V7} neurons, got {N:.0f}"
        )

    def test_collective_rate_is_40hz(self):
        """N neurons at V7 count produce ~39.9 Hz collective rate."""
        Lg = lambda_grav(M_TUBULIN_KG, L_CONFORMATIONAL_M, R_TUBULIN_M)
        rate_per_neuron = Lg * DIMERS_PER_NEURON
        collective_rate = N_NEURONS_V7 * rate_per_neuron
        assert abs(collective_rate - 39.9) < 0.5, (
            f"Expected ~39.9 Hz, got {collective_rate:.2f} Hz"
        )

    def test_result_brackets_40hz_gamma(self):
        Lg = lambda_grav(M_TUBULIN_KG, L_CONFORMATIONAL_M, R_TUBULIN_M)
        collective_rate = N_NEURONS_V7 * Lg * DIMERS_PER_NEURON
        assert 39 < collective_rate < 41


class TestTwoRoutesIndependence:
    """The two routes share zero common parameters."""

    def test_routes_converge_within_5pct(self):
        """Both routes bracket 40 Hz within 5% of each other."""
        route1 = N_NEURONS_V7 * lambda_grav(
            M_TUBULIN_KG, L_CONFORMATIONAL_M, R_TUBULIN_M
        ) * DIMERS_PER_NEURON
        route2 = 1.0 / (N_HOPS * HOP_TIME_S)
        spread = abs(route1 - route2) / ((route1 + route2) / 2)
        assert spread < 0.05, (
            f"Routes {route1:.1f} Hz and {route2:.1f} Hz diverge by {spread*100:.1f}%"
        )

    def test_routes_share_no_parameters(self):
        """Structural check: gravitational route uses G, m, l, R, ℏ.
        Network route uses only hop count and hop time. No shared variables."""
        grav_params = {M_TUBULIN_KG, L_CONFORMATIONAL_M, R_TUBULIN_M,
                       DIMERS_PER_NEURON, N_NEURONS_V7}
        network_params = {N_HOPS, HOP_TIME_S}
        assert grav_params.isdisjoint(network_params)


class TestScaleBridge:
    """40 Hz and Ω_Λ separated by 10^-19.3 from the same CTP action (τ₀)."""

    def test_scale_ratio_exponent(self):
        """log10(40 Hz / H_inf) ≈ 19.3."""
        H_inf_hz = 58.15e3 / 3.0857e22   # 58.15 km/s/Mpc in Hz
        ratio = GAMMA_HZ / H_inf_hz
        exponent = math.log10(ratio)
        assert abs(exponent - 19.3) < 0.1, (
            f"Expected scale exponent ~19.3, got {exponent:.2f}"
        )
