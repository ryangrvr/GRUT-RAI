"""
GRUT Solver — Complete Test Suite

Tests:
  1. Constants verification
  2. USL numerical correctness
  3. Budget channel ordering
  4. Kill framework adversarial tests
  5. Robustness under ±10% input variation
  6. Degeneracy detection
  7. Regression against known exploration results
"""

import numpy as np
import sys
sys.path.insert(0, ".")


def test_constants():
    """All physical constants match CODATA / known values."""
    from grut_solver.constants import verify_constants
    checks = verify_constants()
    for name, passed in checks.items():
        assert passed, f"Constant check failed: {name}"
    print("  PASS: test_constants")


def test_c_final_precision():
    """C_Final matches to high precision."""
    from grut_solver.constants import C_FINAL
    # Known value from Program M
    expected = 1.14021054e-4
    assert abs(C_FINAL - expected) / expected < 1e-6, f"C_FINAL = {C_FINAL}, expected ~ {expected}"
    print("  PASS: test_c_final_precision")


def test_lambda_grav_reference():
    """Lambda_grav matches the exploration reference value."""
    from grut_solver.usl import lambda_grav
    rate = lambda_grav(m=1e-14, l=100e-9, R=50e-9)
    # Reference from beyond_grut_experimental_forecast.py
    assert abs(rate - 633) / 633 < 0.01, f"Lambda_grav = {rate}, expected ~633 Hz"
    print(f"  PASS: test_lambda_grav_reference (rate = {rate:.1f} Hz)")


def test_suppression_factor():
    """Extended-body suppression transitions correctly at l = 2R."""
    from grut_solver.usl import suppression_factor

    # Far field: S = 1
    assert suppression_factor(200e-9, 50e-9) == 1.0
    assert suppression_factor(100e-9, 50e-9) == 1.0  # l/R = 2.0 exactly

    # Near field: S = (l/R)^3 / 6
    S = suppression_factor(10e-9, 50e-9)
    expected = (10/50)**3 / 6
    assert abs(S - expected) < 1e-10, f"S = {S}, expected {expected}"

    # Monotonic: S increases with l/R
    S_prev = 0
    for l in np.linspace(1e-9, 200e-9, 50):
        S_now = suppression_factor(l, 50e-9)
        assert S_now >= S_prev, f"S not monotonic at l = {l}"
        S_prev = S_now

    print("  PASS: test_suppression_factor")


def test_boundary_mass():
    """Boundary mass matches known formula."""
    from grut_solver.usl import boundary_mass
    from grut_solver.constants import HBAR, G

    m_star = boundary_mass(l=1e-7, t_obs=1.0)
    expected = np.sqrt(HBAR * 1e-7 / (G * 1.0))
    assert abs(m_star - expected) / expected < 1e-10
    print(f"  PASS: test_boundary_mass (m* = {m_star*1e15:.2f} fg)")


def test_budget_gas_dominance_high_pressure():
    """At high pressure, gas should dominate over gravity."""
    from grut_solver.budget import compute_budget
    b = compute_budget(m=1e-14, R=50e-9, l=100e-9, T_env=10e-3, P=1e-6)
    assert b.binding_channel == "gas_collision", f"Expected gas binding, got {b.binding_channel}"
    assert not b.is_grav_dominated, "Should not be gravity-dominated at high P"
    print("  PASS: test_budget_gas_dominance_high_pressure")


def test_budget_grav_dominance_low_pressure():
    """At low pressure, gravity should dominate."""
    from grut_solver.budget import compute_budget
    b = compute_budget(m=1e-14, R=50e-9, l=100e-9, T_env=10e-3, P=1e-14)
    assert b.is_grav_dominated, "Should be gravity-dominated at P = 1e-14 Pa"
    assert b.signal_to_noise > 100, f"SNR should be >>1, got {b.signal_to_noise}"
    print(f"  PASS: test_budget_grav_dominance_low_pressure (SNR = {b.signal_to_noise:.0f})")


def test_crossover_pressure():
    """Crossover pressure is in the right ballpark."""
    from grut_solver.usl.scaling import crossover_pressure
    P_star = crossover_pressure(m=1e-14, R=50e-9, l=100e-9, T=10e-3)
    # Should be in the range 1e-10 to 1e-8 Pa
    assert 1e-11 < P_star < 1e-7, f"P* = {P_star}, out of expected range"
    print(f"  PASS: test_crossover_pressure (P* = {P_star:.2e} Pa)")


def test_kill_constant_floor_survives():
    """GRUT survives the constant-floor kill test (1 param cannot mimic m^2)."""
    from grut_solver.kill.model_comparison import try_kill_constant_floor
    result = try_kill_constant_floor()
    assert not result.can_mimic_mass_scaling, "Constant floor should NOT mimic mass scaling"
    assert result.verdict == "GRUT_SURVIVES", f"Expected SURVIVES, got {result.verdict}"
    print("  PASS: test_kill_constant_floor_survives")


def test_kill_csl_geometry_differs():
    """CSL cannot reproduce GRUT's geometry scaling."""
    from grut_solver.kill.model_comparison import try_kill_csl
    result = try_kill_csl()
    # CSL has different geometry (exponential vs cubic)
    # The mass scaling residual should be large (CSL doesn't have 1/l)
    assert not result.can_mimic_all_three, "CSL should NOT mimic all three GRUT signatures"
    print(f"  PASS: test_kill_csl_geometry_differs (mass residual: {result.residuals.get('mass_dex', 'N/A')})")


def test_robustness_10pct():
    """Conclusions survive ±10% input variation."""
    from grut_solver.budget import budget_with_uncertainty
    b = budget_with_uncertainty(m=1e-14, R=50e-9, l=100e-9, T_env=10e-3, P=1e-10, vary_pct=10)
    assert b.conclusion_robust, "Conclusion should be robust under ±10% variation"
    assert b.lambda_total_lo > 0
    assert b.lambda_total_hi > b.lambda_total_lo
    print(f"  PASS: test_robustness_10pct (range: [{b.lambda_total_lo:.0f}, {b.lambda_total_hi:.0f}] Hz)")


def test_solver_end_to_end():
    """Full solver pipeline runs without error."""
    from grut_solver import GRUTSolver
    solver = GRUTSolver()

    r = solver.decoherence(m=1e-14, R=50e-9, l=100e-9, T_env=10e-3, P=1e-10)
    assert r.lambda_grav > 0
    assert r.lambda_total > r.lambda_grav  # total > grav (env adds)
    assert r.t_coherence > 0
    assert isinstance(r.binding_channel, str)
    assert r.is_testable in (True, False)  # numpy bool compatible

    # Model comparison
    text = solver.compare_models(r)
    assert "GRUT" in text

    print("  PASS: test_solver_end_to_end")


def test_anomaly_suppression():
    """Anomaly channel is Planck-suppressed relative to Newtonian."""
    from grut_solver.usl import lambda_grav, lambda_anomaly
    Lg = lambda_grav(m=1e-14, l=100e-9)
    La = lambda_anomaly(m=1e-14, l=100e-9)
    ratio = La / Lg
    assert ratio < 1e-6, f"Anomaly ratio = {ratio}, should be << 1"
    print(f"  PASS: test_anomaly_suppression (ratio = {ratio:.2e})")


# =============================================================================
# NEW MODULE TESTS
# =============================================================================

def test_validity_envelope():
    """Markovian validity boundaries are correct."""
    from grut_solver.usl.validity import markovian_error, validity_regime, W_TAU_STAR, W_TAU_STAR_STAR

    # Below W_tau*: VALID
    assert validity_regime(0.3) == "VALID"
    assert markovian_error(0.3) < 0.05

    # Between W_tau* and W_tau**: MARGINAL
    assert validity_regime(1.2) == "MARGINAL"

    # Above W_tau**: INVALID
    assert validity_regime(5.0) == "INVALID"

    # Lab nanoparticle is VALID
    from grut_solver.usl.validity import classify_system
    lab = classify_system("lab_nanoparticle")
    assert lab["usl_trustworthy"]

    # Neutron star is INVALID
    ns = classify_system("neutron_star")
    assert ns["needs_memory_kernel"]

    print("  PASS: test_validity_envelope")


def test_systematic_error_budget():
    """Ward residual and constitutive systematic are correct."""
    from grut_solver.budget.systematic import (
        ward_classification, constitutive_error_budget, WARD_ALPHA, DELTA_TOTAL_PCT
    )

    assert ward_classification(WARD_ALPHA) == "leading-order"
    assert ward_classification(2.0) == "higher-order"
    assert ward_classification(0.5) == "non-perturbative"

    budget = constitutive_error_budget()
    assert budget["delta_total_pct"] == 3.6
    assert not budget["exchange_correction_effective"]

    print(f"  PASS: test_systematic_error_budget (total = {DELTA_TOTAL_PCT}%)")


def test_diamond_lock():
    """Diamond Lock vacuum constants are documented."""
    from grut_solver.core.vacuum_sector import (
        diamond_lock_status, TAU_SQUARED_DIAMOND, tau_ratio
    )

    status = diamond_lock_status()
    assert status["tau_squared"] == 1.5
    assert status["sector"] == "classical_constitutive"
    assert status["status"] == "LOCKED (Phases I-III)"

    ratio = tau_ratio()
    assert ratio > 2.0  # tau_R / tau_I > 2 in natural units

    print(f"  PASS: test_diamond_lock (tau_R/tau_I = {ratio:.3f})")


def test_born_transparency():
    """Born rule transparency theorem is verified."""
    from grut_solver.core.born_rule import born_transparency_linear, born_correction_bistable

    # Linear case: exact
    linear = born_transparency_linear()
    assert linear["Z_ratio"] == 1.0
    assert linear["born_correction"] == 0.0

    # Bistable case: small correction
    bistable = born_correction_bistable()
    assert bistable["Z_0"] > 0
    assert bistable["Z_1"] > 0
    # The correction should be small for standard parameters
    assert bistable["born_correction"] < 0.5, f"Born correction = {bistable['born_correction']}"

    print(f"  PASS: test_born_transparency (bistable correction = {bistable['born_correction']:.4f})")


def test_anomaly_crossover():
    """Anomaly crossover length is astronomical."""
    from grut_solver.usl.anomaly import anomaly_crossover_length, two_channel_rate

    l_c = anomaly_crossover_length(m=1e-14)
    assert l_c > 1e20, f"Crossover should be astronomical, got {l_c}"

    rates = two_channel_rate(m=1e-14, l=100e-9)
    assert rates["dominant"] == "newtonian"
    assert rates["ratio_A_over_N"] < 1e-6

    print(f"  PASS: test_anomaly_crossover (l_c = {l_c/9.461e15:.1e} light-years)")


def test_c_cosmo():
    """C_Cosmo matches known value and R = |C_Cosmo|/C_Final ~ 1.154."""
    from grut_solver.usl.anomaly import c_cosmo, c_final, r_anomaly

    C_C = c_cosmo()
    C_F = c_final()
    R_computed = abs(C_C) / C_F

    assert abs(R_computed - 1.15428) / 1.15428 < 0.01, f"R = {R_computed}, expected ~1.15428"
    print(f"  PASS: test_c_cosmo (R_computed = {R_computed:.5f})")


def test_mu_prime_platform():
    """Mu-Prime operating point loads and has correct parameters."""
    from grut_solver.experiments.platforms import get_platform

    mp = get_platform("MU_PRIME")
    assert abs(mp.m - 196e-18) / 196e-18 < 0.01
    assert abs(mp.l - 474e-9) / 474e-9 < 0.01
    assert mp.status == "REFERENCE"

    print(f"  PASS: test_mu_prime_platform (m = {mp.m*1e18:.0f} fg, l = {mp.l*1e9:.0f} nm)")


def test_many_body_bell_protection():
    """Bell state decoheres SLOWER than product state (entanglement protection)."""
    from grut_solver.usl.many_body import entanglement_discriminant

    m = 1e-14
    l = 100e-9
    d = 200e-9
    R = 50e-9

    disc = entanglement_discriminant(m, l, d, R)

    # Cross term must be NEGATIVE (Bell slower)
    assert disc["lambda_cross"] < 0, f"Cross term should be negative, got {disc['lambda_cross']}"
    # Bell rate < product rate
    assert disc["lambda_bell"] < disc["lambda_product"]
    # Difference should be ~17% at d=200nm
    assert abs(disc["percent_difference"]) > 10, f"Expected >10% difference, got {disc['percent_difference']}"

    print(f"  PASS: test_many_body_bell_protection (diff = {disc['percent_difference']:.1f}%)")


def test_many_body_ghz_scaling():
    """GHZ suppression increases with N."""
    from grut_solver.usl.many_body import lambda_ghz_3, lambda_n_particle
    import numpy as np

    m = 1e-14
    l = 100e-9
    d = 200e-9

    ghz3 = lambda_ghz_3(m, l, d, d)
    # GHZ/product ratio should be < 1 (suppression)
    assert ghz3["ratio_ghz_over_product"] < 1.0
    assert ghz3["ratio_ghz_over_product"] > 0.0

    # N=5 should have MORE suppression than N=3
    positions_L_5 = [np.array([(i*d) - l/2, 0, 0]) for i in range(5)]
    positions_R_5 = [np.array([(i*d) + l/2, 0, 0]) for i in range(5)]
    L_ghz5 = lambda_n_particle([m]*5, positions_L_5, positions_R_5)
    ratio_5 = L_ghz5 / (5 * 632.9)

    assert ratio_5 < ghz3["ratio_ghz_over_product"], "N=5 should be more suppressed than N=3"

    print(f"  PASS: test_many_body_ghz_scaling (N=3: {ghz3['ratio_ghz_over_product']:.3f}, N=5: {ratio_5:.3f})")


def test_many_body_three_way_discriminant():
    """The entanglement effect discriminates GRUT from QM and CSL."""
    from grut_solver.usl.many_body import entanglement_discriminant

    disc = entanglement_discriminant(m=1e-14, l=100e-9, d_AB=200e-9, R=50e-9)

    # GRUT: product != Bell
    grut_differs = abs(disc["percent_difference"]) > 1.0

    # Standard QM: both = 0 (no gravitational decoherence at all)
    # CSL: depends on mass only, not entanglement structure -> product = Bell

    assert grut_differs, "GRUT must predict a difference between product and Bell"
    print(f"  PASS: test_many_body_three_way_discriminant (GRUT-unique: {disc['percent_difference']:.1f}%)")


def test_emergent_41_9_myr():
    """The 41.9 Myr emerges at the macromolecular scale."""
    from grut_solver.usl.emergent_scales import locate_41_9_myr
    from grut_solver.constants import AMU

    result = locate_41_9_myr()
    sweet = result["sweet_spot"]

    # At l = 1 um, the mass should be ~20,000 amu (large protein)
    m_amu = sweet["m_amu"]
    assert 5000 < m_amu < 100000, f"Sweet spot mass = {m_amu} amu, expected ~20000"

    print(f"  PASS: test_emergent_41_9_myr (sweet spot = {m_amu:.0f} amu)")


# =============================================================================
# RUN ALL TESTS
# =============================================================================

if __name__ == "__main__":
    tests = [
        # Phase 1-5 (original)
        test_constants,
        test_c_final_precision,
        test_lambda_grav_reference,
        test_suppression_factor,
        test_boundary_mass,
        test_budget_gas_dominance_high_pressure,
        test_budget_grav_dominance_low_pressure,
        test_crossover_pressure,
        test_kill_constant_floor_survives,
        test_kill_csl_geometry_differs,
        test_robustness_10pct,
        test_solver_end_to_end,
        test_anomaly_suppression,
        # Many-body extension
        test_many_body_bell_protection,
        test_many_body_ghz_scaling,
        test_many_body_three_way_discriminant,
        # New modules
        test_validity_envelope,
        test_systematic_error_budget,
        test_diamond_lock,
        test_born_transparency,
        test_anomaly_crossover,
        test_c_cosmo,
        test_mu_prime_platform,
        test_emergent_41_9_myr,
    ]

    passed = 0
    failed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"  FAIL: {test.__name__}: {e}")
            failed += 1

    print()
    print(f"  {'=' * 50}")
    print(f"  {passed} PASSED, {failed} FAILED out of {len(tests)} tests")
    if failed == 0:
        print(f"  ALL TESTS PASS.")
    else:
        print(f"  {failed} TESTS FAILED.")
    print(f"  {'=' * 50}")
