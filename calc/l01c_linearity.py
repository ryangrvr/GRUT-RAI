#!/usr/bin/env python3
"""l01c_linearity: the third instrument of the Level-0 necessity sweep
(D-LIN).

Charter: L0_1C_CHARTER_01.md, FROZEN at commit 2da022d after the
adversarially verified pre-freeze review (L0_1C_PREFREEZE_REVIEW_01.md;
its measured preview values are quarantined there and adjudicate
nothing here). Authority: L0_1B_OWNER_RULING_01.md; the owner's four
prohibitions bind.

The frozen question: is linearity necessary for the phenomena, or only
for the instrument?  H3 under attack, not protection.

Two instruments by construction:
    A: the eigen-reduction (P_exact-reduction; definitional).
    B: the phenomenon battery (P_memory, P_positivity), direct
       time-domain RK4 of the gradient flow  xdot = -K_b x - 4 beta x^3,
       substrate-eigen-free. jacobi_eig touches Instrument B only as
       instrument mathematics on the measured data Gram (M-3).

Vocabulary (frozen): member = beta value; leg = (beta, a) pair.
38 trajectories: 18 legs + 18 halved-schedule audits + 2 linear
continuations. Pure stdlib. Deterministic (no RNG). Single run.
Run: python3 calc/l01c_linearity.py   (writes ../L0_1C_RESULT.json)
"""

import hashlib
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c1_seam import build_K
from partition_selection_p1 import jacobi_eig

T0 = time.time()
CHECKS = []
HALT = []
DEFECTS = []


def check(ok, msg, kind="ok"):
    CHECKS.append({"kind": kind, "pass": bool(ok), "summary": msg})
    tag = {"ok": "GATE", "ctrl": "CONTROL", "note": "NOTE", "diag": "DIAG"}[kind]
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg)


def halt_check(ok, msg):
    check(ok, msg, "ctrl")
    if not ok:
        HALT.append(msg)


# ---- the certified textual copy of the L0-1a comparator (RC-6) ---------
TAUS = [1.0 + 0.5 * i for i in range(79)]   # 1.0 .. 40.0 step 0.5


def fit_residuals(ks):
    """Frozen comparator: max abs residual of least-squares linear fits
    of ln k vs tau (exponential model) and ln k vs ln tau (algebraic)."""
    y = [math.log(k) for k in ks]

    def rmax(xs):
        n = len(xs)
        sx, sy = sum(xs), sum(y)
        sxx = sum(x * x for x in xs)
        sxy = sum(x * yy for x, yy in zip(xs, y))
        b = (n * sxy - sx * sy) / (n * sxx - sx * sx)
        a = (sy - b * sx) / n
        return max(abs(yy - (a + b * x)) for x, yy in zip(xs, y)), b

    r_exp, rate = rmax(TAUS)
    r_alg, slope = rmax([math.log(t) for t in TAUS])
    grade = "EXPONENTIAL-GRADE" if r_exp < r_alg else "ALGEBRAIC-GRADE"
    return r_exp, r_alg, grade, rate, slope


# ---- the substrate (frozen: the committed machinery) -------------------
N = 24
K_FULL = build_K(N, 0.0)
KB = [row[1:] for row in K_FULL[1:]]          # bath block, dim 23
NB = 23
# nonzero pattern of K_b, extracted once; the flow's linear map IS K_b
NZ = [[(j, -KB[i][j]) for j in range(NB) if KB[i][j] != 0.0]
      for i in range(NB)]
NZP = [[(j, KB[i][j]) for j in range(NB) if KB[i][j] != 0.0]
       for i in range(NB)]                    # +K_b rows (for V)

MEMBERS = [0.0, 0.03, 0.1, 0.3, 1.0, 3.0]
AMPS = [0.001, 1.0, 3.0]
STRONG = [(1.0, 3.0), (3.0, 3.0)]
K40_L01A = 6.8195192260507686e-09
R_EXP_SEAL = 1.9809889100368165
R_ALG_SEAL = 4.7907669413552245

# frozen grids (recordings by step index, never accumulated tau)
EE_STEPS = (5, 10, 20, 50, 100, 200, 450)     # h1 steps
EE_TAUS = [s * 1e-4 for s in EE_STEPS]
EARLY_TAUS = [0.05 * j for j in range(1, 20)]  # every 500th h1 step
GATED_TAUS = TAUS                              # h1 step 10000 + every 200th h2 step


def V_of(x, beta):
    q = 0.0
    for i, row in enumerate(NZP):
        xi = x[i]
        q += xi * sum(c * x[j] for j, c in row)
    return 0.5 * q + beta * sum(v ** 4 for v in x)


def deriv(x, beta):
    return [sum(c * x[j] for j, c in row) - 4.0 * beta * x[i] ** 3
            for i, row in enumerate(NZ)]


def rk4_run(x0, beta, n1, h1, n2, h2, rec1_every, rec2_every,
            ee_steps=(), keep_state_at_phase1_end=False):
    """Integrate by integer step counts; return recorded x1 lists
    (ee, early, gated-after-phase1) plus V at every recorded point and
    the min recorded x1 over all grids. Gated list starts with the
    phase-1 end record (tau = 1)."""
    x = list(x0)
    ee, early, gated, vs = [], [], [], []
    minr = float("inf")
    state1 = None
    ees = set(ee_steps)
    for s in range(1, n1 + 1):
        k1 = deriv(x, beta)
        k2 = deriv([xi + 0.5 * h1 * ki for xi, ki in zip(x, k1)], beta)
        k3 = deriv([xi + 0.5 * h1 * ki for xi, ki in zip(x, k2)], beta)
        k4 = deriv([xi + h1 * ki for xi, ki in zip(x, k3)], beta)
        x = [xi + h1 / 6.0 * (a + 2 * b + 2 * c + d)
             for xi, a, b, c, d in zip(x, k1, k2, k3, k4)]
        if s in ees:
            ee.append(x[0]); vs.append(V_of(x, beta)); minr = min(minr, x[0])
        if s % rec1_every == 0 and s < n1:
            early.append(x[0]); vs.append(V_of(x, beta)); minr = min(minr, x[0])
    gated.append(x[0]); vs.append(V_of(x, beta)); minr = min(minr, x[0])
    if keep_state_at_phase1_end:
        state1 = list(x)
    for s in range(1, n2 + 1):
        k1 = deriv(x, beta)
        k2 = deriv([xi + 0.5 * h2 * ki for xi, ki in zip(x, k1)], beta)
        k3 = deriv([xi + 0.5 * h2 * ki for xi, ki in zip(x, k2)], beta)
        k4 = deriv([xi + h2 * ki for xi, ki in zip(x, k3)], beta)
        x = [xi + h2 / 6.0 * (a + 2 * b + 2 * c + d)
             for xi, a, b, c, d in zip(x, k1, k2, k3, k4)]
        if s % rec2_every == 0:
            gated.append(x[0]); vs.append(V_of(x, beta)); minr = min(minr, x[0])
    return ee, early, gated, vs, minr, state1


def lin_continuation(state1):
    """The X-diag linear-continuation run: from the recorded tau = 1
    state, the pure linear flow on (1, 40], identical h2 stepping."""
    x = list(state1)
    gated, vs = [x[0]], [V_of(x, 0.0)]
    minr = x[0]
    h2 = 2.5e-3
    for s in range(1, 15601):
        k1 = deriv(x, 0.0)
        k2 = deriv([xi + 0.5 * h2 * ki for xi, ki in zip(x, k1)], 0.0)
        k3 = deriv([xi + 0.5 * h2 * ki for xi, ki in zip(x, k2)], 0.0)
        k4 = deriv([xi + h2 * ki for xi, ki in zip(x, k3)], 0.0)
        x = [xi + h2 / 6.0 * (a + 2 * b + 2 * c + d)
             for xi, a, b, c, d in zip(x, k1, k2, k3, k4)]
        if s % 200 == 0:
            gated.append(x[0]); vs.append(V_of(x, 0.0)); minr = min(minr, x[0])
    return gated, vs, minr


# ---------------- Instrument A / eigen reference ------------------------
print("=== INSTRUMENT A: the eigen reference (sealed machinery) ===")
lam, Vv = jacobi_eig([row[:] for row in KB])
U2 = [Vv[0][k] ** 2 for k in range(NB)]
K0_EIG = sum(U2)
K_EIG = [sum(U2[k] * math.exp(-lam[k] * t) for k in range(NB)) for t in TAUS]
rel40 = abs(K_EIG[-1] - K40_L01A) / K40_L01A
re_c, ra_c, grade_c, _, _ = fit_residuals(K_EIG)
halt_check(abs(K0_EIG - 1.0) < 1e-12 and rel40 < 1e-9,
           f"RC-1(eigen) k(0) = {K0_EIG:.15f} (|Delta| < 1e-12) and "
           f"k(40) matches the sealed 6.8195192260507686e-9 "
           f"(|rel Delta| = {rel40:.1e} < 1e-9)")
halt_check(abs(re_c - R_EXP_SEAL) < 1e-12 and abs(ra_c - R_ALG_SEAL) < 1e-12
           and grade_c == "EXPONENTIAL-GRADE",
           f"RC-6 comparator certification: the textual copy reproduces "
           f"the sealed anchor residuals R_exp (|Delta| = "
           f"{abs(re_c - R_EXP_SEAL):.1e}) and R_alg (|Delta| = "
           f"{abs(ra_c - R_ALG_SEAL):.1e}), grade {grade_c} (exact)")

# ---------------- Instrument B: the 38 trajectories ---------------------
print("\n=== INSTRUMENT B: the deletion lattice (18 legs + 18 halved "
      "audits + 2 linear continuations) ===")
LEGS = {}
minr_global = float("inf")
lyap_bad = []
for beta in MEMBERS:
    for a in AMPS:
        x0 = [0.0] * NB
        x0[0] = a
        keep = (beta, a) in STRONG
        ee, early, gated, vs, minr, st1 = rk4_run(
            x0, beta, 10000, 1e-4, 15600, 2.5e-3, 500, 200,
            ee_steps=EE_STEPS, keep_state_at_phase1_end=keep)
        eeh, earlyh, gatedh, vsh, minrh, _ = rk4_run(
            x0, beta, 20000, 5e-5, 31200, 1.25e-3, 1000, 400)
        r = [v / a for v in gated]
        rh = [v / a for v in gatedh]
        rc2 = max(abs(f / h - 1.0) for f, h in zip(gated, gatedh))
        for tag, vseq in (("full", vs), ("half", vsh)):
            for p, q in zip(vseq, vseq[1:]):
                if q - p > 1e-12 * (p + 1e-30):
                    lyap_bad.append((beta, a, tag, q - p))
        minr_global = min(minr_global, minr, minrh)
        steps = max(r[i + 1] - r[i] for i in range(len(r) - 1))
        re_l, ra_l, grade_l, rate_l, _ = fit_residuals(r) if min(r) > 0 \
            else (float("nan"), float("nan"), "UNDEFINED", float("nan"), 0)
        # M-3 data Gram (indices: tau_i = 1 + 0.5 i, sums land at 2 + i + j)
        G = [[r[2 + i + j] for j in range(39)] for i in range(39)]
        glam, _ = jacobi_eig(G)
        gmin = min(glam)
        # window-tail slope (gated tau >= 20): LS slope of ln r vs tau
        xs = TAUS[38:]
        ys = [math.log(v) for v in r[38:]]
        n = len(xs)
        sx, sy = sum(xs), sum(ys)
        b_t = (n * sum(x * y for x, y in zip(xs, ys)) - sx * sy) / \
              (n * sum(x * x for x in xs) - sx * sx)
        LEGS[(beta, a)] = {
            "beta": beta, "a": a, "r_gated": r, "r_early":
                [v / a for v in early], "r_ee": [v / a for v in ee],
            "rc2_sup_rel": rc2, "k40_r": r[-1], "max_step": steps,
            "R_exp": re_l, "R_alg": ra_l, "grade": grade_l,
            "gram_min_eig": gmin, "tail_slope": -b_t,
            "min_recorded_r": min(minr, minrh) / a,
            "state1": st1,
        }
        print(f"   beta={beta:5.2f} a={a:5.3f}: r(40)={r[-1]:.4e}  "
              f"RC2={rc2:.2e}  step_max={steps:+.2e}  {grade_l:17s}  "
              f"Gram_min={gmin:+.3e}")

LINCONT = {}
for beta, a in STRONG:
    st1 = LEGS[(beta, a)]["state1"]
    lg, lv, lminr = lin_continuation(st1)
    minr_global = min(minr_global, lminr)
    for p, q in zip(lv, lv[1:]):
        if q - p > 1e-12 * (p + 1e-30):
            lyap_bad.append((beta, a, "lincont", q - p))
    full = [LEGS[(beta, a)]["r_gated"][i] * a for i in range(79)]
    d_act = max(abs(f / l - 1.0) for f, l in zip(full, lg))
    LINCONT[(beta, a)] = {"D_act": d_act}
    print(f"   D_act(beta={beta}, a={a}) = {d_act:.4f} (ungated)")
for leg in LEGS.values():
    leg.pop("state1", None)

# ---------------- RC gates over the lattice -----------------------------
print("\n=== RC: CONTROLS (halt-grade) ===")
r00 = LEGS[(0.0, 0.001)]["r_gated"]
rc1_td = max(abs(rr / kk - 1.0) for rr, kk in zip(r00, K_EIG))
halt_check(rc1_td < 1e-6,
           f"RC-1(time-domain) the (beta=0, a=0.001) leg matches the "
           f"eigen form on the gated grid: sup |r/k - 1| = "
           f"{rc1_td:.1e} < 1e-6 (Instrument B certified against the "
           f"sealed machinery)")
rc2_worst = max(l["rc2_sup_rel"] for l in LEGS.values())
halt_check(rc2_worst < 1e-9,
           f"RC-2 per-leg halved-schedule audit, all 18 legs: worst "
           f"sup |rel Delta| = {rc2_worst:.1e} < 1e-9")
halt_check(not lyap_bad,
           f"RC-3 Lyapunov descent across consecutive recorded points, "
           f"all 38 trajectories: {len(lyap_bad)} breaches")
rc4 = max(max(abs(a_ / b_ - 1.0) for a_, b_ in
              zip(LEGS[(0.0, amp)]["r_gated"], r00)) for amp in (1.0, 3.0))
halt_check(rc4 < 1e-9,
           f"RC-4 superposition at beta = 0: sup |r(a)/r(0.001) - 1| = "
           f"{rc4:.1e} < 1e-9 for a in {{1.0, 3.0}}")
halt_check(minr_global > 0.0,
           f"RC-5 the sign identity (charter Sec. 3.2 theorem): every "
           f"recorded point of every grid at every trajectory is "
           f"strictly positive (min = {minr_global:.3e}); any r <= 0 "
           f"would be an integrator artifact, HALT, never physics")

# ---------------- X: the deletion is real -------------------------------
print("\n=== X: the deletion is real ===")
xdef = {}
for beta in MEMBERS:
    for a in AMPS:
        if beta > 0.0:
            xdef[(beta, a)] = max(
                abs(p / q - 1.0) for p, q in
                zip(LEGS[(beta, a)]["r_gated"], LEGS[(beta, 0.001)]["r_gated"]))
x1_vals = {s: xdef[s] for s in STRONG}
x1_ok = all(v > 0.1 for v in x1_vals.values())
check(x1_ok,
      f"X-1 amplitude collapse fails at both strong legs "
      f"(certification-grade per Sec. 3.5): deficits "
      + ", ".join(f"(beta={b}, a={a}): {v:.4f}"
                  for (b, a), v in x1_vals.items())
      + " > 0.1")
check(True, "X-diag (ungated): D_act "
      + ", ".join(f"(beta={b})={d['D_act']:.4f}"
                  for (b, a), d in LINCONT.items())
      + "; collapse map and linear-regime hug reported in the artifact",
      "diag")

# ---------------- M: the phenomena --------------------------------------
print("\n=== M: the phenomena under the deletion (Instrument B) ===")
roles = {}
for beta in MEMBERS:
    for a in AMPS:
        roles[(beta, a)] = ("replication" if beta == 0.0 else
                            "control" if a == 0.001 else "adjudicating")
m1_fail = [k for k, l in LEGS.items() if l["grade"] != "EXPONENTIAL-GRADE"]
m2_fail = [k for k, l in LEGS.items() if l["max_step"] > 1e-12]
m3_fail = [k for k, l in LEGS.items() if l["gram_min_eig"] < -1e-10]
m1 = not m1_fail
m2 = not m2_fail
m3 = not m3_fail
check(m1, f"M-1 P_memory: the certified comparator classifies r "
          f"EXPONENTIAL-GRADE at every leg"
          + ("" if m1 else f" -- FAILURES at {m1_fail}"))
check(m2, f"M-2 P_positivity (monotone half): max step increase "
          f"{max(l['max_step'] for l in LEGS.values()):+.2e} <= +1e-12 "
          f"at every leg" + ("" if m2 else f" -- FAILURES at {m2_fail}"))
check(m3, f"M-3 P_positivity (Gram half, the unpreviewed live gate): "
          f"min trajectory-Gram eigenvalue "
          f"{min(l['gram_min_eig'] for l in LEGS.values()):+.3e} >= "
          f"-1e-10 at every leg" + ("" if m3 else f" -- FAILURES at {m3_fail}"))
anchor_tail = LEGS[(0.0, 0.001)]["tail_slope"]
check(True, f"M-diag (ungated): anchor window-tail slope "
            f"{anchor_tail:.4f} (the correct window reference; "
            f"lambda_min = 0.3045 is asymptotic-only); per-leg tail "
            f"slopes, R_exp/R_alg, Gram spectra floors, and the "
            f"early/early-early transient maps are in the artifact",
      "diag")

# identity-protected legs: an M failure there is HALT, never physics
for fails, gate in ((m1_fail, "M-1"), (m2_fail, "M-2"), (m3_fail, "M-3")):
    for k in fails:
        if roles[k] != "adjudicating":
            HALT.append(f"{gate} failure at identity-protected "
                        f"{roles[k]} leg {k}: instrument, never physics "
                        f"(charter Sec. 1/Sec. 5)")

# ---------------- outcome rule (frozen Sec. 5) --------------------------
SCOPE = ("within the declared background mathematics (real symmetric "
         "matrices, exact eigendecomposition, the frozen RK4 schedule), "
         "the convex quartic on-site class on the C1-a bath (N = 24), "
         "the declared amplitudes a in {0.001, 1.0, 3.0}, window, "
         "grids, and comparator")
gated_checks = [c for c in CHECKS if c["kind"] in ("ok", "ctrl")]
n_ok = sum(1 for c in gated_checks if c["pass"])
fails = [c["summary"] for c in gated_checks if not c["pass"]]

adj_fail = [(k, g) for fl, g in ((m1_fail, "M-1"), (m2_fail, "M-2"),
                                 (m3_fail, "M-3"))
            for k in fl if roles[k] == "adjudicating"]
x1_fail_count = sum(1 for v in x1_vals.values() if v <= 0.1)

if HALT:
    label = "HALT"
    v_exact = v_mem = v_pos = "HALT (no line issues; instrument first)"
elif x1_fail_count == 2:
    label = "L01C-VACUOUS"
    v_exact = v_mem = v_pos = ("no line issues: the deletion never bit "
                               "at the tested amplitudes")
elif adj_fail and x1_ok:
    label = "OUTCOME-A"
    props = sorted({{"M-1": "P_memory", "M-2": "P_positivity",
                     "M-3": "P_positivity"}[g] for _, g in adj_fail})
    v_exact = ("LINEARITY: NECESSITY-CERTIFIED for P_exact-reduction "
               "(definitional; Sec. 3.1) -- " + SCOPE) \
        if x1_ok else "L01C-PARTIAL (P_exact-reduction line)"
    v_mem = ("linearity is load-bearing for P_memory at the failing "
             f"legs {[k for k, g in adj_fail if g == 'M-1']} -- " + SCOPE
             ) if any(g == "M-1" for _, g in adj_fail) else \
        ("LINEARITY: NOT-LOAD-BEARING for P_memory (at the declared "
         "amplitudes; D_act recorded) -- " + SCOPE)
    v_pos = ("linearity is load-bearing for P_positivity as "
             f"operationalized at the failing legs "
             f"{[k for k, g in adj_fail if g in ('M-2', 'M-3')]} -- "
             + SCOPE) if any(g in ("M-2", "M-3") for _, g in adj_fail) \
        else ("LINEARITY: NOT-LOAD-BEARING for P_positivity as "
              "operationalized (nonnegativity identity-held; monotone "
              "decrease and Gram PSD tested; D_act recorded) -- " + SCOPE)
elif x1_fail_count == 1:
    label = "L01C-PARTIAL"
    bit = [f"(beta={b}, a={a})" for (b, a), v in x1_vals.items() if v > 0.1]
    v_exact = v_mem = v_pos = (
        f"no NOT-LOAD-BEARING line may issue: X-1 is a single "
        f"conjunction and the deletion bit only at {bit}; re-charter "
        f"obligation attaches at the leg where it failed to bite")
elif fails:
    label = "L01C-PARTIAL"
    v_exact = v_mem = v_pos = "L01C-PARTIAL (see failed gates)"
else:
    label = "OUTCOME-B-CERTIFIED"
    v_exact = ("LINEARITY: NECESSITY-CERTIFIED for P_exact-reduction "
               "(definitional status on the face, Sec. 3.1: the gate "
               "instantiates the premise's failure, it discovers "
               "nothing) -- " + SCOPE)
    v_mem = ("LINEARITY: NOT-LOAD-BEARING for P_memory (at the declared "
             "amplitudes; the deletion's in-window action recorded at "
             "the D_act level) -- " + SCOPE)
    v_pos = ("LINEARITY: NOT-LOAD-BEARING for P_positivity, as "
             "operationalized by the declared window-cone battery and "
             "the trajectory-Gram PSD reading (nonnegativity "
             "identity-held per Sec. 3.2; monotone decrease and Gram "
             "PSD tested; D_act recorded) -- " + SCOPE)

out = {
    "fork": "L0-1c (D-LIN, the Level-0 sweep's third instrument)",
    "charter": "L0_1C_CHARTER_01.md (FROZEN 2da022d; pre-freeze review "
               "record L0_1C_PREFREEZE_REVIEW_01.md)",
    "authority": "L0_1B_OWNER_RULING_01.md (D-LIN authorized per the "
                 "frozen descent order)",
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()),
    "environment": {"python": sys.version.split()[0], "pure_stdlib": True,
                    "deterministic": "no RNG"},
    "defect_history": DEFECTS,
    "measurements": {
        "legs": {f"beta={b},a={a}": {k: v for k, v in l.items()}
                 for (b, a), l in LEGS.items()},
        "collapse_defect_map": {f"beta={b},a={a}": v
                                for (b, a), v in xdef.items()},
        "linear_regime_hug": {f"beta={b}": max(
            abs(p / q - 1.0) for p, q in
            zip(LEGS[(b, 0.001)]["r_gated"], K_EIG))
            for b in MEMBERS if b > 0.0},
        "D_act": {f"beta={b}": d["D_act"] for (b, a), d in LINCONT.items()},
        "eigen_reference": {"k0": K0_EIG, "k40": K_EIG[-1],
                            "comparator_R_exp": re_c,
                            "comparator_R_alg": ra_c},
        "leg_roles": {f"beta={b},a={a}": r for (b, a), r in roles.items()},
    },
    "checks": CHECKS,
    "adjudication": {
        "run_label": label,
        "precedence": "HALT > L01C-VACUOUS > OUTCOME-A > L01C-PARTIAL "
                      "(run-level labels only; per-property lines never "
                      "composed)",
        "verdict_exact_reduction": v_exact,
        "verdict_memory": v_mem,
        "verdict_positivity": v_pos,
        "outcome_B": ("CERTIFIED, with the Sec. 3.4 transient-limited "
                      "qualifier on the face: the tested deletion is "
                      "transient-limited on the declared window; "
                      "P_continuum and P_geometry visibly unclaimed"
                      if label == "OUTCOME-B-CERTIFIED" else
                      "NOT CERTIFIED (see run_label)"),
        "scope": SCOPE,
    },
    "elapsed_s": round(time.time() - T0, 2),
}
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                    "L0_1C_RESULT.json")
blob = json.dumps(out, indent=1)
with open(path, "w") as fh:
    fh.write(blob)
sha = hashlib.sha256(blob.encode()).hexdigest()
print(f"\nartifact written: {os.path.abspath(path)} (sha {sha[:16]}...)")
print(f"\nL0-1c: {n_ok}/{len(gated_checks)} gated checks passed; "
      f"failures: {len(fails)}; halts: {len(HALT)}")
if HALT:
    print("HALT: " + "; ".join(HALT))
    sys.exit(2)
print(f"RUN LABEL: {label}")
print(f"VERDICT LINE 1 (P_exact-reduction): {v_exact[:100]}...")
print(f"VERDICT LINE 2 (P_memory): {v_mem[:100]}...")
print(f"VERDICT LINE 3 (P_positivity): {v_pos[:100]}...")
print("HARD STOP: verdicts recorded pending owner ruling.")
sys.exit(0 if not fails else 1)
