# H¹ CLOSURE — PHASE 4: MECHANISM SYNTHESIS / MINIMAL SUFFICIENT CONDITION

**Date:** 2026-09-03 · **Instrument:** `wall_kr_h1_phase4_mechanism.py` ·
**Artifact:** `WALL_KR_H1_PHASE4_RESULT.json` · **Base:** dffe1ca (Phases 1/2/3 CLOSED).
**Battery: 59/59 testable gates, zero failures (895 s, post-reconciliation rerun; the
first 52/52 run's verdicts all reproduced, plus the adopted-under-gate leg corrections:
q-freeness, the fourth channel, RES fields bound to measured outcomes; no giant global
zero-tests — the native zero is proven by the per-key decomposition identity + ladder
closed form + small per-sector polynomial sums).**
**CLASSIFICATION: `MECHANISM-FACTORIZED`.**
Read-only; register sha256 identical pre/post; A–F unselected; nothing banked; Phase 5 NOT
started. W-0.

## THE EXACT FACTORIZATION (gated, not interpretive)

The native O(H) mixed object and its three controlled deformation directions organize as
the **exact identity**

$$ M(\alpha,\beta;V) \;=\; \alpha\,X_s \;+\; \beta\,X_w \;+\; F_{\mathrm{ladder}}(V),
\qquad F_{\mathrm{ladder}} = \sum_{N=0}^{4} \Lambda_N(V)\cdot\big(i\,\mathrm{pref}\,
q^{N-1}W^2\big), $$

with native values **α = 0, β = 0, Λ_N ≡ 0**. Every ingredient is separated algebraically
and gated per key:

- per line, m_line = −(u+u′)·flat + dem (product rule);
- per key, m_key(full, with the vertex a² weight) **= D_k exactly** — the weight
  contribution (B_conf + W_vert) = (−2+2)(u+u′)flatAflatB cancels PER KEY;
- per key, D_k = i·pref(g+h−e−f)(−1)^{e+f}q^{N−1}W² (the ladder closed form, all 36 keys);
- the state slot is the L1 identity: the BD pair's O(H) state term ≡ 0 per line pair.

## THE THREE CANCELLATION DEPTHS (the architecture)

| slot | native condition | cancels | depth |
|---|---|---|---|
| **state** | c_s = 0 (BD pair O(H) state term ≡ 0) | internally, per line pair, BEFORE any contraction | identity level |
| **weight** | c_w = 2−2 = 0 (vertex a² vs two-line conformal) | pairwise between ingredients, PER KEY | pairwise |
| **ladder** | Λ_N ≡ 0 per sector | only AFTER routing aggregation (individual V_k·D_k are NOT zero — witnessed) | collective |

This answers §2's "which terms cancel where" exactly: one ingredient cancels internally,
one pairwise, one only after routing aggregation — three genuinely different depths.

**On the C×L question (§3D):** M does **not organize** as a single global product C×L in
the natural form class (one propagator-free factor × one W²-type kernel) — with α on, the
object spans three distinct phase classes, which no single-kernel product can do. The
structure is additive. The genuine product form lives inside the ladder leg only:
F_ladder = Σ_N Λ_N × (kernel), where Λ_N is the propagator-free compatibility factor.
*(Softened per Leg B: the first draft's flat "does not exist" was an ungated negative
without a declared form class.)*

## PHASES 2 AND 3 AS VALIDATION PROBES (§3 — re-derived, not read)

- **Phase 2's α direction switches on exactly the state slot:** X_s ≠ 0 (re-derived
  in-run), and its phase classes {+2iqu′, −2iqu} are **DISJOINT** from the native class
  {−2iq(u−u′)}.
- **Phase 3's β direction switches on exactly the weight slot:** X_w = (u+u′)Σ₀ ≠ 0
  (re-derived in-run).
- **The V_k perturbation moves exactly the ladder functionals Λ_N.**
- **Same native identity, one factor removed each time** — §3C answered YES: both phases
  exposed the same decomposition with exactly one independently controlled coefficient
  switched on.

## COUNTERFACTUALS (§6 — only the mathematically natural ones, defined by the factorization)

- **Superposition (gated, all 36 keys, all configs):** the joint two-parameter family
  gives M(α,β) = αX_s + βX_w + F_ladder with **no α·β cross term at O(H)** — the additive
  structure is exact, not approximate.
- **No mutual compensation (gated):** αX_s + βX_w = 0 forces α = β = 0 — the two exposed
  failure modes live in disjoint phase classes and cannot cancel each other. No further
  natural control exists beyond these; none was invented.

## NECESSITY vs SUFFICIENCY (§4 — the epistemic gate)

| condition | status within the declared frozen frame |
|---|---|
| (i) native O(H) state pair term ≡ 0 | **NECESSARY AND (jointly) SUFFICIENT** — necessity by phase-class disjointness: a nonzero state-slot coefficient cannot be absorbed by any other slot |
| (ii) exact vertex/line conformal balance (c_w = 0) | **NECESSARY AND (jointly) SUFFICIENT** — necessity by u-degree separation: (u+u′)P + Q = 0 with P,Q u,u′-free forces P = Q = 0 |
| (iii) per-sector Λ_N ≡ 0 | **NECESSARY AND (jointly) SUFFICIENT at native scope** — the native V_k are **q-FREE** (GATED), so q-degree separation forces each sector from the aggregate; against q-DEPENDENT V deformations (which the cdecomp contract admits, e.g. ward-like entries) necessity binds in aggregate form only. **CORRECTED per both adversarial legs:** the first draft claimed aggregate-only necessity on the premise "V_k carries q" — that premise is FALSE for the native TT arrays (an under-claim on a wrong premise, fixed in the strengthening direction) |

**SUFFICIENCY IS EXACT:** (i) + (ii) + (iii) ⟹ M_H1 ≡ 0, by the gated decomposition
identity — not by inspection, not by example-collection.

**INDEPENDENCE:** witnessed by the three one-slot deformation directions (α, β, V_k+1) —
no condition implies another; they act at three different depths and are additively
separated. None of the three is redundant.

**Deeper explanation, kept distinct from the minimal set:** the per-sector Λ_N ≡ 0 follows
from Phase 1's graded routing-transposition symmetry contracted with the antisymmetric
demotion weight — that is *why* (iii) holds natively, but the minimal sufficient set needs
only Λ_N ≡ 0 itself (and, minimally, only its aggregate form).

## THE MINIMAL SET (§5)

> **Within the declared frozen frame, the native H¹ = 0 reduces to exactly three
> conditions: (i) the native O(H) state pair term vanishes; (ii) the vertex a² weight
> exactly balances the two-line conformal dressing; (iii) the propagator-free ladder
> functionals Λ_N vanish — per sector, which at native scope (q-free V, gated) is
> equivalent to the aggregate form; sufficiency holds for either form.**

This is the synthesis the order asked for: the Phase-2 and Phase-3 breaks are not two
curiosities — they are the two shallow slots of one exact three-slot identity, and the
strongest legitimate statement is the owner's: *the native H¹ cancellation is structurally
sensitive to at least two separately controlled ingredients* — now sharpened to: **within
the declared frozen frame, it is the simultaneous vanishing of three independent structure
coefficients at three different algebraic depths.**

**The fourth channel (adopted from Leg A, now GATED):** the full-object H¹ additionally
contains the u-free vertex-grading remainder R — Protection 1's frequency-insertion
structure — which sits OUTSIDE the mixed object's three slots and **assembles to zero
pre-angular with flat lines by its own mechanism** (gated, all three configurations). The
complete picture: full H¹ = the three-slot mixed identity + this separately vanishing R
channel, four vanishing structures in all, the fourth explained by Protection 1 (2B.1),
not by the three-slot mechanism.

## d=3 AND ANGULAR STATUS (§7)

Both exposed shapes survive exactly: ⟨X_w⟩ ≠ 0 and ⟨X_s⟩ ≠ 0 post-angular AND at d=3
(exact moment() machinery, no numerics) — **this also closes the Phase-2 addendum's
symbolic-d-only gap for the state leg.** No numeric witness certifies any zero anywhere in
this phase.

## ADVERSARIAL LEG A — ALGEBRA: `CONFIRMED` (workflow wc5upsm97)

Reproduced everything ordered, independently: the line closed forms by hand
(flat = (−q)^a q^c W_f, dem = i(−1)^a q^{a+c−1}(c−a)W_f) and the ladder form on all 81
(e,f,g,h) combinations; the per-key decomposition; F_state = 0 from the BD modes; Λ_N ≡ 0
per sector on all three configs; the class facts with its own denominator-aware splitter;
superposition; both shapes post-angular and at d=3; the α-direction shape re-derived from
Bogoliubov-deformed BD pairs. No hidden use of prior-phase RESULTS (definitions only,
verified to match). Representation dependence: the slots are pinned by an invariant double
grading — phase class × u-degree of the stripped coefficient — with the linear-independence
loophole (hash-equality vs genuine distinctness of exponent forms) explicitly closed.
**Four findings, all adopted:** (1) the FALSE "V_k carries q" premise (see the corrected
necessity table — the leg verified native V_k are q-free, only `ward` carries q_i);
(2) hardcoded-True RES fields feeding the §4/5 summary gates — a milder recurrence of the
self-certification shape — **FIXED AT SOURCE**: the instrument now binds every RES field
to its actual gate outcome, and the corrected battery re-ran green; (3) the un-gated
R-omission — **now GATED** (the fourth-channel gate above); (4) the frozen T3 exec's
internal T3-0 checks run in a sub-namespace whose failures would not propagate — compensated
by Phase 4's own sha pin and git-clean gates on the caches (disclosed). The leg also
disclosed and fixed two bugs in its own scratch tooling before its accepted runs.

## ADVERSARIAL LEG B — INTERPRETATION: `CONFIRMED` (workflow wc5upsm97)

The final statement **is genuinely the stronger form** and the algebra supports it: the
within-frame biconditional (M ≡ 0 ⟺ the three conditions) is carried by the decomposition
identity + the two separation arguments, not by control-sampling. The leg independently
verified the one unstated premise both separations need — all 36 V_k are u,u′-free and
phase-free in all three configs — **premise holds**. Controls properly recast as one-slot
probes with directions re-derived in-run; no stray uniqueness or GRUT claims; the minimal
set is genuinely minimal (no two-condition subset suffices; no condition implies another);
the Phase-1 symmetry is correctly positioned as the explanans for (iii), outside the
certified conditions. **Five wording corrections, all adopted:** the q-premise fix; the
RES binding fix (at source); the C×L softening with a declared form class; the inline
frame qualifier on the sharpened sentence; the (iii)-either-form harmonization between
md and JSON.

## NOT CLAIMED

"a² is uniquely required" over any admissible theory space; GRUT content; per-sector
ladder necessity against q-DEPENDENT V deformations (established at native q-free scope
only); any statement beyond the declared frozen frame; any H1-THEOREM-A/B/C adjudication
(that is a later phase).

## GOVERNANCE EXIT (§12)

Register sha pre == post; frozen artifacts unchanged; Phase-1/2/3 artifacts byte-identical;
A–F UNSELECTED; W-0; nothing banked; HEAD == origin/v4; **Phase 5 NOT started.**

## CLASSIFICATION: `MECHANISM-FACTORIZED`

## W-0 STATUS — synthesis computed and reported; no frozen input modified; A–F unchanged; nothing banked.
