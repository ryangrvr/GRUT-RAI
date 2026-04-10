"""
Sector 13 — Consciousness and 1 Space: Test Suite

14 tests covering all computed quantities.
Speculative claims are NOT tested (they are conceptual, not computational).
"""

import pytest
import numpy as np
import sys
sys.path.insert(0, ".")


# ── 1. One Space ─────────────────────────────────────────────

def test_target_functional_dimension():
    """F[z] dimensionality is positive and scales with fields x modes."""
    from grut_solver.sectors.consciousness.one_space import target_functional_dimension
    r = target_functional_dimension(n_fields=37, n_spatial_modes=1000)
    assert r["d_real"] == 2 * 37 * 1000
    assert r["d_real"] > 0
    print(f"  PASS: target_functional_dimension (D = {r['d_real']})")


def test_bekenstein_bound():
    """Bekenstein bound is approximately 10^120-10^125 bits."""
    from grut_solver.sectors.consciousness.one_space import one_space_entropy_bound
    r = one_space_entropy_bound()
    log_bits = r["bekenstein_bound_log10_bits"]
    assert 115 < log_bits < 135, f"Bekenstein bound log10 = {log_bits}"
    print(f"  PASS: bekenstein_bound (log10 = {log_bits:.1f})")


def test_holographic_bound():
    """Holographic bound is approximately 10^122 bits."""
    from grut_solver.sectors.consciousness.one_space import one_space_entropy_bound
    r = one_space_entropy_bound()
    log_bits = r["holographic_bound_log10_bits"]
    assert 120 < log_bits < 130, f"Holographic bound log10 = {log_bits}"
    assert r["binding_bound"] == "holographic"
    print(f"  PASS: holographic_bound (log10 = {log_bits:.1f})")


# ── 2. Boundary ──────────────────────────────────────────────

def test_thermal_below_gravitational():
    """Thermal boundary mass is below gravitational at T=310K."""
    from grut_solver.sectors.consciousness.boundary import boundary_mass_at_temperature
    r = boundary_mass_at_temperature(l=0.7e-9, t_obs=0.025, T=310.0)
    assert r["m_boundary_thermal_kg"] < r["m_boundary_grav_kg"]
    assert r["binding_mechanism"] == "thermal"
    ratio = r["log10_ratio"]
    assert ratio > 5, f"Ratio is only {ratio:.1f} orders"
    print(f"  PASS: thermal_below_gravitational (ratio = {ratio:.0f} orders)")


def test_boundary_width():
    """Transition zone width is computed and positive."""
    from grut_solver.sectors.consciousness.boundary import boundary_width_neural
    r = boundary_width_neural(T=310.0)
    assert r["width_decades"] >= 0
    assert r["m_upper_amu"] >= r["m_lower_amu"]
    print(f"  PASS: boundary_width ({r['width_decades']:.1f} decades, "
          f"range: {r['m_lower_amu']:.1e} — {r['m_upper_amu']:.1e} amu)")


# ── 3. Ordered Water ─────────────────────────────────────────

def test_ordered_water_improvement():
    """Confined water has longer decoherence time than bulk."""
    from grut_solver.sectors.consciousness.ordered_water import ordered_water_decoherence_time
    r = ordered_water_decoherence_time(confinement_factor=0.1)
    assert r["improvement_factor"] > 1.0
    assert r["t_confined_s"] > r["t_bulk_s"]
    print(f"  PASS: ordered_water_improvement (factor = {r['improvement_factor']:.1f}x)")


def test_gap_still_exists():
    """Even at extreme confinement, the thermal gap persists (> 15 orders)."""
    from grut_solver.sectors.consciousness.ordered_water import gap_analysis
    r = gap_analysis([0.001])
    gap = r["scan"][0]["remaining_gap_orders"]
    assert gap > 15, f"Gap too small: {gap} orders"
    print(f"  PASS: gap_still_exists (gap = {gap:.1f} orders at f=0.001)")


# ── 4. Pattern Survival ──────────────────────────────────────

def test_mutual_information_decay():
    """Mutual information starts positive and decays under dephasing."""
    from grut_solver.sectors.consciousness.pattern_survival import (
        mutual_information_under_decoherence
    )
    r = mutual_information_under_decoherence(n_sites=4, gamma_local=1e12,
                                             J_coupling=1e8,
                                             t_values=[1e-15, 1e-13, 1e-11])
    assert r["I_initial"] >= 0
    # Should decay: later times have less MI
    I_values = [x["I_AB"] for x in r["results"]]
    assert I_values[0] >= I_values[-1], "MI should decay over time"
    print(f"  PASS: mutual_information_decay (I_0 = {r['I_initial']:.3f})")


def test_entanglement_entropy():
    """GHZ entropy decays N times faster than single qubit."""
    from grut_solver.sectors.consciousness.pattern_survival import (
        entanglement_entropy_decay
    )
    r = entanglement_entropy_decay(n_qubits=8, decoherence_rate=1e15)
    assert r["S_initial_bits"] == 1.0
    assert r["t_half_s"] < 1.0 / (2 * 1e15), "Should be faster than single qubit"
    assert r["ratio_entropy_to_water"] < 1.0, "GHZ should decohere faster"
    print(f"  PASS: entanglement_entropy (t_half = {r['t_half_s']:.2e} s, "
          f"ratio = {r['ratio_entropy_to_water']:.3f})")


def test_topological_index():
    """Topological index computed and honest about uncorrelated noise."""
    from grut_solver.sectors.consciousness.pattern_survival import (
        topological_index_survival
    )
    r = topological_index_survival(lattice_size=13, gamma=1e15)
    assert r["t_survive_analytical_s"] > 0
    # Honest result: for uncorrelated noise on 13 sites, topology does NOT help
    # (winding number error grows as sqrt(N))
    assert r["ratio_to_local"] < 1.0, "Should be worse than local for uncorrelated noise"
    print(f"  PASS: topological_index (ratio = {r['ratio_to_local']:.2f}x, "
          f"topology_helps = {r['topology_helps']})")


# ── 5. Resonance ─────────────────────────────────────────────

def test_linear_resonance():
    """N_neurons for 40 Hz matches Application 9 (~33,000-45,000)."""
    from grut_solver.sectors.consciousness.resonance import linear_resonance_condition
    r = linear_resonance_condition(40.0)
    assert 25000 < r["N_neurons"] < 50000, f"N = {r['N_neurons']}"
    assert r["brain_fraction"] < 0.001  # < 0.1% of brain
    print(f"  PASS: linear_resonance (N = {r['N_neurons']:.0f})")


# ── 6. Antenna ───────────────────────────────────────────────

def test_coupling_efficiency_tiny():
    """Coupling fraction is astronomically small (< 10^-50)."""
    from grut_solver.sectors.consciousness.antenna import coupling_efficiency
    r = coupling_efficiency()
    assert r["log10_coupling_fraction"] < -50
    assert r["coupling_fraction"] > 0  # nonzero
    print(f"  PASS: coupling_efficiency (10^{r['log10_coupling_fraction']:.0f})")


def test_impedance_match_at_resonance():
    """At resonance N, impedance mismatch is near zero."""
    from grut_solver.sectors.consciousness.antenna import impedance_matching
    r = impedance_matching(n_neurons=38000)
    assert r["Z_mismatch"] < 0.1, f"Z = {r['Z_mismatch']}"
    print(f"  PASS: impedance_match (Z = {r['Z_mismatch']:.4f})")


# ── 7. Falsifiability ────────────────────────────────────────

def test_kill_conditions_nonempty():
    """Kill conditions list is non-empty with required fields."""
    from grut_solver.sectors.consciousness.falsifiability import kill_conditions
    kc = kill_conditions()
    assert len(kc) >= 5
    for k in kc:
        assert "id" in k
        assert "description" in k
        assert "measurement" in k
        assert "threshold" in k
        assert "status" in k
    print(f"  PASS: kill_conditions ({len(kc)} conditions)")


def test_adversarial_summary_honest():
    """Adversarial summary correctly categorizes computed vs speculative."""
    from grut_solver.sectors.consciousness.falsifiability import adversarial_summary
    s = adversarial_summary()
    assert s["n_computed"] > 0
    assert s["n_speculative"] > 0
    assert not s["verdict"]["gap_closed"], "Gap should NOT be closed"
    assert s["verdict"]["remaining_gap_orders"] > 10
    print(f"  PASS: adversarial_summary (gap = {s['verdict']['remaining_gap_orders']:.0f} orders, "
          f"{s['n_computed']} computed, {s['n_speculative']} speculative)")


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    passed = 0
    failed = 0
    for t in tests:
        try:
            t()
            passed += 1
        except Exception as e:
            print(f"  FAIL: {t.__name__}: {e}")
            failed += 1
    print(f"\n{'='*60}")
    print(f"Sector 13: {passed} passed, {failed} failed, {passed+failed} total")


# ── 8. Self-Reference ────────────────────────────────────────

def test_pure_self_reference_immune():
    """Pure self-reference (z_target=z) has zero distance at any noise."""
    from grut_solver.sectors.consciousness.self_reference import (
        compare_standard_vs_self_referential
    )
    r = compare_standard_vs_self_referential(
        noise_amplitudes=[1e2, 1e6], n_steps=5000
    )
    for row in r["results"]:
        if row["noise_amplitude"] > 0:
            assert row["self_ref_mean_distance"] < 1e-10, (
                f"Self-ref distance {row['self_ref_mean_distance']} at noise {row['noise_amplitude']}"
            )
            assert row["standard_mean_distance"] > 0.1
    print("  PASS: pure_self_reference_immune (distance = 0 at all noise levels)")


def test_nontrivial_self_reference_robust():
    """99% self-reference is significantly more robust than standard."""
    from grut_solver.sectors.consciousness.self_reference import (
        nontrivial_self_reference
    )
    r = nontrivial_self_reference(alpha=0.99, noise_amplitudes=[1e4], n_steps=10000)
    row = r["results"][0]
    assert row["ratio"] > 5, f"Ratio only {row['ratio']:.1f}x"
    print(f"  PASS: nontrivial_self_reference (ratio = {row['ratio']:.1f}x at alpha=0.99)")


def test_alpha_critical_threshold():
    """Critical alpha for 90% noise reduction exists and is < 1."""
    from grut_solver.sectors.consciousness.self_reference import alpha_sweep
    r = alpha_sweep(noise_amplitude=1e4, n_steps=10000)
    assert r["alpha_critical"] is not None
    assert 0 < r["alpha_critical"] < 1.0
    print(f"  PASS: alpha_critical = {r['alpha_critical']}")


def test_two_routes_to_40hz():
    """Gravitational and self-referential loop both produce ~40 Hz."""
    from grut_solver.sectors.consciousness.self_reference import refresh_rate_derivation
    r = refresh_rate_derivation()
    assert abs(r["f_grav_hz"] - 40) / 40 < 0.2, f"Grav: {r['f_grav_hz']}"
    assert abs(r["f_refresh_hz"] - 40) / 40 < 0.2, f"Loop: {r['f_refresh_hz']}"
    assert r["two_routes_one_frequency"]
    print(f"  PASS: two_routes_to_40hz (grav={r['f_grav_hz']:.1f}, loop={r['f_refresh_hz']:.1f})")


def test_minimum_complexity():
    """Minimum network matches 38,000 neurons."""
    from grut_solver.sectors.consciousness.self_reference import (
        minimum_complexity_for_self_reference
    )
    r = minimum_complexity_for_self_reference()
    assert 25000 < r["N_min_neurons"] < 50000
    assert r["above_kauffman_threshold"]
    print(f"  PASS: minimum_complexity (N = {r['N_min_neurons']:.0f}, k={r['mt_lattice_k']} > k_c={r['kauffman_k_critical']})")
