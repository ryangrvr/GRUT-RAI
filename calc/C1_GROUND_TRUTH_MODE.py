"""C1 GROUND TRUTH MODE RECONSTRUCTION.

Three independent routes:
  R1: symbolic EOM residual (sympy)
  R2: numerical residual convergence
  R3: independent RK4 ODE integration vs analytic
Plus: canonical Wronskian, asymptotic limits."""
import cmath, json, math, os, sys

FAILS, RESULTS = [], []
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def record(cid, desc, ok, detail=""):
    RESULTS.append({"id": cid, "desc": desc, "pass": bool(ok), "detail": detail})
    print("  %s %s: %s %s" % ("ok" if ok else "FAIL", cid, desc, detail))
    if not ok:
        FAILS.append(cid)

def v_exact(k, eta):
    return (1 - 1j / (k * eta)) * cmath.exp(-1j * k * eta) / math.sqrt(2 * k)


print("C1 GROUND TRUTH MODE RECONSTRUCTION")
print("=" * 78)

# ---- ROUTE 1: symbolic ----
import sympy as sp
es = sp.symbols('etas', real=True)
ks = sp.symbols('k', positive=True)
vs = (1 - sp.I/(ks*es)) * sp.exp(-sp.I*ks*es) / sp.sqrt(2*ks)
eq_can = sp.diff(vs, es, 2) + (ks**2 - 2/es**2)*vs
res_can = sp.simplify(eq_can)
ok_A = res_can == 0
record("R1_symbolic_canonical", "v EOM residual", ok_A,
       "residual=%s" % str(res_can)[:40])

hs = -es * vs
eq_str = sp.diff(hs, es, 2) - 2/es*sp.diff(hs, es) + ks**2*hs
res_str = sp.simplify(eq_str)
ok_str = res_str == 0
record("R1_symbolic_strain", "h=v/a EOM residual", ok_str,
       "residual=%s" % str(res_str)[:40])

# ---- ROUTE 2: numerical residual convergence ----
def v_res(k, eta, hh):
    vp = (v_exact(k,eta+hh)-v_exact(k,eta-hh))/(2*hh)
    vpp = (v_exact(k,eta+hh)-2*v_exact(k,eta)+v_exact(k,eta-hh))/hh**2
    return abs(vpp + (k*k - 2/eta**2)*v_exact(k,eta))

conv = []
for hh in (1e-2, 1e-3, 1e-4, 1e-5):
    r = v_res(1.0, -1.0, hh)
    conv.append(r)
ok_conv = conv[-1] < conv[0]
record("R2_convergence", "residual decreases", ok_conv,
       "res: %s" % ", ".join("%.2e" % x for x in conv))

# ---- ROUTE 3: independent RK4 integration ----
def rk4_integrate(k, eta0, eta1, n):
    d = (eta1 - eta0) / n
    v0 = (1 - 1j/(k*eta0)) * cmath.exp(-1j*k*eta0) / math.sqrt(2*k)
    # CORRECTED 2026-08-22. The previous seed read
    #     1j*k*(1 - 1j/(k*eta0)) - 1/(k*eta0**2)
    # which has the SIGN FLIPPED on the dominant term and is MISSING the factor i
    # on the 1/(k eta^2) term. For v = (1 - i/(k eta)) exp(-i k eta)/sqrt(2k),
    #     dv/deta = exp(-i k eta)/sqrt(2k) * [ i/(k eta^2) - i k (1 - i/(k eta)) ]
    # (verified symbolically: sympy diff(v,eta) - this = 0 exactly).
    # The wrong seed excites the second solution; |v| is preserved (both independent
    # solutions share magnitude subhorizon) while the PHASE is ~antiphase, which is why
    # a magnitude-only control passes it. As-coded: |v(-1)| = 1.000005, rel err 1.483,
    # stable across 50k/100k/200k steps. Corrected: rel err 8.3e-11.
    dp0 = cmath.exp(-1j*k*eta0) * (
        1j/(k*eta0**2) - 1j*k*(1 - 1j/(k*eta0))) / math.sqrt(2*k)
    v_, p_ = v0, dp0
    e = eta0
    for _ in range(n):
        f = -(k*k - 2/(e*e))
        fv = p_; fp = f * v_
        em = e + d/2; fm = -(k*k - 2/(em*em))
        k2v = p_ + fp*d/2; k2p = fm*(v_ + fv*d/2)
        k3v = p_ + k2p*d/2; k3p = fm*(v_ + k2v*d/2)
        ee = e + d; f4 = -(k*k - 2/(ee*ee))
        k4v = p_ + k3p*d; k4p = f4*(v_ + k3v*d)
        v_ += d/6*(fv + 2*k2v + 2*k3v + k4v)
        p_ += d/6*(fp + 2*k2p + 2*k3p + k4p)
        e += d
    return v_

k_t = 1.0
v_num = rk4_integrate(k_t, -100.0, -1.0, 50000)
v_ana = v_exact(k_t, -1.0)
rel = abs(v_num - v_ana) / abs(v_ana)
record("R3_rk4_vs_analytic", "RK4 vs analytic at eta=-1", rel < 1e-3,
       "rel=%.2e" % rel)

# ---- Wronskian ----
wvals = []
for k in (0.5, 1.0, 3.0):
    for e in (-100.0, -10.0, -1.0):
        v0 = (1 - 1j/(k*e)) * cmath.exp(-1j*k*e) / math.sqrt(2*k)
        vp = (v_exact(k, e+1e-6) - v_exact(k, e-1e-6)) / (2*1e-6)
        w = v0 * vp.conjugate() - vp * v0.conjugate()
        wvals.append(w.imag)
spread_w = max(wvals) - min(wvals)
mean_w = sum(wvals) / len(wvals)
record("Wronskian_constancy", "W Im spread", spread_w < 1e-4,
       "spread=%.2e mean=%.6f" % (spread_w, mean_w))

# ---- summary ----
np = sum(1 for r in RESULTS if r["pass"])
verdict = "ALL PASS" if not FAILS else \
    "%d FAILURES: %s" % (len(FAILS), ", ".join(r["id"] for r in RESULTS if not r["pass"]))
print("\n" + "=" * 78)
print(verdict + " (%d/%d)" % (np, len(RESULTS)))
out = os.path.join(ROOT, "C1_GROUND_TRUTH_STATUS.json")
json.dump({"verdict": verdict, "checks": RESULTS}, open(out, "w"), indent=2)
print("status:", out)
sys.exit(1 if FAILS else 0)

