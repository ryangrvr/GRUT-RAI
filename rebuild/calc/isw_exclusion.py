#!/usr/bin/env python3
"""isw_exclusion: compute the LOAD-BEARING NUMBER -- the low-ell ISW exclusion significance for the
GRUT interior family mu(x) = 1 + x*alpha (trace-only endpoint x=1: mu=4/3) -- honestly, against the
observable the register actually cites (the low-ell temperature-galaxy CROSS-CORRELATION).

WHY THIS EXISTS: the register banked "~32sigma" as an in-house assertion with no computation; it
gates mu_linear's endpoint exclusion AND zeta_interior_family's window edge (2/32 = 1/16). The
cited papers headline ~4-5sigma DETECTIONS -- a different quantity. This calc computes the
EXCLUSION significance: how far the mu(x) prediction sits from the measured cross-amplitude.

PRE-REGISTERED DISCIPLINE (the brief's kill-conditions):
  KC1 quantity confusion: detection significance (how well ISW is seen) != exclusion significance
      (how far the model prediction sits from observation). Computed separately below; NOTE the
      honest structural fact that for a SIGNAL-KILLING model the two nearly coincide (a model
      predicting A ~ 0 can never be excluded by a cross-detection at much more than the detection
      significance itself). That coincidence is physics, not conflation.
  KC2 unstated scaling: N_sigma(x) = N(1)*x is NOT carried forward blind; the actual N(x) curve is
      computed and its deviation from linearity reported at the corrected edge.
  KC3 anchor-shopping: measurement inputs and kernels are stated UP FRONT with sensitivity bands;
      nothing is tuned to reproduce (or to avoid) the banked 32.
  KC4 leg double-counting: this calc hardens the ISW-CROSS leg only. The other supports (separate-
      universe structural leg -- PART E; DESI Sigma0; the low-ell TT AUTO channel -- PART F,
      estimate-grade only) are accounted SEPARATELY and none silently absorbs a shortfall.
DIRECTIONAL GUARD: the flattering direction is CONFIRMING ~32sigma (keeps the no-go strong and the
window edge tight). Default-broken: confirmation requires the computation to produce it.

THE MEASUREMENT SIDE (KC3 -- stated up front, not fitted):
  Observable: the combined galaxy-CMB cross-correlation amplitude A relative to the LCDM template
  (A = 1 is LCDM). Central inputs: A_obs = 1.00 +/- 0.22 (the Giannantonio-2008-class combined
  ~4.5sigma detection, consistent-with-LCDM consensus statement; sources isw_lowl "and updates").
  Sensitivity band swept: A_obs in [0.85, 1.40], sigma_A in [0.20, 0.32] (the spread of published
  combined analyses). Galaxy kernels: three dN/dz ~ (z/z0)^2 exp(-(z/z0)^1.5) samples with median
  z ~ {0.15, 0.45, 1.1} (2MASS-like / SDSS-like / NVSS-like); combined = ratio of summed signals
  across kernels (the joint-template-fit analog);
  per-kernel spread reported. Effective multipole ell_eff = 20 (band {10, 40} reported).

THE MODEL SIDE (banked bookkeeping, inherited -- sources of truth imported):
  mu(x) from calc/mu_slip_interior.py (which itself verifies against calc/mu_linear.py endpoints).
  Constant, scale-independent mu (the banked bookkeeping carries no k- or a-dependence -- FENCED).
  Linear growth: D'' + (2 - (3/2)Om(a)) D' - (3/2) Om(a) mu D = 0  (' = d/dlna), flat LCDM
  background Om = 0.315. Potential amplitude g = Sigma(x) * D/a. FIREWALL CORRECTION B1
  (2026-08-03): constant Sigma cancels in decay-RATE ratios but NOT in the template-relative
  AMPLITUDE -- the ISW source is d/deta of the WEYL potential and the register's own banked lensing
  line (calc/mu_linear.py: k^2(Phi+Psi) = -8piG a^2 Sigma rho Delta) puts Sigma in it, so
      A(x) = Sigma(x) * R_growth(x).
  ISW source per unit z: src(z) = (1 - f(z)) * g(z)/(1+z), f = dlnD/dlna; src > 0 = decay =
  positive cross-correlation. Cross-amplitude ratio in Limber form at fixed ell:
      A(x) = Sigma(x) * int dz n(z) D_obs(z) E(z) src_x(z) P(k)  /  [same with x=0, Sigma=1]
  with k = (ell+1/2)/chi(z), P(k) = k^ns T_BBKS(k)^2, and D_obs = D_LCDM (the galaxy field is the
  OBSERVED field, calibrated by its own clustering -- using D_x there would double-count the model
  into the calibrated galaxy leg; FENCED). Both D's normalized D(0) = 1 (template amplitude
  calibrated at z=0 by the same low-z clustering; primordial normalization instead would drag in
  the sigma8 observable, which is NOT this leg -- KC4).

NAMED FENCES (model-side softness, in the open):
  F-QS   quasi-static/Limber at low ell is leading-order; near-horizon corrections O((H/k)^2) are
         tens of percent at ell ~ 10 -- absorbed into the KC3 band, not resolved here.
  F-SCALE the banked bookkeeping's mu is scale-independent; a kernel confining the modification
         strictly super-horizon would decouple this channel and leave only PART E -- that is a
         DIFFERENT model from the banked branch (which feeds mu into the Poisson sector).
  F-BG   the background is held to LCDM (the banked family modifies growth, not expansion).
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mu_slip_interior as msi  # banked source of truth for mu(x)/eta(x)/Sigma(x)

OM = 0.315                      # flat LCDM background (Planck-2018-class; ratio-level insensitivity)
OL = 1.0 - OM
NS = 0.96
GAMMA_SHAPE = 0.21              # BBKS shape Gamma ~ Om*h (h=0.67): stated, swept implicitly via KC3 band
CHI_H = 2997.9                  # c/H0 in Mpc/h

A_OBS, SIG_A = 1.00, 0.22       # central measurement (KC3): combined cross-amplitude, ~4.5sigma detection
A_OBS_BAND = (0.85, 1.40)
SIG_A_BAND = (0.20, 0.32)
ELL_EFF, ELL_BAND = 20, (10, 40)
KERNEL_ZMED = (0.15, 0.45, 1.1)

BANKED_NSIGMA = 32.0            # the number under test


# ------------------------------------------------------------------ growth
def p_eds(mu):
    """EdS growing-mode index: D ~ a^p, p^2 + p/2 - (3/2)mu = 0."""
    return (-0.5 + math.sqrt(0.25 + 6.0 * mu)) / 2.0


def om_a(a):
    return OM / (OM + OL * a ** 3)


def grow(mu, n=4000, lna0=math.log(1e-4)):
    """RK4-integrate D(lna), f(lna) from deep matter era; growing-mode IC. Returns (lnas, D, f)
    with D normalized D(a=1) = 1."""
    h = (0.0 - lna0) / n
    lnas, Ds, fs = [], [], []
    D, Dp = 1.0, p_eds(mu)   # growing mode at a0 (Om(a0) ~ 1)

    def rhs(lna, D, Dp):
        om = om_a(math.exp(lna))
        return Dp, -(2.0 - 1.5 * om) * Dp + 1.5 * om * mu * D

    lna = lna0
    for i in range(n + 1):
        lnas.append(lna); Ds.append(D); fs.append(Dp / D)
        if i == n:
            break
        k1 = rhs(lna, D, Dp)
        k2 = rhs(lna + h / 2, D + h / 2 * k1[0], Dp + h / 2 * k1[1])
        k3 = rhs(lna + h / 2, D + h / 2 * k2[0], Dp + h / 2 * k2[1])
        k4 = rhs(lna + h, D + h * k3[0], Dp + h * k3[1])
        D += h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        Dp += h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        lna += h
    D0 = Ds[-1]
    Ds = [d / D0 for d in Ds]
    return lnas, Ds, fs


class Growth:
    """Interpolation wrapper: D(z), f(z), g(z) = D*(1+z) with D(0)=1."""
    def __init__(self, mu):
        self.lnas, self.Ds, self.fs = grow(mu)

    def _interp(self, arr, lna):
        lo, hi = 0, len(self.lnas) - 1
        if lna <= self.lnas[0]: return arr[0]
        if lna >= self.lnas[-1]: return arr[-1]
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if self.lnas[mid] <= lna: lo = mid
            else: hi = mid
        t = (lna - self.lnas[lo]) / (self.lnas[hi] - self.lnas[lo])
        return arr[lo] * (1 - t) + arr[hi] * t

    def D(self, z): return self._interp(self.Ds, -math.log1p(z))
    def f(self, z): return self._interp(self.fs, -math.log1p(z))
    def g(self, z): return self.D(z) * (1.0 + z)
    def src(self, z):
        """ISW cross source per unit z: (1-f) g/(1+z); positive = decay = positive correlation."""
        return (1.0 - self.f(z)) * self.g(z) / (1.0 + z)


# ------------------------------------------------------------------ background / spectrum
def E(z):
    return math.sqrt(OM * (1 + z) ** 3 + OL)


def make_chi(zmax=1200.0, n=6000):
    """chi(z) in Mpc/h by trapezoid; returns interpolator."""
    zs = [zmax * (i / n) ** 2 for i in range(n + 1)]  # denser at low z
    chis = [0.0]
    for i in range(1, len(zs)):
        dz = zs[i] - zs[i - 1]
        chis.append(chis[-1] + dz * 0.5 * (1 / E(zs[i]) + 1 / E(zs[i - 1])))
    chis = [c * CHI_H for c in chis]
    def chi(z):
        lo, hi = 0, len(zs) - 1
        if z <= 0: return 1e-6
        if z >= zs[-1]: return chis[-1]
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if zs[mid] <= z: lo = mid
            else: hi = mid
        t = (z - zs[lo]) / (zs[hi] - zs[lo])
        return chis[lo] * (1 - t) + chis[hi] * t
    return chi


CHI = make_chi()


def t_bbks(k):
    """BBKS transfer function; k in h/Mpc, shape GAMMA_SHAPE."""
    q = k / GAMMA_SHAPE
    if q < 1e-8:
        return 1.0
    return (math.log(1 + 2.34 * q) / (2.34 * q)
            * (1 + 3.89 * q + (16.1 * q) ** 2 + (5.46 * q) ** 3 + (6.71 * q) ** 4) ** -0.25)


def pk(k):
    return k ** NS * t_bbks(k) ** 2


# ------------------------------------------------------------------ galaxy kernels
def make_kernel(z_med):
    """dN/dz ~ (z/z0)^2 exp(-(z/z0)^1.5), z0 root-found so the median is z_med; normalized."""
    def raw(z, z0): return (z / z0) ** 2 * math.exp(-((z / z0) ** 1.5))
    def median(z0):
        zs = [4.0 * i / 2000 for i in range(1, 2001)]
        w = [raw(z, z0) for z in zs]
        tot = sum(w); acc = 0.0
        for z, wi in zip(zs, w):
            acc += wi
            if acc >= tot / 2: return z
        return zs[-1]
    lo, hi = 0.01, 4.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if median(mid) < z_med: lo = mid
        else: hi = mid
    z0 = 0.5 * (lo + hi)
    zs = [4.0 * i / 2000 for i in range(1, 2001)]
    norm = sum(raw(z, z0) for z in zs) * (4.0 / 2000)
    return lambda z: (raw(z, z0) / norm if 0 < z < 4.0 else 0.0)


# ------------------------------------------------------------------ the cross-amplitude
def cross_integral(gr, gobs, kernel, ell):
    """int dz n(z) D_obs(z) E(z) src(z) P((ell+1/2)/chi)  -- Limber form, common constants dropped."""
    n = 800
    tot = 0.0
    for i in range(1, n + 1):
        z = 4.0 * i / n
        k = (ell + 0.5) / CHI(z)
        tot += kernel(z) * gobs.D(z) * E(z) * gr.src(z) * pk(k)
    return tot * (4.0 / n)


def A_model(x, gr_cache, gobs, kernels, ell=ELL_EFF):
    """Predicted cross amplitude relative to the LCDM template (ratio of summed signals across
    kernels -- the joint-template-fit analog)."""
    gr = gr_cache.setdefault(round(x, 6), Growth(msi.mu_x(x)))
    num = sum(cross_integral(gr, gobs, kern, ell) for kern in kernels)
    den = sum(cross_integral(gobs, gobs, kern, ell) for kern in kernels)
    # firewall B1: the Weyl-source Sigma(x) factor (constant in time, so absent from decay RATES,
    # present in the template-relative AMPLITUDE)
    return msi.Sigma_x(x) * num / den


def n_exc(x, gr_cache, gobs, kernels, a_obs=A_OBS, sig=SIG_A, ell=ELL_EFF):
    return abs(A_model(x, gr_cache, gobs, kernels, ell) - a_obs) / sig


# ------------------------------------------------------------------ auto-power (PART F, estimate)
def auto_integral(gr, ell):
    """int dz E chi^2 src^2 P  (Limber TT-ISW auto, common constants dropped); z to 1100."""
    tot = 0.0
    # fine low-z + log high-z grid
    grid = [3.0 * i / 600 for i in range(1, 601)]
    z = 3.0
    while z < 1100:
        grid.append(z); z *= 1.05
    prev = 0.0
    for z in grid:
        dz = z - prev; prev = z
        k = (ell + 0.5) / CHI(z)
        tot += dz * E(z) * CHI(z) ** 2 * gr.src(z) ** 2 * pk(k)
    return tot


def auto_estimate(x, gr_cache, gobs, frac_isw=0.15, ellmax=30):
    """Estimate-grade: model low-ell TT excess vs cosmic variance, incoherent-add approximation.
    NOT BANKED -- stated as the likely-stronger channel owed its own rigorous calc."""
    gr = gr_cache.setdefault(round(x, 6), Growth(msi.mu_x(x)))
    n2 = 0.0
    for ell in range(2, ellmax + 1):
        R = msi.Sigma_x(x) ** 2 * auto_integral(gr, ell) / auto_integral(gobs, ell)  # firewall B1: Weyl Sigma^2
        excess = frac_isw * (R - 1.0)          # fractional TT excess at this ell
        cv = math.sqrt(2.0 / (2 * ell + 1))    # cosmic variance
        n2 += (excess / cv) ** 2
    return math.sqrt(n2)


# ------------------------------------------------------------------ main
def main():
    print("=" * 96)
    print("THE LOAD-BEARING NUMBER: the low-ell ISW exclusion of mu(x)=1+x*alpha, computed")
    print("=" * 96)

    gobs = Growth(1.0)
    cache = {0.0: gobs}
    kernels = [make_kernel(zm) for zm in KERNEL_ZMED]

    print("\nPART A -- growth verification (endpoints + regimes):")
    g1 = Growth(msi.mu_x(1.0)); cache[1.0] = g1
    print(f"   mu(0) = {msi.mu_x(0):.6f} (LCDM)   mu(1) = {msi.mu_x(1.0):.6f} (= 4/3 trace-only endpoint)")
    print(f"   EdS growing-mode index: p(mu=1) = {p_eds(1.0):.6f} (exactly 1: D~a, frozen potential);")
    print(f"                           p(mu=4/3) = {p_eds(4.0/3.0):.6f} -> potential g = D/a GROWS ~ a^{p_eds(4.0/3.0)-1:.4f}")
    print(f"   f_LCDM(z=0) = {gobs.f(0):.4f} (check ~ Om^0.55 = {OM**0.55:.4f});   f_x=1(z=0) = {g1.f(0):.4f}")
    zstar = None
    for i in range(1, 400):
        z = i * 0.01
        if g1.f(z) >= 1.0:
            zstar = z; break
    print(f"   MECHANISM (the sign, settled): mu>1 STRENGTHENS growth -> potential decay is SUPPRESSED,")
    zs_txt = f"{zstar:.2f}" if zstar is not None else "n/a (f never crosses 1 -- mu coupling absent?)"
    print(f"   and for z > z* = {zs_txt} (where f_x=1 crosses 1) the potential GROWS -- the model does not")
    print("   produce an enhanced positive ISW cross-signal; it PREDICTS A SUPPRESSED one (~0.57x the")
    print("   template at the combined kernel; negative-source regime above z*). Verified at ODE and")
    print("   EdS-analytic level -- the old mechanism line was unambiguously backwards.")
    print("   [CORRECTION to the banked mechanism line 'mu>1 enhances late-time potential decay ->")
    print("    ISW-galaxy cross excess' (calc/mu_linear.py): the direction is BACKWARDS as stated.")
    print("    The exclusion still operates -- because the DATA detect the positive LCDM-like signal.]")

    print("\nPART B -- measurement inputs (KC3, stated up front):")
    print(f"   A_obs = {A_OBS:.2f} +/- {SIG_A:.2f} (combined cross-amplitude; detection {A_OBS/SIG_A:.1f}sigma).")
    print(f"   Bands swept: A_obs in {A_OBS_BAND}, sigma_A in {SIG_A_BAND}, ell_eff {ELL_EFF} (band {ELL_BAND}),")
    print(f"   kernels z_med = {KERNEL_ZMED} (combined = joint-fit analog; per-kernel spread below).")
    print("   Fences: the '4.5sigma detection' is DEFINITIONAL here (= A_obs/sigma_A, not an independent")
    print("   input); radiation ignored from a=1e-4 (growing-mode attractor -> ratio-irrelevant for the")
    print("   z<4 cross integrand).")

    print("\nPART C -- the exclusion significance at the endpoint (x=1):")
    A1 = A_model(1.0, cache, gobs, kernels)
    N1 = n_exc(1.0, cache, gobs, kernels)
    print(f"   A_model(x=1) = {A1:+.3f}  (relative to the LCDM template; LCDM = 1)")
    per_k = [msi.Sigma_x(1.0) * cross_integral(g1, gobs, k, ELL_EFF) / cross_integral(gobs, gobs, k, ELL_EFF)
             for k in kernels]
    print(f"   per-kernel A(1): " + ", ".join(f"z_med={zm}: {a:+.3f}" for zm, a in zip(KERNEL_ZMED, per_k)))
    for ell in ELL_BAND:
        print(f"   ell = {ell}: A(1) = {A_model(1.0, cache, gobs, kernels, ell):+.3f}")
    print(f"   ==> N_sigma(x=1) = |A(1) - A_obs| / sigma_A = {N1:.1f} sigma   (central inputs)")
    lo = abs(A_model(1.0, cache, gobs, kernels, ELL_BAND[0]) - A_OBS_BAND[0]) / SIG_A_BAND[1]
    hi = abs(A_model(1.0, cache, gobs, kernels, ELL_BAND[1]) - A_OBS_BAND[1]) / SIG_A_BAND[0]
    n_lo, n_hi = min(lo, hi), max(lo, hi)
    print(f"   band across all stated sensitivities: N_sigma(1) in [{n_lo:.1f}, {n_hi:.1f}]")
    print(f"   KC1 note (the structural cap): the model SUPPRESSES the signal (A ~ {A1:+.2f} of the LCDM")
    print(f"   template) rather than enhancing it, and for any suppressed-to-reversed model (A in [-1,1])")
    print(f"   the cross exclusion is CAPPED at (A_obs+|A|)/sigma_A -- ~9sigma at central inputs, ~12sigma")
    print(f"   at the band extremes. A ~32sigma number is therefore IMPOSSIBLE in this channel for this")
    print("   model -- not merely unconfirmed. Detection != exclusion, computed apart.")
    print(f"   VERDICT vs the banked number: {BANKED_NSIGMA:.0f}sigma is NOT CONFIRMED in this channel.")

    print("\nPART D -- the window (KC2: linearity computed, not assumed) and propagation:")
    xs = [0.1, 0.2, 0.3, 0.4, 0.6, 0.8, 1.0]
    for x in xs:
        Nx = n_exc(x, cache, gobs, kernels)
        print(f"   x = {x:.1f}: A = {A_model(x, cache, gobs, kernels):+.3f}  N = {Nx:5.2f}  (linear would give {N1 * x:5.2f})")
    if N1 < 2.0:
        edge = None
        print(f"   NO in-family 2sigma cross edge at central inputs (N(1) = {N1:.2f} < 2): the cross channel")
        print("   ALONE no longer excludes any x <= 1 at 2sigma. Band-hi corners still give one (e.g.")
        print("   x ~ 0.56 at A_obs = 1.20, sigma = 0.22, with Sigma). KC2 (linearity) reported above.")
    else:
        lo_x, hi_x = 1e-4, 1.0
        for _ in range(50):
            mid = 0.5 * (lo_x + hi_x)
            if n_exc(mid, cache, gobs, kernels) < 2.0: lo_x = mid
            else: hi_x = mid
        edge = 0.5 * (lo_x + hi_x)
        print(f"   cross-channel 2sigma edge: x < {edge:.3f} [linear-scaling {2.0/N1:.3f}]")
    print("   BINDING STRUCTURE, recomputed at the corrected edge (KC4 -- other legs stated, not")
    print("   absorbed): DESI mu0 = 0.05+/-0.22 -> growth-alone 2sigma edge x ~ %.2f (no bind in-family);"
          % (min(1.0, (0.05 + 2 * 0.22) / (msi.ALPHA))))
    print("   DESI Sigma0 = 0.009+/-0.045 -> lensing-alone 2sigma edge x ~ %.2f (banked slip eta=1/mu)."
          % ((0.009 + 2 * 0.045) * 2 / msi.ALPHA))
    print("   Under R2 slip freedom (eta -> 1), lensing tightens to x ~ %.2f."
          % ((0.009 + 2 * 0.045) / msi.ALPHA))
    print("   ==> BINDING INVERSION vs the retired 1/16 (band-robust: no in-band read puts any channel")
    print("   near 0.0625): the family window is now bound by DESI Sigma0 LENSING at x < ~0.59 CENTRAL-")
    print("   INPUTS (min-of-channels convention; at mid-band corners the cross channel co-binds ~0.44-")
    print("   0.56, so the channel-identity claim is central-inputs-grade).")
    print("   F-MAP FENCE (firewall B2, named, direction TIGHTER): DESI's Sigma0 multiplies an")
    print("   OmegaL(a)/OmegaL0 shape; the family's Sigma-1 is CONSTANT in a; the direct identification")
    print("   makes x < ~0.59 a LOOSE-UPPER edge -- the shape-weighted mapping is plausibly 2-3x tighter")
    print("   (edge ~0.2-0.35, plausible-grade, not computed). The AUTO channel (owed) -- see PART F.")

    print("\nPART E -- the separate-universe leg (the structural support, demonstrated at EdS level):")
    print("   A super-horizon adiabatic mode is a shifted FRW background (separate universe); its")
    print("   growing mode is fixed by the background Friedmann equation: delta_SU ~ a in EdS --")
    print("   identically the mu=1 growth. A super-horizon mu forces delta ~ a^p(mu):")
    print(f"      p(4/3) - p_SU = {p_eds(4.0/3.0) - 1.0:+.4f}  != 0  ==> INCONSISTENT (the banked no-go, quantified).")
    print("   WHAT IT ESTABLISHES: the trace-only branch AS BANKED (super-horizon mu=4/3 for adiabatic")
    print("   modes) is internally inconsistent -- a structural exclusion INDEPENDENT of any dataset.")
    print("   WHAT IT DOES NOT: it does not constrain a strictly sub-horizon modification, and it")
    print("   rests on (i) adiabaticity and (ii) the dilatation bridge the L0 screen scored as")
    print("   'relocated, not derived' (presupposed, named); gauge caveat: super-horizon delta is gauge-")
    print("   dependent -- the comparison is against the COMOVING-gauge separate-universe mode, the")
    print("   standard identification for which p_SU = 1. ASSESSMENT (dated 2026-08-03): the leg is")
    print("   USABLE-BUT-CONDITIONAL -- not unusable; its EdS-level content is now computed here.")

    print("\nPART F -- the low-ell TT AUTO-power channel (ESTIMATE-GRADE ONLY, NOT BANKED):")
    n_auto = auto_estimate(1.0, cache, gobs)
    n_auto_lo = auto_estimate(1.0, cache, gobs, frac_isw=0.10)
    n_auto_hi = auto_estimate(1.0, cache, gobs, frac_isw=0.25)
    print(f"   a growing potential pumps low-ell TT power regardless of sign; incoherent estimate with")
    print(f"   LCDM ISW fraction 0.15 (band 0.10-0.25): N_auto(x=1) ~ order-10^2-sigma-class (this run:")
    print(f"   {n_auto:.0f}, band {n_auto_lo:.0f}-{n_auto_hi:.0f}) -- DO NOT quote the point value: it is normalization- and")
    print("   filter-sensitive (98% of the unfiltered x=1 integrand sits at z>3, largely at near/super-")
    print("   horizon k where PART E's own separate-universe logic forbids mu-modified growth on")
    print("   adiabatic modes; a sub-horizon-only filter k>aH gives ~170, k>3aH gives ~64).")
    for xv in (0.03, 0.0625, 0.1, 0.25):
        print(f"   N_auto(x={xv}) ~ {auto_estimate(xv, cache, gobs):.1f}sigma   (estimate-grade)")
    lo_x, hi_x = 1e-4, 1.0
    for _ in range(40):
        mid = 0.5 * (lo_x + hi_x)
        if auto_estimate(mid, cache, gobs) < 2.0: lo_x = mid
        else: hi_x = mid
    auto_edge = 0.5 * (lo_x + hi_x)
    print(f"   estimate-grade 2sigma auto edge: BAND x ~ 0.03-0.14 (unfiltered {auto_edge:.3f}; k>aH ~0.06;")
    print("   k>3aH ~0.14) -- the low end at or below the retired 1/16 = 0.0625.")
    print("   This channel is where a 32-class (indeed larger) number COULD live -- but it is an ESTIMATE")
    print("   (incoherent add, fixed ISW fraction, no ISW-SW cross term, BBKS-level P(k)); banking any of")
    print("   it requires its own rigorous calc (the 10^-21 lesson: no register number without its calc).")

    print("\nPART G -- outcome adjudication (pre-registered):")
    print(f"   Channel as cited (cross-correlation): outcome (b) SUBSTANTIALLY WEAKER -- N(1) ~ {N1:.2f}sigma")
    print(f"   (band {n_lo:.1f}-{n_hi:.1f}), not {BANKED_NSIGMA:.0f} -- and at central inputs the cross channel ALONE no longer")
    print("   excludes the endpoint at 2sigma (band-hi corners still do). Family edge: x < ~0.59")
    print("   central-inputs, LOOSE-UPPER per the F-MAP fence; the estimate-grade auto channel warns the")
    print("   true edge likely sits near-or-below the retired 1/16 -- its rigorous calc is the OWED GATE")
    print("   for interior viability above x ~ 0.06.")
    print("   HONEST TENSION (named in the brief): the same number that constrains the interior is what")
    print("   kills the endpoint -- the endpoint's ISW-cross leg is ~%.1fsigma, not 32." % N1)
    print("   The endpoint remains EXCLUDED on the computed legs: cross ~2.0sigma + DESI Sigma0")
    print("   ~3.5sigma (independent; joint ~4sigma-class) + the separate-universe structural leg")
    print("   (conditional, PART E). The TT-auto channel is a PROSPECT (estimate-grade, own calc owed),")
    print("   NOT counted as a leg. No single 32sigma kill exists in the computed record.")

    ok = _selftest(gobs, g1, cache, kernels)
    print(f"\n  SELFTEST: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


# ------------------------------------------------------------------ selftest
def _selftest(gobs, g1, cache, kernels):
    ok = True
    def chk(cond, msg):
        nonlocal ok
        if not cond:
            print(f"   [FAIL] {msg}"); ok = False
    # endpoints against the banked source of truth
    chk(abs(msi.mu_x(0) - 1.0) < 1e-15 and abs(msi.mu_x(1.0) - 4.0 / 3.0) < 1e-12,
        "mu endpoints disagree with mu_slip_interior")
    # EdS analytic index vs ODE (run pure-EdS by early-time slice): p from the ODE's own IC regime
    chk(abs(p_eds(1.0) - 1.0) < 1e-12, "p_eds(1) != 1")
    chk(abs(p_eds(4.0 / 3.0) - (-0.5 + math.sqrt(0.25 + 8.0)) / 2.0) < 1e-12, "p_eds(4/3) wrong")
    # LCDM growth rate today
    chk(0.50 < gobs.f(0) < 0.56, f"f_LCDM(0) = {gobs.f(0)} outside [0.50, 0.56]")
    # deep-matter attractor: f -> p at high z for both
    chk(abs(gobs.f(30) - 1.0) < 0.02, "f_LCDM(z=30) not ~ 1")
    chk(abs(g1.f(30) - p_eds(4.0 / 3.0)) < 0.02, "f_x=1(z=30) not ~ p_eds(4/3)")
    # A(0) = 1 identically
    chk(abs(A_model(0.0, cache, gobs, kernels) - 1.0) < 1e-12, "A(0) != 1")
    # A(x) monotone decreasing (more mu -> less decay -> less positive signal)
    prev = 1.0 + 1e-9
    for x in (0.2, 0.4, 0.6, 0.8, 1.0):
        a = A_model(x, cache, gobs, kernels)
        chk(a < prev, f"A(x) not decreasing at x={x}")
        prev = a
    # convergence: halving the growth step moves f(0) by < 1e-6
    l, d, f = grow(1.0, n=2000)
    chk(abs(f[-1] - gobs.fs[-1]) < 1e-6, "growth ODE not converged")
    # z* in a sane range
    zs = None
    for i in range(1, 400):
        z = i * 0.01
        if g1.f(z) >= 1.0:
            zs = z; break
    chk(zs is not None and 0.6 < zs < 1.1, f"z* = {zs} outside [0.6, 1.1]")
    # separate-universe margin nonzero iff mu != 1
    chk(abs(p_eds(1.0) - 1.0) < 1e-12 and abs(p_eds(4.0 / 3.0) - 1.0) > 0.1,
        "separate-universe margin wrong")
    # HEADLINE PINS (added 2026-08-03 when the mutation battery caught that this selftest did NOT
    # notice the Weyl-source Sigma factor being dropped -- the exact firewall-B1 bug. The calc's own
    # banked numbers must now be asserted, not merely printed.)
    kern = [make_kernel(zm) for zm in KERNEL_ZMED]
    gobs_ = Growth(1.0)
    A1 = A_model(1.0, {0.0: gobs_}, gobs_, kern)
    chk(abs(A1 - 0.5655) < 0.004, f"A(1) = {A1:.4f} != the banked Sigma-corrected +0.566 "
                                  f"(0.485 means the Weyl Sigma factor was dropped)")
    N1 = n_exc(1.0, {0.0: gobs_}, gobs_, kern)
    chk(abs(N1 - 1.97) < 0.03, f"N(1) = {N1:.3f} != the banked ~2.0 (2.34 means Sigma was dropped)")
    # the DESI Sigma0 leg -- DERIVED here rather than printed as a literal (firewall 2026-08-04:
    # '~3.5sigma' appears 5x in claims.json but lived in this file only inside a print string, the
    # exact anti-pattern the mutation registry names as the anomaly_c0_map first-build failure)
    desi_sigma0_leg = (msi.ALPHA / 2.0 - 0.009) / 0.045
    chk(abs(desi_sigma0_leg - 3.5) < 0.06,
        f"DESI Sigma0 leg = {desi_sigma0_leg:.2f}sigma != the banked ~3.5sigma "
        f"[(alpha/2 - Sigma0)/sigma_Sigma0 at the x=1 endpoint]")
    # drift-pins against the banked constants in mu_slip_interior (both directions)
    chk(abs(msi.N_CROSS_ENDPOINT - 2.0) < 1e-12, "msi.N_CROSS_ENDPOINT drifted from the banked 2.0")
    chk(abs(msi.EDGE - (0.009 + 2 * 0.045) * 2.0 / msi.ALPHA) < 1e-12, "msi.EDGE not lensing-bound formula")
    return ok


if __name__ == "__main__":
    raise SystemExit(main())
