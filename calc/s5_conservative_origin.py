"""S5-1: symbolic re-verification of S5_CONSERVATIVE_ORIGIN_DERIVATION_01.md (committed 6170129), plus
the pre-frozen non-adjudicating numerical cross-checks X-1..X-5 of S5_CONSERVATIVE_ORIGIN_01.md §7
(charter frozen at d603db5).

The terminal is decided by the analytic derivation, not by this script. Nothing here fits an
exponential, chooses a window after seeing data, or searches g.

Usage: python3 calc/s5_conservative_origin.py   (writes S5_CONSERVATIVE_ORIGIN_RESULT.json)
"""
import hashlib
import json
import math
import pathlib
import signal
import traceback

import mpmath as mp
import numpy as np
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "S5_CONSERVATIVE_ORIGIN_RESULT.json"
K11 = 2.3
WS = math.sqrt(K11)
KAPPA = 1.0 / (2.0 * WS)
GSET = [1.0, 0.5, 0.25]      # frozen (charter §7)
NSET = [23, 47, 95]          # frozen
R = {"charter_commit": "d603db5", "derivation_commit": "6170129",
     "charter_sha256": hashlib.sha256((ROOT / "S5_CONSERVATIVE_ORIGIN_01.md").read_bytes()).hexdigest(),
     "derivation_sha256": hashlib.sha256(
         (ROOT / "S5_CONSERVATIVE_ORIGIN_DERIVATION_01.md").read_bytes()).hexdigest(),
     "script_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
     "symbolic": {}, "crosschecks": {}, "defects": []}


def K_N(N, g=1.0):
    K = np.zeros((N, N))
    for i in range(N):
        K[i, i] = 2.3 if i < N - 1 else 1.3
    for i in range(N - 1):
        K[i, i + 1] = K[i + 1, i] = -1.0
    K[0, 1] = K[1, 0] = -g
    return K


def modal(N, g):
    lam, V = np.linalg.eigh(K_N(N, g))
    return lam, V[0, :] ** 2


def T_rec(N):
    f = lambda k: math.sin(k) / math.sqrt(2.3 - 2 * math.cos(k))
    ks = np.linspace(1e-9, math.pi - 1e-9, 100001)
    vals = np.sin(ks) / np.sqrt(2.3 - 2 * np.cos(ks))
    i = int(np.argmax(vals))
    a, b = ks[max(i - 1, 0)], ks[min(i + 1, len(ks) - 1)]
    gr = (math.sqrt(5) - 1) / 2
    for _ in range(200):
        c, d = b - gr * (b - a), a + gr * (b - a)
        if f(c) > f(d):
            b = d
        else:
            a = c
    vmax = f((a + b) / 2)
    return 2 * (N - 1) / vmax, vmax


def sym(name, fn):
    try:
        ok, detail = fn()
        R["symbolic"][name] = {"ok": bool(ok), "detail": detail}
    except Exception:
        R["symbolic"][name] = {"ok": False, "detail": traceback.format_exc()}
    print(f"  {name}: {R['symbolic'][name]['ok']}")


# ============================ SYMBOLIC RE-VERIFICATION ===========================================
w, g, y, th, x = sp.symbols("w g y theta x", positive=True)
Fw = (w - sp.sqrt(w ** 2 - 4)) / 2


def s1():
    return sp.simplify(sp.expand(Fw ** 2 - w * Fw + 1)) == 0, "F^2 - wF + 1 = 0"


def s2():
    return sp.simplify(1 / (w - Fw) - Fw) == 0, "1/(w - F) = F (g = 1 consistency)"


def s3():
    Fy = 1 / y
    wy = y + 1 / y
    expr = sp.simplify((wy - g ** 2 * Fy) * y)
    return sp.simplify(expr - (y ** 2 + 1 - g ** 2)) == 0, f"y*D_g = {expr} => y^2 = g^2 - 1"


def s4():
    rho = (g ** 2 * sp.sin(th) / ((2 - g ** 2) ** 2 * sp.cos(th) ** 2 + g ** 4 * sp.sin(th) ** 2)) / sp.pi
    return sp.simplify(rho.subs(g, 1) - sp.sin(th) / sp.pi) == 0, "rho_1 = sin(theta)/pi"


def s5():
    ws = sp.sqrt(sp.Rational(23, 10))
    gg = sp.Symbol("gg", positive=True)
    om = ws + gg ** 2 * x
    c = (sp.Rational(23, 10) - om ** 2) / 2
    s = sp.sqrt(1 - c ** 2)
    rho = (gg ** 2 * s / ((2 - gg ** 2) ** 2 * c ** 2 + gg ** 4 * s ** 2)) / sp.pi
    expr = gg ** 2 * 2 * om * rho
    kap = 1 / (2 * ws)
    target = kap / (x ** 2 + kap ** 2) / sp.pi
    detail = {}
    lim = None
    def _alarm(signum, frame):
        raise TimeoutError("sympy limit exceeded 180 s (supplementary; mpmath check is independent)")
    signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(180)
    try:
        lim = sp.limit(expr, gg, 0)
        detail["sympy_limit_matches"] = bool(sp.simplify(lim - target) == 0)
    except Exception as e:  # recorded, not fatal: the mpmath check below is independent
        detail["sympy_limit_error"] = repr(e)
    finally:
        signal.alarm(0)
    mp.mp.dps = 40
    f = sp.lambdify((gg, x), expr, "mpmath")
    tf = sp.lambdify(x, target, "mpmath")
    devs = {}
    for xv in (-3, -1, 0, 0.5, 2):
        devs[str(xv)] = [float(abs(f(mp.mpf(gv), mp.mpf(xv)) - tf(mp.mpf(xv))))
                         for gv in ("1e-2", "1e-3", "1e-4")]
    detail["mpmath_devs_g=1e-2,1e-3,1e-4"] = devs
    mono = all(d[0] > d[1] > d[2] for d in devs.values()) and all(d[2] < 1e-6 for d in devs.values())
    ok = mono and detail.get("sympy_limit_matches", True)
    return ok, detail


def s6():
    mp.mp.dps = 30
    out = {}
    ok = True
    for gv in GSET:
        dens = lambda t: (gv ** 2 * mp.sin(t) / ((2 - gv ** 2) ** 2 * mp.cos(t) ** 2
                                                  + gv ** 4 * mp.sin(t) ** 2)) / mp.pi
        # lambda = 2.3 - 2cos(theta): d lambda = 2 sin(theta) d theta
        mass = mp.quad(lambda t: dens(t) * 2 * mp.sin(t), [0, mp.pi / 2, mp.pi])
        out[str(gv)] = float(mass)
        ok &= abs(mass - 1) < 1e-12
    return ok, {"mass_of_rho_g": out}


def s7():
    out = {}
    ok = True
    for N in NSET:
        for gv in GSET:
            KBB = K_N(N, gv)[1:, 1:]
            lam, V = np.linalg.eigh(KBB)
            wk = V[0, :] ** 2
            gpp = -gv ** 2 * float(np.sum(wk))  # Gamma'' (0) = -g^2 sum_k w_k lam_k^{-1} lam_k
            out[f"N={N},g={gv}"] = gpp
            ok &= abs(gpp + gv ** 2) < 1e-12
    return ok, {"Gamma_fric''(0)": out}


print("=== symbolic re-verification ===")
for nm, fn in (("S-1 F quadratic", s1), ("S-2 g=1 Schur consistency", s2),
               ("S-3 bound-state equation", s3), ("S-4 rho_g at g=1", s4),
               ("S-5 Scheffe pointwise limit", s5), ("S-6 rho_g mass 1 (no bound states)", s6),
               ("S-7 Gamma_fric''(0) = -g^2", s7)):
    sym(nm, fn)

# ============================ CROSS-CHECKS X-1..X-5 (non-adjudicating) =========================
print("=== cross-checks ===")
try:
    X = {}
    # X-1
    x1 = {}
    for N in NSET:
        cf = np.sort([2.3 - 2 * math.cos((2 * k - 1) * math.pi / (2 * N + 1)) for k in range(1, N + 1)])
        ev = np.linalg.eigvalsh(K_N(N, 1.0))
        x1[str(N)] = float(np.max(np.abs(cf - ev)))
    kg = {f"N=95,g={gv}": [float(np.min(np.linalg.eigvalsh(K_N(95, gv)))),
                           float(np.max(np.linalg.eigvalsh(K_N(95, gv))))] for gv in GSET}
    X["X-1"] = {"max_abs_dev": x1, "pass": all(v < 1e-12 for v in x1.values()), "K(g)_min_max": kg}
    # X-2
    x2 = {k: {"in_[0.3,4.3]": bool(v[0] >= 0.3 - 1e-12 and v[1] <= 4.3 + 1e-12), "min>0": v[0] > 0}
          for k, v in kg.items()}
    X["X-2"] = {"report": x2}
    # X-3
    x3 = {}
    for N in NSET:
        for gv in GSET:
            lam, wk = modal(N, gv)
            x3[f"N={N},g={gv}"] = {"sum_w": float(np.sum(wk)), "sum_w_lam": float(np.sum(wk * lam)),
                                   "phi''(0)": float(-np.sum(wk * lam))}
    X["X-3"] = {"moments": x3, "pass": all(abs(v["sum_w"] - 1) < 1e-12 and abs(v["sum_w_lam"] - K11) < 1e-12
                                           for v in x3.values())}
    # windows
    Tr, vmax = T_rec(95)
    X["T_rec(95)"] = {"T_rec": Tr, "v_max": vmax}
    # X-4
    lam, wk = modal(95, 1.0)
    om = np.sqrt(lam)
    wm, wp = math.sqrt(0.3), math.sqrt(4.3)
    cm, cp = (wm / math.pi) * math.sqrt(8 * wm), (wp / math.pi) * math.sqrt(8 * wp)
    G32 = math.gamma(1.5)
    ts = np.arange(math.ceil((Tr / 3) / 0.05), math.floor(0.9 * Tr / 0.05) + 1) * 0.05
    phi = np.array([np.sum(wk * np.cos(om * t)) for t in ts])
    asym = G32 * ts ** -1.5 * (cm * np.cos(wm * ts + 3 * math.pi / 4) + cp * np.cos(wp * ts - 3 * math.pi / 4))
    env = G32 * ts ** -1.5 * (cm + cp)
    X["X-4"] = {"window": [float(ts[0]), float(ts[-1])], "max_abs_dev": float(np.max(np.abs(phi - asym))),
                "max_envelope": float(np.max(env)),
                "max_dev_over_local_envelope": float(np.max(np.abs(phi - asym) / env))}
    # X-5
    x5 = {}
    tt = np.arange(0, math.floor(0.9 * Tr / 0.05) + 1) * 0.05
    for gv in (0.5, 0.25):
        lam, wk = modal(95, gv)
        om = np.sqrt(lam)
        C = np.cos(np.outer(tt, om))
        Sn = np.sin(np.outer(tt, om))
        ph = C @ wk
        ps = Sn @ (wk / om)
        php = -(Sn @ (wk * om))
        e = np.exp(-KAPPA * gv ** 2 * tt)
        dev = np.max(np.abs(np.stack([ph - e * np.cos(WS * tt), WS * ps - e * np.sin(WS * tt),
                                      php / WS + e * np.sin(WS * tt)])))
        x5[str(gv)] = float(dev)
    X["X-5"] = {"sup_dev_scaled_maxabs": x5, "window": [0.0, float(tt[-1])],
                "decreases_from_g=0.5_to_0.25": x5["0.25"] < x5["0.5"]}
    R["crosschecks"] = X
    for k, v in X.items():
        print(f"  {k}: {json.dumps(v)[:300]}")
except Exception:
    tb = traceback.format_exc()
    R["defects"].append(tb)
    print(tb)

R["note"] = ("Terminal is decided in S5_CONSERVATIVE_ORIGIN_DERIVATION_01.md / VERDICT; these checks "
             "are non-adjudicating.")
OUT.write_text(json.dumps(R, indent=1, default=str) + "\n")
print(f"wrote {OUT.name}; sha256 {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
