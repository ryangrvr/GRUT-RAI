# Q3 — OBSERVABLE-ASSEMBLY PRECONDITION GATE

> **THIS IS A DESIGN / ADJUDICABILITY ARTIFACT. IT IS NOT A Q3 RESULT.**
>
> **Q3 remains OPEN** (`program/QUESTION_LEDGER.md:163`). The previous physicality gate,
> `program/gates/Q3_PHYSICAL_SCALE_BRIDGE_GATE.md`, **produced no valid verdict**: four drafts
> (**B**, **C**, **E**, **C**) each failed the two-audit protocol, and that document is stamped
> **"⛔ FAILED AUDIT — NOT A RESULT. DO NOT CITE."** Nothing here classifies Λ_R as physical or
> unphysical, and nothing here reopens that adjudication.
>
> This document answers a **prior** question: *what must exist before "is Λ_R physically
> observable?" can be adjudicated on this record?*
>
> **Scope correction (post-audit).** An earlier draft of this document framed its verdict as
> *"the question is not yet posed."* **That framing is withdrawn.** The question is very likely
> well-posed; what the record lacks is the *object the question quantifies over* and the
> *machinery to answer it in either direction*. The verdict below is therefore
> **NOT CURRENTLY ADJUDICABLE**, which is an answerability claim, not a posedness claim. The
> distinction was collapsed in the first draft and both audits caught it.

**Date:** 2026-09-08 · **Register:** untouched (74 nodes, sha256 `beaeb84e8a6f8468`) ·
**Ledger delta: 0** · W-0 held · No physics computation. No fifth classification.

---

## 1. WHY THIS GATE EXISTS

**Attribution.** The observation that the failed adjudication kept terminating at one missing
object is **the void gate's own**, recorded in its failure stamp
(`Q3_PHYSICAL_SCALE_BRIDGE_GATE.md:26-29, :36-38`). It is not originated here, and it carries no
authority from that document. What this gate contributes is the **independent** status
reconstruction of §2.1 — every row of which was verified directly against the record — which is
what actually establishes that the object is missing.

So verified independently: the graviton-probe assembly, the ρ_TT extraction, the one-clock
reduction proof, the gauge and renormalization dispatch statuses, and menu γ are each owed or
undecided (§2.1). **That** is the finding. It indicates the
proposition under adjudication is under-specified at the observable level, not that the
adjudicator was indecisive.

**Owner rulings applied (2026-09-08):**
1. **Q3 disposition remains `OPEN`.** The ledger is authoritative; a failed gate produces no
   valid disposition to apply. Two siblings assert otherwise —
   `Q3_DIMENSIONAL_TRANSMUTATION_GATE.md:181` (proposes OPEN → GATED, owner-owed) and
   `Q3_LAMBDA_PHYSICAL_CONTENT_GATE.md:191` (asserts *"Q3 remains GATED"*). Neither is applied.
2. **"Form-factor feature" is not to be defined ad hoc.** It is treated here as a
   **specification defect** and routed (§4), not repaired by interpretation.
3. **No determination of Λ_R's physicality is attempted.**

---

## 2. PHASE 1 — RECONSTRUCTION

Six record sweeps, each adversarially re-verified for phantom citations and over-classification.
**The verifiers found 11–16 citation defects and 6–9 misclassifications per sweep**, all in the
same direction: objects filed as *constructed* that are only written down. Every load-bearing
item below was then re-checked directly; items the verifiers overturned are marked.

Buckets: **constructed** = actually built (executed script, value table, banked node) ·
**schematic** = written as formula/definition, never built · **conditional** = asserted only
under a stated unmet condition · **future work** = explicitly owed.

### 2.1 The assembly chain — what exists and what does not

| Ingredient | Status | Record |
|---|---|---|
| Scalar-probe source/observer/external-leg assembly | **constructed** (external: Glavan–Miao–Prokopec–Woodard) | `SPECIALIST_BRIEF_rung3_spine.md:43` — *"the only gauge-invariant assembled observables require inserted matter"* |
| **Graviton-probe** assembly | **FUTURE WORK — explicitly does not exist** | `CLASS_C_WALL_CONTRACTS.md:22-25` — *"built for a SCALAR probe; the graviton-probe version does not exist and must be constructed (wall A)"* |
| Tier-4 contract-level retarded K_R (graviton loop) | **constructed**, banked | `PHYSICS_LEDGER/WALL_KR_CONTRACT_RETARDED_VERDICT.md:19-24`; register `kr_contract_retarded_tier4` |
| Ward-sourced noise transversality | **constructed** | `calc/RESULTS_noise_transversality.md:7-10` |
| Admissible-operator-basis enumeration | **constructed** | `calc/RESULTS_operator_basis.md:28-29` |
| TT projector | **banked as a priced INPUT**, interrogated and found **CHOSEN, not forced** | register `p_tt_ansatz` (tier `assumed`, ledger +1); `BRIEF_p_tt_interrogation.md:3` |
| ρ_TT / η — the designated observable | **FUTURE WORK** | `SPECIALIST_BRIEF_rung3_spine.md:43` — the three-step extraction *"does not yet exist"*; `DISPATCH_ONE_PAGE.md:22` gives the formula only |
| One-clock spectral reduction | **NOT GRANTED** | `CLASS_C_MANIFEST.json` (repo root), key `clock.declaration` — *"no global rho(omega) presumed; any one-clock spectral reduction requires its own proof for the assembled object"* |
| Gauge status of the dispatch | **UNDECIDED-DISPATCH** | `CLASS_C_MANIFEST.json`, key `gauge`; and `CLASS_C_WALL_CONTRACTS.md:72` — it stays so *"until the dispatched computation exists"* |
| Renormalization status of the dispatch | **UNDECIDED-DISPATCH** | `CLASS_C_MANIFEST.json` |
| Scheme-independence demonstration (menu γ) | **FUTURE WORK** | `Q3_LAMBDA_PHYSICAL_CONTENT_GATE.md:30` — *"open and never executed"* |
| Σ at O(k_ext²) | **FUTURE WORK, scope-disclosed** | `PHYSICS_LEDGER/wall_kr_tier4_retarded.py:300-301` — *"The O(k^2) dependence of Sigma was not computed at T3 (scope-disclosed)"* |

**A live tension, recorded not resolved.** `PHYSICS_LEDGER/K_R_CONTRACT_EXECUTION_CHARTER.md:25`
gives the table header `| object | is | is NOT |`, and `:33` reads
`| TT projection | strictly downstream of the full non-TT assembly (frozen A3 discipline) | an input |`
— i.e. the charter states TT projection **is not an input**, while the register banks
`p_tt_ansatz` as exactly that, priced at ledger +1. *(This is a verifier catch: the reconstruction
sweep initially read the `is NOT` column as an assertion and reported the opposite.)* Routed §7.

### 2.2 What the executed record actually contains in the analytic sector

Constructed: the **branch point at ω = 0 with a real-axis cut** (`PHYSICS_LEDGER/WALL_KR_CONTRACT_RETARDED_VERDICT.md:68-70`,
banked); the static-patch pole-free result and the retraction of the "gapped tower" reading
(`RUNG3_KEYSTONE_MAP.md:158-166`); the Matsubara ladder of the finite-T **noise** kernel
(`calc/finite_T_pole_structure.py:24-27`). Conditional or refused: the no-additional-real-axis-zero
statement, banked **as conditional** and on the reference slice only; *"NO pole claim is made"*.
Future work: the pole-vs-cut dispatch itself, and any QNM/ringdown computation
(`SIGNATURE_AUDIT.md:35`; `PHYSICS_LEDGER/FOREST_PHASE12_TARGET_ADJUDICATION.md:89-93` — machinery absent).

**No propagation observable (Δφ, v_g, QNM, ringdown) has ever been computed from the Tier-4
kernel.** Where such numbers exist they come from a different object — `calc/RESULTS_gw.md:12`
(*"it is not binding"*), `:14` (*"26–66 orders to spare"*) and `:26` (*"the effect stays 21–62
orders below threshold"*) are computed from an `Im[χ] ~ (ω/ω_c)^q` toy, not from the Tier-4
kernel. *(This claim also appears in the void gate at `Q3_PHYSICAL_SCALE_BRIDGE_GATE.md:121-123`;
it is re-derived here from the primaries above and carried on that.)*

---

## 3. PHASE 2 — THE MINIMAL MISSING OBJECT

**This section specifies structure. It does not construct an observable and does not name a
physical prediction.** Only ingredients the record itself already requires are retained.

The chain the record's own contracts impose, from source to measurable quantity:

    (1) SOURCE                  a declared, gauge-invariant source coupling for a GRAVITON probe
          |                     EXISTS for a scalar probe only.
    (2) PROBE / FIELD           the gauge-invariant field variable the response is read on
          |                     TT projection is banked as a CHOSEN input (p_tt_ansatz), and the
          |                     charter separately says it is NOT an input. Unreconciled.
    (3) RESPONSE                the two-time retarded response G_R(x,x') of the assembled system
          |                     The record's PRIMARY class-C object. Kernel-level Sigma exists;
          |                     the assembled G_R does not.
    (4) OBSERVER                observer vertex + external-mode-function corrections
          |                     EXISTS for a scalar probe only.
    (5) RENORMALIZED ASSEMBLY   the assembled object with its local sector fixed
          |                     Local slot fixed at H^0 (c0=c2=0 exact, c4 CALCULATED); the
          |                     ASSEMBLED object's renormalization is UNDECIDED-DISPATCH.
    (6) REDUCTION               one-clock reduction to a spectral density rho_TT(omega)
          |                     NOT GRANTED: "requires its own proof for the assembled object".
    (7) SCHEME TRANSFORMATION   the law by which (5)-(6) transform under admissible scheme change
          |                     Menu gamma: "open and never executed".
    (8) MEASURABLE QUANTITY     a quantity with a declared comparison to data
                                The one channel carried to a number (Gamma_T) is built from
                                Im Sigma alone and carries no scheme slot -- primary:
                                calc/RESULTS_gw_tensor_friction.md:31-32, "Im L = pi =>
                                mu-independent -- no scheme slot enters the friction".
                                (Also in the void gate at :124 and :274-275; re-derived here.)

**Links present: (3) partially, (5) partially. Links absent: (1), (2)-unreconciled, (4), (6), (7).**
Of the eight, **four are explicitly owed and one is contradicted between two authorities.**

**Necessity, correctly scoped (audit repair).** This chain is **not** a general precondition for
"a quantity compared to data" — the record refutes that reading itself. **Γ_T is computed,
priced, and compared to an observational bound** (`calc/RESULTS_gw_tensor_friction.md:34-38` for the value table and **`:40`** for the bound comparison — *"62.7 orders below the shared-slot bound few×H₀ at 100 Hz"*) **with links (1), (4), (6) and (7) undischarged.**
The chain is necessary specifically for **the designated class-C observable** — the object whose
gauge invariance and spectral reduction the record itself conditions on assembly. An earlier
draft asserted the general necessity and is corrected here.

**The minimal object.** For the sentence *"observable O depends on Λ_R"* to be **decidable** at
this scope, O must be a quantity for which links (1)–(7) are discharged. The record already names
exactly one such candidate and already names it as unbuilt:

> **ρ_TT(ω→0) = 2 Im G_R^TT(ω)**, obtained *"after (i) gauge-invariant assembly, (ii) IR
> resummation, and (iii) analytic continuation"* — `SPECIALIST_BRIEF_rung3_spine.md:43`, which
> states this three-step extraction *"does not yet exist"* and is *"the single blocking
> computation."*

**SUPERSESSION, DISCLOSED (audit catch).** That brief is dated 2026-08-12. A **later, live**
document supersedes its *priority*: `STATE.md:113` reads **"`rung3`'s forward move is no longer
the arXiv:2602.07908 specialist computation"**, redirecting the program's forward move to a
different, sharper question (*does the projected memory kernel inherit the Matsubara ladder?*).

**What this does and does not change.** It does **not** change the status of the assembled
observable — it remains unbuilt, and §2.1's rows stand. It **does** mean this gate must not
present the assembly as *the program's current forward priority*; it is the precondition for
**this specific question**, not the record's live next step. Any owner decision to fund the
assembly is therefore a decision to **re-prioritise against `STATE.md:113`**, and is flagged as
such rather than smuggled in as continuity.

**No new object is proposed here.** The precondition is the record's own named blocking
computation, plus §4's specification repair and §5's criterion gap.

---

## 4. PHASE 3 — "FORM-FACTOR FEATURE": TERMINOLOGY AUDIT

### 4.1 Findings (machine-verified this gate)

- **Exactly 5 occurrences repo-wide.** No plural forms; zero in `books/`, `docs/`, `GLOSSARY.md`,
  the register, or any `calc/` script; zero in the `release/` duplicates.
- **Four of the five are inside the void artifact** `Q3_PHYSICAL_SCALE_BRIDGE_GATE.md` (its
  failure stamp, its screen table, its decision tree, its re-quotation) and carry no authority.
- **The single live occurrence** is `Q3_LAMBDA_PHYSICAL_CONTENT_GATE.md:183`, as an **exclusion
  clause inside standing reopening condition (iii)**:

  > *"**(iii)** any observable — not a form-factor feature — shown to depend on Λ_R"*

- **It is never defined** — not in the live gate, not in the glossary, not in the register, not in
  any charter or calc. `git log -S "form-factor feature" --all` returns **one** commit (42ad402).
  It entered the record already undefined. **No document owes a definition.**
- **The posedness tension is stated by the record itself.** The same sentence that carries (iii)
  introduces the list as *"**Exact reopening conditions**, each externally decidable"*
  (`:180`). A condition containing an undefined exclusion term is not externally decidable.

### 4.2 A provenance defect found while auditing the term

The void gate justified applying (iii) by asserting that *the register* types the response's
coefficients as form factors. **It does not.** `provenance/claims.json` uses "form factor" exactly
twice — at `:319` (the FRW-frame component count, *"5 independent form factors"*) and `:865`
(`x_anom(k)`). The c₀/c₂ line at `:920` writes `K_R = c2(omega,k^2)*P2 + c0(omega,k^2)*P0s` and
**does not contain the phrase**. The typing of c₀/c₂ as "form factors" originates in a *gate*
(`Q3_DIMENSIONAL_TRANSMUTATION_GATE.md:103`), not in the register. **The attribution is a
misattribution and is recorded as such.** No consequence is drawn from it here.

### 4.3 Proposed specification repair — a menu, deliberately unselected

**No replacement is chosen.** Per the ruling, the repair is routed. What follows is the set of
mutually distinguishable operational criteria the record's own vocabulary already supports, so the
owner can select — or reject all — without this gate deciding the scientific outcome.

| # | Candidate operational criterion | Mechanically testable? | Record support |
|---|---|---|---|
| R1 | **Momentum/frequency dependence.** A quantity is form-factor-like iff it is a non-constant function of (ω, k²). | Yes | The record's only machine-enforced sense: mutant `form_factor_loses_k_squared_scaling` (`provenance/mutation_registry.py:294-298`); `S_IF.md:90-96` declares x *a kernel, not a constant* |
| R2 | **Kernel-level vs assembled.** Form-factor-like iff it is a coefficient of the un-assembled kernel rather than an output of the discharged assembly chain (§3). | Yes, once §3 exists | `CLASS_C_WALL_CONTRACTS.md:41` — *"Only the FULLY ASSEMBLED observable"* is expected gauge-invariant |
| R3 | **Feature-of vs function-itself.** Form-factor *feature* = a located property (a zero, a pole, a sign change, a threshold) of a response function, as against the response function itself. | Yes | Fits (iii)'s drafting context: the sibling had just refuted the *zero of Re Σ*, literally a located feature |
| R4 | **Gauge/scheme status.** Form-factor-like iff its value is not invariant under the admissible gauge and scheme transformations. | Partly, now — see note | **NOTE (propagated from §6.1):** the source here, `CLASS_C_WALL_CONTRACTS.md:103-108`, is **not** merely a menu candidate. It is a **live, stated, mechanical criterion** of the record, and §6.1 treats it as such. It is retained in this table only to show the shape a terminology repair could take; **selecting or rejecting R4 does not affect that criterion's standing**, which is independent of this menu |
| R5 | **Strike the clause.** Remove the exclusion and let (iii) rest on "observable", once "observable" itself has a criterion (§5). | Yes | Removes one undefined term but exposes the deeper one |

**A mechanical consequence the owner should see before selecting — attributed, and corrected.**
This consequence is **not original here**: the void gate's failure stamp records it
(`Q3_PHYSICAL_SCALE_BRIDGE_GATE.md:36-38`), applied there to its own reopening condition. It is
restated only because it was re-verified against `Q3_LAMBDA_PHYSICAL_CONTENT_GATE.md:183`
directly, and it is carried on that re-verification rather than on the void gate's authority.

**Corrected scope of the consequence.** Under **R1** — any non-constant function of (ω, k²) —
the excluded class contains **ρ_TT = 2 Im G_R^TT**, the record's designated Class-C observable,
making (iii) unsatisfiable by the very object designated to satisfy it. **It does NOT follow
under R3 as R3 is written**: R3 excludes a *located property* (a zero, a pole, a sign change) **as
against the response function itself**, and ρ_TT *is* the response function, so R3 leaves it
admissible. A prior draft invented a "broad R3" to extend the reductio; that was a defect and is
withdrawn. Under **R2**, (iii) becomes satisfiable exactly when §3's chain is discharged.

**This is reported as a consequence of readings, not as an argument for any of them.** R2 is not
recommended here; R3's survival of the reductio is stated precisely so the menu is not decided by
the framing.

### 4.4 The record can write such a clause — it simply never did here

`books/BOOK_IX_TESTS_PREDICTIONS.md:84-88` defines *"What counts as a prediction"* with a five-part
operational test and an explicit word-policing clause (*"Nothing else may carry the word"*). The
capacity is demonstrated. No counterpart exists for **"observable"** or for **"form-factor
feature."**

---

## 5. PHASE 4 — WHAT A REDUNDANCY / FIELD-REDEFINITION CLAIM REQUIRES

**No demonstration is performed here.** This section lists the required inputs and classifies each.

### 5.1 The vocabulary is absent from the record

Machine-verified repo-wide, including `release/`:

    "redundant operator"                      -> 0 occurrences
    "EOM-proportional"                        -> 0 occurrences
    "proportional to the equations of motion" -> 0 occurrences

**These are PHRASE counts, and phrase-absence is not concept-absence.** An earlier draft inferred
from these zeros that "the record contains no redundancy vocabulary at all" and that a redundancy
claim "cannot be stated." **Both inferences are false and are withdrawn.** The concept is present
and operative on GRUT objects: `AGENT_COORDINATION.md:3515` derives a term marked **"-- PURE
EoM"**, and `:3518` reads *"The EoM terms collapse propagators (tadpole-class => LOCAL per V4)"*.
The record also states removability directly, in the α_M locus of §5.2.

**What the counts do establish, and only this:** the program has **no standardized, glossary-level
term** for operator redundancy, so redundancy arguments here are conducted ad hoc, in locally
invented wording, without a shared predicate to check them against. That is a terminology gap
(§7 item 12), not an absence of the idea.

### 5.2 The one place the record does discuss removability

Exactly one non-void locus, and it is **not about a GRUT object**: `SIGNATURE_AUDIT.md:60` fences
**α_M** (running Planck mass) as coming *"from a Hermitian action: removable by field redefinition,
graviton-number-conserving, sign-indefinite …, achromatic, and noiseless"*, with *"A genuine
dissipative Im Σ_R is none of those."* Mirrored at `books/BOOK_IV:471-472` and register node at
`provenance/claims.json:80`. **It is an imported category fence, not a removal performed on
anything in this program.**

### 5.3 Required inputs, and their status

| Input a redundancy claim needs | Status |
|---|---|
| An **on-shell / assembled** observable to be invariant *of* | **ABSENT** — §3, links (1)(4)(6) |
| **Source-vertex** transformation | **ABSENT** for the graviton probe |
| **Observer-vertex** transformation | **ABSENT** for the graviton probe |
| The **equations of motion** at the working order, and the operator's relation to them | **PARTIAL/BLOCKED** — the ω⁴ carrier is attributed to the *Ricci²/Riemann² classes* (`PHYSICS_LEDGER/WALL_KR_D5_RENORMALIZATION_AUDIT.md:79-84`); *(that these classes are not interchangeable for a redundancy argument, and that O(k_ext²) is the datum separating them, are **this gate's own inferences, not record statements** — flagged as originated and owed their own verification)*; **Σ at O(k_ext²) was never computed** (`wall_kr_tier4_retarded.py:300-301`) |
| **Locality / covariance** licence | **OWED, and narrowly scoped.** *(This scoping analysis appears in the void gate's §4, which its own stamp voids in full; it is re-derived here directly from the two sources and carried on that, not on the void gate.)* F7 (`PHYSICS_LEDGER/WALL_A_A3_DECLARATIONS.md:62-67`) bars citing regulator symmetry as evidence — but **only** *"in the wall-question (i) placement verdict"*. The D5 `CONDITIONAL` (`:84-88`) governs **the H² linkage of (c0p, c2p)**, not the ω⁴-slot identification. Both were mis-scoped in the failed drafts, in opposite directions |
| **Order in perturbation theory** — what the redefinition induces at next order | **UNSPECIFIED.** *This status is the **sixth** import from the void gate (see §9)* (`Q3_PHYSICAL_SCALE_BRIDGE_GATE.md:24-25` — *"Absorbing it requires next-order counterterm structure the record does not have"*), **attributed here rather than asserted**. This gate does **not** independently establish it; it is carried as the void gate's claim and is flagged as needing its own verification before any weight is placed on it |
| **Freedom to choose a finite local constant** | **BARRED.** `PHYSICS_LEDGER/WALL_KR_D5_EXECUTION_VERDICT.md:11-12` — *"THE SCHEME MAY BE DECLARED. THE FINITE LOCAL NUMBERS MAY ONLY BE CALCULATED."* A demonstration that adjusts a finite slot constant is not licensed |

**Six of seven inputs are absent, blocked, owed, or barred.** A redundancy claim — in either
direction — is not currently constructible from this record.

### 5.4 The distinction the failed drafts collapsed

**Parameter redefinition** (re-expressing (μ, c₄) as Λ_R — an exact reparameterization;
`PHYSICS_LEDGER/WALL_KR_MU_OWNER_DECISION_PACKAGE.md:57-60` gives the shift law and the redundancy statement,
and `:62` carries the invariant stamped *"RG-invariant (gated)"*. It is **not banked** — that
document's own `:8` reads *"W-0: computed-and-reported, NOT banked. HARD STOP."*) is **not** **physical field redefinition** (a change
of variables on h acting on action, source and observer together). The first is established. The
second requires §5.3. Any future gate must keep them apart on the face of the argument.

---

## 6. PHASE 5 — ADJUDICABILITY

**Question under test:** *"Does a physical observable change when Λ_R changes?"*

> ### **VERDICT: NOT CURRENTLY ADJUDICABLE ON THIS RECORD.**
>
> **Not** *"the question is ill-posed."* That framing appeared in the first draft and is
> **withdrawn**: three of its four supporting legs were answerability arguments, which the same
> section then disclaimed. The question is very likely well-posed. It cannot be *answered*, in
> either direction, from what the record currently contains.

| # | Item | Kind | Status |
|---|---|---|---|
| 1 | Sharpness of the predicate *physical observable* at contract scope | **posedness-adjacent** | **PARTIAL, not absent** — see 6.1 |
| 2 | The one designated observable is unbuilt, and its spectral reduction ungranted | **answerability** | §2.1 |
| 3 | The standing reopening condition (iii) carries an undefined exclusion term | **specification defect** — and in a *different* sentence than the question under test | §4 |
| 4 | The negative demonstration is not constructible: six of seven inputs absent, blocked, owed or barred | **answerability** | §5.3 |

### 6.1 Correction: the record does supply criteria

An earlier draft claimed the record has *no* operational criterion for "physical observable."
**That is too strong and is withdrawn.** Two exist:

- `GLOSSARY.md:15` states a test in operational form — two response functionals are equivalent
  ***"iff no admissible experiment distinguishes their transport"*** — and `:17` flags the entry
  for sharpening under u5/u6. **Flagged for sharpening is not absent.**
- `CLASS_C_WALL_CONTRACTS.md:103-108` states a **mechanical** criterion, and it is the sharpest
  thing in the record on this question: the existence and classification of the low-frequency
  structure *"is required to be scheme-independent for the result to be physical — because these
  are nonanalytic-in-ω structures, and analytic (local/contact) redefinitions cannot move them
  without changing the theory's observable content. Amplitudes and local pieces MAY be
  scheme-dependent."*

The first draft demoted this second criterion to a menu option (§4.3 R4) and cited only its
rationale clause. **It is not a menu option; it is a live, stated criterion**, and any future
adjudication must engage it directly rather than route around it.

The residual gap is therefore **applicability, not existence**. Both criteria are stated over an
assembled object (`CLASS_C_WALL_CONTRACTS.md:103` scopes its criterion to *"the low-frequency
structure"* of the class-C object; `GLOSSARY.md:8` scopes its test to *"response functionals
χ(ω,k)"*), and the assembled object does not exist (item 2). **This inapplicability is a
consequence of item 2, not an independent finding, and it is not a reason to set the criteria
aside** — a future adjudication must apply them to whatever object it constructs.

### 6.2 The standing negative already on the record — cited, not adopted

An earlier draft cited `Q3_LAMBDA_PHYSICAL_CONTENT_GATE.md` four times without citing what that
**live, non-void** gate books about the question under test. That omission is repaired here:

> `:160-161` — *"**Observable invariance: no candidate exists**, and the one nominated was
> definitional (§4). That is the gate's sharpest negative and it is **evidential, not graded**."*
> `:165-166` — *"no observable is known to depend on Λ_R at all."*

This gate **neither adopts nor contests** that finding — doing either would be the physicality
determination the owner ruling forbids. It is recorded because a precondition inventory that omits
the record's own standing negative is not neutral. Note also its form: `:165` is **epistemic**
(*"no observable is **known** to depend"*), which is consistent with this gate's item 2 and does
not by itself settle anything.

### 6.3 What this is and is not

**Is:** the question cannot be answered from the present record, and §§3, 5, 7 inventory exactly
what is missing. **Is not:** any claim that Λ_R is physical, that it is unphysical, that the
question is ill-posed, or that it is permanently unanswerable.

## 7. PHASE 6 — ROUTING

Nothing below is executed here.

| # | Missing ingredient | Class |
|---|---|---|
| 1 | **Sharpening** the *physical observable* predicate to applicability (two criteria exist — §6.1) | **SPECIFICATION GAP** |
| 2 | Definition or removal of "form-factor feature" in reopening condition (iii) | **SPECIFICATION GAP** |
| 3 | Charter-vs-register contradiction on TT projection as an input (§2.1) | **SPECIFICATION GAP** |
| 4 | Misattribution of the c₀/c₂ "form factor" typing to the register (§4.2) | **SPECIFICATION GAP** |
| 5 | Q3 disposition discrepancy: ledger `OPEN` vs `Q3_LAMBDA…:191` "GATED" | **SPECIFICATION GAP** |
| 6 | Graviton-probe source / observer / external-mode-function assembly | **FRONTIER-RESERVED** — the record's own named blocking computation |
| 7 | One-clock spectral reduction proof for the assembled object | **FRONTIER-RESERVED** |
| 8 | Σ at O(k_ext²) | **IN-HOUSE AVAILABLE** — scope-disclosed omission, not a frontier problem |
| 9 | Menu γ — scheme-independence demonstration for the local slot | **IN-HOUSE AVAILABLE** — the frozen PV cross-check pattern already exists |
| 10 | Next-order counterterm structure for induced terms (§5.3) | **UNRESOLVED** |
| 11 | A numerical μ / Λ_R declaration | **NEW EMPIRICAL INPUT** — `PHYSICS_LEDGER/WALL_KR_MU_CONVENTION_RULING.md:75-77`, *"a new free input"*; :86-88, *"priced as a new register input"*. Not to be adopted silently |
| 12 | A standardized redundancy predicate (the concept is used ad hoc — §5.1) | **SPECIFICATION GAP** |
| 13 | Band tension: Tier-4 validity is ω ≫ H (register `kr_contract_retarded_tier4`, field `statement`: *"Validity: omega >> H … omega << H refused by the evaluator"*); the designated object is defined at ω → 0 | **UNRESOLVED** |

**Items 1–5 and 12 are specification repairs**: cheap, owner-decidable, and none requires physics.
**Items 8–9 are in-house.** Only **6–7** are genuine frontier work.

---

## 8. PHASE 7 — MINIMUM Q3 REOPENING CONDITION

Not *"compute more."* Stated as **necessary conditions only** — an earlier draft attached a
sufficiency claim, which contradicted its own item 4 and is **withdrawn** (see 8.1).

> **The object:** the **gauge-invariantly assembled, renormalized, pure-graviton TT retarded
> response** — source vertex, observer vertex and external-mode-function corrections constructed
> for a **graviton** probe — **together with the proof that licenses its one-clock reduction** to
> a spectral density ρ_TT(ω).
>
> That is: §3 links **(1)**, **(4)**, **(6)** discharged, with **(2)** reconciled and **(7)**
> executed.

**Evaluation region — corrected.** The first draft additionally demanded evaluation *"inside the
declared band ω ≫ H."* **That requirement is withdrawn as inflationary**: the designated object is
defined *at* ω → 0 (`CLASS_C_WALL_CONTRACTS.md:18` — `rho_TT(w->0) = 2 Im G_R^TT(w)`, `eta = lim
Im G_R^TT / w`), and `SPECIALIST_BRIEF_rung3_spine.md:43` makes *"analytic continuation to ω→0"*
the third step of the extraction. Demanding the object be delivered in a band it is not defined in
would make reopening harder than the record itself requires. The band question — that the Tier-4
kernel's own validity is ω ≫ H (register `kr_contract_retarded_tier4`, field `statement`) — is a **live tension between the kernel and the designated
object**, and it is routed (§7 item 13), not imposed as a bar.

**Two specification repairs are additionally necessary**, neither requiring computation:

- **(a)** sharpening the predicate *physical observable* to the point of applicability against an
  assembled object — noting that two criteria already exist (§6.1), so this is sharpening, not
  invention;
- **(b)** resolution of *"form-factor feature"* in reopening condition (iii) — selection from §4.3
  or removal of the clause (§4).

### 8.1 Sufficiency is NOT claimed

With the object above plus (a) and (b), items 1–3 of §6 are discharged. **Item 4 is not.** The
negative direction additionally requires §7 item 10 (next-order counterterm structure,
**UNRESOLVED**) and item 12 (a standardized redundancy predicate, **SPECIFICATION GAP**). Until
those land, a *positive* answer becomes reachable while a *negative* one may not — an asymmetry
this gate records and does not resolve.

## 9. METHOD AND DISCLOSURE

**Reconstruction method.** Six parallel record sweeps, each re-checked by an independent
adversarial verifier tasked to find phantom citations and over-classification. The verifiers
returned 11–16 citation defects and 6–9 misclassifications per sweep — uniformly in the
over-claiming direction — including one sweep that read a table's `is NOT` column as an assertion
and reported a charter as saying the opposite of what it says (§2.1). **No sweep finding was
adopted without direct re-verification**; the machine counts in §4.1, §4.2 and §5.1 were re-run
here.

**Scope held.** No physics computation. No numerical experiment. No fifth classification. No
definition supplied for any undefined term. `Q1`, `Q2`, `Q2-SY`, `Q2-BRIDGE` untouched. The register
is untouched and the ledger is unmodified: **Q3 remains OPEN.**

**On the failed gate — corrected disclosure.** A first draft claimed this document cites the void
gate **only** to record what it claimed and that it failed. **That was false**, and both audits
caught it: **six** passages took load-bearing content from it. **Five** are explicitly attributed **and
independently re-derived from primary sources**: the convergence observation (§1), the (iii)
unsatisfiability consequence (§4.3), the F7/D5 scoping analysis (§5.3), the propagation-observable
negative (§2.2, re-derived from `calc/RESULTS_gw.md:12,:14,:26`), and Γ_T's scheme-blindness
(§3 link 8, re-derived from `calc/RESULTS_gw_tensor_friction.md:31-32`). The **sixth**, the
next-order-counterterm status in §5.3's last row, is attributed but **NOT** independently
re-derived; it is carried explicitly as the void gate's claim and flagged as unverified.

**This count was wrong twice before reaching six** — stated as "three" in the first draft, then
corrected to "four" in the second, each time inside the paragraph whose purpose is to disclose
exactly this dependency. Both errors were caught by audit, not by self-review, and the sequence is
recorded rather than presented as a single clean correction. The detection method that found
imports five and six — for each distinctive claim, grep the repo and check whether its only
non-target home is the void gate — is recorded here as the reusable check.

Its four drafts remain void; its §4 removability argument, screen table and classification carry no
weight here. Its stamp records that the two audits split over draft 4 (AUDIT A: physics earned,
provenance failed; AUDIT B: classification E) **and adjudicates that split** to *"removability is
PLAUSIBLE AND NOT ESTABLISHED"* (`Q3_PHYSICAL_SCALE_BRIDGE_GATE.md:9-11, :31`) — an adjudication
this gate neither adopts nor reopens. A first draft stated the split was left unresolved; that was
false against the record and is corrected.

**Standing lesson, recorded.** The four-draft cycle B → C → E → C was not indecision. Each draft
reached a verdict before the structure was derived, and the structure could not be derived because
**the object the verdict quantifies over does not exist.** The recurring failure shape logged
elsewhere in this program — *a gate whose identity is definitional proves nothing* — appeared here
in a new form: **a gate whose quantifier has no domain decides nothing.**
