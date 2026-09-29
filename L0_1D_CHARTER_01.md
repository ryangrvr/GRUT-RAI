# L0-1d — D-HERM-a (CYCLE AFFINITY): CHARTER + PRE-REGISTRATION (frozen before evaluation)

**STATUS: DRAFT REVISION 2 — NOT YET FROZEN. EXECUTION BLOCKED.**
The floor termination condition is adopted
(`L0_1_FLOOR_TERMINATION_ADOPTION_01.md`). The analytic-only pre-freeze
review (three independent reviewers, no member dynamics computed) is
complete. Its confirmed findings are incorporated below and recorded
in `L0_1D_PREFREEZE_REVIEW_01.md`. Revision 2 adds new mathematics
(the exact moment-Hankel battery, §2–§3), which gets one focused
analytic verification before freeze. The charter freezes at the commit
that removes this banner.

**Fork:** L0-1d, the first floor fork. It works on obligation **O-1**.
**Authority:** registry rulings R-1 … R-4 (R-3 at declared
linear-class scope); design basis `L0_1_FLOOR_DESIGN_01.md`. The
owner's four prohibitions bind. **Preview discipline:** no member
dynamics, kernel, Gram matrix, or member spectrum was computed to
write this charter or to review it. Every claim is a theorem, a
definition, or a labeled analytic expectation.

## 0. The frozen question, the hypothesis, the outcomes

> **When the generator stops being self-adjoint, is it asymmetry
> itself, or cycle affinity (broken detailed balance), that bears on
> the tested response properties?**

**H-HERM-1 (under attack):** cycle affinity, not asymmetry as such,
bears on P_positivity component (c), complete monotonicity (CM). It
does not bear on P_memory, whose exponential envelope accretivity
holds by identity.

**What the fork certifies vs what theorems already fix (stated first,
per the review):**
- **Theorem (Kolmogorov + F-1):** zero cycle affinity with
  sign-consistent couplings makes the generator diagonally
  symmetrizable. The retained-site kernel is then exactly that of a
  symmetric **reciprocal twin**, so it is exactly CM. *Affinity is
  necessary for a CM breach* is therefore a theorem, not a finding.
- **Analytic, not theorem (§3.4):** that every declared circulating
  member *does* breach CM.
- **Certified by this run:** the exact CM status of every declared
  member (a finite exact computation, §2); the P_memory reading at
  every member; and the maps.

**Outcomes (per-property, never composed):**
- **Outcome A, a zero-affinity member leaves the reciprocal class:**
  identity-impossible, so it is HALT (RC-3, RC-8).
- **Outcome B, the affinity split (the target):** every zero-affinity
  member is exactly CM, every circulating member is exactly not CM,
  and the memory envelope reading survives everywhere.
- **Outcome C, affinity without a CM breach:** some circulating
  member is exactly CM. This is a genuine, exact falsification of
  H-HERM-1's CM half at that member. It would mean the retained site
  sees no non-real pole, no negative residue, and no higher-order
  pole there.

**Held fixed:** the symmetric part K_s of every ring member, so
**accretivity (R-4) is held by construction.** Every member is also
Metzler (§3.3), so nonnegativity, component (a), is held by identity.
**Disclosed limitation (review finding):** K_s and the edge products
K_ij·K_ji cannot both be held fixed. Holding K_s makes every deformed
edge's product 1 − γ²a_e². The reciprocal twins (§1) separate that
renormalization from affinity.

## 1. Members, twins, conventions (frozen)

Kernel object: k(τ) = e₁ᵀe^{−Kτ}e₁ on a 23-dimensional bath block,
where e₁ is the site attached to the system.

**Conventions.** Sites 1…23. Ring edge e_i = (i, i+1) for i = 1…22,
and edge e₂₃ = (23, 1). An antisymmetric deformation with pattern a
sets K_{i,i+1} = −(1 − γa_i) and K_{i+1,i} = −(1 + γa_i), so transport
i → i+1 has rate 1 + γa_i. **Cycle affinity:**
𝒜 = Σ_i ln[(1 + γa_i)/(1 − γa_i)].

**Tree set T (the record's anchor; F-1 instantiation).** K_b = the
(1:, 1:) block of `build_K(24, 0)`, equal to 0.3I + L_path + e₁e₁ᵀ,
deformed along the 22 path edges with a_i = 1. **γ_T ∈ {0, 0.9}.**
γ = 0 is the sealed anchor.

**Ring substrate.** K_s = K_b + (e₁ − e₂₃)(e₁ − e₂₃)ᵀ: the tree bath
plus the closing spring (23, 1). Its diagonal is 3.3 at site 1 and 2.3
elsewhere.
- **Circulating members C(γ):** a_i = 1 on all 23 edges, so
  𝒜 = 23·ln((1+γ)/(1−γ)). **γ_C ∈ {0, 0.1, 0.3, 0.6, 0.9}.**
- **Balanced members B(γ) (zero affinity, same K_s, the
  asymmetry-without-affinity control the review asked for):**
  a_i = +1 for i = 1…11, −1 for i = 12…22, 0 for i = 23, so 𝒜 = 0
  exactly. **γ_B ∈ {0.3, 0.9}.**
- **Reciprocal twins S(γ) (references only, no trajectories):** the
  symmetric matrix with K_s's diagonal and every ring edge coupling
  −√(1 − γ²). S(γ) has the same edge products as C(γ) and zero
  affinity. Its moments equal C(γ)'s for every order n ≤ 22, because
  only walks that wind all the way round the ring (at least 23 steps)
  see affinity. **For γ_C ∈ {0.1, 0.3, 0.6, 0.9}.**
- **The tree twin S_T(γ)** = diag(K_b) − √(1−γ²)·Adj_path, the F-1
  reference for T(γ). Here "twin" never means K_s.

**Member roles:** T(0), C(0), B(·), and T(0.9) are zero-affinity,
identity-protected members. **C(γ > 0) are the adjudicating members.**
All γ values are exact rationals (1/10, 3/10, 3/5, 9/10), so every
exact computation in §2 is exact in ℚ.

## 2. Instruments and batteries (frozen)

**Instrument E (exact, static; R-3 at declared linear-class scope).**
For each member, compute in exact rational arithmetic (`fractions`):
- the Krylov vectors vₙ = Kⁿe₁;
- the moments sₙ = (vₙ)₁ for n = 0 … 47;
- the Krylov dimension r, the exact rank of [v₀ … v₂₃];
- the Hankel matrices H₀ = [s_{i+j}] and H₁ = [s_{i+j+1}],
  0 ≤ i, j < r.

**Exact CM test:** k is CM ⟺ H₀ ≻ 0 and H₁ ≻ 0. The test uses exact
LDLᵀ pivots, and every pivot must be strictly positive. The theorem is
§3.4.

**Exact mechanism map (ungated):**
- the retained-site recurrence polynomial p (monic, degree r, from
  the exact Krylov dependence);
- squarefreeness (gcd(p, p′));
- the number of distinct real roots, by an exact Sturm sequence;
- the inertia of H₀ (signs of its exact pivots), when no zero pivot
  arises.

**Instrument B (time-domain, eigen-free; P_memory and maps).**
x(0) = e₁, ẋ = −Kx, k(τ) = x₁(τ). RK4 on L0-1c's integer-count
schedule, carried verbatim: 10000 steps of h₁ = 10⁻⁴, then 15600 steps
of h₂ = 2.5×10⁻³. Recordings are made at step indices, and τ is never
accumulated. Every trajectory also gets a halved-schedule audit.
- **P_memory:** the RC-7-certified textual copy of `fit_residuals` +
  TAUS, applied to the discrete envelope
  E(τ_i) = max_{j ≥ i} |k(τ_j)| over the recorded gated grid (R-1).

**Eigen references (`jacobi_eig`, symmetric matrices only):** the
sealed anchor; S_T(0.9); C(0) (symmetric); the twins S(γ); every
member's K_s (for μ = λ_min(K_s)). `jacobi_eig` is also used on the
symmetric data Gram of the ungated operational map.

**Operational Gram map (ungated; measures what a trajectory battery
can see):** G_ij = k(τ_i + τ_j), τ_i ∈ {1.0, …, 20.0}. The minimum
eigenvalue is recorded, both full and halved schedule, at every
member.

**Grids:** gated τ ∈ [1, 40] step 0.5; early τ ∈ [0.05, 0.95] step
0.05. **Trajectories:** 9 members × (full + halved) = **18**.

## 3. Honesty note, stated before the run (identities first)

1. **F-1, reciprocal twin (identity).** For |γ| < 1, T(γ) is
   diagonally similar to S_T(γ), so k_{T(γ)} = k_{S_T(γ)} exactly.
   Likewise B(γ) is diagonally similar to its own symmetric twin,
   because its single cycle is balanced (Kolmogorov). **These kernels
   do change with γ;** what is identity-held is that they stay in the
   reciprocal (exactly CM) class. RC-3 and RC-8 instantiate this.
2. **Accretive envelope (identity).** K_s ⪰ μI gives
   |k(τ)| ≤ ‖e^{−Kτ}‖₂ ≤ e^{−μτ}. μ = λ_min(K_b) ≈ 0.3045 on T, and
   μ > 0.3 strictly on the ring. RC-6 instantiates this. The
   exponential *bound* on memory is therefore identity-held at every
   member. The comparator's *grade* on E is not fixed by it.
3. **Metzler sign (identity).** Every off-diagonal entry of −K is
   1 ± γa_i ≥ 0 and e₁e₁ᵀ is diagonal only, so k(τ) ≥ e^{−(max
   diag)τ} > 0. RC-5 instantiates this.
4. **The exact CM theorem behind Instrument E.** Here k is an
   exponential polynomial whose moments sₙ = (−1)ⁿk⁽ⁿ⁾(0) satisfy the
   order-r recurrence p. By Bernstein's theorem and the uniqueness of
   exponential-polynomial representations, k is CM ⟺ the retained-site
   spectral data are r real, simple, nonnegative poles with positive
   residues. That excludes a non-real pole, a negative residue, and a
   higher-order (Jordan) pole. By the finite Hamburger/Hermite theorem,
   the quadratic form ⟨p, q⟩ = L(pq) on polynomials of degree < r has
   Gram matrix H₀. It is positive definite ⟺ all r atoms are real and
   simple with positive weights; each complex pair or Jordan block
   contributes indefinite signature. H₁ ≻ 0 then places the atoms in
   (0, ∞). The test is exact: no tolerance, no integration, no
   floating point.
5. **Why a circulating member should breach CM (analytic, not
   theorem).** The review corrected the charter's earlier circulant
   picture, which ignored the e₁e₁ᵀ defect and was wrong at small γ.
   - Let R be the ring reflection fixing site 1. Then RK(γ)R = K(γ)ᵀ,
     so K is self-adjoint in the indefinite form xᵀRy, and the kernel
     is even in γ.
   - At γ = 0, the 11 R-odd modes vanish at site 1. The 12 R-even
     modes strictly interlace them, so the spectrum is simple.
   - **Hence the spectrum stays real for small γ > 0** (γ below the
     first collision, an exceptional point).
   - In that real phase, the weight of an odd-born mode is
     cⱼ = (vⱼ,₁)² / (vⱼᵀRvⱼ), with vᵀRv = −1 + O(γ²), and vⱼ,₁ = O(γ)
     nonzero by first-order perturbation, because all its terms have
     one sign. **So cⱼ = −O(γ²) < 0: CM breaks through negative real
     weights, with no oscillation.**
   - Beyond an exceptional point, non-real poles break it.

   Either way, a breach is expected at every γ > 0. It is
   analytic-leaning rather than theorem because the perturbation
   argument is first-order and the exceptional-point locations are not
   derived.
6. **Labeled analytic expectations for the maps (recorded to be
   confirmed or refuted; they move no label):**
   - C(0.1) is in the real phase: the Sturm count equals r, and p is
     squarefree.
   - H₀ inertia at C(0.1) shows negative pivots, consistent with
     negative real weights.
   - The operational Gram minimum eigenvalue at small γ is at or near
     the integration floor. That would mean the trajectory battery
     cannot see a breach the exact battery does see, at least at the
     smallest γ.
   - Somewhere in (0.1, 0.9], exceptional points appear, and the Sturm
     count drops below r.
7. **Classification.**
   - *Identity-grade:* RC-3, RC-5, RC-6, RC-8, and every zero-affinity
     member's exact-CM result.
   - *Analytic-leaning:* H-1, the exact breach at every C(γ > 0); M-1
     on T(0), which is sealed.
   - *Not banded, genuinely attackable:* M-1 on T(0.9), B(·) and the
     C members. The E-staircase of an oscillating kernel could flip the
     comparator's grade; §5 routes such a flip.
   - *Also not banded:* X-1′ (§4). Moments agree with the twin up to
     n = 22, so the affinity effect is late-onset, and a null is
     possible.
   - *Genuinely unpredicted (maps):* phase structure, exceptional-point
     location, operational detection versus exact breach, and E(40)
     and tails.
   - **Component (b), monotone decrease, is not adjudicated.**
     H-HERM-1 makes no claim about it; it belongs to H-HERM-2 (O-2).
     It is mapped.
8. **F-7 corrected (the review's finding; the owner's O-2 ruling
   applied).**
   - F-7 is an **observability/identity result about the retained-site
     observable**, never evidence about accretivity or H-HERM-2's
     physics. It holds only for generators diagonally similar to a
     normal matrix. For a single directed weighted cycle that requires
     a **uniform diagonal** (and a nonzero return weight).
   - **The record's attachment convention (e₁e₁ᵀ) breaks that
     hypothesis**, so F-7 does **not** cover the natural O-2 candidate:
     the attached, spectrally stable, non-accretive directed ring.
   - Even where F-7 applies, it excludes only growth above
     e^{−min Re λ·τ}. It does not make the kernel "invisible".
   - **O-2 is therefore not deferred on F-7 grounds.** The attached
     directed ring is a live O-2 candidate for its own charter.
     "Perron weight at e₁ above 1" is recorded only as a sufficient
     witness of non-normal-similarity, not a necessary condition.

## 4. The gates (frozen, mechanical)

**Controls and identities (halt-grade; a breach anywhere is HALT):**
- **RC-1 replication:**
  - the eigen-form anchor k(40) = 6.8195192260507686×10⁻⁹
    (|rel Δ| < 10⁻⁹);
  - the anchor time-domain run matches its eigen form,
    sup |k_td − k_eig|·e^{μτ} < 10⁻⁶ on the gated grid.
- **RC-2 halved-schedule audit, every trajectory:**
  sup |k_full − k_half|·e^{μτ} < 10⁻⁶. This is envelope-normalized,
  per the review's analytic RK4 bound; a relative-to-k tolerance would
  be infeasible at the minima of an oscillating kernel.
- **RC-3 reciprocal twins, time-domain:** k_{T(0.9)} matches the eigen
  kernel of S_T(0.9), and k_{C(0)} matches its own eigen kernel. Both
  checks use sup |Δk|·e^{μτ} < 10⁻⁶.
- **RC-5 sign:** k > 0 at every recorded point of every trajectory.
- **RC-6 accretive envelope:** |k(τ)| ≤ e^{−μτ}(1 + 10⁻⁹) at every
  recorded point of every member.
- **RC-7 comparator certification (R-1 instantiated):**
  - on the **eigen-form** anchor kernel, E = k exactly at every gated
    point;
  - the comparator on E reproduces R_exp = 1.9809889100368165 and
    R_alg = 4.7907669413552245 (|Δ| < 10⁻¹² each) and the grade string
    "EXPONENTIAL-GRADE" exactly.
- **RC-8 exact CM on every zero-affinity member (identity):** H₀ ≻ 0
  and H₁ ≻ 0 exactly, at T(0), T(0.9), C(0), B(0.3), and B(0.9).
- **RC-9 exact-arithmetic self-check:** at C(0), the Krylov dimension
  r is exactly 12 (the R-even sector). Separately, at every member the
  exact moments s₀ … s₄ match the float moments of the recorded K to
  |rel Δ| < 10⁻¹²; a mismatch means the rational and float
  constructions diverge.

**X, the affinity deletion acts in the window (conditions only the
P_memory line):**
- **X-1′:** at C(0.9), sup over the gated grid of
  |k_{C(0.9)} − k_{S(0.9)}|·e^{μτ} > 0.01. This is not banded (§3.7).

**The response properties:**
- **H-1, P_positivity (c), exact (the H-HERM-1 gate; analytic-leaning):**
  every adjudicating member C(0.1), C(0.3), C(0.6), C(0.9) fails the
  exact CM test (H₀ or H₁ not ≻ 0).
- **M-1, P_memory (R-1 envelope reading):** the comparator on E reads
  EXPONENTIAL-GRADE at every member.
- **Maps (ungated):**
  - the exact mechanism map (r, squarefreeness, Sturm real-root count,
    H₀ inertia) at every member;
  - operational Gram minimum eigenvalue (full and halved) at every
    member;
  - the monotone-decrease status of component (b) at every member;
  - E(40) and tail slopes;
  - 𝒜 and μ per member;
  - the early-grid transient map;
  - |k_C − k_S| per γ.

## 5. Outcome rule (frozen, mechanical; lines never composed)

**Scope clause, on the face of every recorded line under every
outcome, including PARTIAL and HALT:** *within the declared background
mathematics — exact rational arithmetic for Instrument E, the frozen
RK4 schedule for Instrument B, and exact symmetric eigendecomposition
for the identity references — the declared members T ∈ {0, 0.9},
C ∈ {0, 0.1, 0.3, 0.6, 0.9}, B ∈ {0.3, 0.9} on the sealed C1 bath and
its one-spring ring closure, with K_s held, and the declared window,
grids, and comparator.*

**The lines:**
- **L-1 · NON-RECIPROCITY WITHOUT CYCLE AFFINITY: REDUCIBLE TO A
  RECIPROCAL TWIN (identity-grade; F-1 and Kolmogorov
  instantiated).** Issued iff RC-3 and RC-8 hold. Its face states that
  these kernels change with γ and stay in the reciprocal class.
- **L-2 · CYCLE AFFINITY: BREAKS P_positivity (c), complete
  monotonicity, exactly, at every declared circulating member.**
  Issued iff H-1 holds. Its face:
  - (i) *necessity of affinity for any breach is a theorem*;
  - (ii) *the breach at each declared member is certified by exact
    computation*;
  - (iii) components: **(c) adjudicated exactly; (a) held by identity
    at all members; (b) not adjudicated, mapped.**
- **L-3 · CYCLE AFFINITY: NOT-LOAD-BEARING for P_memory (R-1 envelope
  reading; accretivity held).** Issued iff M-1 holds and X-1′ holds.
- **M-1 failure at any member while RC-6 is clean:** recorded as
  **COMPARATOR-LIMITATION.** The comparator graded E ALGEBRAIC although
  the identity-held bound |k| ≤ e^{−μτ} holds. This is an instrument
  finding, never "affinity load-bearing for P_memory". L-3 is not
  issued, and the run label is L01D-PARTIAL.
- **X-1′ failure:** L-3 is not issued (the memory line would be
  vacuous). L-1 and L-2 are unaffected. Run label L01D-PARTIAL.

**Run labels:**
- **Outcome B (the affinity split):** L-1, L-2, and L-3 all issue.
  Recorded as: *on one substrate with one symmetric part,
  zero-affinity asymmetry keeps the retained-site kernel exactly in the
  reciprocal, completely monotone class; cycle affinity takes it out
  of that class at every declared member; the exponential memory
  envelope survives throughout.*
- **Outcome C (affinity without CM breach):** RC clean, and some
  C(γ > 0) passes the exact CM test. H-HERM-1's CM half is **exactly
  falsified at the listed members.** L-1 and L-3 are still issued or
  withheld on their own conditions.
- **L01D-PARTIAL:** comparator limitation, X-1′ failure, or any other
  non-RC gate failure.
- **HALT:** any RC breach.
- **Precedence (run labels only):** HALT > Outcome C > L01D-PARTIAL.
  Outcome B requires all three lines. The precedence composes no lines
  and suppresses none.

**Mapping to O-1's terminal labels** (proposed; the owner assigns the
label, per T2):

| Run outcome | Supports | Uses O-1's one re-charter? |
|---|---|---|
| Outcome B | **CLASS-SPLIT** for P_positivity (c): zero-affinity class exactly CM, affinity class exactly not CM, same substrate. L-3 is certified inside it. | no |
| Outcome C | **FALSIFIED** (H-HERM-1's CM half), terminal | no |
| L01D-PARTIAL / HALT | non-terminal | **yes.** A second non-terminal outcome ends O-1 as UNFORMULABLE-WITH-DOCUMENTED-REASON unless the owner rules CLASS-SPLIT from the record (T3). |

Under every outcome: no v4 channel moves; no red gate is touched; GR2,
L0-1a/b/c, and the public paper are untouched. **HARD STOP** after the
verdict, pending owner ruling on the lines and O-1's terminal label.

## 6. Instrument contract

`calc/l01d_cycle_affinity.py`: pure stdlib (`fractions` for
Instrument E). It imports `build_K` (for K_b) and `jacobi_eig`
(symmetric references and the symmetric data Gram only) unchanged. It
carries the RC-7-certified textual copy of `fit_residuals` + TAUS. RK4
runs exactly as in §2. It is deterministic, with no RNG, and runs once:
18 trajectories plus exact moment computations for 9 members. It
writes `L0_1D_RESULT.json` (sha-hashed) with `defect_history`. Runtime
is minutes. Scope: the §5 clause, nothing else.
