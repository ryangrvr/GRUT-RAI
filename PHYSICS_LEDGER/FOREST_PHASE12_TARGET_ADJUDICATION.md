# FOREST — PHASE 12: AMPLITUDE-CHANNEL TARGET ADJUDICATION

**Date:** 2026-09-04 · **Instrument:** `forest_phase12_adjudication.py` ·
**Artifact:** `FOREST_PHASE12_TARGET_ADJUDICATION.json` · **Base:** acae001.
**Battery: 44/44 (post-reconciliation).** **DECISION: `NEITHER-DISCRIMINATING`**
— corrected from the first draft's `BOTH-BLOCKED`.

**Both legs returned findings that changed this record.** Leg A: **INCONCLUSIVE** — it
caught that I carried forward the favourable half of a register fence while dropping the
half that guts candidate A's selected channel, from a string my own instrument had loaded
and gated. Leg B: **FAILED** — the decision label overstated, the outcome set was
truncated, and candidate B was mischaracterized. All corrections applied at source.
Neither candidate preselected; neither computed. No register mutation, **no target
computation launched**, no A–F selection. Scope declared: the v4 working tree. W-0.

## 2 · CANDIDATE A — Γ_T / STANDARD-SIREN AMPLITUDE

**Observable:** achromatic cosmological tensor friction Γ_T at ω∼H₀, read in the
**standard-siren amplitude** channel. **The channel conclusion is right; the SPEC's stated
mechanism is a category error I propagated unchecked.** "Achromatic, therefore degenerate
with the coalescence phase" is wrong: Γ_T is a *damping rate acting on |h|*, contributing
no phase, so it cannot be degenerate with φ_c. The **correct** reason sits in
`calc/gw_dissipation_bounds.py`: the IR pole's Re part is negligible at LIGO frequencies,
so the dephasing figure is untouched while the amplitude channel is uncovered. And my
claim that Q-D *"independently confirms"* Phase 11's fence is **withdrawn as circular** —
Phase 11's fence and Q-D trace to the same source file. One source, not two.

**Scaffolding:** a **pre-registered SPEC exists** (`calc/SPEC_gw_tensor_friction.md` —
*"Pass/fail is pre-registered below, before any result exists"*), with an owner ruling to
build; **the code does not exist.**

**Outcome set — CORRECTED.** The SPEC pre-registers **four** outcomes, not the three I
listed: PASS, FAIL-BUT-INFORMATIVE, CLOSES THE QUESTION, and **REFUSE** — *"if the sector
question cannot be settled from the booked family."* REFUSE is the outcome under which A
is **undecidable**, and I used the truncated list to certify A as "decidable." Withdrawn.

**The blocker, in the SPEC's own words (Q-A, "this dominates everything else"):** does the
τ₂ pole appear in the **P^TT** channel at all, or only in the scalar **P^(0s)** channel
that `p_tt_ansatz` excludes? If scalar-only, *"the whole friction result is zero in this
channel and the question closes."* Both horns are stated, and the SPEC's verdict on them
is explicit: **"Neither horn supports a quoted number."**

**Parameters:** B is a *staked illustrative* amplitude with **two live values ~3.2 orders
apart** — B = 0.4 → Γ_T = 0.2 H₀ (inside the few×H₀ slot bound by ~5×) versus B ~ 2.4e-4 →
Γ_T ~ 1.2e-4 H₀ (**invisible**). The SPEC orders both be reported and neither picked
silently. Identifying B with ε is *"a separate unverified assumption."*

**Standard-theory overlap — CORRECTED, and this is the phase's central repair.** The
first draft quoted the favourable half of `rung3_single_pole`'s fence ("explicitly
DISTINCT from α_M") and promoted it to *"the one real structural distinction"* — **while
omitting the half of the same string that disqualifies the selected channel.** The fence
reads in full:

> **"A detected Ξ₀ ≠ 1 could NEVER confirm GRUT and would bear on it only AFTER a
> conservative-vs-dissipative decomposition"** … α_M is *"sign-indefinite and
> slot-degenerate"* … **CATEGORY FENCE:** α_M is *"removable by field redefinition,
> graviton-number-conserving, sign-indefinite, **achromatic**, and noiseless; a genuine
> dissipative kernel is none of these."*

Three consequences, all against A as I framed it: (i) the category distinction is **real
in physical character**; (ii) **achromaticity — the property my whole channel argument
leaned on — is exactly what Γ_T *shares* with the standard-MG parameter**, not what
separates it; (iii) the separating feature is the **mandatory noise ξ**, which implies a
*different observable* (a stochastic background) in a channel **this phase did not select
and does not assess**. In the standard-siren amplitude channel there is one friction slot,
and Γ_T and α_M·H enter it identically. **For the form the overlap is severe; for the
selected observable it is total.**

The register additionally grades the dissipative Γ_T + noise **form** as **U1-GENERIC**
published open-EFT — **"NO validation credit for the form."**

## 3 · CANDIDATE B — BH QNM / RINGDOWN

**Observable:** QNM frequencies / ringdown damping times — concrete and measurable.

**The quantity IS posed — my "unposed" was wrong (Leg B).** `SIGNATURE_AUDIT.md` states
GRUT's dissipative tidal response (Im χ, `rung4`) is *"a horizon/tidal dissipation channel
that could in principle shift QNM frequencies or ringdown damping times — a place where a
dynamical (lossy) tidal response differs from GR's conservative one."* What is absent is
the **machinery**, so the quantity cannot be **computed** — not that it has not been
**posed**.

**Expected disposition, restored (I dropped it):** *"confirms invisible"* —
**invisible-by-inheritance, an inheritance argument, NOT a computation**, and per Phase 11
channel-conditional. **Governance status:** B is a **named owed calculation** in two
governance documents — `POSTULATE_MAP.md` M6 and the standing soft-spot caveat on
`SIGNATURE_AUDIT.md`'s own EMPTY verdict.

**Machinery: ABSENT.** Zero repository files mention **Kerr**, **Teukolsky**, **tidal
heating**, **Love number**, or **horizon flux**. The only Regge–Wheeler/Zerilli material is
`calc/static_patch_tt_response.py` — the **de Sitter static patch**, whose own text states
*"Every M-dependent term in it drops at M = 0."* **That is not a black hole.** There is no
BH perturbation problem in the corpus onto which a GRUT term could be added.

**History:** a prior QNM reading in this exact neighbourhood was **RETRACTED** —
*"gapped-tower ⇒ QNM (the boundary check tested the wrong thing)."*

**Ancestry:** its parent `rung4_love_kk` is itself classified **FAILS-DIFFERENTIATION**,
and per Phase 11 its "22–62 orders" is a **dephasing-branch** figure that does *not* cover
the amplitude channel a ringdown damping time lives in — so B inherits neither a
suppression argument nor an exemption from one.

## 4 · STANDARD-THEORY SUBTRACTION

**A:** the *form* is standard (published open-EFT); the *distinction from α_M* is real but
structural, not yet numerical. **B:** cannot be subtracted against a baseline, because the
GRUT-side quantity has not been posed.

## 5 · PARAMETER IDENTIFIABILITY

**A:** B — *staked*, spanning 3.2 orders; B≡ε — *unverified assumption*; the sector family
(TT-only vs two-survivor) — *unsettled*, and the SPEC notes each horn costs something.
**B:** the response function is unpinned throughout (α_g set to 1 as *most generous for
detectability*; the branch index a choice; ω_c spanning many orders in-corpus).

## 6 · FALSIFICATION TEST

**A fails as it stands:** with Q-A unanswered and B running down to *invisible*, a null is
absorbed by B → small. No "GRUT predicts X vs standard predicts Y" can be written today.
**B fails more basically:** with no BH perturbation problem in the corpus, the equation
that would differ from GR **cannot be written at all** — the Phase-11 hostile referee
issued exactly that demand and recorded it **not met**.

## 7 · EXPERIMENTAL ACCESS

Both terminate in GW-detector observables. Beyond that the repository does not establish
detector-specific sensitivity for either, and **no projected numbers are invented here**:
**UNKNOWN**.

## 10 · HEAD-TO-HEAD MATRIX

| Criterion | Γ_T amplitude (A) | BH QNM (B) |
|---|---|---|
| observable defined | YES — standard-siren amplitude | YES — ω_QNM, τ_ring |
| current calculation exists | NO (SPEC written, code absent) | NO (and no prior problem to extend) |
| GR baseline | no tensor friction | GR QNM spectrum (not in-repo) |
| standard MG overlap | **TOTAL in the selected channel** — one friction slot; Ξ₀≠1 "could NEVER confirm GRUT" without decomposition; form is U1-generic | quantity IS posed (Im χ tidal); machinery absent, so uncomputable |
| free parameters | B staked, ~3.2 orders; B≡ε unverified; sector family unsettled | response function unpinned throughout |
| nuisance degeneracy | **slot-degenerate with α_M** (the decisive one); dephasing blind because the IR pole's Re part is negligible at LIGO f — *not* phase degeneracy | QNM shifts degenerate with mass/spin in single-mode ringdown fits |
| gauge dependence | not established in-repo | not established in-repo |
| scheme dependence | sector-family choice is a declared convention fork | UNKNOWN |
| falsifiable **today** | **NO** — null absorbed by B → small | **NO** — no equation can be written |
| current data access | siren amplitude (channel identified) | ringdown (channel exists) |
| major unresolved assumptions | Q-A sector; Q-B value; Q-C B≡ε | entire BH perturbation problem |
| reason to compute | a pre-registered question with **four** outcomes incl. REFUSE — but its PASS horn does **not** open a discriminator in this channel | none until the machinery exists |

## 11 · TARGET DECISION — `NEITHER-DISCRIMINATING`

**Corrected from `BOTH-BLOCKED` (Leg B).** "Blocked" implicates a removable obstacle
behind which a target sits. Nothing establishes that implicature for either candidate, and
for A it is **contradicted by its own channel fence**: even a clean PASS returns a number
whose form earns no validation credit, in a slot where a detection *"could never confirm
GRUT."* Neither candidate survives §11's parameter and falsifiability gates.

- **A: `NOT-DISCRIMINATING-IN-THE-SELECTED-CHANNEL`.** Its equation *can* be written —
  what cannot be written is a **difference**. Slot-degenerate with α_M; B spans 3.2
  orders; four pre-registered outcomes including **REFUSE**.
- **B: `POSED-BUT-UNCOMPUTABLE`.** The quantity is posed (Im χ tidal dissipation); the BH
  perturbation machinery does not exist in the corpus; expected disposition on record is
  *"confirms invisible."*

**Why A was not selected anyway.** Selecting A would mean selecting a question whose own
SPEC states **"neither horn supports a quoted number"** — which is the Phase-10 error
exactly: choosing an unresolved question and calling it a parameter-free discriminator. I
declined to repeat it.

**The owner question, restated with its counter-case (Leg B: my first framing was "a
nomination presented as a neutral deferral" — three endorsements, zero counter-case).**
Whether to authorize A's Q-A as a **closure calculation** is an owner decision, and §11
does not empower this phase to take it. The case *against*, which I owed and omitted:
**REFUSE** is a live pre-registered outcome (A may be undecidable from the booked family);
ω_c spans **39.6 orders** in-corpus and the SPEC itself warns *"do not let an unpinned
constant enter a headline"*; the SPEC's trap 4 warns that a Γ_T landing near the slot
bound *"is to be scrutinised hardest, never celebrated"* — and the staked B = 0.4 lands
**5× inside** it; under horn 1 (TT-only) the zeroing outcome **cannot occur**, so
"valuable in either direction" is false there; and a detection in this channel **could
never confirm GRUT**. My "cheap, decidable, valuable either way" was one-sided and is
withdrawn as stated.

**One observation, recorded and deliberately NOT promoted:** the separating feature of a
genuine dissipative kernel — the **mandatory noise** — points at a *stochastic background*
observable that no phase has assessed. Naming it here is not selecting it; converting it
into a candidate is Phase-11-type mapping work under its own order.

## 12/13 · ADVERSARIAL LEGS

[[LEGS]]

## 15 · GOVERNANCE EXIT

H¹ unchanged; Phases 1–11 byte-identical; register unchanged; A–F unchanged; W-0; **no
target computation launched** (`calc/gw_tensor_friction.py` still absent); HEAD ==
origin/v4.

## W-0 STATUS — adjudicated; both blocked; nothing banked; nothing computed.
