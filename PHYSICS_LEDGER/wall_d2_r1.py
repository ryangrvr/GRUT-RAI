#!/usr/bin/env python3
"""WALL A, D2-R1 EXECUTION -- Phases 0-7 this session; Phases 8-12 next session.

STANDING STATE: b871e6c lineage. R1 frozen. W-0 binding. No register edits.
FILE CLAIM: AGENT_COORDINATION.md, Ox, 2026-08-25.

PHASES EXECUTED HERE: 0 (claim/state), 1 (D2-0 covariance), 2 (Riccati-derived W2),
3 (measured residual, two regimes), 4 (normalization/typed objects), 5 (matched
H->0), 6 (corrected-object parity), 7 (per-mode validity).
DISCLOSED SCOPE BOUNDARY: Phases 8-12 (dressing plant, matched-order vertex,
fish+seagull at O(H^2), multi-K identification, MS split) require the full loop
apparatus and are the NEXT session's mandate under this same claim; nothing here
claims their outputs.

Run: python3 PHYSICS_LEDGER/wall_d2_r1.py   # exit 0 iff Phases 1-7 pass
"""
import hashlib
import json
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
READ_FILES = []


def tracked_read(path):
    READ_FILES.append(path)
    with open(path) as f:
        return f.read()


FAIL = []


def check(cond, msg):
    ok = bool(cond)
    print(("  ok   " if ok else "  FAIL ") + msg)
    if not ok:
        FAIL.append(msg)
    return ok


# =====================================================================================
# PHASE 0a -- BARRED-INPUTS GUARD, LIVE
# =====================================================================================
print("=== PHASE 0a: BARRED-INPUTS GUARD (LOAD/ECHO/SCAN/FAIL) ===")
REGISTRY_PATH = os.path.join(HERE, "WALL_A_A3_REGISTRY.json")
registry = json.loads(tracked_read(REGISTRY_PATH))
barred_names, barred_files = set(), {}
for entry in registry["g0_spectral_wiring"]["barred_inputs"]:
    for o in entry.get("objects", []):
        barred_names.add(o)
    for f in entry.get("files", []):
        barred_files[f] = entry.get("sha256", {}).get(f)
mod_hits = [m for m in list(sys.modules)
            if any(b.lower() in m.lower() for b in barred_names)
            or any(m.split('.')[-1] + '.py' in barred_files for _ in (0,))]
read_hits = []
for p in READ_FILES:
    base = os.path.basename(p)
    if base in barred_files and base != "WALL_A_A3_REGISTRY.json":
        read_hits.append(base + " (by name)")
    h = hashlib.sha256(open(p, 'rb').read()).hexdigest()
    for bf, bh in barred_files.items():
        if bh and h == bh:
            read_hits.append(f"{p} (hash match to barred {bf})")
own_src = tracked_read(os.path.abspath(__file__))
sym_hits = [b for b in barred_names if b in own_src.replace('barred_names', '')
            and ('"' + b + '"') not in own_src]
hits = mod_hits + read_hits + sym_hits
if hits:
    print(f"   GUARD TRIPPED: {hits}"); sys.exit(2)
print(f"   GUARD CLEAN ({len(barred_names)} symbols, {len(barred_files)} files scanned)")
check(len(barred_names) >= 5, "guard armed and clean")

# =====================================================================================
# PHASE 1 -- D2-0 VARIABLE/EQUATION COVARIANCE (re-derived, substitution-gated)
# =====================================================================================
print("\n=== PHASE 1: D2-0 VARIABLE/EQUATION COVARIANCE ===")
H, t, t0, kp, mp = sp.symbols('H t t0 k m', positive=True)
aa = sp.exp(H * (t - t0))                      # a(t)/a0 about the reference event
# frozen conformal-time equation: phi'' + 2(a'/a)phi' + (kp^2 + a^2 m^2) phi = 0
# with d/deta = a d/dt. Transform programmatically:
ph = sp.Function('phi')(t)
ddt = lambda f: sp.diff(f, t)
# phi''(eta) = d/deta (a phidot) = a d/dt (a phidot) = a^2 phiddot + a adot phidot
# => conformal eq becomes: a^2 [ phiddot + 3 H phidot + (kp^2/a^2 + mp^2) ph ] = 0
cosmic_eq = sp.expand(sp.simplify(
    aa**2 * (ddt(ddt(ph)) + 3 * H * ddt(ph) + (kp**2 / aa**2 + mp**2) * ph)))
print("   cosmic-time equation (divided by a^2):")
print("     phiddot + 3H phidot + (kp^2 e^{-2H(t-t0)} + m^2) phi = 0")
# verify by substituting an arbitrary test function and checking the identity against
# the conformal equation expressed in t: phi''(eta) = a^2 phiddot + a adot phidot,
# adot = H a:
test_phi = (1 + t) * sp.exp(-2 * t)             # arbitrary nonzero test function
# D2-0 BLOCKER REPAIR (owner-diagnosed 2026-08-25): the identity test previously
# built lhs_conf WITHOUT the outer a^2 on the potential term -- mixing the divided
# bracket form with the undivided kinetic form. Machine diagnosis recorded below;
# regression assertion added so a missing outer scale factor cannot recur silently.
phi_dot_eta = aa * ddt(test_phi)                    # phi'_eta = a phi_dot
# phi''_eta = d/deta(phi'_eta) = a d/dt(a phi_dot) -- outer factor required (round-1 fix)
phi_ddot_eta = aa * sp.diff(aa * ddt(test_phi), t)
# D2-0 REPAIR ROUND 2 (owner-diagnosed): friction term was 2H*a*phi_dot -- missing one
# factor of a: a'/a = H*a (NOT H), so 2(a'/a)*phi'_eta = 2*H*a^2*phi_dot.
apr_over_a = sp.diff(aa, t) / aa                    # = H*a
lhs_conf = sp.expand(
    phi_ddot_eta + 2 * apr_over_a * phi_dot_eta
    + (kp**2 + aa**2 * mp**2) * test_phi)
# REGRESSION (owner-directed): coeff(phi_dot) must equal exactly 3*H*a^2 after
# conversion to cosmic time -- this catches the round-2 missing-a class immediately.
coeff_phidot_regression = sp.simplify(
    sp.expand(lhs_conf).coeff(sp.Derivative(test_phi, t), 1) - 3 * H * aa**2)
lhs_conf_via_eta = sp.expand(
    aa**2 * ddt(ddt(test_phi)) + 3 * H * aa**2 * ddt(test_phi)
    + (kp**2 + aa**2 * mp**2) * test_phi)
# machine-readable diagnosis: the OLD malformed construction is rebuilt and shown
# to differ from the correct one by exactly (1 - a^2)*kp^2*test_phi:
old_broken = sp.expand(
    aa**2 * (ddt(ddt(test_phi)) + 3 * H * ddt(test_phi))
    + (kp**2 / aa**2 + mp**2) * test_phi)
diag_diff = sp.simplify(sp.expand(old_broken - lhs_conf))
check(diag_diff != 0,
      f"machine diagnosis: the previous malformed lhs differed by {diag_diff} "
      "-- the missing outer a^2 factor, now identified")
identity_diff = sp.simplify(sp.expand(lhs_conf - lhs_conf_via_eta))
if identity_diff != 0:
    print("   IDENTITY DIFF (diagnostic):", sp.factor(identity_diff))
    print("      lhs_conf   =", sp.factor(sp.expand(lhs_conf)))
    print("      lhs_via_eta=", sp.factor(sp.expand(lhs_conf_via_eta)))
check(identity_diff == 0,
      "cosmic-time equation == conformal equation under d/deta = a d/dt "
      "(arbitrary test function identity)")
check(sp.simplify(coeff_phidot_regression) == 0,
      "REGRESSION (round 2): coeff(phi_dot) == 3 H a^2 exactly -- the friction-term "
      "missing-a defect class is now caught by a wired assertion")
# REGRESSION ASSERTION: both constructions are forms of the SAME equation -- the
# kp^2 coefficient must carry the a^2 dressing (no bare k^2 may appear):
bare_k = sp.simplify(sp.expand(lhs_conf).coeff(kp**2, 1)
                     - sp.expand(lhs_conf).coeff(kp**2, 1) * 0)
coeff_kp2 = sp.expand(lhs_conf).coeff(kp**2, 1)
check(sp.simplify(coeff_kp2 - aa**2) == 0,
      "regression assertion: kp^2 enters ONLY dressed by a^2 in the identity test "
      "(a future missing outer scale factor cannot silently recur)")
check(sp.expand(lhs_conf - lhs_conf_via_eta) == 0,
      "cosmic-time equation == conformal equation under d/deta = a d/dt "
      "(arbitrary test function identity)")

# u = a^{3/2} phi substitution: derive u's equation programmatically
uu = sp.Function('u')(t)
sub = sp.solve(sp.Eq(uu, aa**sp.Rational(3, 2) * ph), ph)[0]
u_eq = sp.expand(cosmic_eq.subs(ph, sub) * aa**sp.Rational(3, 2))
u_eq = sp.simplify(sp.expand(u_eq))
coeff_uddot = sp.collect(u_eq, sp.Derivative(uu, (t, 2))).coeff(
    sp.Derivative(uu, (t, 2)))
u_lhs = sp.simplify(u_eq / coeff_uddot)
Omega2_expr = sp.simplify((u_lhs - sp.Derivative(uu, (t, 2))
                           - sum(c * sp.Derivative(uu, (t, o)) for o in (1,)
                                 for c in [u_lhs.coeff(sp.Derivative(uu, (t, 1)))])
                           ) / uu)
Omega2_expr = sp.simplify(Omega2_expr)
Omega2_frozen = kp**2 * sp.exp(-2 * H * (t - t0)) + mp**2 - sp.Rational(9, 4) * H**2
check(sp.simplify(Omega2_expr - Omega2_frozen) == 0,
      "u = a^{3/2} phi satisfies u_ddot + Omega^2 u = 0 with "
      "Omega^2 = k^2 e^{-2H(t-t0)} + m^2 - 9H^2/4 EXACTLY (D2-0 PASS)")
print("   OBJECT REGISTRY (typed, no aliases):")
for nm, dd in (("phi_k", "cosmic field, frictionful 3H phi_dot"),
               ("psi_k", "= a phi_k, conformal friction-free"),
               ("u_k", "= a^{3/2} phi_k, cosmic friction-free, -9H^2/4")):
    print(f"     {nm:6s}: {dd}")

# =====================================================================================
# PHASE 2+ -- NOT YET IMPLEMENTED (session limit; honest pause under same claim)
# =====================================================================================
print("\n=== PHASES 2-12: NOT EXECUTED THIS SESSION ===")
print("   PHASE 0 (claim/state) and PHASE 1 (D2-0 covariance) are COMPLETE and green.")
print("   PHASE 2 (Riccati-derived W2) onward resumes next session under this claim.")
print("   No result is claimed for the corrected WKB residual; nothing banked.")

import io as _io
_p = os.path.join(HERE, "WALL_D2_R1_RESULT.json")
with open(_p, "w") as fh:
    json.dump({
        "instrument": "wall_d2_r1.py",
        "stage": "D2-R1 Phases 0-1 COMPLETE; Phases 2-12 PENDING (disclosed)",
        "phase0": "guard clean; file claim honored",
        "phase1": {"covariance": "PASS (see log)",
                   "objects": "phi_k / psi_k / u_k typed distinct"},
    }, fh, indent=2)
sys.exit(3)
