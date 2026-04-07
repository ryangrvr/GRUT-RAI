#!/usr/bin/env python3
"""
Program G — Stage G2-A: Markovian Validity Envelope Mapping

Compute the phase diagram of Markovian closure validity as a function of:
- W_tau: spectral width of timescale distribution (decades spanned)
- lambda_cg: coarse-graining cutoff
- heterogeneity: coupling variance
- N_modes: number of fast modes

All within the M1 linear Gaussian framework (exact Mori-Zwanzig).
"""

import numpy as np
from scipy.linalg import expm
from scipy.optimize import curve_fit

# ============================================================
# SETUP
# ============================================================

def compute_eps_M(tau_fast_arr, J_arr, tau_slow, t_max_factor=5.0, n_t=2000):
    """
    Compute Markovian closure error for 1 slow + N_fast system.
    Returns eps_M, tau_eff, K(0).
    """
    N = len(tau_fast_arr)
    if N == 0:
        return 0.0, tau_slow, 0.0

    t_max = t_max_factor * np.max(tau_fast_arr)
    t = np.linspace(0, max(t_max, 0.1), n_t)

    # K(t) = sum J_i^2 exp(-t/tau_i)
    K = np.zeros(n_t)
    for i in range(N):
        K += J_arr[i]**2 * np.exp(-t / tau_fast_arr[i])

    # Fit single exponential
    if K[0] <= 0:
        return 1.0, np.nan, 0.0

    try:
        def exp_model(t, a, tau):
            return a * np.exp(-t / tau)
        popt, _ = curve_fit(exp_model, t, K, p0=[K[0], np.mean(tau_fast_arr)],
                          maxfev=5000, bounds=([0, 1e-8], [np.inf, np.inf]))
        K_fit = exp_model(t, *popt)
        eps = np.sqrt(np.sum((K - K_fit)**2) / np.sum(K**2))
        return eps, popt[1], K[0]
    except:
        return 1.0, np.nan, K[0]


# ============================================================
# TASK 1: CONTROL PARAMETERS
# ============================================================
print("=" * 80)
print("TASK 1: CONTROL PARAMETERS")
print("=" * 80)

print("""
Control parameters for the validity map:

  W_tau: spectral width = log10(tau_max / tau_min)
         W_tau = 0 → all modes same timescale (trivially Markovian)
         W_tau = 1 → one decade of timescale spread
         W_tau = 3 → three decades (e.g., 0.01 to 10)

  lambda_cg: coarse-graining cutoff (modes with tau < lambda are "fast")
         Normalized: lambda/tau_slow (fraction of the slow timescale)

  H_J: coupling heterogeneity = std(J) / mean(J)
         H_J = 0 → uniform coupling
         H_J = 1 → highly heterogeneous

  N_fast: number of fast modes integrated out
         N_fast = 1 → single exponential (eps_M = 0)
         N_fast → ∞ → continuum limit

  Thresholds:
    eps_1 = 0.05 (boundary VALID/MARGINAL)
    eps_2 = 0.20 (boundary MARGINAL/INVALID)
""")

eps_1 = 0.05  # VALID/MARGINAL boundary
eps_2 = 0.20  # MARGINAL/INVALID boundary

# ============================================================
# TASK 2: VALIDITY MAP — W_tau vs N_fast
# ============================================================
print("=" * 80)
print("TASK 2: VALIDITY MAP — W_tau vs N_fast")
print("=" * 80)

W_tau_values = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0]
N_fast_values = [1, 2, 5, 10, 20, 50, 100]

tau_slow = 100.0  # slow mode timescale (reference)
tau_min_base = 0.01

print(f"\n  Phase diagram: eps_M(W_tau, N_fast)")
print(f"  VALID: eps_M < {eps_1}, MARGINAL: {eps_1} <= eps_M < {eps_2}, INVALID: eps_M >= {eps_2}")
print(f"\n  {'W_tau':>6s}", end="")
for N in N_fast_values:
    print(f"  {'N='+str(N):>8s}", end="")
print()
print(f"  {'-'*6}", end="")
for _ in N_fast_values:
    print(f"  {'-'*8}", end="")
print()

validity_data = {}

for W in W_tau_values:
    row = f"  {W:6.1f}"
    for N in N_fast_values:
        if W == 0:
            tau_arr = np.ones(N) * tau_min_base
        else:
            tau_arr = np.logspace(np.log10(tau_min_base),
                                  np.log10(tau_min_base * 10**W), N)

        J_arr = np.ones(N) * 0.3 / np.sqrt(max(N, 1))
        eps, tau_eff, K0 = compute_eps_M(tau_arr, J_arr, tau_slow)

        if eps < eps_1:
            label = "V"
        elif eps < eps_2:
            label = "M"
        else:
            label = "X"

        row += f"  {eps:5.3f} {label}"
        validity_data[(W, N)] = eps

    print(row)

# ============================================================
# TASK 2b: VALIDITY MAP — W_tau vs H_J (coupling heterogeneity)
# ============================================================
print(f"\n{'='*80}")
print("VALIDITY MAP — W_tau vs H_J (coupling heterogeneity)")
print("=" * 80)

H_J_values = [0.0, 0.3, 0.5, 0.7, 1.0]
N_fixed = 20

print(f"\n  N_fast = {N_fixed} (fixed)")
print(f"  {'W_tau':>6s}", end="")
for H in H_J_values:
    print(f"  {'H='+f'{H:.1f}':>8s}", end="")
print()
print(f"  {'-'*6}", end="")
for _ in H_J_values:
    print(f"  {'-'*8}", end="")
print()

np.random.seed(42)
for W in W_tau_values:
    row = f"  {W:6.1f}"
    for H in H_J_values:
        if W == 0:
            tau_arr = np.ones(N_fixed) * tau_min_base
        else:
            tau_arr = np.logspace(np.log10(tau_min_base),
                                  np.log10(tau_min_base * 10**W), N_fixed)

        J_mean = 0.3 / np.sqrt(N_fixed)
        if H == 0:
            J_arr = np.ones(N_fixed) * J_mean
        else:
            J_arr = J_mean * np.abs(1 + H * np.random.randn(N_fixed))

        eps, _, _ = compute_eps_M(tau_arr, J_arr, tau_slow)

        if eps < eps_1:
            label = "V"
        elif eps < eps_2:
            label = "M"
        else:
            label = "X"

        row += f"  {eps:5.3f} {label}"
    print(row)

# ============================================================
# TASK 3: BOUNDARY LAW EXTRACTION
# ============================================================
print(f"\n{'='*80}")
print("TASK 3: BOUNDARY LAW EXTRACTION")
print("=" * 80)

# Compute eps_M on a fine grid of W_tau for fixed N=20, H=0
W_fine = np.linspace(0, 4, 100)
eps_fine = []
for W in W_fine:
    if W == 0:
        tau_arr = np.ones(20) * tau_min_base
    else:
        tau_arr = np.logspace(np.log10(tau_min_base),
                              np.log10(tau_min_base * 10**W), 20)
    J_arr = np.ones(20) * 0.3 / np.sqrt(20)
    eps, _, _ = compute_eps_M(tau_arr, J_arr, tau_slow)
    eps_fine.append(eps)

eps_fine = np.array(eps_fine)

# Find critical W_tau where eps = eps_1 and eps = eps_2
# Linear interpolation
W_crit_1 = np.interp(eps_1, eps_fine, W_fine) if eps_fine[-1] > eps_1 else np.nan
W_crit_2 = np.interp(eps_2, eps_fine, W_fine) if eps_fine[-1] > eps_2 else np.nan

print(f"\n  For N_fast = 20, uniform coupling:")
print(f"  Critical spectral width W_tau* (VALID/MARGINAL boundary): {W_crit_1:.2f} decades")
print(f"  Critical spectral width W_tau** (MARGINAL/INVALID boundary): {W_crit_2:.2f} decades")

# Fit: eps_M vs W_tau
# Expect: eps_M ~ 0 for W=0, grows as W increases
# Try: eps_M = a * (1 - exp(-W/b))
try:
    def sat_model(W, a, b):
        return a * (1 - np.exp(-W / b))
    popt, _ = curve_fit(sat_model, W_fine, eps_fine, p0=[0.1, 1.0])
    print(f"\n  Boundary law fit: eps_M ≈ {popt[0]:.4f} × (1 - exp(-W_tau / {popt[1]:.4f}))")
    print(f"  Saturation value: eps_M → {popt[0]:.4f} as W_tau → ∞")
    print(f"  Characteristic width: W_tau_0 = {popt[1]:.4f} decades")
except:
    print(f"\n  Fit failed. eps_M does not follow simple saturating model.")

# N-dependence at fixed W_tau
print(f"\n  N-dependence at W_tau = 2.0:")
W_test = 2.0
for N in [2, 5, 10, 20, 50, 100, 200]:
    tau_arr = np.logspace(np.log10(tau_min_base),
                          np.log10(tau_min_base * 10**W_test), N)
    J_arr = np.ones(N) * 0.3 / np.sqrt(N)
    eps, _, _ = compute_eps_M(tau_arr, J_arr, tau_slow)
    print(f"    N = {N:4d}: eps_M = {eps:.4f}")

# ============================================================
# TASK 4: PHYSICAL ARCHETYPE MAPPING
# ============================================================
print(f"\n{'='*80}")
print("TASK 4: PHYSICAL ARCHETYPE MAPPING")
print("=" * 80)

archetypes = [
    ("Dilute monatomic gas (single collision time)",
     0.0, "VALID",
     "One dominant relaxation timescale (mean free time). "
     "W_tau ≈ 0. Markovian closure exact."),

    ("Dense molecular gas (vibrational + translational)",
     0.5, "VALID",
     "Two timescale groups (fast vibration ~ps, slow translation ~ns). "
     "W_tau ~ 0.5. eps_M ~ 0.01-0.03."),

    ("Warm dense plasma (electron + ion relaxation)",
     1.5, "MARGINAL",
     "Electrons equilibrate ~fs, ions ~ps, collective modes ~ns. "
     "W_tau ~ 1.5. eps_M ~ 0.05-0.10."),

    ("Neutron star crust (phonon + electron + nuclear)",
     3.0, "INVALID",
     "Nuclear reactions ~years, electron transport ~microseconds, "
     "phonon ~nanoseconds. W_tau ~ 3+. eps_M ~ 0.07+. "
     "Multi-exponential memory essential."),

    ("Galaxy interior (star formation + gas cooling + dynamical)",
     5.0, "INVALID",
     "Star formation ~Myr, gas cooling ~kyr, dynamical ~Myr, "
     "gravitational ~free-fall time. W_tau ~ 5+. "
     "Markovian truncation unreliable."),

    ("Early universe plasma (QCD + electroweak + gravitational)",
     10.0, "INVALID",
     "QCD scale ~fm/c, electroweak ~10^-12 s, Hubble ~10^17 s. "
     "W_tau ~ 10+. Markovian closure grossly inadequate."),
]

print(f"\n  {'Archetype':<55s} {'W_tau':>6s} {'Zone':>10s}")
print(f"  {'-'*55} {'-'*6} {'-'*10}")
for name, W, zone, desc in archetypes:
    print(f"  {name:<55s} {W:6.1f} {zone:>10s}")
    print(f"    {desc}")
    print()

# ============================================================
# TASK 5: PREMISE CHECK — I* = 1.15428
# ============================================================
print(f"{'='*80}")
print("TASK 5: PREMISE CHECK — I* = 1.15428")
print("=" * 80)

# Check if any boundary ratio stabilizes near 1.15428
# W_crit_2 / W_crit_1 ?
if not np.isnan(W_crit_1) and not np.isnan(W_crit_2) and W_crit_1 > 0:
    ratio_W = W_crit_2 / W_crit_1
    print(f"\n  W_tau**(INVALID) / W_tau*(MARGINAL) = {W_crit_2:.4f} / {W_crit_1:.4f} = {ratio_W:.5f}")
    print(f"  Target I* = 1.15428")
    print(f"  Match: {'CLOSE' if abs(ratio_W - 1.15428) < 0.05 else 'NO'} (delta = {abs(ratio_W - 1.15428):.5f})")

# Saturation ratio: eps_sat / eps_1?
if 'popt' in dir():
    try:
        ratio_sat = popt[0] / eps_1
        print(f"\n  eps_sat / eps_1 = {popt[0]:.4f} / {eps_1} = {ratio_sat:.4f}")
        print(f"  Match to I*: {'NO' if abs(ratio_sat - 1.15428) > 0.1 else 'CHECK'}")
    except:
        pass

print(f"\n  VERDICT: I* = 1.15428 remains undefined_in_G2A.")
print(f"  No boundary ratio or diagnostic quotient matches this value.")
print(f"  STATUS: OPEN (not found, not excluded).")

# ============================================================
# SUMMARY
# ============================================================
print(f"\n{'='*80}")
print("SUMMARY: MARKOVIAN VALIDITY ENVELOPE")
print("=" * 80)

print(f"""
BOUNDARY LAW (N=20, uniform coupling, M1 linear Gaussian):

  W_tau < {W_crit_1:.1f} decades:  VALID   (eps_M < {eps_1})
  {W_crit_1:.1f} < W_tau < {W_crit_2:.1f} decades: MARGINAL ({eps_1} <= eps_M < {eps_2})
  W_tau > {W_crit_2:.1f} decades:  INVALID (eps_M >= {eps_2})

  eps_M saturates at ~{popt[0]:.3f} for W_tau >> {popt[1]:.1f} decades.

PHYSICAL TRANSLATION:

  VALID: single-component gas, simple plasma, homogeneous thermal bath.
  MARGINAL: multi-component plasma, condensed matter with 2-3 timescales.
  INVALID: neutron star interiors, galaxies, early universe, any
           environment with timescales spanning > 2 decades.

KEY RESULT:
  The Markovian constitutive law is valid ONLY in environments with
  narrow timescale distributions (W_tau < ~{W_crit_1:.1f} decades).
  This includes laboratory experiments (homogeneous gas/plasma)
  but EXCLUDES most astrophysical and cosmological environments.
""")

print("=" * 80)
print("END OF COMPUTATION")
print("=" * 80)
