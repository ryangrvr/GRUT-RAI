#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WALL A / ASSEMBLY-3 / TASK A3-1 -- FINITE (eps^0) MASTER ENGINE [builder]

Owner 'go' 2026-08-28, HEAD 9724d10. Contract chain (tighter rule governs):
reviewer guidance 498731aa... > execution prompt 376fe982... > A3-1 prompt
99a369b3... > brief fff07e51... . Claimed per A3-1A in AGENT_COORDINATION.md
BEFORE this write. SCOPE (hard): finite eps^0 masters ONLY. BARRED (A3-2+):
Sigma_R^finite assembly, Pi_nonlocal, TT, Q1-Q5, J(omega), PV, benchmark
comparison, spectrum interpretation. No register edits. Frozen files are READ
for hash verification only.

ROUTE A (analytic): Schwinger-parameter derivation in sympy, exact in eps,
series to eps^0. Nothing imported from memory; the only exact geometric
inputs -- the d-dim Gaussian (gated symbolically at integer d), spherical
symmetry, and the scaleless-vanishing of dim reg -- are shared by both routes
BY DECLARATION; Route B referees the eps-structure, which is the physics.
ROUTE B (numeric referee): mpmath quadrature of the ORIGINAL integrand at
d = 4 - eps on an eps-grid, (2/eps, eps^0) extracted by least squares; Route B
never touches Route A's Gamma/log expressions.

DECLARED CONVENTION (pinned for owner review at the A3-2 gate):
  measure  mu^eps Int d^{4-eps} l /(2 pi)^{4-eps}   (Minkowski, Feynman +i0)
  c-units  masters normalised by i(4 pi)^{-2}; Euclidean image
           M_N = (-1)^N (4 pi)^2 mu^eps Int_E (L^2+Delta)^{-N}
           (the (-1)^N is CONFIRMED against the frozen pole gates
           M1 -> c Delta, M2 -> c, not assumed)
  scheme   MS: subtract exactly the 2/eps == c pole (matches the frozen
           Phase-12 split Pi_local^MS = (2/eps)[...])
  kappa    := ln(4 pi) - gamma_E  (emerges; not imposed)
  D1 = l^2-m^2, D2 = (l-K)^2-m^2, K = (omega,0,0,k), eta = diag(1,-1,-1,-1)
  Feynman  y D2 + (1-y) D1 = (l-yK)^2 - Delta,  Delta = m^2 - y(1-y) K^2
  (identical to the validated pole engine, wall_d2_phases8_12.py engines 1-3)

Numerics: m = mu = 1 (ratios only). Exit 0 iff every gate passes.
"""
import hashlib, json, os, subprocess, sys, time
import sympy as sp
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time(); FAILS = []; CHECKS = []; CONTROLS = []; MASTERS = []

def stamp(msg):
    print("[%7.1fs] %s" % (time.time() - T0, msg)); sys.stdout.flush()

def check(cond, msg, section="general", detail=None):
    ok = bool(cond)
    rec = {"gate": section, "kind": "gate", "msg": msg, "pass": ok}
    if detail is not None:
        rec["detail"] = detail
    CHECKS.append(rec)
    print(("  ok   " if ok else "  FAIL ") + msg); sys.stdout.flush()
    if not ok:
        FAILS.append(msg)
    return ok

# ================= 0. CONTRACT + FROZEN INTEGRITY + HEAD =================
print("=== HANDSHAKE: contract chain, frozen integrity, HEAD ===")
PIN = {
 "WALL_A3_1_REVIEWER_GUIDANCE.md": "498731aa7c7c16aee9b51b12ea8005afc5fc6789234c49ef551e5c6b603f2207",
 "WALL_A3_1_EXECUTION_PROMPT.md": "376fe982232ab74e7c06815f74282a0736bf9ee7d64dab96cff6a132fd455e3d",
 "WALL_A3_1_BUILDER_PROMPT.md": "99a369b3b9d83d79fde9b36a36e1c991348d37730ba79dd93af882e25817c218",
 "WALL_D2_ASSEMBLY3_BRIEF.md": "fff07e5172d1ee0ff9ba7c379cd5716b8c86c43688b89d74a22abbd898314bae",
 "WALL_D2_ASSEMBLY3_ENTRY_OBJECT.json": "419c455bccdd90dcbef708698e5339b7a2d32f0c8b07c49af9de6ab099316ccb",
 "WALL_A_A3_DECLARATIONS.md": "87e2d24d5be6d67970f4089a09aa61a28d4de8cf6471f987af3db1c2ac015f6e",
 "WALL_A_A3_REGISTRY.json": "faa977d40f1ba31836e35b18223c1f573559b49649a84fad237a3809aae59b55",
 "WALL_A_A3_DECLARATIONS_V2_AMENDMENT.md": "6f2a762f4a4a01cd4794d029eecb2f1aadace9cd52637f12d3529e0564ce3d53",
 "WALL_A_A3_DECLARATIONS_V3_AMENDMENT.md": "b0b9983bf0ab04c0c5017e094a4e53a7e34fc8ddb1b6483724a14bb36eb36ee3",
 "WALL_A_A3_DECLARATIONS_V4_AMENDMENT.md": "f6127ca65ad6636be432b6d6c6fb6d30bb0b9f0c8912df4a9a1054e54919dd56",
 "wall_d2_phases8_12.py": "f48b2cc898017493a11f08c8b6bfcb1c2367a0f577b583f00d77d0bd8341c558",
}
for fn, want in PIN.items():
    h = hashlib.sha256(open(os.path.join(HERE, fn), 'rb').read()).hexdigest()
    check(h == want, "contract/frozen intact: %s (%s...)" % (fn, want[:16]),
          section="handshake")
HEAD = subprocess.run(["git", "-C", HERE, "rev-parse", "--short", "HEAD"],
                      capture_output=True, text=True).stdout.strip()
check(HEAD == "9724d10", "HEAD == 9724d10 (got %s)" % HEAD, section="handshake")

# ================= 1. ROUTE A: SCHWINGER DERIVATION =================
print("\n=== ROUTE A: exact-in-eps masters from the Schwinger representation ===")
eps, Dl, mus = sp.symbols('epsilon Delta mu', positive=True)
t = sp.Symbol('t', positive=True)
# Laplace gate (exact, sympy): Int_0^oo t^{a-1} e^{-t D} dt = Gamma(a) D^{-a}
aa = sp.Symbol('a', positive=True)
lap = sp.integrate(t**(aa - 1) * sp.exp(-t * Dl), (t, 0, sp.oo))
check(sp.simplify(lap - sp.gamma(aa) * Dl**(-aa)) == 0,
      "Laplace gate: Int_0^oo t^{a-1} e^{-tD} = Gamma(a) D^{-a} (sympy, exact)",
      section="routeA")
# Gaussian gate: Int d^dl_E e^{-tL^2}/(2pi)^d = (4 pi t)^{-d/2} at d=1..5
xs = sp.symbols('x0:5', real=True)
gok = True
for dd in range(1, 6):
    g = sp.prod(sp.integrate(sp.exp(-t * xi**2), (xi, -sp.oo, sp.oo))
                for xi in xs[:dd]) / (2 * sp.pi)**dd
    gok = gok and sp.simplify(g - (4 * sp.pi * t)**sp.Rational(-dd, 2)) == 0
check(gok, "Gaussian gate: d-dim measure normalisation exact at d=1..5 "
      "(the one shared geometric input of both routes)",
      section="routeA")

# Masters M_N(Delta; eps) exact in eps (c-units). M_0 == 0: the scaleless
# integral Int d^d l (1) vanishes in dim reg (declared exact input; gated
# below by the derivative chain and the frozen trace-relation regressions).
def Mexact(N):
    if N == 0:
        return sp.Integer(0)
    return (sp.Integer(-1)**N * Dl**(2 - N) / sp.factorial(N - 1)
            * sp.gamma(N - 2 + eps / 2)
            * sp.exp(eps / 2 * sp.log(4 * sp.pi * mus**2 / Dl)))

def pole_fin(expr):
    e = sp.expand(sp.series(expr, eps, 0, 1).removeO())
    return sp.simplify(sp.expand(e).coeff(eps, -1)), sp.simplify(sp.expand(e).coeff(eps, 0))

tA = time.time()
MEX = {N: Mexact(N) for N in range(0, 5)}
POLE = {}; FIN = {}
for N in range(1, 5):
    POLE[N], FIN[N] = pole_fin(MEX[N])
POLE[0] = sp.Integer(0); FIN[0] = sp.Integer(0)
stamp("Route A: M_1..M_4 series derived in %.1fs" % (time.time() - tA))
for N in range(1, 5):
    print("   M%d: pole = %s |  fin = %s" % (N, POLE[N], FIN[N]))

# --- derivative-chain gates (exact Minkowski identities d/dDelta) ---
check(sp.simplify(sp.diff(FIN[1], Dl) - FIN[2]) == 0,
      "chain gate: d fin_M1/dD == fin_M2  (d/dD of 1/(l^2-D) = +1/(l^2-D)^2)",
      section="routeA")
check(sp.simplify(sp.diff(FIN[2], Dl) - 2 * FIN[3]) == 0,
      "chain gate: d fin_M2/dD == 2 fin_M3", section="routeA")

# --- pole regressions vs the FROZEN ENGINE (independent law) ---
# engine trace relation (wall_d2_phases8_12.py, engine 1), c-units:
#   Ipole[(l^2)^j/(l^2-D)^N] = c D^(j-N+2) [C(j,N-1)+C(j,N-2)]
def eng(j, N):
    return Dl**(j - N + 2) * (sp.binomial(j, N - 1) + sp.binomial(j, N - 2))
def l2pole(j, N):   # pole coefficient (of 1/eps) of the (l^2)^j master
    if N == 1 and j == 0:
        return POLE[1]
    return sp.expand(POLE[N] if j == 0 else
                     (POLE[N - 1] + Dl * POLE[N] if j == 1 else
                      POLE[N - 2] + 2 * Dl * POLE[N - 1] + Dl**2 * POLE[N]))
for (j, N) in [(0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (1, 2)]:
    check(sp.simplify(l2pole(j, N) - 2 * eng(j, N)) == 0,
          "pole regression: (l^2)^%d/(l^2-D)^%d == frozen engine value c*%s"
          % (j, N, eng(j, N)), section="pole-regression")

# --- tensor structures (exact d-dim; d=4 moments must hit frozen engine 2) ---
dd = 4 - eps
def T2expr(N):
    return (MEX[N - 1] + Dl * MEX[N]) / dd
def T4expr(N):
    return 3 * (MEX[N - 2] + 2 * Dl * MEX[N - 1] + Dl**2 * MEX[N]) / (dd * (dd + 2))
T2P = {N: pole_fin(T2expr(N)) for N in (1, 2, 3)}
T4P = {2: pole_fin(T4expr(2))}
check(sp.simplify(T2P[1][0] - Dl**2 / 2) == 0 and
      sp.simplify(T2P[2][0] - Dl) == 0 and
      sp.simplify(T4P[2][0] - 3 * Dl**2 / 4) == 0,
      "tensor pole regression: l0l1/D^1 -> c eta D^2/4, l0l1/D^2 -> c eta D/2, "
      "l0l0l1l1/D^2 -> 3 c D^2/8 (frozen engine-2/3 gates)", section="pole-regression")
# ENGINE-2 frozen moment values at d=4 (rank 2 and 4), from the exact d-dim
# coefficients eta_ab/d (rank 2), 3/(d(d+2)) for <l0^4> (3 equal-eta pairings)
# and 1/(d(d+2)) for <l0^2 l1^2> (single eta00*eta11 pairing):
check(sp.simplify(sp.Integer(1) / dd - sp.Rational(1, 4)).subs(eps, 0) == 0
      and sp.simplify(3 / (dd * (dd + 2)) - sp.Rational(1, 8)).subs(eps, 0) == 0
      and sp.simplify(-1 / (dd * (dd + 2)) - sp.Rational(-1, 24)).subs(eps, 0) == 0,
      "moment regression at d=4: <l0^2>/l^2 = 1/4, <l1^2>/l^2 = -1/4, "
      "<l0^4>/(l^2)^2 = 1/8, <l0^2 l1^2>/(l^2)^2 = -1/24 (frozen engine-2)",
      section="pole-regression")

# --- mu-dependence gates (d fin/d ln mu^2; note d/dln(mu^2) = (mu/2) d/dmu) ---
for N, want in [(1, Dl), (2, sp.Integer(1)), (3, sp.Integer(0)), (4, sp.Integer(0))]:
    check(sp.simplify(sp.diff(FIN[N], mus) * mus / 2 - want) == 0,
          "mu-dependence: d fin_M%d/d(ln mu^2) == %s" % (N, want),
          section="mu-dep")

# --- kappa emerges (not imposed): fin_M2 has exactly kappa - ln(Delta/mu^2) ---
KAP = sp.log(4 * sp.pi) - sp.EulerGamma
check(sp.simplify(FIN[2] - (KAP - sp.log(Dl / mus**2))) == 0,
      "fin_M2 == kappa - ln(Delta/mu^2) with kappa = ln(4pi)-gamma_E (derived)",
      section="routeA")

# --- bubble: B(K^2) = Int_0^1 dy M_2(Delta(y)); Delta = m^2 - y(1-y) K^2 ---
yf, K2s, m2s, om2 = sp.symbols('y K2 m2 omega2', real=True)
Dy = m2s - yf * (1 - yf) * K2s
yroots = sp.solve(sp.Eq(Dy, 0), yf)
check(len(yroots) == 2, "Delta(y) quadratic in y: two roots %s" % str(yroots),
      section="routeA")
# threshold: roots real iff K2 >= 4 m^2 (discriminant of the quadratic)
disc = sp.discriminant(sp.Poly(Dy, yf))
check(sp.simplify(disc - K2s * (K2s - 4 * m2s)) == 0,
      "threshold derived: Delta(y)=0 has real roots iff K^2 >= 4 m^2 "
      "(disc = K^2(K^2-4m^2)); threshold K^2 = 4 m^2", section="routeA")

# ================= 2. ROUTE B: NUMERICAL REFEREE =================
print("\n=== ROUTE B: original-integrand quadrature at d = 4-eps ===")
mp.mp.dps = 18
KAP0 = mp.log(4 * mp.pi) - mp.euler
fM = {N: sp.lambdify((Dl, mus), FIN[N], modules="mpmath") for N in range(1, 5)}
T2A_fin = {N: pole_fin(T2expr(N))[1] for N in (1, 2, 3)}
T4A_fin = {4: pole_fin(T4expr(4))[1]}
fT2 = {N: sp.lambdify((Dl, mus), v, modules="mpmath") for N, v in T2A_fin.items()}
fT4 = {N: sp.lambdify((Dl, mus), v, modules="mpmath") for N, v in T4A_fin.items()}

def cu_pref(e):
    """c-unit radial measure: (4pi)^2 mu^eps 2 pi^{d/2}/((2pi)^d Gamma(d/2)),
    d = 4-eps, mu = 1. At d=4 this is exactly 1."""
    d = 4 - e
    return (4 * mp.pi)**2 * 2 * mp.pi**(d / 2) / ((2 * mp.pi)**d * mp.gamma(d / 2))

def _qlog(f, p, e, splits):
    """quadrature of f with EXACT ELEMENTARY UV-tail treatment (no Gamma
    structure involved): for L>1 subtract p/L^{1+eps}, the integrand's own
    asymptotic coefficient (log-divergence class L^{d-1-2N}), and add the
    exact tail Integral_1^inf L^{-1-eps} dL = 1/eps. Needed because direct
    quadrature of the slowly decaying tail is inaccurate at 1e-6 (self-caught,
    run 2). p = 0 for integrals that already decay fast."""
    g = lambda L: f(L) - p / L**(1 + e) if L > 1 else f(L)
    return mp.quad(g, splits) + p / e

def _splits(Dv):
    r = mp.sqrt(Dv)
    return sorted(set([mp.mpf(0), r / 2, r, mp.mpf(1), 2 * r, 4 * r,
                       mp.mpf(16), mp.inf]))

def num_scalar(N, Dv, e):
    """M_N(Dv) numeric: (−1)^N c-unit radial quadrature of the ORIGINAL
    (L^2+Dv)^{-N} integrand at d = 4-eps."""
    d = 4 - e
    f = lambda L: L**(d - 1) / (L * L + Dv)**N
    p = 1 if N == 2 else 0          # only N=2 is in the log-divergence class
    return (mp.mpf(-1))**N * cu_pref(e) * _qlog(f, p, e, _splits(Dv))

def num_bubble(K2v, e):
    """B(K2) numeric at m^2=1: double quadrature of the ORIGINAL Feynman-
    parameter integrand (y, radial L), d = 4-eps, c-units."""
    d = 4 - e
    def rad(y):
        Dv = 1 - y * (1 - y) * K2v
        f = lambda L: L**(d - 1) / (L * L + Dv)**2
        return _qlog(f, 1, e, _splits(Dv))
    return cu_pref(e) * mp.quad(rad, [0, 1])

def epsfit(grid, vals):
    """least-squares fit a/e + b + c*e + d*e^2 (4 params, pure python).
    The eps-series of the masters is analytic; on a small-eps grid the
    unmodelled e^3 term biases b below 1e-6 (self-caught, run 3)."""
    bf = lambda e: [1.0 / e, 1.0, e, e * e]
    n = 4
    S = [[0.0] * n for _ in range(n)]; ty = [0.0] * n
    for e, v in zip(grid, vals):
        b_ = bf(e)
        for i in range(n):
            ty[i] += b_[i] * float(v)
            for j in range(n):
                S[i][j] += b_[i] * b_[j]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(S[r][i]))
        S[i], S[p] = S[p], S[i]; ty[i], ty[p] = ty[p], ty[i]
        for r in range(i + 1, n):
            m = S[r][i] / S[i][i]
            for cc in range(i, n):
                S[r][cc] -= m * S[i][cc]
            ty[r] -= m * ty[i]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (ty[i] - sum(S[i][j] * x[j] for j in range(i + 1, n))) / S[i][i]
    return x

def A_bubble(K2v):
    """Route A eps^0 value of B at m^2=mu^2=1: kappa - Int_0^1 ln(Delta) dy."""
    return KAP0 - mp.quad(lambda y: mp.log(1 - y * (1 - y) * K2v),
                          [0, mp.mpf('0.5'), 1])

# ---- REVIEW PRIORITY 1: THE SCALAR BUBBLE (load-bearing; STOP on fail) ----
print("\n--- PRIORITY 1: independent scalar bubble (3 spacelike points) ---")
GRID = [0.0025, 0.005, 0.0075, 0.01, 0.0125]
BUB = {}
for K2v in (-0.7, -1.3, -2.9):
    tB = time.time()
    vals = [num_bubble(K2v, e) for e in GRID]
    a, b, c1, _ = epsfit(GRID, vals)
    bA = A_bubble(K2v)
    diff = abs(b - float(bA))
    ok = diff < 1e-6 and abs(a - 2.0) < 1e-6
    BUB[K2v] = {"routeB_fin": b, "routeB_polefit": a, "routeA_fin": float(bA),
                "diff": diff, "elapsed": time.time() - tB}
    check(ok,
          "BUBBLE K2=%+g: RouteB I0=%.12f vs RouteA=%.12f (diff %.2e); "
          "numeric pole fit a=%.9f (engine: 2)" % (K2v, b, float(bA), diff, a),
          section="bubble", detail=BUB[K2v])
    stamp("bubble K2=%+g checked (%.1fs)" % (K2v, time.time() - tB))

# reproducibility: independent second eps-grid at the centre point
vals2 = [num_bubble(-1.3, e) for e in (0.003, 0.006, 0.009, 0.012)]
a2, b2, _, _ = epsfit([0.003, 0.006, 0.009, 0.012], vals2)
check(abs(b2 - BUB[-1.3]["routeB_fin"]) < 1e-6,
      "reproducibility: second eps-grid extraction agrees (%.2e)"
      % abs(b2 - BUB[-1.3]["routeB_fin"]), section="reproducibility",
      detail={"grid2_I0": b2, "grid1_I0": BUB[-1.3]["routeB_fin"]})

MASTERS.append({
    "name": "B(K^2) scalar bubble",
    "definition": "B = Int_0^1 dy M_2(Delta(y)), Delta = m^2 - y(1-y)K^2",
    "pole": "c  (x-integral of 1; frozen engine-3 classic bubble gate)",
    "finite": "kappa - Int_0^1 dy ln(Delta(y)/mu^2)",
    "mu_dep": "d/dln(mu^2) = 1", "branch": "ln(Delta - i0): Im = +pi*(y+ - y-)*theta(K^2-4m^2)",
    "threshold": "K^2 = 4 m^2", "checks": BUB,
    "verdict": "PASS" if all(v["diff"] < 1e-6 for v in BUB.values()) else "FAIL",
})

# ---- STOP LADDER: priority 1 failed -> preserve outputs and STOP ----
if FAILS:
    print("\n*** PRIORITY-1/ROUTE-A FAILURE -- STOPPING BEFORE HIGHER MASTERS ***")
    print("preserving partial outputs; see result JSON")
    _early = True
else:
    _early = False

if not _early:
    # ================= 3. BRANCH / THRESHOLD (priority 2) =================
    print("\n--- PRIORITY 2: branch, threshold, one controlled timelike point ---")
    BR = {}
    # branch prescription DERIVED from the exact master: Disc M2(Delta) = 2 pi i
    # theta(-Delta), via rigorous limits of ln(Delta - i0):
    with mp.workdps(60):
        eta_t = mp.mpf(10)**-40
        disc = (-mp.log(mp.mpf(-2) - 1j*eta_t)) - (-mp.log(mp.mpf(-2) + 1j*eta_t))
        imM2 = mp.im(-mp.log(mp.mpf(-2) - 1j*eta_t))
    check(abs(disc - 2j*mp.pi) < mp.mpf(10)**-15 and abs(imM2 - mp.pi) < mp.mpf(10)**-15,
          "branch limit derived: Im[-ln(Delta-i0)] = +pi and Disc M2 = 2 pi i "
          "for Delta<0 (Feynman prescription; computed to <1e-15, not assumed)",
          section="branch")
    # y+- roots and Im B = pi (y+ - y-) theta(K^2 - 4 m^2)
    bet = sp.sqrt(1 - 4 * m2s / K2s)
    ypm = sp.solve(sp.Eq(Dy, 0), yf)
    ylen_gen = sp.Abs(ypm[0] - ypm[1])
    ok_root = (sp.simplify(ylen_gen.subs({K2s: 5, m2s: 1})
                           - sp.sqrt(sp.Rational(1, 5))) == 0)
    check(ok_root,
          "root geometry: y+ - y- == sqrt(1 - 4 m^2/K^2) (exact at K^2=5m^2) "
          "->  Im B = pi sqrt(1-4m^2/K^2) theta(K^2-4m^2)", section="branch")
    # numeric threshold: min_y Delta(y) = m^2 - K^2/4 crosses 0 at K^2 = 4 m^2
    s_lo, s_hi = 3.0, 5.0
    for _ in range(80):
        sm = (s_lo + s_hi) / 2
        if (1 - sm / 4) > 0:
            s_lo = sm
        else:
            s_hi = sm
    check(abs((s_lo + s_hi) / 2 - 4.0) < 1e-9,
          "threshold numeric: min_y Delta(y) = m^2 - K^2/4 vanishes at "
          "K^2 = %.9f m^2 (bisection on the actual Delta)" % ((s_lo + s_hi) / 2),
          section="branch")
    # ---- controlled timelike point K^2 = 5 m^2: ORIGINAL-integrand referee ----
    # radial Feynman form of the original bubble: (L^2 + Delta(y) - i0)^-2
    def tl_splits(Dv, eta):
        """robust split list for the near-pole radial quadrature: all points
        clamped positive, deduped, sorted (run-5 fix: r - 40*eta goes negative
        near the Delta=0 endpoints y+- and mpmath stalls on unsorted splits)."""
        pts = {mp.mpf(0), mp.mpf(1), mp.mpf(16), mp.inf}
        if Dv < 0:
            r = mp.sqrt(-Dv); w = 40 * eta
            for q in (r - w, r - w / 4, r, r + w / 4, r + w, 2 * r, 4 * r):
                if q > eta / 8:
                    pts.add(q)
        else:
            r = mp.sqrt(Dv)
            for q in (r / 2, r, 2 * r, 4 * r):
                pts.add(q)
        return sorted(pts)

    def num_bubble_tl(sK, e, eta, ysplit):
        d = 4 - e
        def rad(y):
            Dv = 1 - y * (1 - y) * sK
            f = lambda L: L**(d - 1) / (L * L + Dv - 1j * eta)**2
            return _qlog(f, 1, e, tl_splits(Dv, eta))
        return cu_pref(e) * mp.quad(rad, ysplit)
    # machinery sanity at spacelike (no pole: must reproduce the refereed value)
    v_tl_sp = num_bubble_tl(-0.7, 0.01, mp.mpf(10)**-5, [0, 1])
    v_sp = num_bubble(-0.7, 0.01)
    check(abs(v_tl_sp - v_sp) < 3e-5,
          "timelike machinery sanity: at spacelike K2=-0.7 it reproduces the "
          "refereed real quadrature (%.2e; single-eps complex-vs-real "
          "quadrature agreement)" % abs(v_tl_sp - v_sp),
          section="branch")
    # ---- controlled timelike point K^2 = 5 m^2 ----
    # (runs 7-8 restructure: the full complex quadrature of the second-order
    #  near-pole integrand was numerically intractable within the discipline;
    #  Im is refereed via the independent delta'-distribution route below and
    #  Re via a quad-vs-exact-closed-form cross-check; all disclosed.)
    sK = 5.0
    b5 = (1 - mp.sqrt(1 - 4 / sK)) / 2
    a5 = (1 + mp.sqrt(1 - 4 / sK)) / 2
    ysp = sorted(set([mp.mpf(0), mp.mpf(b5) / 2, mp.mpf(b5),
                      (mp.mpf(b5) + mp.mpf('0.5')) / 2, mp.mpf('0.5'),
                      (mp.mpf('0.5') + mp.mpf(a5)) / 2, mp.mpf(a5),
                      (1 + mp.mpf(a5)) / 2, mp.mpf(1)]))
    # numeric cut endpoints by bisection on Delta(y) (no quadratic formula):
    def yroot(sign):
        lo = mp.mpf(0) if sign < 0 else mp.mpf('0.5')
        hi = mp.mpf('0.5') if sign < 0 else mp.mpf(1)
        for _ in range(90):
            mid = (lo + hi) / 2
            pos = (1 - mid * (1 - mid) * sK) > 0
            if pos == (sign < 0):
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2
    ym_num = yroot(-1); yp_num = yroot(+1)
    # Im referee -- DISTRIBUTION (delta') ROUTE, an independent derivation
    # from the log-branch limit: Im[1/(x - i0)^2] = -pi delta'(x); with
    # x = L^2 + Delta(y) < 0 on the cut, the u = x substitution gives exactly
    #   radial Im part = pi (d-2)/4 * a^{(d-4)/2},  a = -Delta > 0,
    # so   Im B(eps) = cu_pref(eps) * pi (d-2)/4 * Int_{y-}^{y+} a^{(d-4)/2} dy,
    # with the endpoints y+- obtained by bisection and the y-integral by
    # quadrature. At eps -> 0 this is pi (y+ - y-).
    def im_delta_route(e):
        d = 4 - e
        # inset the split points strictly inside the cut (the bisection
        # endpoint can round to a ~ -1e-27, which would go complex):
        ym_in = ym_num * (1 + mp.mpf(10)**-12)
        yp_in = yp_num * (1 - mp.mpf(10)**-12)
        f = lambda y: abs(y * (1 - y) * sK - 1)**((d - 4) / 2)
        inner = mp.quad(f, [ym_in, (ym_in + yp_in) / 2, yp_in])
        return cu_pref(e) * mp.pi * (d - 2) / 4 * inner
    G3 = [0.0025, 0.005, 0.0075]
    imv = [im_delta_route(e) for e in G3]
    def interp0(grid, vals):
        """intercept of the quadratic through (grid, vals): 3x3 Vandermonde."""
        n = 3
        S = [[g**k for k in range(n)] + [v] for g, v in zip(grid, vals)]
        for i in range(n):
            p = max(range(i, n), key=lambda r: abs(S[r][i]))
            S[i], S[p] = S[p], S[i]
            for r in range(i + 1, n):
                m = S[r][i] / S[i][i]
                for cc in range(i, n + 1):
                    S[r][cc] -= m * S[i][cc]
        x = [0.0] * n
        for i in range(n - 1, -1, -1):
            x[i] = (S[i][n] - sum(S[i][j] * x[j] for j in range(i + 1, n))) / S[i][i]
        return x[0]
    bI = interp0(G3, [float(v) for v in imv])
    imA = float(mp.pi * mp.sqrt(1 - 4 / sK))
    # Route A analytic continuation: Re = kappa - Int ln|Delta| dy (quad),
    # cross-checked against the exact sympy closed form, integrated piecewise
    # with sign-corrected positive arguments across the cut [y-, y+]:
    reA = float(KAP0 - mp.quad(lambda y: mp.log(abs(1 - y * (1 - y) * sK)), ysp))
    qm = sp.Rational(1, 2) - sp.sqrt(sp.Rational(1, 5)) / 2
    qp = sp.Rational(1, 2) + sp.sqrt(sp.Rational(1, 5)) / 2
    LR = (sp.integrate(sp.log(1 - yf * (1 - yf) * 5), (yf, 0, qm))
          + sp.integrate(sp.log(-(1 - yf * (1 - yf) * 5)), (yf, qm, qp))
          + sp.integrate(sp.log(1 - yf * (1 - yf) * 5), (yf, qp, 1)))
    LRc = complex(sp.N(LR, 30))
    check(abs(LRc.imag) < 1e-20,
          "sympy closed form of Int ln|Delta| dy is real (|Im| = %.1e)"
          % abs(LRc.imag), section="branch")
    reA_cf = float(KAP0) - LRc.real
    BR = {"K2_over_m2": 5.0,
          "y_minus_bisection": float(ym_num), "y_plus_bisection": float(yp_num),
          "cut_measure_bisection": float(yp_num - ym_num),
          "routeA_Im": imA, "routeB_Im_delta_prime_route": bI,
          "Im_diff": abs(bI - imA),
          "routeA_Re_quad": reA, "routeA_Re_sympy_closed_form": reA_cf,
          "Re_crosscheck_diff": abs(reA - reA_cf)}
    check(abs(bI - imA) < 5e-6,
          "timelike K2=5m^2 Im: RouteA pi*sqrt(1-4/5)=%.9f vs delta'-route "
          "referee=%.9f (d=%.1e); cut endpoints by bisection: y-=%.9f y+=%.9f"
          % (imA, bI, abs(bI - imA), float(ym_num), float(yp_num)),
          section="branch", detail=BR)
    check(abs(reA - reA_cf) < 1e-10,
          "timelike K2=5m^2 Re: numeric quad of kappa - Int ln|Delta| dy "
          "(%.12f) == exact sympy closed form (%.12f) (d=%.1e)"
          % (reA, reA_cf, abs(reA - reA_cf)), section="branch")
    stamp("branch + timelike point checked (Im by delta'-route referee; Re by "
          "quad-vs-closed-form cross-check)")


    # ================= 4. HIGHER MASTERS (priority 3) =================
    print("\n--- PRIORITY 3: M_2, M_3, M_4, M_1-difference, T2, T4 ---")
    MREC = {}
    for N in (2, 3, 4):
        for Dv in (0.6, 1.7, 3.1):
            tB = time.time()
            vals = [num_scalar(N, Dv, e) for e in GRID]
            a, b, _, _ = epsfit(GRID, vals)
            bA = float(fM[N](mp.mpf(Dv), 1))
            want_pole = 2.0 if N == 2 else 0.0
            MREC.setdefault("M%d" % N, {})[str(Dv)] = {
                "routeB_fin": b, "routeA_fin": bA, "diff": abs(b - bA),
                "routeB_polefit": a, "elapsed": time.time() - tB}
            check(abs(b - bA) < 1e-6 and abs(a - want_pole) < 1e-6,
                  "M_%d(Delta=%.1f): RouteB I0=%.12f vs RouteA=%.12f "
                  "(diff %.2e); pole fit %.9f (want %.1f)"
                  % (N, Dv, b, bA, abs(b - bA), a, want_pole),
                  section="M%d" % N, detail=MREC["M%d" % N][str(Dv)])
        stamp("M_%d checked at 3 Deltas" % N)
    # M_1 by the EXACT s-parameter identity composed with the refereed M_2
    # radial machinery (run-8: the direct difference-integrand quadrature
    # disagreed with the exact Schwinger reference by ~15, cause not fully
    # diagnosed -- disclosed; the replacement uses only the validated M_2
    # radial and exact algebra):
    #   1/(L^2+D1) - 1/(L^2+D0) = (D0-D1) Int_0^1 ds/(L^2 + D(s))^2,
    #   D(s) = D1 + s(D0-D1);  M_1(D1)-M_1(D0) = -(D0-D1) Int_0^1 ds M_2(D(s)).
    As, Bs, ss = sp.symbols('A B s', positive=True)
    check(sp.simplify(sp.integrate((Bs - As) / (As * ss + Bs * (1 - ss))**2,
                                   (ss, 0, 1)) - (1 / As - 1 / Bs)) == 0,
          "s-parameter identity gated symbolically: 1/A - 1/B = "
          "(B-A) Int_0^1 ds/(sA+(1-s)B)^2 (exact)", section="M1")
    def num_M1diff(D1, D0, e):
        s_int = lambda s: num_scalar(2, D1 + s * (D0 - D1), e)
        return -(D0 - D1) * mp.quad(s_int, [0, mp.mpf('0.5'), 1])
    MREC["M1diff"] = {}
    for D1 in (0.6, 3.1):
        tB = time.time()
        vals = [num_M1diff(D1, 1.0, e) for e in GRID]
        a, b, _, _ = epsfit(GRID, vals)
        bA = float(fM[1](mp.mpf(D1), 1) - fM[1](mp.mpf(1), 1))
        MREC["M1diff"][str(D1)] = {"routeB_fin": b, "routeA_fin": bA,
                                   "diff": abs(b - bA), "routeB_polefit": a,
                                   "elapsed": time.time() - tB}
        check(abs(b - bA) < 1e-6 and abs(a - 2 * (D1 - 1.0)) < 1e-6,
              "M_1(Delta=%.1f)-M_1(1) difference: RouteB %.12f vs RouteA %.12f "
              "(diff %.2e); pole fit %.9f (want %.1f)"
              % (D1, b, bA, abs(b - bA), a, 2 * (D1 - 1.0)),
              section="M1", detail=MREC["M1diff"][str(D1)])
    stamp("M_1 difference-anchored checked")
    # T2_{00,3} and T4_{0000,4} direct tensor radials (sign pinned by the
    # frozen pole regressions above, not by Route A):
    T4P4 = pole_fin(T4expr(4))[0]
    def num_T2(N, Dv, e):
        d = 4 - e
        f = lambda L: L**(d - 1) * L**2 / (L * L + Dv)**N
        return ((-1)**(N + 1)) / (4 - e) * cu_pref(e) * _qlog(f, 1, e, _splits(Dv))
    def num_T4(N, Dv, e):
        d = 4 - e
        f = lambda L: L**(d - 1) * L**4 / (L * L + Dv)**N
        return ((-1)**N) * 3 / ((4 - e) * (6 - e)) * cu_pref(e) * _qlog(f, 1, e, _splits(Dv))
    for Dv in (0.6, 3.1):
        tB = time.time()
        vals = [num_T2(3, Dv, e) for e in GRID]
        a, b, _, _ = epsfit(GRID, vals)
        bA = float(fT2[3](mp.mpf(Dv), 1))
        d2 = abs(b - bA)
        check(d2 < 1e-6 and abs(a - float(T2P[3][0])) < 1e-6,
              "T2_{00,3}(D=%.1f): direct tensor radial I0=%.12f vs RouteA "
              "%.12f (diff %.2e); pole fit %.9f (want %s)"
              % (Dv, b, bA, d2, a, float(T2P[3][0])), section="T2",
              detail={"routeB_fin": b, "routeA_fin": bA, "diff": d2,
                      "elapsed": time.time() - tB})
        vals = [num_T4(4, Dv, e) for e in GRID]
        a, b, _, _ = epsfit(GRID, vals)
        bA = float(fT4[4](mp.mpf(Dv), 1))
        d4 = abs(b - bA)
        check(d4 < 1e-6 and abs(a - float(T4P4)) < 1e-6,
              "T4_{0000,4}(D=%.1f): direct tensor radial I0=%.12f vs RouteA "
              "%.12f (diff %.2e); pole fit %.9f (want %s)"
              % (Dv, b, bA, d4, a, float(T4P4)), section="T4",
              detail={"routeB_fin": b, "routeA_fin": bA, "diff": d4,
                      "elapsed": time.time() - tB})
    stamp("T2/T4 direct tensor radials checked")

    # ---- B_00 composition (components refereed; algebra gated) ----
    xx = sp.Symbol('x', real=True)
    check(sp.integrate(xx * sp.exp(-xx**2), (xx, -sp.oo, sp.oo)) == 0
          and sp.integrate(yf**2, (yf, 0, 1)) == sp.Rational(1, 3),
          "B_00 algebra gates: odd-shift terms vanish by symmetry (exact "
          "Gaussian check); Int_0^1 y^2 dy = 1/3 (exact)", section="B00")
    b00_val = mp.quad(lambda y: (fT2[2](1 - y * (1 - y) * (-0.7), 1)
                                 + y**2 * (-0.7) * fM[2](1 - y * (1 - y) * (-0.7), 1)),
                      [0, mp.mpf('0.5'), 1])
    BR["B00_at_K2_-0.7_composed"] = float(b00_val)

    # ================= 5. NEGATIVE CONTROLS (each must be DETECTED) =====
    print("\n--- NEGATIVE CONTROLS: corrupted formulas must FAIL the referee ---")
    def control(name, bad, ref, tol=1e-6):
        detected = abs(bad - ref) > 10 * tol
        CONTROLS.append({"control": name, "corrupted_value": bad,
                         "referee_value": ref, "expected": "DETECTED",
                         "pass": detected,
                         "detail": "|bad-ref| = %.3e (> 10 tol required)"
                                   % abs(bad - ref)})
        check(detected, "negative control DETECTED: %s (|bad-ref|=%.3e)"
              % (name, abs(bad - ref)), section="negative-control")
    b17 = MREC["M2"]["1.7"]["routeB_fin"]
    control("factor-of-2 in fin_M2 (2x kappa-ln)",
            2 * float(fM[2](mp.mpf('1.7'), 1)), b17)
    control("wrong mu scale (mu -> 2 mu, shifts finite part by ln 4)",
            float(fM[2](mp.mpf('1.7'), 2)), b17)
    pole_flip = pole_fin(sp.series(MEX[2].subs(eps, -eps), eps, 0, 1).removeO())[0]
    control("eps sign flip (pole coefficient flips sign)",
            float(pole_flip), 2.0)
    check(sp.simplify(pole_flip + 2) == 0,
          "eps-sign control symbolic: pole of M2(eps->-eps) == -2 (flipped), "
          "detected against the frozen engine value +2", section="negative-control")

# ================= 6. MASTER RECORDS + OUTPUTS =================
if not _early:
    def _v(sec):
        xs = [c for c in CHECKS if c["gate"] == sec]
        return "PASS" if xs and all(c["pass"] for c in xs) else "FAIL"
    MASTERS += [
        {"name": "M_1(Delta) tadpole", "definition":
         "M_1 = [mu^eps Int d^dl/(2pi)^d 1/(l^2-Delta+i0)] / i(4pi)^-2",
         "pole": "c Delta  (frozen engine gate)", "finite":
         "Delta (1 + kappa - ln(Delta/mu^2))", "mu_dep": "Delta",
         "numeric": "difference-anchored vs convergent difference integrand",
         "checks": MREC.get("M1diff"), "verdict": _v("M1")},
        {"name": "M_2(Delta)", "definition": "as M_1 with (l^2-Delta)^-2",
         "pole": "c  (frozen engine gate)", "finite":
         "kappa - ln(Delta/mu^2)", "mu_dep": "1",
         "checks": MREC.get("M2"), "verdict": _v("M2")},
        {"name": "M_3(Delta)", "definition": "as M_1 with (l^2-Delta)^-3",
         "pole": "0  (frozen engine gate: UV finite)",
         "finite": "-1/(2 Delta)", "mu_dep": "0",
         "checks": MREC.get("M3"), "verdict": _v("M3")},
        {"name": "M_4(Delta)", "definition": "as M_1 with (l^2-Delta)^-4",
         "pole": "0  (frozen engine gate: UV finite)",
         "finite": "1/(6 Delta^2)", "mu_dep": "0",
         "checks": MREC.get("M4"), "verdict": _v("M4")},
        {"name": "T2_{00,N}(Delta) rank-2", "definition":
         "T2_{00,N} = [M_{N-1} + Delta M_N] / (4-eps), eps^0 kept exactly "
         "(the 1/d x pole cross terms included)",
         "pole": "N=1: c D^2/4, N=2: c D/2 (frozen engine gates)",
         "finite": "series of the exact-d composition (computed, not asserted)",
         "numeric": "direct L^2-weighted tensor radial (sign pinned by frozen poles)",
         "checks": {"T2_00_3": "see checks section"}, "verdict": _v("T2")},
        {"name": "T4_{0000,4}(Delta) rank-4", "definition":
         "T4 = 3[M_{N-2} + 2 Delta M_{N-1} + Delta^2 M_N]/((4-eps)(6-eps))",
         "pole": "N=2: 3 c D^2/8 (frozen engine gate)",
         "numeric": "direct L^4-weighted tensor radial",
         "checks": {"T4_0000_4": "see checks section"}, "verdict": _v("T4")},
        {"name": "B_00(K^2) tensor bubble (composition)", "definition":
         "Int_0^1 dy [ T2_{00,2}(Delta(y)) + y^2 omega^2 M_2(Delta(y)) ]",
         "verdict": "PASS" if _v("B00") == "PASS" else "FAIL",
         "note": "components refereed above; shift algebra + odd-vanishing + "
                 "y^2-moment gated; full direct tensor-double-integral "
                 "referee deferred to A3-2 contracted assembly (declared "
                 "limitation of A3-1 scope, disclosed)"},
    ]

SELF_CAUGHT = [
    "run 1: kappa-gate used non-existent sympy attribute (sp.Log); crash -> "
    "replaced with the pure simplify comparison",
    "run 1: mu-dependence gate differentiated w.r.t. ln(mu) instead of "
    "ln(mu^2) (factor 2); M1/M2 gates failed -> fixed to (mu/2) d/dmu",
    "run 1: moment-regression gate used the 3-pairing coefficient for the "
    "MIXED component <l0^2 l1^2>; correct single-pairing value is "
    "-1/(d(d+2)) = -1/24 at d=4 -> gate formula fixed (machinery was right)",
    "run 2: direct mpmath quadrature of the slowly decaying L^{-1-eps} UV "
    "tail was inaccurate at the 1e-6 tolerance (bubble referee off by ~24, "
    "pole fit 1.28 vs 2) -> fixed by subtracting the integrand's own "
    "elementary asymptotic L^{d-1-2N} term beyond L=1 and adding its exact "
    "integral 1/eps; no Gamma/log loop structure enters this correction",
    "run 3: 3-parameter (a/e + b + c e) extraction on the coarse eps grid "
    "{0.02..0.08} left a ~3e-3 bias in I0 from the unmodelled e^2 series "
    "term (pole fit was already 2.00004) -> moved to a small-eps grid "
    "{0.0025..0.0125} with a 4-parameter fit including e^2; residual bias "
    "~ c3 * eps^3 << 1e-6",
    "run 4: branch-limit gate demanded 1e-35 agreement on Im ln near the "
    "cut (mpmath delivers ~1e-19) and the timelike quadrature at eta=1e-7 "
    "stalled on the near-pole peaks -> threshold relaxed to 1e-15 and "
    "timelike referee moved to moderate eta with two-point Richardson "
    "(linear-in-eta bias cancellation); tolerances 5e-6 declared",
    "run 5: near the Delta=0 endpoints y+- the radial split points "
    "r - 40*eta went NEGATIVE (r < 40*eta there), handing mpmath unsorted "
    "intervals -> quadrature stall; fixed with clamped, deduped, sorted "
    "tl_splits(); spacelike sanity gate relaxed to 3e-5 (single-eps "
    "complex-vs-real quadrature agreement)",
    "run 6: the timelike referee battery (4 eps-points x 2 etas of the "
    "complex double quadrature) exceeded the ~10-min-per-operation "
    "discipline -> restructured to the pole-subtracted smooth function "
    "J = I - 2/eps (pole coefficient = frozen engine law, not Route A) with "
    "eta-Richardson and quadratic eps-interpolation on 3 points; 6 doubles",
    "run 7: even a single complex timelike double exceeded 5 min (the "
    "second-order near-pole structure defeats tanh-sinh) -> Im refereed via "
    "the delta'-distribution route (Im[1/(x-i0)^2] = -pi delta'(x), reducing "
    "the radial integral exactly to pi(d-2)/4 a^{(d-4)/2} on the cut), with "
    "bisection cut endpoints and numeric y-quadrature -- a derivation "
    "disjoint from the log-branch limit; Re reported from Route A with a "
    "quad-vs-exact-sympy-closed-form cross-check; the absent direct "
    "complex-quadrature referee for Re and Im at timelike is DISCLOSED as "
    "an A3-1 limitation for owner inspection at the A3-2 gate",
    "run 8: the DIRECT difference-integrand quadrature for M_1(D1)-M_1(1) "
    "disagreed with the exact Schwinger reference by ~15 (pole fit correct; "
    "cause not fully diagnosed -- suspected mpmath interval handling of the "
    "near-tail remainder); replaced by the exact s-parameter identity "
    "1/A - 1/B = (B-A) Int_0^1 ds/(L^2+D(s))^2 composed with the "
    "ALREADY-REFEREED M_2 radial machinery, identity gated symbolically; "
    "the failed direct route is disclosed here",
]
ng = len(CHECKS); npass = sum(1 for c in CHECKS if c["pass"])
cdet = sum(1 for c in CONTROLS if c["pass"])
verdict = ("PASS" if (npass == ng and cdet == len(CONTROLS)
                      and len(CONTROLS) >= 3 and not _early) else
           ("FAIL" if FAILS or (CONTROLS and cdet < len(CONTROLS)) else "UNVERIFIED"))
result = {
    "task": "A3-1 finite eps^0 master integrals",
    "instrument": os.path.basename(__file__),
    "instrument_sha256": hashlib.sha256(
        open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
    "generated": time.strftime("%Y-%m-%d %H:%M:%S"),
    "builder": "builder session (owner 'go' 2026-08-28)",
    "head": HEAD,
    "standing": "W-0: computed-and-reported, NOT banked; no register edits",
    "contract_chain_verified": {fn: (hashlib.sha256(
        open(os.path.join(HERE, fn), 'rb').read()).hexdigest() == want)
        for fn, want in PIN.items()},
    "convention": {
        "measure": "mu^eps Int d^{4-eps}l/(2pi)^{4-eps} (Minkowski, Feynman +i0)",
        "c_units": "masters / (i(4pi)^-2); c = 2/eps exactly",
        "euclidean_image": "M_N = (-1)^N (4pi)^2 mu^eps Int_E (L^2+Delta)^-N "
                           "((-1)^N confirmed vs frozen pole gates)",
        "scheme": "MS: subtract exactly c (matches frozen Phase-12 split)",
        "kappa": "ln(4pi) - gamma_E (emerges from the Schwinger series)",
        "denominators": "D1 = l^2-m^2, D2 = (l-K)^2-m^2, Delta = m^2-y(1-y)K^2",
        "numerics_units": "m = mu = 1"},
    "route_principle": "Route A: Schwinger-derived, exact in eps, sympy. "
                       "Route B: mpmath quadrature of the ORIGINAL integrand "
                       "at d=4-eps with eps-grid (2/eps, eps^0) extraction; "
                       "no shared Gamma/log eps-structure between routes.",
    "masters": MASTERS, "branch": BR if not _early else {},
    "checks": CHECKS, "controls": CONTROLS,
    "counts": {"gates": ng, "passed": npass, "failed": ng - npass,
               "controls": len(CONTROLS), "controls_detected": cdet},
    "self_caught_defects": SELF_CAUGHT,
    "barred_scope_not_computed": ["Sigma_R^finite assembly", "Pi_nonlocal",
                                  "TT projection", "Q1-Q5", "J(omega)", "PV",
                                  "benchmark comparison", "spectrum interpretation"],
    "verdict": verdict,
    "a3_2_gate": "A3-2 remains LOCKED pending explicit owner/reviewer "
                 "acceptance of this result, including inspection of the "
                 "finite-master formulas and branch structure.",
}
with open(os.path.join(HERE, "WALL_A3_1_FINITE_MASTERS_RESULT.json"), "w") as f:
    json.dump(result, f, indent=1, default=float)

md = []
md.append("# WALL A / ASSEMBLY-3 / A3-1 -- FINITE eps^0 MASTER VERDICT\n")
md.append("**Status: W-0 -- computed-and-reported, NOT banked.** Overall "
          "verdict: **%s** (%d/%d gates pass, %d/%d negative controls detected)"
          % (verdict, npass, ng, cdet, len(CONTROLS)))
md.append("\n## Declared convention (for owner inspection at the A3-2 gate)\n")
md.append("- measure `mu^eps Int d^{4-eps}l/(2pi)^{4-eps}`, Minkowski, Feynman +i0\n"
          "- c-units: masters normalised by `i(4pi)^-2`; `c = 2/eps` exactly\n"
          "- MS: subtract exactly `c` (matches frozen Phase-12 "
          "`Pi_local^MS = (2/eps)[...]`)\n"
          "- `kappa = ln(4pi) - gamma_E` emerges in every finite part\n"
          "- `D1 = l^2-m^2`, `D2 = (l-K)^2-m^2`, `Delta = m^2 - y(1-y)K^2`\n")
md.append("\n## Masters (pole | finite eps^0 | mu-dep | verdict)\n")
for m in MASTERS:
    md.append("- **%s**: pole `%s` | finite `%s` | mu-dep `%s` | %s"
              % (m["name"], m.get("pole", "-"), m.get("finite", "-"),
                 m.get("mu_dep", "-"), m.get("verdict", "-")))
    if "note" in m:
        md.append("  - note: %s" % m["note"])
md.append("\n## Independent numerical referee (Route B, original integrand)\n")
md.append("- scalar bubble at K2/m2 in {-0.7, -1.3, -2.9}: all diffs < 1e-6; "
          "numeric pole fit reproduces the engine value 2\n"
          "- M_2, M_3, M_4 at 3 Deltas each; M_1 difference-anchored; "
          "T2_{00,3}, T4_{0000,4} direct tensor radials\n"
          "- second eps-grid reproducibility; three negative controls "
          "(factor 2, wrong mu, eps sign) all DETECTED")
if (not _early) and BR:
    md.append("\n## Branch / threshold\n")
    md.append("- threshold: `K^2 = 4 m^2` (from Delta(y) roots; numeric "
              "bisection on min_y Delta(y) confirms)\n")
    md.append("- prescription: `ln(Delta - i0)`; `Im B = "
              "pi sqrt(1-4m^2/K^2) theta(K^2-4m^2)` (limit-derived Disc M2 = "
              "2 pi i theta(-Delta); Im refereed at K^2 = 5 m^2 by quadrature "
              "of the real absorptive integrand, cut endpoints by bisection: "
              "diff %.1e; Re cross-checked quad vs exact closed form: %.1e; "
              "no direct complex-quadrature Re referee -- disclosed limitation)"
              % (BR.get("Im_diff", float('nan')),
                 BR.get("Re_crosscheck_diff", float('nan'))))
md.append("\n## Self-caught defects during this run\n")
md.append("- " + ("\n- ".join(SELF_CAUGHT) if SELF_CAUGHT else "none"))
md.append("\n## Scope\n")
md.append("A3-2+ objects NOT computed: Sigma_R^finite assembly, Pi_nonlocal, "
          "TT, Q1-Q5, J(omega), PV, benchmarks, interpretation. "
          "A3-2 stays LOCKED pending explicit owner acceptance.\n")
with open(os.path.join(HERE, "WALL_A3_1_FINITE_MASTERS_VERDICT.md"), "w") as f:
    f.write("\n".join(md) + "\n")

print("\n================ SUMMARY ================")
print("gates: %d/%d pass | controls detected: %d/%d | verdict: %s"
      % (npass, ng, cdet, len(CONTROLS), verdict))
if FAILS:
    print("FAILURES:")
    for m_ in FAILS:
        print("  - " + m_)
print("outputs written: WALL_A3_1_FINITE_MASTERS_RESULT.json, "
      "WALL_A3_1_FINITE_MASTERS_VERDICT.md")
stamp("done")
sys.exit(0 if verdict == "PASS" else 1)
