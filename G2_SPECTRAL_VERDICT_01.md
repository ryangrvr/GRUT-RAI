# G-2 — SPECTRAL/FREQUENCY-DOMAIN GEOMETRY ATTACK: VERDICT

**Date:** 2026-09-25 · **Charter:** `G2_SPECTRAL_CHARTER_01.md` (frozen at
`c83e9d7` before the run) · **Authority:** GitHub Issue #2, owner comment
5827773903 · **Instrument:** `calc/g2_spectral.py` · **Artifact:**
`G2_SPECTRAL_RESULT.json` (sha `75957c4f2b20ef3b…`) · **Battery 35/35,
zero failures, zero halts, single run.** Every halt-grade analytic
identity held (resolvent degeneracy 2.2e-16, heat degeneracy 4.4e-16,
scramble 4.3e-25, full-space spin validation 0.0, congruence 2.6e-10);
matched control exactly 0. G-1's eight reds stand untouched — this was
a fresh attack, not a repair.

## VERDICT

> **GEOMETRY-PARTIAL-SPECTRAL** (decision rule 1) **+
> GEOMETRY-UNDERDETERMINED as a structural limit** (decision rule 2),
> with rule 3 honored: no promotion beyond PARTIAL. **The G-1 metric
> failure was the arrival-time instrument. The G-1 single-site
> degeneracy was not — it is a property of the interface itself.**

### The owner's central question, answered on both branches

**Instrument or fundamental?** Both, cleanly separated:

1. **The quantitative failures were instrumental.** Where G-1's
   time-of-flight gates failed, the frozen spectral functionals pass at
   machine precision: dimension by the shell estimator lands at
   **1.000 / 2.000 / 2.942 / 1.000 (quantum)** on the same 1D/2D/3D/XX
   substrates where arrival-time gave 0.71/1.51/1.67/0.49; all ten
   anchor-pair distances recover the substrate hop counts within
   **0.004** (G-1's held-out predictions erred by 37%); and on the very
   graded chain where G-1's L-CRV measured a speed ratio of 1.106
   against the predicted 1.5, the resistance form tracks the declared
   stiffness density **exactly** (ratio = 1/2.25 to 1e-9, held-out
   prediction to 2e-12).
2. **The degeneracies were not.** The G-1 grid-vs-Lanczos pair, retested
   with the strongest available frequency-domain single-site data —
   resolvent values across four frequencies and heat data across three
   scales — is identical to **2.2e-16**. Spectral data cannot break it,
   because the Lanczos chain matches the seed's complete spectral
   measure (standard mathematics, cited). **Single-site geometric
   underdetermination is a structural limit of the interface, not an
   artifact.** Likewise topology: below the invariant order equal to
   the circumference, C40 and C80 are exactly indistinguishable.

### What was recovered (multi-site access, held out, invariant)

- **Distances:** the heat-kernel hop metric (C1, defined before
  computation), validated against its derived identity on chains
  (errors ≤ 0.001), recovers all anchor distances to ±0.004; the
  integer additive triple d(A1,A4) = d(A1,A5) + d(A5,A4) holds
  **exactly** (36 = 15 + 21); trilateration of the held-out site
  predicts its unseen distances within 0.145/0.183 (gate 0.25, the
  frozen ℓ¹-in-ℓ² slack; MDS capture 0.775 reported).
- **Dimension:** shells at r = 3, 6 give 1.000 / 2.000 / 2.942 —
  the 2D value exact, the 3D value the exact combinatorial value of the
  ℓ¹-shell ratio (146/38). The quantum leg (a genuinely noncommutative
  spin system, verified against the full 2³ Hilbert space at 0.0)
  gives 1.000 with exact integer hop additivity.
- **Metric density:** effective resistance (C2, series-law identity
  derived and verified to 1e-9) recovers the inhomogeneity exactly with
  a genuine held-out prediction.
- **Invariance:** everything survives the 30-rotation substrate
  scramble (4.3e-25) and the 20-rotation congruence on the
  noncommutative model (2.6e-10). Nothing here is a coordinate
  artifact.

### The geometry ladder (the P-4 analogue, now exact)

C40 vs C80: closed-walk counts **equal as exact integers** through
order 38 (e.g. 35,345,263,800 = 35,345,263,800) and differ at order 40
— **by exactly 2, the two winding walks.** The first distinguishing
invariant order equals the shortest non-contractible cycle. In the
time domain: heat-trace difference 0.0 at t = 1 (exact difference
~ t⁴⁰/40!, below the float floor, established by the integer ladder),
4.7e-6 at t = 40. **Low-order spectral matching never certifies global
geometry; topology enters the interface at an invariant order equal to
its own size.** This is P-4's cumulant ladder in geometric form, and
the frequency-domain restatement of G-1's causal horizon.

### What this does to the candidate chain

> influence hierarchy → access → spectral structure → **geometry** →
> gravity: in the tested class, **geometry is not an additional input
> on top of spectral influence data at sufficient access — it is
> recoverable from it** (distances, dimension, metric density, all
> invariantly, all with held-out success), **up to exactly two
> structural limits: the access boundary (one-site collapse) and the
> data's invariant order (sub-circumference topology).** Both limits
> are the same shape as P-5/P-6's access results: what the interface
> determines is bounded by what the access makes available. And per
> the frozen NULL-REDUNDANT discipline: the reconstruction machinery
> (heat kernels, effective resistance, Lanczos, MDS) is standard
> mathematics — the physical content is *which invariants the declared
> access makes recoverable*, not a new law.

## DEFECT HISTORY

None. Single run, no post-hoc edits, no gate failures. (Two dead
placeholder code fragments were removed and the L-C heat computation
switched from dense exponentials to eigendecomposition during
development, before the first execution; no numerical result existed
prior to these edits.)

## FENCES AND SCOPE

No gravity equations, Einstein tensors, or cosmological assumptions
anywhere; no metric was defined into existence (both candidates carry
derived, verified identities); stationarity is a property of the
static testbeds (rider carried); ℏ located-not-generated; type-III
boundary map only; Λ_R, Matsubara, Π₀, U5, ω⁷/class-4 fenced; the
finite type-I results are not generalized. G-1's access/horizon
statement remains empirical and in-class.

## HARD STOP

Verdict recorded: **GEOMETRY-PARTIAL-SPECTRAL** with the recoverable
invariants named (hop distances, dimension, metric density — invariant
and held-out-validated) and the two structural limits promoted
(single-site collapse; sub-order topology). Per the owner's fence, the
gravity sector remains closed and opens **only by explicit ruling** —
the natural next fork being (a) whether (K, N)_grav can now be posed
as a hierarchy point over this recovered geometric substrate (the
ω⁷/class-4 gate is still open), or (b) a geometry-selection question
(which geometry, among the admissible, is realized — the geometric
sibling of S-1), or (c) further bounding of the structural limits.
The owner rules.
