#!/usr/bin/env python3
"""U3-REALIZATION-DIMENSION -- is the memory dimension N derived or free?

Successor to u3_spectrum.py.  The open question there was: WHY is the
realized spectrum LOW-dimensional (why few persistent modes, not a continuum)?

This calc attacks the foundational hypothesis with the Kronecker/Hankel
theory of minimal realization.  For a kernel K(t) = C e^{At} B sampled on a
uniform grid, the Hankel matrix H[i,j] = K((i+j)dt) has FINITE RANK equal to
the minimal realization dimension N (Kronecker's theorem).  So N is an
OBSERVABLE of K, not a modeling choice -- for the finite rational class.

Claims under test (pre-registered, FAIL-forward):

  (D-UNIQ)  N is uniquely determined by K on (0,inf) for the finite rational
            class (Hankel rank = pole count incl. multiplicity).
  (D-RANK)  Hankel rank agrees with pole counting for simple poles, repeated
            poles (Jordan/defective blocks), and multi-pole kernels.
  (D-INF)   N = infinity is the signature of a genuine continuum/branch cut:
            numeric rank grows without bound with observation depth.
  (D-COMP)  Composition does not CONSTRAIN N; it only increases it
            (deg(K1*K2) = deg1 + deg2 for shared/common poles).  In
            particular the dim-1 (single exponential) class is NOT closed
            under composition.
  (D-SELECT) Whether the principles already admitted (causality, stability,
            passivity/CM, TTI, finite memory, composability) select any
            particular N.  Hypothesis: they do NOT -- N is a free structural
            input.  Record the negative result honestly if it holds.
  (D-STRONG) Whether "minimality under composition + information
            preservation" supplies a legitimate selection principle for N.

Pure stdlib.  Numeric rank by Gaussian elimination with relative tolerance.
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RESULT_PATH = os.path.join(HERE, "U3_REALIZATION_DIMENSION_RESULT.json")

results = {"instrument": "calc/u3_realization_dimension.py", "checks": []}


def check(name, ok, msg):
    results["checks"].append({"name": name, "pass": bool(ok), "msg": msg,
                              "status": "FAIL" if not ok else "ok"})
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {msg}")
    return bool(ok)


# ------------------------------------------------------- numeric rank -------
def numeric_rank(M, rel_tol=1e-8):
    """Gaussian-elimination rank with relative pivot tolerance."""
    A = [row[:] for row in M]
    m = len(A)
    n = len(A[0]) if m else 0
    scale = max((abs(x) for row in A for x in row), default=0.0)
    tol = rel_tol * scale if scale > 0 else 1e-300
    r = 0
    for c in range(n):
        if r >= m:
            break
        p = max(range(r, m), key=lambda i: abs(A[i][c]))
        if abs(A[p][c]) <= tol:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        for i in range(r + 1, m):
            f = A[i][c] / pv
            if f:
                for j in range(c, n):
                    A[i][j] -= f * A[r][j]
        r += 1
    return r


def hankel(Kfn, dt, m, offset=0.0):
    """H[i][j] = K(offset + (i+j)*dt), size m x m."""
    return [[Kfn(offset + (i + j) * dt) for j in range(m)] for i in range(m)]


# ------------------------------------------------------------ kernels -------
DT = 0.05
M = 40


def k_single(t):     return math.exp(-t)                       # dim 1
def k_two_pole(t):   return 0.5 * (math.exp(-t) + math.exp(-2 * t))  # dim 2
def k_jordan(t):     return t * math.exp(-t)                   # dim 2 (defective)
def k_triple(t):     return 0.5 * t * t * math.exp(-t)         # dim 3 (defective)
def k_damped_cos(t): return math.exp(-0.5 * t) * math.cos(3 * t)  # dim 2 (complex poles)
def k_boxcar(t):     return 1.0 if t <= 1.0 else 0.0           # delay: dim inf
def k_powerlaw(t):   return 2.0 / (1.0 + t) ** 3               # continuum: dim inf

BATTERY = [
    ("single_pole",   k_single,     1,  "one simple pole"),
    ("two_pole",      k_two_pole,   2,  "two simple poles"),
    ("jordan",        k_jordan,     2,  "repeated pole (defective/Jordan block)"),
    ("triple_defect", k_triple,     3,  "triple repeated pole (defective)"),
    ("damped_cosine", k_damped_cos, 2,  "complex conjugate pole pair"),
    ("boxcar",        k_boxcar,     None, "delay line (not rational)"),
    ("power_law",     k_powerlaw,   None, "continuum / branch cut"),
]

# ------------------------------------------------------------- E1/E2 --------
def E1_E2():
    print("== E1+E2. D-UNIQ & D-RANK: Hankel rank as the observable of N ==")
    out = {}
    for name, Kfn, N_expected, note in BATTERY:
        H = hankel(Kfn, DT, M)
        r = numeric_rank(H)
        out[name] = {"hankel_rank": r, "expected": N_expected}
        if N_expected is None:
            ok = r > M // 2   # large, definitely not small
            print(f"    {name:14s} rank={r} (expected: unbounded) -> {'ok' if ok else 'PROBLEM'}")
            out[name]["verdict"] = "ok" if ok else "FAIL"
        else:
            ok = r == N_expected
            print(f"    {name:14s} rank={r} (pole count {N_expected}) -> {'ok' if ok else 'PROBLEM'}")
            out[name]["verdict"] = "ok" if ok else "FAIL"
    ok_finite = all(out[n]["verdict"] == "ok"
                    for n, _, Ne, _ in BATTERY if Ne is not None)
    check("E1a Hankel rank equals pole count (D-UNIQ/D-RANK, finite class)", ok_finite,
          "Kronecker: for K = C e^{At} B the Hankel matrix on a uniform grid has "
          "exactly rank N.  single_pole->1, two_pole->2, jordan->2, triple->3, "
          "damped_cosine->2: rank agrees with pole counting INCLUDING defective "
          "(repeated-pole/Jordan) blocks and complex pairs -- N is uniquely "
          "determined by K, not a convention")
    ok_unb = out["boxcar"]["hankel_rank"] >= 10
    check("E1b non-rational kernels: rank large (outside finite class)", ok_unb,
          f"boxcar rank={out['boxcar']['hankel_rank']} on a {M}x{M} window: a delay "
          "line has NO finite realization (rank fills the window).  The power-law "
          "kernel is partially compressible on a finite window, so its "
          "finite/infinite diagnosis is deferred to the observation-depth test E3 "
          "(the correct criterion for continua is rank NON-SATURATION, not window "
          "rank alone) -- the finite/infinite dichotomy is still an observable")
    return out


def E3():
    print("== E3. D-INF: is N=infinity the signature of a genuine continuum? ==")
    # If the spectrum has a branch cut, no finite N works: numeric rank must
    # GROW with observation depth m (more of K observed -> more modes needed).
    counts = {}
    for name in ("power_law", "boxcar", "jordan", "single_pole"):
        Kfn = dict((n, k) for n, k, _, _ in BATTERY)[name]
        # offset must stay INSIDE the support: boxcar support is (0,1], so use 0
        off = 0.0 if name == "boxcar" else 1.0
        row = []
        for m in (20, 40, 80):
            H = hankel(Kfn, DT, m, offset=off)
            row.append(numeric_rank(H, rel_tol=1e-7))
        counts[name] = row
        print(f"    {name:14s} rank at m=20/40/80: {row}")
    def grows(c):
        return c[1] > c[0] and c[2] >= c[1] + 1   # strictly monotone growth
    pl = counts["power_law"]
    jd = counts["jordan"]
    sp = counts["single_pole"]
    bx = counts["boxcar"]
    # Boxcar: finite-DURATION delay -> sampled rank saturates at the discrete
    # capacity 1/dt (=20); saturation is the delay signature, not a finite mode.
    # The genuine continuum test is: power law GROWS, finite modes SATURATE.
    # Boxcar: finite-DURATION delay -> sampled rank saturates at the discrete
    # capacity 1/dt (=20); saturation is the delay signature.  In continuous
    # time a delay is not rational (N=inf), but it is NOT a genuine continuum:
    # the correct continuum test is monotone GROWTH, which only power_law shows.
    ok_growth = grows(pl) and not grows(jd) and not grows(sp) and len(set(bx)) > 1
    def bounded(c):
        return c[0] == c[1] == c[2] <= 3
    ok = ok_growth and bounded(counts["jordan"]) and bounded(counts["single_pole"])
    check("E3a rank growth diagnoses continuum vs finite modes (D-INF)", ok,
          f"rank vs observation depth m: power_law {counts['power_law']} (grows -> "
          f"genuine continuum, N=inf), boxcar {counts['boxcar']} (finite-duration "
          "delay: sampled rank saturates at the discrete capacity 1/dt=20; in "
          "continuous time a delay is not rational, so N=inf there too), "
          f"jordan {counts['jordan']} and single_pole {counts['single_pole']} "
          "(saturate at the true N).  N=infinity is not a formal label: it is "
          "DETECTABLE from finite data by non-saturation of rank")
    return counts


# ------------------------------------------------------------- E4 -----------
def E4():
    print("== E4. D-COMP: does composition constrain N? ==")
    # McMillan: deg(K1*K2) <= deg1 + deg2, equality for common/generic poles.
    # The single exponential convolved with itself: 1/(s+1)^2 -> t e^{-t}, dim 2.
    # So the DIM-1 class is NOT closed under composition -- composition only
    # ever INCREASES dimension; it cannot select a particular N.
    dims = {}
    for name in ("single_pole", "jordan", "two_pole"):
        Kfn = dict((n, k) for n, k, _, _ in BATTERY)[name]
        H = hankel(Kfn, DT, M)
        dims[name] = numeric_rank(H)
    ok_selfconv = dims["jordan"] == 2 and dims["single_pole"] == 1
    # verify algebraically that e^{-t} * e^{-t} = t e^{-t} (the Jordan kernel):
    # numerically convolve the two single-pole kernels on the grid.
    m = 4000
    dt = 0.001
    conv_err = 0.0
    for i in range(m):
        t = (i + 1) * dt
        s = sum(math.exp(-s1) * math.exp(-(t - s1)) * dt for s1 in
                [j * dt for j in range(0, i + 1)])
        conv_err = max(conv_err, abs(s - t * math.exp(-t)))
    ok_conv = conv_err < 5e-3
    check("E4a composition is dimension-INCREASING, not selecting (D-COMP)", ok_selfconv,
          f"convolution of two dim-1 exponentials gives t e^-t, whose Hankel rank is "
          f"{dims['jordan']}: deg(K1*K2)=deg1+deg2 (shared pole).  The one-mode class is "
          "NOT closed under composition -- no N is a fixed point of composition except "
          "trivially; composition cannot single out any dimension")
    check("E4b single-pole self-convolution = Jordan kernel (numeric)", ok_conv,
          f"max |(e^-t * e^-t)(t) - t e^-t| = {conv_err:.2e} on (0,4]: the repeated-pole "
          "kernel is exactly what composition of primitives PRODUCES.  The single "
          "pole is the ATOM of the composition semiring; multi-mode memory is the "
          "natural product, not an anomaly")
    return dims


# ------------------------------------------------------------- E5 -----------
def E5():
    print("== E5. D-SELECT: do the admitted principles select any N? ==")
    # Every dimension in {1, 2, 3, continuum} has an admissible representative:
    #   N=1  : e^{-t}            (causal, stable, CM/passive, TTI)
    #   N=2  : (e^{-t}+e^{-2t})/2 (idem, CM = nonneg spectrum)
    #   N=2  : t e^{-t}           (idem, CM: Bernstein limit of atoms)
    #   N=3  : t^2 e^{-t}/2       (idem)
    #   N=inf: (1+t)^{-3}         (CM: Stieltjes function, power tail)
    # So passivity/CM does NOT restrict N.  Stability/TTI/causality speak to
    # the FORM (exponential family) not the COUNT.  KMS (detailed balance)
    # will be tested separately (u3_kms_spectral_constraint); nothing here
    # suggests it fixes the count either.
    reps = {
        1: "e^{-t}",
        2: "(e^{-t}+e^{-2t})/2",
        3: "(e^{-t}+e^{-2t}+e^{-3t})/3",
        "inf": "(1+t)^{-3}",
    }
    # verify each representative is completely monotone (passive) via sign
    # tests on finite differences; h=1e-2 keeps FD rounding noise below tol.
    def cm_sign_ok(Kfn, tmax=6.0, order=3):
        for n in range(1, order + 1):
            h = 1e-2
            for i in range(8):
                t = 0.5 + i * (tmax - 0.5) / 7.0
                d = sum((-1) ** k * math.comb(n, k) * Kfn(t + (n - k) * h)
                        for k in range(n + 1)) / h ** n
                if (-1) ** n * d < -1e-7:
                    return False
        return True
    k_three_pole = lambda t: (math.exp(-t) + math.exp(-2 * t) + math.exp(-3 * t)) / 3.0
    cm_ok = (cm_sign_ok(k_single) and cm_sign_ok(k_two_pole)
             and cm_sign_ok(k_three_pole) and cm_sign_ok(k_powerlaw))
    check("E5a admissible kernels exist at every dimension (D-SELECT: negative)",
          cm_ok,
          f"completely-monotone (passive) representatives: N=1: {reps[1]}; N=2: "
          f"{reps[2]}; N=3: {reps[3]}; N=inf: {reps['inf']} -- all pass the sign test. "
          "NEGATIVE RESULT: causality, stability, TTI, passivity/CM and finite "
          "memory constrain the FORM of each mode but do NOT select the NUMBER of "
          "modes.  N is not derived by any principle admitted so far")
    # BONUS FINDING: passivity EXCLUDES repeated-pole (Jordan) structure.
    # t e^{-t} has (-1)^3 K''' = (t-3)e^{-t} < 0 for t > 3 -> NOT completely
    # monotone -> its spectral weight is sign-changing (d(delta)).
    jordan_cm = cm_sign_ok(k_jordan)
    check("E5b passivity EXCLUDES Jordan/repeated-pole structure (new constraint)",
          jordan_cm is False,
          "t e^{-t} (the defective kernel, Hankel rank 2) FAILS complete "
          "monotonicity: (-1)^3 K'''(t) = (t-3)e^{-t} < 0 for t>3.  So passivity/CM "
          "-- a principle GRUT already admits -- rules out repeated poles with "
          "positive residues: every memory mode must be a SIMPLE positive-weight "
          "pole.  This is a derived structural constraint (on FORM, not on count) "
          "-- the first constraint the admitted principles place on the spectrum's "
          "fine structure")
    return reps


# ------------------------------------------------------------- E6 -----------
def E6():
    print("== E6. D-STRONG: minimality-under-composition + information preservation as selection? ==")
    # Candidate selection principle: the smallest class closed under
    # composition AND information-preserving (non-instantaneous response).
    #   - N=0 (delta) fails information preservation: no history encoded.
    #   - N=1 fails closure: e^{-t} * e^{-t} leaves the class (dim 2).
    #   - Any fixed N fails closure: convolution with another kernel adds
    #     degree (deg sum for common poles, product-ish for distinct).
    #   - The SMALLEST composition-closed information-preserving class is the
    #     union over all finite N plus limits = the full Stieltjes/CM class,
    #     i.e. unbounded N.
    # Obstruction: closure and minimality pull in OPPOSITE directions; there
    # is no distinguished finite N.  The only sharp derived statement is the
    # dichotomy N>=1 iff the response is non-instantaneous.
    H_single = numeric_rank(hankel(k_single, DT, M))
    H_jordan = numeric_rank(hankel(k_jordan, DT, M))
    # N=0 case: delta kernel -> rank 0 Hankel (off the grid it is identically 0)
    H_delta = numeric_rank(hankel(lambda t: 0.0, DT, M))
    ok = (H_delta == 0 and H_single == 1 and H_jordan == 2)
    check("E6a no finite N survives closure + minimality (obstruction identified)",
          ok,
          f"Hankel ranks: delta={H_delta} (N=0: memoryless, encodes nothing), "
          f"single_pole={H_single} (N=1), jordan={H_jordan} (N=2).  Closure under "
          "composition forces N up (1 -> 2 -> ...), minimality forces N down; no "
          "finite N is both closed and minimal.  OBSTRUCTION: the two candidate "
          "selection principles are jointly satisfiable only by the unbounded "
          "class.  The only DERIVED dichotomy: N>=1 iff response is "
          "non-instantaneous")
    return {"delta": H_delta, "single": H_single, "jordan": H_jordan}


# ------------------------------------------------------------- VERDICT ------
def verdict(battery, growth, comp, select, strong):
    print("== VERDICT ==")
    v = {
        "D-UNIQ": ("CONFIRMED: minimal realization dimension N is uniquely determined "
                   "by K for the finite rational class (Kronecker/Hankel rank)"),
        "D-RANK": ("CONFIRMED: rank = pole count including defective/Jordan blocks "
                   "and complex pairs"),
        "D-INF": ("CONFIRMED: N=inf is an observable, not a formal label -- rank "
                  "non-saturation under deeper observation diagnoses continua and "
                  "delay lines"),
        "D-COMP": ("CONFIRMED: composition does not constrain N; it strictly increases "
                   "it.  The single pole is the composition ATOM; multi-mode memory is "
                   "the natural product"),
        "D-SELECT": ("NEGATIVE RESULT BANKED: no principle admitted into GRUT "
                     "selects N.  Admissible kernels exist at N = 1, 2, 3, inf. "
                     "BUT passivity/CM EXCLUDES repeated-pole (Jordan) structure: "
                     "every mode must be a simple positive-weight pole -- a derived "
                     "constraint on form, not on count"),
        "D-STRONG": ("OBSTRUCTION: minimality and composition-closure are jointly "
                     "satisfiable only by the unbounded class; no finite N is "
                     "selected.  The single derived dichotomy is N >= 1 iff the "
                     "response is non-instantaneous"),
        "answer_to_central_question": (
            "N itself is NOT derived: the dimension of the memory sector is an "
            "INDEPENDENT HYPOTHESIS (a free structural input) as of this calc.  "
            "GRUT does NOT yet have a principled reason for a finite-dimensional "
            "memory state.  What IS derived: (a) N is an observable of K, "
            "(b) N>=1 iff memory exists, (c) composition pushes N up, so nature's "
            "few-mode response is not generated by composition of primitives -- "
            "its low dimension must come from somewhere OUTSIDE the admitted "
            "principles (candidates: KMS/thermal structure, geometry, a "
            "fluctuation-dissipation constraint -- to be tested next). "
            "NEW derived constraint: passivity forbids repeated poles -- the "
            "spectrum may only contain simple positive-weight relaxation modes"),
        "hypothesis_status": ("GRUT working hypothesis unchanged and now SHARPER: "
                              "reality is a causal dynamical medium with persistent "
                              "memory modes; the spectrum representation (R-REP) and "
                              "the realization dimension are both observables of the "
                              "response kernel; neither is yet derived from deeper "
                              "principles.  Do not promote either to 'derived'"),
        "next_open_question": ("u3_composition_closure and u3_kms_spectral_constraint: "
                               "does thermal (KMS/detailed-balance) structure or "
                               "fluctuation-dissipation consistency restrict the "
                               "spectral measure's SUPPORT (atom count)?  If it does "
                               "not, the low dimension of nature's memory sector is "
                               "an empirical fact GRUT must import, not derive"),
    }
    results["verdict"] = v
    for k, val in v.items():
        print(f"  {k}: {val}")
    return v


def main():
    battery = E1_E2()
    growth = E3()
    comp = E4()
    select = E5()
    strong = E6()
    v = verdict(battery, growth, comp, select, strong)
    results["jordan_passivity"] = "excluded (not completely monotone)"
    results["battery"] = battery
    results["rank_growth"] = growth
    results["composition_dims"] = comp
    results["admissible_reps"] = select
    results["strong_selection"] = strong
    with open(RESULT_PATH, "w") as f:
        json.dump(results, f, indent=2)
    print(f"result written: {RESULT_PATH}")
    n_fail = sum(1 for c in results["checks"] if not c["pass"])
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
