# H¹ CLOSURE — PHASE 7: EH-TT GENERALITY / THEOREM-BOUNDARY AUDIT

**Date:** 2026-09-03 · **Instrument:** `wall_kr_h1_phase7_generality.py` ·
**Artifact:** `WALL_KR_H1_PHASE7_RESULT.json` · **Base:** b10c4d9 (Phases 1–6 CLOSED).
**Battery: 22/22 testable gates, zero failures (200 s; post-reconciliation rerun — the
first 19/19 run's verdicts all reproduced, plus the leg corrections gated at source:
degree-4 on the complete basis, the u,u′-freeness companion assumption, the direct (a,b)
polarization identity, and the completed degree-3 basis).**
**CLASSIFICATION: `TWO-DERIVATIVE-CLASS-GENERALIZED`** — with the boundary sharpened to
the EVEN-momentum-degree class. Λ_N ≡ 0 was a TARGET throughout, never a premise.
Read-only; register sha256 identical pre/post; A–F unselected; nothing banked; Phase 8
NOT started. W-0.

## §3 · POLARIZATION: FROM THREE CONFIGS TO THE TENSOR LEVEL

**Tensor-level homogeneity (gated):** all 7,560 flat vertex terms have total degree
EXACTLY 2 in the full unrouted 4-momenta (12 components p{1,2,3}_{0..3}) — **before any
external slotting, internal routing, or projection.** Every slotting is linear with
momentum-free (polarization) coefficients, so premise (i) descends to EVERY external TT
polarization and EVERY routing automatically: the three frozen configurations were
representatives **for premise (i)**, not load-bearing for it — the probe direction
remains load-bearing for the conclusion's polarization *coverage* (§3b).

**The full TT polarization space at the frozen probe direction (gated):** the
symmetrized mixed Gram argument closes P1's polarization-span caveat at direction z —
(G^{pc})_k = (G^{cp})_{kᵀ} (cross-symmetry), each mixed array is the graded mixed Gram,
and **Λ^{pc}_N + Λ^{cp}_N ≡ 0 for every sector.** And no longer by bilinearity alone:
**gated directly** — with the superposed entries E(e) = a·E(plus) + b·E(cross),
Λ_N(e) ≡ 0 IDENTICALLY in symbolic (a,b), every sector — the FULL 2-parameter TT space. **NOT claimed:** probe-DIRECTION generality
(plus_x probes a second direction with its 1-parameter family; no cross_x exists in the
frozen cache).

## §4/§8 · THE ABSTRACT THEOREM (replacing the genericity control with a formal proof)

For **GENERIC entries with free symbolic coefficients** on the full degree-2 monomial
basis and a **GENERIC symbolic symmetric pairing** π_rs = π_sr, the whole chain — V ==
graded G, G symmetric, Λ_N ≡ 0 — holds as **POLYNOMIAL IDENTITIES in all 24 free
coefficients** (gated). This is a formal theorem for the class, not a sample: any
even-degree entry family, any symmetric slot pairing, no EH coefficients anywhere.

## §6/§7/§10 · THE BOUNDARY — AND IT MOVED

| contamination | effect (gated, complete bases) |
|---|---|
| generic DEGREE-0 (cosmological-constant-type, no derivatives) | **HARMLESS** — the full chain intact, Λ_N ≡ 0 still a polynomial identity |
| generic DEGREE-1 | breaks the graded bridge AND leaves Λ_N a NONZERO polynomial |
| generic DEGREE-3 (complete 10-monomial basis) | likewise breaks bridge and Λ |
| generic DEGREE-4 (complete 15-monomial basis) | **HARMLESS** — Λ_N ≡ 0 a polynomial identity through sector N=8 |

**The derivation's true premise is EVENNESS of total momentum degree, not
exactly-degree-2** — Phase 6's premise was stronger than needed. Support stated
precisely (per Leg B): **GATED at degrees {0, 2, 4}** with odd counterexamples at
{1, 3}, all on complete bases; **higher even degrees follow from the parity identity**
((−1)^{ω-deg} = (−1)^{total deg}·(−1)^{ν-deg}) — a derivation, not separately gated. The
precise obstruction is parity: the odd part acquires an extra (−1) under total momentum
reflection, splitting the grading. Consequences for §6's list: a generic cosmological
constant would NOT break the ladder identity (it breaks exactness-of-2 but not
evenness) — and Leg A verified this **in the concrete construction** (degree-0 injections
into the real plus_z entry 11_11: harmless; the cache's H-carrying terms indeed hold the
O(H²) degree-0 deposits, corroborating the declared-Λ order counting); gauge-fixing
terms, if present and two-derivative, would be degree-2 (harmless) — their absence in
the frozen construction remains structural by declaration (P6); measure/local
non-derivative terms would be degree-0 (harmless); odd-derivative terms are the boundary.

## §5/§9 · ROUTING AND INGREDIENT CLASSIFICATION

**Gated:** the frozen TT flat entries are q-FREE **and u,u′-FREE** (all three configs —
the latter the companion assumption Leg A found unnamed in the first draft, now gated) —
so BOTH non-ω legs of the frozen D2 transform (q→−q and u→u′) are vacuous at flat level,
and the abstract theorem's ω→−ω-only analogue is FAITHFUL to the full frozen convention;
±q routing is an upstream cache-construction fact, outside the theorem. Classification: dummy-index relabeling and
slot exchange = mathematical identities (the abstract theorem uses only these); the D2
representation = frozen convention whose entire flat-level content is ω→−ω, derived
equal to the ν-reflection by the bridge; q-sign/momentum assignment = upstream
conventions, vacuous at flat level; **d, angular averaging, momentum conservation, CTP,
retarded prescription, on-shell conditions, TT projection = ABSENT from the abstract
theorem BY CONSTRUCTION** — no such symbol or constraint exists in it. That is the
strongest form of the §9 independence proof: inspection of a complete formal object, not
citation of earlier controls.

## §11 · NECESSITY / SUFFICIENCY FOR THE GENERALIZED THEOREM

- **Even-degree homogeneity:** SUFFICIENT (polynomial identity); NECESSARY at generic
  level (generic odd admixture leaves Λ a nonzero polynomial — gated; special odd
  entries could still cancel, so necessity is generic, not universal).
- **Symmetric slot pairing:** SUFFICIENT; NOT NECESSARY (P6 refinement:
  entry-proportionality is an alternative route — cited, closed).
- **Additional EH-specific condition: NONE.** The abstract theorem needs no EH input
  beyond membership in the even-degree class; **EH enters only as the provenance of that
  membership** (the two-derivative action, gated at tensor level).

## §12 · ADVERSARIAL LEG A — MATHEMATICAL GENERALITY: `CONFIRMED` (workflow wyczryawe)

Reproduced every load-bearing gate from scratch and **formally closed the descent
arguments** the first draft carried as reasoning: (a) trilinearity of all 26,032 vertex
terms gated (exactly one e-factor per leg) — with tensor-level degree-2 homogeneity this
makes the slotting-linearity descent airtight (any TT polarization is a constant tensor;
any routing is a linear homogeneous momentum substitution; both preserve exact degree 2);
(b) **NENT=3 sufficiency PROVEN**, not assumed: the identity is bilinear in the entry
index and linear in the pairing, and the leg extracted the pairwise-bracket identities
that carry the theorem to ARBITRARY entry count and ring-valued coefficients (the
concrete Q[n̂]-valued pairing included); (c) the **concrete degree-0 injection** demanded
by the order: real injections into the plus_z entry 11_11 — degree-0 and even-ν
injections harmless, ω and ω·ν₁·ν₂ break at the predicted sectors; (d) a no-grading
control breaks EXACTLY the odd sectors N=1,3 — the parity mechanism is the operative one;
(e) the three-way faithfulness identity (full frozen D2 == ω→−ω alone == ν-reflection)
gated per entry, all configs; (f) the u,u′-freeness companion assumption identified and
gated (adopted at source above). Cosmological-constant order counting verified three
ways. No hidden d/TT/routing/momentum-conservation assumptions — the abstract object's
symbol inventory is literally {ω, ν₁, ν₂, free coefficients, π}.

## §13 · ADVERSARIAL LEG B — THEOREM WORDING: `CONFIRMED` (workflow wyczryawe)

Every quantifier-bearing phrase traced to its domain: the "EVERY polarization/routing"
claims are syntactically bound to premise-(i) descent (justified); "necessarily" occurs
only inside the quoted-and-negated disclaimer; "EH implies"/"all EH vertices"/affirmative
"universal" are absent from md, JSON, and instrument. **The four levels are separated
with no cross-level promotion anywhere** — and the verdict string is deliberately
conservative relative to the sharpened even-class boundary (an under-claim). The record
cannot be read as "every EH graviton calculation has H¹=0": the exact sentence is quoted
and negated in §14 and in the machine-readable not_claimed. Findings, ALL adopted at
source: the degree≥4 tail of "ANY even" was derivation-extended beyond the gated degrees
— **now gated at degree 4** (complete basis; the leg's own independent degree-4 run also
passes); two within-level label-riding instances (universals appended to the degree-0/3
gate labels) — moved to a support-scoped note; "representatives, not load-bearing" scoped
to premise (i); the Λ-vs-Λ_N symbol collision fixed; the JSON kind retitled so it cannot
be skimmed as an achieved-generality label; the §6 degree-4 row promoted from
parity-argument prose to a gated table row.

## §14 · CLASSIFICATION AND THE QUANTIFIED DOMAIN

**`TWO-DERIVATIVE-CLASS-GENERALIZED`.** The exact quantified statement:

> For ANY entry family of even total momentum degree (in the ω-and-ν variables of the
> flat construction) shared by both vertex slots, contracted through ANY symmetric slot
> pairing, with the frozen fixed-ω reflection convention, the ladder functionals Λ_N
> vanish identically — a polynomial identity of the class, of which the frozen EH
> construction is one member (its membership gated at tensor level, 7,560 terms).
> *Support for "ANY even": gated at degrees {0, 2, 4} on complete bases, odd
> counterexamples at {1, 3}; higher even degrees by the parity identity (derivation).*

**The levels, kept separate per §13:** theorem about the frozen construction — YES
(P6); theorem about the declared two-derivative (even-degree) class — YES (this phase);
theorem about EH in general — NOT claimed ("every EH graviton calculation of this class
necessarily has H¹=0" is not established: only the LADDER leg is generalized here; the S
and W legs keep their own provenances, and probe-direction generality is open); theorem
about GRUT — NOT claimed, and the direction of travel is the opposite (the ladder's
explanation is class-structural, not GRUT-specific).

## GOVERNANCE EXIT (§16)

Register sha pre == post; frozen set unchanged; Phases 1–6 byte-identical; A–F
UNSELECTED; W-0; nothing banked; HEAD == origin/v4; **Phase 8 NOT started.**

## W-0 STATUS — boundary audit computed, gated, and reported; no frozen input modified; nothing banked.
