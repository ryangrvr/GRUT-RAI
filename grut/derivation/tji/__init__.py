"""GRUT TJI sector — master-integral pipeline for the 3-propagator 2-loop
sunset integral TJI[D, k², {{1,0},{1,0},{1,0}}].

Phase-0 (this module): flat-space Laurent expansion in pure Python/SymPy,
producing the exact rational finite coefficient (scheme-dependent). The
V7 §26.2.3 FeynCalc run reported 7/4 in a specific MS-bar convention;
SymPy's raw gamma-function expansion produces a different exact rational
in the pre-MS-bar scheme. Scheme reconciliation is a Phase-0.5 item.

Phase-1 (deferred): Euclidean S⁴ evaluation with Allen-Jacobson propagators
and Hartle-Hawking thermal state. The Phase-0 infrastructure is the
starting point. Interface: `allen_jacobson.s4_propagator()` (stub only).

See `theory/derivation/TJI_PHASE_1_CALCULATION_PLAN.md` for the Phase-1 spec.
"""
