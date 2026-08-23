# CLASS_C_BENCHMARK_MATRIX — emitted, never hand-typed

*Generated 2026-08-22 12:29 by `provenance/class_c_benchmark_matrix.py` (Phases 5-6). Verdict: **ALL APPLICABLE CELLS PASS**.*

*Provenance: rows marked SAME-CODE RERUN execute existing implementations**-- regression checks, NOT independent confirmations. The row marked**INDEPENDENT-CODE is computed by a fresh implementation written against**the closed form only.*

| limit | component | benchmark | measured | tolerance | status | provenance |
|---|---|---|---|---|---|---|
| exactly-solvable special case | worldline_reduction (fold identity) | closed form vs quadrature, max over w grid | max rel.err 7.8e-12 | — | PASS (SAME-CODE RERUN) |
| H->0 / flat-vacuum limit (pipeline) | tt_worldline_spectrum (half-line transform) | numeric vs exact (w/2pi)e^{-eps w}, worst over w grid | worst rel.err 0.0e+00 | — | PASS (SAME-CODE RERUN) |
| exactly-solvable special case (INDEPENDENT CODE) | fold identity, fresh Simpson implementation | w=1.7, Lam=20.0 | rel.err 0.0e+00 | — | PASS (INDEPENDENT-CODE) |
| fail-closed contract | class_c_manifest_gate | require() refuses UNDECIDED sections | 3 refusals observed | — | PASS (SAME-CODE RERUN) |
| fail-closed contract | class_c_solver | refuses while prerequisites undecided (--selftest) | exit 0, REFUSED=True | — | PASS (SAME-CODE RERUN) |
| parameter-leakage closure | class_c_dependency_closure | 8 bypass mutants caught + clean source passes + live surface closed | exit 0, SURVIVED=0 | — | PASS (SAME-CODE RERUN) |
| contamination | class_c_contamination_audit | active-surface verdict | class_c_contamination_audit: CLEAN | — | PASS (SAME-CODE RERUN) |

## Not-yet-applicable limits (declared, so absence is visible)

- **H->0 limit of assembled G_R^TT**: NOT YET APPLICABLE -- class C uncomputed.
- **KMS/thermal limit of assembled response**: NOT YET APPLICABLE.
- **gauge-equivalent formulation agreement**: NOT YET APPLICABLE -- gauge UNDECIDED-DISPATCH.
- **weak-coupling limit of interacting Sigma**: NOT YET APPLICABLE.

## What this matrix does and does not establish

Green cells establish that the machinery reproduces its known limits.
They do NOT establish any class-C physics result; walls A-C stand.
