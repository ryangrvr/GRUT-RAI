# L0-1d — D-HERM-a (CYCLE AFFINITY): CHARTER + PRE-REGISTRATION (frozen before evaluation)

**STATUS: DRAFT — NOT YET FROZEN. EXECUTION BLOCKED.** Per the owner
(`L0_1_FLOOR_REGISTRY_RULINGS_01.md`), this charter may not freeze
until **(1)** the floor termination condition is adopted
(`L0_1_FLOOR_TERMINATION_DRAFT_01.md`), and **(2)** it has passed the
house pre-freeze adversarial review. That review should be
**analytic-only**: reviewers may not integrate the member dynamics, so
that, unlike L0-1c, there is nothing to quarantine. The charter
freezes at the commit that removes this banner. No instrument exists
and no gate binds until then.

**Fork:** L0-1d, the first floor fork; discharges obligation **O-1**
of the draft termination condition. **Authority:** the owner's
registry rulings R-1 … R-4 and sequence authorization;
design basis `L0_1_FLOOR_DESIGN_01.md` §§1–3. The owner's four
prohibitions bind. **Preview discipline:** no computation was run to
write this charter; every number below is a theorem, a definition,
or an analytic estimate labeled as such.

## 0. The frozen question, the hypothesis, the named outcomes

> **When the generator stops being self-adjoint, is it asymmetry
> itself, or cycle affinity (broken detailed balance), that bears on
> the tested response properties?**

**H-HERM-1 (under attack):** cycle affinity, not asymmetry as such,
is load-bearing for P_positivity (the complete-monotonicity reading);
it is not load-bearing for P_memory, which accretivity holds by
identity.

- **Outcome A (asymmetry matters):** asymmetric members with **zero**
  cycle affinity (trees) change the retained-site kernel. F-1 makes
  this identity-impossible; a breach is HALT (an instrument bug).
- **Outcome B (the affinity split, the target):** zero-affinity
  asymmetry is invisible from the retained site; nonzero affinity
  breaks the complete-monotonicity reading while the memory envelope
  survives.
- **Outcome C (affinity undetected):** even at the strongest tested
  affinity, the operational CM battery registers no breach at the
  frozen tolerance. H-HERM-1 is then falsified *at operational scope*,
  and the record states that exact CM is still broken by theorem
  (§3.4). The operational battery simply cannot see it at this
  tolerance.

**What is held fixed:** the symmetric part K_s of every member is
unchanged by the deletion (the deletion is purely antisymmetric), so
**accretivity (R-4) is held by construction** and the gap is held in
the accretive sense. Every member is also Metzler (§3.3), so
nonnegativity of the kernel is held by identity.

## 1. Members (frozen)

The kernel object is the record's convention: k(τ) = e₁ᵀe^{−Kτ}e₁ on
a bath block K, where e₁ is the bath site attached to the system.

**Tree set T (zero cycle affinity; the "asymmetry without affinity"
control).** The sealed C1 bath block K_b (from `build_K(24, 0)`), with
an antisymmetric path deformation: K = K_b + γA_path, where
(A_path)_{i,i+1} = +1, (A_path)_{i+1,i} = −1 along the chain.
γ ∈ {0, 0.3, 0.9}. γ = 0 is the sealed anchor.

**Ring set H (nonzero cycle affinity; the deletion).** A 23-site
pinned bath ring: K_s = 0.3·I + L_ring + e₁e₁ᵀ. Here L_ring is the
unit-spring Laplacian of the cycle 1–2–…–23–1, and e₁e₁ᵀ is the
system spring on the attached site (the record's attachment
convention). The members are K(γ) = K_s + γA_ring, with A_ring the
antisymmetric circulation around the ring:
γ ∈ {0, 0.1, 0.3, 0.6, 0.9}. **Deletion measure (analytic):** the
cycle affinity 𝒜(γ) = 23·ln((1 + γ)/(1 − γ)), which is zero only at
γ = 0.

**Leg roles:** T members are identity-protected controls (F-1). The
ring γ = 0 member is the symmetric replication leg of the new
substrate. The ring γ > 0 members are the adjudicating legs.

## 2. Instrument and batteries (frozen)

**Instrument B (time-domain, eigen-free):** x(0) = e₁,
ẋ = −Kx, k(τ) = x₁(τ). Classical RK4 with the L0-1c integer-count
schedule, carried verbatim: 10000 steps of h₁ = 10⁻⁴, then 15600
steps of h₂ = 2.5×10⁻³; recordings at step indices only; τ is never
accumulated. Every trajectory also gets a halved-schedule audit.

**Eigen references (identity controls only):** `jacobi_eig` on
*symmetric* matrices only: the sealed anchor; each tree member's
symmetrized chain (§3.1); the ring's γ = 0 member; and every
member's K_s (for accretivity).

**Batteries (under the amended registry):**
- **P_memory:** the certified textual copy of `fit_residuals` + TAUS
  (the L0-1c carrying mechanism) applied to the envelope
  E(τ) = max_{τ′∈[τ,40]} |k(τ′)| on the gated grid (R-1).
- **P_positivity, component (c), complete monotonicity:** the
  trajectory Gram G_ij = k(τ_i + τ_j), τ_i ∈ {1.0, 1.5, …, 20.0},
  minimum eigenvalue compared with −10⁻¹⁰ (the L0-1c M-3 form).
- **P_positivity, component (b), monotone decrease:** mapped, **not
  gated** in this fork (§3.4 explains why).
- **P_positivity, component (a), nonnegativity:** identity-held
  (§3.3). It lives in RC-5 and never adjudicates.

**Grids:** gated τ ∈ [1, 40] step 0.5; early τ ∈ [0.05, 0.95] step
0.05 (diagnostic only).

**Trajectory inventory:** 8 members × (full + halved) = 16.

## 3. Honesty note, stated before the run (identities first)

1. **Tree transparency, F-1 (identity; makes Outcome A impossible).**
   For |γ| < 1 every tree member has K_ij·K_ji = 1 − γ² > 0 and no
   cycles. It is therefore diagonally similar to the symmetric chain
   with the same diagonal and off-diagonals −√(1 − γ²), and because
   the similarity is diagonal, **its retained-site kernel equals that
   symmetric chain's kernel exactly.** RC-3 instantiates this; a
   breach is HALT.
2. **Accretive envelope (identity).** K_s ⪰ μI with μ = λ_min(K_s)
   gives ‖e^{−Kτ}‖ ≤ e^{−μτ}, so |k(τ)| ≤ e^{−μτ} for every member.
   μ ≥ 0.3 on the ring (K_s = 0.3I + positive semidefinite terms), and
   μ = λ_min(K_b) on the tree set. RC-6 instantiates this; a breach is
   HALT. The consequence is that **finite-memory survival is
   analytic-leaning**: the envelope's decay is forced, and only the
   comparator's grade on E is not strictly forced.
3. **Metzler sign (identity).** For |γ| ≤ 1 every off-diagonal entry
   of −K is ≥ 0 (they are 1 ± γ), so e^{−Kτ} is entrywise nonnegative
   and k(τ) ≥ 0, and in fact k(τ) > 0. RC-5; a breach is HALT.
4. **Exact CM is broken by theorem; the gate reads operational
   detectability.** Exponentials with distinct exponents are linearly
   independent (Bernstein's representation is unique), so any member
   whose retained site carries weight on a complex eigenpair is **not**
   completely monotone, exactly, for any γ > 0 at which that happens.
   This fork does **not** discover that. What it measures is where the
   *operational* battery (a 39-point Gram at tolerance −10⁻¹⁰)
   registers the breach. **Analytic estimate, labeled:** in the normal
   (circulant) approximation that ignores the e₁e₁ᵀ defect, the
   retained site weights every ring mode equally (1/23), and the modes
   acquire frequencies 2γ·sin θ_k on top of the symmetric decay rates.
   At γ = 0.9 the first oscillatory pair then carries about twice the
   slowest real mode's weight, which suggests a breach far above
   tolerance at γ = 0.9 and a crossover somewhere below. The gate at
   γ = 0.9 is therefore **analytic-leaning**. The crossover location
   is the genuinely unpredicted content. Monotone decrease is mapped,
   not gated: once oscillatory weight is present, a positive kernel
   can lose monotonicity. Gating it would add an analytic-leaning
   gate without adding information, so it goes in the map.
5. **Classification of the content.** *Identity-grade:* RC-3 (tree
   transparency), RC-5 (sign), RC-6 (envelope), and every T-member
   line. *Analytic-leaning:* M-1 on ring members; H-1 at γ = 0.9.
   *Genuinely unpredicted:* the operational CM crossover γ*, the
   monotone-decrease map, and E(40) and tail structure across γ.
6. **Scope of what this fork can say.** It tests asymmetry and cycle
   affinity **with accretivity held**. It says nothing about
   accretivity versus spectral stability (O-2), for the reason in
   §3.7.
7. **F-7, a design-stage finding that defers O-2 (theorem, recorded
   here because it shaped this charter).** F-1 generalizes: if D⁻¹KD
   is **normal** for some positive diagonal D, then
   e₁ᵀf(K)e₁ = e₁ᵀf(N)e₁ with N normal. The retained-site kernel is
   then a non-negatively weighted mixture of e^{−λ_k τ} whose weights
   sum to 1, so |k(τ)| ≤ e^{−min Re λ·τ}: **no transient growth at
   the retained site, whatever K_s is.** A single one-way weighted
   cycle is such a K (it is diagonally similar to a scaled circulant).
   So the natural "stable but not accretive" construction, a directed
   ring with its spectral gap held, is **invisible from the retained
   site even at non-accretive members.** A real H-HERM-2 test needs a
   generator that is not diagonally similar to any normal matrix at
   the retained site: several cycles with incommensurate imbalances,
   and non-normal Perron weight at e₁ above 1. Building such a
   substrate is itself a formulability obligation. O-2 therefore stays
   open. It is either chartered once such a substrate is designed, or
   it ends UNFORMULABLE-WITH-REASON with F-7 recorded as the reason.

## 4. The gates (frozen, mechanical)

**Controls and identities (halt-grade; a breach anywhere is HALT):**
- **RC-1 replication:** the sealed anchor (T, γ = 0) has eigen
  k(40) = 6.8195192260507686×10⁻⁹ (|rel Δ| < 10⁻⁹), and its
  time-domain run matches the eigen form, sup |k/k_eig − 1| < 10⁻⁶.
- **RC-2** halved-schedule audit on every trajectory: sup over the
  gated grid of |rel Δ| < 10⁻⁹.
- **RC-3 tree transparency (F-1):** at γ ∈ {0.3, 0.9}, the tree
  member's time-domain kernel equals the eigen kernel of its
  symmetrized chain, sup rel < 10⁻⁶.
- **RC-4 new-substrate replication:** the ring γ = 0 time-domain
  kernel equals its eigen kernel, sup rel < 10⁻⁶.
- **RC-5 sign:** k > 0 at every recorded point of every trajectory.
- **RC-6 accretive envelope:** |k(τ)| ≤ e^{−μτ}·(1 + 10⁻⁹) at every
  recorded point of every member, with μ = λ_min(K_s) from
  `jacobi_eig`.
- **RC-7 comparator and envelope certification (R-1 instantiated):**
  on the sealed anchor, E = k exactly at every gated point, and the
  comparator applied to E reproduces the sealed R_exp =
  1.9809889100368165 and R_alg = 4.7907669413552245 (|Δ| < 10⁻¹² each)
  and the grade string "EXPONENTIAL-GRADE" exactly.

**X, the deletion is real (conditions every ring line):**
- **X-1:** sup over the gated grid of |k_{γ=0.9}/k_{γ=0} − 1| > 0.01
  on the ring. Certification-grade.

**The response properties:**
- **M-1 P_memory (analytic-leaning):** the comparator on E reads
  EXPONENTIAL-GRADE at every ring member and every tree member.
- **H-1 P_positivity (CM reading), the H-HERM-1 gate:** the ring
  γ = 0 member passes (Gram min eig ≥ −10⁻¹⁰; identity), **and** the
  ring γ = 0.9 member fails (Gram min eig < −10⁻¹⁰;
  analytic-leaning).
- **Maps (ungated):** Gram min eig vs γ (the operational crossover
  γ*); monotone-decrease status per member; E(40); tail slope; 𝒜(γ);
  μ per member; the early-grid transient map.

## 5. Outcome rule (frozen, mechanical; lines never composed)

**Scope clause, on the face of every recorded line under every
outcome:** *within the declared background mathematics (real matrices,
exact symmetric eigendecomposition for the identity controls, the
frozen RK4 schedule), the tree set on the sealed C1 bath and the
23-site pinned ring with the system-spring attachment, antisymmetric
deformations |γ| ≤ 0.9 with K_s held, the declared window, grids,
comparator, and Gram tolerance.*

- **NON-RECIPROCITY WITHOUT CYCLE AFFINITY: TRANSPARENT (F-1
  instantiated; identity-grade)** iff RC-3 holds.
- **CYCLE AFFINITY: NOT-LOAD-BEARING for P_memory** (envelope reading,
  R-1; accretivity held; analytic-leaning) iff M-1 holds and X-1
  holds.
- **CYCLE AFFINITY: LOAD-BEARING for P_positivity (CM reading)** iff
  H-1 holds and X-1 holds. The face states that exact CM is broken by
  theorem for any γ with complex spectral weight at the retained site
  (§3.4), and that the line certifies *operational detection* at
  γ = 0.9, with the crossover γ* mapped.
- **Outcome B (the affinity split) is certified** iff all three lines
  land. Recorded as: *asymmetry without cycle affinity is invisible
  to the retained-site response; cycle affinity breaks its
  complete-monotonicity structure while the memory envelope survives,
  with accretivity held.*
- **Outcome C** iff RC-clean, X-1 holds, and the ring γ = 0.9 member
  passes M-3. Recorded as: H-HERM-1 falsified at operational scope;
  exact CM still broken by theorem; the obligation's re-charter (at
  most one, per T3) would need a sharper battery.
- **L01D-VACUOUS** iff X-1 fails.
- **L01D-PARTIAL** for any other gate failure; **HALT** on any RC
  breach.
- **Precedence (run-level labels only):** HALT > VACUOUS > Outcome C
  > PARTIAL. Outcome B requires every gate to pass, so it never
  co-occurs with these. This orders labels only; it neither composes
  nor suppresses the per-property lines.

Under every outcome: no v4 channel moves; no red gate is touched; GR2
and L0-1a/b/c are untouched; the public paper is untouched. **HARD
STOP** after the verdict, pending owner ruling on the lines and the
O-1 terminal label.

## 6. Instrument contract

`calc/l01d_cycle_affinity.py`: pure stdlib. It imports `build_K` (the
tree set's K_b) and `jacobi_eig` (symmetric identity references
only) unchanged, and carries the RC-7-certified textual copy of
`fit_residuals` + TAUS. RK4 exactly as §2; deterministic, no RNG;
single run; the 16 trajectories of §2. It writes `L0_1D_RESULT.json`
(sha-hashed) with `defect_history`. Scope: the §5 clause, nothing
else.
