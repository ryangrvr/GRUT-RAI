# GR2-d — VERDICT

**Date:** 2026-09-27 · **Charter:** `GR2D_CONE_CHARTER_01.md`, frozen at
`ff8db42`, Amendment 01 (pre-run, disclosed) at `18624a6` · **Authority:**
`GR2C_OWNER_RULING_01.md` (GR2-d authorization), under
`GR2_CAMPAIGN_DIRECTIVE_01.md` Layer 4 / seam S2 · **Instrument:**
`calc/gr2d_cone.py` (pure stdlib; no RNG) · **Artifact:**
`GR2D_CONE_RESULT.json` (sha `c1718e6c1f7eddbf…`) · **Battery: 22/25
gated checks; 3 failures; zero halts, in the recorded run.**

## THE VERDICT — D-PARTIAL

> **The pre-registered demonstration did not come in at frozen
> strength. Gate Q-2 — the quantum two-cone demonstration — missed its
> threshold: the arrival gap between the record's two sector parameter
> sets at r = 5 is 0.15, below the required 0.19 (10% of the larger
> arrival). V-2 (the owner's boxed gate) and V-3 (the trichotomy) fail
> by frozen conjunction, because both were chartered to require the
> classical AND the quantum demonstrations jointly. Under the frozen
> outcome rule this is D-PARTIAL — not D-CONE-NOT-DERIVED, and not
> D-CONE-SELECTED.**

The failure is disclosed, not repaired: no threshold is reinterpreted
after the run, no leg is rerun, and the miss is recorded exactly as the
instrument measured it.

## What failed, precisely

- **Q-2.** Measured quantum fronts (7-site open chains, commutator
  arrival at relative threshold 0.1): t\*_A = (0.05, 0.45, 0.90, 1.40,
  1.90); t\*_B = (0.05, 0.40, 0.85, 1.30, 1.75). Sector B — (J, h_x,
  h_z) = (1.3, 0.7, 0.5) — is *faster*, and the gap at r = 5 is 0.15 ≈
  8%, under the frozen 10%. The pre-freeze expectation (a
  transverse-Ising bound heuristic, v ≈ 2·min(J, h), predicting a ~25%
  gap with B slower) was wrong for these mixed-field chains in both
  size and direction. The heuristic error is the disclosed cause of the
  frozen threshold's miss; by house discipline it is a failed gate, not
  a reinterpretable one.
- **V-2, V-3.** Both pass their *classical* components and fail only
  because their frozen conjunctions include Q-2.

## What passed, at recorded strength (22 of 25)

1. **All controls and identities (halt-grade), 8/8:** the C1-a seam
   kernels replicate the owner-verified reproduction-note values to
   every digit; the L-X slope replicates 8.005419679013105; the
   classical procedure replicates its disclosed calibration
   (v_A = 1.0256410256; momentum identity 3.0e-14); the quantum
   equal-time commutators vanish (3.8e-14) and unitarity holds
   (8.1e-14).
2. **N — the classical two-cone demonstration PASSED:** v_B/v_A =
   1.2968 (analytic √1.69 = 1.3), both sectors earned-admissible
   (kernels ≥ 0, identical topology). Two admissible sectors, two
   cones — at recorded strength in the classical leg.
3. **X — exchange composes, it does not select:** the hybrid
   long-wavelength cone equals the *average* √((K_A+K_B)/2) of the
   supplied stiffnesses to 7 digits for both pairs; the branches retain
   the two sector characters at q\* = 0.6 (gaps 0.2361, 0.5663, per
   Amendment 01); a common cone appears exactly when the supplied
   inputs are equal (compatibility row, 1.0000000); and cross-sector
   propagation exists (strain leakage 2.9e-02) while no universal cone
   is created — the ruling's distinction, mechanical.
4. **K — the earned frequency battery is EXACTLY blind to the cone,
   for every representation:** the λ-relabeling leaves every exponent
   class bit-identical (deviation 0.0) and positivity intact while the
   front speed doubles — density, current-type, and stress vertices
   alike (no reliance on spin-2, per GR2-b).
5. **M — memory is not support:** the memory battery passes
   identically for slow and fast sectors; each sector separately shows
   a sharp support boundary (2.3e-14, 8.8e-14) whose slope is
   sector-dependent.
6. **V-1 — the survivor count PASSED:** 0 of the 7 different-cone
   systems is eliminated by any earned admissibility test.
7. **Q-1/Q-3/Q-4 and the Z-probe diagnostic:** the quantum fronts
   exist, move outward, share an identical interaction graph and
   earned positivity; the Z-probe arrivals (2.25 vs 2.20) confirm the
   front is a property of the sector, not the probe.

## What this outcome does and does not establish

- It does **not** establish that a universal causal cone is derived.
  Nothing in the run produced an earned discriminator selecting a
  cone; V-1's survivor count stands at 0 eliminated, and the classical,
  exchange, relabeling, and memory legs all came in on the
  not-derived side.
- It does **not** establish D-CONE-NOT-DERIVED, because the frozen
  bar for that verdict — the quantum demonstration at ≥ 10% — was not
  met. The measured 8% gap is nonzero and directionally informative,
  but the charter gets exactly the strength it pre-registered, no more.
- The near-coincidence itself is a finding worth recording: the two
  MFIM parameter sets the record happens to use have Lieb–Robinson
  fronts within ~8% of each other — a fact about those two supplied
  parameter choices, not a universality mechanism; the classical leg
  shows the cone moves freely with the supplied stiffness.

## Provenance notes (disclosed)

- **Charter Amendment 01 (pre-run, `18624a6`):** the original X-2
  compared global branch maxima, which nearly coincide for (1, 1.69) —
  a near-coincidence of two different quantities discovered in a
  pre-run satisfiability check; repaired to the interior-q comparison,
  fully disclosed including the lost blindness for that gate.
- **This run is run 1 and is the recorded run.** No halts fired;
  `defect_history` is empty; the Q-2 miss is a gate failure under the
  frozen rule, not an instrument defect.

## Consequence and hard stop

Under the frozen outcome rule: **no status moves in any direction.**
The causal cone is **not** upgraded, and its irreducibility
demonstration is **not** certified at campaign strength — the
demonstration half stands complete in the classical/exchange/
relabeling/memory legs and incomplete in the quantum leg. M-3, U-1,
TT-1 and all GR2 recorded statuses stand unchanged. The public paper is
not touched.

The natural follow-up — **the owner's to authorize, not this fork's to
take** — is a re-chartered quantum leg (a GR2-d2) with sector
parameters chosen for genuinely distinct Lieb–Robinson speeds and a
threshold set by disclosed calibration of the quantum procedure, as the
classical leg's was; the present fork's frozen heuristic threshold is
the disclosed defect to correct there.

**HARD STOP.** Verdict recorded pending owner ruling.
