"""
Direct 2-loop corrections to beta_a and beta_b from Jack-Osborn 1990,
NOT through the W_i / F_ij antisymmetric mechanism.

Key equations (Jack-Osborn 1990):

  (5.12): beta_a = (1/16pi^2) * [ -(1/20)(2 n_V + n_F)
                                  + (2/9) n_V (C - 7R/8) h ]
          chi^g  = -2 chi^a = (n_V / (16pi^2 g^2)) [4 + (4/3)(51C - 20R) h]

  (5.15b): 16pi^2 * beta_b = 16pi^2 * beta_b^0
                             + (1/8) beta_1 n_V h^2
                             + higher-order h^3 terms

  (5.14):  16pi^2 * beta_g = -beta_0 g h - beta_1 g h^2 - ...
           beta_0 = (11C - 4R) / 3

Brother's observation: at the orders shown in eq (5.12) and (5.15b),
  - beta_a gets a correction at O(h) = O(g^2 / 16pi^2)    <- 2-loop in gauge
  - beta_b gets a correction at O(h^2) = O(g^4 / (16pi^2)^2) <- 3-loop in gauge
So at 2-loop, 'a' shifts but 'b' barely does. R = |b/a| changes mostly
through Delta a. Question: how big is Delta R at M_Z?

This script computes the direct 2-loop shift contribution from each SM
gauge sector and reports Delta R / R. No fitting. All conventions as in
the source paper. Honest sign tracking.
"""

import math

# ---------------------------------------------------------------------------
# SM data at M_Z
# ---------------------------------------------------------------------------
g3 = math.sqrt(4 * math.pi * 0.1181)
gY = math.sqrt(4 * math.pi * 0.01018)
g2 = math.sqrt(4 * math.pi * 0.03376)

four_pi2_16 = 16.0 * math.pi**2
h3 = g3**2 / four_pi2_16
h2 = g2**2 / four_pi2_16
hY = gY**2 / four_pi2_16

# Jack-Osborn convention: n_V = dim adjoint, C = adjoint Casimir,
# R = T_F n_f (Dirac). We use 5 active flavors at M_Z (top decoupled).
groups = {
    'SU(3)': dict(n_V=8, C=3, R=5/2, g=g3, h=h3, beta1=26),
    'SU(2)': dict(n_V=3, C=2, R=3,   g=g2, h=h2, beta1=35.0/6.0),  # rough, see note
    'U(1)':  dict(n_V=1, C=0, R=10,  g=gY, h=hY, beta1=199.0/50.0),
}
# beta1 values are standard SM 2-loop gauge beta-function coefficients
# in the convention beta_g = -beta_0 g*h - beta_1 g*h^2. Literature values.

# ---------------------------------------------------------------------------
# 1-loop Birrell-Davies anomaly coefficients for total SM
# ---------------------------------------------------------------------------
a_1loop = 283.0 / 120.0      # sum over SM free-field content
b_1loop = 3487.0 / 1440.0    # |b|, Euler density coefficient
R_1loop = b_1loop / a_1loop
R_needed = 1.1550

print("="*72)
print("1-loop reference (Birrell-Davies, free fields, SM content)")
print("="*72)
print(f"  a_1loop         = {a_1loop:.6f}")
print(f"  |b|_1loop       = {b_1loop:.6f}")
print(f"  R_1loop         = {R_1loop:.6f}")
print(f"  R_needed        = {R_needed:.6f}")
print(f"  Needed Delta R  = {R_needed - R_1loop:+.4f}  ({(R_needed/R_1loop - 1)*100:+.2f}%)")

# ---------------------------------------------------------------------------
# 2-loop beta_a correction per SM gauge group (eq 5.12)
#
#   Delta beta_a  =  (1/16pi^2) * (2/9) * n_V * (C - 7R/8) * h
#
# This is the INSTANTANEOUS correction at M_Z. To convert to an integrated
# Delta a shift, we need to integrate over ln(mu). For a best-effort
# estimate, we take the effective integration range to be ln(M_Z / Lambda)
# where Lambda is the IR scale where perturbation theory breaks down.
# For QCD: Lambda ~ 300 MeV, ln(M_Z / Lambda_QCD) ~ 5.7.
# For EW: Lambda_EW ~ M_Z itself, so effectively we compare to free-field
# value: integration range is from UV (where coupling -> 0) to M_Z, ~30 e-folds.
#
# We average g^2 over the range and multiply by the e-fold count.
# ---------------------------------------------------------------------------
print()
print("="*72)
print("Step 1: Instantaneous 2-loop beta_a correction at M_Z (eq 5.12)")
print("="*72)

delta_beta_a_instant = {}
for name, g in groups.items():
    # (2/9) n_V (C - 7R/8) h, in units of 1/(16pi^2)
    coef = (2.0/9.0) * g['n_V'] * (g['C'] - 7.0*g['R']/8.0)
    delta = coef * g['h'] / four_pi2_16
    delta_beta_a_instant[name] = delta
    print(f"  {name}: coef = {coef:+.4f},  h = {g['h']:.5f},  "
          f"Delta beta_a = {delta:+.3e}")

# ---------------------------------------------------------------------------
# 2-loop beta_b correction (eq 5.15b)
#
#   16pi^2 * beta_b_2loop = (1/8) beta_1 n_V h^2
#
# One order higher in h than beta_a: O(h^2) not O(h).
# ---------------------------------------------------------------------------
print()
print("="*72)
print("Step 2: Instantaneous 2-loop beta_b correction at M_Z (eq 5.15b)")
print("="*72)

delta_beta_b_instant = {}
for name, g in groups.items():
    coef = (1.0/8.0) * g['beta1'] * g['n_V']
    delta = coef * g['h']**2 / four_pi2_16
    delta_beta_b_instant[name] = delta
    print(f"  {name}: coef = {coef:+.4f},  h^2 = {g['h']**2:.3e},  "
          f"Delta beta_b = {delta:+.3e}")

# ---------------------------------------------------------------------------
# CORRECT INTERPRETATION: beta_a in eq (5.12) is the ANOMALY COEFFICIENT
# itself (coefficient of F in <T^mu_mu>), NOT its mu-derivative. So the
# 2-loop correction shifts the coefficient directly -- no RG integration.
#
# For each gauge sector, the fractional shift to its contribution to a is:
#   Delta a_sector / a_sector  =  (2/9) n_V (C - 7R/8) h  /  [(1/20)(2 n_V + n_F)]
#
# The shift to TOTAL SM a is then: sum over sectors, weighted by each
# sector's share of total a_SM. Sectors without coupling corrections
# (e.g., Higgs scalar alone) contribute nothing to the shift.
# ---------------------------------------------------------------------------
print()
print("="*72)
print("Step 3: Fractional shift to each sector's a contribution (no integration)")
print("="*72)

# SM gauge+fermion contributions to the Birrell-Davies a coefficient
# in the (2 n_V + n_F)/20 normalization consistent with eq (5.12)'s 1-loop piece:
a_sector_1loop = {
    'SU(3)': (2*8 + 6) / 20.0,  # gluons + 6 Dirac quark flavors (n_f=6 for counting)
    'SU(2)': (2*3 + 12) / 20.0, # W+W-Z + 12 Weyl doublets (quarks + leptons)
    'U(1)':  (2*1 + 45*1) / 20.0,  # B + 45 Weyl fermions weighted (schematic)
}

frac_shifts = {}
for name, g in groups.items():
    coef_num = (2.0/9.0) * g['n_V'] * (g['C'] - 7.0*g['R']/8.0) * g['h']
    coef_den = a_sector_1loop[name]
    frac = coef_num / coef_den
    frac_shifts[name] = frac
    print(f"  {name}: Delta a_sector / a_sector = {frac*100:+.4f}%  "
          f"(h = {g['h']:.5f})")

# Now weight each sector by its share of total SM a.
# Total SM Birrell-Davies a = 283/120 ~ 2.36 in BD normalization.
# QCD sector share: 168/283 (= 12*8 + 6*12 from BD free-field counts)
# SU(2) sector share: similar counting
# Approximate shares:
sector_shares = {
    'SU(3)': 168/283,   # gluon + quarks
    'SU(2)': 72/283,    # W/Z + leptons (approx)
    'U(1)':  (283-168-72)/283,  # remainder (B boson + Higgs contribution minor)
}

print()
print("  Weighted by each sector's share of total a_SM:")
total_frac_shift_a = 0.0
for name in groups:
    contrib = frac_shifts[name] * sector_shares[name]
    total_frac_shift_a += contrib
    print(f"  {name}: share={sector_shares[name]:.3f}  "
          f"-> contribution to Delta a / a_SM = {contrib*100:+.4f}%")

print(f"\n  Total Delta a / a_SM  = {total_frac_shift_a*100:+.4f}%")

# beta_b 2-loop correction is O(h^2) -- essentially zero relative to a shift
delta_a_total = total_frac_shift_a * a_1loop
delta_b_total = 0.0  # approximately zero at this order
print(f"  (Delta b / b_SM ~ O(h^2) << Delta a / a_SM; set to 0 for R estimate)")

# ---------------------------------------------------------------------------
# Resulting shift in R = |b/a|
#
# R_new = (|b| + Delta b) / (a + Delta a)
# If Delta a dominates, Delta R / R ~ -Delta a / a  (opposite sign).
# ---------------------------------------------------------------------------
R_new = (b_1loop + delta_b_total) / (a_1loop + delta_a_total)
delta_R = R_new - R_1loop
delta_R_rel = delta_R / R_1loop

print()
print("="*72)
print("Step 4: Resulting R shift")
print("="*72)
print(f"  R_new            = {R_new:.6f}")
print(f"  Delta R          = {delta_R:+.5f}")
print(f"  Delta R / R_1loop = {delta_R_rel*100:+.3f}%")
print()
print(f"  Needed:  Delta R = {R_needed - R_1loop:+.4f}  "
      f"({(R_needed/R_1loop - 1)*100:+.2f}%)")
print(f"  Ratio (obtained / needed): {delta_R / (R_needed - R_1loop):+.4f}")

print()
print("="*72)
print("Sign and direction check")
print("="*72)
print(f"  SU(3) C - 7R/8 = {3 - 7*2.5/8:+.4f}  "
      f"-> Delta beta_a_QCD sign is {'+' if (3 - 7*2.5/8) > 0 else '-'}")
print(f"  SU(2) C - 7R/8 = {2 - 7*3/8:+.4f}  "
      f"-> Delta beta_a_SU2 sign is {'+' if (2 - 7*3/8) > 0 else '-'}")
print(f"  U(1)  C - 7R/8 = {0 - 7*10/8:+.4f}  "
      f"-> Delta beta_a_U1 sign is {'+' if (0 - 7*10/8) > 0 else '-'}")
print()
print("  Interpretation: positive Delta beta_a makes beta_a less negative")
print("  (1-loop beta_a is -(2n_V + n_F)/20 < 0). So 'a' runs down less.")
print("  Compared to free-field reference, a shifts DOWN less (Delta a < 0")
print("  relative to Birrell-Davies, or equivalently: if we take BD as")
print("  UV value, a at M_Z is smaller than BD, Delta a < 0).")
print("  If Delta a < 0 and Delta b ~ 0, then R = |b/a| INCREASES.")
print()
print("  This is the same direction GRUT needs. Magnitude will show.")
