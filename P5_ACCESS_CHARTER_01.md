# P-5 — ATTACK THE ACCESS STRUCTURE: OWNER RULING RECORD + CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Date:** 2026-09-25 · **Authority:** GitHub Issue #2, owner comment
**5827176252** (the authoritative instruction; this charter freezes the
implementation). **P-4 acceptance recorded with its binding statements:**
𝔠_full remains a CANDIDATE interface characterization, complete only
within the declared finite bounded-access class; (K,N) is the two-point
face; the order-8 gate failure stays recorded (the asymptotic diagnostic
may explain, does not erase, the red); the hierarchy/Gram condition is
NULL-AS-NEW-PRINCIPLE with a descriptive unification dividend; and —
**tightened** — *"access is the last place a new principle could hide" is
NOT a theorem; it is the present remainder that P-5 must attack.* The
conceptual chain under test: microscopic dynamics → influence hierarchy →
sector structure → **access structure?** → effective physics.

**Question (owner, verbatim in substance):** what, if anything, determines
the physical access boundary itself? "Access structure" is a **CANDIDATE,
not an axiom**, tested across: representational choice vs dynamically
constrained structure vs genuinely additional physical structure.
**Fences:** Λ_R, Matsubara, Π₀, U5, ω⁷/class-4, no proof-of-QM; no move
to gravity or geometry until P-5 completes (owner gate). Operational
constructions only (owner point F): every claim below has a construction
and a pre-registered observable.

## 1. THE LEGS (frozen; all exact finite spin models; ≥1 genuinely noncommuting)

- **L-E (positive control for MERE REPRESENTATION, owner point E):**
  bath = 3 spins (ω = 1 each), B = Σ gᵢσ_xⁱ, g = (0.5, 0.4, 0.3), probe
  pure dephasing (λ = 1). Refactorize by the **entangling** bath unitary
  V = exp(−i·0.7·σ_x²σ_z³) (a genuinely noncommuting recombination of the
  declared subsystems): H → VHV†, B → VBV†, |gs⟩ → V|gs⟩. Pre-registered
  observable: the probe coherence trajectory on t ∈ [0, 10] (200 pts).
  **Gate:** identical to < 1e-9 ⇒ the factorization/embedding is
  REPRESENTATIONAL.
- **L-A (access as bookkeeping across INEQUIVALENT declarations, owner
  point A):** bath-small = 1 spin (ω = 1, g = 0.5) vs bath-big = the same
  accessed spin ⊕ a dynamically decoupled 2-spin hidden sector
  (H_hid = 0.8σ_x²σ_x³ + 0.3σ_z², hidden initial state |↓↓⟩). Different
  total algebras, identical coupling map. **Gate:** in-access coherence
  identical < 1e-9; the declared partition difference changes nothing
  coupled.
- **L-B/C (dynamical constraint + emergent minimal algebra, owner points
  B, C):** on a 2-spin bath (16-dim operator space), compute the
  **dynamically generated algebra** 𝒜(seed; H) = closure of {I, H, B}
  under products (Hilbert–Schmidt Gram–Schmidt span, iterated to
  stability). Frozen cases: (i) generic seed + generic H → expected full
  dimension 16; (ii) parity-symmetric seed and H ([·, σ_z¹σ_z²] = 0) →
  expected commutant-block dimension 8; (iii) abelian seed with commuting
  H → small closure (measured). **Adjudication rule:** the closure is
  canonical GIVEN a seed (uniqueness = span construction); symmetry
  constrains it to the commutant (bicommutant theory CITED as standard —
  NULL-REDUNDANT as a new principle); **the seed itself remains a
  declaration** — reported as the residual, not absorbed. Seedless
  minimality: no canonical selection generically — tied to P-1's
  trichotomy (structured dynamics may distinguish; generic does not);
  class UNDERDETERMINED.
- **L-D (the counterattack, owner point D):** two constructions sharing
  ALL candidate universal constraints and identical in-access influence
  hierarchy: hidden-A (H_hid as above) vs hidden-B
  (H_hid = −1.1σ_x²σ_x³ + 0.6σ_z³), same hidden initial state, same
  accessed spin and coupling. Pre-registered observables: (i) in-access:
  the probe coherence, t ∈ [0, 10] — **gate: identical < 1e-9**;
  (ii) out-of-access: ⟨σ_z²(t)⟩ — **gate: differs > 0.05**;
  (iii) **the access-extension probe:** at t* = 3.0 the coupling map
  changes (B → B + 0.4σ_x², a quench); post-quench probe coherence —
  **gate: differs > 1e-3 between hidden-A and hidden-B** while pre-quench
  coherence is identical. Frozen consequence rule: (i)+(ii) ⇒
  **ACCESS-SPLIT** (the boundary is underdetermining: in-access data
  cannot fix out-of-access physics); (iii) ⇒ the split is **conditionally
  physical**: invisible forever under fixed access, consequential exactly
  when access changes.

## 2. OUTCOME TAXONOMY (owner minimum, frozen mechanical)

**REPRESENTATIONAL** (L-E/L-A gates) · **DYNAMICALLY-CONSTRAINED** (L-B/C
dimensions land as declared, seed residual reported) · **ACCESS-SPLIT**
(L-D gates) · **NULL-REDUNDANT** (any found constraint reducing to
standard structure — bicommutant, state positivity — so recorded) ·
**UNDERDETERMINED** (seedless minimality; or any leg failing to decide).
Components reported separately, never averaged. A clean failure that
locates the first genuine obstruction is a successful outcome.

## 3. CONTROLS

The L-E identity is analytic (unitary equivalence) — a numerical breach
> 1e-9 HALTS as an instrument bug, never physics; the L-A/L-D in-access
identity is analytic (commuting factor) — same halt rule; the L-D
out-of-access and post-quench differences carry the matched control
(hidden-A vs hidden-A: 0 to 1e-12); closure dimensions verified stable
under one extra iteration; all thresholds frozen above.

## 4. DELIVERABLES AND STOP

1. `calc/p5_access.py` (pure stdlib; emits `P5_ACCESS_RESULT.json`,
   sha-hashed).
2. `P5_ACCESS_VERDICT_01.md` + closing comment on Issue #2.
3. **HARD STOP at the verdict.** Per the owner gate, gravity and geometry
   stay closed until then (and open only per the owner's rule if P-5
   fails/underdetermines).
