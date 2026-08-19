# GRUT I — what survived

*The human-readable crystallization of the register at the Version I close. This is a **presentation layer over `provenance/claims.json`** — no new content, no new physics. Every claim gets exactly **one** label. It is checked to match the machine register tier-for-tier. This is the **depositable product**: the honest statement of where the responsiveness hypothesis reached, and where it stopped.*

> **Frozen snapshot.** This document is the **Version I deposit — 26 claims, gate GREEN, net +12** — and is held fixed at that milestone. Version II has since opened, and the map has grown borrowed/open scaffold (**live register now 45 nodes: 34 GRUT claims + 11 borrowed/open-field scaffold, net now +13** — the 2026-08-02 restriction booking, the program's first net move — see [`GRUT_II_Agenda.md`](GRUT_II_Agenda.md), `provenance/coverage.py`); those post-V1 nodes are deliberately **not** added here. The 26 labels below are the V1 close.
<!-- REGISTER-SYNC: 50 nodes, net +15 -->
<!-- REGISTER-TOTAL: 71 = 50 grut + 21 vacuum-cluster; nets +15 grut, +0 cluster -->

---

## The four surviving pillars (lead with these)

1. **Open-system ontology.** The gravitational vacuum *is* a responsive open quantum system — a Schwinger–Keldysh influence action with a system↔bath split (`rung1`). The Schwinger–Keldysh machinery is standard physics; **adopting it as the vacuum's fundamental ontology is GRUT's bet.** This is the spine/bedrock — a Bin-1 primitive (see `POSTULATE_MAP.md`), not a derivation.
2. **Responsiveness-as-constitutive.** The retarded response χ(ω) *is* the constitutive law of the vacuum: FDT/KMS detailed balance locks the noise to Im χ (`rung2`), and Kramers–Kronig links the elastic (Love) and dissipative parts (`rung4`). Responsiveness — not a Lagrangian of fields — is the organizing primitive. (Standard physics, organized under the ontology.)
3. **Finite memory.** The vacuum carries a finite memory time (a posit *within* the `rung1` ontology). **Whether that memory is a single Debye pole (collisional, analytic) or a branch cut (free-streaming, collisionless) is open** — universality-probe #1 (`rung3`, deferred). The pillar is finite-memory-*as-premise*; its microscopic realization is the probe, not a settled result.
4. **Self-auditing method.** The machine-checkable anti-laundering register — auditor + resident + harness — that marks every claim *shown* vs *assumed* and refuses to let contradictions or laundering in silently. **Its own novelty screen has now RUN** (`method_novelty`, the fourth pillar's gauntlet): every component is prior art (GRADE tiering · Popper falsifiers · Lakatos input-accounting · CI/linter gates · W3C-PROV lineage · blind analysis · red-team/LLM chain-of-verification); the *synthesis* is **weakly** novel; the freshest part is the application to AI-assisted theory-building. The **"biggest / most-novel contribution" framing is RETRACTED** as an over-claim — the meta-level repeat of the founding mistake. And by the method's own cardinal rule (no claim banks on self-verification), it has been validated on exactly one problem — its own — which is the weakest possible evidence and the precise conflict of interest it exists to flag. **Verdict: a promising in-house discipline, *not* a banked contribution; it owes independent external validation.** (Tier `to-derive`.) The value is in execution and rigor, not invention.

> **The honest headline (both directions at once):** GRUT survived as **one ontological bet, a way of policing it, and a credited set of derived *boundaries*** (the no-gos — see next section). It did **not** survive as new *positive* predictive physics (✓ derived = 0). Zero novel predictions; a real set of walls; and a method that, screened on itself, honestly **refused to overrate itself** — and so is `to-derive`, not banked, until someone else uses it.

---

## The derived boundaries (⊘) — GRUT's genuine GRUT-specific output

Zero novel *positive* predictions (see the tally) — but the framework **does** establish a credited set of **derived boundaries**: GRUT-specific *negatives*, each computed or obstruction-backed (settled-negative on named obstructions — not impossibility proofs; see the calibration below), each a wall any completion must respect. **Every no-go is a boundary of the theory** — this is the project's real value, foregrounded here rather than buried. Full register: [`NO_GO_LEDGER.md`](NO_GO_LEDGER.md).

> **A real finding, not bookkeeping:** even *one of GRUT's own boundaries turns out to be rung3-conditional* — the gravitational-decoherence invisibility (`rung8`) rests on the open super-Ohmic pole structure, so it dropped from the established set on screen. **The bath gates the no-gos too**, not just the positive claims — which is why the anchor-dependence of every boundary is stated with it below. **[CORRECTED 2026-08-10c, in the ledger's direction — this is the deposit document, and the correction reached `STATE.md` first and skipped it: THREE of the four are anchor-clean; the FOURTH is anchor-CONDITIONAL. `NO_GO_LEDGER.md` is the authority and reads: the no-crossing is "conditional on the open `rung3` (a no-go cannot outrank its anchor) — held `to-derive`." So the economical-w(z) entry's no-crossing component is NOT clean of the anchor.]**

**Established boundaries (computed / obstruction-backed; none `rung3`- or `p_tt_ansatz`-gated):**
- **GW dissipation is invisible-by-suppression** (`rung4`) — Im χ → GW dephasing / v_g≠c is real but *computed* **22–62 orders below detectable** (broadband Planck-suppression, structural; it does *not* sample S(0), so it is rung3-independent). A GRUT-derived boundary on its own would-be signature.
- **The α→TT bridge is settled-negative** (`rung9b`) — settled-negative **on three named obstructions** (*projector orthogonality* primary: trace = spin-0, TT = spin-2; g^μν P^TT = 0). The orthogonality kills **that route**, not every route — per `NO_GO_LEDGER.md`'s own calibration this is **not a formal no-go** (impossibility in every extension is *not* claimed; two rescues are named: a new metric-built scalar→TT intertwiner, or the c/C_T Weyl-sector CFT route). Frozen (Version I).
- **An economical (sub-CPL) evolving w(z) is settled-negative** (`rung7_wz`) — matching DESI economically needs ≥2 modes; the conformalon (the natural cheap candidate) **cannot** supply one (no Starobinsky–Yokoyama mass; w=+1/3; ratio O(1)). Structural — holds regardless of pole structure.
- **μ=4/3 is excluded** (`mu_linear`) — the linear-scalar modification GRUT's own coefficient naively suggests is excluded (multi-leg, re-graded 2026-08-03: ISW-cross **computed ~2.0σ** [Σ-corrected; `calc/isw_exclusion.py`; the old ~32σ retired] + DESI Σ₀ ~3.5σ [joint ~4σ-class] + separate-universe no-go [EdS-quantified, conditional]). This exclusion is **`p_tt`-INDEPENDENT**. (The *positive* μ=1=ΛCDM prediction is **not** here — it rests on `p_tt_ansatz`, so it stays `? open`.)

**Held OPEN, deliberately *not* boundaries (conditional — a no-go cannot outrank its open anchor):** the **gravitational-decoherence invisibility** (`rung8`) is rung3-conditional — its dominant diagonal channel's quietness needs the *open* super-Ohmic S(0)=0 (the off-diagonal channel is Planck-robust but sub-dominant); the **no-crossing** of w=−1 (`rung7_w3`) and the **wₐ-sign** (`rung7_w2`) are `rung3`-gated; **μ=1=ΛCDM** is `p_tt`-gated. These stay `? open`, never `⊘`.

---

## Legend

| Label | Meaning |
|---|---|
| **✓ derived** | a novel positive result GRUT genuinely derives |
| **⊘ derived boundary (no-go)** | a GRUT-specific boundary the framework genuinely establishes (a derived *negative*) |
| **✓ standard-physics** | established/borrowed physics, organized under the ontology (not a GRUT novelty) |
| **△ plausible** | an adopted assumption with support — *not* derived |
| **? open** | genuinely unresolved (to-derive / derived-pending) |
| **✗ retracted** | refuted, withdrawn, settled-negative, or moot |

## The register, label-for-label (matches `claims.json`)

| Claim | Tier (register) | Label | One-line honest status |
|---|---|---|---|
| `rung1_inin_action` | shown | **✓ standard-physics** | SK influence-action formalism (standard); adopted as the vacuum's ontology — the open-system **pillar** & Bin-1 primitive. |
| `rung2_kms_gate` | shown | **✓ standard-physics** | FDT/KMS detailed balance as an admission gate (Kubo, Callen–Welton). Responsiveness pillar. |
| `rung3_single_pole` | derived-pending | **? open** | single pole vs branch cut — **universality-probe #1**, dispatch-ready/deferred. The bath. |
| `rung4_love_kk` | shown | **⊘ derived boundary** | the Love/KK tidal structure is standard (responsiveness substrate); the GRUT-specific *output* is the **computed GW-dissipation boundary** — invisible-by-suppression, 22–62 orders below detectable. |
| `rung5_gr_limit` | assumed | **✓ standard-physics** | GR recovered via Clausius (Jacobson) — **borrowed, not hosted** (Ward identity can't fix the action). |
| `rung6_qm_limit` | assumed | **✓ standard-physics** | master-equation reduction (standard); **the Born measure is an inherited primitive**, not derived. |
| `rung7_wz` | to-derive | **⊘ derived boundary** | the established boundary is **no economical (sub-CPL) DESI match** — needs ≥2 modes; the conformalon can't supply the cheap one (settled-negative, independent of `rung3`). (The broader evolving-w(z) differentiator stays `? open`; the no-crossing/wₐ-sign are `? open` in `rung7_w2/w3`.) |
| `rung8_falsifier` | to-derive | **? open** | decoherence invisible **if** super-Ohmic (rung3-as-claimed); the off-diagonal channel is Planck-robust (10⁻²⁹…10⁻⁴⁷, `rung3`-independent), but the *dominant* diagonal channel's quietness (S(0)=0) rests on the **open** `rung3` super-Ohmic structure — a **conditional** boundary, not established. |
| `rung9a_value` | shown | **✓ standard-physics** | α = a/c = 1/3 — Duff anomaly ratio, adopted as a *conditional-theorem* axiom (IF the conformal mode is the carrier). |
| `rung9b_bridge` | assumed | **⊘ derived boundary** | the anomaly→TT **bridge is settled-negative** on three named obstructions (projector orthogonality primary: trace=spin-0 vs TT=spin-2) — **not a formal no-go**; the route is killed, not every route; frozen (Version I). (c₀=α survives only as an adopted DC normalization — that residue is an assumption, but the *boundary* is the GRUT-specific output.) |
| `arrow_of_time` | assumed | **△ plausible** | dissipation's **existence** is intrinsic (shown-grade); its **direction** is imported (Past Hypothesis, a Bin-1 primitive). GRUT *locates* the assumption; it does not derive the arrow. |
| `mu_linear` | derived-pending | **⊘ derived boundary** | the **μ=4/3 exclusion** is the established, `p_tt`-INDEPENDENT boundary (re-graded 2026-08-03: ISW-cross computed ~2.0σ + DESI Σ₀ ~3.5σ + separate-universe no-go, EdS-quantified). *Split:* the positive **μ=1=ΛCDM** prediction is **not** credited here — it rests on `p_tt_ansatz` and stays `? open`. |
| `p_tt_ansatz` | assumed | **△ plausible** | the pure-TT projector — the **load-bearing structural assumption**. *(Live correction 2026-08-02: the p_tt interrogation answered the M3 question — **CHOSEN, not forced**; "derivable from the action in principle" is now known FALSE for the declared structure; only a dynamical rung3 route survives. The V1 label stands as the frozen snapshot; see `p_tt_ansatz.boundary_condition`.)* |
| `founding_h1_zeta_casimir` | shown | **✓ standard-physics** | ζ/Casimir two-levels-of-description — textbook, **not uniquely GRUT**. |
| `founding_h2_R_zeta_bridge` | to-derive | **? open** | disfavored long-shot; the direct 1/3↔−1/12 numerology is **✗ refuted**; survives only as a frontier-reserved spectral question, *not a physical claim*. |
| `founding_h3_doubleslit_anchor` | to-derive | **? open** | deferred; analogy-only; the one steelman killed by `rung8` (wrong basis, invisible). |
| `info_i1_renorm_as_information` | shown | **✓ standard-physics** | renormalization-as-information / a-theorem monotones — standard info-RG, **already in GRUT** via rung1/2/9a. |
| `info_i2_beyond_standard_bridge` | to-derive | **✗ retracted** | screened-refuted: dissolves into standard info-RG (QFI = Kubo-Mori = FDT theorem decisive). No beyond-standard content. |
| `info_i3_distinct_consequence` | to-derive | **✗ retracted** | moot — I2 dissolved, so there is no distinct consequence to test (interpretation, not claim). |
| `l0_r1_redundancy_exists` | shown | **✓ standard-physics** | adiabatic-dilatation redundancy (Weinberg soft theorem) — generic, **not uniquely GRUT**. |
| `l0_r2_exact_unique_breaker` | to-derive | **? open** | frontier-reserved; the strong "memory = sole structure-source" **dissolves** (anomaly co-breaks; mode presupposed); exact-at-L₀→0 holds but is generic. |
| `l0_r3_payoff_mu_linear` | to-derive | **? open** | contingent on r2; does **not** graduate `mu_linear`; foundational-theorem scope (no new physics). |
| `rung7_w1_wz_map` | shown | **✓ standard-physics** | the relaxing-χ → w(z) EFT-of-dark-energy map (Gubitosi–Piazza–Vernizzi) — generic. |
| `rung7_w2_wa_sign` | to-derive | **? open** | the no-crossing is robust-but-`rung3`-gated; the wₐ **sign is open** (both over-claims — "wₐ>0 wrong" *and* "wₐ≤0 second-law-fixed" — **✗ retracted**); sourced = flat. |
| `rung7_w3_nocrossing_export` | to-derive | **? open** | the no-crossing no-go (generic/Vikman; `rung3`-gated) — a falsifiable *direction*, not a signature. |
| `method_novelty` | to-derive | **? open** | the fourth pillar's gauntlet: every component is prior art; the *synthesis* is weakly novel (freshest: AI-assisted theory-building); **"biggest contribution" over-claim ✗ retracted**; not banked — owes **independent external validation** (a different team, a different problem). |

## Tally — and the finding that falls out of it

| Label | Count |
|---|---|
| ✓ derived (novel positive prediction) | **0** |
| ⊘ derived boundary (no-go) | **4** |
| ✓ standard-physics | 9 |
| △ plausible | 2 |
| ? open | 9 |
| ✗ retracted | 2 |
| **Total** | **26** |

**Read honestly in both directions at once.** The headline stays stark and true: **✓ derived (novel positive prediction) = 0** — GRUT derives no new positive physics; its *shown* content (9) is standard physics organized under one ontology. **But the framework is not output-empty:** it establishes **4 derived boundaries** (⊘) — GW-dissipation *computed* invisible-by-suppression, the α→TT bridge and the economical-w(z) both *obstruction-backed* settled-negative (not impossibility proofs — see the calibration above), and the μ=4/3 exclusion — each GRUT-specific, each a wall a completion must respect; **three are clean of the open anchor and the economical-w(z) entry's no-crossing component is anchor-CONDITIONAL** **[CORRECTED 2026-08-10c, in the ledger's direction — this is the deposit document, and the correction reached `STATE.md` first and skipped it: THREE of the four are anchor-clean; the FOURTH is anchor-CONDITIONAL. `NO_GO_LEDGER.md` is the authority and reads: the no-crossing is "conditional on the open `rung3` (a no-go cannot outrank its anchor) — held `to-derive`." So the economical-w(z) entry's no-crossing component is NOT clean of the anchor.]** (Plus the arrow's existence/direction decomposition, a methodological boundary living inside `arrow_of_time`.) The remaining 9 open are the live frontier — including the gravitational-decoherence invisibility (`rung8`), a boundary that *would* be established **but for** its dependence on the open `rung3` super-Ohmic structure (**the bath gates the no-gos too**), and `method_novelty`, the fourth pillar's now-completed gauntlet — open because the method, screened on itself, returned "weakly-novel synthesis, not banked; owes independent external validation" (and **retracted** the "biggest contribution" over-claim). 2 are adopted assumptions; 2 retracted. Net: **zero novel positive predictions, four derived boundaries (three anchor-clean, one anchor-conditional), and a self-auditing method that screened itself and honestly declined to bank itself.** Fully consistent with [`SIGNATURE_AUDIT.md`](SIGNATURE_AUDIT.md): signature-null on *positive* signatures, while the *no-go directions* are the real content.

## The structural axis — why the survivors survived (refinement, 2026-07-02)

A second axis over the same 26 claims (no relabeling; this explains the pattern the labels already show): **every surviving positive statement is *structural*; every death was *numerical*.**

| | claims | kind |
|---|---|---|
| **Survived** | open-system ontology (`rung1`) · finite memory / constitutive physics (`rung2`, `rung4`) · the responsiveness premise · provenance / the method · form-universality (`u1`) | **structural** |
| **Died** | μ=4/3 (`mu_linear` boundary) · anomaly normalization (`rung9b`) · conformalon dark energy (`rung7_wz`) · every candidate signature (`rung4` GW, `rung8`) | **numerical** |

This is not luck — and the honest flip side must be stated: **structural claims are robust *because* they are less falsifiable.** Robustness and untestability are **one coin** here — the *same fact* as signature-null (`SIGNATURE_AUDIT.md`), seen from the other side. A structural survivor is not evidence of correctness; it is evidence that the claim doesn't stick its neck out far enough to be killed. So the structural survival is real, but it must not be re-read as vindication — it is exactly why the forward moves are foundational (F1–F3), not empirical.

## What this means, honestly

- **What survived as structure:** an ontological bet (responsive open-system vacuum), responsiveness-as-constitutive-law, finite-memory-as-premise, and a self-auditing method (whose own novelty is unscreened).
- **What survived as output:** four **derived boundaries** (⊘) — the GW-dissipation invisibility limit (computed), the α→TT-bridge and economical-w(z) settled-negatives (obstruction-backed, not impossibility proofs), and the μ=4/3 exclusion — **THREE of the four clean of the open anchor; the economical-w(z) entry's no-crossing component is anchor-CONDITIONAL** (`NO_GO_LEDGER.md`: "conditional on the open `rung3` (a no-go cannot outrank its anchor) — held `to-derive`"). Every no-go is a wall of the theory; this is the GRUT-specific content. *[This fourth site was found by the enforcement hook, not by reading — the correction had already been applied at three sites in this same file and still missed one.]* (A fifth, the decoherence invisibility, *would* qualify but is rung3-conditional — **the bath gates the no-gos too** — so it stays open.)
- **What did not survive:** any new falsifiable *positive* signature, any novel positive derivation, the ζ-numerology, the beyond-standard information principle, the conformalon *unification*, and the strong L₀-redundancy claim. (Note: the α→TT bridge and the economical-w(z) did not survive *as derivations* — but their settled-negative *results* are exactly the boundaries credited above.)
- **What is open:** the bath's pole structure (universality-probe #1) and the pure-TT projector — the two frontiers where the ledger could still move; plus the rung3-gated no-crossing/wₐ-sign, held open until their anchor resolves. *(Live mark 2026-08-03: the p_tt frontier's symmetry route has since closed — CHOSEN; its surviving rung3 route costs what it saves, so that frontier can no longer move the NET ledger. See the p_tt row correction above and `p_tt_ansatz.boundary_condition`.)*

This is the depositable Version I. The forward program — whether responsiveness can be *derived* (or is fundamental), and whether response is *universal* — is in [`GRUT_II_Agenda.md`](GRUT_II_Agenda.md). The discipline's verdict on itself: **honest, narrow, and not yet a theory of anything beyond what it borrows — pending the bath and the method's own novelty screen.**
