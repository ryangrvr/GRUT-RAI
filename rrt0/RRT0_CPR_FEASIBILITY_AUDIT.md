# RRT0_CPR_FEASIBILITY_AUDIT.md — DOES AN INDEPENDENT REFERENCE STRUCTURE EXIST?

Status: FEASIBILITY AUDIT ONLY — no clustering run, no alignment run, no firewall rerun,
no model modification, no RRT-1 design. Uncommitted pending explicit authorization.
Claim boundaries and Section-22 vocabulary of `RRT0_CLAIM_BOUNDARIES.md` apply.
Provenance: branch `rrt0-phase2`, HEAD `291ea4c`; frozen seeds = primary 20260213 +
robustness {1,2,3,4,5} (`RRT0_INPUT_LEDGER.json`); firewall conditions used seed 1.

## PRE-REGISTERED SECTION (written and saved before the existence computation)

### Q1 — What exact CPR-style object would be reconstructed
CPR (Cotler–Penington–Ranard, *Locality from the Spectrum*, CMP 368 (2019) 1267,
arXiv:1702.06142) reconstructs, from the SPECTRUM alone, the tensor-product structure (TPS)
in which a Hamiltonian is local — proving (existence half) that a k-local TPS exists only for
a measure-zero set of Hamiltonians, and (uniqueness half) that when one exists it is
generically unique.

**At d = 4 the question degenerates into an exactly solvable form, and this is the audit's
central finding.** C⁴ admits exactly one nontrivial factorization type, C² ⊗ C². Two regimes:
- **k ≤ 2 locality WITH interaction terms: VACUOUS.** Every two-qubit Hamiltonian is
  "2-local" in every TPS (the whole system is two sites). A reference defined this way
  exists trivially and uniquely fails maximally — every TPS qualifies — so it cannot serve
  as a clustering referent. Ruled out as ill-posed-for-purpose.
- **k = 1 locality (non-interacting TPS): the ONLY non-vacuous CPR-style reference at
  d = 4.** H ≅ A⊗1 + 1⊗B for single-qubit A, B. This is the object whose existence is at
  stake, and it is EXACTLY decidable:

> **Existence criterion (derived, exact at d = 4).** A non-interacting TPS exists iff the
> sorted spectrum λ₁ ≤ λ₂ ≤ λ₃ ≤ λ₄ satisfies the sum-set condition
> **δ := (λ₁ + λ₄) − (λ₂ + λ₃) = 0.**
> (Necessity: spec(A⊗1 + 1⊗B) = {aᵢ + bⱼ}; the extremes pair as a_min+b_min and
> a_max+b_max, the middle two are the cross terms, and the two pair-sums coincide.
> Sufficiency: given δ = 0, set a-splitting and b-splitting from the sorted gaps and
> conjugate. Uniqueness: generic when the a-gap ≠ b-gap.)
> δ, normalized by the spread (λ₄ − λ₁), is the complete obstruction invariant.

If a reference exists, the operator-space referent it induces is the partition of the
15-dim Gell-Mann space into **{A-local (3), B-local (3), interaction (9)}** — note this is
a **3-class partition, not the registered K = 4**: a design fact any future alignment
experiment must confront, recorded here, not repaired.

### Q2 — Defined for the actual ensemble and dynamics?
Yes, trivially: the CPR reference is a function of the SPECTRUM of H only. The state
ensemble (maximally mixed + Haar pure) and the intervention machinery never enter its
definition — they would enter only a later alignment experiment. No obstruction here.

### Q3 — Can the structure legitimately be absent?
Yes, and generically it is: δ = 0 is one linear condition on four eigenvalues — measure zero
under GUE. **Registered expectation (not hard-coded): the frozen draws fail it with
δ/(λ₄−λ₁) = O(1)**, i.e. `NO_REFERENCE_LOCAL_STRUCTURE_FOR_FROZEN_MODEL_FAMILY`. Absence is
a legitimate, informative outcome: it would establish that the failed sector-selection
result cannot be rescued by handing the clusterer a referent the frozen family never had.

### Q4 — Independent of the sector pipeline?
Completely. The test consumes eig(H) only; the pipeline consumes response rows of
intervened states. No shared statistic, no shared choice, no circularity.

### Q5 — Mathematical assumptions required
(i) finite dimension, exact diagonalization (float64, d = 4 — exact to roundoff);
(ii) the 2×2 factorization is the only nontrivial TPS type at d = 4;
(iii) the exact/approximate distinction: the criterion above is EXACT locality, which is
what carries CPR's uniqueness protection. An APPROXIMATE reference (minimizing the
interaction norm over the TPS orbit) is computable at d = 4 but is **not covered by the CPR
theorems**, would require its own preregistration with matched-random nulls, and is
explicitly **out of scope** here — flagged so it cannot slip in later as if theorem-backed;
(iv) a numerical tolerance for δ (below), non-delicate because the expected defect is O(1).

### Q6 — Pre-registered outcome classification (frozen before computation)
Per frozen seed, with δ_rel := |δ|/(λ₄ − λ₁):
  `REFERENCE_EXISTS`        iff δ_rel ≤ 1e-10
  `NO_REFERENCE_LOCAL_STRUCTURE_FOR_FROZEN_MODEL_FAMILY` iff δ_rel > 1e-6
  `UNRESOLVED`              iff 1e-10 < δ_rel ≤ 1e-6 (numerically ambiguous band)
Family verdict = the seed-wise outcomes reported individually; no aggregation that could
hide a mixed result. Criterion will not change after inspection.

### Q7 — Minimum computation to establish existence/nonexistence
One eigenvalue decomposition per frozen seed plus the δ arithmetic — microseconds. It is
executed below AS the feasibility determination (it is not the alignment experiment, which
remains unrun). Guards honored: the GUE family is not tuned; the failed clustering result is
not consulted; absence of a reference is not read as evidence against relational physics in
general — it bounds only what the frozen (d = 4, GUE) family can support.

---
## RESULTS (appended after execution; pre-registered text above unedited)

**Executed:** 2026-09-06 · one `eigvalsh` per frozen seed · machine-readable
`rrt0/reports/CPR_FEASIBILITY.json` · pre-registration sha256 at save time
`942bee3961c2577c4c310965…` · criterion unchanged after inspection.

## VERDICT: **`NO_REFERENCE_LOCAL_STRUCTURE_FOR_FROZEN_MODEL_FAMILY`** — unanimous, 6/6 seeds

| seed | δ = (λ₁+λ₄)−(λ₂+λ₃) | δ_rel | outcome |
|---|---|---|---|
| 20260213 (primary) | +0.601633 | 0.144773 | NO_REFERENCE |
| 1 (firewall seed) | +0.042418 | 0.012593 | NO_REFERENCE |
| 2 | −0.923907 | 0.260907 | NO_REFERENCE |
| 3 | +0.635429 | 0.191258 | NO_REFERENCE |
| 4 | +0.332351 | 0.088722 | NO_REFERENCE |
| 5 | −0.005929 | 0.002565 | NO_REFERENCE |

Every δ_rel sits far above the 10⁻⁶ absence threshold (the closest, seed 5 at 2.6×10⁻³, is
still ~2,500× outside the UNRESOLVED band). The registered expectation — measure-zero
condition, GUE misses almost surely — is confirmed for every frozen draw, including
**seed 1, the seed the sector firewall actually ran on** (δ_rel = 0.0126).

## CONSEQUENCES (scoped)

1. **The failed sector-selection result cannot be rescued by a CPR referent.** The frozen
   family possesses no non-vacuous CPR-style local structure for the clustering to have
   matched. The `SECTOR_SELECTION_UNRESOLVED` outcome stands on its own terms, and the
   CPR-alignment EXPERIMENT is **not well-posed for the frozen family** — it is dissolved,
   not deferred.
2. **This is a bound on the frozen (d = 4, GUE) family only.** It is not evidence against
   relational physics generally, and not evidence that selection structure cannot exist in
   other model families. Any family engineered to satisfy δ = 0 would be a NEW pre-registered
   experiment (and tuning the family to obtain locality is barred here by order).
3. **Seed 5's near-miss carries no weight.** Approximate locality is outside CPR's theorem
   protection (assumption iii); reading δ_rel = 0.0026 as "almost a reference" would be
   exactly the unprotected inference this audit exists to prevent.
4. The K-mismatch recorded in Q1 (natural TPS operator partition = 3 classes {3,3,9} vs
   registered K = 4) is now moot for this family but remains a design fact for any successor.

## WHAT CANNOT BE CONCLUDED
Nothing about approximate/near-local structure (unregistered, unprotected); nothing about
other dimensions, ensembles, or graph-structured Hamiltonians; nothing about the RAI residue
(inexpressible in this class per `CROSS_WORKSTREAM_RRT0_RAI_AUDIT.md` §5); nothing about
RRT-1, whose design remains unstarted by order.

## STOP-POINT
No clustering run, no alignment run, no firewall rerun, no model modification, no RRT-1
design, no commit (pending explicit authorization). RRT-0's status ladder now reads:
semantic integrity PASS → reducibility PASS → mirror invariance PASS → sector selection
UNRESOLVED → **CPR reference: ABSENT for the frozen family.**
