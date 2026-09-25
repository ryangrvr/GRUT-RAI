# P-4 — ATTACK ON THE INFLUENCE HIERARCHY: CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Date:** 2026-09-25 · **Chartered by:** owner (`P3_P4_OWNER_RULING_01.md`
§4, seven-point attack program). Question: **can the influence hierarchy
be characterized by universal admissibility constraints — what replaces
the Gaussian cone when all cumulants are admitted?** The hierarchy is a
CANDIDATE under attack, not an established object (binding tightening,
ruling §2). Redundancy rule binding at hierarchy level: a characterization
reducible to state positivity is NULL-AS-NEW-PRINCIPLE (its unification
value, if any, is reported separately). ℏ stays located-not-generated.
Fences: Λ_R, Matsubara, Π₀, U5; ω⁷/class-4; no proof-of-QM. All models
exact finite spin baths (dephasing probe, common machinery with P-3,
reused where validated, fresh where the leg demands independence).

## 1. THE MATCHING LADDER (owner points 1–3)

- **L4-A (order-4 mismatch, reused):** P-3's pair — matched (K, N), κ₃ = 0
  both, κ₄ = −4g⁴ vs −8g⁴ (g = 0.5). Coherence difference Δ₄ re-measured.
- **L4-B (order-6 mismatch, new construction):** two 3-spin baths at
  COMMON frequency ω₀ = 1 with coupling-square multisets of equal power
  sums p₁ = Σyᵢ and p₂ = Σyᵢ² but different p₃ = Σyᵢ³:
  y_A = (1, 2, 3); y_B = (y₁, 1.5, y₃) with y₁ + y₃ = 4.5,
  y₁y₃ = 4.25 (t = 1.5 branch). At common frequency this matches ALL
  connected cumulants through order 4 — including multi-time — and first
  differs at order 6 (κ₆ ∝ p₃). Frozen verification gates: equal-time m₂,
  m₄ match to 1e-9 and m₆ differ; C(t) matches at sample times to 1e-9;
  a sample MULTI-TIME connected 4-point matches to 1e-9; a sample
  connected 6-point differs.
- **L4-C (λ-scaling forensics — discrimination enters at the first
  unmatched order):** coherence differences at λ = 0.4 vs λ = 0.2 must
  scale as the first unmatched cumulant order: ratio ≈ 2⁴ = 16 for L4-A,
  ≈ 2⁶ = 64 for L4-B, each within the frozen factor window [0.7, 1.4]×.
- **Frozen consequence rule:** L4-A + L4-B detected ⇒ **finite matching
  never certifies equivalence** (constructive at two orders, with the
  scaling law showing the pattern continues); full-hierarchy matching
  certifies WITHIN the finite bounded class (the P-3 Q5 result is the
  positive control: full-influence-equal realizations are probe-identical
  at 1.1e-14) — bounded-operator moment determinacy is CITED as standard
  mathematics, verified only in-class, never claimed beyond it.

## 2. THE SINGLE POSITIVE OBJECT (owner points 4–5)

**Candidate (hypothesis only):** complete positive-definiteness of the
influence moment hierarchy — state positivity on the *-algebra generated
by {B(t)}, operationally: every finite Gram matrix M_ij = ⟨Xᵢ†Xⱼ⟩ over
monomials in {B(tₖ)} is PSD.

- **H4-A (classical face):** equal-time Hankel matrix H_ij = ⟨B^{i+j}⟩
  (orders 0–6) PSD on the real baths; a TAMPERED hierarchy with
  m₄ < m₂² (Cauchy–Schwarz violation) must be DETECTED (halt-grade
  detector).
- **H4-B (quantum face):** the multi-time operator Gram over
  {1, B(0), B(t)} is PSD on the real baths at declared sample times; a
  TAMPERED pair with the antisymmetric (commutator) part of C(t) inflated
  ×1.5 at fixed symmetric part must be DETECTED — this face is the
  hierarchy-level home of the ℏ floor.
- **H4-C (unification claim, tested not assumed):** the P-2 cone's two
  constraints are LOW-ORDER FACES of the single Gram condition — C-pos
  and the ℏ floor from the order-2 face (numerical demonstration on the
  model, plus citation of P-3 Q1's ν ± J/2 ⪰ 0 as the frequency-domain
  form). If the faces do NOT reproduce the cone, that failure is reported.
- **Redundancy adjudication (frozen):** if the candidate object is
  exhibited as state positivity (Gram construction), the verdict is
  CHARACTERIZED-AND-REDUCIBLE: NULL-AS-NEW-PRINCIPLE, with the
  unification dividend (one object replacing two axioms) reported
  separately and never promoted to a new law.

## 3. THE DESCRIPTIVENESS ATTACK (owner points 6–7)

Try to construct two different full hierarchies satisfying all candidate
constraints but producing different observable physics **within the
declared access structure** (probe coupled through B). Frozen adjudication:

- In the finite class, the reduced probe dynamics is a functional of the
  contour-ordered influence functional BY CONSTRUCTION (Feynman–Vernon at
  operator level) — so an in-access counterexample requires two states
  with identical full hierarchies and different reduced dynamics. The
  instrument attacks this constructively: the L4-B pair (maximally
  different microscopics at matched low orders) is pushed to
  higher-order matching in a declared attempt; any residual difference
  must track an explicitly named unmatched cumulant (the λ-scaling
  gate), else DESCRIPTIVE-ONLY is declared.
- **Honest scope line (frozen):** failure to find a counterexample
  in-class establishes completeness OF THE INTERFACE for the declared
  access, not a statement about physics outside the access boundary
  (D-1's lesson carries: access, not vocabulary, is where distinctions
  live).

## 4. OUTCOME CLASSES (frozen, mechanical)

**CHARACTERIZED-AND-REDUCIBLE** (compact object exists = hierarchy
positive-definiteness; contains the cone as its two-point face; reducible
to state positivity) · **LADDER-ESTABLISHED** (finite matching never
certifies; discrimination enters at the first unmatched order by
λ-scaling; full matching certifies in-class) · **DESCRIPTIVE-ONLY** (a
constraint-satisfying pair with different in-access physics exists) ·
**FACE-FAILURE** (the cone is NOT a face of the candidate object) ·
**FAILS-NULL** (a leg's construction fails). Components reported
separately; never averaged.

## 5. CONTROLS

All matching gates at 1e-9 before any coherence comparison; both tampered
detectors halt-grade; the matched-relabeling control (< 1e-12) rides every
coherence leg; λ-scaling windows frozen above; L4-B's y_B computed in-run
from the declared equations (no hand-tuned numerals beyond t = 1.5).

## 6. DELIVERABLES AND STOP

1. `calc/p4_hierarchy.py` (pure stdlib; emits `P4_HIERARCHY_RESULT.json`,
   sha-hashed).
2. `P4_HIERARCHY_VERDICT_01.md` — per-leg verdicts, the composite, what
   "replaces" the Gaussian cone at recorded strength, and the standing
   non-derived remainder (which hierarchy reality realizes; the floor's
   scale).
3. **HARD STOP at the verdict.** Owner rules next.
