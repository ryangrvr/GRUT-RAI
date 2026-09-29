# L0-1h — D-HERM-b (O-2) DESIGN 01, rev 2: accretivity vs spectral stability on the attached one-way ring

**Status: DESIGN — NOT A CHARTER.** No computation was run on any
declared member (n = 23, a = 1). Items marked *identity* or *theorem*
have proofs here. Items marked *estimate* rest on non-member toys only.
**The owner's direction binds** (`L0_1_FLOOR_SYNTHESIS_DRAFT_01.md`
§3a): attack as hard as possible; O-2 is allowed to fail; the direction
is O-2 → O-7, never the reverse.

**Rev 2 (after one independent verification pass):** J-1 … J-5 were
confirmed, and J-4's exceptional set was removed. E-2 and E-3 were
promoted to theorems (P-1, P-2). E-1's conclusion was confirmed, but
its criterion was wrong and has been replaced. §4's overclaim was
withdrawn. H-HERM-2 has been split into clauses **before** any member
is evaluated (§4). The toys are archived as
`calc/feasibility/l01h_verifier_toy{1..5}_nonmember.py`; each skips
n = 23, a = 1. **Disclosure:** one toy ran n = 25, a = 1, a close
neighbour of the family.

**O-2's frozen content (T1):** D-HERM-b, accretivity vs spectral
stability. The hypothesis, as the L0-1d draft stated it:

> **H-HERM-2:** on members that hold spectral stability but drop
> accretivity, transient growth breaks P_positivity's monotone half; of
> the two passivity notions, it is **accretivity** that carries
> positivity.

## §1 The family (the named candidate; the charter freezes its parameters)

The **attached directed ring:** n = 23 sites, one-way transport
i → i+1 (with n → 1), and the record's attachment spring on site 1:

> K(d, g) = d·I + a·E₁₁ − g·Q, where Q_{i+1,i} = 1, Q_{1,n} = 1,
> a = 1, and g > 0.

- **Accretive** ⟺ K_s = (K + Kᵀ)/2 ⪰ 0 (strictly: ≻ 0). The threshold
  is d > d_acc(g) = g − δ.
- **Spectrally stable** ⟺ every eigenvalue has Re λ > 0.

## §2 Exact structure (identities; all confirmed)

**J-1 (secular equation, closed-form resolvent).** With w = d + s:
- **G(s) = e₁ᵀ(K + s)⁻¹e₁ = w^{n−1}/p(w)**, where
  **p(w) = w^{n−1}(w + a) − gⁿ = det(wI − gQ + aE₁₁)**.
- For g > 0, e₁ is cyclic for both K and Kᵀ: the Krylov vectors are
  triangular with leading coefficient (−g)ᵐ. Also p(0) = −gⁿ ≠ 0, so
  G has no cancellation. **The poles of G are the whole spectrum,** and
  the retained site sees every mode.
- At g = 0, e₁ is not cyclic: the eigenvalue d, of multiplicity n − 1,
  is hidden from G.
- **The positive root w\* has the largest real part.** Suppose w is not
  real and Re w ≥ w\*. Then |w|^{n−1}|w + a| > w\*^{n−1}(w\* + a) = gⁿ,
  which contradicts p(w) = 0. So **stability ⟺ d > w\*
  ⟺ (g/d)ⁿ < 1 + a/d.** (Rev 1 had "1 + a/g", a typo.)

**J-2 (the lap expansion).** Expanding G in gⁿ:
- G = Σ_{j≥0} g^{nj}/[w^{(n−1)j}(w + a)^{j+1}].
- **k(t) = e^{−(d+a)t} + Σ_{j≥1} g^{nj}e^{−dt}hⱼ(t)**, where hⱼ is the
  convolution of t^{(n−1)j−1}/((n−1)j−1)! with tʲe^{−at}/j!.
- Each hⱼ satisfies 0 ≤ hⱼ ≤ t^{nj}/(nj)!, so the series converges for
  every t, uniformly on compacts. Term-by-term inversion is valid.

**J-3 ((a), nonnegativity).** −K is Metzler, so k(t) > 0.

**J-4 ((c), CM: broken for every g > 0, with no exceptions).**
- By Descartes' rule (n odd), p has at most three real roots. So for
  n = 23 it has at least 20 non-real roots.
- A double root occurs only at the real point w₀ = −(n−1)a/n, for a
  single value of g. **Non-real roots are therefore always simple.**
- Their residues, w/(nw + (n−1)a), are never zero.
- A CM kernel has a transform ∫dμ(x)/(s + x), which is holomorphic off
  the real axis. G is rational with a non-real pole of nonzero residue,
  so it cannot be such a transform. **CM fails for every g > 0 (n ≥ 4),
  accretive or not.** (Rev 1's "isolated exceptional set" was
  unnecessary.)

**J-5 (accretive ⇒ decay).** If K_s ⪰ μI, then |k(t)| ≤ e^{−μt}. This
is superseded by P-1.

## §3 Promoted and corrected

**P-1 (theorem, was E-2: no retained-site growth for ANY stable member).**
- −K is Metzler and irreducible. Its Perron vector is
  v_i = (g/w\*)^{i−1} > 0, with Kv = (d − w\*)v. Row 1 uses
  p(w\*) = 0, i.e. g(g/w\*)^{n−1} = w\* + a.
- e^{−Kt} is entrywise nonnegative, so
  k(t) = (e^{−Kt})₁₁v₁ ≤ (e^{−Kt}v)₁ = e^{−(d−w\*)t}.
- Hence **k(t) ≤ e^{−(d−w\*)t} < 1 for all t > 0 on every stable
  member, accretive or not.** The same holds for every diagonal entry.
- When K_s is not ⪰ 0, the **state norm** ‖e^{−Kt}‖ does grow at
  t = 0⁺. That growth is real, but no diagonal kernel can see it.
- **This settles the "observability limit" framing exactly.** Transient
  growth exists in the state, but it is provably invisible at the
  retained site. That is a property of the observable, not a verdict
  on accretivity (per the owner's O-2 ruling).
- Toy check: no violations of the bound across 360 band members.

**P-2 (theorem, was E-3: the stable, non-accretive band is non-empty,
n ≥ 3, a > 0).**
- At d = w\*, Kv = 0, so vᵀK_s v = 0 and λ_min(K_s) ≤ 0.
- Suppose equality held. Then v would minimise the form, so K_s v = 0
  and hence Kᵀv = 0.
- Rows 2 … n−1 of Kᵀv = 0 force g = w\*, which makes v uniform. But
  then row 1 of Kv reads a = 0, a contradiction.
- So d_acc > w\* strictly, and **the band (w\*, d_acc) is non-empty.**
  It is empty only if a = 0 (or n = 2).
- The sign question is settled. Only the band's width at n = 23 is left
  to compute.
- **Corrected width scaling (estimate, toy-confirmed).** The defect
  δ = g − d_acc lies in (0, a/n).
  - Regime na ≫ g: δ ≈ (π²g/2n²)(1 − 4g/(an)), and the width is
    ≈ g·ln(1 + a/g)/n − π²g/(2n²). This is O(1/n), with an O(1/n²)
    correction. (Rev 1 wrongly gave δ = O(a/n).)
  - Regime na ≪ g: the width is ≈ a²(n−1)(n−2)/(6gn²).

**E-1 (estimate, corrected): (b) breaks inside the accretive region.**
- **Rev 1's criterion was wrong.** The ratio of lap 1 to the direct
  term, gⁿe^{at}h₁(t), increases to ∞ for every g > 0, so it sets no
  threshold.
- **The correct criterion:** (b) breaks when lap 1 overtakes the direct
  term while lap 1 is still rising, i.e. before t ≈ (n − 2)/d.
- **Large-n asymptote:** g_b/d → e^{−(1 + a/d)}, with a correction of
  order (ln n)/n that pushes it upward. A stronger attachment makes (b)
  break *more easily*. The threshold compares the direct escape rate
  d + a with the lap transit time.
- **Non-member toys (d = 1, a = 1):** g_b ≈ 0.72, 0.50, 0.34, 0.30 and
  0.21 at n = 5, 7, 11, 13 and 25. **In every toy, g_b < g_acc**
  (including n = 3). So accretive, non-monotone members exist. Rev 1's
  "g ≳ 0.5" was too high.
- **Toy observation, not a theorem:** in every toy, every stable,
  non-accretive member was also non-monotone. So (b) separated in one
  direction only: every monotone member was accretive.

## §4 H-HERM-2, split into clauses (written before any member is evaluated)

**Disclosure:** this split was written *after* the non-member toys. It
follows the hypothesis's own grammar, and it adds no success condition.

| Clause | Content | Standing before the charter |
|---|---|---|
| **H2-m (mechanism)** | On stable, non-accretive members, *transient growth* at the retained site is what breaks (b). | **Excluded by theorem P-1** for every member of the family. No computation needed. |
| **H2-s (sufficiency: "carries")** | Accretive ⇒ (b) holds at the retained site. | Estimated to FAIL (E-1). Decided by exact computation of g_b(d) against d_acc on the declared grid. |
| **H2-n (necessity)** | Stable and non-accretive ⇒ (b) fails. | Toy-consistent. Decided by exact computation on the declared grid, over the non-empty band (P-2). |

**The mapping from clauses to O-2's single terminal label is the
owner's to fix before evaluation.** The operator recommends the
following, so that the hypothesis is not rescued by its surviving part:
- The hypothesis asserts H2-m **and** "carries". If H2-m falls by
  theorem (it has) or H2-s fails at member scope, then **O-2 =
  FALSIFIED**, with its scope named clause by clause.
- H2-n is recorded as a separate result at its own grade. It never
  upgrades the label.
- If H2-n also held, the accurate reading would be: "accretivity is
  necessary for the monotone half at the retained site, not sufficient;
  what breaks (b) is the lap (transport round the cycle), not growth."

**What rev 1 overclaimed, now withdrawn.** Rev 1 said "no
retained-site component separates accretivity from stability." That
may be false in one direction (H2-n). Whether it is decides at member
scope, and the result is not to be anticipated here.

## §5 Recommended form (the O-4 precedent)

**A theorem document** (J-1 … J-5, P-1, P-2) **plus an exact
appendix.** G is rational in s, and p has integer coefficients once d
and g are rational. The appendix list is frozen before evaluation:
1. Exact d_acc(g) (the sign of λ_min(K_s) through exact Sylvester
   pivots) and exact w\*(g) (Sturm isolation of p's positive root) on a
   declared rational (d, g) grid.
2. The band's width at n = 23 (its non-emptiness is already P-2).
3. g_b(d), bracketed rigorously: k′(t) > 0 somewhere, with a certified
   bracket from interval evaluation of the lap series and its truncation
   bound (J-2).
4. H2-s and H2-n decided on every grid point.
5. max_t k(t), reported only as a check on P-1, never as a gate.

**Separately pre-registered, never folded into O-2's label:** the
affinity line. The one-way ring has maximal cycle affinity
(K_ij·K_ji = 0) and breaks CM for every g > 0 (J-4). This is
consistent with O-1, and it is evidence for O-7's clause DB (the
generator route).

## §6 Standing

This design changes no status and creates no property → ingredient
edge. **P-1 is a theorem about every member**, so H2-m is already
decided without any member computation. O-2 remains **open** until a
charter or theorem document is ruled on.
