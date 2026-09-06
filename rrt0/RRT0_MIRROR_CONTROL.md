# RRT0_MIRROR_CONTROL.md — ORIENTATION-BLINDNESS / PIPELINE-INVARIANCE CONTROL

Status: CALIBRATION CONTROL — NOT a physics test, NOT a rescue of the sector firewall.
Scope: entirely inside the frozen RRT-0 finite closed linear-unitary model class.
The prior result `SECTOR_SELECTION_UNRESOLVED` (2/7 controls, null_p = 1.000) is
PRESERVED UNCHANGED and is not reinterpreted by anything below.
Label vocabulary: Section 22 of RRT0_CLAIM_BOUNDARIES.md. Forbidden-claims firewall applies.

## PRE-REGISTERED SECTION (written and saved BEFORE any mirrored run; append-only below)

### Provenance
Branch `rrt0-phase2`, HEAD `74e945f` (working tree: this file + driver + regression test are
the only additions; no frozen artifact touched; RRT0_FREEZE.json hashes unmodified).

### Exact mirror transformation M
M is entrywise complex conjugation (the antiunitary K) applied COVARIANTLY to every model
tensor, with the propagator conjugated accordingly:

    H      -> H*            (equivalently H^T; H Hermitian)
    U      -> U*            (note: U* = exp(+i dt H*) — the conjugated-model propagator
                             with the evolution orientation reversed; implemented as np.conj(U))
    rho0   -> rho0*         (registered bootstrap state, same seed stream)
    rho_h  -> rho_h*        (held-out states, same seed stream)
    sigma_a-> sigma_a*      (intervention projectors)
    B_b    -> B_b*          (readout basis)

Nothing else changes: identical seeds, seed-stream call order, lam/tau grids, clustering
procedure and initializations, split construction, null construction, thresholds, statistics.

### Why M is the prescribed mirror (equivalence + orientation reversal), checked
(i) FROZEN-CLASS EQUIVALENCE: E_alpha[rho] = (1-lam)rho + lam sigma has real lam, so
E_alpha(rho*) = (E_alpha(rho))*. Every registered statistic is built from entries
    r_ab = | Tr[ B_b · U^tau (E_a(rho0) - rho0) U^{-tau} ] |
and conj(Tr[X1 X2 ...]) = Tr[X1* X2* ...] gives r_ab(M-model) = |conj(trace)| = r_ab exactly.
Hence the discovery matrices, and everything downstream of them, are invariants of M.
(ii) ORIENTATION REVERSAL: U -> U* maps exp(-i dt H) to exp(+i dt H*): the representation of
the evolution orientation is reversed (K is the time-reversal antiunitary for this class).
M is therefore the finite-type-I analogue of the RAI campaign's conjugation/parity gauge
maps: an antiunitary isomorphism of the model that no internal registered statistic may
distinguish. This control tests the PIPELINE for that blindness; it says nothing about
physical orientation beyond the frozen class.

### Compared quantities and declared tolerances
Per registered condition (the frozen 6-condition grid):
  Q1 discovery matrix X (15x15):        max-abs entry difference  <= 1e-12
  Q2 all seven control scalars:         abs difference            <= 1e-9
     (null_p, split_consistency, basis_agreement, k_agreement, lam_agreement,
      seed_agreement, held_out_accuracy)
  Q3 reference partition:  same_invariant = pair_agreement(orig, mirror) == 1.0 required;
     labeling may differ (same_labeling = best-permutation agreement, reported not gated).
Aggregate verdict fields (status, n_pass, failed_controls): must be identical.

### Acceptance criterion (frozen before inspection)
  PASS: every Q1/Q2 within tolerance and every Q3 same_invariant == 1.0, with only
        relabeling/covariance differences; aggregate fields identical.
  FAIL — PIPELINE ASYMMETRY: any invariant quantity beyond tolerance.
  UNRESOLVED: numerical instability or an incompletely specified transformation prevents
        adjudication.
The criterion will not be changed after seeing the result.

### Failure localization ladder (if FAIL)
Stage 1: X matrices (model/statistic level) -> Stage 2: clustering on identical X
(initialization/tie-breaking) -> Stage 3: control constructions. Earliest differing stage is
reported; if not localizable, stop before any interpretation.

### Expected outcome (registered as expectation, not hard-coded)
Exact invariance is a THEOREM of the class (section above), so PASS with differences at or
near 0.0 is expected. Any FAIL therefore indicates a pipeline defect (most likely) or an
implementation deviation from M — not physics.

---
## RESULTS (appended after execution; pre-registered text above is never edited)

**Executed:** 2026-09-06 · driver `rrt0/scripts/run_mirror_control.py` ·
interpreter `rrt0/.venv312/bin/python` (numpy 2.5.2) · machine-readable
`rrt0/reports/MIRROR_CONTROL.json` (sha256 `029ad05d7e78a934a85c8447…`).
Command: `rrt0/.venv312/bin/python rrt0/scripts/run_mirror_control.py`.
Implementation note: M applied by in-process rebinding of the pipeline module's imported
names for the mirrored pass only; no pipeline or frozen file edited; original pass ran first
on the untouched module state.

## VERDICT: **PASS** (per the pre-registered criterion; criterion unchanged after inspection)

| quantity | tolerance | worst case over all 6 conditions |
|---|---|---|
| Q1 discovery-matrix max-abs difference | 1e-12 | **0.0 (exact)** |
| Q2 all seven control scalars, abs diff | 1e-9 | **0.0 (exact)** |
| Q3 partition same_invariant (pair agreement) | == 1.0 | **1.0** (same_labeling also 1.0) |
| aggregate fields (status, n_pass, failed_controls) | identical | **identical** |

Both passes return `SECTOR_SELECTION_UNRESOLVED`, 2/7 — the original pass thereby also
REPRODUCES the committed `SECTOR_SELECTION_FIREWALL.json` outcome (incidental regression
confirmation; that result remains preserved and unreinterpreted).

The exact-zero differences confirm the pre-registered theorem at bit level: IEEE complex
conjugation is exact and every registered statistic is conjugation-invariant entrywise, so
the pipeline is bit-identically blind to the mirror. Regression coverage added:
`rrt0/tests/test_mirror_control.py` (exact invariance + genuine orientation reversal of the
propagator representation), passing.

## INTERPRETATION (limits explicit)
This is evidence of **mirror/orientation invariance of the tested pipeline within the frozen
model class**, i.e. a calibration PASS: the sector machinery introduces no orientation
asymmetry of its own, matching the class-level theorem. It is NOT evidence about physical
orientation, time's arrow, causality, emergence, or anything beyond the frozen
(finite, closed, linear-unitary, externally-intervened) class; the reducibility ceiling
`IRREDUCIBLE_EMERGENT_INFLUENCE = OUT_OF_SCOPE` stands unconditionally; and the failed
sector-firewall controls (incl. null_p = 1.000) are untouched by this PASS — the pipeline is
orientation-clean AND its selection statistic remains unresolved. Those are different facts.

## LIMITATIONS
Single frozen seed grid (the registered 6 conditions); the exactness of the invariance means
this control cannot detect asymmetries that would only appear under non-covariant mirrors
(none is prescribed); PASS licenses proceeding to the CPR-alignment design question, nothing
more. Stop-point honored: no CPR run, no RRT-1 design, no battery, no commit.
