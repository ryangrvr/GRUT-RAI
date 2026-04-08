#!/usr/bin/env python3
"""
Program M - Stage M2: Finite Counterterm and Scheme Shift Test

Determine whether -108000 in C_Cosmo is anomaly-protected or scheme-dependent.
"""
import numpy as np
from scipy.special import zeta

pi = np.pi
z3 = zeta(3)
ln2 = np.log(2)

C_Final_num = 3*(99 + 2*pi**2 + 576*ln2*z3)
C_Final_den = 16384 * pi**6
C_Final = C_Final_num / C_Final_den

C_Cosmo_num = -108000 + pi**4 + 1536*pi**4*ln2 + 540*z3
C_Cosmo_den = 276480 * pi**4
C_Cosmo = C_Cosmo_num / C_Cosmo_den

R0 = abs(C_Cosmo) / abs(C_Final)

print("=" * 90)
print("Program M - Stage M2: Finite Counterterm and Scheme Shift Test")
print("=" * 90)

# ============================================================
# STEP 1: EXPLICIT FINITE RENORMALIZATION SHIFT
# ============================================================
print()
print("=" * 90)
print("STEP 1: FINITE RENORMALIZATION SHIFT ANALYSIS")
print("=" * 90)

print(f"""
The effective action at 3-loop order contains (schematically):

  Gamma = ... + C_Final R ln(Box/mu^2) R + C_Cosmo R + c_2 R^2 + c_W C_{{munu}} C^{{munu}} + c_GB E_4 + ...

where:
  R ln(Box/mu^2) R = nonlocal (anomaly-induced, finite)
  R = cosmological-type term
  R^2, C^2, E_4 = higher-derivative local operators (Weyl^2, Gauss-Bonnet)

Under a FINITE RENORMALIZATION (scheme change), one is free to add:

  Delta S = int d^4x sqrt(-g) [delta_a R^2 + delta_b C_{{munu}} C^{{munu}} + delta_c E_4 + delta_Lambda R]

The key operator for C_Cosmo is delta_Lambda * R (a shift of the cosmological term).

Question: does the scheme freedom allow delta_Lambda to be arbitrary?
""")

# The effective action has a term C_Cosmo * R.
# Under finite renormalization: C_Cosmo -> C_Cosmo + delta_Lambda / C_Cosmo_den
# (where delta_Lambda is the coefficient of the R counterterm in the same normalization)
#
# Actually, C_Cosmo is defined as the coefficient in:
# Pi^(0)(q^2) = C_Final q^2 ln(q^2/mu^2) + C_Cosmo + O(q^4)
#
# A finite shift of the COSMOLOGICAL CONSTANT adds a q^2-independent constant
# to Pi^(0): Pi^(0) -> Pi^(0) + delta_Lambda
# This shifts C_Cosmo -> C_Cosmo + delta_Lambda
# C_Final is UNAFFECTED (the q^2 ln(q^2) part is nonlocal, cannot be shifted by a local counterterm)

# So: delta_C affects C_Cosmo but NOT C_Final
# R(delta_C) = |C_Cosmo + delta_C| / |C_Final|

# What is the natural SCALE of delta_C?
# In dim reg with MS-bar: the finite part after pole subtraction is FIXED.
# In a DIFFERENT scheme (e.g., on-shell subtraction at q^2 = M^2):
# Pi^(0)(q^2 = 0) would be subtracted differently.
# The finite shift delta_C can be of ORDER the coefficient itself:
# delta_C ~ O(C_Cosmo) ~ O(10^-4)
#
# BUT: the scheme freedom is CONSTRAINED by diffeomorphism invariance.
# The cosmological constant Lambda in the Einstein equation is PHYSICAL
# (it is measured). Any scheme change that shifts C_Cosmo must be
# compensated by a shift in Lambda_bare to keep Lambda_obs fixed:
# Lambda_obs = Lambda_bare + C_Cosmo + delta_C
# So: delta_C is ABSORBED into Lambda_bare.
#
# The PHYSICAL question is: given Lambda_obs = fixed, does R depend
# on how we split Lambda_obs into Lambda_bare + C_Cosmo?

print("ANALYSIS: What can delta_C be?")
print()
print("C_Cosmo enters the effective action as a vacuum energy contribution:")
print("  Lambda_eff = Lambda_bare + C_Cosmo")
print()
print("Under a finite renormalization:")
print("  C_Cosmo -> C_Cosmo + delta_C")
print("  Lambda_bare -> Lambda_bare - delta_C  (to keep Lambda_obs fixed)")
print()
print("C_Final is UNAFFECTED (nonlocal term, cannot be shifted by local counterterm).")
print()
print("Therefore: R(delta_C) = |C_Cosmo + delta_C| / |C_Final|")
print()
print(f"  C_Cosmo = {C_Cosmo:.6e}")
print(f"  C_Final = {C_Final:.6e}")
print(f"  R(0) = {R0:.6f}")
print()

# What delta_C shifts R by 10%?
# R(delta_C) = |C_Cosmo + delta_C| / C_Final = R0 * (1 + delta_C / C_Cosmo)
# (for delta_C << C_Cosmo)
# For 10% shift: delta_C / C_Cosmo = 0.1 -> delta_C = 0.1 * C_Cosmo
delta_C_10pct = 0.1 * abs(C_Cosmo)
print(f"  delta_C for 10% shift in R: {delta_C_10pct:.6e}")
print(f"  This is {delta_C_10pct/abs(C_Cosmo)*100:.1f}% of C_Cosmo")
print()

# Now: what is the natural SIZE of scheme-freedom delta_C?
# At 3 loops in dim reg, the finite parts are O(alpha^3) where alpha ~ 1/(16pi^2)
# C_Cosmo ~ 10^-4, so delta_C from a scheme change is also ~ 10^-4 at most.
# But the rational part alone is -108000 / (276480 pi^4) = -4.01e-3
# while the transcendental part is +104455 / (276480 pi^4) = +3.88e-3
# The DIFFERENCE is C_Cosmo = -1.32e-4.
# A scheme change that shifts -108000 by even 1% (1080) would shift
# the rational part by 1080/(276480 pi^4) = 4.01e-5, which is
# 4.01e-5 / 1.32e-4 = 30% of C_Cosmo. That would shift R by 30%.

# Let me parametrize directly in terms of the rational coefficient
# C_Cosmo = (-108000 + transcendental) / denominator
# If -108000 -> -108000 + delta_n (integer shift in numerator rational part)

print("SENSITIVITY TO RATIONAL COEFFICIENT SHIFT:")
print()
print("C_Cosmo_num = -108000 + (pi^4 + 1536 pi^4 ln(2) + 540 zeta(3))")
trans_part = pi**4 + 1536*pi**4*ln2 + 540*z3
print(f"           = -108000 + {trans_part:.2f}")
print(f"           = {C_Cosmo_num:.2f}")
print()
print("If the rational part shifts: -108000 -> -108000 + delta_n")
print()

delta_n_values = [-5000, -2000, -1000, -500, -100, 0, 100, 500, 1000, 2000, 5000]
print(f"  {'delta_n':>8s} {'C_Cosmo_num':>14s} {'C_Cosmo':>14s} {'R':>12s} {'dR/R':>10s}")
print(f"  {'-'*8} {'-'*14} {'-'*14} {'-'*12} {'-'*10}")

for dn in delta_n_values:
    C_num_new = (-108000 + dn) + trans_part
    C_new = C_num_new / C_Cosmo_den
    R_new = abs(C_new) / abs(C_Final)
    dR_rel = (R_new - R0) / R0
    print(f"  {dn:8d} {C_num_new:14.2f} {C_new:14.6e} {R_new:12.6f} {dR_rel:+10.4f}")

# ============================================================
# STEP 2: WARD IDENTITY / ANOMALY CONSISTENCY CHECK
# ============================================================
print()
print("=" * 90)
print("STEP 2: WARD IDENTITY / ANOMALY CONSISTENCY CHECK")
print("=" * 90)

print("""
QUESTION: Does altering -108000 violate any physical constraint?

A) DIFFEOMORPHISM WARD IDENTITY: nabla_mu T^{mu nu} = 0
   This constrains the DIVERGENT part of the effective action (pole residues).
   It does NOT constrain the FINITE part (the subtracted remainder).
   Finite renormalization freedom in the cosmological constant sector
   is ALLOWED by diffeomorphism invariance.

   VERDICT: -108000 is NOT protected by diffeomorphism Ward identities.

B) TRACE ANOMALY: <T^mu_mu> = a E_4 + c C^2 + b R^2
   The trace anomaly coefficients (a, c) are SCHEME-INDEPENDENT at one loop
   (the a-theorem, Zamolodchikov in 2D, Komargodski-Schwimmer in 4D).
   At higher loops, the anomaly coefficients can receive scheme-dependent
   corrections through mixing with local counterterms.

   The question: is C_Cosmo determined by the a-anomaly coefficient?

   C_Cosmo is the ZERO-MOMENTUM LIMIT of Pi^(0)(q^2). This is the
   vacuum energy contribution, which is RELATED to but NOT IDENTICAL with
   the trace anomaly. The trace anomaly constrains the q^2-dependent
   structure (through c_2 R^2, etc.) but the q^2 = 0 value (vacuum energy)
   is a SEPARATE quantity with its own renormalization.

   VERDICT: The trace anomaly constrains the DERIVATIVE of Pi^(0)(q^2)
   (hence C_Final, which multiplies q^2 ln q^2), but NOT the VALUE
   at q^2 = 0 (C_Cosmo). The zero-momentum value is a vacuum energy
   contribution subject to independent finite renormalization.

C) ANOMALY MATCHING (at phase transitions / thresholds):
   The Wess-Zumino consistency condition requires that anomaly coefficients
   match across energy thresholds. But this applies to the ANOMALY
   COEFFICIENTS (a, c), not to the vacuum energy (cosmological constant).
   C_Cosmo is not an anomaly coefficient in the Wess-Zumino sense.

   VERDICT: Anomaly matching does NOT protect C_Cosmo.

D) DIRECT PHYSICAL OBSERVABLE:
   C_Cosmo contributes to Lambda_eff. But Lambda_eff = Lambda_bare + C_Cosmo,
   and Lambda_bare is a free parameter. Only Lambda_eff (the sum) is
   observable. C_Cosmo itself is NOT an observable — it is a calculational
   intermediate whose value depends on the split between bare and anomaly
   contributions.

   VERDICT: C_Cosmo is NOT directly observable. Only Lambda_eff = Lambda_bare + C_Cosmo
   is physical. Shifting C_Cosmo and Lambda_bare in opposite directions
   leaves physics unchanged.

OVERALL VERDICT: -108000 is NOT anomaly-protected.
It is subject to finite renormalization freedom in the cosmological
constant sector. Diffeomorphism invariance, trace anomaly matching,
and Wess-Zumino conditions do NOT forbid shifting the rational part.
""")

# What about C_Final?
print("CROSS-CHECK: Is C_Final protected?")
print()
print("C_Final multiplies the NONLOCAL operator R ln(Box/mu^2) R.")
print("This operator CANNOT be generated by any LOCAL counterterm.")
print("Therefore: no finite renormalization can shift C_Final.")
print("C_Final IS anomaly-protected (by nonlocality).")
print()
print("ASYMMETRY: C_Final is protected (nonlocal). C_Cosmo is NOT (local).")
print("The ratio R = |C_Cosmo / C_Final| inherits the FRAGILITY of C_Cosmo.")

# ============================================================
# STEP 3: ALTERNATIVE BASIS DECOMPOSITION
# ============================================================
print()
print("=" * 90)
print("STEP 3: ALTERNATIVE BASIS DECOMPOSITION")
print("=" * 90)

print("""
The 4D gravitational action has three independent curvature-squared operators:
  1. R^2 (Ricci scalar squared)
  2. R_{mu nu} R^{mu nu} (Ricci tensor squared)
  3. R_{mu nu rho sigma} R^{mu nu rho sigma} (Riemann tensor squared)

Or equivalently, in the Gauss-Bonnet + Weyl basis:
  1. C_{mu nu rho sigma} C^{mu nu rho sigma}  (Weyl tensor squared)
  2. E_4 = R^2 - 4 R_{mu nu} R^{mu nu} + R_{mu nu rho sigma} R^{mu nu rho sigma}  (Gauss-Bonnet)
  3. R^2

The Gauss-Bonnet term E_4 is TOPOLOGICAL in 4D (does not contribute to
the equations of motion). So only C^2 and R^2 are dynamically relevant.

The TRACE ANOMALY in 4D involves:
  <T^mu_mu> = a E_4 + c C^2 + (local terms)

The a-coefficient is the one protected by the a-theorem (monotonicity
under RG flow). The c-coefficient is NOT monotonic but IS scheme-independent
at one loop.

C_Cosmo enters the effective action as a coefficient of R (not R^2).
It is a COSMOLOGICAL CONSTANT type term, not a curvature-squared term.
Under a basis change of the curvature-squared operators, C_Cosmo is UNCHANGED
(it does not involve curvature-squared operators).

HOWEVER: at 3 loops, there are CROSS-TERMS between the R term and the
R^2, C^2 terms through operator mixing. A basis change in the curvature-
squared sector COULD shift the finite part of the R coefficient through
these cross-terms.

VERDICT: C_Cosmo is in a SEPARATE operator class (dimension-2 vs dimension-4)
from the curvature-squared operators. Basis changes among the curvature-squared
operators do NOT directly shift C_Cosmo. But operator MIXING at higher loops
could introduce indirect sensitivity. This is a higher-order effect.
""")

# ============================================================
# STEP 4: NUMERICAL SENSITIVITY MAP
# ============================================================
print("=" * 90)
print("STEP 4: NUMERICAL SENSITIVITY MAP")
print("=" * 90)
print()

# Plot R(delta_C) where delta_C shifts C_Cosmo
# delta_C in units of C_Cosmo itself (fractional shift)

print("R as a function of additive shift delta_C to C_Cosmo:")
print()
print("Note: delta_C is in the SAME UNITS as C_Cosmo (~10^-4).")
print("Parametrize delta_C as fraction of |C_Cosmo|.")
print()

fracs = np.linspace(-2.0, 2.0, 41)
print(f"  {'delta_C/|C_C|':>14s} {'delta_C':>14s} {'R':>12s} {'dR/R (%)':>10s}")
print(f"  {'-'*14} {'-'*14} {'-'*12} {'-'*10}")

for frac in fracs:
    dC = frac * abs(C_Cosmo)
    R_shifted = abs(C_Cosmo + dC) / abs(C_Final)
    dR_pct = (R_shifted - R0) / R0 * 100
    if abs(frac - round(frac, 1)) < 0.01 or abs(frac) < 0.01:
        print(f"  {frac:14.2f} {dC:14.6e} {R_shifted:12.6f} {dR_pct:+10.2f}%")

# Key thresholds
print()
print("KEY THRESHOLDS:")
# delta_C that shifts R by 1%
dC_1pct = 0.01 * abs(C_Cosmo)
print(f"  delta_C for dR/R = 1%:  {dC_1pct:.4e} = {dC_1pct/abs(C_Cosmo)*100:.1f}% of |C_Cosmo|")
# delta_C that shifts R by 10%
dC_10pct = 0.10 * abs(C_Cosmo)
print(f"  delta_C for dR/R = 10%: {dC_10pct:.4e} = {dC_10pct/abs(C_Cosmo)*100:.1f}% of |C_Cosmo|")
# delta_C that makes R = 1 (C_Cosmo = C_Final)
dC_R1 = abs(C_Final) - abs(C_Cosmo)
print(f"  delta_C for R = 1:      {dC_R1:.4e}")
# delta_C that makes C_Cosmo = 0
dC_zero = -C_Cosmo  # C_Cosmo is negative, so dC must be +|C_Cosmo|
print(f"  delta_C for C_Cosmo = 0: {dC_zero:.4e}")

print()
print("In terms of the rational coefficient -108000:")
dC_per_unit_n = 1.0 / C_Cosmo_den
print(f"  1 unit of rational shift (delta_n = 1): delta_C = {dC_per_unit_n:.4e}")
dn_for_1pct = dC_1pct / dC_per_unit_n
dn_for_10pct = dC_10pct / dC_per_unit_n
print(f"  delta_n for dR/R = 1%:  {dn_for_1pct:.0f}")
print(f"  delta_n for dR/R = 10%: {dn_for_10pct:.0f}")

# ============================================================
# FINAL VERDICT
# ============================================================
print()
print("=" * 90)
print("FINAL VERDICT")
print("=" * 90)

print(f"""
FINDINGS:

1. FINITE RENORMALIZATION FREEDOM EXISTS.
   C_Cosmo can be shifted by delta_C through addition of a finite
   local cosmological counterterm delta_Lambda * R. This is ALLOWED
   by diffeomorphism invariance.

2. C_Final IS PROTECTED.
   It multiplies a NONLOCAL operator (R ln Box R) that cannot be
   generated by any local counterterm. C_Final is anomaly-fixed.

3. WARD IDENTITIES DO NOT PROTECT C_Cosmo.
   Diffeomorphism invariance constrains the divergent part (poles)
   but not the finite remainder. The trace anomaly constrains
   the q^2-dependent part (C_Final) but not the q^2 = 0 value (C_Cosmo).
   Anomaly matching (Wess-Zumino) applies to anomaly coefficients (a, c)
   not to the cosmological constant.

4. C_Cosmo IS NOT DIRECTLY OBSERVABLE.
   Only Lambda_eff = Lambda_bare + C_Cosmo is physical.
   The split between Lambda_bare and C_Cosmo is convention-dependent.

5. SENSITIVITY:
   delta_n = {dn_for_1pct:.0f} (in the rational coefficient) shifts R by 1%.
   delta_n = {dn_for_10pct:.0f} shifts R by 10%.
   Given that -108000 is an integer determined by diagram combinatorics
   in MS-bar, a scheme change could shift it by O(100-1000), which
   would shift R by O(3-30%).

CLASSIFICATION: R IS FRAGILE.

The ratio R = |C_Cosmo/C_Final| inherits the scheme freedom of C_Cosmo.
C_Final is protected by nonlocality (anomaly-fixed).
C_Cosmo is NOT protected (local operator, subject to finite renormalization).
R is a DEFINITE NUMBER in MS-bar but is NOT a scheme-independent invariant.

The paper's claim that R is "independent of the renormalization scale mu,
the specific gauge choice, and regularization artifacts" is:
  - CORRECT for mu-independence (exact: no mu in the formula)
  - CORRECT for gauge-independence (standard in dim reg with gauge fixing)
  - INCORRECT for scheme-independence (C_Cosmo has finite renormalization freedom)

TOKEN: r_scheme_fragile

The fragility is specific: C_Final is safe, C_Cosmo is not.
R depends on the finite renormalization prescription for the vacuum energy.
""")
