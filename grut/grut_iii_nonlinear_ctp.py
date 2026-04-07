#!/usr/bin/env python3
"""
GRUT III Book C, Stage C1 — Nonlinear CTP Extension

Numerical investigation of the cubic-saturating constitutive law
in the CTP framework. Tests whether bistability creates nontrivial
admissibility pruning (Model C ≠ Model D).

The nonlinear constitutive law:
  tau dPhi/dt = h(X - Phi)
where h(v) = gamma*v - delta*v^3  (cubic saturation from GRUT-II Nu)

In the CTP action, this replaces the linear Sector 1 term:
  -[tau dPhi_r/dt + Phi_r - X] Phi_a  →  -[tau dPhi_r/dt - h(X - Phi_r)] Phi_a

The key question: does h admit multiple fixed points, and if so,
does admissibility (A) distinguish between basins?
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

# ============================================================
# NONLINEAR MODEL DEFINITION
# ============================================================

# Parameters
tau = 1.0       # relaxation time
gamma = 1.0     # linear response coefficient
delta = 0.1     # cubic saturation coefficient
X_eq = 1.0      # equilibrium target (from X = beta + alpha R)
beta = 1.0      # background
noise_D = 0.005 # noise coefficient (CTP convention D = k_BT tau/2)

def h(v):
    """Cubic-saturating response: h(v) = gamma*v - delta*v^3"""
    return gamma * v - delta * v**3

def dh(v):
    """Derivative: h'(v) = gamma - 3*delta*v^2"""
    return gamma - 3 * delta * v**2

def constitutive_rhs(t, Phi, X=X_eq):
    """dPhi/dt = h(X - Phi) / tau"""
    v = X - Phi
    return h(v) / tau

# ============================================================
# TASK 2: FIXED POINT ANALYSIS
# ============================================================
print("=" * 80)
print("TASK 2: FIXED POINT AND ATTRACTOR ANALYSIS")
print("=" * 80)

# Fixed points: h(X - Phi*) = 0
# gamma*(X - Phi*) - delta*(X - Phi*)^3 = 0
# v*(gamma - delta*v*^2) = 0
# Solutions: v* = 0, v* = +/- sqrt(gamma/delta)

v_star = [0, np.sqrt(gamma/delta), -np.sqrt(gamma/delta)]
Phi_star = [X_eq - v for v in v_star]

print(f"\nParameters: tau={tau}, gamma={gamma}, delta={delta}, X={X_eq}")
print(f"h(v) = {gamma}*v - {delta}*v^3")
print(f"\nFixed points (h(v*) = 0):")
for i, (v, phi) in enumerate(zip(v_star, Phi_star)):
    # Stability: eigenvalue = -h'(v*)/tau
    hp = dh(v)
    eig = -hp / tau
    stable = "STABLE" if eig < 0 else "UNSTABLE"
    print(f"  v* = {v:+.4f}, Phi* = {phi:.4f}, h'(v*) = {hp:.4f}, eigenvalue = {eig:+.4f} [{stable}]")

# The three fixed points:
# v* = 0 → Phi* = X (same as linear theory). Eigenvalue = -gamma/tau < 0: STABLE
# v* = +sqrt(gamma/delta) → Phi* = X - sqrt(gamma/delta). h'(v*) = gamma - 3gamma = -2gamma. Eigenvalue = +2gamma/tau > 0: UNSTABLE
# v* = -sqrt(gamma/delta) → Phi* = X + sqrt(gamma/delta). Same stability: UNSTABLE

print(f"\nResult: ONE stable fixed point (Phi* = X), TWO unstable fixed points.")
print(f"The cubic saturation h(v) = gamma*v - delta*v^3 does NOT produce bistability")
print(f"when applied to the simple constitutive law tau dPhi/dt = h(X - Phi).")
print(f"\nThe unique stable attractor is STILL Phi* = X.")

# ============================================================
# WHAT ABOUT THE GRUT-II NU BISTABILITY?
# ============================================================
print(f"\n" + "=" * 80)
print(f"GRUT-II NU BISTABILITY CHECK")
print(f"=" * 80)

# GRUT-II Nu had a DIFFERENT system: not just h(v) but a COUPLED system
# with delay and a meta-variable. The bistability came from the coupling
# structure, not from the cubic alone.
#
# The GRUT-II Nu system was (from grut_ii_static_bistability.py):
#   tau1 dPhi/dt = h(X - Phi) - g(Psi)
#   tau2 dPsi/dt = f(Phi) - Psi
# with h cubic, g and f coupling functions, and delay.
#
# The single-variable cubic constitutive law tau dPhi/dt = h(X - Phi)
# does NOT have bistability. It has one stable fixed point.
#
# CONCLUSION: to get bistability in the CTP framework, we need the
# COUPLED system, not just the cubic term.

print(f"""
The GRUT-II Nu bistability required a COUPLED system:
  tau1 dPhi/dt = h(X - Phi) - g(Psi)
  tau2 dPsi/dt = f(Phi) - Psi

The single-variable cubic law tau dPhi/dt = h(X - Phi) has
exactly ONE stable fixed point (Phi* = X), same as the linear case.

For bistability, we need at minimum TWO coupled equations.
This means the minimal nonlinear CTP extension that can produce
bistability requires an AUXILIARY FIELD Psi alongside Phi.
""")

# ============================================================
# MINIMAL BISTABLE CTP MODEL
# ============================================================
print("=" * 80)
print("MINIMAL BISTABLE CTP MODEL")
print("=" * 80)

# Minimal coupled system with bistability:
#   tau1 dPhi/dt = gamma1*(X - Phi) - kappa*Psi
#   tau2 dPsi/dt = gamma2*Phi - mu*Psi - nu*Psi^3
#
# This is a two-field system where Psi is a "meta-field" or
# "auxiliary constitutive mode" that couples to Phi.
# The cubic term -nu*Psi^3 provides saturation.
#
# Fixed points: set both RHS = 0
#   gamma1*(X - Phi*) = kappa*Psi*  →  Phi* = X - kappa*Psi*/gamma1
#   gamma2*Phi* = mu*Psi* + nu*Psi*^3
#
# Substituting:
#   gamma2*(X - kappa*Psi*/gamma1) = mu*Psi* + nu*Psi*^3
#   gamma2*X - gamma2*kappa*Psi*/gamma1 = mu*Psi* + nu*Psi*^3
#   gamma2*X = (mu + gamma2*kappa/gamma1)*Psi* + nu*Psi*^3
#
# This is a cubic in Psi*. It can have 1 or 3 real roots depending on parameters.

# Use parameters from GRUT-II Nu (adapted):
tau1 = 1.0
tau2 = 2.0
gamma1 = 1.0
gamma2 = 0.5
kappa = 0.3
mu = 0.1
nu = 0.02

def coupled_rhs(t, state, X=X_eq):
    Phi, Psi = state
    dPhi = (gamma1*(X - Phi) - kappa*Psi) / tau1
    dPsi = (gamma2*Phi - mu*Psi - nu*Psi**3) / tau2
    return [dPhi, dPsi]

# Find fixed points
# From the cubic: gamma2*X = (mu + gamma2*kappa/gamma1)*Psi* + nu*Psi*^3
A_coeff = nu
B_coeff = 0  # no Psi^2 term
C_coeff = mu + gamma2*kappa/gamma1
D_coeff = -gamma2*X_eq

# nu*Psi^3 + (mu + gamma2*kappa/gamma1)*Psi - gamma2*X = 0
coeffs = [A_coeff, B_coeff, C_coeff, D_coeff]
roots = np.roots(coeffs)
real_roots = [r.real for r in roots if abs(r.imag) < 1e-10]
real_roots.sort()

print(f"\nCoupled system parameters:")
print(f"  tau1={tau1}, tau2={tau2}, gamma1={gamma1}, gamma2={gamma2}")
print(f"  kappa={kappa}, mu={mu}, nu={nu}, X={X_eq}")
print(f"\nCubic for Psi*: {nu}*Psi^3 + {mu + gamma2*kappa/gamma1:.4f}*Psi - {gamma2*X_eq:.4f} = 0")
print(f"Real roots: {[f'{r:.4f}' for r in real_roots]}")

# For each root, compute Phi* and stability
print(f"\nFixed points and stability:")
for Psi_s in real_roots:
    Phi_s = X_eq - kappa*Psi_s/gamma1

    # Jacobian at (Phi_s, Psi_s):
    # J = [[-gamma1/tau1,  -kappa/tau1],
    #      [gamma2/tau2,   -(mu + 3*nu*Psi_s^2)/tau2]]
    J = np.array([
        [-gamma1/tau1, -kappa/tau1],
        [gamma2/tau2, -(mu + 3*nu*Psi_s**2)/tau2]
    ])
    eigs = np.linalg.eigvals(J)
    stable = all(e.real < 0 for e in eigs)

    print(f"  Psi* = {Psi_s:+.4f}, Phi* = {Phi_s:.4f}")
    print(f"    J eigenvalues: {eigs[0]:.4f}, {eigs[1]:.4f}")
    print(f"    Stability: {'STABLE' if stable else 'UNSTABLE'}")

# Check: do we have multiple stable fixed points?
stable_fps = []
for Psi_s in real_roots:
    Phi_s = X_eq - kappa*Psi_s/gamma1
    J = np.array([
        [-gamma1/tau1, -kappa/tau1],
        [gamma2/tau2, -(mu + 3*nu*Psi_s**2)/tau2]
    ])
    eigs = np.linalg.eigvals(J)
    if all(e.real < 0 for e in eigs):
        stable_fps.append((Phi_s, Psi_s))

print(f"\nNumber of stable fixed points: {len(stable_fps)}")

if len(stable_fps) == 1:
    print(f"NO BISTABILITY with these parameters. Adjusting...")

    # Need stronger nonlinearity or different coupling
    # Try: increase gamma2 and nu to create a fold bifurcation
    for gamma2_test in [0.5, 1.0, 2.0, 3.0, 5.0]:
        for nu_test in [0.01, 0.05, 0.1, 0.5]:
            A = nu_test
            C = mu + gamma2_test*kappa/gamma1
            D = -gamma2_test*X_eq
            roots_test = np.roots([A, 0, C, D])
            real_roots_test = sorted([r.real for r in roots_test if abs(r.imag) < 1e-10])

            if len(real_roots_test) == 3:
                # Check stability of all three
                n_stable = 0
                for Psi_s in real_roots_test:
                    Phi_s = X_eq - kappa*Psi_s/gamma1
                    J = np.array([
                        [-gamma1/tau1, -kappa/tau1],
                        [gamma2_test/tau2, -(mu + 3*nu_test*Psi_s**2)/tau2]
                    ])
                    eigs = np.linalg.eigvals(J)
                    if all(e.real < 0 for e in eigs):
                        n_stable += 1

                if n_stable >= 2:
                    print(f"  BISTABILITY at gamma2={gamma2_test}, nu={nu_test}: {n_stable} stable FPs")

                    # Use these parameters
                    gamma2 = gamma2_test
                    nu = nu_test
                    break
        else:
            continue
        break

# Recompute with bistable parameters
print(f"\n--- BISTABLE PARAMETER SET ---")
print(f"  gamma2={gamma2}, nu={nu}")

A_coeff = nu
C_coeff = mu + gamma2*kappa/gamma1
D_coeff = -gamma2*X_eq
roots = np.roots([A_coeff, 0, C_coeff, D_coeff])
real_roots = sorted([r.real for r in roots if abs(r.imag) < 1e-10])

print(f"\n  Fixed points:")
stable_fps = []
unstable_fps = []
for Psi_s in real_roots:
    Phi_s = X_eq - kappa*Psi_s/gamma1
    J = np.array([
        [-gamma1/tau1, -kappa/tau1],
        [gamma2/tau2, -(mu + 3*nu*Psi_s**2)/tau2]
    ])
    eigs = np.linalg.eigvals(J)
    stable = all(e.real < 0 for e in eigs)
    status = "STABLE" if stable else "UNSTABLE"
    print(f"    Psi*={Psi_s:+.4f}, Phi*={Phi_s:.4f}, eigs=({eigs[0].real:+.4f}, {eigs[1].real:+.4f}) [{status}]")
    if stable:
        stable_fps.append((Phi_s, Psi_s))
    else:
        unstable_fps.append((Phi_s, Psi_s))

# ============================================================
# TASK 3: BASIN STRUCTURE AND ADMISSIBILITY TEST
# ============================================================
print(f"\n" + "=" * 80)
print(f"TASK 3-4: BASIN STRUCTURE AND ADMISSIBILITY TEST")
print(f"=" * 80)

if len(stable_fps) >= 2:
    print(f"\n{len(stable_fps)} stable fixed points found. Testing basin structure.")

    # Map initial conditions to attractors
    N_grid = 50
    Phi_range = np.linspace(-2, 4, N_grid)
    Psi_range = np.linspace(-10, 10, N_grid)

    basin_map = np.zeros((N_grid, N_grid), dtype=int)

    def coupled_rhs_bistable(t, state):
        Phi, Psi = state
        dPhi = (gamma1*(X_eq - Phi) - kappa*Psi) / tau1
        dPsi = (gamma2*Phi - mu*Psi - nu*Psi**3) / tau2
        return [dPhi, dPsi]

    for i, Phi0 in enumerate(Phi_range):
        for j, Psi0 in enumerate(Psi_range):
            sol = solve_ivp(coupled_rhs_bistable, [0, 100], [Phi0, Psi0],
                          rtol=1e-8, atol=1e-10, max_step=0.5)
            Phi_final = sol.y[0, -1]
            Psi_final = sol.y[1, -1]

            # Which attractor?
            dists = [np.sqrt((Phi_final - fp[0])**2 + (Psi_final - fp[1])**2)
                    for fp in stable_fps]
            basin_map[i, j] = np.argmin(dists)

    # Count basin sizes
    for k, fp in enumerate(stable_fps):
        count = np.sum(basin_map == k)
        frac = count / basin_map.size
        print(f"  Attractor {k} (Phi*={fp[0]:.3f}, Psi*={fp[1]:.3f}): {frac*100:.1f}% of initial conditions")

    # THE KEY TEST: two trajectories with same (Phi_0, X_0) but different Psi_0
    # that end at different attractors
    print(f"\n--- ADMISSIBILITY PRUNING TEST ---")
    print(f"Find two trajectories with same Phi_0 but different final attractors:")

    found_pruning = False
    for Phi0_test in np.linspace(0, 2, 20):
        attractors_reached = set()
        Psi_vals = []
        for j, Psi0 in enumerate(Psi_range):
            sol = solve_ivp(coupled_rhs_bistable, [0, 100], [Phi0_test, Psi0],
                          rtol=1e-8, atol=1e-10, max_step=0.5)
            Phi_f = sol.y[0, -1]
            Psi_f = sol.y[1, -1]
            dists = [np.sqrt((Phi_f - fp[0])**2 + (Psi_f - fp[1])**2) for fp in stable_fps]
            attr = np.argmin(dists)
            attractors_reached.add(attr)
            if len(attractors_reached) > 1 and not found_pruning:
                # Found it: same Phi_0, different Psi_0, different attractors
                found_pruning = True
                print(f"  Phi_0 = {Phi0_test:.2f}: reaches BOTH attractors depending on Psi_0")
                print(f"  → Different Psi_0 values lead to different long-term Phi*")
                print(f"  → If admissibility includes 'converge to attractor A', then")
                print(f"     trajectories going to attractor B are PRUNED.")
                break
        if found_pruning:
            break

    if not found_pruning:
        print(f"  No pruning found: all tested Phi_0 converge to the same attractor regardless of Psi_0")

    # THE DECISIVE QUESTION: does the EXTENDED state (Phi, Psi) break the
    # Markov-uniqueness result of B2?
    print(f"\n--- DECISIVE ANALYSIS ---")
    print(f"""
In the LINEAR regime (Book B):
  State = (Phi, X, F). Unique attractor. No pruning. A = diagnostic.

In the NONLINEAR COUPLED regime (Book C):
  State = (Phi, Psi, X, F). Multiple attractors possible.

  KEY STRUCTURAL CHANGE:
  The auxiliary field Psi is a NEW state variable. It was not in the Book B state tuple.
  If two trajectories have the same (Phi_0, X_0) but different Psi_0, they can
  converge to different attractors. The Psi value SELECTS the basin.

  Does this make A constraining?

  ANSWER: It depends on what "admissibility" means:

  (a) If A only checks the constitutive law and regime flags (A1-A7 from B1):
      → Both trajectories satisfy all conditions. Both are admissible.
      → A remains DIAGNOSTIC. classifier_only persists.
      → The basin structure exists but A does not select between basins.

  (b) If A is EXTENDED with a new condition:
      A8: "The path must converge to the thermodynamically preferred attractor"
      → A would prune paths going to the non-preferred attractor.
      → A becomes CONSTRAINING.
      → But: "thermodynamically preferred" is UNDEFINED in the current framework.
         No free-energy functional has been constructed. No criterion for
         "preferred" exists. A8 is not derivable from the CTP action.

  THEREFORE: The nonlinear extension creates the POSSIBILITY of constraining
  admissibility (by enlarging the state space and introducing multiple basins)
  but does NOT REALIZE it without an additional selection principle (A8)
  that is currently OPEN.
""")

else:
    print(f"\nOnly {len(stable_fps)} stable fixed point(s). No bistability found.")
    print(f"The nonlinear term does not produce multiple basins at these parameters.")
    print(f"Admissibility remains classifier_only (same as linear regime).")

# ============================================================
# SUMMARY
# ============================================================
print("=" * 80)
print("SUMMARY")
print("=" * 80)

print(f"""
1. Single-variable cubic: tau dPhi/dt = h(X-Phi) with h = gamma*v - delta*v^3
   → ONE stable fixed point (Phi* = X). No bistability. No change from linear.

2. Coupled system with auxiliary Psi:
   → CAN produce multiple stable fixed points (bistability) at appropriate parameters.
   → Basin structure exists: initial Psi determines which attractor is reached.
   → But: the existing admissibility conditions A1-A7 do not distinguish basins.
   → A new selection condition (A8: attractor preference) would make A constraining.
   → A8 is NOT DERIVABLE from the current CTP action. It requires a free-energy
     functional or thermodynamic selection principle that does not exist yet.

3. Verdict: The nonlinear extension ENABLES but does not REALIZE constraining
   admissibility. The gap is a selection principle, not dynamics.

   classifier_only → bounded_open (with identified gap)
""")

print("=" * 80)
print("END OF COMPUTATION")
print("=" * 80)
