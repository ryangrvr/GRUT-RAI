# L0-1b — LOCALITY: CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Fork:** L0-1b, the second fork of the Level-0 necessity sweep.
**Authority:** `L0_1A_OWNER_RULING_01.md` (D-LOC authorized next;
Outcomes A and B named in advance) within
`GRUT_PROGRAM_STATE_SYNTHESIS_01.md` §§28, 34; design basis
`L0_1_NECESSITY_SWEEP_DESIGN_01.md` §4 D-LOC. The owner's four
prohibitions bind.

## 0. The frozen question and the two named outcomes (the owner's)

> **Is locality actually necessary for the response itself, or only
> for geometry?**

- **Outcome A (collapse):** remove locality and everything collapses —
  locality is a broad substrate requirement.
- **Outcome B (the split):** response survives while spatial geometry
  fails — *response does not require space; space requires a
  particular organization of response.*

**The deletion touches locality ONLY:** every member keeps the pin
(0.3) and positive couplings, so the gap and passivity — both
necessity-certified in L0-1a — are held fixed by construction. A
memory or positivity change at a nonlocal member could then only be an
instrument defect, and the gates treat it as such.

## 1. Members (frozen; N = 24; global coupling norm held)

Weighted all-pairs spring networks, w_ij = c_α · |i−j|^{−α}, with c_α
fixed by the frozen normalization Σ_{i<j} w_ij = 23 (the anchor's total
spring weight). Members: **anchor** (nearest-neighbor only, w = 1.0) —
α ∈ {4, 3, 2, 1.5, 1, 0.5} (the crossover map) — **deleted member**
α = 0 (the uniform complete graph, w_ij = 1/12 each: locality fully
deleted). K = 0.3·I + L(w); bath = the (1:, 1:) block; kernel
k(τ) = Σu²e^{−λτ} on τ ∈ [1, 40] step 0.5, exactly the L0-1a
machinery.

## 2. The pre-committed geometry battery (discharging the design obligation)

Geometry reads the **relational coupling structure**: the resistance
metric on the full coupling Laplacian L(w), pins excluded —
R_ij = (e_i − e_j)ᵀ L⁺ (e_i − e_j), the record's resistance-geometry
grade. **The pre-committed criterion:**

- **Q = max_{i≠j} R_ij / min_{i≠j} R_ij** (the distance dynamic range)
  and the **line-ordering test** (R_{1,j} strictly increasing in j).
- **SURVIVES** at a member iff Q ≥ 12 (= N/2) AND the ordering is
  monotone. **FAILS** iff Q < 2 (all points nearly equidistant — no
  recoverable line structure). **DEGRADED** otherwise — mapped,
  ungated.

## 3. Honesty note, stated before the run (the L0-1a factorization precedent)

The END behaviors are analytic: the anchor obeys the series law
(R_ij = |i−j| exactly, so Q = 23 and monotone), and the deleted
member's complete-graph symmetry forces R_ij = 2/(N·w) = 1 exactly for
every pair (Q = 1). The certification at the ends is therefore
**structural**, and the instrument's gates there are identity-grade —
a breach is an instrument bug, never physics. The genuinely unknown,
attackable content is: (i) the **crossover map** — where in α the
recovered geometry collapses (frozen note, ungated: folklore expects
the boundary near α ≈ 2 for 1D long-range networks; the map tests it);
(ii) the one **non-identity gated prediction** H-SR below.

## 4. The gates (frozen, mechanical)

**Controls and identities (halt-grade):**
- RC-1 the anchor reproduces L0-1a's anchor exactly: K(anchor) equals
  `build_K(24, 0)` entrywise (< 1e-15) and k(40) matches L0-1a's
  recorded 6.8195e-9 (|rel Δ| < 1e-6).
- RC-2 per member: k(0) = 1 (|Δ| < 1e-12); λ_min(bath) ≥ 0.3 − 1e-12
  (the pin identity — gap and passivity held); L(w) has exactly one
  zero mode (< 1e-10) with the second eigenvalue > 1e-10
  (connectivity).
- RC-3 the end identities: anchor max|R_ij − |i−j|| < 1e-9; deleted
  member max|R_ij − 1| < 1e-9.

**P_memory and P_positivity under the deletion (analytic-backed):**
- M-1 (gate) k(40) < 1e-5 at **every** member (the finite-memory-grade
  survival, guaranteed by the held pin: k(40) ≤ e^{−12}).
- M-2 (gate) the kernel is monotone decreasing at every member (steps
  ≤ +1e-12; positivity survival by construction).
- M-diag (ungated): the grade comparator per member, reported.

**P_geometry under the deletion:**
- G-1 (gate; identity-backed) the anchor SURVIVES (Q ≥ 12, monotone
  ordering) and the deleted member FAILS (Q < 2) under the §2
  criterion.
- G-2 (gate; the attackable non-identity prediction) **H-SR:** the
  short-range class survives genuine nonlocality — at α = 4 (all pairs
  coupled, weights summable), Q ≥ 12 and the ordering is monotone.
- G-map (ungated): Q(α) and the ordering status for every member — the
  crossover map, the fork's exploratory payload.

## 5. Outcome rule (frozen, mechanical; per-property lines, never composed)

- **LOCALITY: NOT-LOAD-BEARING for P_memory / for P_positivity** iff
  M-1 / M-2 hold at every member including the full deletion (two
  lines).
- **LOCALITY: NECESSITY-CERTIFIED for P_geometry** iff RC-3 and G-1
  hold (with G-2's status reported inside the line).
- **THE SPLIT (Outcome B) is certified** iff all three lines land as
  above — recorded as: *response does not require locality; recoverable
  spatial geometry does — within the declared background mathematics,
  the tested weighted-network class on N = 24, and the §2 criterion.*
- **Outcome A (collapse)** would require M-1/M-2 failures at nonlocal
  members — which the held pin makes identity-impossible; any such
  breach is **HALT** (instrument bug), and Outcome A is then decidable
  only by a future fork that deletes locality without the pin held
  (out of scope here, noted for the record).
- **L01B-PARTIAL** for any other gate failure; **HALT** on any RC
  breach.

Under every outcome: no v4 channel moves; no red gate is touched; GR2
and L0-1a unmodified; the public paper untouched. **HARD STOP** after
the verdict, pending owner ruling (which decides L0-1c, linearity,
next per the frozen descent order).

## 6. Instrument contract

`calc/l01b_locality.py`: pure stdlib; imports `build_K` (anchor
control) and `jacobi_eig` unchanged; deterministic, no RNG; single
run; writes `L0_1B_RESULT.json` (sha-hashed) with `defect_history`;
runtime seconds. Scope: the weighted-network class above; the §2
criterion; nothing else.
