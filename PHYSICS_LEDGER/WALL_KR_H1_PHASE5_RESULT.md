# H¹ CLOSURE — PHASE 5: CONDITION-FORCING / PROVENANCE AUDIT

**Date:** 2026-09-03 · **Instrument:** `wall_kr_h1_phase5_provenance.py` ·
**Artifact:** `WALL_KR_H1_PHASE5_RESULT.json` · **Base:** e5009bc (Phases 1–4 CLOSED).
**Battery: 19/19 testable gates, zero failures (80 s; second run — the first run's three
S-Wronskian gates FAILED LOUDLY on a wrong normalization condition, disclosed and
corrected below).** **CLASSIFICATION: `PARTIALLY-FORCED`.**
Read-only; register sha256 identical pre/post; A–F unselected; nothing banked; Phase 6 NOT
started. W-0.

## THE QUESTION (§1) AND THE ANSWER IN ONE VIEW

Which of the three native H¹=0 conditions are DERIVED, which are INPUTS/DECLARATIONS, and
which remain UNFORCED?

| condition | forced by | classification |
|---|---|---|
| **S** (state slot = 0), amplitude direction | canonical normalization in the FRW background: a²(u)·W[h,h*] = const (GATED; x≠0 shifts it at O(H)) | **STANDARD IDENTITY** |
| **S**, mixing direction | no standard identity **among the declared in-repo inputs** — the Bogoliubov direction PRESERVES the canonical Wronskian at O(H) (GATED; its cross-Wronskians vanish identically since h̄(u)=h*(u) pointwise); only the declared positive-frequency/BD-at-this-order prescription excludes it. *(The literature's BD-selection arguments — dS invariance, Hadamard — are not in-repo inputs and were not invoked; importing them could only move this row toward DERIVED, so the classification errs conservative.)* | **DECLARED CONSTRUCTION** |
| **W** (weight balance), total-zero | conformal-weight bookkeeping of the declared EH+dS+normalization inputs, via the in-repo T1/T2 derivations (both coefficients RE-GATED from the frozen artifacts) | **DERIVED FROM PRE-EXISTING INPUT** |
| **W**, the 2-vs-2 split | the σ-reweighting gate: vertex 2→2−2σ, endpoint −1→−1+σ, total ≡ 0 ∀σ — the split moves, the total doesn't | **DECLARED CONSTRUCTION (convention)** |
| **L** (Λ_N = 0) | nothing found: both naive symmetry derivations FAIL (ω-flip relabeling gated FALSE in bedc989; Bose line-exchange weight-EVEN, gated inert here); the operative P1 transposition symmetry is gated-not-derived | **STRUCTURALLY CHARACTERIZED (on the three frozen configurations; P1 THEOREM-LOCAL heritage) BUT UNFORCED** |

**GRUT-SPECIFIC PRINCIPLE: NONE FOUND** *(a search verdict over the §8 candidate table,
not a proof of absence)*. No GRUT-specific input appears in any provenance or verification
chain — every forced piece traces to standard structure (canonical normalization,
conformal-weight bookkeeping) or to declared standard inputs (EH action, dS geometry, BD
prescription, field normalization). Per §11's demand: what has been achieved is **A (exact
algebraic characterization) plus B (derivation from standard inputs) for S and W — where
B for the S-mixing direction and the 2-vs-2 split holds only in the input-citation sense,
the condition being the declared input itself — and A only for L.** A is not reported as
C anywhere.

## S — THE STATE SLOT (§4)

The general multiplicative O(H) deformation h → (1+(x+iy)H)h gives pair state term exactly
2x·(flat pair) — S in this direction ⟺ x = 0, and the phase direction y drops identically
(GATED). The canonical FRW Wronskian a²(u)W[h,h*] is O(H)-flat for the native mode, shifts
by 2x·(flat value) under the x-deformation, and is preserved at O(H) by the Bogoliubov
direction — its cross-Wronskians vanish identically, the full Wronskian rescaling only at
O(α²H²) (all GATED). So: **canonical normalization forces the amplitude direction; only
the state declaration excludes the mixing direction.** Completeness of the dichotomy (per
Leg A): h* solves the same real-coefficient mode equation, so {x, y, α} spans ALL
solution-preserving O(H) state deformations — the two directions are the whole space, not
a sample. No unforced remainder; nothing GRUT.

**Disclosed instrument correction:** the first draft tested the FLAT-space Wronskian and
its three gates FAILED LOUDLY — the bare Wronskian is 2iq(1−Hu)², and the a² weight
compensates its O(H) part exactly. The corrected gates use the canonical FRW condition.
The failure is itself a provenance datum: **the S-amplitude direction and the W-balance
trace to the same a-weight bookkeeping.**

## W — THE WEIGHT SLOT (§5)

Coefficient 2 RE-GATED from the frozen 26,032-term artifact (V₃⁽¹⁾ = 2u·V₃⁽⁰⁾ + R, R
u-free); endpoint weight −1 RE-GATED from the frozen W₊ literal. Their provenance chains
run through the in-repo T1/T2 *derivations* (EH action + dS + TT gauge + mode
equation/normalization), not through a declaration of the coefficients themselves. The
σ-reweighting gate then separates precisely what the order demanded: **"the frozen EH
construction has coefficient 2" is demonstrated; "coefficient 2 is physically forced" is
NOT claimed — the σ-invariant TOTAL-ZERO is what is forced.**

## L — THE LADDER SLOT (§6): THE ONE UNFORCED CONDITION, NOW WITH A SHARPER PREMISE SET

Both naive symmetry derivations fail:
- the ω-transporting vertex-relabeling identity is **gated FALSE** (bedc989 — the named
  negative result);
- the Bose line-exchange candidate is **inert**: the ladder weight (g+h−e−f)(−1)^{e+f} is
  exchange-EVEN (GATED), and the native V is line-exchange symmetric (36/36 on plus_z) —
  consistent, but an even weight on a symmetric array cannot pair-cancel.

**Premise diagnostics (the audit's discovery):** Λ_N ≡ 0 survives with the TT projector
replaced by the plain symmetrizer (no transversality, no trace term), by the transverse
symmetrizer without the trace subtraction (plus_z only — disclosed), and even by the
**unsymmetrized single-δ pairing** — the symmetrizer and single-δ replicated on **all
three configurations**. To the extent tested, **the projector structure is IMMATERIAL**:
on the tested contractions and configurations, a SUFFICIENT premise set shrinks to the
raw flat vertex bilinears + D2 routing + the derivative parity weight — an eventual
derivation of L cannot lean on TT/projector structure. (Leg B's cancellation probe: under
single-δ, 22 keys carry nonzero weighted entries that genuinely cancel across keys — the
zero is collective, not termwise trivial.) Also not premises (cited from closed gates):
dimension (d symbolic throughout), momentum conservation (Route B per-line
decomposition), the CTP assembly (Stage-1 pointwise zeros pre-assembly).

The operative mechanism — P1's fixed-ω graded routing-transposition symmetry — is itself
GATED, not derived; its derivation from first principles remains the named open
generalization. **L = structurally characterized but unforced.**

## INDEPENDENCE (§7) AND HOSTILE ALTERNATIVES (§9)

All six pairwise implications among S, W, L: **DISPROVED BY CONTROL** — each closed
one-slot control supplies a frame point with two conditions holding and one failing
(Phase 3: S,L∧¬W; Phase 2: W,L∧¬S; V_k+1: S,W∧¬L). The three are logically independent
requirements **of the frame's parameter space** — they are not coordinates of one deeper
identity. Caveat, kept explicit: the witnesses are frame-admissible parameter moves, not
alternative physical theories; independence-as-frame-requirements is established,
fundamentality is NOT.

## DEEPER-PRINCIPLE SEARCH (§8) — candidates that could fail, and did or didn't

| candidate | outcome |
|---|---|
| canonical normalization | **DERIVES S (amplitude)** — and could have failed: it visibly fails for x≠0 |
| BD/positive-frequency prescription | INPUT that excludes S (mixing); not derived from anything deeper in-repo |
| conformal-weight bookkeeping | **DERIVES W (total)** — the same accounting that fixes the canonical Wronskian |
| field-normalization convention | explains the 2-vs-2 SPLIT only |
| Bose internal-leg exchange | INERT for L (weight-even; gated) |
| vertex relabeling with ω-flip | FALSE for L (gated, bedc989) |
| TT projection / trace structure | NOT a premise of L (diagnostics) |
| dimension, momentum conservation, CTP | not premises (cited gates) |
| diffeo/gauge, dS geometry, locality, time-reversal | explanatory context only; no derivation without importing the result |
| **any GRUT-specific principle** | **NONE FOUND** |

## FINAL CLASSIFICATION (§12)

**`PARTIALLY-FORCED`** — S and W are forced (given the declared standard inputs) by standard
identities with complete in-repo provenance chains; L is exactly characterized, its naive
derivations are refuted, its premise set is sharply narrowed, and it remains underived.
Under §12's vocabulary this is **PARTIALLY FORCED**, with the honest reading the owner
anticipated holding for the L slot specifically: the most elegant piece of the mechanism
is currently a property of the construction, not a derived principle.

## ADVERSARIAL LEG A — PROVENANCE: `CONFIRMED` (workflow w8zf5yge7; independent 25/25)

The two load-bearing attacks both FAIL, with strengthenings adopted:
- **The a²W condition is not an ad-hoc fix:** a² is the UNIQUE integrating factor
  exp(∫2a′/a) of the frozen mode equation (a²h′)′ + q²a²h = 0 — no freedom to tune it —
  and as a control, a³W is NOT constant at O(H). Moreover the identical statement
  a²(h h*′ − h′h*) = 2ik = const was **already gated EXACTLY in the frozen T2 instrument**
  (with |P| = a² derived from the action) — Phase 5's corrected gate converges to the
  pre-existing frozen normalization, not a new fit.
- **"In-repo derivation" is real, not declaration-laundering:** T1 genuinely derives the
  cubic vertex (explicit graded Christoffel/Ricci from √−g(R−2Λ), with independent
  anchors); T2 derives the kernel (BD mode gated as an EXACT solution; a²W = 2ik gated;
  normalization fixed via the G_R/commutator identity + Kubo positivity). The leg also
  tied the endpoint weight tighter than Phase 5 did: **W₊ == (κ²/q)h(u)h*(u′) EXACTLY**,
  so the line weight literally inherits the derived mode normalization. Sharpness
  control: weights 1 and 3 do NOT strip u — 2 is sharp.
- No circularity (the Wronskian a² is the QUADRATIC kinetic weight, the audited balance
  the CUBIC vertex weight; shared ancestry disclosed, no premise-conclusion loop);
  controls used only as counterexample witnesses — legitimate.
Four observations, all adopted as disclosures: the projector diagnostics are RESULTs
feeding DIAG, not battery gates (by design — a diagnostic flip would remap premises, not
invalidate the audit); the span-completeness step behind "no unforced remainder in S" was
unwritten in the instrument — the leg verified it and it now appears in §S above; the
transverse-no-trace variant ran on plus_z only (disclosed above); dead code (unused
phase_classes/iszero; one unreachable verdict branch — see the epistemology note below).

## ADVERSARIAL LEG B — PHYSICAL INTERPRETATION: `CONFIRMED` (workflow w8zf5yge7)

Leg B's independent answer to "what, exactly, has been explained?" matches the record's:
WHY two of the three conditions hold (S-amplitude = the textbook canonical identity — the
leg verified the frozen mode is EXACTLY the phase-stripped BD graviton mode; W-total =
weight bookkeeping rooted in real T1/T2 derivations), and that the third is **"a real
regularity deserving a derivation, currently without one."** A/B/C discipline held; GRUT
language scan CLEAN (every occurrence negative or classificatory); L neither undersold
nor oversold; PARTIALLY-FORCED follows from the per-condition classifications and is
**robust in the safe direction** (importing the literature's BD-selection arguments could
only make it MORE forced). Six wording corrections, ALL adopted above.

**Verdict epistemology (adopted from both legs, stated plainly):** "PARTIALLY-FORCED,
19/19" certifies the S/W forcing and governance at GATE strength; the L-unforcedness half
has SEARCH-VERDICT strength — refuted candidates plus citation, which is the correct
epistemology for a negative (one refutes candidates; one cannot gate a non-existence).
The instrument's third verdict branch is unreachable dead code for the same reason (any
forcing-gate failure forces INCONCLUSIVE first) — disclosed, harmless on this run since
the INCONCLUSIVE guard means a failed forcing gate can never masquerade as a verdict.

## GOVERNANCE EXIT (§14)

Register sha pre == post; frozen set unchanged; Phases 1–4 byte-identical; A–F UNSELECTED;
W-0; nothing banked; HEAD == origin/v4; **Phase 6 NOT started.**

## W-0 STATUS — audit computed and reported; no frozen input modified; nothing banked.
