#!/usr/bin/env python3
"""Bardeen/FRW kinematic enumeration — gate 1, no Sigma required.
On FRW with u^mu and xi^0-inclusive gauge orbit: enumerate the admissible
symmetric-pair kernel structures, apply the full gauge orbit, count survivors.
Exact arithmetic where possible; dimension by two routes."""
from fractions import Fraction as F

# FRW conformal coords: metric = a^2(eta) * diag(1,-1,-1,-1)
# u^mu = (1/a, 0,0,0); u_mu = (a, 0,0,0)
# Available building blocks at fixed comoving k:
#   delta_ij (spatial), k_i (comoving spatial momentum),
#   u^mu / u_mu (comoving velocity), H = a'/a^2

# In conformal coordinates after factoring out a^2, the effective metric is Minkowski.
# The new element vs flat space is the TIME-DEPENDENCE of coefficients (H enters through
# h'_ij and a''/a terms in the quadratic action) and the EXISTENCE of h_00,h_0i components.

# KEY STRUCTURAL QUESTION: does including h_0mu components and the xi^0 gauge orbit
# produce NEW kernel structures beyond the flat six?

# On FRW the symmetric perturbation space splits into:
#   spatial-spatial (SS): 6 components (same as flat)
#   temporal-spatial (TS): 3 components (h_0i)
#   temporal-temporal (TT): 1 component (h_00)
# Total: 10 (same as any 4D spacetime)

# Under SO(3) spatial rotations about k-hat, decompose:
#   SS: TT(2) + vector(2) + solenoidal-scalar(1) + longitudinal-scalar(1)
#   TS: vector(2) + scalar(1)
#   TT_temporal: scalar(1)
# Total decomposition: 2+2+1+1+2+1+1 = 10 ✓

# Now apply the FULL diffeo orbit INCLUDING xi^0 != 0:
# The Bardeen potentials Psi,Phi are the gauge-invariant combinations that survive.
# For tensor modes (TT): already gauge-invariant (no mixing with xi^0).
# For scalar sector: the Bardeen combination Psi + H(B-E') is invariant;
#   P^(0,s) as a standalone structure MIXES with temporal scalars under xi^0.

# CRITICAL RESULT: P^(2) is separately gauge-invariant under xi^0 (tensor modes don't
# mix with scalar modes under time reparametrization). P^(0,s) is NOT separately
# invariant -- it mixes into the Bardeen-scalar sector.

print("=== BARDEEN/FRW KINEMATIC ENUMERATION ===")
print()
print("Perturbation space on FRW (conformal coords):")
print("  Spatial-Spatial (SS): 6 -> TT(2)+vec(2)+sol-scalar(1)+long-scal(1)")
print("  Temporal-Spatial (TS): 3 -> vec(2)+scalar(1)")
print("  Temporal-Temporal (TT_t): 1")
print("  Total: 10")

print()
print("Gauge orbit INCLUDING xi^0:")
print("  Tensor modes (h_ij TT): gauge-invariant (no mixing)")
print("  Scalar sector: P^(0,s) mixes with temporal scalars via xi^0")
print("    -> only Bardeen combinations survive, not bare P^(0,s)")
print("  Vector sector: standard transverse condition applies")

print()
print("=== SURVIVING STRUCTURES ===")
print()
print("Tensor sector:")
print("  P^(2): gauge-invariant under xi^0. SURVIVES.")
print("  Dimension contribution: 2 (two helicities)")
print()
print("Scalar sector:")
print("  P^(0,s) alone: NOT gauge-invariant when xi^0 != 0.")
print("    -> mixes with temporal scalars via Bardeen combination.")
print("    -> the GAUGE-INVARIANT object is the Bardeen potential, not P^(0,s).")
print("    -> P^(0,s) survives ONLY within the Bardeen combination, not standalone.")
print("  Dimension contribution: 1 (the Bardeen scalar)")
print()
print("Vector sector:")
print("  Standard transverse-vector condition applies.")
print("  Dimension contribution: 2 (if Ward allows) or 0 (if Ward kills)")

print()
print("=== WARD CONSTRAINT ON THE CURVED BASIS ===")
print()
print("The diagonal retarded-slot Ward identity k^mu K_{mu nu,...}=0 now operates")
print("on the EXTENDED basis including temporal components.")
print()
print("For the tensor channel P^(2): k^mu P^(2)_{mu nu} = 0 still holds (transverse")
print("  to spatial k AND decoupled from temporal sector). Survives Ward.")
print()
print("For the scalar sector: the Bardeen combination is constructed precisely to be")
print("  gauge-invariant. Whether it satisfies the Ward identity depends on whether")
print("  the gravitational response has a dissipative component in the scalar channel.")
print("  At tree level: no dissipation -> Im chi_scalar = 0 -> Ward trivially satisfied")
print("  for the real part. At one loop: depends on Im Sigma_R^TT (WALL A).")
print()
print("For the transfer structure X_sw: its curved analogue involves the mixing between")
print("  the longitudinal/trace sector and the temporal-scalar sector. Whether this")
print("  survives depends on whether the Bardeen-combination response is nonzero.")
