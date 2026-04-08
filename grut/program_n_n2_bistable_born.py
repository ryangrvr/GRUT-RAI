#!/usr/bin/env python3
"""
Program N - Stage N2: Bistable Quantum-Constitutive Selection

N1 showed: linear constitutive dynamics CANNOT select outcomes (one attractor = averaging).
N2 tests: does BISTABLE constitutive dynamics produce outcome selection with Born-rule statistics?

Model:
  Quantum system: 2-level, superposition |psi> = c0|0> + c1|1>
  Constitutive sector: coupled (Phi, Psi) with cubic saturation (GRUT-II Nu architecture)
  Coupling: the quantum state determines which attractor basin the constitutive field enters

The key mechanism:
  1. Quantum amplitudes c0, c1 set the initial constitutive landscape
     (through branch-dependent sources X_0, X_1)
  2. The coupled (Phi,Psi) system has TWO stable fixed points
  3. Noise drives the system into one basin
  4. The PROBABILITY of selecting basin i should be tested against |c_i|^2

NO IMPORTED ASSUMPTIONS about the Born rule.
NO assumption that tau = hbar/(kT).
NO assumption about the noise floor.
The Born rule is the TARGET, not the input.
"""

import numpy as np

# ============================================================
# MODEL: BISTABLE CONSTITUTIVE DYNAMICS
# ============================================================

# From GRUT-II Nu / Book C:
# tau1 dPhi/dt = a*(X - Phi) - kappa*Psi
# tau2 dPsi/dt = epsilon*Phi + (sigma-1)*Psi - nu*Psi^3
#
# With the QUANTUM modification:
# X depends on the quantum state through the density matrix:
# X = X_0 * rho_00 + X_1 * rho_11
# (same mean-field coupling as N1, but now the constitutive dynamics is BISTABLE)

# Bistable parameters (from C2, verified):
tau1 = 1.0
tau2 = 1.0
a = 1.0
kappa = 0.3
epsilon = 0.2
sigma = 2.0
nu = 1.0

# The source values for the two branches:
X_branch_0 = 2.0   # constitutive target when system is in |0>
X_branch_1 = -2.0  # constitutive target when system is in |1>

# Quantum parameters
hbar = 1.0
E0 = 0.0; E1 = 0.0  # DEGENERATE energy levels (no free precession)
lambda_c = 0.3  # coupling of Phi back to quantum sector

# ============================================================
# FIND THE TWO ATTRACTORS
# ============================================================

def find_attractors(X_val):
    """Find stable fixed points of the coupled (Phi, Psi) system for given X."""
    # At FP: a*(X - Phi) - kappa*Psi = 0 and epsilon*Phi + (sigma-1)*Psi - nu*Psi^3 = 0
    # From first: Phi = X - kappa*Psi/a
    # Substitute: epsilon*(X - kappa*Psi/a) + (sigma-1)*Psi - nu*Psi^3 = 0
    # epsilon*X + (sigma - 1 - epsilon*kappa/a)*Psi - nu*Psi^3 = 0
    c_lin = sigma - 1 - epsilon*kappa/a
    c_const = epsilon * X_val
    # nu*Psi^3 - c_lin*Psi - c_const = 0
    coeffs = [nu, 0, -c_lin, -c_const]
    roots = np.roots(coeffs)
    real_roots = sorted([r.real for r in roots if abs(r.imag) < 1e-8])

    fps = []
    for Psi_s in real_roots:
        Phi_s = X_val - kappa * Psi_s / a
        J = np.array([[-a/tau1, -kappa/tau1],
                       [epsilon/tau2, (sigma - 1 - 3*nu*Psi_s**2)/tau2]])
        eigs = np.linalg.eigvals(J)
        stable = all(np.real(eigs) < 0)
        if stable:
            fps.append((Phi_s, Psi_s))
    return fps

# For X = 0 (equal superposition: X = X_0*0.5 + X_1*0.5 = 0):
fps_equal = find_attractors(0.0)
print("=" * 90)
print("N2: Bistable Quantum-Constitutive Selection")
print("=" * 90)
print(f"\nAt equal superposition (X = 0):")
print(f"  Stable fixed points: {len(fps_equal)}")
for i, (phi, psi) in enumerate(fps_equal):
    print(f"  FP{i}: Phi* = {phi:.4f}, Psi* = {psi:.4f}")

# For different X values (different superposition ratios):
print(f"\nAttractor structure vs source X:")
print(f"  {'X':>8s} {'#FPs':>6s} {'Phi*_A':>10s} {'Phi*_B':>10s}")
for X_test in np.linspace(-2, 2, 21):
    fps = find_attractors(X_test)
    if len(fps) >= 2:
        print(f"  {X_test:8.2f} {len(fps):6d} {fps[0][0]:10.4f} {fps[-1][0]:10.4f}")
    elif len(fps) == 1:
        print(f"  {X_test:8.2f} {len(fps):6d} {fps[0][0]:10.4f} {'---':>10s}")
    else:
        print(f"  {X_test:8.2f} {len(fps):6d} {'---':>10s} {'---':>10s}")

# ============================================================
# BASIN SELECTION WITH NOISE
# ============================================================
print(f"\n{'='*90}")
print("BASIN SELECTION: noise-driven Phi falling into one attractor")
print("=" * 90)

D_Phi = 0.3  # noise on Phi
D_Psi = 0.3  # noise on Psi
dt = 0.01
T_sim = 30.0
N_steps = int(T_sim / dt)

def run_bistable_trial(X_source, D_Phi, D_Psi, seed, Phi_init=0.0, Psi_init=0.0):
    """Run one stochastic trial of the bistable (Phi, Psi) system.
    Returns the final (Phi, Psi) and which attractor it reached."""
    np.random.seed(seed)
    Phi = Phi_init
    Psi = Psi_init

    for step in range(N_steps):
        dW_Phi = np.random.randn() * np.sqrt(dt)
        dW_Psi = np.random.randn() * np.sqrt(dt)

        dPhi = (a*(X_source - Phi) - kappa*Psi) / tau1 * dt + np.sqrt(2*D_Phi)/tau1 * dW_Phi
        dPsi = (epsilon*Phi + (sigma-1)*Psi - nu*Psi**3) / tau2 * dt + np.sqrt(2*D_Psi)/tau2 * dW_Psi

        Phi += dPhi
        Psi += dPsi

    return Phi, Psi

# First: verify bistability at X = 0 with noise
N_ens = 300
print(f"\n  Noise test at X = 0 (equal superposition), D = {D_Phi}:")
print(f"  Ensemble size: {N_ens}")

basin_A = 0; basin_B = 0; basin_other = 0
fps_ref = find_attractors(0.0)

if len(fps_ref) >= 2:
    Phi_A, Phi_B = fps_ref[0][0], fps_ref[-1][0]
    Phi_mid = (Phi_A + Phi_B) / 2

    for trial in range(N_ens):
        Phi_f, Psi_f = run_bistable_trial(0.0, D_Phi, D_Psi, seed=trial)
        if Phi_f < Phi_mid:
            basin_A += 1
        else:
            basin_B += 1

    print(f"  Attractor A (Phi* = {Phi_A:.3f}): {basin_A}/{N_ens} = {basin_A/N_ens:.3f}")
    print(f"  Attractor B (Phi* = {Phi_B:.3f}): {basin_B}/{N_ens} = {basin_B/N_ens:.3f}")
    print(f"  At X = 0 (symmetric): expect ~50/50. Got: {basin_A/N_ens:.3f}/{basin_B/N_ens:.3f}")

# ============================================================
# BORN RULE TEST: vary |c0|^2 and check basin fractions
# ============================================================
print(f"\n{'='*90}")
print("BORN RULE TEST: does p(basin) = |c_i|^2?")
print("=" * 90)

# The quantum superposition |psi> = c0|0> + c1|1> produces:
# X = X_branch_0 * |c0|^2 + X_branch_1 * |c1|^2
# = X_branch_0 * p0 + X_branch_1 * (1-p0)
# where p0 = |c0|^2

# As p0 varies from 0 to 1, X varies from X_branch_1 to X_branch_0.
# The bistable landscape shifts with X, which changes the basin volumes.

# The BORN RULE prediction: the fraction of outcomes landing in the
# basin associated with branch |0> should equal p0 = |c0|^2.

# How we associate basins with branches:
# When p0 = 1 (pure |0>): X = X_branch_0 = 2.0. The system should be
# near the attractor that corresponds to Phi ~ 2.0.
# When p0 = 0 (pure |1>): X = X_branch_1 = -2.0. System near Phi ~ -2.0.

# For intermediate p0: both attractors exist (if bistable at that X).
# The fraction going to the "branch 0" attractor is what we measure.

c0_sq_values = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
N_ens_born = 400

print(f"\n  X_branch_0 = {X_branch_0}, X_branch_1 = {X_branch_1}")
print(f"  D = {D_Phi}, N_ensemble = {N_ens_born}")
print(f"  Phi starts at 0 (unbiased), Psi starts at 0")
print()
print(f"  {'|c0|^2':>8s} {'X_source':>10s} {'#FPs':>6s} {'frac(0)':>10s} {'Born pred':>10s} {'delta':>8s}")
print(f"  {'-'*8} {'-'*10} {'-'*6} {'-'*10} {'-'*10} {'-'*8}")

born_deltas = []

for c0_sq in c0_sq_values:
    X_source = X_branch_0 * c0_sq + X_branch_1 * (1 - c0_sq)

    # Find attractors at this X
    fps = find_attractors(X_source)
    n_fps = len(fps)

    if n_fps < 2:
        # Only one attractor — no selection possible
        # The system always goes to the single attractor
        # This is the "no bistability" regime
        frac_0 = 1.0 if X_source > 0 else 0.0
        delta = frac_0 - c0_sq
        born_deltas.append(delta)
        print(f"  {c0_sq:8.2f} {X_source:10.3f} {n_fps:6d} {frac_0:10.3f} {c0_sq:10.3f} {delta:+8.3f}  (monostable)")
        continue

    # Two attractors: run ensemble
    Phi_A_val = fps[0][0]
    Phi_B_val = fps[-1][0]
    # Which attractor is "branch 0"?
    # Branch 0 corresponds to X_branch_0 = 2.0 (positive).
    # The attractor with LARGER Phi is the "branch 0" attractor.
    if Phi_A_val > Phi_B_val:
        Phi_0_attractor = Phi_A_val
        Phi_1_attractor = Phi_B_val
    else:
        Phi_0_attractor = Phi_B_val
        Phi_1_attractor = Phi_A_val
    Phi_boundary = (Phi_0_attractor + Phi_1_attractor) / 2

    count_0 = 0
    for trial in range(N_ens_born):
        Phi_f, Psi_f = run_bistable_trial(X_source, D_Phi, D_Psi, seed=trial*13 + int(c0_sq*1000))
        if Phi_f > Phi_boundary:
            count_0 += 1

    frac_0 = count_0 / N_ens_born
    delta = frac_0 - c0_sq
    born_deltas.append(delta)

    print(f"  {c0_sq:8.2f} {X_source:10.3f} {n_fps:6d} {frac_0:10.3f} {c0_sq:10.3f} {delta:+8.3f}")

born_deltas = np.array(born_deltas)
mean_abs_delta = np.mean(np.abs(born_deltas))
max_abs_delta = np.max(np.abs(born_deltas))

print(f"\n  Mean |delta|: {mean_abs_delta:.4f}")
print(f"  Max |delta|:  {max_abs_delta:.4f}")

if mean_abs_delta < 0.05:
    verdict = "BORN RULE EMERGES (mean |delta| < 5%)"
elif mean_abs_delta < 0.10:
    verdict = "BORN RULE APPROXIMATELY EMERGES (mean |delta| < 10%)"
elif mean_abs_delta < 0.20:
    verdict = "PARTIAL BORN RULE (mean |delta| < 20%)"
else:
    verdict = "BORN RULE DOES NOT EMERGE"

print(f"\n  VERDICT: {verdict}")

# ============================================================
# MECHANISM ANALYSIS
# ============================================================
print(f"\n{'='*90}")
print("MECHANISM ANALYSIS")
print("=" * 90)

# How does X_source affect the basin structure?
# As c0_sq increases (more |0>), X_source increases toward X_branch_0.
# This shifts the constitutive landscape, making the "branch 0" basin
# LARGER and the "branch 1" basin SMALLER.
# The Born rule would require: basin_volume(0) / total = |c0|^2.

# Test: plot the attractor positions and basin boundary vs X_source
print(f"\n  Basin structure vs |c0|^2:")
print(f"  {'|c0|^2':>8s} {'X':>8s} {'Phi*_lo':>10s} {'Phi*_hi':>10s} {'boundary':>10s} {'basin_asym':>12s}")

for c0_sq in [0.1, 0.3, 0.5, 0.7, 0.9]:
    X_s = X_branch_0 * c0_sq + X_branch_1 * (1 - c0_sq)
    fps = find_attractors(X_s)
    if len(fps) >= 2:
        lo = min(f[0] for f in fps)
        hi = max(f[0] for f in fps)
        bnd = (lo + hi) / 2
        # Basin asymmetry: how much the boundary shifts relative to Phi_init = 0
        asym = -bnd / (hi - lo) if hi != lo else 0  # positive = favoring high-Phi basin
        print(f"  {c0_sq:8.2f} {X_s:8.2f} {lo:10.4f} {hi:10.4f} {bnd:10.4f} {asym:+12.4f}")
    else:
        print(f"  {c0_sq:8.2f} {X_s:8.2f} {'monostable':>10s}")

# ============================================================
# NOISE-INDEPENDENCE TEST
# ============================================================
print(f"\n{'='*90}")
print("NOISE-INDEPENDENCE TEST")
print("=" * 90)
print(f"\n  Does the basin fraction depend on D (noise amplitude)?")
print(f"  If Born rule is STRUCTURAL: frac(0) should be D-independent.")
print(f"  If it depends on noise details: frac(0) varies with D.")

c0_test = 0.3
X_test = X_branch_0 * c0_test + X_branch_1 * (1 - c0_test)
N_ens_D = 300

print(f"\n  |c0|^2 = {c0_test}, Born prediction = {c0_test}")
print(f"  {'D':>8s} {'frac(0)':>10s} {'delta':>10s}")
print(f"  {'-'*8} {'-'*10} {'-'*10}")

for D_test in [0.05, 0.1, 0.2, 0.5, 1.0, 2.0]:
    fps = find_attractors(X_test)
    if len(fps) < 2:
        print(f"  {D_test:8.2f} {'monostable':>10s}")
        continue
    Phi_hi = max(f[0] for f in fps)
    Phi_lo = min(f[0] for f in fps)
    Phi_bnd = (Phi_hi + Phi_lo) / 2

    count = 0
    for trial in range(N_ens_D):
        Phi_f, _ = run_bistable_trial(X_test, D_test, D_test, seed=trial*31+7)
        if Phi_f > Phi_bnd:
            count += 1
    frac = count / N_ens_D
    print(f"  {D_test:8.2f} {frac:10.3f} {frac - c0_test:+10.3f}")

# ============================================================
# FINAL STRUCTURAL ASSESSMENT
# ============================================================
print(f"\n{'='*90}")
print("FINAL STRUCTURAL ASSESSMENT")
print("=" * 90)

print(f"""
  N2 tested whether bistable constitutive dynamics produces:
  A) Branch instability: YES (two attractors at each X in the bistable range)
  B) Single-outcome stabilization: YES (noise drives Phi into one basin)
  C) |psi|^2 statistics: TESTED ABOVE

  The MECHANISM:
  As |c0|^2 increases, X_source shifts toward X_branch_0.
  This shifts the constitutive landscape:
  - The "branch 0" attractor moves
  - The "branch 1" attractor moves
  - The BASIN BOUNDARY shifts
  The fraction of noise-driven trajectories landing in each basin
  depends on where the basin boundary is RELATIVE TO Phi_init = 0.

  This is a PURELY CONSTITUTIVE mechanism:
  - The quantum amplitudes enter ONLY through X_source = sum c_i^2 X_i
  - The bistability is a property of the constitutive sector
  - The noise is environmental (not quantum)
  - The selection is stochastic (basin selection by noise)

  Whether frac(0) = |c0|^2 depends on whether the basin boundary shift
  is LINEAR in |c0|^2 — which depends on the SPECIFIC nonlinear dynamics
  of the (Phi, Psi) system.
""")

print("=" * 90)
print("END OF COMPUTATION")
print("=" * 90)
