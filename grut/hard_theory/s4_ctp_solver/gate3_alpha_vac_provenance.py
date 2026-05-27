#!/usr/bin/env python3
"""
Gate 3 Alpha_vac Provenance Audit

The CTP action term audit established that R = sqrt(4/3) follows from

    alpha_vac = 1/3  =>  n_g(0)^2 = 1 + alpha_vac = 4/3  =>  R = sqrt(4/3)

This audit answers the five book-readiness questions about alpha_vac:

    Q1: Where does alpha_vac = 1/3 enter the GRUT action?
    Q2: Is it derived from TT projection, vacuum susceptibility, or
        dimensional averaging — and is the route explicit?
    Q3: Is it independent of R? (must not be reverse-engineered)
    Q4: Does it survive convention changes?
    Q5: Does it match the cited KS 2011 path?

Key finding: TWO ROUTES, different epistemic status

  Route 1 — v11 Appendix H (NARRATIVE, not physics):
    "alpha = 1/d, d = 3 spatial dimensions"
    Motivational, not a calculation. Not a recognized published result.
    Does NOT appear in KS 2011, Duff 1994, or any standard text.
    Status: ASSERTION (per ALPHA_VAC_PROVENANCE.md April 2026 audit).

  Route 2 — KS 2011 / Duff 1994 trace anomaly (PUBLISHED, EXACT):
    For a real conformally-coupled scalar in 4D curved spacetime:
      (a, c) = (1, 3)  [in standard units; per KS 2011 eq A.5 and Duff 1994]
      a/c = 1/3  EXACTLY.
    This IS a published, verifiable, convention-independent result.
    Status: EXACT, PUBLISHED, INDEPENDENT OF R.

  The load-bearing identification (GRUT-specific):
    "The gravitational conformal mode acts as a real conformally-coupled
    scalar — the IR carrier of vacuum response."
    If this identification holds: alpha_vac = a/c = 1/3 is a derived result.
    If not: alpha_vac = 1/3 remains an axiom.

Book-ready conclusion:
  Route 2 (KS 2011 / Duff 1994) is the correct provenance chain.
  Replace the v11 App H "alpha = 1/d" language with:
    "alpha_vac = a/c = 1/3 for a real conformally-coupled scalar
    (KS 2011 eq A.5 / Duff 1994 eq 30-31), given the identification of
    the gravitational conformal mode as the IR scalar carrier."
  The identification step is the load-bearing claim; it requires its own
  justification chapter.

Spec: gate3-alpha-vac-provenance-spec-v1.0
Date: 2026-05-26
"""

import json
import math
import numpy as np
from fractions import Fraction
from pathlib import Path
from datetime import datetime

SPEC_VERSION = "gate3-alpha-vac-provenance-spec-v1.0"
SPEC_DATE    = "2026-05-26"

# ── Per-species trace anomaly coefficients (KS 2011 / Duff 1994) ─────────────
#
# Source: Komargodski-Schwimmer 2011 arXiv:1107.3987, Appendix A eq (A.4)-(A.6)
#         Duff 1994 arXiv:hep-th/9308075, eqs (30)-(31)
#
# Units: 1/(360 * (4*pi)^2) = 1/(90 * (8*pi)^2)
#
# Both sources agree exactly on these values (no convention ambiguity).
#
#   Species              (a,  c)         a/c
#   Real scalar (conf.)  (1,  3)         1/3    <- alpha_vac
#   Weyl fermion         (11/2, 9)       11/18
#   Gauge field (+ gh.)  (62, 36)        31/18

TRACE_ANOMALY = {
    "real_scalar": {
        "species":      "Real scalar (conformally coupled)",
        "a":            Fraction(1),
        "c":            Fraction(3),
        "source":       "KS 2011 eq (A.5); Duff 1994 eq (30)-(31)",
        "description":  "Single real scalar with xi = 1/6 conformal coupling",
    },
    "weyl_fermion": {
        "species":      "Weyl fermion",
        "a":            Fraction(11, 2),
        "c":            Fraction(9),
        "source":       "KS 2011 eq (A.5); Duff 1994 eq (30)-(31) [1 Dirac = 2 Weyl]",
        "description":  "Single Weyl (chiral) fermion",
    },
    "gauge_field": {
        "species":      "Gauge field (vector + ghosts)",
        "a":            Fraction(62),
        "c":            Fraction(36),
        "source":       "KS 2011 eq (A.5); Duff 1994 eq (30)-(31)",
        "description":  "Non-abelian gauge boson including FP ghost contribution",
    },
}


# ── Q1: Where does alpha_vac enter the GRUT action? ──────────────────────────

ACTION_ENTRY_POINT = {
    "term":        "S_const = -(1/2) ∫∫ h_a K^R h_r d^4x d^4x'",
    "kernel":      "K^R = alpha_vac * chi(omega) * P^TT",
    "DC_limit":    "K^R(0) = alpha_vac * P^TT = (1/3) P^TT",
    "mechanism":   "Constitutive cross-term in linearized gravitational CTP action",
    "file":        "grut/derivation/phi_munu/linearized_ctp_action.py",
    "result":      "n_g(0)^2 = 1 + alpha_vac = 4/3  =>  R = sqrt(4/3)",
    "answer":      "alpha_vac enters as the coefficient of the TT-projected constitutive kernel",
}


# ── Q2: Which derivation route is used? ──────────────────────────────────────

def route_comparison() -> dict:
    """
    Compare Route 1 (v11 App H) and Route 2 (KS 2011 / Duff 1994).

    Only Route 2 is a genuine published-physics derivation.
    """
    scalar = TRACE_ANOMALY["real_scalar"]
    a_over_c = scalar["a"] / scalar["c"]

    return {
        "Route_1_v11_AppH": {
            "formula":   "alpha = 1/d = 1/3  (d = 3 spatial dimensions)",
            "source":    "v11.1 Genesis Codex Appendix H §H.4",
            "argument":  "Bulk->brane dimensional reduction of trace anomaly",
            "status":    "ASSERTION — narrative, not a published physics result",
            "problems": [
                "No intermediate calculation in §H.4",
                "The 'α = 1/d' formula does not appear in KK theory, trace anomaly literature, or viscoelastic theory",
                "'Conformal projection of trace anomaly' is not a recognized technical term",
                "Standard KK results depend on compactification details, not simply on d",
            ],
            "verdict":   "Not suitable for a published paper; must be replaced",
        },
        "Route_2_KS2011_Duff1994": {
            "formula":   "a/c = 1/3 for a real conformally-coupled scalar",
            "source":    "KS 2011 arXiv:1107.3987 eq (A.5); Duff 1994 arXiv:hep-th/9308075 eq (30)-(31)",
            "argument":  "Standard 4D trace anomaly: T^mu_mu = a E_4 - c W^2; (a,c) = (1,3) for real scalar",
            "a_over_c":  float(a_over_c),
            "a_over_c_exact": str(a_over_c),
            "matches_alpha_vac": a_over_c == Fraction(1, 3),
            "status":    "PUBLISHED — textbook result, two independent source confirmations",
            "properties": [
                "Exact rational (not approximation)",
                "Convention-independent: both KS 2011 and Duff 1994 agree",
                "Reproducible from heat kernel theory",
                "Does NOT require knowledge of R to compute",
            ],
            "verdict":   "Correct provenance route for the book",
        },
        "identification_step": {
            "claim":   "The gravitational conformal mode acts as a real conformally-coupled scalar",
            "status":  "GRUT-SPECIFIC IDENTIFICATION (load-bearing)",
            "if_holds": "alpha_vac = a/c = 1/3 is derived, not assumed",
            "if_not":   "alpha_vac = 1/3 remains an axiom (as per April 2026 audit)",
            "what_is_needed": (
                "A chapter showing that the conformal mode of the metric in 4D "
                "gravitational CTP theory IS a real conformally-coupled scalar "
                "(ξ = 1/6 coupling), and that this identification is NOT reverse-engineered "
                "from R = sqrt(4/3)."
            ),
        },
    }


# ── Q3: Is alpha_vac = 1/3 independent of R? ─────────────────────────────────

def independence_check() -> dict:
    """
    Test whether alpha_vac = 1/3 can be computed without knowing R.

    Route 2 computation order:
      1. List SM field content (scalars, fermions, gauge bosons)
      2. Look up per-species (a, c) from Duff 1994 Table 1
      3. For a single real scalar: (a, c) = (1, 3) => a/c = 1/3
      4. Identify gravitational conformal mode as a real scalar
      5. alpha_vac = a/c = 1/3
      6. [THEN] n_g(0) = sqrt(1 + 1/3) = sqrt(4/3) = R

    Step 5 precedes Step 6. The computation of a/c = 1/3 uses ONLY:
      - Duff 1994 per-species coefficients (published)
      - The identification of the conformal mode (GRUT-specific)
    It does NOT use R anywhere.

    Historical check: was 1/3 reverse-engineered?
      Per ALPHA_VAC_PROVENANCE.md Stage 1e:
        v6 claimed a/c = 4/3 from holographic SCFT (the value came first)
        v11 then provided "alpha = 1/d, d = 3" as narrative
      This suggests the historical route WAS reverse-engineered.
      BUT: Route 2 (a/c = 1/3 for a scalar from Duff 1994) is NOT
      reverse-engineered — it is an independent published calculation
      that happens to give the same value.
    """
    scalar = TRACE_ANOMALY["real_scalar"]
    a_over_c = scalar["a"] / scalar["c"]

    # Simulate Route 2 computation: compute a/c without knowing R
    a_val = float(scalar["a"])
    c_val = float(scalar["c"])
    alpha_from_trace_anomaly = a_val / c_val

    R_target = math.sqrt(4.0 / 3.0)
    # Now compute R from alpha — note R is computed AFTER alpha, not before
    R_from_alpha = math.sqrt(1.0 + alpha_from_trace_anomaly)

    return {
        "computation_order": [
            "Step 1: Duff 1994 per-species (a,c) for real scalar: (1, 3)",
            "Step 2: a/c = 1/3  [no R used]",
            "Step 3: Identify conformal mode as real scalar",
            "Step 4: alpha_vac = a/c = 1/3  [still no R used]",
            "Step 5: n_g(0) = sqrt(1 + 1/3) = sqrt(4/3) = R  [R computed last]",
        ],
        "alpha_from_trace_anomaly":      float(alpha_from_trace_anomaly),
        "R_computed_after_alpha":        float(R_from_alpha),
        "R_computed_equals_R_target":    abs(R_from_alpha - R_target) < 1e-12,
        "R_used_in_alpha_computation":   False,
        "route_2_independent":           True,
        "historical_caveat": (
            "The HISTORICAL route was reverse-engineered: v6 had a/c = 4/3 from holography, "
            "v11 provided 'alpha = 1/d' as narrative. But Route 2 (Duff 1994 a/c for scalar) "
            "is a published calculation that does NOT require knowing R beforehand. "
            "The fact that it gives the same answer as the historical claim does not make "
            "it circular — it makes it an independent confirmation."
        ),
        "independence_verdict": "INDEPENDENT via Route 2. Historical route was circular; Route 2 is not.",
    }


# ── Q4: Convention invariance ─────────────────────────────────────────────────

def convention_check() -> dict:
    """
    Does a/c = 1/3 survive normalization convention changes?

    The trace anomaly T^mu_mu = a E_4 - c W^2 with (a,c) = (1,3) for a scalar
    is written in units of 1/(360 (4pi)^2). In other normalizations:

    Convention A (KS 2011):    (a, c) = (1, 3)             -> a/c = 1/3
    Convention B (Duff 1994):  N_S=1: b = 1/120(4pi)^2,
                                       b' = -1/360(4pi)^2   -> |b'|/b = 1/3
    Convention C (N * norm):   (a, c) -> (N*a, N*c)         -> a/c = 1/3 (invariant)

    The ratio a/c is DIMENSIONLESS and NORMALIZATION-INDEPENDENT.
    Both sources give exactly a/c = 1/3 for a real conformally-coupled scalar.
    """
    scalar = TRACE_ANOMALY["real_scalar"]

    # Convention A: (a,c) = (1,3) — KS 2011 units
    a_A = Fraction(1)
    c_A = Fraction(3)
    ratio_A = a_A / c_A

    # Convention B: from Duff 1994 eq (30)-(31) for N_S = 1 scalar
    # b (Weyl^2 coeff) = 1/(120*(4pi)^2) for N_S = 1
    # b' (Euler coeff) = -1/(360*(4pi)^2) for N_S = 1
    # |b'|/b = (1/360)/(1/120) = 120/360 = 1/3
    b_prime_abs = Fraction(1, 360)
    b            = Fraction(1, 120)
    ratio_B      = b_prime_abs / b

    # Convention C: overall scale factor N (normalization choice)
    N = Fraction(7, 3)   # arbitrary
    a_C = N * a_A
    c_C = N * c_A
    ratio_C = a_C / c_C

    return {
        "convention_A_KS2011": {
            "a": str(a_A), "c": str(c_A), "a_over_c": str(ratio_A),
            "equals_1_3": ratio_A == Fraction(1, 3),
        },
        "convention_B_Duff1994": {
            "b_prime_abs": str(b_prime_abs), "b": str(b), "ratio": str(ratio_B),
            "equals_1_3": ratio_B == Fraction(1, 3),
        },
        "convention_C_rescaled": {
            "scale_N": str(N), "a": str(a_C), "c": str(c_C), "a_over_c": str(ratio_C),
            "equals_1_3": ratio_C == Fraction(1, 3),
        },
        "invariant": True,
        "verdict": "a/c = 1/3 is CONVENTION-INDEPENDENT: an exact rational ratio that survives all normalization changes",
    }


# ── Q5: Does it match the KS 2011 citation? ──────────────────────────────────

def ks2011_path_check() -> dict:
    """
    Does the KS 2011 route actually support alpha_vac = 1/3?

    KS 2011 (arXiv:1107.3987) Appendix A gives per-species trace anomaly:
      Real scalar (conformally coupled): (a, c) = (1, 3) in standard units
      => a/c = 1/3

    This is IN the KS 2011 paper (eq A.5 table). The v11 App H claim
    "alpha = 1/d from dimensional reduction" is NOT in KS 2011.

    The closure_protocol.py docstring correctly cites KS 2011 for a/c = 1/3.
    The ALPHA_VAC_PROVENANCE.md (April 2026) correctly noted that KS 2011
    does not contain "alpha = 1/d" — but it was checking the v11 App H
    CLAIM against KS 2011, not the a/c = 1/3 claim.

    Resolution: TWO DIFFERENT CLAIMS were both attributed to KS 2011:
      (a) "alpha = 1/d from dimensional reduction" -> NOT in KS 2011 (v11 App H)
      (b) "a/c = 1/3 for real conformally-coupled scalar" -> IS in KS 2011
    Only (b) is valid. The book should cite (b), not (a).
    """
    scalar = TRACE_ANOMALY["real_scalar"]

    return {
        "claim_a_v11_AppH": {
            "statement":  "alpha = 1/d from conformal projection of trace anomaly under dimensional reduction",
            "in_KS2011":  False,
            "in_Duff1994": False,
            "status":     "NOT SUPPORTED by cited papers; v11 App H narrative only",
        },
        "claim_b_KS2011_Duff1994": {
            "statement":  "a/c = 1/3 for a real conformally-coupled scalar",
            "reference":  "KS 2011 arXiv:1107.3987 eq (A.5); Duff 1994 arXiv:hep-th/9308075 eq (30)-(31)",
            "a":          str(scalar["a"]),
            "c":          str(scalar["c"]),
            "a_over_c":   str(scalar["a"] / scalar["c"]),
            "in_KS2011":  True,
            "in_Duff1994": True,
            "status":     "SUPPORTED — textbook result in two independent published sources",
        },
        "what_ALPHA_VAC_PROVENANCE_found": (
            "April 2026 audit found 'alpha = 1/d' not in KS 2011 — CORRECT, "
            "but it was checking Claim (a), not Claim (b). "
            "Claim (b) IS in KS 2011 and is the correct provenance. "
            "The resolution: closure_protocol.py's updated docstring citing "
            "'KS 2011 a/c = 1/3 for real scalar' is correct. The April audit's "
            "finding (about Claim a) and the current code (about Claim b) are "
            "BOTH correct and not in conflict."
        ),
        "book_citation": (
            "Cite KS 2011 arXiv:1107.3987 eq (A.5) and Duff 1994 arXiv:hep-th/9308075 "
            "eq (30)-(31) for 'a/c = 1/3 for a real conformally-coupled scalar'. "
            "Do NOT cite KS 2011 for 'alpha = 1/d from dimensional reduction'."
        ),
    }


# ── Sensitivity: Omega_Lambda vs alpha_vac ───────────────────────────────────

def sensitivity_analysis() -> dict:
    """
    Omega_Lambda vs alpha_vac (from ALPHA_VAC_PROVENANCE.md Stage 4).

    The cosmological formula H_inf = (2-R)/(S*tau_0) with:
      S = 12*pi/alpha_vac^2  (screening factor)
      R = sqrt(1 + alpha_vac)
      tau_0 = 41.9 Myr (fixed)
      H_0 = 70 km/s/Mpc (fixed)

    Omega_Lambda = (H_inf/H_0)^2
    (Note: full formula involves other factors; this is the leading-order
     sensitivity check from ALPHA_VAC_PROVENANCE.md.)
    """
    tau_0_myr = 41.9
    tau_0_s   = tau_0_myr * 3.15576e13  # Myr -> seconds
    H_0_hz    = 70.0 * 1e3 / 3.0857e22  # km/s/Mpc -> Hz
    planck_OL = 0.6889

    alpha_vals = [0.25, 0.27, 1.0/3.0, 0.40, 0.50]
    rows = []
    for alpha in alpha_vals:
        S  = 12.0 * math.pi / alpha**2
        R  = math.sqrt(1.0 + alpha)
        H_inf = (2.0 - R) / (S * tau_0_s)
        OL = (H_inf / H_0_hz)**2 if H_inf > 0 else float('nan')
        rows.append({
            "alpha_vac": alpha,
            "alpha_exact": "1/3" if abs(alpha - 1.0/3.0) < 1e-9 else str(round(alpha, 3)),
            "S": float(S),
            "R": float(R),
            "H_inf_Hz": float(H_inf),
            "Omega_Lambda": float(OL) if not math.isnan(OL) else "nan",
            "planck_deviation_pct": float(100*(OL - planck_OL)/planck_OL) if not math.isnan(OL) else "nan",
            "physical": (0 < OL < 1) if not math.isnan(OL) else False,
        })

    canonical = next(r for r in rows if abs(r["alpha_vac"] - 1.0/3.0) < 1e-9)
    return {
        "rows": rows,
        "canonical": canonical,
        "sensitivity_verdict": (
            "Only alpha_vac near 1/3 gives physically sensible Omega_Lambda "
            "in the Planck range. alpha = 1/4 gives 0.24; alpha = 1/2 gives >1. "
            "The framework genuinely requires alpha near 1/3; this is load-bearing."
        ),
        "planck_val": planck_OL,
    }


# ── Summary: five questions answered ─────────────────────────────────────────

def five_question_summary() -> dict:
    """Compact answers to Ryan's five book-readiness questions."""
    return {
        "Q1_where_enters_action": {
            "answer": "Constitutive cross-term S_const: K^R = alpha_vac * chi(omega) * P^TT",
            "status": "IDENTIFIED",
        },
        "Q2_derivation_route": {
            "answer": (
                "Route 2 (KS 2011 / Duff 1994): a/c = 1/3 for real conformally-coupled scalar. "
                "NOT Route 1 (v11 App H 'alpha = 1/d' narrative, which is an assertion). "
                "The load-bearing step is the identification: conformal mode = real scalar."
            ),
            "status": "ROUTE 2 IS EXPLICIT AND PUBLISHED; identification step needs its own chapter",
        },
        "Q3_independent_of_R": {
            "answer": (
                "YES via Route 2: a/c = 1/3 is computed from Duff 1994 coefficients "
                "before R is defined. Historical route was circular (v6 had 4/3 first). "
                "Route 2 is not circular."
            ),
            "status": "INDEPENDENT (Route 2)",
        },
        "Q4_convention_invariance": {
            "answer": "YES: a/c = 1/3 is dimensionless and normalization-independent. KS 2011 and Duff 1994 agree exactly.",
            "status": "CONFIRMED",
        },
        "Q5_KS2011_match": {
            "answer": (
                "YES for Claim (b): 'a/c = 1/3 for real scalar' IS in KS 2011 eq (A.5). "
                "NO for Claim (a): 'alpha = 1/d from dimensional reduction' is NOT in KS 2011. "
                "The closure_protocol.py docstring cites Claim (b) — correct. "
                "v11 App H cites Claim (a) — not supported."
            ),
            "status": "RESOLVED: Route 2 matches KS 2011; Route 1 does not",
        },
    }


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 80)
    print("Gate 3 Alpha_vac Provenance Audit")
    print(f"Spec: {SPEC_VERSION}")
    print(f"Start: {datetime.now().isoformat()}")
    print("=" * 80)

    repo_root = Path(__file__).resolve().parents[3]

    # ── 1. Per-species trace anomaly coefficients ───────────────────────────
    print("\n1. Per-species trace anomaly (KS 2011 / Duff 1994)")
    print("-" * 60)
    for k, v in TRACE_ANOMALY.items():
        a_over_c = v["a"] / v["c"]
        print(f"  {v['species']:<40}  (a,c) = ({v['a']}, {v['c']})  a/c = {a_over_c}")
    scalar = TRACE_ANOMALY["real_scalar"]
    print(f"\n  Real scalar: a/c = {scalar['a']}/{scalar['c']} = 1/3 = alpha_vac  [EXACT, PUBLISHED]")

    # ── 2. Route comparison ─────────────────────────────────────────────────
    print("\n2. Route comparison: v11 App H vs KS 2011 / Duff 1994")
    print("-" * 60)
    rc = route_comparison()
    r1 = rc["Route_1_v11_AppH"]
    r2 = rc["Route_2_KS2011_Duff1994"]
    print(f"  Route 1 (v11 App H):       {r1['status']}")
    print(f"  Route 2 (KS 2011 / Duff):  {r2['status']}")
    print(f"  a/c from Route 2 = {r2['a_over_c_exact']} = {r2['a_over_c']:.10f}")
    print(f"  a/c == 1/3: {r2['matches_alpha_vac']}")
    print(f"\n  Identification step: {rc['identification_step']['status']}")

    # ── 3. Independence check ───────────────────────────────────────────────
    print("\n3. Independence: is alpha_vac = 1/3 computed before R?")
    print("-" * 60)
    ic = independence_check()
    for step in ic["computation_order"]:
        print(f"  {step}")
    print(f"\n  alpha_vac from trace anomaly: {ic['alpha_from_trace_anomaly']:.10f}")
    print(f"  R computed after alpha:       {ic['R_computed_after_alpha']:.10f}")
    print(f"  R used in alpha computation:  {ic['R_used_in_alpha_computation']}")
    print(f"  Route 2 independent of R:     {ic['route_2_independent']}")
    print(f"\n  Historical caveat: {ic['historical_caveat'][:80]}...")

    # ── 4. Convention invariance ────────────────────────────────────────────
    print("\n4. Convention invariance")
    print("-" * 60)
    cc = convention_check()
    print(f"  KS 2011 units:   (a,c) = ({cc['convention_A_KS2011']['a']}, {cc['convention_A_KS2011']['c']})  -> a/c = {cc['convention_A_KS2011']['a_over_c']}  ok={cc['convention_A_KS2011']['equals_1_3']}")
    print(f"  Duff 1994 units: |b'|/b = {cc['convention_B_Duff1994']['ratio']}  ok={cc['convention_B_Duff1994']['equals_1_3']}")
    print(f"  Rescaled (N={cc['convention_C_rescaled']['scale_N']}): a/c = {cc['convention_C_rescaled']['a_over_c']}  ok={cc['convention_C_rescaled']['equals_1_3']}")
    print(f"  Invariant: {cc['invariant']}  — {cc['verdict']}")

    # ── 5. KS 2011 citation check ───────────────────────────────────────────
    print("\n5. KS 2011 path: which claim is actually supported?")
    print("-" * 60)
    kc = ks2011_path_check()
    print(f"  Claim (a) 'alpha = 1/d from dimensional reduction':  in_KS2011 = {kc['claim_a_v11_AppH']['in_KS2011']} -> {kc['claim_a_v11_AppH']['status']}")
    print(f"  Claim (b) 'a/c = 1/3 for real scalar':               in_KS2011 = {kc['claim_b_KS2011_Duff1994']['in_KS2011']} -> {kc['claim_b_KS2011_Duff1994']['status']}")
    print(f"\n  {kc['what_ALPHA_VAC_PROVENANCE_found'][:120]}...")

    # ── 6. Sensitivity ──────────────────────────────────────────────────────
    print("\n6. Sensitivity: Omega_Lambda vs alpha_vac")
    print("-" * 60)
    sa = sensitivity_analysis()
    print(f"  {'alpha_vac':>12}  {'R':>10}  {'Omega_L':>10}  {'Planck dev':>12}  {'Physical':>10}")
    for row in sa["rows"]:
        OL = row["Omega_Lambda"]
        dev = row["planck_deviation_pct"]
        OL_str  = f"{OL:.4f}" if isinstance(OL, float) else OL
        dev_str = f"{dev:+.2f}%" if isinstance(dev, float) else dev
        marker = "  <-- canonical" if abs(row["alpha_vac"] - 1.0/3.0) < 1e-9 else ""
        print(f"  {row['alpha_exact']:>12}  {row['R']:>10.6f}  {OL_str:>10}  {dev_str:>12}  {row['physical']!r:>10}{marker}")
    print(f"\n  {sa['sensitivity_verdict']}")

    # ── 7. Five-question summary ────────────────────────────────────────────
    print("\n7. Five book-readiness questions")
    print("-" * 60)
    fq = five_question_summary()
    for q, v in fq.items():
        print(f"  [{q}] {v['status']}")
        print(f"       {v['answer'][:100]}...")

    # ── Summary ─────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  alpha_vac = 1/3:       from Route 2 (KS 2011 / Duff 1994), NOT Route 1 (v11 App H)")
    print(f"  a/c = 1/3 for scalar:  EXACT, PUBLISHED, CONVENTION-INDEPENDENT")
    print(f"  Independent of R:      YES (Route 2 computes a/c before R)")
    print(f"  KS 2011 match:         YES for Claim (b); NO for Claim (a)")
    print(f"  Load-bearing step:     Identification 'conformal mode = real scalar' (needs chapter)")
    print(f"  Sensitivity:           High — only alpha near 1/3 gives physical Omega_Lambda")
    print(f"  Book action:           Replace 'alpha = 1/d' (Route 1) with 'a/c = 1/3 from Duff 1994'")
    print(f"                         + Write identification chapter for conformal mode = scalar")

    # ── Output ──────────────────────────────────────────────────────────────
    out_dir  = repo_root / "theory" / "hard_theory" / "gate3_dl_outputs"
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / "gate3_alpha_vac_provenance.json"

    # Make trace anomaly JSON-serializable (Fraction -> str)
    trace_anom_serial = {
        k: {kk: str(vv) if isinstance(vv, Fraction) else vv
            for kk, vv in v.items()}
        for k, v in TRACE_ANOMALY.items()
    }

    output = {
        "spec":                  SPEC_VERSION,
        "spec_date":             SPEC_DATE,
        "date":                  datetime.now().isoformat(),
        "trace_anomaly_table":   trace_anom_serial,
        "action_entry_point":    ACTION_ENTRY_POINT,
        "route_comparison":      route_comparison(),
        "independence_check":    independence_check(),
        "convention_check": {
            k: {kk: str(vv) if isinstance(vv, Fraction) else vv
                for kk, vv in v.items()}
            for k, v in convention_check().items()
            if isinstance(v, dict)
        } | {"invariant": True, "verdict": convention_check()["verdict"]},
        "ks2011_path_check":     ks2011_path_check(),
        "sensitivity_analysis":  sensitivity_analysis(),
        "five_questions":        five_question_summary(),
        "summary": {
            "alpha_vac":                  1.0/3.0,
            "alpha_vac_exact":            "1/3",
            "a_over_c_real_scalar":       "1/3",
            "route_for_book":             "Route 2 (KS 2011 / Duff 1994): a/c = 1/3 for real scalar",
            "route_to_drop":              "Route 1 (v11 App H 'alpha = 1/d'): assertion, not physics",
            "independent_of_R":           True,
            "convention_invariant":       True,
            "matches_KS2011_claim_b":     True,
            "load_bearing_identification": "conformal mode of gravity = real conformally-coupled scalar",
            "needs_chapter":              "Identification chapter: why conformal mode = scalar (not circular)",
            "sensitivity":               "HIGH — only alpha near 1/3 gives physical Omega_Lambda",
        },
    }

    with open(out_file, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\nOutput: {out_file}")
    print("=" * 80)
    print(f"End: {datetime.now().isoformat()}")
    print("=" * 80)


if __name__ == "__main__":
    main()
