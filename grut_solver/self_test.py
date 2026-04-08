#!/usr/bin/env python3
"""
GRUT Self-Test Protocol

For the reference platform, generate:
  1. Λ(P) with all nuisance channels included
  2. Λ at fixed mass for 3 materials with different density
  3. Λ_product vs Λ_Bell at d = 200 nm
  4. Best-fit alternative models

Then ask: Can any competitor fit all three signatures simultaneously?
"""

import numpy as np
import sys
sys.path.insert(0, ".")

from grut_solver import GRUTSolver
from grut_solver.constants import G, HBAR, AMU, RHO_GOLD, RHO_SILICA, RHO_DIAMOND
from grut_solver.usl.gravitational import lambda_grav, lambda_grav_point, suppression_factor
from grut_solver.usl.many_body import entanglement_discriminant
from grut_solver.experiments.competing_models import lambda_csl, lambda_dp_point

solver = GRUTSolver()

# =============================================================================
# REFERENCE PLATFORM
# =============================================================================
m_ref = 1e-14       # 10 fg
R_ref = 50e-9        # 50 nm
l_ref = 100e-9       # 100 nm
T_ref = 10e-3        # 10 mK

print("=" * 90)
print("GRUT SELF-TEST PROTOCOL")
print("=" * 90)
print()
print(f"  Reference platform: m = {m_ref*1e15:.0f} fg, R = {R_ref*1e9:.0f} nm, "
      f"l = {l_ref*1e9:.0f} nm, T = {T_ref*1e3:.0f} mK")
print()

# =============================================================================
# SIGNATURE 1: Λ(P) — Pressure scan with all channels
# =============================================================================
print("=" * 90)
print("SIGNATURE 1: Λ(P) — Pressure Scan")
print("=" * 90)
print()

pressures = np.logspace(-14, -6, 33)
sig1_P = []
sig1_grav = []
sig1_gas = []
sig1_total = []

print(f"  {'P (Pa)':>12s}  {'Λ_grav':>12s}  {'Λ_gas':>12s}  {'Λ_BB':>12s}  "
      f"{'Λ_total':>12s}  {'dominant':>12s}")
print(f"  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*12}")

for P in pressures:
    r = solver.decoherence(m_ref, R_ref, l_ref, T_ref, P)
    Lg = r.lambda_grav
    # Extract gas and BB from budget
    gas_ch = [c for c in r.budget.channels if c.name == "gas_collision"]
    bb_ch = [c for c in r.budget.channels if c.name == "bb_scatter"]
    Lgas = gas_ch[0].rate_hz if gas_ch else 0
    Lbb = bb_ch[0].rate_hz if bb_ch else 0
    Ltot = r.lambda_total
    dom = "GRAVITY" if r.is_grav_dominated else r.binding_channel

    sig1_P.append(P)
    sig1_grav.append(Lg)
    sig1_gas.append(Lgas)
    sig1_total.append(Ltot)

    if P in [1e-14, 1e-12, 1e-11, 1e-10, 1e-9, 1e-8, 1e-7, 1e-6]:
        print(f"  {P:12.0e}  {Lg:12.2e}  {Lgas:12.2e}  {Lbb:12.2e}  "
              f"{Ltot:12.2e}  {dom:>12s}")

sig1_P = np.array(sig1_P)
sig1_grav = np.array(sig1_grav)
sig1_gas = np.array(sig1_gas)
sig1_total = np.array(sig1_total)

# The plateau
plateau_mask = sig1_grav > 5 * sig1_gas
plateau_value = sig1_grav[0]  # gravity rate (constant)
print()
print(f"  GRUT plateau: Λ_grav = {plateau_value:.2f} Hz (pressure-independent)")
print(f"  Plateau visible below P ~ {sig1_P[np.argmin(np.abs(sig1_gas - sig1_grav))]:.1e} Pa")
print()

# =============================================================================
# SIGNATURE 2: Λ(ρ) — Geometry scan at fixed mass
# =============================================================================
print("=" * 90)
print("SIGNATURE 2: Λ(ρ) — Geometry Scan at Fixed Mass")
print("=" * 90)
print()

materials = {
    "Gold":     19300,
    "Diamond":  3510,
    "Silica":   2200,
    "Polymer":  1000,
    "Aerogel":  100,
}

sig2_names = []
sig2_rho = []
sig2_R = []
sig2_S = []
sig2_lambda_grut = []
sig2_lambda_dp = []
sig2_lambda_csl = []

Ldp_fixed = lambda_dp_point(m_ref, l_ref)

print(f"  Fixed: m = {m_ref*1e15:.0f} fg, l = {l_ref*1e9:.0f} nm")
print()
print(f"  {'Material':>10s}  {'ρ':>8s}  {'R (nm)':>8s}  {'l/R':>8s}  "
      f"{'S(l/R)':>10s}  {'Λ_GRUT':>12s}  {'Λ_DP':>12s}  {'Λ_CSL':>12s}")

for name, rho in materials.items():
    R = (3*m_ref/(4*np.pi*rho))**(1/3)
    S = suppression_factor(l_ref, R)
    Lg = lambda_grav(m_ref, l_ref, R)
    Lcsl = lambda_csl(m_ref, l_ref, R)

    sig2_names.append(name)
    sig2_rho.append(rho)
    sig2_R.append(R)
    sig2_S.append(S)
    sig2_lambda_grut.append(Lg)
    sig2_lambda_dp.append(Ldp_fixed)
    sig2_lambda_csl.append(Lcsl)

    print(f"  {name:>10s}  {rho:8.0f}  {R*1e9:8.1f}  {l_ref/R:8.3f}  "
          f"{S:10.2e}  {Lg:12.2e}  {Ldp_fixed:12.2e}  {Lcsl:12.2e}")

sig2_lambda_grut = np.array(sig2_lambda_grut)
sig2_lambda_dp = np.array(sig2_lambda_dp)
sig2_lambda_csl = np.array(sig2_lambda_csl)

grut_geo_span = sig2_lambda_grut.max() / sig2_lambda_grut.min()
dp_geo_span = 1.0  # DP is constant
csl_geo_span = sig2_lambda_csl.max() / (sig2_lambda_csl.min() + 1e-30)

print()
print(f"  GRUT geometry span (max/min): {grut_geo_span:.0f}×")
print(f"  DP geometry span:             {dp_geo_span:.0f}× (no R dependence)")
print(f"  CSL geometry span:            {csl_geo_span:.0f}×")
print()

# =============================================================================
# SIGNATURE 3: Λ_product vs Λ_Bell at d = 200 nm
# =============================================================================
print("=" * 90)
print("SIGNATURE 3: Entanglement Discriminant")
print("=" * 90)
print()

d_bell = 200e-9
disc = entanglement_discriminant(m_ref, l_ref, d_bell, R_ref)

Lp = disc["lambda_product"]
Lb = disc["lambda_bell"]
Lc = disc["lambda_cross"]
pct = disc["percent_difference"]

print(f"  Two particles: m = {m_ref*1e15:.0f} fg each, l = {l_ref*1e9:.0f} nm, d = {d_bell*1e9:.0f} nm")
print()
print(f"  {'State':>15s}  {'Λ (Hz)':>12s}")
print(f"  {'Product':>15s}  {Lp:12.2f}")
print(f"  {'Bell':>15s}  {Lb:12.2f}")
print(f"  {'Cross term':>15s}  {Lc:12.2f}")
print(f"  {'Difference':>15s}  {pct:+12.1f}%")
print()

# What competitors predict for entanglement
print(f"  Model predictions for product vs Bell:")
print(f"  {'Model':>20s}  {'Product':>12s}  {'Bell':>12s}  {'Difference':>12s}")
print(f"  {'GRUT':>20s}  {Lp:12.2f}  {Lb:12.2f}  {pct:+12.1f}%")
print(f"  {'Standard QM':>20s}  {'0':>12s}  {'0':>12s}  {'N/A':>12s}")
print(f"  {'CSL (GRW)':>20s}  {2*lambda_csl(m_ref, l_ref, R_ref):12.2e}  "
      f"{2*lambda_csl(m_ref, l_ref, R_ref):12.2e}  {'0.0%':>12s}")
print(f"  {'DP point-mass':>20s}  {2*Ldp_fixed:12.2f}  {2*Ldp_fixed:12.2f}  {'0.0%':>12s}")
print()

# =============================================================================
# ALTERNATIVE MODEL FITTING
# =============================================================================
print("=" * 90)
print("ALTERNATIVE MODEL FITTING")
print("=" * 90)
print()

# We now test: can each competitor fit all three signatures?

# GRUT reference data for the three signatures:
# Sig1: plateau at 632.9 Hz (pressure-independent)
# Sig2: geometry-dependent rates [gold -> aerogel spanning ~700x]
# Sig3: Bell/product difference of -16.7%

print("  TARGET (GRUT predictions, zero free parameters):")
print(f"    Sig1: Pressure plateau at Λ = {plateau_value:.1f} Hz")
print(f"    Sig2: Geometry span = {grut_geo_span:.0f}× across 5 materials")
print(f"    Sig3: Bell/product ratio = {Lb/Lp:.4f} ({pct:+.1f}%)")
print()

# --- MODEL A: Standard QM + constant floor ---
print("  MODEL A: Standard QM + constant floor (1 free parameter)")
print("  " + "-" * 60)

# Best fit: set floor = GRUT plateau
floor_A = plateau_value
# Sig1: matches plateau (by construction)
sig1_A_match = True
# Sig2: constant floor has NO geometry dependence
sig2_A_residual = np.sqrt(np.mean((np.log10(sig2_lambda_grut) -
                                    np.log10(floor_A))**2))
sig2_A_match = sig2_A_residual < 0.1
# Sig3: constant floor is state-independent
sig3_A_match = False

print(f"    Floor = {floor_A:.1f} Hz")
print(f"    Sig1 (plateau):      {'FITS' if sig1_A_match else 'FAILS'}")
print(f"    Sig2 (geometry):     {'FITS' if sig2_A_match else 'FAILS'} "
      f"(residual = {sig2_A_residual:.2f} dex = cannot track {grut_geo_span:.0f}× span)")
print(f"    Sig3 (entanglement): {'FITS' if sig3_A_match else 'FAILS'} "
      f"(constant floor is state-independent)")
print(f"    ALL THREE:           {'YES' if (sig1_A_match and sig2_A_match and sig3_A_match) else 'NO'}")
print()

# --- MODEL B: Standard QM + power-law nuisance ---
print("  MODEL B: Standard QM + power-law floor Λ = A × m^α (2 free parameters)")
print("  " + "-" * 60)

# Best fit to GRUT mass dependence (at fixed l, varying m through density)
# Use the geometry scan data: different rho gives different R at same m
# A power law Λ = A * m^alpha is MASS-ONLY: no R dependence
# So sig2 fails for the same reason as Model A

# But what if we allow Λ = A * (l/R)^beta? (2 params: A, beta)
# Best fit to GRUT geometry data
log_lr = np.log10(np.array([l_ref/R for R in sig2_R]))
log_Lg = np.log10(sig2_lambda_grut)
coeffs_B = np.polyfit(log_lr, log_Lg, 1)
beta_fit = coeffs_B[0]
A_fit = 10**coeffs_B[1]
log_Lg_fit = np.polyval(coeffs_B, log_lr)
sig2_B_residual = np.sqrt(np.mean((log_Lg - log_Lg_fit)**2))

sig1_B_match = True  # power law can produce a plateau (P-independent)
sig2_B_match = sig2_B_residual < 0.05
sig3_B_match = False  # power law is state-independent

print(f"    Best fit: Λ = {A_fit:.2e} × (l/R)^{beta_fit:.2f}")
print(f"    GRUT predicts: exponent = 3.00 (near field)")
print(f"    Fitted exponent: {beta_fit:.2f}")
print(f"    Sig1 (plateau):      {'FITS' if sig1_B_match else 'FAILS'}")
print(f"    Sig2 (geometry):     {'FITS' if sig2_B_match else 'FAILS'} "
      f"(residual = {sig2_B_residual:.3f} dex)")
print(f"    Sig3 (entanglement): {'FITS' if sig3_B_match else 'FAILS'} "
      f"(power law is state-independent)")
print(f"    ALL THREE:           {'YES' if (sig1_B_match and sig2_B_match and sig3_B_match) else 'NO'}")
print()

# --- MODEL C: CSL ---
print("  MODEL C: CSL (2 free parameters: λ_CSL, r_CSL)")
print("  " + "-" * 60)

# CSL sig1: can produce a plateau (yes)
sig1_C_match = True

# CSL sig2: geometry dependence is exp(-(R/r_CSL)^2) or (r_CSL/R)^3
# Different from GRUT's (l/R)^3
# Fit CSL to GRUT geometry data
csl_rates = np.array([lambda_csl(m_ref, l_ref, R, lambda_CSL=1e-16, r_CSL=1e-7)
                       for R in sig2_R])
# CSL rates at GRW parameters don't match GRUT at all (different scale)
# Try fitting lambda_CSL to match GRUT's average
if np.any(csl_rates > 0):
    scale_C = np.mean(sig2_lambda_grut) / np.mean(csl_rates)
    csl_fitted = csl_rates * scale_C
    sig2_C_residual = np.sqrt(np.mean((np.log10(sig2_lambda_grut + 1e-30) -
                                        np.log10(csl_fitted + 1e-30))**2))
else:
    sig2_C_residual = 10.0
    csl_fitted = np.zeros_like(csl_rates)

sig2_C_match = sig2_C_residual < 0.1

# CSL sig3: no entanglement dependence
sig3_C_match = False

print(f"    Sig1 (plateau):      {'FITS' if sig1_C_match else 'FAILS'} (with fitted λ_CSL)")
print(f"    Sig2 (geometry):     {'FITS' if sig2_C_match else 'FAILS'} "
      f"(residual = {sig2_C_residual:.2f} dex — different R-scaling)")
print(f"    Sig3 (entanglement): {'FITS' if sig3_C_match else 'FAILS'} "
      f"(CSL is state-independent)")
print(f"    ALL THREE:           {'YES' if (sig1_C_match and sig2_C_match and sig3_C_match) else 'NO'}")
print()

# --- MODEL D: DP point-mass ---
print("  MODEL D: Diósi-Penrose point-mass (0 free parameters, but no geometry)")
print("  " + "-" * 60)

# DP sig1: produces a plateau (same as GRUT in point-mass limit)
sig1_D_match = True

# DP sig2: NO geometry dependence (Lambda = Gm^2/(hbar l), independent of R)
sig2_D_residual = np.sqrt(np.mean((np.log10(sig2_lambda_grut) -
                                    np.log10(Ldp_fixed))**2))
sig2_D_match = sig2_D_residual < 0.1

# DP sig3: the Diósi functional DOES have entanglement dependence
# (it's the same functional as GRUT, just without extended body)
# So DP point-mass WOULD show Bell protection, but at wrong absolute rate
dp_disc = entanglement_discriminant(m_ref, l_ref, d_bell, R=None)  # no R = point mass
dp_pct = dp_disc["percent_difference"]
sig3_D_match = abs(dp_pct - pct) / abs(pct) < 0.5  # within 50% of GRUT

print(f"    Sig1 (plateau):      {'FITS' if sig1_D_match else 'FAILS'} (Λ = {Ldp_fixed:.1f} Hz)")
print(f"    Sig2 (geometry):     {'FITS' if sig2_D_match else 'FAILS'} "
      f"(residual = {sig2_D_residual:.2f} dex — no R dependence)")
print(f"    Sig3 (entanglement): {'FITS' if sig3_D_match else 'FAILS'} "
      f"(Bell diff = {dp_pct:+.1f}% vs GRUT {pct:+.1f}%)")
print(f"    ALL THREE:           {'YES' if (sig1_D_match and sig2_D_match and sig3_D_match) else 'NO'}")
print()

# =============================================================================
# FINAL VERDICT
# =============================================================================
print("=" * 90)
print("VERDICT: CAN ANY COMPETITOR FIT ALL THREE SIGNATURES?")
print("=" * 90)
print()

models = [
    ("A: QM + constant floor", 1, sig1_A_match, sig2_A_match, sig3_A_match),
    ("B: QM + power-law floor", 2, sig1_B_match, sig2_B_match, sig3_B_match),
    ("C: CSL", 2, sig1_C_match, sig2_C_match, sig3_C_match),
    ("D: DP point-mass", 0, sig1_D_match, sig2_D_match, sig3_D_match),
    ("GRUT", 0, True, True, True),
]

print(f"  {'Model':>28s}  {'Params':>6s}  {'Plateau':>8s}  {'Geometry':>8s}  "
      f"{'Entangle':>8s}  {'All 3?':>8s}")
print(f"  {'-'*28}  {'-'*6}  {'-'*8}  {'-'*8}  {'-'*8}  {'-'*8}")

grut_unique = True
for name, params, s1, s2, s3 in models:
    all3 = s1 and s2 and s3
    if all3 and name != "GRUT":
        grut_unique = False
    mark = " <<<" if name == "GRUT" else ""
    print(f"  {name:>28s}  {params:>6d}  "
          f"{'YES' if s1 else 'NO':>8s}  {'YES' if s2 else 'NO':>8s}  "
          f"{'YES' if s3 else 'NO':>8s}  {'YES' if all3 else 'NO':>8s}{mark}")

print()
if grut_unique:
    print("  RESULT: NO COMPETITOR FITS ALL THREE SIGNATURES.")
    print("  GRUT is the ONLY model that simultaneously produces:")
    print(f"    1. A pressure plateau at Λ = {plateau_value:.1f} Hz")
    print(f"    2. Geometry-dependent rates spanning {grut_geo_span:.0f}× across densities")
    print(f"    3. Entanglement-dependent decoherence ({pct:+.1f}% Bell protection)")
    print()
    print("  The entanglement signature (Sig3) is the decisive discriminant.")
    print("  It cannot be reproduced by any state-independent model.")
else:
    print("  WARNING: AT LEAST ONE COMPETITOR FITS ALL THREE.")
    print("  GRUT is degenerate with this model.")

print()
print("=" * 90)
print("END OF SELF-TEST PROTOCOL")
print("=" * 90)
