# H¹ CLOSURE — PHASE 6: LADDER-IDENTITY DERIVATION ATTACK

**Date:** 2026-09-03 · **Instrument:** `wall_kr_h1_phase6_ladder_derivation.py` ·
**Artifact:** `WALL_KR_H1_PHASE6_RESULT.json` · **Base:** 016d84b (Phases 1–5 CLOSED).
**Battery: 34/34 testable gates, zero failures (27 s).**
**CLASSIFICATION: `LADDER-DERIVED`.**
Read-only; register sha256 identical pre/post; A–F unselected; nothing banked; Phase 7
NOT started. W-0.

## B · THE DERIVATION (every step gated; no prior-phase identity used as premise)

The Phase-1 swap relation, Λ_N ≡ 0, and the Phase-4 factorization were NOT premises.
Two raw premises, both read off the frozen construction:

- **PREMISE (i) — HOMOGENEITY:** every monomial of every flat C⁰ entry has total
  (ω,ν₁,ν₂,q)-degree EXACTLY 2 (GATED, all entries, all three configurations) — the
  two-derivative character of the Einstein–Hilbert action at the flat level. Hence each
  entry is EVEN under total momentum reflection, giving **the bridge, per entry:**
  E(−ω,−q)(ν) = E(ω,q)(−ν) — *the frozen D2 transform IS a pure ν-reflection* (GATED).
- **PREMISE (ii) — SLOT SYMMETRY:** the contraction Π is symmetric under exchanging the
  two vertex slots (GATED for P^TT and for the single-δ pairing) — dummy-index
  relabeling.

**Derived step 1** (from i): per key, **V[(e,f),(g,h)] = (−1)^{g+h}·G[(e,f),(g,h)]** —
the frozen routing array IS the graded untransformed Gram array (GATED, all 36 keys,
all three configs).
**Derived step 2** (from ii): **G is symmetric under key transposition** (GATED).
**Conclusion:**

$$ \Lambda_N \;=\; (-1)^N \sum_k (g{+}h{-}e{-}f)\,G_k \;=\; 0 $$

— an antisymmetric weight against a symmetric array, cancelling **per
transposition-orbit** {k, kᵀ} (diagonal keys carry zero weight), at FIXED ω. The direct
Λ_N ≡ 0 (N = 0..4) is REPRODUCED on all three configurations — derived, not assumed.

## WHAT THE DERIVATION EXPLAINS (each item previously a bare gated fact)

| previously observed | now derived from |
|---|---|
| the fixed-ω (no-flip) form of the P1 symmetry | the reflection restores fixed ω; NO symmetry supports an ω-flipped form (the flipped variant's FALSITY remains P1's gated fact, resting additionally on the ω-oddness of the mixed S-blocks — leg-verified, consistent with but not derivable from (i)+(ii)) |
| Phase-5 projector-immateriality | ANY slot-symmetric contraction satisfies premise (ii) |
| d / momentum-conservation / CTP immateriality | none of them appears in any step |
| the sector bound N ≤ 4 | degree ≤ 2 per vertex (premise i) |
| the T-array symmetry (P1's "graded routing-transposition symmetry") | T_{j,m} = (−1)^{j+m}⟨E_j, E_m⟩_Π — literally a Gram-type symmetric form on the ν-graded components of ONE vertex function *(follows from derived steps 1–2; the aggregated (j,m)-block identity not separately gated here — Phase 7 could gate it, as it could the hostile-(b) per-sector pattern N=1,2,3, currently label-detail on an any-nonzero boolean, leg-verified)* |

## D/E · ROUTING ORBITS AND SECTORS (§5, §6)

Orbits = key-transposition pairs {k, kᵀ}, from the VERIFIED symmetry (not chosen for
prettiness); cancellation is **intra-orbit** and exact; diagonal keys are annihilated by
the weight. All five sectors collapse to the single generating identity above (the §7
generating-function object is the Gram form itself; no extra machinery needed).

## G · HOSTILE DISPROOF MODE (§10) — the controls that carried the phase

- **HOSTILE (a), premise (i):** injecting a DEGREE-1 momentum term into one C entry
  breaks the bridge AND Λ_N ≠ 0 (GATED) — homogeneity is load-bearing.
- **HOSTILE (b), premise (ii):** a two-projector contraction isolating the single
  incompatible cross-pair 11_11 ⊗ 11_33 breaks G-symmetry AND Λ_N ≠ 0 at sectors 1,2,3
  (GATED) — slot symmetry is load-bearing for the derivation route.
- **DISCLOSED, the full §10 chain:** three earlier hostile-(b) drafts failed against
  their own gates — (1) an index-weighted δ-pairing is INERT on support (the δs force
  a=aᵖ); (2) off-diagonal support (1,1)→(1,2) misses the nonzero entries (empty arrays);
  (3) support (1,1)→(2,2) is asymmetric and supported — and Λ STILL cancelled, which
  was not a bug but the refinement below. Each failure was caught by the gate designed
  to catch it; none was papered over.

## THE REFINEMENT THE HOSTILE CHAIN FORCED (gated)

Draft 3's survival had a reason: **the operative intermediate condition is G-SYMMETRY
itself.** Under the asymmetric pairing 11_11 ⊗ 22_22, G came out symmetric anyway —
because those two entries' ν-stripped coefficient vectors are **PROPORTIONAL** (gated),
making the outer product symmetric under ANY pairing; whereas 11_11 and 11_33 are NOT
proportional (gated), which is exactly why hostile (b) breaks there. Refined chain:

> Λ_N = 0 ⟸ G symmetric ⟸ **either** premise (ii) (slot-symmetric Π, any entries —
> the route covering the NATIVE contraction) **or** entry-proportionality (special
> entry pairs, any Π).

No second mechanism was observed — the derivation factors through G-symmetry in every
observed case (an accidental cancellation with asymmetric G is refuted-by-search, not
gated impossible). Premise (ii) is sufficient, and NOT necessary in general.

**Residual structure (d2, recorded, not chased):** the entries partition into 5
proportionality classes (plus_z): [11_11, 22_22], [11_22, 22_11], [11_33, 22_33],
[13_13, 23_23], [33_11, 33_22] — visibly the 1↔2 transverse-index exchange pattern.
*(Leg B's cross-config data sharpens the observation: 5 classes on ALL three configs —
cross_z with two singletons [12_33],[33_12]; plus_x pairing indices 2↔3 — i.e. the
pattern is transverse-index exchange in each configuration's OWN transverse plane.)*
Observation only; WHY the EH vertex produces these proportionalities is open.

## F · WHAT THE DERIVATION DOES AND DOES NOT USE (§8, §9)

NOT used: d (symbolic or otherwise), angular averaging, momentum conservation (the
argument is per-vertex; independent line momenta never enter), CTP/retarded structure,
on-shell conditions, TT conditions — the derivation **closes BEFORE TT projection**, and
the full chain was re-verified under the single-δ pairing (GATED). USED: premise (i)
(gated on the raw artifact), premise (ii) (gated), the ν-grading bookkeeping, the frozen
D2 convention (whose entire content, by the bridge, is the ν-reflection).

## NECESSITY / SUFFICIENCY (§11)

SUFFICIENT: (i)+(ii) ⟹ Λ_N ≡ 0 — exact, gated, covering the native contraction.
NECESSITY, honestly split: (i) load-bearing (hostile a); (ii) load-bearing for the
derivation route (hostile b) but NOT necessary in general (the refinement) — G-symmetry
is the operative condition. **Premise provenance (sharpened per Leg B):** (i) is the
two-derivative character of EH at the flat level — produced by T1's in-repo derivation
from the declared action and gated directly on the artifact; the EXACTNESS of degree 2
also uses the declared Λ = 3H² being O(H²) (a generic cosmological constant would
deposit derivative-free cubic monomials at flat level), and gauge-fixing/measure terms
are absent BY DECLARED CONSTRUCTION (full unfixed h; classical action-level vertex) —
structural, not merely unobserved. (ii) is dummy-index relabeling — a standard
identity. **NEITHER IS GRUT-SPECIFIC.**

## H · ADVERSARIAL LEG A — ALGEBRA: `CONFIRMED` (workflow w698vxp9d)

Reconstructed independently from the RAW frozen cache in a **different representation**
(its own ν-decomposition via sp.Poly, its own P^TT, its own stricter zero-test): all
steps reproduce on all three configs, including the 5-class partition byte-for-byte.
**The circularity attack fails on commit archaeology:** the D2 convention was frozen at
65ccb1b (2026-09-01, TIER 3 COMPLETE) — two days BEFORE P1 existed — with loop-routing
provenance that never touches the ν symbols; the bridge is a discovered equivalence, not
a definition, and it is falsifiable (it fails under the hostile-a admixture). **The
derivation is a structural theorem:** the leg's genericity control (random integer
degree-2 entries over the same key skeleton, random symmetric pairing) gives Λ_N ≡ 0
identically, and a degree-1 admixture or asymmetric pairing breaks it generically — the
zero is structural, not an EH-coefficient coincidence. **P1's swap relation verified as
a corollary** (per-key V_k = (−1)^N V_kᵀ aggregates to S_{m,j} = (−1)^{j+m}S_{j,m}),
with the ω-flip variant re-confirmed FALSE. No hidden P1/P4 use (prior phases enter only
as ancestry gates). Two record-accuracy notes, adopted: the TT configs' flat entries are
**q-free entirely** (free symbols exactly {ω,ν₁,ν₂}; the (ω,ν₁,ν₂,q)-degree phrasing is
technically satisfied but the bridge's q→−q leg is vacuous at this level; only the
excluded `ward` config carries q_i); and the ±q spatial routing is of course baked into
the upstream cache construction — covered by the THEOREM-LOCAL scope declaration.

## I · ADVERSARIAL LEG B — INTERPRETATION: `CONFIRMED` (workflow w698vxp9d)

**The §13 question answered: EXPLAINED, not merely re-verified** — on four
adversarially-checked grounds: premise independence (neither premise mentions Λ_N; both
gated on the raw object); the derived steps are genuine logical consequences, not
parallel gated facts; **counterfactual dependence — the discriminator between explanation
and shorter verification — is gated in both directions** (hostile a and b); and the
framework absorbed its own anomaly (draft 3's cancellation explained inside the same
structure, its remainder honestly quarantined). Premise provenance survives hard
scrutiny with the Λ~H² nuance adopted above; gauge-fixing/measure absence is structural
(declared unfixed-h, classical action vertex). The refinement does not weaken the
derivation ("a derivation needs sufficiency, and the sufficient route covers the actual
frozen object"; premise (ii)'s non-necessity is a fact about counterfactual contractions
nobody uses). Classification exactly right under §13's vocabulary — and notably
conservative: "the ingredients for a THEOREM-EH-TT generalization are now visibly close,
and the record still refuses to claim it." GRUT scan CLEAN ("this phase, if anything,
moves the H¹ mechanism FURTHER from GRUT-specific territory, and says so plainly").
Battery recount honest (34 substantive booleans; the P1 vacuous-gate defect cured; no
gate(True) prose). Seven wording corrections, ALL adopted (the ω-flip explains-item
rescoped; the Λ~H² provenance nuance; the premise-(ii) label fixed at source — the P1
label-riding lesson applied to itself; the observed-case qualifier led; the
Gram-row/per-sector gating notes; the cross-config d2 data; the §13 reassignment below).

**§13 label reassignment (adopted):** STILL UNFORCED no longer attaches to the ladder
identity within-frame — it now attaches to a NEW, smaller object: the d2
proportionality-class partition, a property of non-native contractions, outside the
native forcing chain.

## J/K · EPISTEMIC CLASSIFICATION AND EXACT SCOPE

**`LADDER-DERIVED`** — under §13's vocabulary the ladder identity is **DERIVED FROM EH**
(premise i) plus a **STANDARD IDENTITY** (premise ii), within the declared frozen frame:
the three frozen TT configurations and routing conventions (THEOREM-LOCAL heritage).
This upgrades Phase 5's L row: the last unforced condition of the H¹ mechanism now has a
derivation whose premises trace to the declared EH input and standard algebra. NOT
claimed: generality beyond the frozen configurations/conventions; necessity of the
premises beyond the tested directions; any GRUT-specific content. The Phase-5/Phase-7
consequence — that ALL THREE H¹ conditions now trace to standard structure — is left to
the later phases to adjudicate formally.

## GOVERNANCE EXIT (§16)

Register sha pre == post; frozen set unchanged; Phases 1–5 byte-identical; A–F
UNSELECTED; W-0; nothing banked; HEAD == origin/v4; **Phase 7 NOT started.**

## W-0 STATUS — derivation computed, gated, and reported; no frozen input modified; nothing banked.
