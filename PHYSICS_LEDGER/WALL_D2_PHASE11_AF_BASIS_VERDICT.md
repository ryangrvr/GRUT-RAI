# PHASE-11 ACTION-FUNCTIONAL BASIS RECONSTRUCTION -- VERDICT

Instrument: `wall_d2_phase11_af_basis.py` (owner-authorized 2026-08-27; standing state 5fd77c0).
Verdict: **GREEN** (fail count 0).

## What was built

The toy-validated split-frequency functional-Hessian construction, generalised to the
four frozen operators {sqrt(-g), sqrt(-g)R, sqrt(-g)R^2, sqrt(-g)R_mnR^mn}: the machinery's
sector-graded cascade is mirrored with SPLIT u-frequencies (wE for the E leg, wP for the P
leg), so the eps1*eps2 density resolves as D(u; wE, wP) = Sum_pq B_pq(u) (-i wE)^p (+i wP)^q -- the per-leg derivative
counts that the shared-frequency construction conflates. The master formula then produces the
IBP-invariant action-functional kernels; the old coincident-density kernel is the (l,r)=(0,0)
term (checked identity), and the (l,r)!=(0,0) terms are the explicit distributional
corrections  -C(u_c) dd''(Delta) + (1/4)C''(u_c) dd(Delta)  it could not see. Independence
condition wired: old kernels / H^2 residual / span test are used ONLY as validation targets
(G2, G6); no correction coefficient is guessed, fitted, or solved for.

## Gates (all hard)

- **C**: 3 checks, 0 failed
- **E**: 1 checks, 0 failed
- **G0**: 5 checks, 0 failed
- **G1**: 16 checks, 0 failed
- **G2**: 50 checks, 0 failed
- **G3**: 4 checks, 0 failed
- **G4**: 1 checks, 0 failed
- **G5**: 14 checks, 0 failed
- **G6**: 7 checks, 0 failed
- **M**: 2 checks, 0 failed

## Findings (computed)

- H^0 kernels are UNCHANGED (gated): corrected == coincident-density.
- H^1 corrections OCCUR for: EH -- genuine action-functional Hessian corrections. The previous 'corrections exactly O(H^2)' theorem is RETIRED as toy-only (its proof used the toy's single even structure); the replacement gate derives the exact Hessian of S=Int B(u)[hA'hB+hA hB'] three independent ways (direct EL Hessian, raw-kernel centred slots, master kernel): K~ = -B'(u_c), an O(H^1) correction from u-dependent O(H) coefficients that the old construction is blind to; on the real tables the H^1 correction is attributed exclusively to such structures.
- Nonzero H^2 corrections for: EH, R2, Rmn2.
- The old basis is the r=0 term of this construction (G6 control-'C' identity).

## How to reclassify (span test UNCHANGED)

    python3 wall_d2_span_test.py               # old basis (baseline; must
                                             #  reproduce the 96/300 reading)
    AFB_LOAD=1 python3 wall_d2_span_test.py    # corrected AF basis

The machinery's Phase-11 BASIS section carries a DEFAULT-OFF cache hook (AFB_LOAD=1 plus
.p11_af_basis_cache.txt); the loop side, .p10_assembly_cache.txt, the identification
section and wall_d2_span_test.py are untouched, and the default path is unchanged.

## Fence

W-0: computed and reported only. The reclassification concerns LOCAL UV counterterm
structure only; it determines nothing about Q1 placement, Im chi, convergence class, or
relaxational/resonant character. No register edits; nothing banked.
