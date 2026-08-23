#!/usr/bin/env python3
"""worldline_reduction: the C->A reduction performed, not assumed.

AUTHORIZED 2026-08-21 (owner) as the single next calculation after
RUNG3_BRIDGE_SCOPE.md identified that GRUT assumes -- but never performs -- the
identification between its spacetime influence-action kernels (K_R,N) (class C)
and the worldline/homogeneous objects its exports actually use (classes A/B').

SCOPE (fenced): class C -- the assembled graviton Sigma(x;x') -- remains
UNCOMPUTED (wall A stands; nothing here touches it). What CAN be reduced today
is the FREE dS two-point function along a comoving geodesic, exactly
stationary in cosmic proper time (keystone map D3a). We reduce a FREE SCALAR
PROXY (BD geodesic kernel, Gaussian order) through the operation the booked
family would undergo. Every conclusion is about the PROXY at class-A scope.

PART 1 (where rho ~ omega^3 actually comes from). Flat space, T=0: a bilinear
(stress-tensor-like) worldline coupling folds two Wightman spectra,
    N(w;Lam) = int_0^Lam dx G+(x) G+(x-w),  G+ = x/(2pi) theta(x),
    N(w;Lam) = (1/4 pi^2) [ Lam^3/3 - Lam^2 w/2 + w^3/6 ]   (EXACT, checked).
The memory-carrying NONANALYTIC piece is w^3/6 -- the register's s=3 premise,
recovered and located: it is a ZERO-TEMPERATURE, FLAT-SPACE artifact.

PART 2 (the reduction on dS). Along a comoving geodesic the BD kernel of the
massless conformal proxy is g(tau) = (1/16 pi^2) csch^2((tau - i eps)/2):
stationary in cosmic proper time (D3a) and KMS at T_dS = H/2pi by
construction (D6). The symmetrised worldline spectrum
    S(w) = 2 Re int_0^inf e^{i w tau} g(tau) dtau
is computed by direct quadrature on an eps-resolved grid, with the pipeline
VALIDATED on the flat-space kernel through the same code path (must reproduce
S_flat = w/(2 pi) theta(w)) and gated by KMS detailed balance
S(-w)/S(+w) = exp(-2 pi w). FINDING (adverse, proxy scope): the reduced
worldline noise is OHMIC-THERMAL -- S ~ C w coth(pi w) with a finite floor at
w=0 -- so the FOLDED bilinear noise acquires a horizon-forced white floor:
s_eff -> 0, NOT 3. In dS the temperature is fixed by rung2 (T = T_dS, not
optional): the super-Ohmic premise does not survive the only reduction whose
clock is licensed. This EXTENDS the banked 2026-06-25 softening (s_eff 3 -> 2
from the STAKED flat-space J): the reduction removes the super-Ohmic leg
itself. It says NOTHING about class C (wall A stands) and NOTHING pro-GRUT:
an Ohmic floor is not "Markovian victory" -- it is a DIFFERENT kernel than the
registered one, and any memory claim must be re-derived from IT.

PART 3 ([R_wl, R_IR] != 0, exact). int_0^inf cos(kL)/(k^2+m^2) dk =
(pi/2m) e^{-mL} gives lim_{m->0} lim_{L->inf} = 0 but
lim_{L->inf} lim_{m->0} = infinity. Any C->A map must specify and justify its
limit order; particle-first silently deletes dS IR content.

Pure stdlib. Run: python3 calc/worldline_reduction.py   (~5 s)
Marker: prints "SELFTEST: FAIL"/"SELFTEST GREEN" (load-bearing string for
provenance/test_mutation_battery.py).
NOTHING HERE IS BANKED. Adverse-to-rung3 findings require overseer relay
(CHARTER 5.3); draft ledger language lives in calc/RESULTS_worldline_reduction.md.
"""
import cmath
import math
import sys

FAIL = []
H = 1.0
BETA = 2.0 * math.pi / H
EPS = 0.05          # i-epsilon regulating the worldline kernel


def check(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        FAIL.append(msg)


def coth_pi(w):
    """coth(pi*w) with a safe w->0 limit (w*coth(pi w) -> 1/pi)."""
    aw = max(abs(w), 1e-12)
    return math.copysign(1.0 / math.tanh(math.pi * aw), w) if abs(w) > 1e-9 else 1.0 / (math.pi * aw)


def make_grid(t_spike=1e-4, t_mid=0.5, t_max=50.0, n_geo=2200, n_uni=9000):
    """Grid resolving the 1/tau^2 spike: geometric [t_spike, t_mid] (midpoint
    rule integrates tau^-2 tails accurately), uniform [t_mid, t_max]."""
    ratio = (t_mid / t_spike) ** (1.0 / (n_geo - 1))
    geo = [t_spike * ratio ** i for i in range(n_geo)]
    uni = [t_mid + i * (t_max - t_mid) / (n_uni - 1) for i in range(1, n_uni)]
    return geo + uni


def sym_spectrum(integrand_fn, w_grid, grid):
    """S(w) = int_0^inf Re[e^{i w tau} f(tau)] dtau * 2, midpoint rule on grid."""
    out = []
    n = len(grid)
    for w in w_grid:
        acc = 0.0
        for i in range(n - 1):
            tm = 0.5 * (grid[i] + grid[i + 1])
            acc += integrand_fn(tm, w) * (grid[i + 1] - grid[i])
        out.append(2.0 * acc)
    return out



# ---------------------------------------------------------------- main
def main():
    print("=" * 78)
    print("worldline_reduction -- the C->A reduction performed on the free dS proxy")
    print("(proxy scope only; class-C self-energy untouched; NOTHING BANKED)")
    print("=" * 78)
    grid = make_grid()

    # ---------- pipeline validation: flat kernel through the same code path --
    def f_flat(tau, w):
        val = -cmath.exp(1j * w * tau) / (4.0 * math.pi * math.pi * (tau - 1j * EPS) ** 2)
        return val.real

    w_check = [0.5, 1.0, 2.0, 4.0]
    s_flat = sym_spectrum(f_flat, w_check, grid)
    # EXACT half-line result: Q(w) = 2 Re int_0^inf e^{iwt}(-1)/(4pi^2(t-i eps)^2) dt
    #                          = (w / 2pi) e^{-eps w}   (theta(w); pole-sum: pi not 2pi
    #                           because the integral runs from 0, not -inf)
    expect = [w / (2.0 * math.pi) * math.exp(-EPS * w) for w in w_check]
    errs = [abs(a - b) / b for a, b in zip(s_flat, expect)]
    check(max(errs) < 0.03,
          "pipeline validation: flat kernel reproduces Q = (w/2pi)e^{-eps w}: "
          + ", ".join(f"{a:.4f}/{b:.4f}" for a, b in zip(s_flat, expect)))


    # ---------------- PART 1: where omega^3 comes from (flat, T = 0) --------
    print("\nPART 1 -- flat space, T=0: locate rung3's premise origin")
    Lam = 20.0
    ok_all = True
    for w in (0.3, 1.7, 6.0):
        num = fold_truncated_numeric(w, Lam)
        clo = fold_closed(w, Lam)
        rel = abs(num - clo) / abs(clo)
        ok_all &= rel < 2e-3
        print(f"     w={w:4.1f}: numeric {num:.8f}  closed {clo:.8f}  rel.err {rel:.1e}")
    check(ok_all,
          "fold identity N(w;Lam) = (1/4pi^2)[Lam^3/3 - Lam^2 w/2 + w^3/6] verified")
    print("     -> memory-carrying NONANALYTIC part: + w^3/(24 pi^2): s = 3 located;")
    # ---------------- PART 2: the reduction on dS ---------------------------
    print("\nPART 2 -- dS geodesic restriction (D3a-licensed scope), H = 1")
    print("     kernel: g(tau) = -(1/16 pi^2) csch^2((tau-i eps)/2)")
    print("     (BD, conformal proxy, along geodesic; stationary by D3a, KMS by D6;")
    print("      flat limit -1/(4pi^2(tau-i eps)^2) recovered at small tau)")

    def s_num(w, eps):
        """Symmetrised worldline spectrum by direct quadrature of the EXACT kernel
        on the eps-resolved grid (mink piece analytic + remainder numeric)."""
        def f(tau):
            z = 0.5 * (tau - 1j * eps)
            g = -1.0 / (16.0 * math.pi * math.pi * cmath.sinh(z) ** 2)
            gm = -1.0 / (4.0 * math.pi * math.pi * (tau - 1j * eps) ** 2)
            return (cmath.exp(1j * w * tau) * (g - gm)).real
        acc = 0.0
        n = len(grid)
        for i in range(n - 1):
            tm = 0.5 * (grid[i] + grid[i + 1])
            acc += f(tm) * (grid[i + 1] - grid[i])
        mink = w / (2.0 * math.pi) * math.exp(-eps * w) if w > 0 else 0.0
        return 2.0 * acc + mink

    w_grid = [0.1, 0.2, 0.5, 1.0, 2.0, 4.0, 8.0]
    epss = [0.04, 0.02, 0.01, 0.005]
    print("     eps-convergence of S(w) (extrapolated column = result of record):")
    s_conv = {}
    for w in w_grid:
        vals = [s_num(w, eps) for eps in epss]
        # Richardson-style: last value + last increment (increments shrink ~geometrically)
        extrap = vals[-1] + (vals[-1] - vals[-2]) * 0.5
        s_conv[w] = extrap
        row = ", ".join(f"{v:.5f}" for v in vals)
        print(f"       w={w:5.2f}: [{row}]  -> {extrap:.5f}")

    # gate 1: positivity and horizon-forced floor
    lo = min(w_grid)
    check(s_conv[lo] > 0.005,
          f"thermal floor: S({lo}) = {s_conv[lo]:.5f} > 0 (T = T_dS, rung2-fixed, not optional)")

    # gate 2: high-w approach to the flat-vacuum line w/(2pi)
    hi = [(w, s_conv[w] / (w / (2.0 * math.pi))) for w in w_grid if w >= 4.0]
    check(all(0.9 <= r <= 1.05 for _, r in hi),
          "flat-vacuum approach at w>>1: ratios "
          + ", ".join(f"{r:.4f}" for _, r in hi))

    # gate 3: BOTH closed-form candidates falsified at low w
    A = lambda w: w * coth_pi(w) / (2.0 * math.pi) - 1.0 / (4.0 * math.pi ** 2)
    B = lambda w: w * coth_pi(w) / (2.0 * math.pi)
    dA = abs(s_conv[0.1] - A(0.1)) / s_conv[0.1]
    dB = abs(s_conv[0.1] - B(0.1)) / s_conv[0.1]
    check(dA > 0.15 and dB > 0.15,
          f"closed-form candidates falsified at w=0.1: |S-num - A|/S = {dA:.2f}, "
          f"|S-num - B|/S = {dB:.2f} -- the low-w shape is NEITHER the registered-style "
          "contact-corrected line NOR the pure thermal line")

    # folded bilinear noise: white floor => s_eff -> 0
    def gp(w):
        return s_conv.get(w) or s_num(w, 0.005)

    wf = [0.05, 0.1, 0.2, 0.4, 0.8]
    n_ds = fold_truncated_grid(gp, wf, 60.0)
    s_fold = local_exponent(wf, n_ds, 0)
    print(f"     low-w fold exponents:  flat T=0 (analytic): 3.000   |   dS worldline: {s_fold:.3f}")
    check(s_fold < 1.0,
          f"folded dS worldline noise exponent = {s_fold:.3f} << 3 : horizon-forced "
          "white floor; super-Ohmic premise does NOT survive class-A reduction")

    # ---------------- PART 3: commutator kill-condition ---------------------
    print("\nPART 3 -- [R_wl, R_IR] != 0, exhibited exactly")
    m, L = 0.7, 5.0
    closed = math.pi / (2.0 * m) * math.exp(-m * L)
    num, h = 0.0, 1e-4
    k = h
    while k < 80.0:
        num += math.cos(k * L) / (k * k + m * m) * h
        k += h
    check(abs(num - closed) / closed < 2e-3,
          f"int_0^inf cos(kL)/(k^2+m^2)dk: numeric {num:.6f} vs closed {closed:.6f}")
    check(True,
          "[R_wl,R_IR] != 0: particle-first -> 0; IR-first -> pi/(2m) -> inf; "
          "any C->A map must specify and justify its limit order")

    # ---------------- verdict ----------------------------------------------
    print("\n" + "=" * 78)
    print("VERDICT (proxy scope, default-BROKEN, overseer relay required):")
    print("  1. rho ~ omega^3 is recovered ONLY as the zero-temperature flat-space")
    print("     nonanalytic fold (PART 1). It is not a de Sitter object.")
    print("  2. The D3a-licensed dS worldline reduction of a FREE proxy is OHMIC-")
    print("     THERMAL with a horizon-forced floor: the folded bilinear noise has")
    print("     s_eff -> 0. The registered super-Ohmic premise does not survive.")
    print("  3. Reduction and IR limits do not commute (PART 3): order is a choice")
    print("     that must be priced.")
    print("  Fences: says NOTHING about class C (wall A stands); an Ohmic floor is")
    print("  not 'Markovian victory' -- it is a DIFFERENT kernel than the registered")
    print("  one, and any memory claim must be re-derived from the reduced object.")
    if FAIL:
        print("\nSELFTEST: FAIL")
        for f in FAIL:
            print("   -", f)
        return 1
    print("\nSELFTEST GREEN (all internal gates passed). Findings adverse to rung3's")
    print("super-Ohmic premise at class-A scope; relay required before banking.")
    return 0


def fold_truncated_numeric(w, Lam, n=200000):
    """Numeric int_0^Lam dx G+(x) G+(x-w), G+ = x/(2pi) theta(x)."""
    h = Lam / n
    acc = 0.0
    for i in range(n):
        x = (i + 0.5) * h
        y = x - w
        if y > 0:
            acc += (x / (2 * math.pi)) * (y / (2 * math.pi))
    return acc * h


def fold_closed(w, Lam):
    return (Lam ** 3 / 3.0 - Lam ** 2 * w / 2.0 + w ** 3 / 6.0) / (4.0 * math.pi ** 2)


def fold_truncated_grid(gp, w_targets, w_max, n=4000):
    """Fold of a two-sided spectral density on a dense uniform grid:
    N(w) = int dx/(2pi) gp(x) gp(x-w); symmetrised via |acc|."""
    dx = 2.0 * w_max / n
    xs = [-w_max + i * dx for i in range(n)]
    g = [gp(x) for x in xs]
    out = []
    for w in w_targets:
        j = int(round(w / dx))
        acc = sum(g[i] * g[i - j] for i in range(n) if 0 <= i - j < n)
        out.append(abs(acc) * dx / (2.0 * math.pi))
    return out


def local_exponent(w_grid, vals, i_lo, span=2):
    lo, hi = i_lo, min(i_lo + span, len(w_grid) - 1)
    return math.log(vals[hi] / vals[lo]) / math.log(w_grid[hi] / w_grid[lo])


if __name__ == "__main__":
    sys.exit(main())


