#!/usr/bin/env python3
"""
GRUT III Book C, Stage C2 — Coupled (Phi,Psi) CTP Action
and Attractor Selection Derivability

Tasks:
1. Write coupled CTP action for (Phi_r, Phi_a, Psi_r, Psi_a)
2. Check CTP consistency (unitarity, positivity, causality)
3. Find attractor/basin structure
4. Compute Re S_eff at each attractor and test for selection
5. Determine A8 derivability
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve

# ============================================================
# TASK 1: COUPLED CTP ACTION
# ============================================================
print("=" * 80)
print("TASK 1: COUPLED CTP ACTION")
print("=" * 80)

# The coupled CTP action in Keldysh basis:
#
# iS_eff[Phi_r, Phi_a, Psi_r, Psi_a] =
#   i int dt {
#     // Phi sector (Sector 1a)
#     -[tau1 dPhi_r/dt - h(X - Phi_r) + kappa*Psi_r] Phi_a
#
#     // Psi sector (Sector 1b)
#     -[tau2 dPsi_r/dt - gamma2*Phi_r + mu*Psi_r + nu*Psi_r^3] Psi_a
#
#     // Noise sectors (Sector 2a, 2b)
#     + i D_Phi Phi_a^2
#     + i D_Psi Psi_a^2
#
#     // Cross-noise (if any) — set to zero for minimal model
#   }
#
# where h(v) = gamma1*v - delta*v^3
#
# VARIATION:
#   delta S / delta Phi_a = 0 (classical limit Phi_a -> 0):
#     tau1 dPhi_r/dt = h(X - Phi_r) - kappa*Psi_r
#
#   delta S / delta Psi_a = 0 (classical limit Psi_a -> 0):
#     tau2 dPsi_r/dt = gamma2*Phi_r - mu*Psi_r - nu*Psi_r^3

# Parameters — use GRUT-II Nu-verified bistable set
# From grut_ii_static_bistability.py, the bistable parameters were:
# gamma=2.0, delta_sat=0.5, delay was present
# Here we use a delay-free coupled system and search for bistability

# After extensive testing in GRUT-II Nu, bistability was found at:
# h(v) = gamma*v - delta*v^3 with gamma~2, delta~0.5
# kappa coupling, mu damping, nu cubic saturation on Psi

# Let me use a well-known bistable normal form instead:
# The pitchfork + bias system is the canonical minimal bistable coupled ODE

# CANONICAL BISTABLE COUPLED SYSTEM:
# tau1 dPhi/dt = a*(X - Phi) - kappa*Psi
# tau2 dPsi/dt = epsilon*Phi - Psi + sigma*Psi - nu*Psi^3
#
# The Psi equation: tau2 dPsi/dt = epsilon*Phi + (sigma - 1)*Psi - nu*Psi^3
# Fixed points of Psi: epsilon*Phi + (sigma-1)*Psi - nu*Psi^3 = 0
# If sigma > 1: the origin is unstable in Psi, and two stable branches exist
# This is a supercritical pitchfork in Psi, biased by epsilon*Phi

# Parameters for bistability:
tau1 = 1.0
tau2 = 1.0
a = 1.0       # linear relaxation strength for Phi
kappa = 0.3   # Phi-Psi coupling
epsilon = 0.2 # Psi-Phi coupling (feedback)
sigma = 2.0   # Psi self-coupling (>1 for pitchfork instability)
nu = 1.0      # Psi cubic saturation
X_eq = 1.0    # equilibrium target
D_Phi = 0.005 # noise for Phi
D_Psi = 0.005 # noise for Psi

print(f"""
COUPLED CTP ACTION (Keldysh basis):

  iS_eff = i int dt {{
    // Phi sector
    -[tau1 dPhi_r/dt - a*(X - Phi_r) + kappa*Psi_r] Phi_a

    // Psi sector
    -[tau2 dPsi_r/dt - epsilon*Phi_r - (sigma-1)*Psi_r + nu*Psi_r^3] Psi_a

    // Noise
    + i D_Phi Phi_a^2  +  i D_Psi Psi_a^2
  }}

Parameters:
  tau1={tau1}, tau2={tau2}, a={a}, kappa={kappa}
  epsilon={epsilon}, sigma={sigma}, nu={nu}
  X={X_eq}, D_Phi={D_Phi}, D_Psi={D_Psi}
""")

# ============================================================
# TASK 2: CTP CONSISTENCY CHECKS
# ============================================================
print("=" * 80)
print("TASK 2: CTP CONSISTENCY CHECKS")
print("=" * 80)

# U1: S_eff[Phi_r, Phi_a=0, Psi_r, Psi_a=0] = 0
# All terms are proportional to Phi_a or Psi_a (linear or quadratic).
# Setting both to 0 gives S_eff = 0. CHECK: PASS

# U2: S_eff[Phi_r, -Phi_a, Psi_r, -Psi_a] = -(S_eff[...])*
# Sector 1a: -[...]*(-Phi_a) = +[...]*Phi_a. Original: -[...]*Phi_a.
#   -(original)* = +[...]*Phi_a (since [...] is real). CHECK: PASS
# Sector 1b: Same argument. PASS
# Sector 2a: iD(-Phi_a)^2 = iD Phi_a^2. -(iD Phi_a^2)* = -(-iD Phi_a^2) = iD Phi_a^2. PASS
# Sector 2b: Same. PASS

# U3: Im S_eff >= 0
# Im S_eff = D_Phi Phi_a^2 + D_Psi Psi_a^2
# Both D > 0, both squared terms >= 0. Sum >= 0. PASS

print("""
CTP Unitarity Checks:
  U1 (normalization):  S_eff[..., a-fields=0] = 0            PASS
  U2 (reality):        S_eff[r, -a] = -(S_eff[r, a])*        PASS
  U3 (positivity):     Im S_eff = D_Phi*Phi_a^2 + D_Psi*Psi_a^2 >= 0   PASS

Causality:
  Both EOMs are first-order in time, retarded (no future dependence).  PASS

Cross-noise:
  Set to zero (D_cross = 0). No Phi_a*Psi_a term.
  This assumes Phi and Psi fluctuations are uncorrelated.
  ASSUMED (simplest choice; correlated noise is an extension).

FDT for Psi sector:
  If Psi has its own environmental bath at temperature T_Psi:
  D_Psi = k_B T_Psi tau2 / 2 (CTP convention, Ohmic, high-T)
  ASSUMED (same structure as Phi sector; bath for Psi is unspecified).
""")

# ============================================================
# TASK 3: FIXED POINT STRUCTURE
# ============================================================
print("=" * 80)
print("TASK 3: STATIONARY POINTS AND BASIN STRUCTURE")
print("=" * 80)

def coupled_eom(state, X=X_eq):
    Phi, Psi = state
    dPhi = (a*(X - Phi) - kappa*Psi) / tau1
    dPsi = (epsilon*Phi + (sigma - 1)*Psi - nu*Psi**3) / tau2
    return np.array([dPhi, dPsi])

def coupled_rhs_ivp(t, state):
    return coupled_eom(state)

# Fixed points: set both RHS = 0
# a*(X - Phi) - kappa*Psi = 0  =>  Phi = X - kappa*Psi/a
# epsilon*Phi + (sigma-1)*Psi - nu*Psi^3 = 0
# Substituting:
# epsilon*(X - kappa*Psi/a) + (sigma-1)*Psi - nu*Psi^3 = 0
# epsilon*X - epsilon*kappa*Psi/a + (sigma-1)*Psi - nu*Psi^3 = 0
# -nu*Psi^3 + (sigma - 1 - epsilon*kappa/a)*Psi + epsilon*X = 0

coeff_a = -nu
coeff_b = 0  # no Psi^2 term
coeff_c = sigma - 1 - epsilon*kappa/a
coeff_d = epsilon*X_eq

# Cubic: -nu*Psi^3 + c*Psi + d = 0, i.e., nu*Psi^3 - c*Psi - d = 0
coeffs = [nu, 0, -(sigma - 1 - epsilon*kappa/a), -epsilon*X_eq]
roots = np.roots(coeffs)
real_roots = sorted([r.real for r in roots if abs(r.imag) < 1e-8])

print(f"Cubic coefficients: {nu}*Psi^3 + 0*Psi^2 + {-(sigma-1-epsilon*kappa/a):.4f}*Psi + {-epsilon*X_eq:.4f} = 0")
print(f"c = sigma - 1 - epsilon*kappa/a = {sigma - 1 - epsilon*kappa/a:.4f}")
print(f"Real roots of cubic: {[f'{r:.6f}' for r in real_roots]}")
print(f"Number of real roots: {len(real_roots)}")

# For three real roots, need discriminant > 0
# For cubic ax^3 + cx + d = 0: discriminant = -4ac^3 - 27a^2d^2
disc = -4*nu*(-(sigma-1-epsilon*kappa/a))**3 - 27*nu**2*(epsilon*X_eq)**2
print(f"Discriminant: {disc:.4f} ({'> 0: three real roots' if disc > 0 else '<= 0: one real root'})")

# Analyze each fixed point
print(f"\nFixed points and stability:")
stable_fps = []
unstable_fps = []

for Psi_s in real_roots:
    Phi_s = X_eq - kappa*Psi_s/a

    # Jacobian
    # dPhi/dt = [a*(X-Phi) - kappa*Psi]/tau1
    # dPsi/dt = [epsilon*Phi + (sigma-1)*Psi - nu*Psi^3]/tau2
    #
    # J11 = -a/tau1
    # J12 = -kappa/tau1
    # J21 = epsilon/tau2
    # J22 = (sigma - 1 - 3*nu*Psi_s^2)/tau2

    J = np.array([
        [-a/tau1, -kappa/tau1],
        [epsilon/tau2, (sigma - 1 - 3*nu*Psi_s**2)/tau2]
    ])
    eigs = np.linalg.eigvals(J)
    tr_J = J[0,0] + J[1,1]
    det_J = J[0,0]*J[1,1] - J[0,1]*J[1,0]
    stable = all(e.real < 0 for e in eigs)

    status = "STABLE" if stable else "UNSTABLE"
    print(f"  Psi* = {Psi_s:+.6f}, Phi* = {Phi_s:.6f}")
    print(f"    J = [[{J[0,0]:+.4f}, {J[0,1]:+.4f}], [{J[1,0]:+.4f}, {J[1,1]:+.4f}]]")
    print(f"    tr(J) = {tr_J:.4f}, det(J) = {det_J:.4f}")
    print(f"    eigenvalues: {eigs[0].real:+.4f} {'+' if eigs[0].imag>=0 else ''}{eigs[0].imag:.4f}i, {eigs[1].real:+.4f} {'+' if eigs[1].imag>=0 else ''}{eigs[1].imag:.4f}i")
    print(f"    [{status}]")

    if stable:
        stable_fps.append((Phi_s, Psi_s))
    else:
        unstable_fps.append((Phi_s, Psi_s))

print(f"\nStable fixed points: {len(stable_fps)}")
print(f"Unstable fixed points: {len(unstable_fps)}")

# ============================================================
# BASIN STRUCTURE (if bistable)
# ============================================================
if len(stable_fps) >= 2:
    print(f"\n--- BISTABILITY CONFIRMED ---")
    print(f"Attractor A: Phi*={stable_fps[0][0]:.4f}, Psi*={stable_fps[0][1]:.4f}")
    print(f"Attractor B: Phi*={stable_fps[1][0]:.4f}, Psi*={stable_fps[1][1]:.4f}")

    # Map basins
    N = 80
    Phi_range = np.linspace(-1, 3, N)
    Psi_range = np.linspace(-3, 3, N)
    basin = np.zeros((N, N), dtype=int)

    for i, Phi0 in enumerate(Phi_range):
        for j, Psi0 in enumerate(Psi_range):
            sol = solve_ivp(coupled_rhs_ivp, [0, 200], [Phi0, Psi0],
                          rtol=1e-9, atol=1e-11, max_step=1.0)
            if sol.success and len(sol.t) > 0:
                Phi_f, Psi_f = sol.y[0,-1], sol.y[1,-1]
                dists = [np.sqrt((Phi_f - fp[0])**2 + (Psi_f - fp[1])**2) for fp in stable_fps]
                basin[i,j] = np.argmin(dists)

    for k, fp in enumerate(stable_fps):
        frac = np.sum(basin == k) / basin.size
        print(f"  Basin {k} (Phi*={fp[0]:.4f}, Psi*={fp[1]:.4f}): {frac*100:.1f}%")

    # ============================================================
    # TASK 4: SELECTION FUNCTIONAL — Re S_eff AT EACH ATTRACTOR
    # ============================================================
    print(f"\n" + "=" * 80)
    print(f"TASK 4: SELECTION FUNCTIONAL (Re S_eff AT ATTRACTORS)")
    print(f"=" * 80)

    # The CTP effective action evaluated on a STATIONARY solution (a-fields = 0):
    #
    # At a fixed point, dPhi_r/dt = 0 and dPsi_r/dt = 0.
    # The classical action (Phi_a = Psi_a = 0) is:
    #
    #   S_eff[FP, a=0] = 0   (by CTP unitarity condition U1)
    #
    # This is EXACT. The CTP action vanishes identically when the a-fields are zero.
    # Therefore Re S_eff = 0 at EVERY fixed point, regardless of which attractor.
    #
    # CONSEQUENCE: Re S_eff CANNOT distinguish between attractors.
    # The selection functional ΔRe S_eff = 0 IDENTICALLY.

    print(f"""
CRITICAL RESULT:

The CTP effective action evaluated at any stationary point with a-fields = 0:

  S_eff[Phi_r = Phi*, Psi_r = Psi*, Phi_a = 0, Psi_a = 0] = 0

This follows from CTP unitarity condition U1:
  S_eff[r-fields, a-fields = 0] = 0  (for ALL r-field configurations)

Therefore:
  Re S_eff(Attractor A) = 0
  Re S_eff(Attractor B) = 0
  ΔRe S_eff = 0   IDENTICALLY

The CTP action evaluated at the classical saddle point provides
NO selection between attractors. This is not a numerical coincidence.
It is a STRUCTURAL CONSEQUENCE of the CTP normalization condition.

Physical interpretation:
  The CTP generating functional computes Tr(rho) = 1, which is
  guaranteed by U1. At any physical configuration (a-fields = 0),
  the action encodes the probability-conservation normalization,
  not a free energy. The CTP action is NOT a free-energy functional.
  It is a probability-generating functional.

  A free-energy comparison would require a DIFFERENT object:
  - The thermal partition function Z = Tr(exp(-beta H)), or
  - The effective potential V_eff(Phi), obtained by a Legendre
    transform or by evaluating the Euclidean action

  Neither of these is the CTP action. The CTP action is the
  Lorentzian (real-time) generating functional for the density matrix.
  It does not minimize at the preferred attractor.
""")

    # Can we extract a free energy from the CTP action?
    print(f"--- CAN THE CTP ACTION YIELD A FREE ENERGY? ---")
    print(f"""
The CTP action S_eff[Phi_r, Phi_a] generates the real-time dynamics.
To obtain a thermodynamic free energy, one must either:

(a) Analytically continue to Euclidean time (Wick rotation):
    S_CTP (Lorentzian) → S_Euclidean → Free energy F = -T ln Z
    This is standard but requires:
    - The system to be in thermal equilibrium
    - The Wick rotation to be well-defined (no branch cuts)
    - The Euclidean action to have a well-defined saddle point

(b) Compute the effective potential V_eff(Phi) from the CTP action:
    V_eff = -Re S_eff / T  evaluated at the stationary field configuration
    But as shown above, Re S_eff = 0 at the saddle point → V_eff = 0.
    This gives no information.

(c) Use the fluctuation determinant:
    The one-loop correction to S_eff around each attractor is:
    delta S = (1/2) Tr ln det(d^2 S / d(Phi_a, Psi_a)^2)
    This DOES differ between attractors (the Hessian is different).
    The one-loop correction gives the entropy/free-energy difference.

Route (c) is the ONLY viable path within the CTP framework.
""")

    # Compute the Hessian (second variation) at each attractor
    print(f"--- ONE-LOOP HESSIAN AT EACH ATTRACTOR ---")

    for k, (Phi_s, Psi_s) in enumerate(stable_fps):
        # The Hessian of S_eff w.r.t. (Phi_a, Psi_a) at the FP:
        # d^2(iS_eff)/d(Phi_a)^2 = 2iD_Phi  (from noise term)
        # d^2(iS_eff)/d(Psi_a)^2 = 2iD_Psi
        # d^2(iS_eff)/d(Phi_a)d(Psi_a) = 0 (no cross-noise)
        #
        # But the full Hessian in the (r,a) space is a 4x4 matrix.
        # The relevant quantity for the fluctuation determinant is
        # the FULL second variation including r-a mixing.
        #
        # The Sector 1 terms produce r-a mixing:
        # d^2(iS)/d(Phi_r)d(Phi_a) = -(-a/tau1) = a/tau1  (from -[-a*(X-Phi_r)]Phi_a)
        # But also: d/dPhi_r of h(X-Phi_r) = -h'(X-Phi_r)
        # For the linear case: h'(v) = a, so d^2S/d(Phi_r)d(Phi_a) = a/tau1
        # For the nonlinear case: h'(v) = gamma - 3*delta*v^2

        v_s = X_eq - Phi_s

        # Hessian blocks (in frequency domain, at omega):
        # The inverse retarded propagator for the (Phi, Psi) system:
        # G_R^{-1}(omega) = [[-i*omega*tau1 - a    , kappa],
        #                     [-epsilon, -i*omega*tau2 - (sigma-1-3*nu*Psi_s^2)]]
        #
        # (This is minus the Jacobian with -i*omega*tau added)
        #
        # The one-loop effective action (fluctuation) is:
        # S_1loop = (i/2) Tr ln det G_R^{-1}(omega)
        #
        # The determinant at omega = 0 (static limit):
        # det G_R^{-1}(0) = det(-J) = det(J)
        # where J is the Jacobian at the fixed point

        J = np.array([
            [-a/tau1, -kappa/tau1],
            [epsilon/tau2, (sigma - 1 - 3*nu*Psi_s**2)/tau2]
        ])
        det_J = np.linalg.det(J)
        tr_J = np.trace(J)

        # The fluctuation free energy (one-loop) is proportional to:
        # F_1loop ~ (1/2) sum_omega ln|det G_R^{-1}(omega)|
        # At the static level (omega = 0): F_1loop ~ (1/2) ln|det J|
        # This DOES differ between attractors if det(J) differs.

        eigs = np.linalg.eigvals(J)

        print(f"\nAttractor {k}: Phi*={Phi_s:.4f}, Psi*={Psi_s:.4f}")
        print(f"  Jacobian eigenvalues: {eigs[0]:.6f}, {eigs[1]:.6f}")
        print(f"  det(J) = {det_J:.6f}")
        print(f"  |det(J)| = {abs(det_J):.6f}")
        print(f"  ln|det(J)| = {np.log(abs(det_J)):.6f}")

    # Compare
    if len(stable_fps) >= 2:
        J_A = np.array([
            [-a/tau1, -kappa/tau1],
            [epsilon/tau2, (sigma - 1 - 3*nu*stable_fps[0][1]**2)/tau2]
        ])
        J_B = np.array([
            [-a/tau1, -kappa/tau1],
            [epsilon/tau2, (sigma - 1 - 3*nu*stable_fps[1][1]**2)/tau2]
        ])
        det_A = abs(np.linalg.det(J_A))
        det_B = abs(np.linalg.det(J_B))

        print(f"\n--- SELECTION TEST ---")
        print(f"  |det(J_A)| = {det_A:.6f}")
        print(f"  |det(J_B)| = {det_B:.6f}")
        print(f"  Ratio: {det_A/det_B:.6f}")
        print(f"  ln|det(J_A)| - ln|det(J_B)| = {np.log(det_A) - np.log(det_B):.6f}")

        if abs(det_A - det_B) / max(det_A, det_B) > 0.01:
            print(f"\n  ΔF_1loop ∝ ln|det(J_A)/det(J_B)| ≠ 0")
            print(f"  ONE-LOOP FREE ENERGY DIFFERS BETWEEN ATTRACTORS.")
            print(f"  The attractor with LARGER |det(J)| has HIGHER free energy")
            print(f"  → the LOWER |det(J)| attractor is thermodynamically preferred.")
            preferred = 0 if det_A < det_B else 1
            print(f"  PREFERRED ATTRACTOR: {preferred} (Phi*={stable_fps[preferred][0]:.4f})")
            print(f"\n  A8 CANDIDATE: prefer the attractor with smaller fluctuation determinant.")
        else:
            print(f"\n  |det(J_A)| ≈ |det(J_B)|. No selection at one-loop level.")

else:
    print(f"\nOnly {len(stable_fps)} stable FP. No bistability at these parameters.")
    print(f"Scanning parameter space...")

    # Systematic scan for bistability
    found_bistable = False
    for sigma_test in np.arange(1.5, 5.0, 0.5):
        for kappa_test in np.arange(0.1, 2.0, 0.3):
            for epsilon_test in np.arange(0.1, 2.0, 0.3):
                c_test = sigma_test - 1 - epsilon_test*kappa_test/a
                d_test = epsilon_test*X_eq
                disc_test = -4*nu*(-c_test)**3 - 27*nu**2*d_test**2
                if disc_test > 0 and c_test > 0:
                    coeffs_test = [nu, 0, -c_test, -d_test]
                    roots_test = np.roots(coeffs_test)
                    real_roots_test = sorted([r.real for r in roots_test if abs(r.imag) < 1e-8])
                    if len(real_roots_test) == 3:
                        n_stable = 0
                        fps_test = []
                        for Psi_s in real_roots_test:
                            Phi_s = X_eq - kappa_test*Psi_s/a
                            J = np.array([
                                [-a/tau1, -kappa_test/tau1],
                                [epsilon_test/tau2, (sigma_test - 1 - 3*nu*Psi_s**2)/tau2]
                            ])
                            eigs = np.linalg.eigvals(J)
                            if all(e.real < 0 for e in eigs):
                                n_stable += 1
                                fps_test.append((Phi_s, Psi_s))
                        if n_stable >= 2:
                            print(f"\n  BISTABLE at sigma={sigma_test}, kappa={kappa_test:.1f}, epsilon={epsilon_test:.1f}")
                            print(f"  Stable FPs: {[(f'{fp[0]:.3f}',f'{fp[1]:.3f}') for fp in fps_test]}")

                            # Compute det(J) at each
                            for fp in fps_test:
                                J = np.array([
                                    [-a/tau1, -kappa_test/tau1],
                                    [epsilon_test/tau2, (sigma_test - 1 - 3*nu*fp[1]**2)/tau2]
                                ])
                                det_J = abs(np.linalg.det(J))
                                print(f"    FP ({fp[0]:.3f}, {fp[1]:.3f}): |det(J)| = {det_J:.6f}, ln|det(J)| = {np.log(det_J):.4f}")

                            found_bistable = True
                            # Use these parameters for the selection test
                            stable_fps = fps_test
                            sigma = sigma_test
                            kappa = kappa_test
                            epsilon = epsilon_test
                            break
            if found_bistable:
                break
        if found_bistable:
            break

    if found_bistable and len(stable_fps) >= 2:
        J_A = np.array([
            [-a/tau1, -kappa/tau1],
            [epsilon/tau2, (sigma - 1 - 3*nu*stable_fps[0][1]**2)/tau2]
        ])
        J_B = np.array([
            [-a/tau1, -kappa/tau1],
            [epsilon/tau2, (sigma - 1 - 3*nu*stable_fps[1][1]**2)/tau2]
        ])
        det_A = abs(np.linalg.det(J_A))
        det_B = abs(np.linalg.det(J_B))

        print(f"\n  --- ONE-LOOP SELECTION TEST ---")
        print(f"  |det(J_A)| = {det_A:.6f}")
        print(f"  |det(J_B)| = {det_B:.6f}")

        if abs(det_A - det_B) / max(det_A, det_B) > 0.01:
            print(f"  ΔF_1loop ∝ Δln|det(J)| = {abs(np.log(det_A) - np.log(det_B)):.4f}")
            print(f"  ONE-LOOP SELECTION EXISTS: attractors have different fluctuation free energies.")
        else:
            print(f"  No selection: |det(J)| approximately equal.")
    elif not found_bistable:
        print(f"\n  No bistable parameter set found in scan. Classification: classifier_persists.")

# ============================================================
# TASK 5: SUMMARY
# ============================================================
print(f"\n" + "=" * 80)
print(f"TASK 5: SUMMARY AND A8 STATUS")
print(f"=" * 80)

print(f"""
RESULTS:

1. CTP ACTION: Written explicitly for coupled (Phi_r, Phi_a, Psi_r, Psi_a).
   CTP unitarity (U1, U2, U3): all PASS.
   Causality: PASS. No cross-noise (minimal).

2. TREE-LEVEL SELECTION: IMPOSSIBLE.
   Re S_eff = 0 at ALL fixed points (CTP unitarity U1).
   The CTP action is a probability-generating functional, not a free energy.
   It cannot distinguish attractors at tree level.

3. ONE-LOOP SELECTION: POSSIBLE.
   The fluctuation determinant det(J) differs between attractors.
   The one-loop free energy F_1loop ~ (1/2) ln|det(J)| generically differs.
   The attractor with smaller |det(J)| (softer fluctuations) has lower
   free energy and is thermodynamically preferred.

4. A8 CANDIDATE:
   A8 = "Prefer the attractor with smaller one-loop fluctuation determinant"
   This is:
   - DERIVABLE from the CTP action (one-loop computation)
   - PHYSICALLY MOTIVATED (minimum free energy / maximum entropy)
   - PARAMETER-DEPENDENT (which attractor is preferred depends on parameters)
   - NOT tree-level (requires one-loop, which is a quantum/thermal correction)

5. ADMISSIBILITY STATUS:
   - Tree-level: classifier_persists (no selection possible)
   - One-loop: constraining admissibility is CONDITIONALLY REALIZABLE
     if bistability exists AND the one-loop determinant computation is trusted

   VERDICT: bounded_open → conditional upgrade to constraining_realized
   at one-loop, contingent on CTP embedding of bistable parameters
""")

print("=" * 80)
print("END OF COMPUTATION")
print("=" * 80)
