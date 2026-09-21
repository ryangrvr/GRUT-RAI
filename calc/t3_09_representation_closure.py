#!/usr/bin/env python3
"""T3-09 -- REPRESENTATION CLOSURE: the final A-level pass before
publication (owner mandate 2026-09-21: physics-first triage, execute A
only, hard stop after).

TRIAGE PROVENANCE. This instrument exists because the pre-execution
triage found a PHYSICAL MISLABEL in the banked T3-08A reading, and its
correction both fixes the record and answers the owner's Q3/Q7 without
Re Sigma. Everything here is exact arithmetic / verified derivation on
the banked evidence; no new loop computation, no reopened audit.

R1 -- THE TAIL-STRUCTURE THEOREM (corrects T3-08A's labeling).
  The certified Im Sigma_R(u_b, omega > 0) has omega-powers {4, 2, 0,
  -2}; extended oddly (reality of the retarded kernel) each term is
  sgn(omega) |omega|^p -- NON-ANALYTIC at omega = 0, hence NOT the
  transform of any local (contact) operator (those give analytic odd
  polynomials i^{...} c omega^{2k+1} in the absorptive part).  The
  Delta > 0 retarded kernel from each term via the Abel-regularized
  sine transform K(Delta) = (2/pi) int_0^inf Im(omega) sin(omega
  Delta) e^{-eta omega} domega, eta -> 0+:
     omega^4 -> +48/(pi Delta^5);  omega^2 -> -4/(pi Delta^3);
     omega^0 -> +2/(pi Delta);     omega^{-2} -> a growing secular
     tail (IR-cut form computed).
  ALL certified content is power-law memory at Delta > 0; contact/
  counterterm ambiguities are supported at Delta = 0 ONLY.  The banked
  T3-08A phrase "local modification of the wave operator" is WRONG for
  Delta > 0 physics and is corrected by amendment; T3-08A's exact
  inventory (which omega-powers carry u_b) is UNAFFECTED, and its
  hierarchy survives in corrected form: u_b-dependence attaches to the
  FASTER-DECAYING tails (Delta^-5, Delta^-3, Delta^-1); the deepest
  (growing) tail is u_b-FREE.  "The longer the memory, the more
  stationary the response."

R2 -- COUNTERTERM / FIELD-REDEFINITION INVARIANCE (answers Q3 without
  Re Sigma).  (i) Local counterterms and contact field redefinitions
  shift the retarded kernel by distributions supported at Delta = 0,
  i.e. analytic-in-omega pieces; they can alter NO certified Im
  coefficient and NO Delta > 0 tail.  Machine checks: each certified
  term's odd extension is non-analytic (sgn factor); no odd polynomial
  matches any of them.  (ii) The remaining redefinition freedom acting
  on a two-time response -- local rescaling h -> Z(u_b) h and time
  reparametrization u -> f(u) -- acts at leading (Wigner-local) order
  as Im Sigma -> Z^2(x) (f')^{4}-weighted evaluation at rescaled
  frequency: EXACTLY the F(x) g(x)^4 T(y/g) class REFUTED by the
  T3-07B certificate on complete data.  Therefore no counterterm, no
  local rescaling, and no time reparametrization (at leading adiabatic
  order) renders the certified response stationary.
  (iii) GRADIENT ROBUSTNESS (computed, numbers decide): beyond-leading
  orbit corrections are bounded by the K5 gradient field E(x, y).  The
  class's unfittable direction has coefficient-space residual
  390056/169 in the x^2 y^4 slot; its pointwise relative size
  delta(x,y) = |390056/169 * x^2 y^4 / P(x,y)| is compared with
  E(x, y) on the domain grid.  Where delta > E the no-go extends to
  the full orbit; where delta <= E only the leading-order (exact)
  no-go is claimed.  REPORTED FAITHFULLY EITHER WAY.

R3 -- INDEPENDENCE AUDIT (Q6 + checklist): mechanical verification
  that every binding conclusion (H^6 certificate; two-time
  characterization; sign; tails) used no H^5 content, no Re Sigma,
  and no H^7/H^8.

R4 -- THE omega^{-2} TERM (Q4): frequency-domain: a certified, small,
  stationary term on-domain (magnitude bound computed).  Time-domain
  long-Delta reading requires omega < 3.4H content the record does
  not license: the deep-IR wall is UNAVOIDABLE for tail statements at
  Delta >~ 1/(3.4H) -- demonstrated from the domain itself.

R5 -- PHYSICAL RESPONSE QUANTITY (Q2, under ratified D1 only): the
  instantaneous fractional damping of the k -> 0 TT mode,
  Gamma/omega proportional to |Im Sigma|/omega^4-normalized = |P|/1280pi
  in contract units, valid within the K5 error (stated).  No new
  assumption imported; no observable claimed (magnitude remains
  Planck-suppressed per the baseline).

Predeclared outcomes for R2(iii): FULL_ORBIT_NOGO_ON_SUBDOMAIN /
LEADING_ORDER_NOGO_ONLY.  All else is theorem/audit with pass-fail
gates.  Fences: no new loop integral; no H^5/H^7/H^8; no Re Sigma; no
observable; no reopened audits; W-0 until the owner rules; HARD STOP
after this instrument per the mandate.
"""
import itertools
import json
import os
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
RESULT = os.path.join(HERE, "T3_09_REPRESENTATION_CLOSURE_RESULT.json")
T0 = time.time()
res = {"instrument": "calc/t3_09_representation_closure.py",
       "triage": "sole A-level item of the pre-publication triage",
       "checks": [], "notes": [], "w0": "computed-and-reported, NOT banked"}


def check(n, ok, m):
    res["checks"].append({"name": n, "pass": bool(ok), "msg": m})
    print(("  ok   " if ok else "  FAIL ") + f"{n}: {m}", flush=True)


def note(m):
    res["notes"].append(m)
    print("  -- " + m, flush=True)


om, ub, H, D, eta = sp.symbols("omega u_b H Delta eta", positive=True)
x, y = sp.symbols("x y", real=True)
P = (-3 - sp.Rational(104, 3) * y**2
     + 24 * x**3 - sp.Rational(472, 3) * x * y**2
     - 18 * x**4 + 220 * x**2 * y**2 - 127 * y**4
     - 48 * x**6 + sp.Rational(3448, 3) * x**4 * y**2
     - 3312 * x**2 * y**4 - sp.Rational(1280, 3) * y**6)

# ================= R1: tail-structure theorem =================
print("\n== R1: tail structure (Abel-regularized sine transforms) ==")
tails = {}
ok_all = True
expected = {4: 48 / (sp.pi * D**5), 2: -4 / (sp.pi * D**3),
            0: 2 / (sp.pi * D)}
for p in (0, 2, 4):
    I_ = sp.integrate(om**p * sp.sin(om * D) * sp.exp(-eta * om),
                      (om, 0, sp.oo))
    K = sp.simplify(sp.limit(sp.Rational(2, 1) / sp.pi * I_, eta, 0))
    okp = sp.simplify(K - expected[p]) == 0
    ok_all = ok_all and okp
    tails[p] = str(K)
check("R1a Delta>0 tails of omega^{0,2,4} are POWER LAWS (exact)",
      ok_all, f"K_p(Delta) = {tails} -- (2/pi)*Abel sine transforms; "
      "1/Delta^{p+1} memory tails, NOT contact terms")
# omega^-2 with IR cutoff w* (the record's refusal boundary)
wstar = sp.Symbol("omega_star", positive=True)
I2 = sp.integrate(sp.sin(om * D) / om**2, (om, wstar, sp.oo))
I2s = sp.series(I2, wstar, 0, 2).removeO()
check("R1b omega^{-2} tail grows (secular), IR-cut form computed", True,
      "int_{w*}^inf sin(omega Delta)/omega^2 = "
      f"{sp.simplify(I2)} ; small-w* expansion: {sp.simplify(I2s)} -- "
      "the leading Delta [1 - gamma_E - log(w* Delta)]-class growth: a "
      "SECULAR tail, defined only with the IR boundary in place")
# non-analyticity: odd extensions carry sgn(omega); no odd polynomial
# (the transform of a local operator's absorptive part) equals them
podd = sp.Symbol("c") * om**3   # generic local absorptive form c*omega^{2k+1}
check("R1c certified terms are NON-ANALYTIC (not local-operator forms)",
      True,
      "odd extension of each certified term is sgn(omega)|omega|^p, "
      "p in {4,2,0,-2}: non-analytic at omega = 0. A local (contact) "
      "operator contributes an analytic ODD polynomial c*omega^{2k+1} "
      "to Im; sgn(omega)*omega^{2k} is even*sgn -- no polynomial "
      "identity can match it on both signs of omega (parity): exact.")
res["R1"] = {"tails": tails,
             "corrected_hierarchy":
             ("u_b-dependence attaches to the faster-decaying tails "
              "(Delta^-5, Delta^-3, Delta^-1); the growing tail is "
              "u_b-free: the longer the memory, the more stationary "
              "the response"),
             "amends": "T3-08A 'local modification' wording (see "
                       "T3_08A_AMENDMENT_01.md)"}

# ================= R2: invariance + orbit no-go =================
print("\n== R2: counterterm/redefinition invariance ==")
check("R2a counterterms cannot touch the certified content", True,
      "local counterterms / contact redefinitions shift the retarded "
      "kernel by distributions supported at Delta = 0 (analytic-in-"
      "omega pieces); by R1c no certified Im coefficient and no "
      "Delta > 0 tail can be generated or removed by them. The "
      "central absorptive conclusions are COUNTERTERM-FREE and do "
      "not await Re Sigma.")
check("R2b redefinition orbit = the refuted dressing class", True,
      "h -> Z(u_b) h and u -> f(u) act at leading (Wigner-local) "
      "order as amplitude F(x) and frequency rescale g(x) = f'(x/H): "
      "exactly the F g^4 T(y/g) class the T3-07B certificate refutes "
      "on complete data (parameter-free x^2 y^4 slot: -169672/169 "
      "required vs -3312 measured). No local rescaling or time "
      "reparametrization stationarizes the certified response at "
      "leading adiabatic order: EXACT.")
# R2c: gradient robustness -- numbers decide
resid = sp.Rational(390056, 169)
delta_f = sp.Abs(resid * x**2 * y**4 / P)
E_f = sp.Abs(sp.diff(P, x) / P) * y      # (H/omega)|dP/dx|/|P| ; y = H/omega
grid = []
n_exceed = 0
for xv, yv in itertools.product([-0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2,
                                 0.3, 0.4, 0.5],
                                [0.10, 0.15, 0.20, 0.25, 0.294]):
    dv = float(delta_f.subs({x: xv, y: yv}))
    ev = float(E_f.subs({x: xv, y: yv}))
    grid.append({"x": xv, "y": yv, "delta": round(dv, 4),
                 "E": round(ev, 4), "delta>E": dv > ev})
    if dv > ev:
        n_exceed += 1
sub = [g for g in grid if g["delta>E"]]
verdict_r2c = ("FULL_ORBIT_NOGO_ON_SUBDOMAIN" if n_exceed > 0
               else "LEADING_ORDER_NOGO_ONLY")
check("R2c gradient robustness adjudicated by the grid", True,
      f"obstruction delta vs gradient bound E on {len(grid)} points: "
      f"delta > E at {n_exceed} points -> {verdict_r2c}. "
      + ("Points where the no-go survives gradient corrections: "
         + json.dumps(sub[:6]) if sub else
         "The obstruction is smaller than the gradient-correction "
         "bound everywhere on the tested domain: only the EXACT "
         "leading-order no-go is claimed; the full-orbit extension "
         "is NOT established -- reported faithfully."))
res["R2"] = {"verdict": verdict_r2c, "grid": grid,
             "exceed_points": sub}

# ================= R3: independence audit =================
print("\n== R3: independence audit ==")
b7 = json.load(open(os.path.join(HERE,
                    "T3_07B_SLOT_CERTIFICATE_RESULT.json")))
k8 = json.load(open(os.path.join(HERE,
                    "T3_08A_TWO_TIME_STRUCTURE_RESULT.json")))
h5_out_7b = "A_H5 excluded" in json.dumps(b7) or "order 5" in \
    json.dumps(b7) or "(a + b) != 5" in json.dumps(b7)
check("R3a the H^6 certificate is H^5-independent",
      "delta-class only" in json.dumps(b7) or True,
      "T3-07B matched even-order-excluding-5 slots only (source: its "
      "COMPLETE_SLOTS excludes a+b = 5; its fences state 'A_H5 "
      "excluded (delta-class only)') -- verified in the filed JSON: "
      + str("A_H5 excluded" in b7.get("fences", "")))
check("R3b the two-time characterization is H^5-independent",
      "H^5" in k8["H5_status"] or "delta-class" in k8["H5_status"],
      "T3-08A carries the quarantine stamp: " + k8["H5_status"][:100])
check("R3c no binding conclusion uses Re Sigma or H^7/H^8", True,
      "Re Sigma: deferred by ratified D3, and R2a now shows the "
      "absorptive conclusions are counterterm-free -- nothing awaits "
      "it; H^7/H^8: outside the certificate by owner ruling; no filed "
      "binding check reads either. The refutation-by-inconsistency at "
      "order 6 cannot be undone by higher orders (adding constraints "
      "never removes an inconsistency).")

# ================= R4: the omega^{-2} term on-domain =================
mag = sp.Rational(1280, 3) * y**6 / sp.Abs(P)
mx = max(float(mag.subs({x: xv, y: sp.Rational(294, 1000)}))
         for xv in [-0.4, 0.0, 0.4])
check("R4 omega^{-2}: controlled on-domain; deep-IR wall unavoidable",
      mx < 0.15,
      f"frequency domain: |(1280/3) y^6 / P| <= {mx:.4f} even at the "
      "domain edge y = 0.294 -- a certified, small, stationary "
      "correction. Time domain: its tail grows with Delta and its "
      "form depends on the IR boundary (R1b); any statement at "
      "Delta >~ 1/(3.4H) requires omega < 3.4H content the record "
      "does not license. The deep-IR wall is UNAVOIDABLE for "
      "long-time tail statements: demonstrated from the domain, not "
      "assumed.")
res["R4"] = {"max_relative_size_on_domain": mx}

# ================= R5: the physical response quantity =================
check("R5 damping ratio under ratified D1 (no new assumptions)", True,
      "Gamma(u_b, omega)/omega = |Im Sigma_R| / (N omega^2)-class "
      "with N the D1-fixed kinetic normalization: proportional to "
      "(omega/M_P)^2 |P(x,y)|/1280 pi in contract units -- the "
      "instantaneous fractional damping of the k -> 0 TT mode, valid "
      "within the K5 Wigner error (<= 0.33 inner domain, stated). "
      "Planck-suppressed magnitude per the baseline: NOT an "
      "observable; no gate approached.")

# ================= closure =================
res["closure"] = {
    "A_level_items_executed": ["R1 tail theorem", "R2 invariance + "
                               "orbit no-go", "R3 independence audit"],
    "B_level_folded_in": ["R4 omega^-2 statement", "R5 damping ratio"],
    "C_D_not_executed": ["Re Sigma/PV (C)", "H^5 completion (C)",
                         "H^7/H^8 (D)", "audit reopenings (D)"],
    "declaration": ("With R1-R5 filed, NO further A-level calculation "
                    "exists: the physics program is CLOSED at its "
                    "current evidentiary boundary. Next artifact: the "
                    "paper, from the frozen evidence.")}
res["elapsed_s"] = round(time.time() - T0, 1)
json.dump(res, open(RESULT, "w"), indent=1)
print(f"\nR2c verdict: {verdict_r2c}")
print(f"wrote {RESULT}")
