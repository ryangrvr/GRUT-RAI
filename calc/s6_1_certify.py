"""S6-1 deterministic certification instrument.

Charter: S6_1_COARSEGRAINED_ARROW_CHARTER_01.md (frozen fbd15c8), protocol P-1..P-8.
Theorem block: S6_1_THEOREM_01.md (LS-0..LS-5), verified and committed before this script.

Adjudicating arithmetic uses only mpmath interval arithmetic (iv) at 128 bits. There is no RNG,
no simulation and no floating-point grid gate. The N=95 float64 values are report-only cross-checks (P-8).

Objects (N = infinity; theorem LS-0/LS-1):
  mu = e1-spectral measure of K_inf = 2.3 - T;  lambda = 2.3 - 2cos(theta), dmu = (2/pi) sin^2(theta) dtheta.
  Families I^{c,s}_{k,w}(t) = int w lambda^{k/2} {cos,sin}(sqrt(lambda) t) dmu, with w1 = 1, w2 = 2.3 - lambda.
  Deviations (LS-1.3):
    dQ11 = (Ts/2.3) c0^2 - (Tb/r) cm^2 + (Ts-Tb) sm^2
    dP11 = (Ts/2.3) sp^2 - (Tb/r) sm^2 + (Ts-Tb) c0^2
    dC11 = -(Ts/2.3) sp c0 + (Tb/r) sm cm + (Ts-Tb) c0 sm
    dQ12 = (Ts/2.3) c0 c02 - (Tb/r) cm cm2 + (Ts-Tb) sm sm2
    J    = -(Ts/2.3) sp2 c0 + (Tb/r) sm2 cm + (Ts-Tb) c02 sm
  X_J(T) = 1.15(Q11(0)-Q11(T)) + 0.5(P11(0)-P11(T)) + Q12(T)       (LS-2.1; record convention)
  D = 0.5[Q11/(Tb r) + P11/Tb - 2 - ln((Q11 P11 - C11^2)/(Tb^2 r))],  X_sigma(T) = D(0) - D(T).

Pre-run primitive tests (charter §5.2, disclosed). These were run on NON-MEMBER mathematical controls only: no
temperature pair was evaluated.
  - The quadrature families match independent mpmath quadrature at t in {0.7, 3.3, 9.1}, within 1e-25.
  - The derivative identities d c0/dt = -sp and d sm/dt = c0 hold.
  - The jet algebra (jmul, jlog) matches sympy series.
  - The V constants and the per-box timing (about 0.2 s) were measured.
  - The theorem verifier's p40 formula matches a 2-D FFT at the non-member pairs (3,2) and (0.3,0.7).

Usage: python3 calc/s6_1_certify.py   (writes S6_1_RESULT.json)
"""
import hashlib
import json
import math
import pathlib
import time
import traceback

import mpmath
from mpmath import iv

iv.prec = 128  # P-1
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "S6_1_RESULT.json"


def sha(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


R = {"charter_commit": "fbd15c8",
     "charter_sha256": sha("S6_1_COARSEGRAINED_ARROW_CHARTER_01.md"),
     "theorem_sha256": sha("S6_1_THEOREM_01.md"),
     "script_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
     "protocol": {"prec_bits": 128, "strip_a": "1/5", "N_formula": "ceil((nu*t_max+100)/a)",
                  "h0": "1/16", "max_depth": 16, "cap_evals_per_member": 400000,
                  "V_theta_boxes": 256, "small_T_k_max": 20, "small_T_safety": "T0*M3 <= 1.5*lower(X''(0))"},
     "integrity": {}, "members": {}, "crosscheck_N95": {}, "LS3": {}, "defects": []}

# ---------------------------------------------------------------- constants (P-1)
ONE = iv.mpf(1)
PI = iv.pi
A0 = iv.mpf(23) / 10                       # K11 = 2.3
SQ129 = iv.sqrt(iv.mpf(129) / 100)
RR = (A0 - SQ129) / 2                      # r = (2.3 - sqrt 1.29)/2  (LS-0.4)
STRIP = iv.mpf(1) / 5                      # a = 1/5 (P-2)


def cosh(x):
    e = iv.exp(x)
    return (e + 1 / e) / 2


def sinh(x):
    e = iv.exp(x)
    return (e - 1 / e) / 2


ALPHA_MIN = A0 - 2 * cosh(STRIP)
NU = sinh(STRIP) / iv.sqrt(ALPHA_MIN)
LAM_MAX = A0 + 2 * cosh(STRIP)
assert (A0 - 2 * cosh(iv.mpf(1) / 4)).a > 0  # analyticity for |Im theta| < 1/4


def up(x):
    return x.b


def lo(x):
    return x.a


def s(x):
    return str(x)


def n_nodes(tmax):
    """P-2: N(t_max) = ceil((nu t_max + 100)/a), from the upper enclosure (+1 guards float rounding; conservative)."""
    val = (NU * iv.mpf(tmax) + 100) / STRIP
    return int(math.ceil(float(up(val)))) + 1


def contains(I, v):
    v = iv.mpf(v)
    return I.a <= v.b and v.a <= I.b


def tmax_of(t):
    t = iv.mpf(t)
    return max(abs(t.a), abs(t.b))


_node_cache = {}


def nodes(N):
    """Nodes theta_j = 2 pi j/N, j = 1..floor((N-1)/2). The integrand is even and 2pi-periodic, and vanishes at
    theta = 0 and pi, so sum_{j=0}^{N-1} F = 2 * sum_{j=1}^{floor((N-1)/2)} F(theta_j)."""
    if N in _node_cache:
        return _node_cache[N]
    out = []
    for j in range(1, (N - 1) // 2 + 1):
        th = 2 * PI * j / N
        lam = A0 - 2 * iv.cos(th)
        om = iv.sqrt(lam)
        wt = (2 / PI) * iv.sin(th) ** 2
        pw = {q: lam ** (iv.mpf(q) / 2) for q in range(-2, 6)}
        out.append((lam, om, wt, pw, wt * (A0 - lam)))
    _node_cache[N] = out
    return out


def quad_err(k, wkind, tmax, N):
    """P-2 rigorous trapezoid error bound 2 pi B/(e^{aN}-1)."""
    W = ONE if wkind == 1 else 2 * cosh(STRIP)
    if k < 0:
        Lk = ALPHA_MIN ** (iv.mpf(k) / 2)
    else:
        Lk = LAM_MAX ** (iv.mpf(k) / 2)
    B = (2 / PI) * cosh(STRIP) ** 2 * W * Lk * cosh(NU * iv.mpf(tmax))
    return up(2 * PI * B / (iv.exp(STRIP * N) - 1))


# base families: name -> (k, wkind, type)
FAM = {"c0": (0, 1, "c"), "c02": (0, 2, "c"), "cm": (-2, 1, "c"), "cm2": (-2, 2, "c"),
       "sm": (-1, 1, "s"), "sm2": (-1, 2, "s"), "sp": (1, 1, "s"), "sp2": (1, 2, "s")}


def families(t, order):
    """Enclosures of d^n/dt^n of every base family, n = 0..order, valid for all t in the interval t.
    d^n [lam^{k/2} cos(om t)] = lam^{(k+n)/2} cos(om t + n pi/2); similarly for sin."""
    t = iv.mpf(t)
    tmax = tmax_of(t)
    N = n_nodes(tmax)
    nd = nodes(N)
    acc = {(nm, n): iv.mpf(0) for nm in FAM for n in range(order + 1)}
    for lam, om, wt, pw, wt2 in nd:
        x = om * t
        cs, sn = iv.cos(x), iv.sin(x)
        trig_c = [cs, -sn, -cs, sn]      # cos(x + n pi/2)
        trig_s = [sn, cs, -sn, -cs]      # sin(x + n pi/2)
        for nm, (k, wk, ty) in FAM.items():
            wv = wt if wk == 1 else wt2
            for n in range(order + 1):
                tr = trig_c[n % 4] if ty == "c" else trig_s[n % 4]
                acc[(nm, n)] += wv * pw[k + n] * tr
    h = PI / N
    out = {}
    for (nm, n), v in acc.items():
        k, wk, _ = FAM[nm]
        e = quad_err(k + n, wk, tmax, N)
        out[(nm, n)] = 2 * h * v + iv.mpf([-e, e])
    return out


# ---------------------------------------------------------------- Taylor jets (coefficients a_j = f^(j)/j!)
def jconst(c, n):
    return [iv.mpf(c)] + [iv.mpf(0)] * n


def jadd(a, b):
    return [x + y for x, y in zip(a, b)]


def jscale(a, c):
    return [x * c for x in a]


def jmul(a, b):
    n = len(a)
    return [sum((a[i] * b[k - i] for i in range(k + 1)), iv.mpf(0)) for k in range(n)]


WHOLE = iv.mpf(["-inf", "inf"])


def jlog(u):
    """Series log. If the enclosure of u0 is not strictly positive, the log is undefined on part of the box:
    return the whole real line (the box is then not certified and P-3/P-4 subdivide; interval semantics)."""
    n = len(u)
    if not (u[0].a > 0):
        return [WHOLE] * n
    g = [iv.log(u[0])] + [iv.mpf(0)] * (n - 1)
    for k in range(1, n):
        acc = u[k]
        for j in range(1, k):
            acc -= iv.mpf(j) / k * g[j] * u[k - j]
        g[k] = acc / u[0]
    return g


def fam_jets(t, order):
    f = families(t, order)
    return {nm: [f[(nm, n)] / math.factorial(n) for n in range(order + 1)] for nm in FAM}


def member_consts(Ts, Tb):
    Ts, Tb = iv.mpf(Ts), iv.mpf(Tb)
    return Ts, Tb, Ts / A0, Tb / RR, Ts - Tb


def cov_jets(F, Ts, Tb, order):
    Ts, Tb, a, b, c = member_consts(Ts, Tb)
    m = jmul
    dQ11 = jadd(jadd(jscale(m(F["c0"], F["c0"]), a), jscale(m(F["cm"], F["cm"]), -b)), jscale(m(F["sm"], F["sm"]), c))
    dP11 = jadd(jadd(jscale(m(F["sp"], F["sp"]), a), jscale(m(F["sm"], F["sm"]), -b)), jscale(m(F["c0"], F["c0"]), c))
    dC11 = jadd(jadd(jscale(m(F["sp"], F["c0"]), -a), jscale(m(F["sm"], F["cm"]), b)), jscale(m(F["c0"], F["sm"]), c))
    dQ12 = jadd(jadd(jscale(m(F["c0"], F["c02"]), a), jscale(m(F["cm"], F["cm2"]), -b)), jscale(m(F["sm"], F["sm2"]), c))
    Jj = jadd(jadd(jscale(m(F["sp2"], F["c0"]), -a), jscale(m(F["sm2"], F["cm"]), b)), jscale(m(F["c02"], F["sm"]), c))
    n = order
    Q11 = jadd(jconst(Tb * RR, n), dQ11)
    P11 = jadd(jconst(Tb, n), dP11)
    C11 = dC11
    Q12 = jadd(jconst(Tb * RR * RR, n), dQ12)
    return {"dQ11": dQ11, "dP11": dP11, "dC11": dC11, "dQ12": dQ12, "J": Jj,
            "Q11": Q11, "P11": P11, "C11": C11, "Q12": Q12}


def D0_closed(Ts, Tb):
    Ts, Tb = iv.mpf(Ts), iv.mpf(Tb)
    return (Ts / (A0 * Tb * RR) + Ts / Tb - 2 - iv.log(Ts * Ts / (A0 * Tb * Tb * RR))) / 2


def X_jet(obs, sgn, Ts, Tb, t, order):
    """Jet of the forward-oriented X_f at t (t may be an interval box)."""
    F = fam_jets(t, order)
    cv = cov_jets(F, Ts, Tb, order)
    n = order
    Tsv, Tbv = iv.mpf(Ts), iv.mpf(Tb)
    if obs == "J":
        XJ = jadd(jadd(jscale(jadd(jconst(Tsv / A0, n), jscale(cv["Q11"], -1)), A0 / 2),
                       jscale(jadd(jconst(Tsv, n), jscale(cv["P11"], -1)), iv.mpf(1) / 2)), cv["Q12"])
        return jscale(XJ, sgn), cv
    det = jadd(jmul(cv["Q11"], cv["P11"]), jscale(jmul(cv["C11"], cv["C11"]), -1))
    D = jscale(jadd(jadd(jadd(jscale(cv["Q11"], 1 / (Tbv * RR)), jscale(cv["P11"], 1 / Tbv)), jconst(-2, n)),
                    jadd(jscale(jlog(det), -1), jconst(iv.log(Tbv * Tbv * RR), n))), iv.mpf(1) / 2)
    X = jadd(jconst(D0_closed(Ts, Tb), n), jscale(D, -1))
    return X, cv


# ---------------------------------------------------------------- LS-4 tail constants
def V_const(k, wkind, nbox=256):
    """V_{k,w} <= sum_i (pi/nbox) sup_{theta in box_i} |g'(theta)|, with
    g' = (2/pi)[w' lam^{(k+1)/2} sin + w (k+1) lam^{(k-1)/2} sin^2 + w lam^{(k+1)/2} cos]."""
    tot = iv.mpf(0)
    for i in range(nbox):
        th = iv.mpf([lo(PI * i / nbox), up(PI * (i + 1) / nbox)])
        sn, cs = iv.sin(th), iv.cos(th)
        lam = A0 - 2 * cs
        w = ONE if wkind == 1 else A0 - lam
        wp = iv.mpf(0) if wkind == 1 else -2 * sn
        gp = (2 / PI) * (wp * lam ** (iv.mpf(k + 1) / 2) * sn + w * (k + 1) * lam ** (iv.mpf(k - 1) / 2) * sn * sn
                         + w * lam ** (iv.mpf(k + 1) / 2) * cs)
        sup = max(abs(lo(gp)), abs(up(gp)))
        tot += iv.mpf(sup) * (PI / nbox)
    return iv.mpf(up(tot))


def tail_consts(Ts, Tb, V):
    Ts_, Tb_, a, b, c = member_consts(Ts, Tb)
    ac = abs(c)
    CQ11 = a * V[(0, 1)] ** 2 + b * V[(-2, 1)] ** 2 + ac * V[(-1, 1)] ** 2
    CP11 = a * V[(1, 1)] ** 2 + b * V[(-1, 1)] ** 2 + ac * V[(0, 1)] ** 2
    CC11 = a * V[(1, 1)] * V[(0, 1)] + b * V[(-1, 1)] * V[(-2, 1)] + ac * V[(0, 1)] * V[(-1, 1)]
    CQ12 = a * V[(0, 1)] * V[(0, 2)] + b * V[(-2, 1)] * V[(-2, 2)] + ac * V[(-1, 1)] * V[(-1, 2)]
    CJ = A0 / 2 * CQ11 + CP11 / 2 + CQ12
    CE = iv.sqrt((CQ11 / (Tb_ * RR)) ** 2 + (CP11 / Tb_) ** 2 + 2 * (CC11 / (Tb_ * iv.sqrt(RR))) ** 2)
    return {"CQ11": CQ11, "CP11": CP11, "CC11": CC11, "CQ12": CQ12, "CJ": iv.mpf(up(CJ)), "CE": iv.mpf(up(CE))}


def Xinf_closed(obs, sgn, Ts, Tb):
    Ts_, Tb_ = iv.mpf(Ts), iv.mpf(Tb)
    if obs == "J":
        return sgn * ((Ts_ - Tb_) + Tb_ * RR * RR / 2)
    return D0_closed(Ts, Tb)


def Xpp0_closed(obs, sgn, Ts, Tb):
    Ts_, Tb_ = iv.mpf(Ts), iv.mpf(Tb)
    if obs == "J":
        return sgn * Ts_ / A0
    return RR * (Tb_ / Ts_ - 1)


# ---------------------------------------------------------------- certification of one member
def certify(obs, sgn, Ts, Tb, tc, is_control):
    rec = {"obs": obs, "orientation": sgn, "Ts": str(Ts), "Tb": str(Tb), "control": is_control}
    Xinf = Xinf_closed(obs, sgn, Ts, Tb)
    X2 = Xpp0_closed(obs, sgn, Ts, Tb)
    rec["X_inf_closed"] = s(Xinf)
    rec["Xpp0_closed"] = s(X2)
    if obs == "J":
        rec["equal_temperature_offset_half_Tb_r2"] = s(iv.mpf(Tb) * RR * RR / 2)
    # P-7(ii): jet at t=0 reproduces X(0)=0, X'(0)=0, X''(0)
    j0, cv0 = X_jet(obs, sgn, Ts, Tb, iv.mpf(0), 2)
    ok0 = contains(j0[0], 0) and contains(j0[1], 0) and contains(2 * j0[2], X2)
    okcov = contains(cv0["Q11"][0], iv.mpf(Ts) / A0) and contains(cv0["P11"][0], Ts) \
        and contains(cv0["Q12"][0], 0) and contains(cv0["C11"][0], 0) and contains(cv0["J"][0], 0)
    okdq12 = contains(cv0["dQ12"][0], -iv.mpf(Tb) * RR * RR)
    rec["integrity_t0"] = {"X0,X'0,X''0": bool(ok0), "initial_covariances": bool(okcov), "dQ12(0)=-Tb r^2": bool(okdq12),
                           "jet0": [s(x) for x in j0]}
    if not (ok0 and okcov and okdq12):
        raise RuntimeError(f"P-7(ii) integrity failure for {obs} {Ts},{Tb}")
    # T-1/T-2 sign (closed form, LS-2)
    rec["X_inf_sign"] = "POSITIVE" if Xinf.a > 0 else ("NEGATIVE" if Xinf.b < 0 else "UNDETERMINED")
    # tail T*
    if obs == "J":
        Tstar = iv.sqrt(2 * tc["CJ"] / abs(Xinf))
    else:
        D0 = D0_closed(Ts, Tb)
        sq = iv.sqrt(iv.mpf(D0.a))              # lower enclosure of sqrt(D(0))
        denom = iv.mpf(0.5) if sq.a >= 0.5 else iv.mpf(sq.a)
        Tstar = iv.sqrt(tc["CE"] / denom)
    Tstar = math.ceil(float(up(Tstar)) * 1000) / 1000.0  # round up
    rec["T_star"] = Tstar
    # P-7(v): consistency at T*
    jT, cvT = X_jet(obs, sgn, Ts, Tb, iv.mpf(Tstar), 0)
    if obs == "J":
        dev = tc["CJ"] / iv.mpf(Tstar) ** 2
        okv = contains(jT[0] + iv.mpf([-dev.b, dev.b]), Xinf)
    else:
        eps = tc["CE"] / iv.mpf(Tstar) ** 2
        Dt = D0_closed(Ts, Tb) - jT[0]
        okv = Dt.a <= up(eps * eps / 2)
    rec["integrity_Tstar"] = {"X(T*)": s(jT[0]), "ok": bool(okv)}
    if not okv:
        raise RuntimeError(f"P-7(v) integrity failure for {obs} {Ts},{Tb}")
    target_sign = 1 if not is_control else -1   # controls: certify X_f < 0 on (0, T0]
    # P-3 small-T
    small = {"status": "UNRESOLVED"}
    X2lo = X2.a if target_sign == 1 else (-X2).a
    if X2lo > 0:
        for k in range(21):
            T0 = (2.0 ** (-k)) * min(1.0, Tstar)
            j3, _ = X_jet(obs, sgn, Ts, Tb, iv.mpf([0, T0]), 3)
            M3 = max(abs(lo(6 * j3[3])), abs(up(6 * j3[3])))
            if T0 * M3 <= 1.5 * X2lo:
                small = {"status": "CERTIFIED", "T0": T0, "k": k, "M3": str(M3)}
                break
    rec["small_T"] = small
    if is_control:
        rec["control_small_T_negative_certified"] = small["status"] == "CERTIFIED"
        return rec
    # P-4 main region [T0, T*]
    verdict = None
    evals = 0
    unresolved = 0
    false_at = None
    if small["status"] != "CERTIFIED":
        verdict = "UNRESOLVED"
    elif Xinf.a <= 0:
        verdict = "FALSE" if Xinf.b < 0 else "UNRESOLVED"
    else:
        T0 = small["T0"]
        h0 = 1.0 / 16
        boxes = []
        a = T0
        while a < Tstar:
            b = min(a + h0, Tstar)
            boxes.append((a, b, 0))
            a = b
        stack = list(reversed(boxes))
        while stack:
            if evals >= 400000:
                verdict = "UNRESOLVED"
                break
            a, b, dep = stack.pop()
            ja, _ = X_jet(obs, sgn, Ts, Tb, iv.mpf(a), 0)
            jb, _ = X_jet(obs, sgn, Ts, Tb, iv.mpf([a, b]), 1)
            evals += 1
            enc = ja[0] + iv.mpf([0, b - a]) * jb[1]
            if enc.a > 0:
                continue
            m = (a + b) / 2
            jm, _ = X_jet(obs, sgn, Ts, Tb, iv.mpf(m), 0)
            evals += 1
            if ja[0].b < 0:
                false_at = (a, s(ja[0]))
                break
            if jm[0].b < 0:
                false_at = (m, s(jm[0]))
                break
            if dep < 16:
                stack.append((m, b, dep + 1))
                stack.append((a, m, dep + 1))
            else:
                unresolved += 1
        if verdict is None:
            if false_at is not None:
                verdict = "FALSE"
            elif unresolved:
                verdict = "UNRESOLVED"
            else:
                verdict = "TRUE"
    rec["main"] = {"evals": evals, "unresolved_boxes": unresolved, "false_at": false_at}
    rec["K2_verdict"] = verdict
    return rec


# ---------------------------------------------------------------- run
MEMBERS = [("2", "1"), ("10", "1"), ("1/2", "1"), ("1/10", "1")]


def frac(x):
    if "/" in x:
        p, q = x.split("/")
        return iv.mpf(int(p)) / int(q)
    return iv.mpf(int(x))


t_start = time.time()
try:
    # P-7(i) moment integrity
    N = n_nodes(0)
    nd = nodes(N)
    mom = {}
    for kk in (-2, 0, 2, 4):
        acc = iv.mpf(0)
        for lam, om, wt, pw, wt2 in nd:
            acc += wt * pw[kk]
        e = quad_err(kk, 1, 0, N)
        mom[kk] = 2 * (PI / N) * acc + iv.mpf([-e, e])
    exact = {-2: RR, 0: iv.mpf(1), 2: A0, 4: iv.mpf(629) / 100}
    okm = all(contains(mom[k], exact[k]) for k in exact)
    R["integrity"]["moments"] = {str(k): {"quad": s(mom[k]), "exact": s(exact[k])} for k in mom}
    R["integrity"]["moments_ok"] = bool(okm)
    if not okm:
        raise RuntimeError("P-7(i) moment integrity failure")
    R["constants"] = {"r": s(RR), "alpha_min": s(ALPHA_MIN), "nu": s(NU), "Lambda_max": s(LAM_MAX)}
    # LS-4 V constants (P-7 iv)
    V = {}
    for kw in [(0, 1), (-2, 1), (-1, 1), (1, 1), (0, 2), (-2, 2), (-1, 2)]:
        V[kw] = V_const(*kw)
    R["V"] = {f"{k},{w}": s(v) for (k, w), v in V.items()}
    R["integrity"]["V_finite_positive"] = all(v.a > 0 for v in V.values())
    if not R["integrity"]["V_finite_positive"]:
        raise RuntimeError("P-7(iv) V constants not positive")
    # P-7(iii) derivative consistency at a few points (member (2,1))
    dc = []
    for tt in (iv.mpf(1) / 3, iv.mpf(2), iv.mpf(5)):
        jj, cv = X_jet("J", 1, frac("2"), frac("1"), tt, 1)
        J = cv["J"][0]
        dc.append(bool(contains(jj[1], J)))
    R["integrity"]["derivative_consistency_J"] = dc
    if not all(dc):
        raise RuntimeError("P-7(iii) derivative consistency failure")

    plan = []
    for Ts, Tb in MEMBERS:
        L1 = (frac(Ts) - frac(Tb)).a > 0
        sgnJ = 1 if L1 else -1
        plan.append(("J", sgnJ, Ts, Tb, not L1))       # J: target on L1, control on L2
        plan.append(("sigma", 1, Ts, Tb, L1))          # sigma: target on L2, control on L1
    for obs, sgn, Ts, Tb, ctrl in plan:
        tc = tail_consts(frac(Ts), frac(Tb), V)
        t0 = time.time()
        rec = certify(obs, sgn, frac(Ts), frac(Tb), tc, ctrl)
        rec["tail_consts"] = {k: s(v) for k, v in tc.items()}
        rec["seconds"] = round(time.time() - t0, 1)
        R["members"][f"{obs}|{Ts},{Tb}"] = rec
        print(obs, Ts, Tb, "control" if ctrl else "target", rec.get("K2_verdict"), rec.get("X_inf_sign"),
              rec["small_T"]["status"], rec["seconds"], "s", flush=True)

    # P-8 LS-3 non-degeneracy: P(t) = 1/4 ||M(t)||_F^2 at t = 0 and t = 1 (leading band-edge forms)
    G32 = iv.sqrt(PI) / 2  # Gamma(3/2)

    def lead(k, wkind, ty, t):
        tot_re = iv.mpf(0)
        for lam_e, sgn_ph in ((iv.mpf(3) / 10, 1), (iv.mpf(43) / 10, -1)):
            om = iv.sqrt(lam_e)
            w = ONE if wkind == 1 else A0 - lam_e
            A = w * lam_e ** (iv.mpf(k) / 2) * (2 * om) ** (iv.mpf(3) / 2) / (2 * iv.sqrt(PI))
            ph = om * t + sgn_ph * 3 * PI / 4
            tot_re += A * (iv.cos(ph) if ty == "c" else iv.sin(ph))
        return tot_re

    for Ts, Tb in MEMBERS:
        vals = []
        for tt in (iv.mpf(0), iv.mpf(1)):
            Fl = {nm: [lead(k, wk, ty, tt)] for nm, (k, wk, ty) in FAM.items()}
            cv = cov_jets(Fl, frac(Ts), frac(Tb), 0)
            Tb_ = frac(Tb)
            E11 = cv["dQ11"][0] / (Tb_ * RR)
            E22 = cv["dP11"][0] / Tb_
            E12 = cv["dC11"][0] / (Tb_ * iv.sqrt(RR))
            vals.append((E11 ** 2 + E22 ** 2 + 2 * E12 ** 2) / 4)
        nonconst = vals[0].b < vals[1].a or vals[1].b < vals[0].a
        R["LS3"][f"{Ts},{Tb}"] = {"P(0)": s(vals[0]), "P(1)": s(vals[1]), "P_nonconstant_certified": bool(nonconst)}

    # P-8 finite-N cross-check (float64, report-only)
    import numpy as np
    Nn = 95
    K = np.diag([2.3] * (Nn - 1) + [1.3]) - np.diag([1.0] * (Nn - 1), 1) - np.diag([1.0] * (Nn - 1), -1)
    ev, U = np.linalg.eigh(K)
    for Ts, Tb in MEMBERS:
        ts, tb = float(frac(Ts).mid), float(frac(Tb).mid)
        KBBi = np.linalg.inv(K[1:, 1:])
        Q0 = np.zeros((Nn, Nn)); Q0[0, 0] = ts / 2.3; Q0[1:, 1:] = tb * KBBi
        P0 = np.eye(Nn) * tb; P0[0, 0] = ts
        rN = np.linalg.inv(K)[0, 0]
        rows = []
        for T in (0.5, 1.0, 2.0, 4.0, 8.0):
            om = np.sqrt(ev)
            C = U @ np.diag(np.cos(om * T)) @ U.T
            S = U @ np.diag(np.sin(om * T) / om) @ U.T
            KS = U @ np.diag(om * np.sin(om * T)) @ U.T
            Q = C @ Q0 @ C + S @ P0 @ S
            P = KS @ Q0 @ KS + C @ P0 @ C
            PQ = -KS @ Q0 @ C + C @ P0 @ S
            XJ = 1.15 * (ts / 2.3 - Q[0, 0]) + 0.5 * (ts - P[0, 0]) + Q[0, 1]
            q11, p11, c11 = Q[0, 0], P[0, 0], PQ[0, 0]
            Dn = 0.5 * (q11 / (tb * rN) + p11 / tb - 2 - math.log((q11 * p11 - c11 ** 2) / (tb * tb * rN)))
            D0n = 0.5 * (ts / (2.3 * tb * rN) + ts / tb - 2 - math.log(ts * ts / (2.3 * tb * tb * rN)))
            jJ, _ = X_jet("J", 1, frac(Ts), frac(Tb), iv.mpf(T), 0)
            jS, _ = X_jet("sigma", 1, frac(Ts), frac(Tb), iv.mpf(T), 0)
            rows.append({"T": T, "XJ_N95": XJ, "XJ_inf_mid": float(jJ[0].mid), "Xsig_N95": D0n - Dn,
                         "Xsig_inf_mid": float(jS[0].mid)})
        R["crosscheck_N95"][f"{Ts},{Tb}"] = rows
except Exception:
    R["defects"].append(traceback.format_exc())
    print(R["defects"][-1])

R["seconds_total"] = round(time.time() - t_start, 1)
R["all_integrity_pass"] = not R["defects"]
OUT.write_text(json.dumps(R, indent=1, default=str) + "\n")
print("integrity pass:", R["all_integrity_pass"], "; wrote", OUT.name, "sha256",
      hashlib.sha256(OUT.read_bytes()).hexdigest(), "; total s", R["seconds_total"])
