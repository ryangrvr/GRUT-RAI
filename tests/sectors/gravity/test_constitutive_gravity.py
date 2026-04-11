"""
Tests for Constitutive Gravity (Direction 2) and Stochastic Gravity (Direction 1).
18 tests covering Bianchi gate, GW propagation, ringdown, singularity,
cosmological memory, and stochastic gravity.
"""
import sys; sys.path.insert(0, ".")
import numpy as np


# ── Bianchi Gate ─────────────────────────────────────────────

def test_bianchi_naive_fails():
    from grut_solver.sectors.gravity.constitutive_gravity import bianchi_check_naive
    r = bianchi_check_naive()
    assert r["bianchi_satisfied"] is False
    assert r["status"] == "FAILS"
    print(f"  PASS: bianchi_naive FAILS (as expected)")

def test_bianchi_linearized_passes():
    from grut_solver.sectors.gravity.constitutive_gravity import bianchi_check_linearized
    r = bianchi_check_linearized()
    assert r["bianchi_satisfied"] is True
    assert r["status"] == "PASSES"
    print(f"  PASS: bianchi_linearized PASSES")

def test_bianchi_projected_passes():
    from grut_solver.sectors.gravity.constitutive_gravity import bianchi_check_projected
    r = bianchi_check_projected()
    assert r["bianchi_satisfied"] is True
    assert r["status"] == "PASSES"
    print(f"  PASS: bianchi_projected PASSES")

def test_gate_status_open():
    from grut_solver.sectors.gravity.constitutive_gravity import bianchi_gate_summary
    r = bianchi_gate_summary()
    assert "OPEN" in r["gate_status"]
    print(f"  PASS: gate_status = {r['gate_status']}")


# ── GW Propagation ───────────────────────────────────────────

def test_transfer_unity_at_low_freq():
    from grut_solver.sectors.gravity.gw_propagation import gw_transfer_function
    from grut_solver.constants import T_PLANCK
    r = gw_transfer_function(0.001, T_PLANCK)
    assert abs(r["amplitude_ratio"] - 1.0) < 1e-10
    assert abs(r["phase_shift_rad"]) < 1e-30
    print(f"  PASS: H(f) -> 1 at low frequency")

def test_ligo_unobservable_planck():
    from grut_solver.sectors.gravity.gw_propagation import ligo_observability
    from grut_solver.constants import T_PLANCK
    r = ligo_observability(T_PLANCK)
    assert not r["detectable"]
    assert r["max_phase_shift_rad"] < 1e-30
    print(f"  PASS: LIGO unobservable at T_Planck (phase = {r['max_phase_shift_rad']:.1e})")

def test_ligo_unobservable_tau_I():
    from grut_solver.sectors.gravity.gw_propagation import ligo_observability
    from grut_solver.constants import TAU_I
    r = ligo_observability(TAU_I)
    assert not r["detectable"]
    assert r["max_phase_shift_rad"] < 1e-20
    print(f"  PASS: LIGO unobservable at tau_I (phase = {r['max_phase_shift_rad']:.1e})")

def test_arrival_time_sign():
    from grut_solver.sectors.gravity.gw_propagation import arrival_time_difference
    from grut_solver.constants import T_PLANCK
    r = arrival_time_difference(T_PLANCK, 50.0, 200.0, 100.0)
    assert r["delta_t_s"] >= 0
    print(f"  PASS: arrival_time_difference >= 0 (dt = {r['delta_t_s']:.2e} s)")


# ── Ringdown ─────────────────────────────────────────────────

def test_qnm_standard_values():
    from grut_solver.sectors.gravity.ringdown import schwarzschild_qnm
    r = schwarzschild_qnm(30.0)
    assert 100 < r["f_R_hz"] < 500  # ~250 Hz for 30 M_sun
    assert r["Q_factor"] > 1
    print(f"  PASS: QNM f = {r['f_R_hz']:.0f} Hz, Q = {r['Q_factor']:.1f}")

def test_qnm_shift_small():
    from grut_solver.sectors.gravity.ringdown import constitutive_qnm_shift
    from grut_solver.constants import T_PLANCK
    r = constitutive_qnm_shift(30.0, T_PLANCK)
    assert r["fractional_shift_R"] < 1e-35
    assert not r["detectable"]
    print(f"  PASS: QNM shift = {r['fractional_shift_R']:.1e} (undetectable)")

def test_waveform_difference_negligible():
    from grut_solver.sectors.gravity.ringdown import ringdown_waveform
    from grut_solver.constants import T_PLANCK
    r = ringdown_waveform(np.linspace(0, 50, 100), 30.0, T_PLANCK)
    assert r["max_difference"] < 1e-30
    print(f"  PASS: waveform max diff = {r['max_difference']:.1e}")


# ── Singularity ──────────────────────────────────────────────

def test_friedmann_bounded_H():
    from grut_solver.sectors.gravity.singularity import constitutive_friedmann_ode
    r = constitutive_friedmann_ode(tau_grav=0.01, n_steps=10000)
    assert r["bounded"]
    assert np.all(np.isfinite(r["H_constitutive"]))
    print(f"  PASS: H(t) bounded, H_max = {r['H_max_constitutive']:.2e}")

def test_bounce_at_planck():
    from grut_solver.sectors.gravity.singularity import singularity_analysis_frw
    r = singularity_analysis_frw()
    assert r["bounces"]
    assert r["H_max_hz"] > 1e40
    print(f"  PASS: FRW bounces, H_max = {r['H_max_hz']:.2e} Hz")

def test_standard_recovery():
    from grut_solver.sectors.gravity.cosmological_memory import modified_friedmann_evolution
    from grut_solver.constants import T_PLANCK
    r = modified_friedmann_evolution(tau_grav=T_PLANCK)
    assert r["max_fractional_deviation"] < 1e-50
    print(f"  PASS: tau->T_Planck recovers standard (dev = {r['max_fractional_deviation']:.1e})")


# ── Cosmological Memory ─────────────────────────────────────

def test_late_time_negligible():
    from grut_solver.sectors.gravity.cosmological_memory import dark_energy_compatibility
    r = dark_energy_compatibility()
    assert not r["helps_dark_energy"]
    assert r["correction_at_z0"] < 1e-50
    print(f"  PASS: DE correction = {r['correction_at_z0']:.1e} (negligible)")

def test_dark_energy_no_help():
    from grut_solver.sectors.gravity.cosmological_memory import dark_energy_compatibility
    from grut_solver.constants import TAU_I
    r = dark_energy_compatibility(TAU_I)
    assert not r["helps_dark_energy"]
    print(f"  PASS: DE no help at tau_I (correction = {r['correction_at_z0']:.1e})")


# ── Stochastic Gravity ───────────────────────────────────────

def test_noise_kernel_standard_at_tau_zero():
    from grut_solver.sectors.gravity.stochastic_gravity import noise_kernel_flat_scalar
    f = np.logspace(6, 12, 20)
    r = noise_kernel_flat_scalar(f, T_K=300.0, tau_grav=0.0)
    N_std = np.array(r["N_standard"])
    N_grut = np.array(r["N_grut"])
    assert np.allclose(N_std, N_grut)
    print(f"  PASS: noise kernel = standard at tau=0")

def test_stochastic_subdominant():
    from grut_solver.sectors.gravity.stochastic_gravity import stochastic_decoherence_rate
    r = stochastic_decoherence_rate(1e-14, 100e-9)
    assert r["ratio_stoch_to_diosi"] < 1e-10
    assert r["dominant_channel"] == "Diósi (Sector 3)"
    print(f"  PASS: stochastic subdominant (ratio = {r['ratio_stoch_to_diosi']:.1e})")


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    passed = failed = 0
    for t in tests:
        try:
            t()
            passed += 1
        except Exception as e:
            print(f"  FAIL: {t.__name__}: {e}")
            failed += 1
    print(f"\n{'='*60}")
    print(f"Constitutive Gravity: {passed} passed, {failed} failed, {passed+failed} total")
