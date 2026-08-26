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

print("ASSEMBLY-2c IN PROGRESS -- Declaration complete (module docstring); "
      "computational gates 2-5 resume next session under the standing file claim.")
sys.exit(3)
