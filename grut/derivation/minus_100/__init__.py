"""−100 on S⁴ resolution attempt.

The −100 integer in expression B of the 3-loop CTP anomaly calculation
on S⁴ is the one remaining open integer in R_anomaly's trace. This
package resolves the STRUCTURAL half of the question (the SM group-
theory identification −100 = −(ΣY²)²) in locked-in regression tests,
and narrows the remaining specialist task to a single numerical
conversion factor.

Three stages:

    Stage 1 — SM hypercharge-squared sum verification (CLOSED).
              `hypercharge_sum.py`: Σ Y² = 10, (ΣY²)² = 100 exact.

    Stage 2 — Flat-space 2-loop master integral (CLOSED).
              `master_integral_tji.py`: TJI finite-part rational 7/4
              reproduced symbolically, confirming the FeynCalc result.

    Stage 3 — Flat-to-S⁴ conversion factor (NARROWED).
              `s4_conversion.py`: target factor −400/7 isolated; candidate
              decompositions into known S⁴ invariants (Vol(S⁴) = 8π²/3,
              T_GH = H/(2π), Matsubara zero-mode measure) listed with
              explicit numerical comparisons. Final curved-space master
              integral evaluation remains the single open specialist task.

See `theory/derivation/MINUS_100_RESOLUTION_ATTEMPT.md` for the full
derivation narrative.
"""
