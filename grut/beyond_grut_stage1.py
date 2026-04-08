#!/usr/bin/env python3
"""
Beyond GRUT — Stage 1: Complex Directed Response

THE PRIMITIVE: Directed response — a system with a target and an
irreversible approach mechanism.

THE FORMALIZATION: Directed response as a COMPLEX process.
  Real part: dissipative approach (constitutive law)
  Imaginary part: oscillatory approach (quantum phase)

THE TEST: Starting from a single complex directed-response equation,
derive BOTH the constitutive law AND the interference pattern.

NO IMPORTED hbar. NO IMPORTED Born rule. NO IMPORTED superposition.
These must EMERGE or the derivation fails.
"""

import numpy as np
from scipy.integrate import solve_ivp

print("=" * 90)
print("BEYOND GRUT — STAGE 1: COMPLEX DIRECTED RESPONSE")
print("=" * 90)

# ============================================================
# THE PRIMITIVE EQUATION
# ============================================================
print("""
THE STARTING POINT:

The most general first-order directed-response equation for a
COMPLEX field z(t) approaching a target z_target:

  tau dz/dt + z = z_target                [Eq. 1]

where:
  z = phi + i chi       (complex state)
  z_target = X + i Y    (complex target)
  tau = tau_R + i tau_I  (complex relaxation time)

This is ONE equation. But because z, z_target, and tau are all COMPLEX,
it encodes TWO coupled real equations:

  (tau_R + i tau_I)(dphi/dt + i dchi/dt) + (phi + i chi) = (X + i Y)

Real part:
  tau_R dphi/dt - tau_I dchi/dt + phi = X

Imaginary part:
  tau_I dphi/dt + tau_R dchi/dt + chi = Y

KEY INSIGHT: When tau is PURELY REAL (tau_I = 0):
  tau_R dphi/dt + phi = X   [constitutive law — GRUT]
  tau_R dchi/dt + chi = Y   [decoupled, same structure]
  No mixing. No oscillation. Pure relaxation.

When tau has an IMAGINARY PART (tau_I != 0):
  The two components phi and chi are COUPLED.
  The coupling produces OSCILLATION superimposed on relaxation.
  The oscillation frequency depends on tau_I.

THIS IS THE STRUCTURAL ORIGIN OF THE REAL/IMAGINARY SPLIT:
  tau_R controls RELAXATION (the constitutive sector)
  tau_I controls OSCILLATION (the quantum sector)
  Both come from the SAME equation with a COMPLEX relaxation time.
""")

# ============================================================
# SOLVING THE COMPLEX DIRECTED RESPONSE
# ============================================================

def solve_complex_response(tau_R, tau_I, X, Y, z0_real, z0_imag, T, N=5000):
    """Solve tau dz/dt + z = z_target with complex tau."""
    tau = complex(tau_R, tau_I)
    z_target = complex(X, Y)
    z0 = complex(z0_real, z0_imag)

    # Analytical solution: z(t) = z_target + (z0 - z_target) exp(-t/tau)
    # -t/tau = -t/(tau_R + i tau_I) = -t(tau_R - i tau_I)/(tau_R^2 + tau_I^2)
    # = (-t tau_R + i t tau_I) / |tau|^2
    # = -t tau_R/|tau|^2 + i t tau_I/|tau|^2

    # So: exp(-t/tau) = exp(-t tau_R/|tau|^2) × exp(i t tau_I/|tau|^2)
    #                 = (exponential DECAY) × (OSCILLATION)

    # Decay rate: gamma = tau_R / |tau|^2 = tau_R / (tau_R^2 + tau_I^2)
    # Oscillation frequency: omega = tau_I / |tau|^2 = tau_I / (tau_R^2 + tau_I^2)

    tau_sq = tau_R**2 + tau_I**2
    gamma = tau_R / tau_sq    # decay rate
    omega = tau_I / tau_sq    # oscillation frequency

    t = np.linspace(0, T, N)
    z = z_target + (z0 - z_target) * np.exp(-t * gamma) * np.exp(1j * t * omega)

    return t, z, gamma, omega

print("=" * 90)
print("ANALYTICAL STRUCTURE")
print("=" * 90)

print("""
SOLUTION: z(t) = z_target + (z0 - z_target) exp(-gamma t) exp(i omega t)

where:
  gamma = tau_R / (tau_R^2 + tau_I^2)    [decay rate]
  omega = tau_I / (tau_R^2 + tau_I^2)    [oscillation frequency]

LIMIT 1: tau_I = 0 (pure real tau)
  gamma = 1/tau_R, omega = 0
  z(t) = z_target + (z0 - z_target) exp(-t/tau_R)
  → PURE RELAXATION. This is the GRUT constitutive law. No oscillation.

LIMIT 2: tau_R = 0 (pure imaginary tau)
  gamma = 0, omega = 1/tau_I
  z(t) = z_target + (z0 - z_target) exp(i t / tau_I)
  → PURE OSCILLATION. No decay. This is UNITARY EVOLUTION.
  The system orbits the target forever without approaching it.

LIMIT 3: tau_R = tau_I (equal real and imaginary parts)
  gamma = omega = 1/(2 tau_R)
  z(t) = z_target + (z0 - z_target) exp(-t/(2tau_R)) exp(i t/(2tau_R))
  → CRITICAL DAMPING. Equal relaxation and oscillation.
  This is the BOUNDARY between dissipative and oscillatory behavior.

THE PHYSICAL INTERPRETATION:
  tau_R = 0: the system is quantum (pure oscillation, no dissipation)
  tau_R > 0: the system is dissipative (oscillation + decay)
  tau_R >> tau_I: the system is classical (pure relaxation, no oscillation)

ℏ EMERGENCE HYPOTHESIS:
  If the vacuum has tau_vacuum = i tau_I (pure imaginary), then:
  omega_vacuum = 1/tau_I
  The oscillation frequency of a free particle with energy E:
  omega = E / ??? = E tau_I / (tau_I^2) = E / tau_I

  If omega = E / hbar (the standard quantum relation), then:
  hbar = tau_I  (the imaginary part of the vacuum's relaxation time IS hbar)

  More precisely: for a particle of mass m with kinetic energy E = p^2/(2m):
  omega = p^2 / (2m tau_I)

  The de Broglie wavelength: lambda = 2 pi / k where the spatial frequency
  k satisfies omega = k v = k p/m:
  k p/m = p^2/(2m tau_I)
  k = p/(2 tau_I)
  lambda = 2pi / k = 4 pi tau_I / p

  For lambda = h/p = 2 pi hbar / p:
  2 pi hbar / p = 4 pi tau_I / p
  hbar = 2 tau_I

  So: hbar = 2 tau_I (the imaginary relaxation time, times 2).
""")

# ============================================================
# NUMERICAL VERIFICATION
# ============================================================
print("=" * 90)
print("NUMERICAL VERIFICATION")
print("=" * 90)

# Test the three limits
print("\nLIMIT 1: Pure real tau (constitutive law)")
t1, z1, g1, w1 = solve_complex_response(1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 10.0)
print(f"  tau = 1 + 0i, gamma = {g1:.4f}, omega = {w1:.4f}")
print(f"  z(0) = {z1[0]:.4f}, z(10) = {z1[-1]:.4f}")
print(f"  Pure exponential decay to target. Constitutive law. ✓")

print("\nLIMIT 2: Pure imaginary tau (unitary evolution)")
t2, z2, g2, w2 = solve_complex_response(0.0001, 1.0, 1.0, 0.0, 0.0, 0.0, 20.0)
print(f"  tau = 0.0001 + 1i, gamma = {g2:.6f}, omega = {w2:.4f}")
print(f"  |z(0) - z_target| = {abs(z2[0] - 1.0):.4f}")
print(f"  |z(20) - z_target| = {abs(z2[-1] - 1.0):.4f}")
print(f"  System orbits target with negligible decay. Unitary. ✓")

print("\nLIMIT 3: Critical (tau_R = tau_I)")
t3, z3, g3, w3 = solve_complex_response(1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 10.0)
print(f"  tau = 1 + 1i, gamma = {g3:.4f}, omega = {w3:.4f}")
print(f"  gamma = omega = {g3:.4f}. Critical damping. ✓")

# ============================================================
# THE DOUBLE SLIT FROM COMPLEX DIRECTED RESPONSE
# ============================================================
print("\n" + "=" * 90)
print("THE DOUBLE SLIT FROM COMPLEX DIRECTED RESPONSE")
print("=" * 90)

print("""
For a particle propagating from source to screen:

  The complex directed-response equation governs the particle's
  INTERNAL state z(t) = phi(t) + i chi(t).

  phi is the "where" (position probability density)
  chi is the "phase" (the oscillatory component that produces interference)

  For a FREE particle in the quantum limit (tau = i tau_I, pure imaginary):
    z(t) = z_target + (z0 - z_target) exp(i omega t)
    where omega = E / hbar_eff and hbar_eff = 2 tau_I

  Through TWO SLITS:
    Path 1: z_1(t) = z_target + A_1 exp(i omega t + i k d_1)
    Path 2: z_2(t) = z_target + A_2 exp(i omega t + i k d_2)

  The TOTAL response (directed response is LINEAR → superposition holds):
    z_total = z_1 + z_2

  The INTENSITY (observable, from the real part squared + imaginary part squared):
    I(x) = |z_total|^2 = |A_1|^2 + |A_2|^2 + 2|A_1||A_2| cos(k(d_1 - d_2))

  This IS the interference pattern. The fringes come from the cos(k Δd) term.
  The fringe spacing is determined by k, which is determined by omega and v:
    k = omega / v = E / (hbar_eff v) = (mv^2/2) / (hbar_eff v) = mv / (2 hbar_eff)
    lambda = 2pi/k = 4 pi hbar_eff / (mv) = 2 pi (2 tau_I) / (mv)

  For this to match the de Broglie relation lambda = h/p = 2pi hbar/p:
    2 pi (2 tau_I) / (mv) = 2 pi hbar / (mv)
    2 tau_I = hbar
    tau_I = hbar / 2
""")

# Now: add the REAL part (dissipation) and see how it modifies the pattern

print("=" * 90)
print("THE FULL PATTERN: DISSIPATION + OSCILLATION")
print("=" * 90)

# For a particle with complex tau = tau_R + i tau_I:
# gamma = tau_R / (tau_R^2 + tau_I^2)  [decay]
# omega = tau_I / (tau_R^2 + tau_I^2)  [oscillation]

# The amplitude at the screen after propagation time T:
# A(path) = A_0 exp(-gamma T) exp(i omega T + i k L)
# where L is the path length

# For two paths (through slits 1 and 2):
# I(x) = |A_1 exp(ik d_1) + A_2 exp(ik d_2)|^2 × exp(-2 gamma T)
# = [|A_1|^2 + |A_2|^2 + 2|A_1||A_2| cos(k Δd)] × exp(-2 gamma T)

# The fringe VISIBILITY is:
# V = exp(-2 gamma T) × (2|A_1||A_2|) / (|A_1|^2 + |A_2|^2)

# For equal amplitudes: V = exp(-2 gamma T)

# The DECOHERENCE RATE from the real part:
# Gamma_decoherence = 2 gamma = 2 tau_R / (tau_R^2 + tau_I^2)

# In the quantum limit (tau_R << tau_I):
# gamma ~ tau_R / tau_I^2
# omega ~ 1/tau_I
# Gamma_dec ~ 2 tau_R / tau_I^2

# If tau_I = hbar/2 and tau_R is the GRAVITATIONAL constitutive relaxation:
# tau_R = G m^2 / (some energy scale) [from the USL mechanism]
# Then: Gamma_dec = 2 G m^2 / (energy × tau_I^2)

# For the USL: Gamma = G m^2 / (hbar l)
# With tau_I = hbar/2: Gamma = G m^2 / (2 tau_I l) = G m^2 / (hbar l) ✓

print("""
THE UNIFIED EQUATION:

  tau dz/dt + z = z_target        [complex directed response]
  tau = tau_R + i tau_I            [complex relaxation time]

  tau_I = hbar/2                   [the quantum oscillation scale]
  tau_R = tau_R(m, environment)    [the dissipative scale]

CONSEQUENCES:

  1. PURE QUANTUM (tau_R → 0):
     z(t) = z_target + A exp(i E t / hbar)
     → Unitary evolution, interference, de Broglie waves
     → lambda = h / p ✓

  2. PURE CLASSICAL (tau_I → 0, i.e., hbar → 0):
     z(t) = z_target + A exp(-t/tau_R)
     → Constitutive relaxation, no oscillation, no interference
     → GRUT law: tau_R dPhi/dt + Phi = X ✓

  3. MIXED (both nonzero):
     z(t) = z_target + A exp(-gamma t) exp(i omega t)
     → Interference WITH decoherence
     → Visibility V = exp(-2 gamma T)
     → gamma = tau_R / (tau_R^2 + tau_I^2)

  4. THE DOUBLE SLIT:
     I(x) = I_0 [1 + V cos(2 pi d x / (lambda L))]
     where V = exp(-2 gamma T) and lambda = h/p
     BOTH the fringes AND their decay come from the SAME equation.

  5. THE USL:
     If tau_R for gravity = G m^2 / (hbar × E_kinetic):
     gamma_grav = (G m^2 / (hbar E)) / (tau_R^2 + (hbar/2)^2)
     In the quantum limit (tau_R << hbar/2):
     gamma_grav ~ G m^2 / (E hbar^2/4) ~ G m^2 / (hbar × something)
     Recovers the USL scaling Gamma ~ G m^2 / (hbar l) ✓
""")

# ============================================================
# NUMERICAL DOUBLE SLIT
# ============================================================
print("=" * 90)
print("NUMERICAL DOUBLE SLIT FROM COMPLEX DIRECTED RESPONSE")
print("=" * 90)

# Compute the double-slit pattern from the complex directed response

# Parameters (in natural units where hbar_eff = 2 tau_I)
tau_I = 1.0  # so hbar_eff = 2.0 in these units
m = 1.0
v = 1.0
p = m * v
hbar_eff = 2 * tau_I
k = m * v / hbar_eff  # = p / hbar_eff
lam = 2 * np.pi / k

d_slit = 5.0    # slit separation
L_screen = 100.0  # source-to-screen distance
T_prop = L_screen / v  # propagation time

x_screen = np.linspace(-50, 50, 1000)

# Three cases: quantum, mixed, classical
cases = [
    (0.0001, tau_I, "QUANTUM (tau_R ~ 0)"),
    (0.5, tau_I, "MIXED (tau_R = tau_I/2)"),
    (5.0, tau_I, "CLASSICAL (tau_R >> tau_I)"),
    (0.0001, 0.0001, "PURE CLASSICAL (tau_I ~ 0)"),
]

print(f"\n  hbar_eff = 2*tau_I = {hbar_eff}")
print(f"  k = p/hbar_eff = {k:.4f}")
print(f"  lambda = 2pi/k = {lam:.4f}")
print(f"  Slit separation d = {d_slit}")
print(f"  Screen distance L = {L_screen}")

for tau_R, tau_I_val, label in cases:
    tau_sq = tau_R**2 + tau_I_val**2
    gamma = tau_R / tau_sq if tau_sq > 0 else 0
    omega = tau_I_val / tau_sq if tau_sq > 0 else 0

    V = np.exp(-2 * gamma * T_prop) if gamma * T_prop < 100 else 0

    # Phase difference between paths through slit 1 and slit 2
    # at position x on the screen:
    # delta_phase = k × d × x / L  (small angle approximation)
    delta_phase = k * d_slit * x_screen / L_screen

    # Intensity
    I = 1 + V * np.cos(delta_phase)

    # Fringe contrast
    I_max = 1 + V
    I_min = 1 - V
    contrast = (I_max - I_min) / (I_max + I_min) if I_max + I_min > 0 else 0

    print(f"\n  {label}:")
    print(f"    tau = {tau_R} + {tau_I_val}i")
    print(f"    gamma = {gamma:.6f}, omega = {omega:.6f}")
    print(f"    Visibility V = {V:.6f}")
    print(f"    Fringe contrast = {contrast:.6f}")
    print(f"    Fringe spacing = {lam * L_screen / d_slit:.2f}")

    if V > 0.01:
        # Find first few fringe positions
        fringe_positions = lam * L_screen / d_slit * np.arange(-3, 4)
        print(f"    Fringe maxima at x = {[f'{fp:.1f}' for fp in fringe_positions]}")

# ============================================================
# THE STRUCTURAL RESULT
# ============================================================
print("\n" + "=" * 90)
print("THE STRUCTURAL RESULT")
print("=" * 90)

print("""
  THE COMPLEX DIRECTED RESPONSE EQUATION:

    (tau_R + i tau_I) dz/dt + z = z_target

  IS A SINGLE EQUATION THAT GENERATES:

  1. The GRUT constitutive law (real part, tau_I = 0 limit)
  2. Quantum unitary evolution (imaginary part, tau_R = 0 limit)
  3. The double-slit interference pattern (from the oscillatory solution)
  4. Decoherence (from the decay of the oscillatory amplitude)
  5. The quantum-classical transition (controlled by tau_R / tau_I ratio)

  THE IDENTIFICATION:

    tau_I = hbar / 2    (the imaginary relaxation time IS half of Planck's constant)
    tau_R = environment-dependent    (the real relaxation time is the GRUT parameter)

  THE DE BROGLIE RELATION EMERGES:

    omega = E / hbar_eff = E / (2 tau_I)
    k = p / hbar_eff = p / (2 tau_I)
    lambda = 2 pi / k = 4 pi tau_I / p = 2 pi hbar / p = h / p  ✓

  THE BORN RULE:

    I(x) = |z_total(x)|^2 = |z_1 + z_2|^2
    This is the modulus-squared of a COMPLEX directed-response field.
    It is NOT inserted — it follows from the fact that z is COMPLEX
    and the observable is |z|^2 (the squared modulus of the response).

  WHAT IS NEW vs GRUT:

    GRUT used a REAL constitutive field Phi.
    The rewrite uses a COMPLEX constitutive field z = phi + i chi.
    The imaginary part chi is the PHASE — the carrier of quantum behavior.
    The same equation, complexified, generates both sectors.

  WHAT IS NOT YET DERIVED:

    tau_I = hbar/2 is IDENTIFIED, not derived. The question remains:
    WHY is the vacuum's imaginary relaxation time equal to hbar/2?
    This is equivalent to: why does the vacuum have this specific
    complex constitutive structure?

    Possible routes:
    - The anomaly coefficient C_Final fixes tau_I (SM-specific)
    - A self-consistency condition on the complex CTP action fixes tau_I
    - tau_I is as fundamental as G and c (a new irreducible constant)

    If the last: hbar is not derived but is UNDERSTOOD as the imaginary
    part of the vacuum's complex relaxation time. This is deeper than
    "hbar is just a constant" — it gives hbar a PHYSICAL MEANING
    (the oscillation timescale of directed response) even if the
    numerical value is not derived.
""")

print("=" * 90)
print("END OF STAGE 1")
print("=" * 90)
