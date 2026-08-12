#!/usr/bin/env python3
"""THE Q^2 BAND TEST: is the conformalon's rung7<->rung9 unification real for the ACTUAL,
SM-fixed Q^2 -- carrying BOTH prefactors to the end?

Q^2 is NOT a knob. It is fixed by Standard-Model field content (Q^2 = -2 b', the a-anomaly
coefficient). So the test is not 'does a viable Q^2 exist' -- it is 'does THE Q^2 the SM hands
us land in the band where alpha still holds AND w(z) is still visible'. No fitting freedom:
either the determined number works or it falsifies the connection.

  <sigma^2> = K_sigma / Q^2          governs BOTH effects (they pull oppositely):
  alpha-shift:  d(alpha)/alpha = k_alpha * <sigma^2>   (must be <~ 0.03 -> alpha held)
  w-deviation:  1 + w           = k_w     * <sigma^2>   (must be ~ 0.2  -> DESI-visible)

K_sigma, k_alpha, k_w are the Antoniadis-Mottola PREFACTORS (with their 4pi^2 / loop / field
sums). They are NOT computed here -- they are being grounded against primaries (workflow). This
calc does the two things it CAN do exactly: (1) the actual Q^2 from SM content, and (2) the
lag-driven w(z) SIGN through the matter->dark-energy transition. The band verdict is then carried
as a function of the prefactor-products, ready to read off when grounded. Units H0=1. Pure stdlib.
"""
import math

# ---------------------------------------------------------------------------------------
# PART 1 -- the actual Q^2 from Standard-Model field content (no fitting freedom)
# ---------------------------------------------------------------------------------------
# a-type (Euler) anomaly central charge per field (standard, units 1/(4pi)^2 absorbed in Q^2 norm):
#   real scalar a=1/360, Weyl fermion a=11/720, vector a=31/180.
# Mottola conformalon kinetic coefficient (matter sector):
#   Q^2 = (1/180)(N_S + (11/2) N_WF + 62 N_V)   [+ graviton/conformalon piece, flagged]
N_S, N_V = 4, 12
for label, N_WF in (("no nu_R", 45), ("with 3 nu_R", 48)):
    Q2_matter = (1.0 / 180.0) * (N_S + (11.0 / 2.0) * N_WF + 62.0 * N_V)
    a_charge = (1.0 / 720.0) * (2 * N_S + 11 * N_WF + 124 * N_V)
    print(f"SM field content ({label}): N_S={N_S}, N_WF={N_WF}, N_V={N_V}")
    print(f"   a-central-charge a_SM = {a_charge:.3f}   (1/360 units)")
    print(f"   Q^2_SM (matter)       = {Q2_matter:.3f}   (~2*a, consistent)  [+ O(few) graviton/conformalon piece]")
Q2_SM = (1.0 / 180.0) * (N_S + (11.0 / 2.0) * 45 + 62.0 * N_V)   # use no-nu_R as baseline
print(f"\n=> THE Q^2 the SM hands us: Q^2_SM ~ {Q2_SM:.2f}  (positive -> stable kinetic term). Fixed, not fit.")
print(f"   <sigma^2> = K_sigma / Q^2_SM = {1.0/Q2_SM:.4f} * K_sigma   (K_sigma from the action).")

# ---------------------------------------------------------------------------------------
# PART 2 -- the band test, carrying BOTH prefactors explicitly (verdict as a function of them)
# ---------------------------------------------------------------------------------------
print("\n" + "=" * 80)
print("PART 2 -- BAND TEST (both prefactor-products carried; do NOT drop a 4pi^2)")
print("=" * 80)
sig2_over_K = 1.0 / Q2_SM          # <sigma^2> = sig2_over_K * K_sigma
alpha_bound, w_target = 0.03, 0.2
print(f"  <sigma^2> = {sig2_over_K:.4f} * K_sigma   (Q^2_SM = {Q2_SM:.2f})")
print(f"  alpha holds  :  k_alpha * K_sigma  <=  alpha_bound / <sigma^2>/K_sigma  =  {alpha_bound/sig2_over_K:.3f}")
print(f"  DESI-visible :  k_w     * K_sigma  ~=  w_target  / <sigma^2>/K_sigma   =  {w_target/sig2_over_K:.3f}")
print(f"  => BAND OPEN iff the action gives:")
print(f"        (k_w * K_sigma)     ~  {w_target/sig2_over_K:.2f}      [w visible]")
print(f"        (k_alpha * K_sigma) <= {alpha_bound/sig2_over_K:.2f}      [alpha holds]")
print(f"     i.e. ratio  k_w/k_alpha >= {w_target/alpha_bound:.1f}  AND absolute  k_w*K_sigma ~ O(1).")
print("  These two prefactor-products are the entire verdict. They are being grounded, not")
print("  estimated. If k_w*K_sigma << 1, w is invisible (connection inert); if k_alpha*K_sigma")
print("  is too large, alpha breaks. The SM-fixed Q^2 sets the scale they are measured against.")

# illustrative: show where the band sits, with PLACEHOLDER prefactors clearly marked
print("\n  [ILLUSTRATIVE ONLY -- placeholder prefactors, NOT the answer]:")
print("    if K_sigma ~ 1/(4pi^2) loop size and k_w, k_alpha ~ O(1):")
Ksig_demo = 1.0 / (4 * math.pi ** 2)
for kw, ka in ((1.0, 0.1), (1.0, 1.0)):
    wdev = kw * Ksig_demo * sig2_over_K
    ash = ka * Ksig_demo * sig2_over_K
    verdict = "BAND OPEN" if (wdev > 0.05 and ash < alpha_bound) else ("alpha breaks" if ash >= alpha_bound else "w too small")
    print(f"      k_w={kw}, k_alpha={ka}: 1+w={wdev:.4f}, d(alpha)/alpha={ash:.4f}  -> {verdict}")
print("    (With a 1-loop K_sigma the w-deviation is ~1e-3, far below DESI's 0.2 -- so the")
print("     connection likely needs K_sigma ~ O(1) (non-loop-suppressed), which is exactly the")
print("     conformal-protection question. This illustrates why the prefactor, not the scaling,")
print("     decides it -- and must be grounded, not guessed.)")

# ---------------------------------------------------------------------------------------
# PART 3 -- the lag-driven w(z) SIGN through the matter->DE transition (computable now)
# ---------------------------------------------------------------------------------------
print("\n" + "=" * 80)
print("PART 3 -- LAG-DRIVEN w(z) SIGN through the transition (the prediction lives in the lag)")
print("=" * 80)
OM, OL = 0.31, 0.69
def Hsq(N):
    a = math.exp(N); z = 1 / a - 1
    return OM * (1 + z) ** 3 + OL

c = 3.0
N0, N1, steps = -2.5, 0.0, 40000
dN = (N1 - N0) / steps
m2 = c * Hsq(N0)                 # start in equilibrium at high z
grid = []
for i in range(steps + 1):
    N = N0 + i * dN
    H2 = Hsq(N)
    grid.append((N, H2 / m2))    # eps = H^2/m^2
    if i < steps:
        m2 += -(m2 / (3 * H2)) * (m2 - c * Hsq(N + 0.5 * dN)) * dN

def eps_at(z):
    N = math.log(1 / (1 + z))
    j = min(range(len(grid)), key=lambda k: abs(grid[k][0] - N))
    return grid[j][1]

print("  m_eff^2 relaxes toward c*H^2 but LAGS while H drops fast in matter domination, then the")
print("  lag relaxes through the transition -> eps=H^2/m^2 rises toward now:")
print("      z       eps=H^2/m^2      (1+w)/[k_w K_sigma]  (= eps)")
prev = None
for z in (3.0, 2.0, 1.0, 0.5, 0.0):
    e = eps_at(z); prev = e
    print(f"   {z:5.2f}      {e:10.4f}            {e:10.4f}")
e0, h = eps_at(0.0), 1e-3
sign_lag = "eps LARGEST now (rises toward z=0)" if eps_at(0.0) > eps_at(1.0) else "eps largest in the PAST"
dwa = (eps_at(h) - eps_at(0.0)) / h     # d eps/dz at 0 ; w_a = k_w * d eps/dz
print(f"\n  lag behavior: {sign_lag}")
print(f"  => w_a = k_w * (d eps/dz)|_0 = k_w * ({dwa:+.4f}).  SIGN of w_a = sign(k_w) x sign({dwa:+.4f}).")
print(f"     d eps/dz < 0 (eps falls with z) -> w_a < 0 (DESI quintom) PROVIDED k_w > 0.")
print(f"     So: DESI sign requires k_w > 0 (conformal stress gives w>-1). That sign is the")
print(f"     w-stress-prefactor question -- grounded by the workflow, NOT assumed here.")

print("\n" + "=" * 80)
print("WHERE THE ANSWER LIVES (honest)")
print("=" * 80)
print(f"""\
  COMPUTED HERE (no freedom): Q^2_SM ~ {Q2_SM:.2f} (positive); the lag makes eps largest-now, so the
  w(z) SHAPE has w_a<0 (DESI quintom) IFF the conformal stress sign k_w>0.
  CARRIED, NOT DROPPED: the band is open iff (k_w*K_sigma) ~ {w_target/sig2_over_K:.1f} and
  (k_alpha*K_sigma) <= {alpha_bound/sig2_over_K:.2f}. Three prefactors (K_sigma, k_alpha, k_w) decide it.
  THE GATE BEFORE ALL OF IT: if conformal symmetry PROTECTS/gaps the mode, K_sigma is suppressed
  (loop-sized) and the w-deviation is ~1e-3 << 0.2 -> connection inert. So the order of questions is:
    (0) is the mode protected? -> if yes, dead.  (1) k_w sign -> DESI sign.  (2) prefactor products -> band.
  All three are in the running prefactor workflow; this calc fixed Q^2_SM and the lag, and carried
  the rest explicitly so the verdict reads off the moment the prefactors land.""")
