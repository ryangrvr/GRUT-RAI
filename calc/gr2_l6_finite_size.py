#!/usr/bin/env python3
"""GR2-L6 -- the 3D red gate's finite-size law (frozen instrument).

Charter: GR2_L6_FINITE_SIZE_CHARTER_01.md, frozen at commit 29ee4d7
(Amendment 01, pre-run disclosed control repair, at 5d5b270), under the
GR-2 campaign directive (GR2_CAMPAIGN_DIRECTIVE_01.md, Layer 6).

Object under study: the L-D 3D pair-count exponent exactly as frozen in
calc/gr1_gravity.py at d827a32 -- open-chain per-axis spectrum
c_k = 2 - 2 cos(pi k / s), 3D tensor cube, all-zero mode excluded,
unordered pairs (self-pairs included) with omega_i + omega_j <= W,
two-point slope S(s) = log2[P(1.8)/P(0.9)].

Pre-registered (sealed in the charter before any new number existed):
  S_inf = 6.2147 (midpoint continuum, frozen window [0.9, 1.8])
  b1    = 22.571 (analytic surface-mode coefficient, quadrature)
  c2    = 150.58 (calibrated on the public sizes 13/21/31 only; disclosed)
  Blind sizes: S(45)=5.7874, S(63)=5.8943, S(91)=5.9848, S(121)=6.0384,
               S(131)=6.0511, each +/-0.05; crossing gate S(131) > 6.
  Counterfactual: no-plane variants flip the bias sign (N-1, N-2).
  Curvature law: continuum slope on [0.45, 0.9] = 6.054 +/- 0.04.

The GR-1 3D gate (5.362 vs 6 +/- 0.6) is RED and STAYS RED under every
outcome of this instrument. Nothing here is a re-adjudication.

Pure stdlib. Deterministic (no randomness anywhere). Single run.
Run: python3 calc/gr2_l6_finite_size.py   (writes ../GR2_L6_RESULT.json)
"""

import bisect
import hashlib
import json
import math
import os
import sys
import time

T0 = time.time()
CHECKS = []
HALT = []  # control breaches: instrument bugs, never physics


def check(ok, msg, kind="ok"):
    CHECKS.append({"kind": kind, "pass": bool(ok), "summary": msg})
    tag = {"ok": "GATE", "ctrl": "CONTROL", "note": "NOTE"}[kind]
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg)


def halt_check(ok, msg):
    check(ok, msg, "ctrl")
    if not ok:
        HALT.append(msg)


# ---------------------------------------------------------------- spectra
def open_modes(s):
    """The GR-1 L-D construction, replicated exactly."""
    cs = [2.0 - 2.0 * math.cos(math.pi * k / s) for k in range(s)]
    return sorted(math.sqrt(a + b + c) for a in cs for b in cs for c in cs
                  if a + b + c > 1e-12)


def noplane_modes(s):
    """Counterfactual: the same cube with the k = 0 plane dropped per axis."""
    cs = [2.0 - 2.0 * math.cos(math.pi * k / s) for k in range(1, s)]
    return sorted(math.sqrt(a + b + c) for a in cs for b in cs for c in cs)


def mid3_modes(M):
    """Midpoint continuum quadrature grid (no boundary planes)."""
    cs = [2.0 - 2.0 * math.cos(math.pi * (k + 0.5) / M) for k in range(M)]
    return sorted(math.sqrt(a + b + c) for a in cs for b in cs for c in cs)


def mid2_modes(M):
    """Midpoint grid for the theta_3 = 0 plane spectrum."""
    cs = [2.0 - 2.0 * math.cos(math.pi * (k + 0.5) / M) for k in range(M)]
    return sorted(math.sqrt(a + b) for a in cs for b in cs)


# ------------------------------------------------------------- pair count
def pairs(oms, W):
    """Unordered pairs i <= j with omega_i + omega_j <= W (as in gr1_gravity)."""
    n = 0
    for i, w in enumerate(oms):
        if w > W:
            break
        n += bisect.bisect_right(oms, W - w, lo=i) - i
    return n


def slope(oms, wlo=0.9, whi=1.8):
    return math.log(pairs(oms, whi) / pairs(oms, wlo)) / math.log(2.0)


MEAS = {}

# ---------------------------------------------------- R: replication controls
print("=== R: REPLICATION CONTROLS (halt-grade; Amendment 01 tolerance 5e-7) ===")
PUBLIC = {13: 5.361664, 21: 5.492996, 31: 5.662049}
for s, ref in PUBLIC.items():
    sl = slope(open_modes(s))
    MEAS[f"S_open_{s}"] = sl
    halt_check(abs(sl - ref) < 5e-7,
               f"R-1 s={s}: replicated slope {sl:.6f} vs recorded {ref:.6f} "
               f"(|Delta| = {abs(sl-ref):.2e} < 5e-7)")

if HALT:
    print("HALT: a replication control breached -- instrument bug, never "
          "physics. No verdict may be issued from this run.")
    sys.exit(2)

# ------------------------------------------------------- C: analytic side
print("\n=== C: CONTINUUM / ANALYTIC GATES ===")
om101 = mid3_modes(101)
S101 = slope(om101)
om121 = mid3_modes(121)
S121 = slope(om121)
MEAS["S_inf_M101"], MEAS["S_inf_M121"] = S101, S121
check(abs(S121 - 6.2147) < 0.002,
      f"C-1a: continuum slope (M=121) = {S121:.4f} vs sealed 6.2147 "
      f"(|Delta| = {abs(S121-6.2147):.4f} < 0.002)")
check(abs(S121 - S101) < 0.002,
      f"C-1b: quadrature convergence |S(121) - S(101)| = "
      f"{abs(S121-S101):.2e} < 0.002")

Slow = slope(om121, 0.45, 0.9)
MEAS["S_inf_lowwindow"] = Slow
check(abs(Slow - 6.054) < 0.04,
      f"C-2: continuum slope on the halved window [0.45, 0.9] = {Slow:.4f} "
      f"vs quadratic-curvature prediction 6.054 (|Delta| = "
      f"{abs(Slow-6.054):.4f} < 0.04)")

# b1 from quadrature: qhat(W) = q23/p3 with the M=101 bulk and M2=1001 plane
N3 = len(om101)
om2 = mid2_modes(1001)
N2 = len(om2)


def F3(x):
    return bisect.bisect_right(om101, x) / N3


qh = {}
for W in (0.9, 1.8):
    p3 = 2.0 * pairs(om101, W) / N3 ** 2
    tot = 0.0
    for x in om2:
        if x > W:
            break
        tot += F3(W - x)
    qh[W] = (tot / N2) / p3
b1 = 3.0 * (qh[0.9] - qh[1.8]) / math.log(2.0)
MEAS["qhat_09"], MEAS["qhat_18"], MEAS["b1"] = qh[0.9], qh[1.8], b1
check(abs(b1 - 22.571) < 0.1,
      f"C-3: surface-mode coefficient b1 = {b1:.3f} (quadrature) vs sealed "
      f"22.571 (|Delta| = {abs(b1-22.571):.3f} < 0.1)")
del om2

# ------------------------------------------------------------ B: blind sizes
print("\n=== B: BLIND SIZES (predictions frozen in the charter) ===")
PRED = {45: 5.7874, 63: 5.8943, 91: 5.9848, 121: 6.0384, 131: 6.0511}
SEALED = {"S_inf": 6.2147, "b1": 22.571, "c2": 150.58}
S131 = None
for s, pred in PRED.items():
    om = open_modes(s)
    sl = slope(om)
    MEAS[f"S_open_{s}"] = sl
    MEAS[f"P09_{s}"], MEAS[f"P18_{s}"] = pairs(om, 0.9), pairs(om, 1.8)
    del om
    check(abs(sl - pred) < 0.05,
          f"B s={s}: measured slope {sl:.4f} vs frozen prediction {pred:.4f} "
          f"(|Delta| = {abs(sl-pred):.4f} < 0.05)")
    surf = SEALED["b1"] / s
    curv = SEALED["S_inf"] - 6.0
    check(True,
          f"decomposition s={s}: deficit vs S_inf = {SEALED['S_inf']-sl:+.4f} "
          f"(surface term -b1/s = {-surf:.4f}; c2/s^2 = "
          f"{SEALED['c2']/s**2:+.4f}); window curvature above 6 = {curv:+.4f}",
          "note")
    if s == 131:
        S131 = sl

check(S131 > 6.000,
      f"B-6 CROSSING GATE: S(131) = {S131:.4f} > 6.000 -- the slope passes "
      f"THROUGH 2d = 6 and keeps rising toward S_inf = {S121:.4f}: the "
      f"sequence does not converge to 6")

# --------------------------------------------- N: mechanism counterfactuals
print("\n=== N: SIGN-FLIP COUNTERFACTUALS (no-plane variants) ===")
for s, gate in ((13, "N-1"), (31, "N-2")):
    sl = slope(noplane_modes(s))
    MEAS[f"S_noplane_{s}"] = sl
    if gate == "N-1":
        check(sl > S121,
              f"N-1 s=13 no-plane: slope {sl:.4f} > S_inf {S121:.4f} -- the "
              f"bias flips sign when the boundary planes are removed "
              f"(with-plane value was {MEAS['S_open_13']:.4f})")
    else:
        hi = S121 + 2.0 * SEALED["b1"] / 31.0
        check(S121 < sl <= hi,
              f"N-2 s=31 no-plane: slope {sl:.4f} in ({S121:.4f}, {hi:.4f}] "
              f"(with-plane value was {MEAS['S_open_31']:.4f})")

check(True,
      "wording note: the GR-1 diagnostic's 'lowest mode sits at 24% of the "
      "window edge' refers to the absolute value omega_min(13) = "
      f"{2.0*math.sin(math.pi/26.0):.3f}; that is 27% of the 0.9 edge and "
      "13% of the 1.8 edge", "note")

# ------------------------------------------------------------------ verdict
gated = [c for c in CHECKS if c["kind"] in ("ok", "ctrl")]
n_ok = sum(1 for c in gated if c["pass"])
fails = [c["summary"] for c in gated if not c["pass"]]
b_gates = [c for c in CHECKS if c["kind"] == "ok" and c["summary"].startswith("B")]
b_all = all(c["pass"] for c in b_gates)
all_pass = not fails

if all_pass:
    verdict = "L6-MECHANISM-DERIVED"
elif b_all:
    verdict = "L6-MECHANISM-PARTIAL"
else:
    verdict = "L6-MODEL-REFUTED"

detail = (f"S_inf(window [0.9,1.8]) = {S121:.4f} (= 6 dimensional "
          f"{S121-6.0:+.4f} lattice-curvature window offset); deficit law "
          f"S(s) = S_inf - b1/s + c2/s^2 with analytic b1 = {b1:.3f}; "
          f"S(131) = {S131:.4f} vs 6; GR-1 3D gate UNCHANGED, RED")

adjud = {
    "verdict": verdict,
    "verdict_detail": detail,
    "gr1_3d_gate": "RED, unchanged (5.362 vs frozen 6 +/- 0.6); this fork "
                   "re-adjudicates nothing",
    "scope": "the L-D pair-count object of gr1_gravity.py, frozen window "
             "[0.9, 1.8]; open-chain tensor-cube spectra; class (b) lattice",
}

out = {
    "fork": "GR2-L6",
    "charter": "GR2_L6_FINITE_SIZE_CHARTER_01.md (frozen 29ee4d7; "
               "Amendment 01 at 5d5b270)",
    "directive": "GR2_CAMPAIGN_DIRECTIVE_01.md (Layer 6)",
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()),
    "environment": {"python": sys.version.split()[0], "pure_stdlib": True,
                    "deterministic": "no randomness anywhere"},
    "sealed_constants": SEALED,
    "measurements": {k: v for k, v in sorted(MEAS.items())},
    "checks": CHECKS,
    "adjudication": adjud,
    "elapsed_s": round(time.time() - T0, 2),
}

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                    "GR2_L6_RESULT.json")
blob = json.dumps(out, indent=1)
with open(path, "w") as f:
    f.write(blob)
sha = hashlib.sha256(blob.encode()).hexdigest()
print(f"\nartifact written: {os.path.abspath(path)} (sha {sha[:16]}...)")
print(f"\nGR2-L6: {n_ok}/{len(gated)} gated checks passed; failures: "
      f"{len(fails)}; halts: {len(HALT)}")
print(f"VERDICT: {verdict} -- {detail}")
print("HARD STOP: verdict recorded pending owner ruling.")
sys.exit(0 if not fails else 1)
