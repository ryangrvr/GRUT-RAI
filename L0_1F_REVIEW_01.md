# L0-1f (O-5) — ANALYTIC REVIEW 01 of the D-ORD-a theorem document

**Date:** 2026-09-29 · **Object:** `L0_1F_DORD_THEOREM_01.md`
revision 1 (`314f2c3`) · **Method:** two independent analytic
reviewers, one attempting to refute each proof and one reviewing scope
and honesty. The operator verified each finding before incorporating
it.

**Toy numerics disclosed.** These were on generic small matrices, not
record members, and were used only to test the document's general
claims:
- the series expansion checked to 1e-17;
- a Jordan block and a complex-pair Hankel, both indefinite;
- OU symmetric vs asymmetric C(τ), checked to 1e-16;
- two counterexamples, verified with `expm`.

## The two mathematical errors in revision 1 (fixed in revision 2)

1. **The D-2 memory-class row was false.** It read "no pole with
   nonzero residue in Re z > −c ⟺ |k| ≤ Ce^{−cτ}". Two counterexamples
   break it, both inside 𝒞₁:
   - **A double pole on the boundary line.** K = [[0.5, 0.5],
     [−0.5, 1.5]] is accretive, with a double eigenvalue at 1, and gives
     k = (1 + τ/2)e^{−τ}.
   - **A double pole with zero residue.** An accretive 3×3 K (listed in
     the reviewer's report) gives k = e^{−3τ} + τe^{−τ}, so
     G = 1/(z+3) + 1/(z+1)². The pole at −1 has residue 0, yet the
     bound fails at c = 2.

   **Fix:** state the condition on poles of the reduced G: Re z < −c,
   or Re z = −c and simple. The row is also relabeled as *not a
   registry battery*.
2. **"Strict Lyapunov function, equivalently non-recurrent" (§3) was
   false.** A homoclinic orbit is non-recurrent yet obstructed.
   **Fix:** D-4 is restated for α(γ) ∩ ω(γ) ≠ ∅. D-3 is sufficient and
   D-4 is necessary. Conley's chain-recurrence theorem is cited as the
   general boundary.

## The framing defects (scope/honesty review; all confirmed)

| # | Finding | Disposition |
|---|---|---|
| DORD-1 (high) | The vector field f is the generator; its magnitude is what the derived clock reads. The formulation removes a time *parameter* but presupposes the generator, and revision 1 called f "static data" without saying so. | §0 now states the generator presupposition first. Gradient rows are restored to (V, g, x₀). Deriving the generator is successor item S-5. |
| DORD-2 (high) | The "one-bit orientation convention" is not free: the sign of f fixes it, and D-1's one-sided transform carries it too. §2 and §4 applied different standards. | §2 and §4 are aligned. The order is derived. "Later" = along f, the generator's sign. D-5 decides *distinguishability* of the lag directions, and naming one of them forward is the same bit. **Put to the owner explicitly (§6).** |
| DORD-3 (high) | 𝒞₃ had no time-free presentation of its battery object. | D-1′ added: the correlation resolvent e₁ᵀ(K+z)⁻¹Σe₁, with Σ from the static Lyapunov equation, scoped to second order (complete for Gaussian). |
| DORD-4 (high) | Revision 1's "equivalently" was false, and §3 was written in result voice. | Fixed (see error 2). §3 retitled "a boundary … no result claimed". |
| DORD-5 (med-high) | Revision 1 re-framed O-7's frozen hypothesis inside O-5, a retroactive surface. | The re-reading is withdrawn and moved to successor item **S-4**. The frozen wording is unchanged. The stable-limit-cycle case is recorded as a scoped boundary finding against H-ORD's "exactly" clause, outside the record's classes. |
| DORD-6 (med-high) | "Every class on the record is safe" was over-broad. | The claim is restricted to the dissipative relaxational classes, with members enumerated. L0-1a's D-GAP pin = 0 member (semidefinite) and D-PASS members (indefinite) are excluded by name. **The Hurwitz / Lyapunov-equation row is added,** which covers O-2's non-accretive candidate. 𝒞₃'s sample-path obstruction is stated. |
| DORD-7 (med) | The O-6 handoff prejudged H-ORD. | Reworded: only the D-4 plus quasi-periodicity/Poincaré consequence is stated. H-ORD is left untested for O-6. |
| DORD-8 (med) | D-3 and D-5 could be read as certifying a property → ingredient edge. | An explicit disclaimer: these are theorems about substrate data, not certified property nodes, and accepting O-5 certifies no edge. |
| DORD-9 (med) | R-3 and grading overreach. | The memory row is relabeled. The registry's P_memory is stated to have no static reading. D-3 (not D-1) is named as what derives the window's τ. Static readings are restricted to 𝒞₁ and 𝒞₃. The R-3 qualification is repeated on the face. |
| Proof-level repairs | D-1 moment circularity (d is unknown in advance); Ho–Kalman citation; D-3 uniqueness needed C^{1,1} (replaced with the transferred-uniqueness argument); D-3's range [0, σ*) and clock divergence; notation (x₁(σ(τ)); F for the monotone function in D-4); D-5(i) extended to all statistics via Gaussian determinacy; the parity hypothesis (even variables) made explicit; the (a)/(b) rows reworded from "no finite characterization" (an unproven impossibility) to "none known in general; decidable in special cases; none claimed"; Poincaré's scope restored to the design's F-4 wording. | All incorporated. |

## Label consequence

The reviewers agree the core theorems are sound as corrected. The
proposed label now depends on one owner ruling, and nothing else
(`L0_1F_DORD_THEOREM_01.md` §6): **does an order derived from substrate
data, with its orientation carried by the sign of the presupposed
generator and labeled as such, satisfy the no-`t` rule?**
- **Yes:** DISCHARGED. This is the operator's recommendation.
- **No:** UNFORMULABLE-WITH-DOCUMENTED-REASON.
