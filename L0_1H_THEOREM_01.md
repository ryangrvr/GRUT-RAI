# L0-1h — O-2 THEOREM DOCUMENT 01 (D-HERM-b): accretivity vs spectral stability on the attached one-way ring

**Status: PROPOSED FREEZE — NOT FROZEN.** The owner adopted this form
(`L0_1H_OWNER_RULING_01.md`). Writing it up exposed a new identity,
**J-6**, which changes the appendix list the owner saw in design rev 2
§5. It also sharpens the question the owner asked the appendix to
watch. **The appendix list freezes only after the owner confirms §0.**
No computation has been run on any member (n = 23, a = 1).

## §0 For the owner, before the freeze

1. **J-6 (identity, §2).** In this family, stability, accretivity and
   retained-site monotone decrease are **three thresholds in d at fixed
   g**, so the three classes are nested (totally ordered) at every g. It
   follows that **H2-s and H2-n cannot separate independently.** At each
   g, exactly one of them holds, or both hold at a single coincidence
   point. They are decided by one comparison: d_mono(g) against
   d_acc(g).
   - The owner's hoped-for asymmetry (accretive but non-monotone members
     exist, and stable non-accretive members are all non-monotone) is
     **one** statement: d_mono(g) > d_acc(g). In words, **the monotone
     class is strictly narrower than the accretive class, which is
     strictly narrower than the stable class (P-2).**
   - Across different g, the comparison could go either way. That would
     be a split in g, reported per g.
2. **The label mapping.** Under design rev 2 §4 (FALSIFIED if H2-m falls
   or H2-s fails), **P-1 has already fixed O-2 = FALSIFIED**, and the
   appendix only records H2-s and H2-n. The owner should confirm this
   mapping, or replace it, knowing that before the freeze.
3. **Instrument asymmetry, declared up front (§4).** The appendix can
   *certify* d_mono > d_acc with an exact witness member. It **cannot
   certify** the reverse, which would need a bound valid for all t.
   A missing witness is reported as NOT CERTIFIED and is never read as
   the reverse.

## §1 The family and the clauses (from design rev 2, unchanged)

- K(d, g) = dI + aE₁₁ − gQ, with n = 23 and a = 1. The retained
  kernel is k(t) = [e^{−Kt}]₁₁.
- (b) "monotone decrease" means k is non-increasing on t > 0.
- The clauses H2-m, H2-s and H2-n are as recorded in
  `L0_1H_OWNER_RULING_01.md`.

## §2 Theorems

- **J-1 … J-5, P-1, P-2:** as stated and proved in
  `L0_1H_DHERM_B_DESIGN_01.md` rev 2, §§2–3. They are incorporated
  here without change.

**J-6 (the monotone criterion is independent of d; the classes are
nested).**
- Write −K = −(d + a)I + P, where **P = gQ + a(I − E₁₁) ≥ 0**
  entrywise. P does not depend on d. Then:
  - k(t) = e^{−(d+a)t}y₁(t), with y(t) = e^{Pt}e₁ ≥ 0;
  - (Py)₁ = g·yₙ, because P₁₁ = 0 and P₁ₙ = g.
- Hence k′(t) = e^{−(d+a)t}[g·yₙ(t) − (d + a)y₁(t)], and

> **k′(t) > 0 ⟺ g·yₙ(t)/y₁(t) > d + a.**

- Define R(g) = sup_{t>0} g·yₙ(t)/y₁(t) and d_mono(g) = R(g) − a.
  Then (b) holds ⟺ d ≥ d_mono(g).
- With w\*(g) and d_acc(g) from J-1 and P-2, at fixed (g, a):
  - stable ⟺ d > w\*;
  - accretive ⟺ d ≥ d_acc;
  - monotone ⟺ d ≥ d_mono.

  All three classes are upper sets in d, so they are totally ordered by
  inclusion.
- **Asymptote.** P is irreducible and aperiodic (a > 0 on its
  diagonal), with Perron vector v_i = (g/w\*)^{i−1} and eigenvalue
  w\* + a. So g·yₙ/y₁ → g·(g/w\*)^{n−1} = w\* + a, using p(w\*) = 0.
  Hence **d_mono ≥ w\*.** Monotone members are never less stable than
  stable ones.
- **Clause decision at each g:**
  - d_mono < d_acc: H2-s holds and H2-n fails;
  - d_mono > d_acc: H2-s fails and H2-n holds, across the whole band
    (w\*, d_acc), not just at grid points;
  - d_mono = d_acc: both hold.
- Toy check: non-member toys confirm the criterion to a relative error
  of about 1e-10 (`calc/feasibility/l01h_j6_check_nonmember.py`).

## §3 Standing, independent of the appendix

- **H2-m: excluded for every member, by P-1.** Retained-site growth is
  impossible on every stable member. State-norm growth exists but no
  diagonal kernel can see it.
- **CM fails for every g > 0 (J-4).** This is recorded under the
  separately pre-registered affinity line, not under O-2's label.

## §4 Exact appendix (PROPOSED list; freezes on owner confirmation)

**Declared g-grid:** g ∈ {1/20, 1/10, 1/4, 1/2, 1, 2, 4, 10}, with
n = 23 and a = 1. All arithmetic is in `fractions` unless marked
float.

- **A-1: w\*(g).** A rational bracket of width ≤ 10⁻¹², by exact sign
  evaluation of p at rational points. There is exactly one positive
  root (Descartes).
- **A-2: d_acc(g).** A rational bracket [ℓ, u] of width ≤ 10⁻¹²:
  - K_s(u) ≻ 0, shown by all exact Sylvester (LDLᵀ) pivots being
    positive;
  - K_s(ℓ) ⊁ 0, shown by some pivot ≤ 0.

  Also report the exact band [A-1 upper, A-2 lower], whose
  non-emptiness is a consistency check of P-2.
- **A-3: the witness for d_mono > d_acc.**
  1. **Float search (non-gating):** scan t ∈ {j/8 : 1 ≤ j ≤ 1600} for
     the maximiser t\* of g·yₙ/y₁.
  2. **Exact certification at rational t\*:**
     - L = the exact Taylor partial sum of e^{Pt\*}e₁ (every term is
       ≥ 0, so L is a lower bound);
     - U₁ = L₁ + a tail bound. Since ‖Pᵐe₁‖_∞ ≤ (g + a)ᵐ, the tail is
       at most x^{M+1}/(M+1)! · (1 − x/(M+2))⁻¹, where x = (g + a)t\*
       and M + 2 > x.
  3. **Certified SEPARATED at g** if g·Lₙ > (u + a)·U₁. Then
     d_mono(g) > u ≥ d_acc(g), and **K(u, g) is an explicit, strictly
     accretive, non-monotone member.**
- **A-4: no witness found.** Report **NOT CERTIFIED** at that g, together
  with the float estimate of d_mono(g) against d_acc(g). The estimate
  is **never promoted**, and a missing witness is **never read as
  d_mono < d_acc.**
- **A-5: P-1 cross-check (not a gate).** Report the float value of
  max_t k(t) at the witness member against e^{−(u−w\*)t}.

**Reporting.** A per-g table: w\* bracket, d_acc bracket, witness
(t\*, u, certified margin) or NOT CERTIFIED, and the clause reading
under J-6. **No aggregate across g** beyond listing the result at each
g. The O-2 label follows the owner's mapping (§0.2), not the appendix.

## §5 Standing

O-2 remains **open.** This document creates no property → ingredient
edge. After the owner confirms §0: freeze the list (commit), build the
instrument and test it on non-members only, run it once on the members,
write the result, post it, and stop.
