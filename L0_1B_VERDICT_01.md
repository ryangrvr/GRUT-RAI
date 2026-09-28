# L0-1b — VERDICT (three lines, never composed)

**Date:** 2026-09-28 · **Charter:** `L0_1B_CHARTER_01.md`, frozen at
`55dafe6` **before** implementation and run · **Authority:**
`L0_1A_OWNER_RULING_01.md` (D-LOC authorized; Outcomes A and B named in
advance) · **Instrument:** `calc/l01b_locality.py` (pure stdlib; no
RNG; the committed C1-a machinery imported unchanged) · **Artifact:**
`L0_1B_RESULT.json` (sha `0ef0081924713ea5…`) · **Battery: 7/7 gated
checks, zero failures, zero halts, in the recorded run.**

## VERDICT LINE 1 — LOCALITY: NOT-LOAD-BEARING for P_memory

> **Finite-memory-grade decay survives every deletion of locality,
> including the full one.** Across the entire lattice — anchor, six
> weighted long-range members, and the uniform complete graph — k(40)
> stays within [6.7×10⁻⁹, 2.05×10⁻⁸], a factor of 3 of the anchor,
> every member under the 10⁻⁵ gate and every member EXPONENTIAL-GRADE
> under the L0-1a comparator. This survival is **analytic-backed by
> construction** (the held pin: k(40) ≤ e⁻¹²), so it certifies only
> what the charter said it could: *with gap and passivity held fixed,
> the response does not care how the couplings are wired.*

## VERDICT LINE 2 — LOCALITY: NOT-LOAD-BEARING for P_positivity

> **The positivity structure survives every deletion of locality.**
> λ_min(bath) ≥ 0.304 at every member (it *rises* with
> delocalization, to 0.383 at the complete graph) and the kernel is
> monotone decreasing on the grid everywhere (max step increase
> −1.2×10⁻⁹ — strictly negative). Analytic-backed as above.

## VERDICT LINE 3 — LOCALITY: NECESSITY-CERTIFIED for P_geometry (G-2 H-SR: survived)

> **Removing locality destroys recoverable spatial geometry.** Under
> the pre-committed resistance-metric battery: the anchor SURVIVES
> (Q = 23.000, exact series law R_ij = |i−j|, ordering monotone); the
> deleted member FAILS (Q = 1.000000 exactly — the complete graph puts
> every pair at resistance 1, no recoverable line structure). Both end
> gates are identity-grade, as the charter's honesty note declared.
> The one attackable non-identity prediction **H-SR survived the
> attack**: at α = 4, with *every* pair coupled, Q = 18.039 and the
> ordering is monotone — genuine nonlocality with summable weights
> still carries a line.

## THE SPLIT (Outcome B): CERTIFIED

All three lines landed as the frozen outcome rule requires. At the
recorded strength, within the declared scope:

> **Response does not require locality; recoverable spatial geometry
> does** — within the declared background mathematics, the tested
> weighted-network class w_ij = c_α·|i−j|^(−α) on N = 24 with the
> coupling norm held at 23, the window τ ∈ [1, 40], and the §2
> resistance criterion. In the owner's pre-named phrasing: *response
> does not require space; space requires a particular organization of
> response.*

**Outcome A (collapse) was not refuted here — it was undecidable
here,** by design: the held pin makes an M-line failure
identity-impossible, so this fork could never have produced Outcome A.
A fork that deletes locality *without* holding the pin would be needed
to test it (out of scope, noted per charter §5).

## The crossover map (ungated; the fork's exploratory payload)

| member | Q | ordering | status |
|---|---|---|---|
| anchor | 23.000 | monotone | SURVIVES |
| α = 4 | 18.039 | monotone | SURVIVES |
| α = 3 | 11.802 | monotone | DEGRADED |
| α = 2 | 5.126 | monotone | DEGRADED |
| α = 1.5 | 3.214 | monotone | DEGRADED |
| α = 1 | 2.104 | monotone | FAILS-adjacent (DEGRADED) |
| α = 0.5 | 1.438 | broken | FAILS |
| α = 0 | 1.000 | broken | FAILS |

Two honest observations, adjudicating nothing:

1. **The frozen folklore note was wrong on its face.** The pre-run
   note expected the geometry boundary near α ≈ 2; under this
   criterion the dynamic range is already down to Q ≈ 5 at α = 2, the
   line ordering breaks between α = 1 and α = 0.5, and full survival
   holds only at α = 4. On this battery, recoverable geometry is more
   fragile against long-range coupling than the 1D folklore suggested.
2. **α = 3 is a near-miss, criterion-relative:** Q = 11.802 against
   the frozen threshold 12 (= N/2). The threshold was frozen before
   the run and is not adjusted; whether α = 3 "really" survives is a
   question about the criterion at this N, not about this run —
   flagged for any future re-charter at larger N, never re-scored
   here.

## What this does and does not establish

- It does **not** say "reality's response is nonlocal" or "space is
  emergent in reality." Scope, on the face: real symmetric matrices,
  exact eigendecomposition, the tested weighted-network class on
  N = 24 with norm held, the declared window and criterion.
- It **does** deliver the sweep's third necessity certificate and its
  first two not-load-bearing certificates — and thereby the program's
  first *structural separation*: within this class, the axioms that
  carry the response (gap, passivity) and the axiom that carries
  geometry (locality) are **different axioms**. Level I shrinks on the
  response side; the geometry burden is now isolated and named.
- The M-line survivals are analytic-backed (the held pin), declared as
  such before the run — they are consistency certificates for the
  L0-1a identities under rewiring, not independent discoveries. The
  earned non-identity content of this fork is G-2 (H-SR) and the
  crossover map.
- No v4 channel moves (the deposit stands as filed); no red gate is
  touched; the public paper is untouched; GR2 and L0-1a unmodified.

**HARD STOP.** Verdicts recorded pending owner ruling — which also
decides whether **L0-1c (D-LIN, linearity)** is chartered next per the
frozen descent order, and whether the pin-free locality fork (the only
route to deciding Outcome A) enters the queue or waits.
