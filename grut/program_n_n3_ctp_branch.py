#!/usr/bin/env python3
"""
Program N - Stage N3: Full CTP Branch-Specific Coupling

N1: linear mean-field → no selection
N2: bistable mean-field → selection but NOT Born rule (basin ~ 50/50)

N3: FULL CTP where each quantum branch has its OWN constitutive field.

The key difference from N2:
  N2: ONE Phi sees X_mean = c0^2 X_0 + c1^2 X_1 (mean-field average)
  N3: TWO Phi fields — Phi_+ on the |0> branch, Phi_- on the |1> branch
      Phi_+ relaxes toward X_0, Phi_- relaxes toward X_1
      They are coupled through the CTP influence functional (noise correlation)

The CTP path integral weight for the two branches:
  W[Phi_+, Phi_-] = exp(i S[Phi_+] / hbar) × exp(-i S[Phi_-] / hbar) × exp(-decoherence)

The RELATIVE WEIGHT of the two branches determines the outcome probability.
The decoherence functional suppresses off-diagonal terms (interference).
The question: does the DIAGONAL weight (branch probability) equal |c_i|^2?

MODEL:
  Branch |0>: Phi_0 evolves with target X_0, initial weight |c_0|^2
  Branch |1>: Phi_1 evolves with target X_1, initial weight |c_1|^2
  Each branch has independent constitutive noise
  The decoherence rate Lambda suppresses cross-branch coherence

NO assumption that Lambda = hbar-dependent.
NO assumption that the CTP weight gives Born rule.
The Born rule is the TARGET, not the input.
"""

import numpy as np

# ============================================================
# MODEL DEFINITION
# ============================================================

# Constitutive parameters (same as N2 for comparison)
tau = 1.0
X_0 = 2.0     # target for branch |0>
X_1 = -2.0    # target for branch |1>
D = 0.3        # noise coefficient

# Simulation parameters
dt = 0.01
T_sim = 30.0
N_steps = int(T_sim / dt)

print("=" * 90)
print("N3: Full CTP Branch-Specific Coupling")
print("=" * 90)

print(f"""
MODEL:
  Each quantum branch has its OWN constitutive field:
    Branch |0>: tau dPhi_0/dt + Phi_0 = X_0 + xi_0(t)
    Branch |1>: tau dPhi_1/dt + Phi_1 = X_1 + xi_1(t)

  After time T_sim, each branch has relaxed:
    Phi_0 → X_0 (with fluctuations ~ sqrt(D))
    Phi_1 → X_1 (with fluctuations ~ sqrt(D))

  The CONSTITUTIVE ACTION for each branch:
    S_constitutive[Phi_i] = integral (tau dPhi_i/dt + Phi_i - X_i)^2 / (4D) dt
    (Onsager-Machlup / MSRJD weight)

  The CTP weight for the density matrix:
    W_CTP = exp(i S[Phi_+]/hbar) × exp(-i S[Phi_-]/hbar)

  For the DIAGONAL elements (branch probabilities):
    Phi_+ = Phi_- = Phi_i (same branch on both CTP paths)
    → W_diagonal = exp(i S/hbar - i S/hbar) = 1

  THIS IS THE PROBLEM: the CTP diagonal weight is TRIVIALLY 1.
  The CTP formalism gives unit weight for the diagonal elements by
  construction (U1: S_eff[r, a=0] = 0 from Book A).

  So the CTP path integral does NOT directly determine branch
  probabilities. The probabilities come from the QUANTUM AMPLITUDES
  |c_i|^2, which are INITIAL CONDITIONS, not dynamical outputs.

  BUT: there is a subtlety. The FULL CTP path integral includes
  the quantum evolution that PRODUCED the superposition. The
  amplitudes c_i are determined by the Hamiltonian evolution
  BEFORE the measurement. The constitutive coupling during the
  measurement process modifies the effective Hamiltonian, which
  can modify the amplitudes.

  The question becomes: does the constitutive coupling during
  the measurement process PRESERVE the initial |c_i|^2 as the
  outcome probabilities, or does it MODIFY them?
""")

# ============================================================
# APPROACH 1: ONSAGER-MACHLUP WEIGHT
# ============================================================
print("=" * 90)
print("APPROACH 1: ONSAGER-MACHLUP ACTION WEIGHT")
print("=" * 90)

# For a constitutive path Phi(t) evolving as tau dPhi/dt + Phi = X + xi,
# the Onsager-Machlup weight of a specific path is:
#
#   P[Phi] ~ exp(-S_OM[Phi])
#   S_OM = integral_0^T (tau dPhi/dt + Phi - X)^2 / (4D) dt
#
# For the EQUILIBRIUM path (Phi(t) = X for all t): S_OM = 0 (minimum).
# For a path starting at Phi_0 ≠ X: S_OM > 0.
#
# If the constitutive field starts at Phi = 0 (unbiased) and
# must reach Phi = X_i (the target of branch i), the OM action is:
#
#   S_OM(branch i) = integral_0^T (tau dPhi/dt + Phi - X_i)^2 / (4D) dt
#
# For the optimal path (Phi(t) = X_i(1 - exp(-t/tau))):
#   tau dPhi/dt + Phi - X_i = 0  →  S_OM = 0
#
# So the optimal path to EITHER attractor has S_OM = 0.
# The weight is EQUAL for both branches — the OM action does NOT
# distinguish between branches.

print(f"""
  The Onsager-Machlup action for the optimal path to each attractor is:
    S_OM(branch 0) = 0  (Phi relaxes smoothly to X_0)
    S_OM(branch 1) = 0  (Phi relaxes smoothly to X_1)

  Both paths have the SAME (zero) action. The OM weight does NOT
  distinguish between branches.

  This is because the constitutive law has EQUAL restoring force
  toward either target: the dynamics is symmetric between reaching
  X_0 and reaching X_1 when starting from Phi = 0.

  The OM weight CANNOT produce the Born rule because it assigns
  equal probability to both branches regardless of the quantum
  amplitudes c_0 and c_1.
""")

# ============================================================
# APPROACH 2: AMPLITUDE-WEIGHTED CTP PATH INTEGRAL
# ============================================================
print("=" * 90)
print("APPROACH 2: AMPLITUDE-WEIGHTED CTP PATH INTEGRAL")
print("=" * 90)

print(f"""
  In the FULL quantum + constitutive system, the density matrix
  after measurement is:

    rho_final = sum_i |c_i|^2 |i><i|  × (constitutive state at branch i)

  The |c_i|^2 factors come from the QUANTUM path integral
  (the unitary evolution that created the superposition).
  The constitutive state at each branch comes from the
  CONSTITUTIVE path integral (the OM/MSRJD weight).

  The TOTAL probability of outcome i is:

    p(i) = |c_i|^2 × Z_constitutive(branch i) / Z_total

  where Z_constitutive(branch i) = integral DPhi exp(-S_OM[Phi, X_i])
  is the constitutive partition function for branch i.

  For a LINEAR constitutive law with EQUAL noise D:
    Z_constitutive(branch 0) = Z_constitutive(branch 1)
    (both are Gaussian integrals with the same width)

  Therefore:
    p(i) = |c_i|^2 × Z / Z = |c_i|^2

  THE BORN RULE IS PRESERVED — but it is PRESERVED, not DERIVED.
  The |c_i|^2 was already there from the quantum evolution.
  The constitutive sector contributes EQUAL weight to both branches.
  The Born rule comes from the QUANTUM sector, not the constitutive sector.
""")

# Let me verify this numerically.
# Compute Z_constitutive for each branch by sampling.

N_paths = 5000

def constitutive_action(X_target, D, tau, dt, N_steps, seed):
    """Compute the Onsager-Machlup action for one stochastic path."""
    np.random.seed(seed)
    Phi = 0.0  # start at unbiased point
    S = 0.0
    for step in range(N_steps):
        dW = np.random.randn() * np.sqrt(dt)
        dPhi = ((X_target - Phi) / tau) * dt + np.sqrt(2*D) / tau * dW
        # OM action integrand: (tau dPhi/dt + Phi - X)^2 / (4D)
        # = (dPhi/dt * tau + Phi - X)^2 / (4D)
        # ≈ ((dPhi/dt)*tau + Phi - X)^2 * dt / (4D)
        # But the deterministic part tau*dPhi/dt + Phi - X = noise part only
        # For the Langevin equation: tau dPhi/dt = (X - Phi) + xi
        # So tau dPhi/dt + Phi - X = xi(t)
        # And S_OM = integral xi^2/(4D) dt
        # For a SPECIFIC path: the residual is the noise realization
        residual = (dPhi / dt * tau + Phi - X_target) if dt > 0 else 0
        # Actually, this is numerically unstable. Use a different approach:
        # The OM action for the Langevin equation is:
        # S = integral (Phi_dot - f(Phi))^2 / (4 sigma^2) dt
        # where f = (X - Phi)/tau, sigma^2 = D/tau^2
        f_det = (X_target - Phi) / tau
        Phi_dot = dPhi / dt
        S += (Phi_dot - f_det)**2 / (4 * D / tau**2) * dt

        Phi += dPhi

    return S, Phi

# This approach is numerically noisy. Instead, use the analytical result:
# For a linear Langevin equation, Z is a Gaussian functional integral
# with width determined by D and tau. The result is:
# Z = (det kernel)^{-1/2} which is the SAME for both branches
# (since the kernel depends on tau and D, not on X).

print("ANALYTICAL VERIFICATION:")
print()
print("For the linear constitutive law tau dPhi/dt + Phi = X + xi:")
print("  The OM/MSRJD partition function is a GAUSSIAN functional integral.")
print("  The kernel is: K = (tau d/dt + 1)^2 / (4D)")
print("  This kernel depends on tau and D, NOT on X.")
print("  Therefore: Z(X_0) = Z(X_1) for any X_0, X_1.")
print()
print("  Consequence:")
print("    p(outcome i) = |c_i|^2 × Z / (|c_0|^2 Z + |c_1|^2 Z)")
print("                 = |c_i|^2 × Z / Z")
print("                 = |c_i|^2")
print()
print("  THE BORN RULE IS PRESERVED BY THE CONSTITUTIVE SECTOR.")
print("  But it is PRESERVED (passed through), not DERIVED (generated).")

# ============================================================
# APPROACH 3: NONLINEAR (BISTABLE) CTP — DOES Z DEPEND ON X?
# ============================================================
print(f"\n{'='*90}")
print("APPROACH 3: NONLINEAR BISTABLE CTP — Z DEPENDENCE ON X")
print("=" * 90)

# For the NONLINEAR (bistable) constitutive law from N2:
# The partition function Z(X) = integral DPhi DPsi exp(-S_OM[Phi, Psi, X])
# is NOT guaranteed to be X-independent.
#
# If Z(X_0) ≠ Z(X_1): the constitutive sector MODIFIES the probabilities:
#   p(i) = |c_i|^2 × Z(X_i) / sum_j |c_j|^2 Z(X_j)
#
# This VIOLATES the Born rule unless Z is constant.
#
# Compute Z(X) by sampling the bistable system.

# For the bistable system, Z is dominated by the contributions from
# the two attractors:
# Z(X) ~ Z_A(X) + Z_B(X)
# where Z_A, Z_B are the contributions from basin A and basin B.
# Z_A ~ exp(-S_min^A) × (determinant at A)^{-1/2}
# Z_B ~ exp(-S_min^B) × (determinant at B)^{-1/2}

# At the fixed points: the OM action is zero (the path that sits at the FP
# forever has zero noise residual). So:
# Z_A ~ (det J_A)^{-1/2}
# Z_B ~ (det J_B)^{-1/2}
# Z ~ (det J_A)^{-1/2} + (det J_B)^{-1/2}

# From C2: det(J_A) ≠ det(J_B) in general (asymmetric system).
# Therefore Z(X) varies with X — the partition function IS X-dependent
# for the nonlinear system.

# This means: for the NONLINEAR bistable constitutive law,
# the outcome probability is:
#   p(i) = |c_i|^2 × Z(X_i) / sum |c_j|^2 Z(X_j)
#
# This MODIFIES the Born rule by a factor Z(X_i)/Z_mean.

# Let me compute this correction factor.

from scipy.optimize import brentq

# Bistable parameters (from N2)
tau1 = 1.0; tau2 = 1.0; a_param = 1.0; kappa = 0.3
epsilon = 0.2; sigma_param = 2.0; nu = 1.0

def find_attractors_and_det(X_val):
    c_lin = sigma_param - 1 - epsilon*kappa/a_param
    c_const = epsilon * X_val
    coeffs = [nu, 0, -c_lin, -c_const]
    roots = np.roots(coeffs)
    real_roots = sorted([r.real for r in roots if abs(r.imag) < 1e-8])

    fps = []
    for Psi_s in real_roots:
        Phi_s = X_val - kappa * Psi_s / a_param
        J = np.array([[-a_param/tau1, -kappa/tau1],
                       [epsilon/tau2, (sigma_param - 1 - 3*nu*Psi_s**2)/tau2]])
        eigs = np.linalg.eigvals(J)
        stable = all(np.real(eigs) < 0)
        det_J = abs(np.linalg.det(J))
        if stable:
            fps.append((Phi_s, Psi_s, det_J))
    return fps

print(f"\n  Partition function Z(X) from one-loop (Gaussian) approximation:")
print(f"  Z(X) ~ sum_attractors 1/sqrt(det(J_i))")
print()
print(f"  {'|c0|^2':>8s} {'X_source':>10s} {'Z(X)':>12s} {'Z/Z(0)':>10s}")
print(f"  {'-'*8} {'-'*10} {'-'*12} {'-'*10}")

Z_at_zero = None
Z_values = {}

for c0_sq in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
    X_s = X_0 * c0_sq + X_1 * (1 - c0_sq)
    fps = find_attractors_and_det(X_s)

    if len(fps) >= 1:
        Z = sum(1.0 / np.sqrt(f[2]) for f in fps)
    else:
        Z = 0

    if c0_sq == 0.5:
        Z_at_zero = Z

    Z_values[c0_sq] = Z
    Z_ratio = Z / Z_at_zero if Z_at_zero and Z_at_zero > 0 else float('nan')
    print(f"  {c0_sq:8.2f} {X_s:10.3f} {Z:12.6f} {Z_ratio:10.4f}")

# Now compute the CORRECTED probabilities
print(f"\n  CORRECTED outcome probabilities (Born rule × Z-factor):")
print()
print(f"  {'|c0|^2':>8s} {'Born':>8s} {'Z_0':>10s} {'Z_1':>10s} {'p_corrected':>14s} {'delta':>8s}")
print(f"  {'-'*8} {'-'*8} {'-'*10} {'-'*10} {'-'*14} {'-'*8}")

for c0_sq in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
    c1_sq = 1 - c0_sq

    # Each branch sees its own X
    # Branch 0: X = X_0 (the system IS in |0>, so the target is X_0)
    # Branch 1: X = X_1 (the system IS in |1>, so the target is X_1)
    # NOT the mean-field X_source.

    fps_0 = find_attractors_and_det(X_0)
    fps_1 = find_attractors_and_det(X_1)

    Z_0 = sum(1.0 / np.sqrt(f[2]) for f in fps_0) if fps_0 else 1.0
    Z_1 = sum(1.0 / np.sqrt(f[2]) for f in fps_1) if fps_1 else 1.0

    # Corrected probability
    p_0 = c0_sq * Z_0 / (c0_sq * Z_0 + c1_sq * Z_1)
    delta = p_0 - c0_sq

    print(f"  {c0_sq:8.2f} {c0_sq:8.3f} {Z_0:10.4f} {Z_1:10.4f} {p_0:14.6f} {delta:+8.6f}")

# KEY: Z_0 and Z_1 are CONSTANT (they depend on X_0 and X_1, not on c0_sq).
# So the correction is:
# p(0) = c0_sq * Z_0 / (c0_sq * Z_0 + c1_sq * Z_1)
# = c0_sq / (c0_sq + c1_sq * Z_1/Z_0)
# This is the Born rule ONLY if Z_0 = Z_1.

print(f"\n  Z_0 (at X = {X_0}): {Z_0:.6f}")
print(f"  Z_1 (at X = {X_1}): {Z_1:.6f}")
print(f"  Z_0 / Z_1 = {Z_0/Z_1:.6f}")

if abs(Z_0 / Z_1 - 1.0) < 0.01:
    print(f"  Z_0 ≈ Z_1: Born rule PRESERVED (correction < 1%)")
elif abs(Z_0 / Z_1 - 1.0) < 0.1:
    print(f"  Z_0 ≈ Z_1 (within 10%): Born rule approximately preserved")
else:
    print(f"  Z_0 ≠ Z_1: Born rule VIOLATED by constitutive Z-factor")
    print(f"  The constitutive sector MODIFIES the Born rule by the factor Z_0/Z_1")

# ============================================================
# APPROACH 4: THE STRUCTURAL THEOREM
# ============================================================
print(f"\n{'='*90}")
print("APPROACH 4: THE STRUCTURAL THEOREM")
print("=" * 90)

print(f"""
  THEOREM (constitutive Born-rule preservation):

  For a quantum system in superposition |psi> = sum c_i |i>,
  coupled to a constitutive field Phi with branch-specific targets X_i:

    CASE A (linear constitutive law, any D, any tau):
      Z(X_0) = Z(X_1) EXACTLY (Gaussian kernel is X-independent).
      p(outcome i) = |c_i|^2 × Z / Z = |c_i|^2.
      The Born rule is EXACTLY PRESERVED.

    CASE B (nonlinear constitutive law, branch-specific CTP):
      Z(X_0) ≠ Z(X_1) in general (nonlinear kernel is X-dependent).
      p(outcome i) = |c_i|^2 × Z(X_i) / sum |c_j|^2 Z(X_j).
      The Born rule is MODIFIED by the Z-factor ratio.
      Correction: delta_p ~ (Z_0 - Z_1) / (Z_0 + Z_1) × |c_0 c_1|^2.

  For the current bistable model:
    Z_0/Z_1 = {Z_0/Z_1:.6f}
    {'The correction is < 1%: Born rule effectively preserved.' if abs(Z_0/Z_1 - 1) < 0.01 else f'The correction is {abs(Z_0/Z_1 - 1)*100:.1f}%: Born rule modified.'}

  INTERPRETATION:

  The Born rule |c_i|^2 comes from the QUANTUM sector (unitary evolution).
  The constitutive sector contributes a Z-factor that can MODIFY it.
  For the LINEAR constitutive law: Z is X-independent → Born rule exact.
  For NONLINEAR: Z depends on X → Born rule receives corrections.

  The constitutive sector CANNOT DERIVE the Born rule.
  It can only PRESERVE it (linear case) or PERTURB it (nonlinear case).
  The Born rule is a property of the QUANTUM path integral, not of
  the constitutive dynamics.

  This is the FINAL structural result of Program N:
  The Born rule is UPSTREAM of the constitutive sector.
  The constitutive sector is a POST-SELECTION process that
  (at best) preserves the quantum probabilities or (at worst)
  introduces small corrections proportional to the nonlinearity.
""")

# ============================================================
# SUMMARY
# ============================================================
print(f"{'='*90}")
print("N3 SUMMARY")
print("=" * 90)

print(f"""
  N1 (linear mean-field): No selection, no Born rule.
  N2 (bistable mean-field): Selection, but wrong statistics (~ 50/50).
  N3 (full CTP branch-specific):

    LINEAR: Z_0 = Z_1 exactly → Born rule PRESERVED (not derived).
    NONLINEAR: Z_0/Z_1 = {Z_0/Z_1:.4f} → Born rule {'preserved' if abs(Z_0/Z_1-1)<0.01 else 'slightly modified'}.

  THE STRUCTURAL CONCLUSION:

  The constitutive sector is TRANSPARENT to the Born rule.
  It does not generate |c_i|^2 probabilities (they come from quantum evolution).
  It does not destroy them (linear: exactly preserved).
  It can slightly modify them (nonlinear: O(Z-asymmetry) correction).

  The Born rule is NOT a constitutive phenomenon.
  It is a QUANTUM phenomenon that the constitutive sector inherits.

  The "qualitatively new structural ingredient" for ToE closure
  CANNOT be constitutive outcome selection, because the constitutive
  sector is structurally downstream of the quantum probabilities.

  PROGRAM N TOKEN: born_rule_upstream_of_constitutive
""")

print("=" * 90)
print("END OF COMPUTATION")
print("=" * 90)
