# H¹ CLOSURE — PHASE 3: a² → a³ VERTEX-WEIGHT DEFORMATION CONTROL

**Date:** 2026-09-03 · **Instrument:** `wall_kr_h1_phase3_a3_control.py` ·
**Artifact:** `WALL_KR_H1_PHASE3_RESULT.json` · **Base:** 39551c7 (Phase 2, CLOSED).
**Battery: 42/42 testable gates, zero failures (737 s; first run, no stalls; every
zero/nonzero decision EXACT-symbolic — no numeric witness needed anywhere this phase).**
**VERDICT: `PHASE3-BREAKS`** — a CONTROL classification only; no
uniqueness claim, no theorem, no Phase 4. Read-only on frozen artifacts; register sha256
identical pre/post; A–F unselected; nothing banked. W-0.

## A · GOVERNANCE STATE

HEAD == origin/v4 by ref identity; worktree clean at start; register sha `beaeb84e…`
unchanged; frozen set byte-identical; bedc989 (Phase 1) and 39551c7 (Phase 2) in ancestry
by returncode; Phase-1/Phase-2 artifacts git-clean — **Phase 2 not reopened**; A–F
unselected; W-0.

## B · EXACT DEFORMATION DEFINITION (the definition was itself a gate — it PASSED)

The order required stopping if the frozen construction admits no unambiguous a²→a³
deformation. It admits exactly one **within the declared multiplicative-weight frame**
(per Leg B; §K already concedes a full a³ vertex differs in more), anchored to the frozen
artifact:

- **RE-GATED from the 26,032-term frozen vertex:** the literal O(H) grading is
  **V₃⁽¹⁾ = 2u·V₃⁽⁰⁾ + R** with R u-FREE — the multiplicative conformal weight is exactly
  2u per vertex, and the coefficient **2 is the a-power** (a² per vertex, a(u) = 1/(1−Hu)).
  **Uniqueness:** the in-run gate tests the c=3 alternative (V₃⁽¹⁾ − 3u·V₃⁽⁰⁾ is *not*
  u-free); the general statement — V₃⁽¹⁾ − c·u·V₃⁽⁰⁾ u-free iff c=2, for ALL real c — is a
  corollary of R u-free + V₃⁽⁰⁾ u-free and nonzero (per Leg A, which also verified the
  grading DESCENDS to the contracted C-matrix level the assembly actually consumes:
  C¹ = 2u·C⁰ + R_contr, u-free, 28/28 entries, all three configs). R = (Σp₀)·S is
  Protection 1's separate structure, untouched.
- **The balance the deformation detunes (gated):** the two-line conformal product carries
  −2(u+u′) at O(H) (one 1/a per mode endpoint, four endpoints); the two vertices' a²
  weight carries +2u+2u′ = +2(u+u′). The multiplicative balance cancels EXACTLY — and the
  Route-B "+2(u+u′) compensator" **is** the two-vertex a² weight (equivalently
  −B_pureconf). Changing the vertex weight therefore mathematically **requires** changing
  this term — the order's carved-out case for the compensator.
- **THE DEFORMATION:** per-vertex conformal weight coefficient **2 → 2+β**; in the pair
  assembly the vertex-weight term becomes **(2+β)(u+u′)·flatA·flatB**. β real, symbolic;
  **β₀ = 1 REGISTERED — the a³ point**; reversible at β=0. Unchanged: flat C⁰ vertex, R,
  line/state kernels, routing, TT projector, derivative algebra. No new physical
  parameter — β interpolates the integer power of the scale factor.

## C · NATIVE-LIMIT RECONSTRUCTION

Independent, Route-B style: V_k from the frozen flat C⁰ vertex; line residuals from the
mode-derived dressing; vertex weight as above. **Not read as inputs:** B_mixed, the Phase-1
swap relation, the Phase-2 M₁ result. **M(β=0) ≡ 0 pointwise pre-angular, exact-symbolic,
all three TT configurations** — VERIFIED (plus_z 126 s, cross_z 367 s, plus_x 528 s
cumulative marks).

## D · DEFORMED RESULT

$$ M(\beta) \;=\; \beta\,(u+u')\,\Sigma_0, \qquad
\Sigma_0 = \sum_k V_k\,\mathrm{pref}\,\mathrm{flat}_A\,\mathrm{flat}_B \;\neq\; 0
\ \text{(EXACT-symbolic, not numeric)} $$

**M₁^(a³) = (u+u′)·Σ₀ ≠ 0 on ALL THREE configurations** — the a²→a³ deformation BREAKS
the cancellation pointwise pre-angular, and (gated via the exact registered moment()
machinery) **⟨Σ₀⟩ ≠ 0 — the breaking survives the exact angular average** on all three.

Linearity and the closed form are gated at a representative key per config and are exact
for all keys by the affine construction (Leg A independently closed the full 3⁴ = 81
derivative-order grid, and derived the forcing analytically: **M(c) = (c−2)(u+u′)Σ₀** —
with Σ₀ ≠ 0 the native coefficient is pinned to 2 uniquely per config); the explicit
registered points
β = ±1 (the a³ point and its mirror) are nonzero, exact. The breaking term's shape,
(u+u′)·Σ₀, is the same fingerprint class as the (disclosed) double-compensation bug — that
bug was, in effect, an accidental vertex-weight deformation, which is exactly why the
campaign's controls catch this class.

## E · LOCALIZATION (the three-way separation, per §6)

| component | fate under β | evidence |
|---|---|---|
| **F1 routing/transposition** (vertex array) | **UNTOUCHED** | β never enters V_k (GATED) |
| **F3 derivative ladder weight** (demotion) | **UNTOUCHED** | the per-sector identity Σ V_k(g+h−e−f)(−1)^{e+f} = 0 holds and is β-free (GATED) |
| **F2 conformal vertex weight** | **DEFORMED** | the added term is exactly β(u+u′)·flat — a pure NON-demotion term; the deformation aggregate D_{j,m} is NOT transposition-antisymmetric (gated observable, all three configs) |
| **F4 state** | **FROZEN** | line/state kernels byte-identical to native |

**The breaking is the detuned multiplicative balance**: native, vertex(+2(u+u′)) cancels
lines(−2(u+u′)) exactly; at β≠0 the residual β(u+u′)·Σ₀ has nothing to cancel against.
**Split-convention independence (adopted from Leg B, verified symbolically):** under ANY
relabeling of the vertex/line split of the O(H) conformal content, the label-invariant
TOTAL multiplicative O(H) content is 0 natively and β(u+u′) under the deformation — the
breaking conclusion survives however the split is worded; only the attribution word
"vertex" is representation-dependent, and the record's scoping ("the declared conformal
vertex-weight structure") carries exactly that caveat.
The complement of Phase 2 is now explicit: Phase 2 broke the cancellation with **routing
intact + vertex weight intact + state deformed**; Phase 3 breaks it with **routing intact +
state intact + vertex weight deformed**. Two independent load-bearing legs, each isolated
by one control; the ladder identity (F3) is a third leg, untouched by both and probed by
each phase's negative control.

## F · THREE-CONFIGURATION TABLE

| config | M(0) | M(β) = β(u+u′)Σ₀ | relevant symmetry | verdict |
|---|---|---|---|---|
| plus_z | ≡ 0 exact | ≠ 0 (Σ₀ ≠ 0 exact; post-angular ≠ 0) | routing untouched; ladder identity holds β-free; D_{j,m} not antisymmetric | BREAKS |
| cross_z | ≡ 0 exact | ≠ 0 (Σ₀ ≠ 0 exact; post-angular ≠ 0) | routing untouched; ladder identity holds β-free; D_{j,m} not antisymmetric | BREAKS |
| plus_x | ≡ 0 exact | ≠ 0 (Σ₀ ≠ 0 exact; post-angular ≠ 0) | routing untouched; ladder identity holds β-free; D_{j,m} not antisymmetric | BREAKS |

## G · NEGATIVE CONTROL (deliberately non-tautological)

Perturbing ONE flat vertex coefficient V_k by +1 (the Route-B Control-A pattern) breaks
the **per-sector ladder identity** — exact-symbolic nonzero — and the full-M assembly
detects it (M₀ + m_key(k*) ≠ 0, exact). This targets the DEMOTION mechanism (F3), which
the a³ deformation provably does **not** touch — so the detectability control acts on a
different mechanism component than the deformation under test, as required. Both gates
passed exact-symbolically (sector N=1 nonzero under the perturbation; the full assembly
M₀ + m_key(k*) nonzero pointwise).

## H · ADVERSARIAL LEG A — CONSTRUCTION: `CONFIRMED` (workflow wn7qtjp7y)

Independently reproduced the load-bearing result through **two** routes: (1) a separately
written assembly deciding M(β=0) ≡ 0 and Σ₀ ≠ 0 exactly with the leg's own zero procedure;
(2) an assembly-free analytic route — the per-key closed form verified on the full 81-key
grid plus the per-sector ladder sums (all sectors, all three configs), which imply M₀ ≡ 0
by pure algebra. **The compensator-is-vertex-weight identification is FORCED, not merely
plausible:** anchored to 2B.1's object-level gate (A_weight == +2(u+u′)Σ₀ == −B_pureconf
via the frozen assemble(), with A_R == 0 separately), to an O(H) source enumeration
leaving no other +2(u+u′)·flat source, and to the analytic forcing M(c) = (c−2)(u+u′)Σ₀.
The leg **would not have stopped** at the definition gate. Five disclosure-level findings,
all adopted here: (1) the in-run "VERTEX SIDE GATED" line is an arithmetic tautology *as
coded* — its label overstates that single gate; the identification is carried by the
grading + native-limit + Σ₀≠0 combination, 2B.1, and the analytic forcing; (2) the
linearity gate is representative-key (closed on all 81 by the leg); (3) gate 6A is
true-by-construction — documentation, not evidence; (4) 2B.1's A_weight tag was
plus_z-only — the leg supplied the per-config closure via the contracted-level grading
(28/28 entries, all configs); (5) Stage 2A's line-kernel check was string-containment —
the leg re-verified the O(H) coefficient symbolically. The leg also disclosed and fixed
two bugs in its OWN scratch tooling before its accepted runs (not in the ledger).

## I · ADVERSARIAL LEG B — INTERPRETATION: `CONFIRMED` (workflow wn7qtjp7y)

No over-generalization at the load-bearing level: §K's disclaimers verbatim, the issued
conclusion exactly the permitted maximum, no theorem/GRUT language outside disclaimers.
Routing used only as an observable. **The sharpest attack — "changing the compensator is
really a line-side change in disguise" — FAILS on three verified grounds:** the pair-level
term equals the uniform per-vertex deformation exactly; the split is fixed by the DECLARED
frozen rules (the vertex artifact's literal grading puts +2u per vertex in the vertex rule;
the frozen WPLUS literal puts (1−Hu)(1−Hu′) on each line); and the label-invariant total
multiplicative O(H) content moves 0 → β(u+u′) under ANY relabeling. Not a representation
artifact: absorbing β(u+u′)Σ₀ would require deforming the frozen line/state kernels or the
derivative algebra — a compensating second deformation, not a relabel. Angular claim exact
and correctly scoped; negative control genuinely non-tautological. Seven wording
corrections, **all adopted** (within-frame qualifier; uniqueness-as-corollary; representative-key
phrasing; "one-parameter" not "minimal"; the split-invariance sentence; the frozen-lines/state
condition on "LOAD-BEARING"; the d=3 post-angular gate — run as the gated addendum
`wall_kr_h1_phase3_d3_note.py`, artifact `WALL_KR_H1_PHASE3_D3_NOTE.json`).

## J · EXACT SCOPE

Frozen flat EH cubic vertex under the declared TT contraction and routing; the three
frozen TT configurations (non-TT `ward` untested, not silently added); O(H); pre-angular
with the post-angular fate gated via the exact registered moment() machinery; **THIS
deformation only** — the multiplicative conformal weight coefficient 2 → 2+β. Status
verbs: definition anchor GATED; native limit VERIFIED; closed form GATED; Σ₀ ≠ 0 GATED
(exact-symbolic, no numeric witness anywhere in a zero-or-nonzero-critical gate this
phase); ladder identity GATED; post-angular GATED. This is a CONTROL.

## K · LIMITATIONS

- A full a³-weighted EH-like vertex would differ in **more** than the multiplicative
  weight (its R-analogue and O(H²) structure would change); this control deforms ONLY the
  multiplicative conformal weight — the piece the frozen grading isolates in closed form.
- **NOT established:** "a² is uniquely required"; "GRUT requires a²"; "the H¹ cancellation
  is impossible without a²". Those need an admissible-deformation space and a uniqueness
  argument this control does not have.
- The strongest permitted conclusion, and the one issued: *this specific a²→a³
  vertex-weight deformation breaks the native H¹ cancellation under the declared frozen
  construction; the native cancellation is sensitive to the declared conformal
  vertex-weight structure.*

## L · GOVERNANCE EXIT

Register sha pre == post; frozen set unchanged; Phase-1/2 artifacts unchanged; A–F
UNSELECTED; W-0 intact; nothing banked; HEAD == origin/v4; **Phase 4 NOT started.**

## VERDICT: `PHASE3-BREAKS`

**For Phase 6's truth table:** the native a² conformal vertex weight is **LOAD-BEARING
under frozen lines/state** (this one-parameter deformation breaks the cancellation, pre-
and post-angular, including at d=3) — alongside Phase 2's state leg and the untouched
ladder identity. Scoped per §13: sensitivity shown for THIS deformation; uniqueness of a²
NOT claimed.

## W-0 STATUS — control computed and reported; no frozen input modified; A–F unchanged; nothing banked.
