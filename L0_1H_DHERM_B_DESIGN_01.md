# L0-1h — D-HERM-b (O-2) DESIGN 01: accretivity vs spectral stability on the attached one-way ring

**Status: DESIGN — NOT A CHARTER.** No computation was run on any
declared member. Items marked *identity* have proofs here. Items marked
*estimate* are analytic sketches pending one focused verification.
**The owner's direction binds** (`L0_1_FLOOR_SYNTHESIS_DRAFT_01.md`
§3a): attack as hard as possible; O-2 is allowed to fail; the direction
is O-2 → O-7, never the reverse.

**O-2's frozen content (T1):** D-HERM-b, accretivity vs spectral
stability. The hypothesis under attack, as the L0-1d draft stated it:

> **H-HERM-2:** on members that hold spectral stability but drop
> accretivity, transient growth breaks P_positivity's monotone half; of
> the two passivity notions, it is **accretivity** that carries
> positivity.

## §1 The family (the named candidate; parameters to be frozen by the charter)

The **attached directed ring:** n = 23 sites, one-way transport
i → i+1 (with n → 1), and the record's attachment spring on site 1:

> K(d, g) = d·I + a·E₁₁ − g·Q, where Q_{i+1,i} = 1, Q_{1,n} = 1,
> a = 1 (the attachment), and g ≥ 0.

- **Accretive** ⟺ K_s = dI + aE₁₁ − (g/2)(Q + Qᵀ) ≻ 0. The bottom of
  the band is ≈ d − g, raised slightly by the defect.
- **Spectrally stable** ⟺ every eigenvalue has Re λ > 0.
- Both are **construction data**, not results. The charter must
  compute them exactly per member and declare the members accordingly.

## §2 Exact structure (identities)

**J-1 (secular equation and closed-form resolvent).** With w = d + s,
the retained-site transform is:
- the free-ring part: [(wI − gQ)⁻¹]₁₁ = w^{n−1}/(wⁿ − gⁿ), since Q^m
  returns to site 1 only when n | m;
- adding the rank-one defect: **G(s) = e₁ᵀ(K + s)⁻¹e₁ =
  w^{n−1}/(w^{n−1}(w + a) − gⁿ).**

The eigenvalues are λ = d − w, with w running over the roots of
**p(w) = w^{n−1}(w + a) − gⁿ**. That is an exact, closed-form degree-n
polynomial. Stability ⟺ every root satisfies Re w < d.

**J-2 (the lap expansion: the kernel is a positive sum of returns).**
Expanding G in gⁿ:

> G = Σ_{j≥0} g^{nj} / [w^{(n−1)j}(w + a)^{j+1}].

Each term inverts to e^{−dt}·hⱼ(t), with hⱼ = the convolution of the
Gamma kernel t^{(n−1)j−1}/((n−1)j−1)! with t^j e^{−at}/j!, so **hⱼ ≥ 0.**
- **k(t) = e^{−(d+a)t} + Σ_{j≥1} g^{nj} e^{−dt} hⱼ(t).**
- The j = 0 term is the pulse decaying straight out of site 1.
- The j ≥ 1 terms are the pulse returning after j laps.

**J-3 (component (a), nonnegativity: identity).** −K is Metzler
(off-diagonals g ≥ 0), so k(t) > 0. J-2 shows it term by term.

**J-4 (component (c), CM: broken for every g > 0, by theorem).**
- By Descartes' rule, p has exactly one positive root and zero or two
  negative roots (for n odd), so at most three real roots. For n = 23
  it therefore has ≥ 20 non-real roots.
- The residues are w^{n−1}/p′(w) ≠ 0, and the roots are simple except
  at isolated values of g, where p and p′ share a root at
  w = −(n−1)a/n.
- Non-real poles with nonzero residue rule out complete monotonicity
  (Bernstein uniqueness). So **CM fails for every g > 0 outside that
  isolated set, whatever d is, accretive or not.**
- This is consistent with O-1: the one-way ring has maximal cycle
  affinity, since K_ij·K_ji = 0.

**J-5 (no growth when accretive: identity).** K_s ≻ μI gives
|k(t)| ≤ e^{−μt} < 1 for t > 0.

## §3 The attackable content, estimated (pending verification)

**E-1 (component (b), monotone decrease, breaks regardless of
accretivity; estimate).**
- The j = 1 lap term rises while t < (n−1)/d, because its Gamma factor
  peaks at ≈ (n−1)/d, and the j = 0 term decays like e^{−(d+a)t}.
- For d = 1, a = 1 at t ≈ 11, the ratio of lap 1 to the direct term is
  roughly g²³·4×10⁶. So **for g ≳ 0.5 the returning pulse makes k rise:
  (b) breaks.**
- **Accretivity at d = 1 holds up to g ≈ 1.** So there is an estimated
  band g ∈ (≈ 0.5, ≈ 1) where the members are **accretive and still
  non-monotone.**
- **If this holds, H-HERM-2's "accretivity carries the monotone half"
  is false in this family.** The monotone half is carried by the
  round-trip gain gⁿ (the lap), which is a cycle-affinity/transport
  quantity, not a passivity quantity.

**E-2 (growth above k(0) = 1, the sharp non-accretive signature, looks
unreachable; estimate).**
- Stability requires d > w*, the positive root. That gives
  (g/d)ⁿ < 1 + a/g, so the per-lap gain is bounded.
- Each lap's Gamma pulse also spreads by about 1/√(2πnj).
- So **k probably never exceeds 1 anywhere in the stable, non-accretive
  band.** Growth at the retained site would then be unobservable in
  this family.
- This is the corrected F-7 situation again. It is not F-7 itself,
  since the attachment breaks normality. It would be an
  **observability limit of the retained-site kernel, not a verdict on
  accretivity** (the owner's O-2 ruling applies).

**E-3 (the width of the stable, non-accretive band is O(1/n);
estimate).**
- Stability: d > g(1 − ln(1 + a/g)/n) approximately.
- Accretivity: d > g − δ, with a defect correction δ = O(a/n).
- **The band between them is O(1/n) wide, and even its sign must be
  computed exactly.** It may be empty or tiny at n = 23. The charter
  must establish exactly whether it is non-empty before declaring any
  "stable, non-accretive" member. If it is empty, H-HERM-2's premise
  has no member in this family.

## §4 What O-2 can honestly deliver

If E-1 … E-3 survive verification, the family decides H-HERM-2 almost
entirely from structure:

| Component at the retained site | Accretive members | Stable, non-accretive members |
|---|---|---|
| (a) nonnegativity | holds (identity) | holds (identity) |
| (c) complete monotonicity | **fails** (theorem, J-4) | **fails** (theorem) |
| (b) monotone decrease | **fails for g ≳ 0.5** (E-1) | fails (E-1) |
| growth above 1 | impossible (identity, J-5) | probably unreachable (E-2) |

So: **no retained-site positivity component separates accretivity
from spectral stability in this family.** Where (b) and (c) break,
they break because of the lap, meaning transport round the cycle.

**The probable O-2 result:** H-HERM-2 **FALSIFIED at scope**, because
accretivity does not carry the monotone half. A cleanly declared
secondary statement would add that the accretive/stable distinction,
through growth, is **not observable at the retained site** in this
family.

**Recommended form (the O-4 precedent):** a theorem document (J-1 …
J-5, plus E-1 … E-3 once verified or proved) with an **exact
appendix**, since G is rational in s with integer structure. Its list,
frozen before evaluation:
- the exact accretive and stable thresholds for the declared (d, g)
  grid;
- the band's non-emptiness;
- the monotone-break threshold g_b(d);
- the maximum of k over t;
- the lap decomposition.

**Separately pre-registered, never folded into O-2's label:** an
affinity line, "the one-way ring (maximal affinity) breaks CM by J-4".
This is consistent with O-1 and adds a second cycle structure to the
generator-route evidence for O-7's clause DB, without being O-2's
verdict.

## §5 Standing

This design changes no status. It creates no property → ingredient
edge. O-2 remains open until a charter or theorem document is ruled on.
