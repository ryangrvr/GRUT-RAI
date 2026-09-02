# D4 K-TERM COMPLETION — INTERNAL-LINE / SLICING SECTOR

**Date:** 2026-09-02 · **Instrument:** `wall_kr_d4_kterm.py` ·
**Artifact:** `WALL_KR_D4_KTERM_COMPLETION_RESULT.json` ·
**Battery: 27/27, zero failures, five controls detecting.** ·
**Frozen inputs byte-identical (the D4-C artifact included); register
untouched; no new physical input; no floating point anywhere.**
**W-0: unbanked. HARD STOP.**

## CLASSIFICATION: **KTERM-A**

**The internal-line requirement PASSES.** The registered K-term
mechanism — transversality + trace cancellation — applied to the
**internal** slot annihilates the full internal orbit direction
exactly: for arbitrary direction, arbitrary gauge parameter, and
**uniformly in H**.

**D4 remains C, pending owner re-adjudication.** No governance rule
defines this execution as the formal D4 completion, so the
classification is not changed here.

## 1. WHAT THE REGISTERED K-TERM ACTUALLY IS (read from source)

From `wall_a4_response_dressed.py`, verbatim: the orbit splits as
**de⁰ = i(KX + XK)** (the *K-terms*) plus **eta-direction** trace
pieces, and the theorem is that *"K-terms cannot reach the transverse
block"* and *"eta-terms shift e11 and e22 equally and cancel in the
traceless combination."* **The "K-term completion" IS transversality +
trace-cancellation executed on the orbit direction** — not a separate
object.

**Governance finding (reported per the stop-clause):** the registered
protocol contains **no separate internal-line machinery**. At matter
scope A4's internal lines were **scalars** and carried no orbit at all,
so none was ever written. The priced completion is therefore the *same
mechanism applied to the internal slot* — a re-derivation, not a new
object. **The declared cost/input obstruction is unchanged**, so the
run proceeded.

## 2. FLAT CONTROL (first, as required)

Re-verified from its frozen record: the flat vertex with a gauge-image
leg under exact conservation and on-shell TT companions is
**identically zero**. The apparatus detects genuine gauge invariance;
proceeding was licensed.

## 3. ROUTE A — REGISTERED MECHANISM ON THE INTERNAL SLOT

With |n| = 1 imposed **by construction** (exact trigonometric
parameterization, not by substitution):

| half | result |
|---|---|
| **K-terms** i(q n_i Y_j + q n_j Y_i) | **annihilated** at every (a,b), arbitrary direction, arbitrary Y |
| **eta/trace** λ δ_ij | **annihilated** for arbitrary λ |
| **full orbit direction** | **annihilated exactly** |

*(Projector sanity passes on this parameterization — a first attempt
that read "nonzero" was a failed `n3**2` substitution, disclosed.)*

## 4. H-ORDER SEPARATION — STRONGER THAN ORDER-BY-ORDER

λ = 2(a′/a)ξ⁰ is the **only** carrier of H in the internal orbit
direction, and the annihilation is **independent of λ**
(∂/∂λ ≡ 0). So H⁰, H¹ and H² are each annihilated separately and **no
order can hide a residual behind another** — the result is *uniform in
H*, not merely checked at three orders.

## 5. ROUTE B — GENUINELY INDEPENDENT

Route B shares no intermediate with Route A: it builds an **explicit
transverse orthonormal dyad** and reads the **A4 TT amplitudes**
directly — ((e₊·δe·e₊) − (e×·δe·e×))/2 and e₊·δe·e× — at **four exact
rational unit directions**. Both amplitudes vanish at every direction.
Route A contracts with the symbolic projector; Route B never touches a
projector. They share only the frozen orbit-direction *definition*
(raw input, permitted).

## 6. WHAT THE D4-C RESIDUAL ACTUALLY WAS — HONEST DIAGNOSIS

The D4-C Part-2 test inserted the gauge image as a **free polarization**
on the vertex's internal slot. **The loop does not do that:** the
internal slot is contracted with the bath propagator **P^TT × W** (T3's
frozen tensor rule, internal time rows zeroed by the T2 declaration).
The D4-C test **bypassed the projector that defines the declared bath**.

Under the required decomposition, the residual is **category B — exact
zero after TT projection.** Not "pure gauge by inspection," not an EOM
cancellation, not a new K-term: the projection *is* the registered
mechanism.

**This corrects the builder's own D4-C interpretation, not the frozen
record** — the D4-C artifact stays byte-identical and its
classification is preserved.

## 7. SCOPE BOUNDARY — NAMED, NOT HIDDEN

This establishes **orbit robustness within the declared TT bath**:
gauge-transforming the internal line moves no TT amplitude. It does
**not** establish that the TT-bath *declaration* is the unique
admissible gauge choice. A general-gauge propagator whose non-TT
content differs is a **D3(iii)** question — the graviton-bath
state/gauge prescription the charter lists as **owner-declared and
underdefined** — not a D4 one, and it is **not answered here**.

## 8. CONTROLS — five, with the weak one flagged as weak

**A.** omit transversality → the K-direction **survives**;
**C.** a generic non-orbit symmetric insertion **survives**;
**D.** break unit-norm (|n|² = 3/4) → the annihilation **fails**;
**E.** omit the trace subtraction → the eta/trace direction
**survives**. Together A and E prove **both halves** of the registered
mechanism load-bearing.
**B.** the sign-flip/antisymmetrized control is **weak by
construction** (an antisymmetric tensor dies against a symmetric
projector regardless) — recorded and flagged as such rather than
counted as teeth.

## 9. NUMERICAL VALIDATION

Six random **exact** unit directions × nine index pairs, all
annihilated **exactly** in rational/radical arithmetic. **No floating
point anywhere in this instrument** — nothing rounds to zero.

## IMPLICATION FOR D4

If the owner accepts this result, D4 becomes eligible for
re-adjudication with both sectors resolved: the **external** orbit by
the operator identity (a54aa7f) and the **internal** orbit by this
completion — with the D3(iii) bath-declaration boundary explicitly
outside both. **Until that owner act, D4 stands at C.**
