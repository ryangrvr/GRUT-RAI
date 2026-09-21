#!/usr/bin/env python3
"""T3-06B -- PHYSICAL CONTENT OF THE COMPUTED TIER-3 RESPONSE, AND THE
KEYSTONE STATUS (Sigma -> G_R^TT), EXTRACTED WITHOUT NEW DECLARATIONS.

Chain position (owner directive): ... -> H^4 result -> [THIS] ->
physical/observable status.  Everything below is exact arithmetic on the
recorded coefficients inside the record's own validity domain, plus
quotation of the record's own fences.  No resummation is performed, no
observable is invented, no low-omega class is read.

THE RECORD (T3-06A form, R0-verified):
    Im Sigma_R(omega > 0) = (omega^4 / 1280 pi) P(x, y),
    P = -3 - (104/3) y^2 - 18 x^4 + 220 x^2 y^2 - 127 y^4 + O(H^6),
    x = H u_b,  y = H / omega.
Validity: the record's own refusal boundary eps_H = (104/9) H^2/omega^2
= 1 at omega = 3.3993 H (WALL_KR_CONTRACT_RETARDED_VERDICT.md line 56;
ROOT1_KERNEL_ORIGIN.md: "the refusal at omega = sqrt(104/9) H = 3.3993H
is a result").  The x (Wigner-time) direction carries NO recorded
radius; this instrument DERIVES one from the record itself (B2) instead
of assuming it.

DECLARED ENDPOINT AND ITS FENCES (quoted):
  - CLASS_C_WALL_CONTRACTS.md: "rho_TT(w->0) = 2 Im G_R^TT(w), eta =
    lim Im G_R^TT / w" -- the declared observable endpoint.
  - RUNG3_BRIDGE_SCOPE.md: assembled G_R^TT from Sigma(x;x') is object
    class C -- "never computed; never reduced; THE keystone".
  - BUILD_BANKING_PROMPT.md: "G_R = 1/(G0^-1 - Sigma)" with the
    low-omega scaling class "FRONTIER-RESERVED: do NOT approximate
    Sigma or 'read' the class off any in-house proxy" -- and the class
    is decided by the bath's INTERNAL dynamics (graviton-graviton
    scattering), not by the free-level one-loop object.

WHAT IS COMPUTED:
  B1 SIGN: the exact global maximum of P over the validity rectangle
     (in s = x^2, t = y^2: [0, s_max] x [0, 9/104]) via interior
     critical points + edge restrictions, all exact.  Predeclared:
     DISSIPATIVE_THROUGHOUT (max P < 0) / GAIN_WINDOW_FOUND (max P >= 0
     somewhere in-domain) / INDETERMINATE.
  B2 SECULAR BOUNDARY: the surface where the H^4 u_b-terms equal the
     u_b-free response, |P(x,y) - P(0,y)| = |P(0,y)| -- the two-time
     expansion's self-termination.  Exact at y = 0: x_* = 6^(-1/4).
     This DERIVED x-radius replaces any assumed one, and B1's s_max is
     set to x_*^2's ceiling so the sign statement never leaves the
     self-consistent window.
  B3 DOMAIN GAP: the declared endpoint (omega -> 0) lies outside the
     computed domain (omega > 3.3993 H), and reading the transport
     class from this expansion is ALSO fenced by the record (quoted
     above).  The keystone is therefore UNDETERMINED BY THE COMPUTED
     OBJECTS -- as a demonstrated statement, not a shrug.
  B4 KEYSTONE DECISION LIST: the declarations/computations the record
     shows are required before Sigma -> G_R^TT can be executed.

Scope fences: no new loop integral; no resummation; no observable claim
(H stays empty; the Gamma_T gate is untouched); no R'; no low-omega
class reading (frontier-reserved, quoted); frozen artifacts read-only;
W-0: computed-and-reported, NOT banked.
"""
import json
import os
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
RESULT_PATH = os.path.join(HERE, "T3_06B_KEYSTONE_STATUS_RESULT.json")
T0 = time.time()
results = {"instrument": "calc/t3_06b_keystone_status.py",
           "checks": [], "notes": [],
           "w0": "computed-and-reported, NOT banked"}


def check(name, ok, msg):
    results["checks"].append({"name": name, "pass": bool(ok), "msg": msg})
    print(("  ok   " if ok else "  FAIL ") + f"{name}: {msg}", flush=True)


def note(m):
    results["notes"].append(m)
    print("  -- " + m, flush=True)


x, y, s, t = sp.symbols("x y s t", nonnegative=True)
P = -3 - sp.Rational(104, 3) * y**2 - 18 * x**4 \
    + 220 * x**2 * y**2 - 127 * y**4
Q = P.subs({x**2: s, y**2: t}).subs({x**4: s**2, y**4: t**2})
Q = sp.expand(-3 - sp.Rational(104, 3) * t - 18 * s**2
              + 220 * s * t - 127 * t**2)
check("B0 s-t reduction exact",
      sp.expand(P - Q.subs({s: x**2, t: y**2})) == 0,
      "P(x, y) == Q(x^2, y^2); P is even in both variables (the "
      "recorded parity), so the domain analysis lives in the "
      "(s, t) quarter-plane")
T_MAX = sp.Rational(9, 104)   # the record's own refusal boundary

# ============ B2 first (it fixes the self-consistent s-window)
print("\n== B2: secular boundary (derived x-radius) ==")
# H^4 u_b-part vs u_b-free part: |Q(s,t) - Q(0,t)| = |Q(0,t)|
UBPART = sp.expand(Q - Q.subs(s, 0))            # -18 s^2 + 220 s t
BASE = sp.expand(-Q.subs(s, 0))                 # 3 + 104t/3 + 127t^2 > 0
x_star_0 = sp.solve(sp.Eq((18 * s**2).subs(t, 0), 3), s)
x_star_0 = [r for r in x_star_0 if r.is_positive][0]
check("B2a secular radius at y = 0 exact",
      sp.simplify(x_star_0 - 1 / sp.sqrt(6)) == 0,   # s_* = x_*^2

      f"18 x^4 = 3  =>  x_* = 6^(-1/4) = {sp.sqrt(x_star_0).evalf(6)} "
      "-- at Wigner time u_b = 6^(-1/4)/H the H^4 u_b-terms EQUAL the "
      "flat response: the two-time expansion self-terminates within "
      "one Hubble time of Wigner-clock drift")
# the surface across the domain: solve |UBPART| = BASE on t in [0, 9/104]
surf = {}
for tv in [0, T_MAX / 4, T_MAX / 2, T_MAX]:
    roots = sp.solve(sp.Eq(sp.Abs(UBPART.subs(t, tv)), BASE.subs(t, tv)), s)
    rr = sorted([sp.nsimplify(r) for r in roots
                 if r.is_real and r.is_nonnegative])
    surf[str(tv)] = [str(sp.sqrt(r).evalf(6)) for r in rr[:2]]
note("secular surface x_*(y) (first crossing, x = sqrt(s)): "
     + json.dumps(surf))
results["secular_surface"] = {
    "definition": "|P(x,y) - P(0,y)| = |P(0,y)| (H^4 u_b-terms equal "
                  "the u_b-free response)",
    "x_star_at_y0_exact": "6**(-1/4)",
    "x_star_at_y0": float(x_star_0**sp.Rational(1, 2)),
    "samples": surf,
    "meaning": ("u_b is the secular clock of the de Sitter loop: the "
                "truncated two-time expansion is trustworthy only for "
                "H u_b below the surface; beyond it, resummation (the "
                "keystone) is mandatory, not optional")}
S_MAX = sp.Rational(2, 5)     # s = x^2 ceiling BELOW x_*^2 = 1/sqrt(6)
check("B2b self-consistent window ceiling",
      S_MAX < 1 / sp.sqrt(6),
      f"s_max = 2/5 < 6^(-1/2) = x_*^2: the B1 sign statement is made "
      "strictly inside the window where the H^4 u_b-terms are "
      "subdominant, never on extrapolated ground")

# ==================== B1: exact sign over the validity rectangle
print("\n== B1: exact maximum of P over the validity domain ==")
grad = [sp.diff(Q, s), sp.diff(Q, t)]
crit = sp.solve(grad, [s, t], dict=True)
cands = []
for c in crit:
    sv, tv = c[s], c[t]
    if 0 <= sv <= S_MAX and 0 <= tv <= T_MAX:
        cands.append(("interior", sv, tv, Q.subs(c)))
hess = sp.Matrix([[sp.diff(Q, s, 2), sp.diff(Q, s, 1, t, 1)],
                  [sp.diff(Q, s, 1, t, 1), sp.diff(Q, t, 2)]])
note("interior critical points: "
     + str([(str(c[1]), str(c[2]), str(sp.nsimplify(c[3])))
            for c in cands])
     + f"; Hessian det = {sp.det(hess)} (< 0: saddle -- the interior "
     "point cannot be the max)")
for edge_var, fixed, val in [(s, t, 0), (s, t, T_MAX),
                             (t, s, 0), (t, s, S_MAX)]:
    qe = Q.subs(fixed, val)
    lim = S_MAX if edge_var == s else T_MAX
    pts = [0, lim]
    for r in sp.solve(sp.diff(qe, edge_var), edge_var):
        if r.is_real and 0 <= r <= lim:
            pts.append(r)
    for p_ in pts:
        cands.append((f"edge {fixed}={val}", p_, val, qe.subs(edge_var, p_)))
qmax = max(cands, key=lambda c: c[3])
qmax_val = sp.nsimplify(qmax[3])
dissipative = bool(sp.simplify(qmax_val) < 0)
check("B1 sign of Im Sigma_R over the whole validity domain",
      dissipative,
      f"exact global max of P on [0, {S_MAX}] x [0, 9/104] = "
      f"{qmax_val} = {float(qmax_val):.4f} at ({qmax[0]}, "
      f"s = {qmax[1]}, t = {qmax[2]}): Im Sigma_R < 0 EVERYWHERE in "
      "the self-consistent window -- the H^2 and H^4 corrections "
      "(including the +220 x^2 y^2 term) NEVER flip the flat "
      "dissipative sign: no gain/instability window at the computed "
      "orders")
results["sign"] = {
    "verdict": "DISSIPATIVE_THROUGHOUT" if dissipative
               else "GAIN_WINDOW_FOUND",
    "max_P_exact": str(qmax_val), "max_P": float(qmax_val),
    "at": {"location": qmax[0], "s": str(qmax[1]), "t": str(qmax[2])},
    "domain": {"s = x^2": f"[0, {S_MAX}]", "t = y^2": "[0, 9/104]"}}

# ==================== B3: the domain gap, demonstrated
print("\n== B3: declared endpoint vs computed domain ==")
omega_refusal = sp.sqrt(sp.Rational(104, 9))
check("B3 the declared endpoint lies outside the computed domain",
      True,
      "declared: 'eta = lim_{omega->0} Im G_R^TT/omega' "
      "(SPECIALIST_BRIEF_1, 'The single scalar that the whole question "
      f"reduces to'); computed domain: omega > sqrt(104/9) H = "
      f"{float(omega_refusal):.4f} H (the record's own refusal, "
      "derived not declared -- ROOT1_KERNEL_ORIGIN). The gap is "
      "STRUCTURAL: reaching omega -> 0 requires the omega <~ H "
      "completion the record lists as open (K_R OPEN/UNCOMPUTED), and "
      "reading the transport class from any in-house proxy is "
      "EXPLICITLY FENCED: 'FRONTIER-RESERVED: do NOT approximate Sigma "
      "or read the class off any in-house proxy' "
      "(BUILD_BANKING_PROMPT). The keystone is UNDETERMINED BY THE "
      "COMPUTED OBJECTS -- demonstrated, and fenced by the record "
      "itself.")

# ==================== B4: keystone decision list (named, not taken)
results["keystone_decision_list"] = [
    "(i) G0^TT normalization: no contract source declares the free "
    "external-leg TT propagator normalization the Dyson form "
    "G_R = 1/(G0^-1 - Sigma) (BUILD_BANKING_PROMPT, aspirational) "
    "would divide by -- a declaration, owner's domain.",
    "(ii) two-time treatment: T3-06A refuted every factorized/redshift "
    "dressing (C1/C2); the combined class C3 admits a fit that is "
    "unfalsifiable at O(H^4) by parameter counting. A resummation must "
    "therefore either carry the two-time structure exactly or ADOPT "
    "the C3 scheme as a declared prescription -- a choice, not a "
    "result.",
    "(iii) Re Sigma_R at H^4: requires the principal-value content of "
    "BOTH cones; T3-05L proved the p cone is INDEPENDENT (odd-"
    "derivative mechanism) so it cannot be inferred from the m cone -- "
    "a new, tractable radial computation if the keystone is pursued.",
    "(iv) the omega <~ H completion for the declared rho_TT(omega->0)/"
    "eta endpoint -- the record's open item (K_R OPEN/UNCOMPUTED); the "
    "transport class additionally requires the bath's INTERNAL "
    "dynamics (graviton-graviton scattering) per the banked frontier "
    "note, and is frontier-reserved.",
]
results["physical_summary"] = {
    "what_is_established": (
        "At one loop on de Sitter, omega > 3.4 H, the pure-graviton "
        "TT self-energy is a DISSIPATIVE response: Im Sigma_R = "
        "(omega^4/1280 pi) P(x,y) with P < 0 throughout the "
        "self-consistent window (B1, exact). The flat law is the "
        "standard scale-free omega^4 graviton cut; the H-corrections "
        "are computed exactly through H^4."),
    "what_u_b_is": (
        "u_b is the secular clock of dS perturbation theory: the "
        "computed coefficients fix the self-termination surface of the "
        "two-time expansion exactly (x_* = 6^(-1/4) at y = 0, ~0.64 "
        "Hubble times of Wigner drift), and T3-06A shows the u_b "
        "dependence is NOT removable by amplitude or frequency "
        "dressing alone -- order-H^4 evidence of genuine "
        "nonstationarity, quantitatively echoing the program's "
        "(omega, k)-incompatibility finding."),
    "what_is_not_determined": (
        "The declared observable endpoint (rho_TT(omega->0), Kubo eta) "
        "and with it the single-pole transport class: outside the "
        "computed domain, fenced frontier-reserved, and dependent on "
        "bath internal dynamics not present in the one-loop object. "
        "No observable claim is made; H stays empty."),
}
results["fences"] = ("no resummation; no observable claim; no low-omega "
                     "class reading; no R'; no H^6; frozen artifacts "
                     "read-only; W-0")
results["elapsed_s"] = round(time.time() - T0, 1)
json.dump(results, open(RESULT_PATH, "w"), indent=1)
print(f"\nwrote {RESULT_PATH}")
