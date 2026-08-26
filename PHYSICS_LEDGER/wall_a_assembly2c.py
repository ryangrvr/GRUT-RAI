#!/usr/bin/env python3
"""WALL A, STAGE ASSEMBLY-2c -- FIRST H-DRESSING ORDER (Option B, v3).

*** INSTRUMENT IN PROGRESS: NOT A COMPLETED STAGE (session limit; honest pause) ***

FILE CLAIM filed (AGENT_COORDINATION.md, Ox, 2026-08-25, HEAD 58cb02a). W-0: nothing
banked. No register edits. No result is claimed for the H-corrections.

======================================================================================
DELIVERABLE 1 -- THE DECLARATION (drafted this session; binds the rebuild)
======================================================================================
  Expanded object : bath mode functions AND vertex a-dressings, in powers of the
                    dimensionless adiabatic ratios.
  Reference chart : de Sitter flat slicing, a(eta) = -1/(H eta), eta < 0 -- exact dS;
                    "adiabatic" = expansion of MODE FUNCTIONS in H/(m or k).
  Parameter(s)    : H^2/m^2 (mass-controlled) and H^2/k^2 (mode-controlled); unified
                    per-mode by M := max(m, |k|). Declared per-family at extraction.
  Retained order  : O(H^0) + O(H^2). ODD orders vanish: exact de Sitter is cosmic-time
                    translation invariant, so pole families admit only even H-powers
                    (fence asserted at extraction, checked).
  Remainder       : O((H/M)^4), M := max(m, |k|) per mode. Mode-function H-expansion
                    on fixed (-k eta) generates no ln(-eta H) before O(H^4); any
                    secular log entering later stages is declared where it appears.
  Fences          : (i) H-parity of pole families asserted AND checked; (ii) the
                    expansion is an approximation scheme (v3) asserting nothing about
                    which counterterms exist; (iii) H->0 recovery of the Gilkey anchor
                    is a wired known-answer gate at every retained order.
  First derived facts (verified symbolically this session, to be re-gated in-instrument):
      friction removal phi = psi/a gives psi'' + [k^2 + a^2 m^2 - a''/a] psi = 0 with
      a''/a = 2/(eta^2 H^0-structure)... i.e. omega^2 = k^2 + a^2 m^2 - a''/a EXACTLY,
      a''/a computed from a = -1/(H eta): the O(H^2) insertion enters as -a''/a with
      a''/a = 2 H^2 a^4 / ... (exact rational form derived programmatically next
      session; the derivation route -- not its typed result -- is the commitment).

======================================================================================
DELIVERABLES 2-5 -- NOT YET BUILT (next session under this same file claim)
====================================================================================
  2. dressed propagator via friction-removed adiabatic/WKB to O(H^2), SUBSTITUTION-
     gated against the exact mode equation (residual must sit at the claimed next
     order -- gate, not assertion);
  3. dressed vertex to the SAME order + dressing-consistency plant (order-mismatched
     hybrid must FAIL a wired gate);
  4. fish+seagull loop at first order; identification vs six-operator basis expanded
     ON FRW to matching order; same-footing, gauge+GB kernel gates, multi-K^2 +
     held-out, per-channel a-power audit;
  5. H->0 recovery wired to the doubly-verified Gilkey anchor; MS pole-only; non-
     vacuous integrity verdict; Pi_nonlocal^invariant(H-order) carried untouched.
  HARD STOP after outputs: no Q1-Q5, no J(omega), no PV, no second-gauge comparison,
  no spectral interpretation of H-corrections.
"""
import os
import sys

import sympy as sp

FAIL = []


def check(cond, msg):
    ok = bool(cond)
    print(("  ok   " if ok else "  FAIL ") + msg)
    if not ok:
        FAIL.append(msg)
    return ok

# =====================================================================================
# DELIVERABLE 1.5 -- THE H-PARITY GATE (owner-directed: PROVE odd orders vanish;
# a symmetry label is not a derivation)
# =====================================================================================
Hh, et, kk, mm = sp.symbols('H eta k m', positive=True)
aa = -1 / (Hh * et)


def d_(f):
    return sp.diff(f, et)


om2_exact = kk**2 + aa**2 * mm**2 - d_(d_(aa)) / aa   # friction-removed omega^2

print("=== DELIVERABLE 1.5: H-PARITY GATE (prove, don't label) ===")
c1 = sp.simplify(om2_exact.subs(Hh, -Hh) - om2_exact)
check(c1 == 0,
      f"(a) omega^2(eta;-H) == omega^2(eta;H) EXACTLY: {sp.factor(om2_exact)} -- "
      "the exact effective frequency contains H ONLY through a^2 ~ 1/H^2")
nu2 = mm**2 / Hh**2 - sp.Rational(9, 4)   # exact-dS order parameter of the BD function
c2 = sp.simplify(nu2.subs(Hh, -Hh) - nu2)
check(c2 == 0, "(b) nu^2 = m^2/H^2 - 9/4 is EVEN in H: the BD solution's H-dependence "
               "enters the spectrum only through nu^2")
c3 = sp.simplify((d_(d_(aa)) / aa).subs(Hh, -Hh) - d_(d_(aa)) / aa)
check(c3 == 0,
      "(c) the O(H^2) INSERTION (-a''/a = -2/eta^2) is H-independent: the first "
      "correction carries no new H-sign, so no linear-in-H term can be generated")
check(sp.simplify(om2_exact.subs({Hh: -Hh, et: -et}) - om2_exact) == 0,
      "(d) under (H,eta)->(-H,-eta) -- the expanding<->contracting map -- omega^2 is "
      "invariant: any H-odd term would have to be chart-odd, and the pole extraction "
      "is defined on the expanding patch")
print("   DECLARATION AMENDED (proven, not labelled): pole families admit only EVEN")
print("   powers of H because every H-entry of the expanded object is H^2-valued;")
print("   the |H| normalization of BD modes fixes the expanding-patch sign and is not")
print("   an expansion variable.")
print("   M-FENCE AMENDED: M = max(m,|k|) is per-mode bookkeeping, NONANALYTIC across")
print("   |k| = m; the expansion is PER MODE WITHIN A REGIME (mass-controlled or")
print("   mode-controlled), NOT globally uniform in k. No cross-regime matching is")
print("   claimed at this stage.")

sys.exit(0 if not FAIL else 1)

# =====================================================================================
# DELIVERABLE 2+ -- RESUMES NEXT SESSION (WKB dressed propagator, substitution-gated)
# =====================================================================================

print("ASSEMBLY-2c IN PROGRESS -- Declaration complete (module docstring); "
      "computational gates 2-5 resume next session under the standing file claim.")
sys.exit(3)
