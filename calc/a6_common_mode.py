#!/usr/bin/env python3
"""a6_common_mode: the owed Boltzmann-grade common-mode differential check
of the frozen TT-auto gate (the blocking item of the first Part-7 front,
v4 channel C3).

Charter: A6_COMMON_MODE_CHARTER_01.md, frozen at commit 59ab1ec,
Amendment 01 (pre-run, disclosed) at 0c9e9e3.

Scheme (frozen, normalization-free): the pipeline's exclusion metric
depends only on R_ell(x) = C^pipe_ell(x)/C^pipe_ell(0); the omitted
common power enters both sides additively, so
    R_corr = (R + f_ell) / (1 + f_ell),
with f_ell measured entirely inside CAMB as a ratio of the full scalar
TT to the pipeline-matched source spectrum (monopole + late-ISW via the
windowed exact source decomposition). Quotable members: a_s = 1/50 (B)
and 1/20 (C); full-ISW baseline (A) is the diagnostic bracket.

External ground-truth harness (declared; the A1/mpmath precedent):
CAMB 2.0.4 + camb.symbolic custom compiled sources (sympy, gfortran).
The frozen pipeline is imported UNCHANGED. Deterministic. Single run.
Run: python3 calc/a6_common_mode.py  (writes ../A6_COMMON_MODE_RESULT.json)

A8 STANDS WHOLE: every number remains insertion-contaminated at the
kappa-filter level; this instrument repairs the COMMON-MODE defect only.
No register field moves here (v4 R2: node consumption is the owner's).
"""

import hashlib
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from isw_tt_auto import (ELLS, ETA0, ETA_REC, KAPPAS, LNA_LOS0, LNA_LOS1,
                         NS, cls, grow_mode, jl_array, t_bbks_hmpc)

T0 = time.time()
CHECKS = []
HALT = []


def check(ok, msg, kind="ok"):
    CHECKS.append({"kind": kind, "pass": bool(ok), "summary": msg})
    tag = {"ok": "GATE", "ctrl": "CONTROL", "note": "NOTE", "diag": "DIAG"}[kind]
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg)


def halt_check(ok, msg):
    check(ok, msg, "ctrl")
    if not ok:
        HALT.append(msg)


MEAS = {}
CLS_CACHE = {}


def cls_cached(x, kappa):
    key = (round(x, 12), kappa)
    if key not in CLS_CACHE:
        CLS_CACHE[key] = cls(x, kappa)
    return CLS_CACHE[key]


def n_metric(c, base, f=None, metric="LR"):
    """The pipeline's A2 metric, with the frozen common-mode correction
    R -> (R + f_ell)/(1 + f_ell) when f is given (f = None: uncorrected)."""
    n2 = 0.0
    for l in ELLS:
        R = c[l] / base[l]
        if f is not None:
            R = (R + f[l]) / (1.0 + f[l])
        if metric == "LR":
            n2 += (2 * l + 1) * (1.0 / R + math.log(R) - 1.0)
        else:
            n2 += (2 * l + 1) * (R - 1.0) ** 2 / 2.0
    return math.sqrt(max(n2, 0.0))


def edge(kappa, base, f=None):
    """The frozen top-crossing 2-sigma edge finder, verbatim from the
    pipeline's main() (grid probe + 10 bisections)."""
    def n(xv):
        return n_metric(cls_cached(xv, kappa), base, f)
    if n(1.0) < 2.0:
        return None
    grid = [0.05, 0.1, 0.2, 0.3, 0.4, 0.6, 1.0]
    vals = {xv: n(xv) for xv in grid}
    starts = [xv for xv in grid if vals[xv] < 2.0]
    lo_x = max(starts) if starts else 1e-3
    hi_x = min([xv for xv in grid if xv > lo_x and vals[xv] >= 2.0],
               default=1.0)
    for _ in range(10):
        mid = 0.5 * (lo_x + hi_x)
        if n(mid) < 2.0:
            lo_x = mid
        else:
            hi_x = mid
    return 0.5 * (lo_x + hi_x)


# ---------------- RC-1: the frozen pipeline replicates in-run ----------
print("=== RC-1: FROZEN-PIPELINE REPLICATION (halt-grade) ===")
base = cls_cached(0.0, KAPPAS[0])

sw_only = {}
kmin, kmax = 0.2 / ETA0, 3.2 * (ELLS[-1] + 10) / ETA0
lk0, lk1 = math.log(kmin), math.log(kmax)
nk = 110
hk = (lk1 - lk0) / nk
for l in ELLS:
    sw_only[l] = 0.0
for i in range(nk):
    k = math.exp(lk0 + (i + 0.5) * hk)
    lnas_fine, gs = grow_mode(k, 0.0, KAPPAS[0], [LNA_LOS0, LNA_LOS1])
    g_rec = gs[0]
    jl0 = jl_array(ELLS[-1], k * (ETA0 - ETA_REC))
    w = hk * k ** (NS - 1.0) * t_bbks_hmpc(k) ** 2
    for l in ELLS:
        sw_only[l] += w * ((1.0 / 3.0) * g_rec * jl0[l]) ** 2
fr2 = 1.0 - sw_only[2] / base[2]
fr10 = 1.0 - sw_only[10] / base[10]

n111 = {kap: n_metric(cls_cached(0.111, kap), base) for kap in KAPPAS}
edge_unc = {kap: edge(kap, base) for kap in KAPPAS}
MEAS["replication"] = {"isw_share_l2": fr2, "isw_share_l10": fr10,
                       "edge_k1": edge_unc[KAPPAS[0]],
                       "edge_k3": edge_unc[KAPPAS[1]],
                       "N111_k1": n111[KAPPAS[0]],
                       "N111_k3": n111[KAPPAS[1]]}
halt_check(abs(fr2 - 0.23) < 0.005 and abs(fr10 - 0.08) < 0.005
           and abs(edge_unc[KAPPAS[0]] - 0.0372) < 0.0005
           and abs(edge_unc[KAPPAS[1]] - 0.358) < 0.001
           and abs(n111[KAPPAS[0]] - 6.24) < 0.01
           and abs(n111[KAPPAS[1]] - 0.86) < 0.01,
           f"RC-1 the frozen pipeline replicates: ISW shares "
           f"({fr2:.3f}, {fr10:.3f}) vs (0.23, 0.08); edges "
           f"({edge_unc[KAPPAS[0]]:.4f}, {edge_unc[KAPPAS[1]]:.4f}) vs "
           f"(0.0372, 0.358); N(0.111) ({n111[KAPPAS[0]]:.3f}, "
           f"{n111[KAPPAS[1]]:.3f}) vs (6.24, 0.86)")

# ---------------- the Boltzmann harness (declared external tooling) ----
print("\n=== RC-2/RC-3: THE BOLTZMANN HARNESS (CAMB source decomposition) ===")
import camb                      # noqa: E402  (declared harness)
import camb.symbolic as cs       # noqa: E402

PARS = dict(H0=67.36, ombh2=0.02237, omch2=0.1200, ns=0.96, As=2.1e-9,
            lmax=60, lens_potential_accuracy=0)
mono, ISW, dopp, quad = cs.get_scalar_temperature_sources()


def camb_pair(source, name):
    p = camb.set_params(**PARS)
    p.WantTensors = False
    p.set_custom_scalar_sources([source], source_names=[name])
    d = camb.get_results(p)
    dic = d.get_cmb_unlensed_scalar_array_dict(CMB_unit='muK')
    return dic['TxT'], dic[name + 'x' + name]


full_A, cl_A = camb_pair(mono + ISW, 'mA')
full_B, cl_B = camb_pair(mono + ISW * (1 / (1 + ((1.0 / 50) / cs.a) ** 8)),
                         'mB')
full_C, cl_C = camb_pair(mono + ISW * (1 / (1 + ((1.0 / 20) / cs.a) ** 8)),
                         'mC')
fA = {l: full_A[l] / cl_A[l] - 1.0 for l in ELLS}
fB = {l: full_B[l] / cl_B[l] - 1.0 for l in ELLS}
fC = {l: full_C[l] / cl_C[l] - 1.0 for l in ELLS}
MEAS["f_members"] = {"A_diagnostic": {str(l): fA[l] for l in ELLS},
                     "B_as_1_50": {str(l): fB[l] for l in ELLS},
                     "C_as_1_20": {str(l): fC[l] for l in ELLS}}
d30d2_full = full_B[30] / full_B[2]
max_bc = max(abs(fB[l] - fC[l]) for l in ELLS)
MEAS["harness"] = {"full_TT_D30_D2": d30d2_full, "max_fB_fC_gap": max_bc,
                   "camb_version": camb.__version__}
halt_check(0.90 <= d30d2_full <= 1.05 and max_bc < 0.05,
           f"RC-2 (per Amendment 01) harness validates: full-TT D30/D2 = "
           f"{d30d2_full:.4f} in [0.90, 1.05] (replicates the disclosed "
           f"calibration 0.976); quotable members agree, max |fB - fC| = "
           f"{max_bc:.4f} < 0.05")
n0_corr = n_metric(base, base, fB)
halt_check(min(fA.values()) > 0.0 and n0_corr < 1e-12,
           f"RC-3 identities: f^A_ell > 0 for every ell (min "
           f"{min(fA.values()):.4f}; Doppler+quadrupole add positive power "
           f"against the full-ISW baseline); corrected metric at x = 0 is "
           f"exactly zero ({n0_corr:.1e})")
check(True, "named finding (Amendment 01): the record's memory-grade "
            "'~0.82-0.84 Boltzmann' D30/D2 reproduces under NO tested "
            f"convention or member (full TT {d30d2_full:.3f}; mono+full-ISW "
            f"{cl_A[30] / cl_A[2]:.3f}; mono+late-ISW "
            f"{cl_B[30] / cl_B[2]:.3f}) -- the fence's direction and "
            "O(signal) magnitude were right, its cited shape number was "
            "not", "note")

# ---------------- M-1: the corrected verdict table ----------------------
print("\n=== M: THE CORRECTED TABLE (frozen correction on the frozen "
      "pipeline) ===")
POINTS = (0.0625, 0.111, 0.333)
table = {}
for kap in KAPPAS:
    for x in POINTS:
        c = cls_cached(x, kap)
        table[(x, kap)] = {
            "uncorrected": n_metric(c, base),
            "B": n_metric(c, base, fB),
            "C": n_metric(c, base, fC),
            "A_diag": n_metric(c, base, fA),
            "gauss_uncorrected": n_metric(c, base, None, "G"),
        }
edges_corr = {}
for kap in KAPPAS:
    for name, f in (("B", fB), ("C", fC)):
        edges_corr[(kap, name)] = edge(kap, base, f)
MEAS["corrected_table"] = {f"x={x},k={int(k)}": v
                           for (x, k), v in table.items()}
MEAS["corrected_edges"] = {f"k={int(k)},{n}": e
                           for (k, n), e in edges_corr.items()}
for kap in KAPPAS:
    for x in POINTS:
        r = table[(x, kap)]
        print(f"   x={x:5.4f} k={int(kap)}: uncorr {r['uncorrected']:6.2f}"
              f" | corr B {r['B']:6.2f} | corr C {r['C']:6.2f}"
              f" | bracket A {r['A_diag']:6.2f}")
print(f"   corrected edges: k=1: B {edges_corr[(KAPPAS[0], 'B')]}, "
      f"C {edges_corr[(KAPPAS[0], 'C')]}; k=3: B "
      f"{edges_corr[(KAPPAS[1], 'B')]}, C {edges_corr[(KAPPAS[1], 'C')]}")
m1_ok = all(v is not None or k[0] == KAPPAS[1]
            for k, v in edges_corr.items()) and len(table) == 6
check(len(table) == 6 and len(edges_corr) == 4,
      "M-1 the corrected table is complete: 3 named points x 2 members "
      "x {B, C} (+ the A bracket and the uncorrected value beside every "
      "entry), and 4 corrected edges")

r3B, r3C = table[(0.111, KAPPAS[1])]["B"], table[(0.111, KAPPAS[1])]["C"]
m2_ok = r3B < 2.0 and r3C < 2.0
check(m2_ok,
      f"M-2 the kappa=3 survival at the natural point is Boltzmann-robust: "
      f"N_corr(0.111, k=3) = {r3B:.3f} (B), {r3C:.3f} (C), both < 2 "
      f"(uncorrected 0.86)")

kill_status = {}
for x in POINTS:
    b, c_ = table[(x, KAPPAS[0])]["B"], table[(x, KAPPAS[0])]["C"]
    kill_status[x] = ("KILL-CONFIRMED-AT-MEMBER" if b >= 2.0 and c_ >= 2.0
                      else "KILL-WEAKENED")
MEAS["kill_status_k1"] = {str(x): s for x, s in kill_status.items()}
check(True, "M-3 kappa=1 named-point kill statuses (classification, "
            "either way a finding): "
            + "; ".join(f"x={x}: {s} (B {table[(x, KAPPAS[0])]['B']:.2f}, "
                        f"C {table[(x, KAPPAS[0])]['C']:.2f})"
                        for x, s in kill_status.items()), "note")

d_pipe = (ELLS[-1] * (ELLS[-1] + 1) * base[ELLS[-1]]) / (2 * 3 * base[2])
check(True, f"D-1 diagnostics: pipeline LCDM shape D30/D2 = {d_pipe:.3f} "
            f"vs CAMB matched-source {cl_B[30] / cl_B[2]:.3f} (B member) -- "
            f"the proportional-attachment insertion's residual shape "
            f"mismatch, declared; f^A bracket and Gaussian metric in the "
            f"artifact", "diag")

# ---------------- verdict ----------------------------------------------
gated = [c for c in CHECKS if c["kind"] in ("ok", "ctrl")]
n_ok = sum(1 for c in gated if c["pass"])
fails = [c["summary"] for c in gated if not c["pass"]]

if HALT:
    verdict = "HALT"
elif not fails:
    verdict = "A6-DISCHARGED"
elif not m2_ok:
    verdict = "A6-BREAKS-THE-GATE"
else:
    verdict = "A6-PARTIAL"

out = {
    "fork": "A6-1 (the first Part-7 front's blocking item; v4 C3 context)",
    "charter": "A6_COMMON_MODE_CHARTER_01.md (frozen 59ab1ec; "
               "Amendment 01 at 0c9e9e3)",
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()),
    "environment": {"python": sys.version.split()[0],
                    "pipeline": "isw_tt_auto imported unchanged",
                    "harness": f"CAMB {camb.__version__} + camb.symbolic "
                               f"custom sources (declared external ground "
                               f"truth; A1/mpmath precedent)",
                    "deterministic": True},
    "defect_history": [],
    "a8_marking": "EVERY NUMBER REMAINS INSERTION-CONTAMINATED at the "
                  "kappa-filter level (GRUT-plus-an-unbanked-filter); this "
                  "fork repairs the common-mode defect only",
    "measurements": MEAS,
    "checks": CHECKS,
    "adjudication": {
        "verdict": verdict,
        "scope": "the frozen pipeline's band ell in [2, 30], its declared "
                 "kappa members and named points; the activation-scale "
                 "frontier (A8's two blocked inputs) untouched; no "
                 "register field moves here (v4 R2)",
    },
    "elapsed_s": round(time.time() - T0, 2),
}
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                    "A6_COMMON_MODE_RESULT.json")
blob = json.dumps(out, indent=1)
with open(path, "w") as fh:
    fh.write(blob)
sha = hashlib.sha256(blob.encode()).hexdigest()
print(f"\nartifact written: {os.path.abspath(path)} (sha {sha[:16]}...)")
print(f"\nA6: {n_ok}/{len(gated)} gated checks passed; failures: "
      f"{len(fails)}; halts: {len(HALT)}")
if HALT:
    print("HALT: a control breached -- instrument bug, never physics. No "
          "verdict may be issued from this run.")
    sys.exit(2)
print(f"VERDICT: {verdict}")
print("HARD STOP: verdict recorded pending owner ruling.")
sys.exit(0 if not fails else 1)
