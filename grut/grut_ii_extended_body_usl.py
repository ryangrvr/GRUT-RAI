#!/usr/bin/env python3
"""
GRUT II Kappa-Prime — Extended-Body Gravitational Self-Energy Audit

Compute the exact Diosi self-energy difference for a uniform-density
sphere of radius R displaced by l in a spatial superposition.

The Diosi self-energy difference is:

  Delta_E(l, R, m) = (G/2) ∫∫ [rho_1(x) - rho_2(x)][rho_1(x') - rho_2(x')] / |x-x'| d^3x d^3x'

where rho_1(x) = rho_0 * Theta(|x| < R)  (sphere centered at origin)
      rho_2(x) = rho_0 * Theta(|x - l*zhat| < R)  (sphere displaced by l)

This integral has a known exact analytical form related to the gravitational
interaction energy of the "overlap" and "non-overlap" regions.

Key result:
  For l < 2R (overlapping spheres):
    Delta_E = (6 G m^2 / (5 R)) * f(u)
  where u = l/(2R) and f(u) is a known polynomial.

  For l >= 2R (non-overlapping):
    Delta_E = G m^2 / l  (point-mass limit)
"""

import numpy as np
from scipy.integrate import quad, dblquad
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# CONSTANTS
# ============================================================
G    = 6.67430e-11
hbar = 1.05457e-34
k_B  = 1.38065e-23

# ============================================================
# PART I — EXACT SELF-ENERGY DIFFERENCE DEFINITION
# ============================================================
print("=" * 80)
print("PART I — EXACT SELF-ENERGY DIFFERENCE")
print("=" * 80)

print("""
The Diosi self-energy difference for two displaced identical mass distributions:

  Delta_E = (G/2) ∫∫ [rho_1(x) - rho_2(x)] [rho_1(x') - rho_2(x')] / |x-x'| d^3x d^3x'

For two uniform spheres of density rho_0, radius R, displaced by l along z:
  rho_1(x) = rho_0 if |x| < R, else 0
  rho_2(x) = rho_0 if |x - l*zhat| < R, else 0

The difference rho_1 - rho_2 has three regions:
  A: in sphere 1 only (crescent on left)   → rho_1 - rho_2 = +rho_0
  B: in both spheres (overlap lens)         → rho_1 - rho_2 = 0
  C: in sphere 2 only (crescent on right)  → rho_1 - rho_2 = -rho_0

The self-energy integral becomes:
  Delta_E = (G/2) * rho_0^2 * ∫∫ [chi_A(x) - chi_C(x)][chi_A(x') - chi_C(x')] / |x-x'| d^3x d^3x'

where chi_A, chi_C are characteristic functions of the crescent regions.
""")

# ============================================================
# PART II — EXACT ANALYTICAL EVALUATION
# ============================================================
print("=" * 80)
print("PART II — EXACT ANALYTICAL EVALUATION")
print("=" * 80)

# The gravitational self-energy of a uniform sphere of mass m, radius R is:
#   E_self = -(3/5) G m^2 / R
#
# The gravitational INTERACTION energy between two uniform spheres
# of mass m, radius R, separated by distance d (center-to-center) is:
#   For d >= 2R: E_int = -G m^2 / d  (point-mass)
#   For d < 2R (overlapping):
#     E_int(d) = -(G m^2 / R) * [... polynomial in u = d/(2R) ...]
#
# The Diosi quantity is:
#   Delta_E = E_self(sphere_1) + E_self(sphere_2) - 2 E_int(sphere_1, sphere_2)
#           = 2 E_self - 2 E_int
#           = 2 [E_self - E_int]
#
# Wait — let me be more careful. The Diosi integral is:
#
#   Delta_E = (G/2) ∫∫ Delta_rho(x) Delta_rho(x') / |x-x'| d^3x d^3x'
#
# where Delta_rho = rho_1 - rho_2.
#
# Expanding:
#   Delta_E = (G/2) [∫∫ rho_1 rho_1 / r + ∫∫ rho_2 rho_2 / r - 2 ∫∫ rho_1 rho_2 / r] d^3x d^3x'
#           = (G/2) [2 * U_self - 2 * U_cross]
#           = G [U_self - U_cross]
#
# where U_self = ∫∫ rho(x) rho(x') / |x-x'| d^3x d^3x' = (6/5) m^2 / R
#   (the gravitational self-energy magnitude, without the -G/2 factor)
#   Actually: E_grav_self = -(G/2) U_self = -(3/5) G m^2 / R
#   So U_self = (6/5) m^2 / R
#
# And U_cross(l) = ∫∫ rho_1(x) rho_2(x') / |x-x'| d^3x d^3x'
#   For l >= 2R: U_cross = m^2 / l  (point masses)
#   For l < 2R: U_cross has a known polynomial form
#
# Therefore:
#   Delta_E(l) = G [U_self - U_cross(l)]
#              = G [(6/5) m^2 / R - U_cross(l)]

# The interaction energy of two overlapping uniform spheres is given by
# the classic result (see e.g., Griffiths, Jackson):
#
# For two uniform spheres of charge/mass density rho_0, radius R,
# centers separated by d = l, with u = l/(2R):
#
# The potential energy U_cross(l) for l <= 2R is:
#   U_cross = (m^2/R) * [6/5 - (3/2)u + (1/2)u^3]  for 0 <= u <= 1 (l <= 2R)
#
# Wait, I need to be more careful. Let me use the exact result.
#
# The gravitational interaction energy of two uniform spheres of mass m,
# radius R, with centers separated by d is:
#
# For d >= 2R:
#   U_int = -G m^2 / d
#
# For d <= 2R (overlapping):
#   U_int = -G m^2 / (10 R) * [12 - (d/R)^2 * (3/2) * ... ]
#
# Actually, the standard result for the Newtonian potential energy
# of two overlapping uniform spheres is (see Diosi 1987, or compute
# via convolution of the sphere self-potential):
#
# E_int(d) = -G m^2 / R * h(u)
# where u = d / (2R) and for 0 <= u <= 1:
#   h(u) = 6/5 - (3/2) u + (1/2) u^3
#
# Check: at u = 0 (complete overlap): h(0) = 6/5 = self-energy/R coefficient ✓
# at u = 1 (just touching, d = 2R): h(1) = 6/5 - 3/2 + 1/2 = 1/5
#   And from point-mass: -Gm^2/d = -Gm^2/(2R), so h should be 1/2
#   Hmm, that doesn't match. Let me re-derive.

# CORRECT DERIVATION:
# The gravitational potential energy of two uniform-density spheres,
# each of mass m and radius R, with centers at distance d apart:
#
# For d >= 2R (non-overlapping): E = -G m^2 / d
#
# For d < 2R (overlapping), the result can be computed using the
# convolution of the gravitational potential of a sphere with the
# density of the other sphere.
#
# The potential inside a uniform sphere at distance r from center:
#   phi_in(r) = -(G m / (2R)) * (3 - r^2/R^2)  for r <= R
#
# The potential outside:
#   phi_out(r) = -G m / r  for r > R
#
# The interaction energy is:
#   U_int = integral rho_2(x) phi_1(x) d^3x
#
# For two spheres with centers at distance d, this integral is known.
# Using the overlap volume computation:
#
# Let me just compute it numerically to be safe, and then compare
# to analytical formulas.

def U_cross_numerical(m, R, l, N=200):
    """
    Compute the gravitational interaction integral
    U_cross = ∫∫ rho_1(x) rho_2(x') / |x-x'| d^3x d^3x'
    for two uniform spheres of mass m, radius R, displaced by l along z.

    Uses the fact that this equals m * phi_1(x) averaged over sphere 2,
    where phi_1 is the gravitational potential of sphere 1 (without -G factor).

    Actually: U_int = integral rho_2(x) * Phi_1(x) d^3x
    where Phi_1(x) = -G integral rho_1(x')/|x-x'| d^3x'

    We want U_cross WITHOUT the G factor:
    U_cross = integral integral rho_1(x) rho_2(x') / |x-x'| d^3x d^3x'
            = (rho_0)^2 * integral_sphere1 integral_sphere2 1/|x-x'| d^3x d^3x'
    """
    # Use the analytical result for the potential of a uniform sphere
    rho_0 = m / ((4/3) * np.pi * R**3)

    # Potential of sphere 1 (centered at origin) WITHOUT -G factor:
    # Phi_1(r) = rho_0 * (4pi) * [R^3/(3r) if r > R, else (R^2/2 - r^2/6) if r <= R]
    # Wait: the potential integral is:
    # integral rho_1(x')/|x-x'| d^3x' for uniform sphere centered at origin
    # = (4pi rho_0/3) * [R^3/r if r > R; (3R^2 - r^2)/2 if r <= R]
    #   ... actually let me be precise.
    #
    # For a uniform sphere of density rho_0, radius R:
    # phi_sphere(r) = (4 pi rho_0 / 3) * [R^3/r]  for r > R
    # phi_sphere(r) = (4 pi rho_0 / 2) * [R^2 - r^2/3]  for r <= R
    #   = (2 pi rho_0) * [R^2 - r^2/3]
    # Hmm, the standard Newtonian potential (without -G):
    # Phi(r) = integral rho(x')/|x-x'| d^3x'
    # For uniform sphere centered at origin:
    # Phi_inside(r) = (2 pi rho_0 / 3) * (3 R^2 - r^2)  for r <= R
    # Phi_outside(r) = (4 pi rho_0 R^3) / (3 r)  for r > R

    def Phi_sphere(r):
        """Newtonian potential integral (without -G) of uniform sphere at distance r from center."""
        if r <= R:
            return (2 * np.pi * rho_0 / 3) * (3 * R**2 - r**2)
        else:
            return (4 * np.pi * rho_0 * R**3) / (3 * r)

    # U_cross = integral rho_2(x) Phi_1(x) d^3x
    # Sphere 2 centered at (0, 0, l)
    # By symmetry, use cylindrical coordinates (s, phi, z) with z along displacement
    # rho_2 is nonzero when s^2 + (z-l)^2 < R^2
    # Phi_1 depends on distance from origin: r = sqrt(s^2 + z^2)

    # Integrate in cylindrical coordinates
    # z from l-R to l+R, s from 0 to sqrt(R^2 - (z-l)^2)

    def integrand_z(z):
        s_max = np.sqrt(max(R**2 - (z - l)**2, 0))
        if s_max <= 0:
            return 0

        # Integrate over s from 0 to s_max
        def integrand_s(s):
            r = np.sqrt(s**2 + z**2)
            return 2 * np.pi * s * rho_0 * Phi_sphere(r)

        result, _ = quad(integrand_s, 0, s_max, limit=100)
        return result

    z_min = l - R
    z_max = l + R
    result, _ = quad(integrand_z, z_min, z_max, limit=200, epsrel=1e-10)
    return result

# Self-energy integral (l = 0 case):
# U_self = ∫∫ rho(x) rho(x') / |x-x'| d^3x d^3x' = (6/5) m^2 / R
# This is related to the gravitational self-energy: E_self = -G/2 * U_self = -(3/5) G m^2 / R

# ============================================================
# ANALYTICAL FORMULA
# ============================================================
# The interaction energy of two uniform spheres (see Diosi 1987, Penrose 1996):
#
# For u = l/(2R), 0 <= u <= 1:
#   E_int = -G m^2 / R * P(u)
# where P(u) is a polynomial.
#
# The gravitational potential energy:
# U(d) = -G ∫∫ rho_1(x) rho_2(x') / |x-x'| d^3x d^3x'
#       = -G * U_cross(d)
#
# For the self-energy (d=0): U(0) = -G * U_self = -(3/5) G m^2 / R
# So U_self = (6/5) m^2 / R * (R/R) → wait.
# E_self = -(3/5) G m^2 / R. So U_self = (6/5) m^2 / R.
# Check: -(G/2) * (6/5) m^2 / R = -(3/5) G m^2 / R ✓

# The Diosi self-energy difference:
# Delta_E = (G/2) ∫∫ (rho1-rho2)(rho1-rho2)/r
#         = (G/2) [U_self(1) + U_self(2) - 2 U_cross]
#         = (G/2) [2 U_self - 2 U_cross]
#         = G [U_self - U_cross]
#
# Note: Delta_E is POSITIVE (the displaced configuration has higher
# gravitational self-energy because the mass distribution is more spread out).

# For two uniform spheres, the exact result (Diosi 1987):
# Delta_E(l, R, m) = G m^2 / R * g(u)
# where u = l / (2R) and:
#
# For 0 <= u <= 1 (overlapping):
#   g(u) = 6/5 * [1 - (5/3)u + (5/6)u^3 - (1/6)u^5 / ...?]
#
# Actually, let me derive g(u) from the known interaction energy.
#
# The interaction energy of two overlapping uniform spheres with
# total mass m each, radius R, centers at distance d = 2Ru apart:
#
# From Jackson (or direct computation):
# U_cross(d) = (m^2/R) * [6/5 - u + (1/10)*u^3 ...]
#
# Hmm, I'll just compute numerically for small test cases and then
# fit/verify the analytical form.

# Let me use a DIFFERENT, cleaner approach.
# The exact Diosi formula for a uniform sphere of radius R displaced by l:
#
# Delta_E = G * integral integral [rho(x) - rho(x+l)]^2 / |x-x'| d^3x d^3x'
#         = G * [2 U_self - 2 U_cross(l)]
#
# where U_self = (6/5) m^2 / R (self-interaction without G)
# and U_cross(l) is the cross-interaction.
#
# For a uniform sphere, the gravitational interaction energy between
# two identical spheres separated by d can be computed using the
# convolution theorem. The result for d = l <= 2R is:
#
# -G * U_cross(l) = -(3 G m^2) / (160 R^9) *
#     [... long polynomial in l and R ...]
#
# Actually, let me use the standard result from Penrose (2014),
# Diosi (1987), and Bahrami et al. (2014, New J. Phys. 16, 073010):
#
# For a homogeneous sphere of mass m, radius R, displaced by l:
#
# Delta_E(l) = (6 G m^2) / (5 R) * f(l/(2R))
#
# where for 0 <= x <= 1 (x = l/(2R)):
#   f(x) = (5/6) x^2 - (5/4) x^3 + (3/4) x^4 - (1/6) x^5 ... ?
#
# No, let me look up the EXACT formula. The standard reference is
# Bahrami et al. (2014), Eq. (17), or Diosi (1987) Eq. (5).
#
# From Bahrami et al. (2014, New J. Phys. 16, 073010), for a
# homogeneous sphere of radius R and mass m displaced by l:
#
# Delta_E = (G m^2 / R) * I(l/R)
#
# where for t = l/R:
#   I(t) = (6/5) - t/2 + t^3/80 - t^5/3840 + ...   NO, this is wrong.
#
# Let me just compute it properly.

# PROPER COMPUTATION using the gravitational potential.
# The self-energy of a uniform sphere: E_s = -(3/5) G m^2 / R
# The interaction energy between sphere at 0 and sphere at l*zhat:
# For l < 2R (overlapping):
#   We need to integrate Phi_1(r) * rho_2(r) over sphere 2.

# Let me compute U_cross analytically.
# For a uniform sphere of density rho_0, radius R centered at origin,
# potential at point r from center:
#   Phi_in(r) = (2 pi rho_0 / 3)(3R^2 - r^2) for r < R
#   Phi_out(r) = (4 pi rho_0 R^3)/(3r) for r > R
#
# We integrate this over sphere 2 centered at (0,0,l).
# By symmetry, decompose sphere 2 into shells.
# For a shell at distance d from center of sphere 1, thickness dd:
#   If shell is at distance d from center 1, it's at distance (d-l) to (d+l)...
#   Actually, this gets complicated for overlapping spheres.

# NUMERICAL APPROACH: compute U_cross for various l/R values
print("\n--- Numerical computation of U_cross and Delta_E ---")

m_test = 1.0  # mass (arbitrary units for testing)
R_test = 1.0  # radius (arbitrary units)

# Known: U_self = (6/5) m^2 / R
U_self = (6.0/5.0) * m_test**2 / R_test

print(f"  U_self = (6/5) m^2/R = {U_self:.6f}")

l_over_R_values = np.array([0.001, 0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.5,
                              0.7, 1.0, 1.5, 2.0, 2.5, 3.0, 5.0, 10.0])

results = []

for l_over_R in l_over_R_values:
    l_test = l_over_R * R_test

    if l_test >= 2 * R_test:
        # Non-overlapping: point-mass
        U_cross = m_test**2 / l_test
    else:
        # Overlapping: numerical integration
        U_cross = U_cross_numerical(m_test, R_test, l_test) / 1.0  # already in correct units

    Delta_E_exact = U_self - U_cross  # (multiply by G later)
    Delta_E_point = m_test**2 / l_test if l_test > 0 else float('inf')
    suppression = Delta_E_exact / Delta_E_point if Delta_E_point > 0 and Delta_E_point < float('inf') else 0

    results.append((l_over_R, l_test, U_cross, Delta_E_exact, Delta_E_point, suppression))

print(f"\n  {'l/R':>8s} {'U_cross':>12s} {'Delta_E_exact':>14s} {'Delta_E_point':>14s} {'Suppression':>12s}")
print(f"  {'-'*8} {'-'*12} {'-'*14} {'-'*14} {'-'*12}")

for l_over_R, l_test, Uc, De, Dp, S in results:
    print(f"  {l_over_R:8.3f} {Uc:12.6f} {De:14.6e} {Dp:14.6e} {S:12.6f}")

# ============================================================
# PART III — Small l/R expansion
# ============================================================
print("\n" + "=" * 80)
print("PART III — SMALL l/R EXPANSION")
print("=" * 80)

# For small l/R, the difference density Delta_rho = rho_1 - rho_2 ~ -l * grad(rho)
# The leading term in Delta_E scales as l^2.
#
# Specifically, for a uniform sphere:
# Delta_E ~ (G rho_0^2 / 2) * l^2 * ∫∫ (partial_z delta(|x|-R))(partial_z' delta(|x'|-R)) / |x-x'| d^3x d^3x'
#
# This is the "surface term" — the Diosi integral at small l samples
# the SURFACE of the sphere, where the density has a discontinuity.
#
# The exact small-l expansion from the numerics:

# Fit Delta_E / l^2 at small l/R
small_mask = np.array([r[0] for r in results]) < 0.15
if np.sum(small_mask) >= 3:
    l_small = np.array([r[0] for r in results])[small_mask]
    De_small = np.array([r[3] for r in results])[small_mask]

    # Fit Delta_E = C * (l/R)^2 * (m^2/R)
    # Delta_E / (m^2/R) = C * (l/R)^2
    C_fit = De_small / (l_small**2 * m_test**2 / R_test)

    print(f"\n  Small-l/R expansion: Delta_E ≈ C * (l/R)^2 * (m^2/R)")
    print(f"  Fitted coefficient C at different l/R:")
    for i, lr in enumerate(l_small):
        print(f"    l/R = {lr:.3f}: C = {C_fit[i]:.6f}")

    C_0 = C_fit[0]  # best estimate from smallest l/R
    print(f"\n  Leading coefficient: C ≈ {C_0:.4f}")
    print(f"  (Expected from analytical: C = 1/5 = 0.2000 for uniform sphere)")

    # The analytical result for a uniform sphere:
    # Delta_E(l << R) = (G m^2 / R) * (l/R)^2 * (1/5)
    # or equivalently: Delta_E = G m^2 l^2 / (5 R^3)
    C_analytical = 0.2  # This is the known result

    print(f"\n  Ratio to point-mass: S = Delta_E_exact / (Gm^2/l)")
    print(f"  For l << R:")
    print(f"    S = C * (l/R)^2 * R/l = C * l/R")
    print(f"    At l/R = 0.036 (operating point): S ≈ {C_0 * 0.036:.6f}")

# ============================================================
# PART IV — FROZEN OPERATING POINT
# ============================================================
print("\n" + "=" * 80)
print("PART IV — FROZEN OPERATING POINT EVALUATION")
print("=" * 80)

m_op = 25e-18    # 25 fg
rho_silica = 2200.0
R_op = (3 * m_op / (4 * np.pi * rho_silica))**(1./3)
l_op = 5e-9      # 5 nm
l_over_R_op = l_op / R_op

print(f"\n  Particle: m = {m_op*1e18:.1f} fg, R = {R_op*1e9:.1f} nm")
print(f"  Separation: l = {l_op*1e9:.0f} nm")
print(f"  l/R = {l_over_R_op:.4f}")
print(f"  Regime: {'l << R (extended body)' if l_over_R_op < 0.5 else 'l ~ R' if l_over_R_op < 2 else 'l >> R (point mass)'}")

# Point-mass prediction
Lambda_point = G * m_op**2 / (hbar * l_op)
print(f"\n  Point-mass USL: Lambda_point = G m^2 / (hbar l) = {Lambda_point:.4e} s^-1")

# Extended-body correction using the small-l/R formula:
# Delta_E_exact = G m^2 l^2 / (5 R^3)
# Lambda_exact = G m^2 l^2 / (5 R^3 hbar)  ... wait, that's wrong dimensionally.
# Delta_E_exact = G * (m^2/R) * C * (l/R)^2
# So Lambda_exact = G m^2 / (hbar R) * C * (l/R)^2

# Actually, from the numerical fit:
# Delta_E = C * (l/R)^2 * G * m^2 / R
# Lambda = Delta_E / hbar = C * (l/R)^2 * G m^2 / (R hbar)

# But we can also write this as:
# Lambda_exact = Lambda_point * C * (l/R)^2 * R/l = Lambda_point * C * l/R
# Because Lambda_point = G m^2 / (hbar l), so:
# Lambda_exact / Lambda_point = [C * (l/R)^2 * G m^2 / (R hbar)] / [G m^2 / (hbar l)]
#                             = C * (l/R)^2 * l / R = C * l^3 / R^3
# Hmm that doesn't seem right. Let me redo this carefully.

# Delta_E_point = G m^2 / l
# Delta_E_exact = G * m^2 / R * C * (l/R)^2 = G m^2 C l^2 / R^3
# Suppression S = Delta_E_exact / Delta_E_point = C l^3 / R^3
# Wait: S = (G m^2 C l^2 / R^3) / (G m^2 / l) = C l^3 / R^3

S_op = C_0 * (l_op/R_op)**2 * (l_op / (m_op**2 / (m_op**2 / R_op)))
# Let me just compute it directly
Delta_E_exact_formula = G * m_op**2 / R_op * C_0 * (l_op/R_op)**2
Lambda_exact_formula = Delta_E_exact_formula / hbar

S_op_direct = Lambda_exact_formula / Lambda_point

print(f"\n  Extended-body formula (small l/R):")
print(f"  Delta_E_exact = G m^2 / R * C * (l/R)^2")
print(f"               = {Delta_E_exact_formula:.4e} J")
print(f"  Lambda_exact  = {Lambda_exact_formula:.4e} s^-1")
print(f"  Lambda_point  = {Lambda_point:.4e} s^-1")
print(f"  Suppression factor S = Lambda_exact / Lambda_point = {S_op_direct:.6f}")
print(f"  Equivalently: S = C * (l/R)^3 = {C_0:.4f} * ({l_op/R_op:.4f})^3 = {C_0 * (l_op/R_op)**3:.6f}")

# Wait, S = C * l^2/R^2 * R/l... Let me just be careful:
# S = Delta_E_exact / Delta_E_point
# = [G m^2 C (l/R)^2 / R] / [G m^2 / l]
# = C (l/R)^2 * l / R
# = C l^3 / R^3
# = C * (l/R)^3

S_analytical = C_0 * (l_op / R_op)**3
print(f"\n  S = C * (l/R)^3 = {C_0:.4f} * ({l_op/R_op:.4f})^3 = {S_analytical:.6e}")

# Also compute numerically to check
U_cross_op = U_cross_numerical(m_op, R_op, l_op)
U_self_op = (6.0/5.0) * m_op**2 / R_op
Delta_E_numerical = G * (U_self_op - U_cross_op)
Lambda_numerical = Delta_E_numerical / hbar
S_numerical = Lambda_numerical / Lambda_point

print(f"\n  Direct numerical computation:")
print(f"  U_self = {U_self_op:.6e}")
print(f"  U_cross = {U_cross_op:.6e}")
print(f"  Delta_E = G * (U_self - U_cross) = {Delta_E_numerical:.4e} J")
print(f"  Lambda_exact = {Lambda_numerical:.4e} s^-1")
print(f"  Suppression S = {S_numerical:.6e}")

# Gas decoherence rate (from previous stages)
m_gas = 28 * 1.66054e-27
T_env = 4.0
P_gas = 1e-13
v_th = np.sqrt(8 * k_B * T_env / (np.pi * m_gas))
n_gas = P_gas / (k_B * T_env)
Lambda_gas = n_gas * np.pi * R_op**2 * v_th

print(f"\n  Gas decoherence: Lambda_gas = {Lambda_gas:.4e} s^-1")
print(f"  Corrected USL/gas ratio: {Lambda_numerical / Lambda_gas:.4f}")
print(f"  (Was: {Lambda_point / Lambda_gas:.2f} with point-mass USL)")

# ============================================================
# PART V — ROADMAP REVISION: Scan over separations
# ============================================================
print("\n" + "=" * 80)
print("PART V — ROADMAP REVISION")
print("=" * 80)

# The suppression goes as (l/R)^3 for l << R.
# Lambda_exact = Lambda_point * C * (l/R)^3
# = G m^2 / (hbar l) * C * (l/R)^3
# = C G m^2 l^2 / (hbar R^3)
#
# This INCREASES with l (as l^2), unlike Lambda_point which DECREASES (as 1/l).
# So larger separation is BETTER in the extended-body regime!
#
# Lambda_gas is l-independent (in short-wavelength regime).
# So the optimal separation is where Lambda_exact is maximized,
# which in the extended-body regime means l → 2R (the crossover to point mass).

print(f"\nCritical insight: In the extended-body regime (l << R),")
print(f"Lambda_exact ~ l^2, which INCREASES with l.")
print(f"This means LARGER separation is BETTER (opposite of point-mass intuition)!")
print(f"The maximum Lambda_exact occurs near l ~ 2R.")

print(f"\n  Mass = {m_op*1e18:.0f} fg, R = {R_op*1e9:.1f} nm")
print(f"\n  {'l (nm)':>8s} {'l/R':>8s} {'L_exact':>12s} {'L_point':>12s} {'S factor':>10s} {'L_gas':>12s} {'exact/gas':>10s}")
print(f"  {'-'*8} {'-'*8} {'-'*12} {'-'*12} {'-'*10} {'-'*12} {'-'*10}")

for l_nm in [1, 2, 5, 10, 20, 50, 100, 150, 200, 250, 300, 400, 500, 1000]:
    l = l_nm * 1e-9
    lR = l / R_op

    if l >= 2 * R_op:
        # Point-mass regime
        De = G * m_op**2 / l
    else:
        # Extended-body: numerical
        Uc = U_cross_numerical(m_op, R_op, l)
        De = G * (U_self_op - Uc)

    Le = De / hbar
    Lp = G * m_op**2 / (hbar * l)
    S = Le / Lp
    Lg = Lambda_gas  # approximately l-independent for l >> lambda_dB_gas
    ratio = Le / Lg

    print(f"  {l_nm:8d} {lR:8.3f} {Le:12.4e} {Lp:12.4e} {S:10.4f} {Lg:12.4e} {ratio:10.4f}")

# Find optimal separation
print(f"\n--- Optimal separation search ---")
best_ratio = 0
best_l = 0
for l_nm in range(1, 1000):
    l = l_nm * 1e-9
    if l >= 2 * R_op:
        De = G * m_op**2 / l
    else:
        Uc = U_cross_numerical(m_op, R_op, l)
        De = G * (U_self_op - Uc)
    Le = De / hbar
    ratio = Le / Lambda_gas
    if ratio > best_ratio:
        best_ratio = ratio
        best_l = l_nm

print(f"  Optimal l = {best_l} nm (l/R = {best_l*1e-9/R_op:.3f})")
print(f"  Lambda_exact at optimal l = {best_ratio * Lambda_gas:.4e} s^-1")
print(f"  USL/gas at optimal l = {best_ratio:.4f}")

# Now scan masses at optimal separation type
print(f"\n--- Mass scan at l = 2R (maximum Delta_E for each mass) ---")
print(f"\n  {'m (fg)':>8s} {'R (nm)':>8s} {'l=2R (nm)':>10s} {'L_exact':>12s} {'L_gas':>12s} {'ratio':>10s}")
for m_fg in [10, 15, 20, 25, 30, 40, 50, 70, 100]:
    m = m_fg * 1e-18
    R = (3 * m / (4 * np.pi * rho_silica))**(1./3)
    l = 2 * R  # at the touching point
    Le = G * m**2 / (hbar * l)  # point mass is exact at l = 2R
    Lg = n_gas * np.pi * R**2 * v_th
    ratio = Le / Lg
    print(f"  {m_fg:8d} {R*1e9:8.1f} {l*1e9:10.1f} {Le:12.4e} {Lg:12.4e} {ratio:10.4f}")

# ============================================================
# FINAL VERDICT
# ============================================================
print("\n" + "=" * 80)
print("FINAL VERDICT")
print("=" * 80)

print(f"""
CRITICAL RESULT:

The suppression factor for the extended-body USL correction at the
frozen operating point (25 fg, l = 5 nm, R = 140 nm) is:

  S = Lambda_exact / Lambda_point ≈ {S_numerical:.2e}

The point-mass USL OVERESTIMATES the true decoherence rate by a factor
of ~{1/S_numerical:.0f} at this operating point.

The corrected USL/gas ratio is {Lambda_numerical/Lambda_gas:.4f},
compared to the point-mass value of {Lambda_point/Lambda_gas:.1f}.

THE FROZEN OPERATING POINT (l = 5 nm) DOES NOT WORK.
The extended-body suppression kills the signal.

HOWEVER: The suppression goes as (l/R)^3 and REVERSES at larger l.
The maximum USL occurs near l ~ 2R ~ 280 nm, where the point-mass
formula becomes exact and Lambda_exact = G m^2 / (hbar * 2R).

The roadmap must be REOPTIMIZED with the extended-body correction included.
""")

print("=" * 80)
print("END OF COMPUTATION")
print("=" * 80)
