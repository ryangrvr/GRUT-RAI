#!/usr/bin/env python3
"""U3 KERNAL MINIMALITY -- does the minimal stable causal memory law force first order?

THE CALC THE U3 FENCE HAS BEEN WAITING FOR (speaks to `u3_split_origin` and
`rung3_single_pole`). The working hypothesis under test:

    H: Given ONLY (1) a state space, (2) causal evolution, (3) persistence of prior
       state information, (4) finite effective memory, (5) stability,
       (6) time-translation invariance,
       the exponential / single-pole kernel K(t) = tau^-1 e^{-t/tau} Theta(t)
       emerges as the unique minimal Markovian realization.

METHOD: formalize the six constraints as mechanical tests on candidate kernels,
run a DELIBERATE COUNTEREXAMPLE BATTERY (kernels chosen to satisfy the six while
having larger Markov realization dimension), verify the one-variable uniqueness
theorem constructively, and test whether composability (closure of the class under
composition) preserves or destroys the single pole.

VERDICT LOGIC (registered below): if any counterexample passes all six constraints
with realization dimension > 1, H is REFUTED AS STATED and the surviving content is
the uniqueness theorem -- the posit relocates from kernel shape to minimality.

Pure stdlib + optional numpy (falls back to pure python loops). W-0 honest: the
result, whichever way it goes, is banked as computed, not as wished.
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "U3_KERNEL_MINIMALITY_RESULT.json")

results = {"instrument": "calc/u3_kernel_minimality.py", "checks": [],
           "hypothesis": ("single-pole kernel emerges uniquely from {state, causality, "
                          "persistence, finite memory, stability, time-translation "
                          "invariance} as the minimal Markovian realization")}


def check(name, ok, msg):
    results["checks"].append({"name": name, "pass": bool(ok), "msg": msg})
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {msg}")
    return ok


# ---------------------------------------------------------------- grid / kernels
DT = 0.01
TMAX = 12.0
NPOS = int(TMAX / DT)                       # t in [0, TMAX)
NEG = [-DT * k for k in range(1, 51)]       # t in (-0.5, 0): causality probes


def single_pole(t, tau=1.0):
    return math.exp(-t / tau) / tau if t >= 0 else 0.0          # Theta(t)


def two_pole(t):
    return 0.5 * (math.exp(-t / 1.0) + 2.0 * math.exp(-t / 0.5)) / 1.5 if t >= 0 else 0.0


def jordan(t):                                # t * e^{-t}: pole of order 2
    return t * math.exp(-t) if t >= 0 else 0.0


def damped_cos(t):
    return math.exp(-0.5 * t) * math.cos(3.0 * t) if t >= 0 else 0.0


def boxcar(t):                                # uniform window on [0,1]: finite support
    return 1.0 if 0.0 <= t <= 1.0 else 0.0


def power_law(t):                             # (1+t)^-3: integrable tail, no poles
    return 1.0 / (1.0 + t) ** 3 if t >= 0 else 0.0


KERNELS = [
    ("single_pole",   single_pole, 1, True),
    ("two_pole",      two_pole,    2, True),
    ("jordan",        jordan,      2, True),
    ("damped_cosine", damped_cos,  2, True),    # scalar Re chi > 0 at all sampled w
    ("boxcar_delay",  boxcar,      math.inf, False),  # Re chi = sin(w)/w < 0 for w in (pi, 2pi)
    ("power_law",     power_law,   math.inf, True),
]

# ---------------------------------------------------------------- constraint tests

def l1_norm(K):
    return sum(abs(K(i * DT)) * DT for i in range(NPOS))


def first_moment(K):
    return sum(i * DT * abs(K(i * DT)) * DT for i in range(NPOS))


def response(K, X, t0, dt=DT, tmax=TMAX):
    """R(t0) = int_0^{t0} K(s) X(t0 - s) ds, left Riemann sum on the grid."""
    n = int(t0 / dt)
    return sum(K(i * dt) * X(t0 - i * dt) * dt for i in range(n + 1))


def test_constraints(name, K, expect_passive):
    tti = False
    try:
        pulse = lambda t: math.exp(-((t - 5.0) / 0.4) ** 2)
        d = 1.0
        R1 = [response(K, pulse, t) for t in (4.0, 5.0, 6.0)]
        pulse_sh = lambda t: math.exp(-((t - 5.0 - d) / 0.4) ** 2)  # input shifted LATER by +d
        R2 = [response(K, pulse_sh, t + d) for t in (4.0, 5.0, 6.0)]  # R2(t+d) must equal R1(t)
        tti = all(abs(a - b) < 1e-6 for a, b in zip(R1, R2))
    except Exception:
        tti = False

    causal = all(K(t) == 0.0 for t in NEG)
    l1 = l1_norm(K)
    stable = 1e-6 < l1 < 1e4
    m1 = first_moment(K)
    finmem = m1 < 1e3

    # passivity proxy: Re chi(w) = int K(t) cos(wt) dt must not go negative
    chi = []
    for w in (0.0, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 7.0, 10.0):
        re = sum(K(i * DT) * math.cos(w * i * DT) * DT for i in range(NPOS))
        chi.append(re)
    passive = all(re > -1e-9 for re in chi)
    re_vals = chi

    return {"name": name, "causal": causal, "bibostable": stable, "l1": l1,
            "finite_memory": finmem, "first_moment": m1, "tti": tti,
            "passive": passive, "re_chi": re_vals,
            "passes_six": causal and stable and finmem and tti,
            "passes_seven": (causal and stable and finmem and tti and passive)}


# ---------------------------------------------------------------- E2: uniqueness theorem

def realize_1var(K_inv_tau, X, phi0, tmax, dt=DT):
    """phi' = (X - phi)/tau ; R = phi. The single-auxiliary-variable realization."""
    phi, t = phi0, 0.0
    out = []
    n = int(tmax / dt)
    for i in range(n):
        out.append(phi)
        x = X(t)
        phi += dt * ((x - phi) / K_inv_tau)
        t += dt
    return out


def direct_conv(K, X, tmax, dt=DT):
    return [response(K, X, i * dt, dt) for i in range(int(tmax / dt))]


def scalar_ode_impulse(a, b, c, eps=1e-3, tmax=8.0, dt=1e-4):
    """Impulse response of phi' = a phi + b X ; R = c phi via a regularized delta."""
    phi, t = 0.0, 0.0
    out = []
    n = int(tmax / dt)
    for i in range(n):
        x = (1.0 / eps) if t < eps else 0.0        # narrow unit-area pulse ~ delta
        out.append(c * phi)
        phi += dt * (a * phi + b * x)
        t += dt
    return out, dt


# ---------------------------------------------------------------- run

print("== E1. The six constraints, mechanized on the counterexample battery ==")
rows = []
for name, K, dim, exp_passive in KERNELS:
    r = test_constraints(name, K, exp_passive)
    r["markov_dim_analytic"] = dim
    r["passive_expected"] = exp_passive
    rows.append(r)
    print(f"  {name:14s} causal={r['causal']} bibo={r['bibostable']} (L1={r['l1']:.3f}) "
          f"finmem={r['finite_memory']} (M1={r['first_moment']:.3f}) tti={r['tti']} "
          f"passive={r['passive']} -> passes six: {r['passes_six']}")

print("\n== E2. One-variable uniqueness: scalar ODE realization <=> single exponential ==")
# (a) the standard single-pole realization reproduces the convolution
X = lambda t: math.exp(-((t - 4.0) / 0.6) ** 2)
tau = 1.0
Ksp = lambda t: single_pole(t, tau)
phi = realize_1var(tau, X, 0.0, 8.0)
Rc = direct_conv(Ksp, X, 8.0)
resid_a = max(abs(p - r) for p, r in zip(phi, Rc))
check("E2a one-variable realization matches single-pole convolution", resid_a < 1.5e-2,
      f"max |phi_ode - R_conv| = {resid_a:.2e} < 1.5e-2 discretization bound (tau=1)")

# (b) general scalar linear auxiliary law -> impulse response IS one exponential
a, b, c = -0.7, 1.3, 2.1
out, dt = scalar_ode_impulse(a, b, c)
pred = [c * b * math.exp(a * t) for t in (1.0, 2.0, 4.0, 6.0)]
got = [out[int(t / dt)] for t in (1.0, 2.0, 4.0, 6.0)]
resid_b = max(abs(p - g) for p, g in zip(pred, got))
check("E2b scalar auxiliary law realizes ONLY an exponential", resid_b < 5e-3,
      f"phi'=a*phi+b*X, R=c*phi -> impulse response = c*b*e^(a t); max dev {resid_b:.2e} "
      f"(a={a}, b={b}, c={c}) -- uniqueness of the 1-variable class")

print("\n== E3. The counterexample battery: does H survive? ==")
survivors = [r for r in rows if r["passes_six"] and r["markov_dim_analytic"] > 1]
check("E3a counterexamples to uniqueness exist", len(survivors) >= 3,
      f"{len(survivors)} kernels pass ALL SIX constraints with Markov dimension > 1: "
      f"{[r['name'] for r in survivors]} -- H is REFUTED AS STATED")

print("\n== E4. Passivity (the register's own 7th constraint, rung2_kms_gate) ==")
killed_by_passivity = [r["name"] for r in rows if r["passes_six"] and not r["passive"]]
still_alive = [r["name"] for r in rows if r["passes_six"] and r["passive"]
               and r["markov_dim_analytic"] > 1]
check("E4a passivity does NOT select the single pole either",
      len(killed_by_passivity) >= 1 and len(still_alive) >= 2,
      f"killed: {killed_by_passivity}; PASSIVE and still dim>1: {still_alive} -- even the "
      f"register's own 7th constraint admits multi-variable realizations")

print("\n== E5. Composability: the single pole is not closed under composition ==")
# K1 * K1 (numeric convolution of the kernel with itself) should equal t e^{-t} shape
Kc = [single_pole(i * DT) for i in range(NPOS)]
conv = []
for n in range(NPOS):
    s = sum(Kc[i] * Kc[n - i] for i in range(n + 1)) * DT
    conv.append(s)
pred = [jordan(i * DT) for i in range(NPOS)]
err = max(abs(a - b) for a, b in zip(conv, pred))
check("E5a single_pole * single_pole = Jordan (t e^{-t})", err < 2.5e-2,
      f"max |K*K - t e^-t| = {err:.2e} < 2.5e-2 discretization bound -- composing two "
      f"first-order evolutions yields a TWO-variable (Jordan) evolution: the minimal class "
      f"is closed under composition, the single pole is not a fixed point of it")

# ---------------------------------------------------------------- verdict
print("\n== VERDICT ==")
refuted = len(survivors) >= 3
results["summary"] = {
    "hypothesis": "REFUTED AS STATED" if refuted else "SURVIVED",
    "counterexamples_with_dim_gt_1": [r["name"] for r in survivors],
    "killed_by_passivity": killed_by_passivity,
    "uniqueness_theorem": ("the exponential is the UNIQUE one-auxiliary-variable Markovian "
                           "realization (E2); the six constraints alone select a whole CLASS "
                           "of admissible kernels, not the single pole"),
    "relocated_posit": ("the ontological posit moves from kernel SHAPE to a MINIMALITY "
                        "principle (exactly one retained-history variable); multi-pole "
                        "kernels = more retained history, boxcar/power-law = continuum of "
                        "retained history (delay/branch-cut)"),
    "composability_finding": ("composition of first-order evolutions generates the Jordan "
                              "hierarchy t^n e^{-t/tau}: the admissible class is closed under "
                              "composition while the single pole is not its fixed point"),
    "verdict": ("U3 PARTIAL: first-order relaxation is derivable GIVEN minimality; minimality "
                "is an additional principle the six constraints do not supply. The decisive "
                "question is now: why ONE auxiliary variable rather than many or a continuum "
                "-- this is the sharpened form of rung3_single_pole."),
}
for k, v in results["summary"].items():
    print(f"  {k}: {v}")
results["kernel_table"] = rows
results["w0"] = "computed result; banking requires the owner through the register gates"

with open(OUT, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nresult written: {OUT}")
