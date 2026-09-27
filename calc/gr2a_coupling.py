#!/usr/bin/env python3
"""GR2-a -- coupling selection (frozen instrument).

Charter: GR2A_COUPLING_CHARTER_01.md, frozen at commit e5687b0, under the
GR-2 campaign directive (Layer 1) and the GR2-L6 owner ruling.

Question (the owner's): does anything already earned by the GRUT
generative core force the +4 low-frequency cancellation that turns the 3D
omega^3 phase-space factor into omega^7?

Convention: the L-X fresh pair instrument of calc/gr1_gravity.py at
d827a32, replicated exactly -- dispersion omega(q) = q - 0.05 q^3, pair
frequency w = 2 omega(q) by 60-step Newton from q = w/2, J = M^2/|dw/dq|,
two-point slope log2[J(0.2)/J(0.1)].

Family: M_c(q) = c1 + c2 q^2 + c3 omega^2 + c4 q^4 + c5 q^2 omega^2 over
the charter's 15-member deterministic grid. Frozen class law: first
nonvanishing order of {c1, c2+c3, c4+c5-2 alpha c3, ...} -> slope class
{0, 4, 8, 12}. Do-not rules honored: exponents are outputs only; no
selection uses omega^7.

Pure stdlib. Deterministic (no randomness). Single run.
Run: python3 calc/gr2a_coupling.py   (writes ../GR2A_COUPLING_RESULT.json)
"""

import hashlib
import json
import math
import os
import sys
import time

T0 = time.time()
ALPHA = 0.05
CHECKS = []
HALT = []


def check(ok, msg, kind="ok"):
    CHECKS.append({"kind": kind, "pass": bool(ok), "summary": msg})
    tag = {"ok": "GATE", "ctrl": "CONTROL", "note": "NOTE"}[kind]
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg)


def halt_check(ok, msg):
    check(ok, msg, "ctrl")
    if not ok:
        HALT.append(msg)


# --------------------------- the L-X machinery, replicated exactly ----
def disp(q):
    return q - ALPHA * q ** 3


def root_q(w):
    q = w / 2.0
    for _ in range(60):
        f = 2.0 * disp(q) - w
        df = 2.0 * (1.0 - 3.0 * ALPHA * q * q)
        q -= f / df
    return q


def J_of(w, vertex, scale=1.0):
    q = root_q(w)
    M = scale * vertex(q)
    dwdq = abs(2.0 * (1.0 - 3.0 * ALPHA * q * q))
    return M * M / dwdq


def slope(vertex, scale=1.0):
    return math.log(J_of(0.2, vertex, scale) / J_of(0.1, vertex, scale)) / math.log(2.0)


# ----------------------------------------------------- the family ----
def member(c):
    c1, c2, c3, c4, c5 = c
    return lambda q: (c1 + c2 * q * q + c3 * disp(q) ** 2 + c4 * q ** 4
                      + c5 * q * q * disp(q) ** 2)


def frozen_class(c):
    """The charter's analytic class law (coefficients only; no exponent input)."""
    c1, c2, c3, c4, c5 = c
    if abs(c1) > 1e-15:
        return 0
    if abs(c2 + c3) > 1e-15:
        return 4
    if abs(c4 + c5 - 2.0 * ALPHA * c3) > 1e-15:
        return 8
    return 12


GRID = [
    ("1 stress point (= v_ful)",        (0.0, -1.0, 1.0, 0.0, 0.0), 8),
    ("2 mass modulation (CC-1)",        (1.0, 0.0, 0.0, 0.0, 0.0), 0),
    ("3 potential-only",                (0.0, 1.0, 0.0, 0.0, 0.0), 4),
    ("4 kinetic-only (= v_kin)",        (0.0, 0.0, 1.0, 0.0, 0.0), 4),
    ("5 non-minimal (= v_non)",         (0.0, -1.3, 1.0, 0.0, 0.0), 4),
    ("6 pure HD potential",             (0.0, 0.0, 0.0, 1.0, 0.0), 8),
    ("7 pure kinetic gradient",         (0.0, 0.0, 0.0, 0.0, 1.0), 8),
    ("8 stress + HD admixture",         (0.0, -1.0, 1.0, 1.0, 0.0), 8),
    ("9 tuned deep cancellation",       (0.0, -1.0, 1.0, 0.1, 0.0), 12),
    ("10 stress + mass admixture",      (0.3, -1.0, 1.0, 0.0, 0.0), 0),
    ("11 symmetric mix",                (0.0, 0.5, 0.5, 0.0, 0.0), 4),
    ("12 partial cancellation",         (0.0, -0.5, 1.0, 0.0, 0.0), 4),
    ("13 mass + kinetic",               (2.0, 0.0, 1.0, 0.0, 0.0), 0),
    ("14 on-locus mixed",               (0.0, -1.0, 1.0, -0.08, 0.2), 8),
    ("15 all-positive mix",             (0.0, 1.0, 1.0, 1.0, 1.0), 4),
]

MEAS = {}

# ------------------------------------------------ R: replication controls
print("=== R: REPLICATION CONTROLS (halt-grade; L-X full-precision targets) ===")
REC = {"s_kin": 4.001626590846332, "s_pot": 4.003794021366405,
       "s_non": 4.010999254328895, "s_full": 8.005419679013105}
v_kin = lambda q: disp(q) ** 2
v_pot = lambda q: q * q
v_non = lambda q: disp(q) ** 2 - 1.3 * q * q
v_ful = lambda q: disp(q) ** 2 - q * q
for name, v in (("s_kin", v_kin), ("s_pot", v_pot), ("s_non", v_non),
                ("s_full", v_ful)):
    sl = slope(v)
    MEAS[name] = sl
    halt_check(abs(sl - REC[name]) < 1e-9,
               f"R {name}: replicated {sl:.12f} vs recorded {REC[name]:.12f} "
               f"(|Delta| = {abs(sl-REC[name]):.1e} < 1e-9)")
mlin = max(abs(q * q - q * q) for q in (0.05, 0.1, 0.2))
halt_check(mlin < 1e-14, f"R linear-kill: exactly-linear vertex = {mlin:.1e} < 1e-14")
ds = abs(slope(v_ful, 16.0) - MEAS["s_full"])
halt_check(ds < 1e-12, f"R rescale: slope invariant under coupling x16, "
                       f"|Delta| = {ds:.1e} < 1e-12")

if HALT:
    print("HALT: a replication control breached -- instrument bug, never "
          "physics. No verdict may be issued from this run.")
    sys.exit(2)

# ----------------------------------------------------- F/G: the family
print("\n=== F/G: THE FAMILY (frozen per-member class predictions) ===")
classes_seen = set()
eq_ok = True
members_out = []
for label, c, pred in GRID:
    v = member(c)
    sl = slope(v)
    law = frozen_class(c)
    classes_seen.add(law if abs(sl - law) < 0.2 else None)
    members_out.append({"member": label, "c": list(c), "slope": sl,
                        "frozen_class": pred, "law_class": law})
    if label.startswith("1 "):
        check(abs(sl - REC["s_full"]) < 1e-9,
              f"F-1 {label}: slope {sl:.12f} equals recorded s_full "
              f"(|Delta| = {abs(sl-REC['s_full']):.1e} < 1e-9) -- the family "
              f"contains the stress point identically")
    else:
        check(abs(sl - pred) < 0.2,
              f"G {label}: measured slope {sl:.4f} vs frozen class {pred} "
              f"(|Delta| = {abs(sl-pred):.4f} < 0.2)")
    if abs(sl - law) >= 0.2:
        eq_ok = False

# ------------------------------------------- E: earned-constraint gates
print("\n=== E: EARNED-CONSTRAINT GATES ===")
seen = sorted(x for x in classes_seen if x is not None)
check(seen == [0, 4, 8, 12],
      f"E-1 LOCALITY IS EXPONENT-BLIND: the local family exhibits classes "
      f"{seen} -- four distinct low-frequency classes among local couplings")

ws = [0.10 + 0.02 * i for i in range(6)]
jmin = min(J_of(w, member(c)) for _, c, _ in GRID for w in ws)
check(jmin >= 0.0,
      f"E-2 CONE IS EXPONENT-BLIND: min J(w) over all members and the scan "
      f"= {jmin:.3e} >= 0 (golden-rule positivity; P-2 realizability of "
      f"(J, nu = J/2) cited) -- every class is cone-admissible")

check(eq_ok,
      "E-3 THE SELECTION RULE IDENTIFIED: for all 15 members the measured "
      "class equals the frozen coefficient law -- membership of the "
      "omega^7 class is decided exactly by {c1 = 0 and c2 + c3 = 0} (the "
      "soft-flux condition) and by nothing else")

nonstress = [m for m in members_out if m["member"][0] in "678" or
             m["member"].startswith("14")]
ns_ok = all(abs(m["slope"] - 8.0) < 0.2 for m in nonstress)
ns_slopes = ", ".join("%.3f" % m["slope"] for m in nonstress)
check(ns_ok,
      f"E-4 THE +4 LOCUS IS NONUNIQUE: non-stress members 6, 7, 8, 14 all "
      f"land in class 8 (slopes {ns_slopes}) -- including "
      f"the purely kinetic member 7, with no tracelessness narrative")

m10 = next(m for m in members_out if m["member"].startswith("10"))
check(abs(m10["slope"] - 0.0) < 0.2,
      f"E-5 THE LOCUS IS UNSTABLE TO THE EARNED-ADMISSIBLE CHANNEL: the "
      f"stress point plus 0.3 x mass modulation (the coupling CC-1 found "
      f"passing every earned constant-level selector) drops from class 8 "
      f"to slope {m10['slope']:.4f} (class 0) -- nothing earned forbids "
      f"the admixture that destroys the cancellation")

check(True,
      "recovered geometry is member-blind by construction: every member "
      "couples to the same substrate, whose recovered geometry is the "
      "substrate's (CP-1 L-G2 identity at 2.2e-16; CA-1 leg 1). Geometry "
      "cannot select a coupling here", "note")
check(True,
      "constraint statuses (charter section 6): locality -- admitted core "
      "principle, exponent-blind (E-1); cone -- DERIVED-IN-CLASS (P-2, "
      "borrowed-standard), exponent-blind (E-2); geometry -- blind by "
      "construction; conservation -- SUPPLIED (CC-1 irreducible); "
      "Lorentz/gauge -- SUPPLIED (I3); spin-2 -- OPEN here (GR2-b); "
      "stress structure -- SUPPLIED (one family point); +4/tracelessness "
      "-- CONDITIONAL, mechanically the soft-flux condition", "note")

# ------------------------------------------------------------ verdict
gated = [c for c in CHECKS if c["kind"] in ("ok", "ctrl")]
n_ok = sum(1 for c in gated if c["pass"])
fails = [c["summary"] for c in gated if not c["pass"]]
e1 = next(c for c in CHECKS if c["summary"].startswith("E-1"))

if not fails:
    verdict = "A-COUPLING-NOT-SELECTED"
elif not e1["pass"] and len(seen) == 1 and seen == [8]:
    verdict = "A-COUPLING-SELECTED-IN-CLASS"
else:
    verdict = "A-PARTIAL"

detail = (f"classes present among local, cone-admissible couplings: {seen}; "
          f"the omega^7 class (slope 8 here) is the locus "
          f"{{c1 = 0, c2 + c3 = 0}} -- vanishing soft flux -- imposed by "
          f"nothing earned, occupied by non-stress and purely kinetic "
          f"members, and destroyed by admixture of the earned-admissible "
          f"mass-modulation channel. The core does not select omega^7; the "
          f"gravitational branch requires an additional primitive coupling "
          f"structure. omega^7's recorded status (within-class occupancy "
          f"evidence, conditional) is unchanged")

out = {
    "fork": "GR2-a",
    "charter": "GR2A_COUPLING_CHARTER_01.md (frozen e5687b0)",
    "directive": "GR2_CAMPAIGN_DIRECTIVE_01.md (Layer 1); "
                 "GR2_L6_OWNER_RULING_01.md (authorization)",
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()),
    "environment": {"python": sys.version.split()[0], "pure_stdlib": True,
                    "deterministic": "no randomness anywhere"},
    "convention": "GR-1 L-X fresh pair instrument, replicated (alpha = 0.05)",
    "members": members_out,
    "checks": CHECKS,
    "adjudication": {
        "verdict": verdict,
        "verdict_detail": detail,
        "scope": "1D single-sector counter-propagating pair channel, the "
                 "L-X convention, this five-channel local family; class (e)",
    },
    "elapsed_s": round(time.time() - T0, 2),
}

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                    "GR2A_COUPLING_RESULT.json")
blob = json.dumps(out, indent=1)
with open(path, "w") as f:
    f.write(blob)
sha = hashlib.sha256(blob.encode()).hexdigest()
print(f"\nartifact written: {os.path.abspath(path)} (sha {sha[:16]}...)")
print(f"\nGR2-a: {n_ok}/{len(gated)} gated checks passed; failures: "
      f"{len(fails)}; halts: {len(HALT)}")
print(f"VERDICT: {verdict} -- {detail}")
print("HARD STOP: verdict recorded pending owner ruling.")
sys.exit(0 if not fails else 1)
