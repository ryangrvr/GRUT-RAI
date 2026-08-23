> **NOT YET SEALED — filed 2026-08-23 pending THREE owner adjudications (§3.7).**
> Deliberately NOT placed in `provenance/prereg/`: that directory is immutable-once-sealed, and
> this document is not sealed. Sealing is the owner's act, not either agent's. Until then it is a
> draft and may not be cited as content.
>
> Authored by seven INDEPENDENT branch agents who could not see each other, precisely so no single
> pass could give the favourable outcomes more care than the adverse ones, then symmetry-audited
> and corrected. `claims.json` untouched throughout.

# The Class-C consequence map — sealed before the result

> **STATUS: SEALED-BEFORE-RESULT. NOTHING BANKED. NOT A PREDICTION.**
>
> This document writes out, for each of the seven permitted Class-C outcomes, exactly what that
> outcome would mean for this register — the tier moves, the ledger consequences, the things it
> would *not* buy, the ways it could be misread, the conditions that would kill it, and an honest
> prior — **before any Class-C result exists**. Its entire value is that the interpretation was
> fixed in advance. It is the same instrument as the termination pre-registration
> (`provenance/prereg/PREREG_TERMINATION_V4_2026-08-10.txt`), pointed at the keystone.
>
> **It banks nothing.** No tier moves, no `ledger_delta` changes, no `sub_status` marker is
> applied by this file. `provenance/claims.json` is untouched. Every register move written below
> is a **candidate for the bank gate**, requiring adversarial pre-screen (CHARTER §1.3) and
> overseer relay (CHARTER §5.3) before it may enter the register.
>
> **It may not be cited as content** by any other artifact — the same fence
> `CLASS_C_DISPATCH_SPEC.md` §7 puts on its own draft language: *"neither may be cited as content
> until banked."*
>
> **NO OUTCOME IS PREFERRED.** The freeze certificate is explicit
> (`CLASS_C_DISPATCH_FROZEN.md`): *"No outcome is preferred; none may be promoted without the
> four-lens screen and bank gate,"* and *"The first class-C result is a DISCOVERY RESULT about the
> assembled gravitational response. It is not a GRUT result and carries no favour."* Writing out a
> favourable branch in detail is not evidence for it; §4 of this document says so on its face.
>
> **No net ledger figure is typed anywhere in this document** (`PUBLIC_NUMBERS.md` rule: nets and
> counts ride `validate.py` / `emit_public_numbers.py` on their own faces). Per-node deltas are
> quoted from the register; nets are not.
>
> **Marking convention.** Text in quotation marks with a file reference is verbatim from the
> repository at HEAD `d006d01`. Paragraphs marked **[INFERENCE]** are constructed by this document
> from cited inputs and are established by nothing.

---

## Section 0 — What is being asked, and against what

### 0.1 The object

`CLASS_C_WALL_CONTRACTS.md` §D4-Q1, verbatim:

> "The gauge-invariantly assembled retarded TT response of the PURE-graviton de Sitter
> self-energy: `rho_TT(w->0) = 2 Im G_R^TT(w), eta = lim Im G_R^TT / w`"

obtained after (i) Schwinger–Keldysh conversion to the retarded object, (ii) gauge-invariant
assembly of source vertex + observer vertex + external-mode-function corrections, (iii) IR
resummation, (iv) continuation to ω → 0. Background: de Sitter, **declared patch flat FLRW**
(`CLASS_C_MANIFEST.json`). State: Bunch-Davies. Content: pure graviton, no matter. Declared order:
O(G²), with the manifest's own on-face caveat that *"whether O(G^2) is actually the first nonzero
order FOR GRAVITON loops is UNESTABLISHED."*

### 0.2 What rung 3 actually asserts — verbatim, because every branch is scored against this

`provenance/claims.json`, `rung3_single_pole.statement`, in full:

> "Committing to relativistic massless fast modes (omega=c|k|) gives DOS~omega^2, J(omega)~omega^3
> (s=3 super-Ohmic); WITHIN the collisional/analytic-bath regime, and PROVIDED the vacuum bath
> carries no second internal dynamical scale, super-Ohmic baths are short-memory and the
> Mori-Zwanzig kernel collapses to single-pole / Markovian-like. Whether GRUT's vacuum IS in that
> regime (pole vs branch-cut) is the open anchor question -- see boundary_condition."

Tier `derived-pending`; `ledger_delta` **0**; `ledger_note`: *"The -1 'derived' credit stays
SUSPENDED (single-pole not cleanly derived) but is NOT a +1 cost either: it is genuinely open."*

**Four features of that sentence are load-bearing, and all four are already flagged in the register
itself:**

1. **Its antecedent is dead and is a prohibited input here.** `J(ω) ∼ ω³` is falsified at class A
   as a *"zero-temperature flat-space artifact"* (`calc/RESULTS_worldline_reduction.md`), and is
   prohibition #1 of the dispatch: *"No J(ω) ∼ ω³ — falsified at class A; importing it anywhere is
   laundering"* (`CLASS_C_DISPATCH_SPEC.md` §4). **The statement's own premise may not be used
   inside the test that scores it.**
2. **"the Mori-Zwanzig kernel" denotes no unique object.** From the node's own `tier_note`: *"the
   phrase 'the Mori-Zwanzig kernel' in this node's own statement DOES NOT DENOTE A UNIQUE OBJECT,
   and the two objects it could denote answer the inheritance question OPPOSITELY."* Repair is
   listed as near-term deliverable #2 in `RUNG3_KEYSTONE_MAP.md` §9 and is **still undone**.
3. **"single-pole" names a single rate that does not exist at free level.** `tier_note`: *"This
   node asserts *the* memory time; the free theory supplies a family indexed by l. SINGLE-POLE IS
   NOT BADLY DOMINATED HERE -- IT NAMES A SINGLE RATE THAT DOES NOT EXIST AT FREE LEVEL."*
4. **The question has been formally renamed for class C.** `CLASS_C_DISPATCH_SPEC.md` §1: *"Does
   the fully assembled class-C gravitational response contain a physically defined low-frequency
   relaxation structure that survives removal of the class-A regulator/epoch artifacts?"* — with
   the criterion *"∂τ_phys/∂k_min = 0 and no arbitrary epoch/window parameter remains… Anything
   whose value tracks k_min or the epoch window is a priced input, not a result."*

Also binding on scoring: the decision is *"a one-bit low-omega scaling CLASS read off a FULL
transport self-energy calc"*; and *"Everything that bears on this node rests on the interacting
self-energy Sigma."*

### 0.3 The seven outcomes, and the package discrepancy this map surfaces without resolving

The immutable certificate lists **seven** slash-separated tokens. `CLASS_C_DISPATCH_SPEC.md` §6 and
`CLASS_C_MANIFEST.json.permitted_outcome_classes` register **six** classes. Mapping:

| this map | certificate token | registered class (spec §6 / manifest) |
|---|---|---|
| **1** | isolated pole | 1. Pole |
| **2** | multiple poles | 2. Multiple poles / **ladder** |
| **3** | branch cut | 3. Branch cut / continuum *(one class)* |
| **4** | continuum | 3. Branch cut / continuum *(same class)* |
| **5** | secular or nonstationary memory | 4. Secular / nonstationary memory |
| **6** | no long-memory structure | 5. No long-memory structure |
| **7** | ill-posed even after assembly | 6. Ill-posed even after assembly |

**Consequences that bind every reader of this map.** Outcomes 3 and 4 are **halves of one banked
class**; neither may be filed as though it owned a separately-registered outcome. Outcome 2's
banked name includes the word *ladder*, which appears only in the spec and manifest. And **a result
banked against "outcome 7" is banked against a class number the machine-readable face does not
carry** — a provenance defect waiting to happen.

**Second discrepancy, also surfaced not resolved.** The immutable certificate records `clock`,
`boundary_conditions`, `approximation_order` as `UNDECIDED-DISPATCH`; live manifest v1.1 has since
moved all three (D1/D2/D3). `gauge` and `renormalization` remain undecided on both faces. The
certificate is immutable by its own terms; v1.1 supersedes by versioning. **Owner adjudication is
owed on which face a result answers.**

### 0.4 The one translation everyone must make, made once here

`CLASS_C_DISPATCH_DECISIONS.md` D1 records, before any result existed:

> "outcome classes 4 (secular/nonstationary) and 6 (ill-posed even after assembly) become
> **structurally likely paths**; the pole/cut question may be unreachable without the epoch-window
> input priced at W* < 0.25 e-folds."

Those numbers are the **spec's six-class numbering**. In this map's seven-token numbering they are
**outcomes 5 and 7**. Anyone quoting "classes 4 and 6" against this map's numbering points the
register's own pre-written expectation at the wrong branches. This sentence is not a preference and
not mine to argue down from inside any branch that benefits.

---

## Section 1 — The standing facts every branch inherits

### 1.1 The class-A pair — what is already computed, and how it is fenced

**Fact A — the scalar worldline proxy has a horizon-forced WHITE FLOOR, fenced both ways.**
`calc/RESULTS_worldline_reduction.md`: *"finite horizon-forced floor: the temperature is rung2-fixed
(T = T_dS), not optional… folded bilinear noise: s_eff(low-w) → ~0, against the registered 3;
therefore the registered premise J(ω) ∼ ω³ does not survive the only reduction whose clock is
licensed."* And, in the same file, the fence in the other direction: *"this is **not** pro-GRUT
either. A white floor is zero-memory, contradicting the FINITE-memory claim as much as it
contradicts s = 3."* Both simple closed forms for the low-ω shape were **falsified** at w = 0.1.
Scope fence on its face: *"Does not touch class C; wall (A)–(C) of the dispatch stand."*

**Fact B — the TT channel is NON-STATIONARY; the spectral question is not posed there.**
`calc/RESULTS_tt_worldline.md`: normalized kernel shapes at three epochs differ by up to **134%**,
*"including a change of character (oscillatory-sign vs monotone-decay)"*, while *"the
conformal-scalar PROXY was exactly stationary along the same geodesic."* Consequence, verbatim:
*"the registered class-A-style spectral analysis (ω-spectrum, pole-vs-cut, single-pole) cannot be
POSED for the gravitational channel without an epoch-window approximation whose validity must itself
be priced."* Stationarity holds only for **W < 0.25 e-folds**; the adverse proxy floor *"neither
transfers nor is refuted — it is **surpassed**."* Two priced dependencies, previously conflated and
now separated: *"The regulator prices the NOISE LEVEL, not the decorrelation time; the EPOCH prices
the decorrelation time"* (amplitude 2.3× across k_min ∈ [0.25, 1.0]).

### 1.2 The free response is POLE-FREE, and the ladder belongs to the STATE

**E4 (retracted-and-corrected 2026-08-19):** *"these frequencies are NOT established as quasinormal…
The free retarded response is pole-free (pure dS is a trivial scattering problem whose amplitude is a
finite Blaschke product). Status: null, not adverse."*

**E5:** *"Zeros, not poles… What survives is an infinite family indexed by multipole, lowest rate
(l+1)H."*

**E6:** *"The ladder is the STATE'S, not the dynamics'. coth(ω/2T) has simple poles at ω_n = −2πinT
with uniform residue 2T = H/π, present for ANY J and any contour-closable regulator… a retarded pole
is a property of THE DYNAMICS and must lie in the lower half plane. Different objects."*

**E8:** *"FREE LADDER ≠ EFFECTIVE SINGLE POLE. No parameter separates the leading term from the rest
(gap and spacing both O(H); ratio O(1), no small quantity). Separation comes only by WAITING…never
by a parametric limit."*

**D4 (the clock price):** *"with HT = e^{Ht} (axis…), e^{−Γt} = (HT)^{−Γ/H} — a **power law in T**,
not an exponential… **Any comparison of rates across more than O(1/H) of elapsed time is
clock-dependent.**"*

**The common floor this creates.** [INFERENCE, from E4 + the register's `G_R = 1/(G0^-1 - Sigma)`]
`G0⁻¹` alone is pole-free. **Every one of the seven shapes must therefore be manufactured by Σ, not
inherited.** No branch gets a free-level head start, and the branch that claims one has crossed a
fence. Additionally, from Fact B: outcomes 1–4 require Σ to *also* make a stationary reduction
exist, which is a **second, separate burden** — *"Each arrow is a separate gated step. An arrow may
FAIL, and failure is a result."*

### 1.3 The three walls, and what each does to the credibility of an arriving result

**WALL A — no graviton-probe assembly exists.** *"arXiv:2602.07908… constructs the assembly for a
**scalar probe**; the gravitational version changes the vertex rules, the reduction identities, and
plausibly the diagram count. **The scalar result cannot be borrowed.**"* Required and absent:
*"source-vertex correction diagrams, observer-vertex correction diagrams, and external graviton-
mode-function correction diagrams — none of which exist in the published corpus for a graviton
probe."*
→ **Wall A gates the EXISTENCE of the object, not its accuracy.** A result without the assembly is
not about the registered object at all; a result *with* one carries that construction's own
unreviewed status as a ceiling on its credibility.

**WALL B — the resummation tool is half-discharged.** The `h_μ0` untangling half was completed; *"the
**RG half was not** (`renormalization group` occurs zero times in its 24 pages; authors 'enjoin
caution')… so **the verdict cannot be read off the gauge-fixed object**."*
→ **Wall B makes gauge-invariance a precondition of reading any verdict at all**, not a robustness
check appended afterwards. Hence the mandatory dual-gauge test, whose acceptance is frozen: *"the
classification outcome (pole/cut/ladder/secular/none) must AGREE between gauges… A classification
disagreement is a structural finding about the assembly, not a numerical discrepancy to average."*

**WALL C — the TTW graviton-loop premise is in-out, not retarded.** *"it is the in-out (Feynman)
object, not retarded; not exact; not usable at coincidence; and a position-space log is not
time-domain secularity (needs the x′ integration of their eq. (109), listed by the epilogue as not
done)."* The register's own primary-source audit: in that paper *"'retarded' occurs 0 times,
'causal' 0, 'Schwinger' 0, 'Keldysh' 0, 'in-in' 0"*, and **the SK step is what CREATES the causal
support and the branch structure.**
→ **Wall C means any branch structure quoted from the in-out object is created by a step not yet
taken.** A verdict read off Table 8 is wrong at the definition, not merely imprecise. Wall C is also
why `renormalization` stays undecided.

**The one scheme-independence requirement that survives the walls** (`CLASS_C_WALL_CONTRACTS.md`
§D5-Q4/Q5): the **existence and classification** must be scheme-independent; amplitudes need not be.
*"If classification changes with scheme, the registered question has answer 'scheme-dependent
existence' — itself a decisive negative/structural result recorded as such (outcome class
6-adjacent), NOT smoothed over."*

### 1.4 The strength vocabulary, and the absence that binds

`NO_GO_LEDGER.md` legend: **FORBIDDEN** = structural impossibility — *"This rebuild's register
currently banks NONE."* **SETTLED-NEGATIVE** = *"No known route + a strong structural obstruction,
but not impossible in every extension — open to a named rescue."* Plus EMPIRICALLY EXCLUDED,
INVISIBLE-BY-SUPPRESSION, BORROWED.

And: *"over-grading a no-go is the exact failure mode this program exists to prevent."* Every entry
is *"a statement about GRUT-as-written, not about nature."*

**A rule that applies to all seven branches equally, stated once here so no branch has to invent
it.** CHARTER §3: *"Banking a resolution of this in-house is an automatic fail."* Therefore **no
outcome in this map proposes a NO_GO_LEDGER entry on arrival.** A first, unreplicated result at one
order with three standing walls does not supply the *"strong structural obstruction"* that
SETTLED-NEGATIVE requires. Where a branch names a candidate ledger entry below, it is a candidate
**for after** independent implementation or external reproduction
(`provenance/CLASS_C_PROVENANCE_LEDGER.md`: SAME-CODE RERUN ≠ INDEPENDENT IMPLEMENTATION ≠ EXTERNAL
REPRODUCTION). Until then the disposition lives as a marker in the node's own `sub_status`
(CHARTER §7), never as a ledger grade.

### 1.5 Two register facts about *who* receives the dispatch, stated because they are the base rate

`provenance/claims.json`, the sealed authority-vocabulary annotation (2026-08-12):

> "'specialist', 'referee', 'independent' and 'external' denote in-house passes -- separate AI
> sessions run by that same author from a clean context. **NO OUTSIDE HUMAN HAS EVER BEEN CONTACTED
> BY THIS PROGRAM: no transmission is logged at any date**, and the author states directly that none
> occurred."

And `STATE.md`: *"The remaining owner act is the dispatch send."* Every branch below conditions on
"when a result eventually exists." **The conditioning event has no precedent in this program's own
record.** That is a fact about the base rate, not about the physics, and it belongs on the face of a
sealed map rather than in the priors of one branch.

---

## Section 2 — The seven outcomes

**Three scoring rules apply identically to all seven.** They are stated here, once, so that no
branch can quietly use different arithmetic from another — which is precisely the asymmetry the
symmetry audit found and Section 3 discloses.

> **RULE L1 — the ledger prices inputs, not verdicts.** `rung3_single_pole`'s Δ moves in exactly two
> circumstances: **(a)** the suspended −1 is released, which requires the memory structure to be
> genuinely *derived* for the registered object; or **(b)** a +1 is booked because the framework
> continues downstream to use a single memory time that the result has shown to be unsourced,
> undefined, or false — an unsourced input at its point of entry. Nothing else moves it. The
> register itself prices **neither** direction in advance (*"is NOT a +1 cost either: it is
> genuinely open"*), so **both are owner adjudications**, and this map proposes rather than
> executes.
>
> **RULE L2 — `background_time_translation_flow`'s +1 retires only through its own written route,
> and that route is currently blocked.** Its `overturning_computation`: *"OVERTURNED / DISCHARGED IF:
> the declared background is one carrying a timelike Killing vector -- the de Sitter static patch is
> the named candidate."* `CLASS_C_MANIFEST.json` declares `"patch": "flat FLRW"`, **which has no
> global timelike Killing vector.** Therefore, under **every** outcome in this map, the −1 is
> **AVAILABLE-BUT-BLOCKED**: it becomes earnable only under a patch re-declaration, which
> `CLASS_C_WALL_CONTRACTS.md` "Cross-contract consequences" §3 makes a **new versioned dispatch**.
> No branch books it. (This rule exists because three branches of the seven did book it and three
> declined; see §3.)
>
> **RULE L3 — the channel policy runs in both directions.** `CLASS_C_MANIFEST.json.channel_policy`:
> track `P^(2)` and `P^(0,s)` separately; *"no scalar result may be exported as TT; transversality
> does not imply tracelessness."* The dispatch object is TT. Therefore **no outcome below fires
> `mu_linear`'s armed trigger, takes `p_tt_ansatz`'s ONE ESCAPE, or moves `rung8_falsifier`'s
> diagonal-coupling verdict**, in either direction, unless the same run separately reports the
> `P^(0,s)` channel. This is stated once and holds for all seven.

---

### Outcome 1 — ISOLATED POLE

*Certificate token 1; banked class 1 ("Pole").* The assembled, gauge-invariant, IR-resummed
`G_R^TT` develops a single isolated relaxation pole in the lower half ω-plane at ω = −iΓ, with
location and residue passing the §1 criterion (∂τ_phys/∂k_min = 0, no epoch/window parameter
surviving), classification agreeing across the mandatory dual-gauge computation (D4-Q5) and two
renormalization prescriptions (D5-Q5), at O(G²) with Bunch-Davies boundary conditions.

**Verdict in one line.** This is the best outcome the register's seven permit, and it still buys
only a **restated** rung 3 — not the banked one, whose antecedent is already dead — at most one
ledger unit, and a memory rate that keystone-map D4 may forbid exporting to any cosmological node
that wants it.

**What it would mean.** Five independent things would have had to go right at once, and that
conjunction is most of the result's content. Wall A discharged *constructively* — a graviton-probe
assembly built where the corpus has only the scalar-probe version. Wall C discharged by actually
performing the SK conversion that creates the causal support, rather than reading the in-out object.
Wall B's resummation carried through or shown inessential. Fourth, and the one nobody should skip
past: **a stationary reduction would exist for the assembled object, in a channel whose free version
was exhibited non-stationary at >134% shape drift.** Fifth, within that reduction the low-ω structure
would be *one* pole, not the free theory's family indexed by multipole with lowest rate (l+1)H.

[INFERENCE] Only one known mechanism supplies items four and five together: de Sitter IR-screening
generates a dynamical mass, an effectively massive field has a dS-invariant state, stationarity
returns, and the pole comes with it. That is the Tsamis–Woodard horn the register already names —
and fences: *"GRUT's single-pole spine is NATURALLY SUPPORTED IF de Sitter IR-SCREENS -- FORWARD
DIRECTION ONLY… The CONVERSE (single-pole -> screening) is UNPROVEN."*

The honest meaning is therefore a **discovery result about de Sitter gravity**, from which a GRUT
consequence follows as a second, separately-arguable inference: rung 3's registered *consequent* is
reached by a route that retires its registered *antecedent*. **That is a restatement of the keystone,
not a graduation of it.**

**Register moves.**

| node | tier / Δ now | proposed | why, and what bars more |
|---|---|---|---|
| `rung3_single_pole` | derived-pending / **0** | **RESTATE**, then either (a) `derived` scoped to O(G² )/TT with the suspended −1 released, or (b) stay `derived-pending` with the pending input **renamed** to "establishment that O(G²) is the leading nonzero order for graviton loops" — **owner adjudication; this map does not choose** | Restatement is mandatory, not cosmetic: you cannot graduate a conditional by verifying its consequent through a different route while its antecedent (`J~ω³`) is dead and prohibited. Under RULE L1 the −1 is releasable only on a genuine derivation; CHARTER's premature-graduation rule is satisfied by dual-gauge + dual-scheme + ∂τ/∂k_min, and **not** satisfied on the order question. Any new input introduced by the wall-A construction offsets the credit at its point of entry. |
| `background_time_translation_flow` | assumed / **1** | **NO MOVE** — −1 available-but-blocked (RULE L2) | Outcome 1 *requires* a proved stationary reduction, and D3b names static-Killing as the only global candidate — but the declared patch is flat FLRW. The discharge is patch-contingent, and a static-patch rate carries D4's exponential↔power-law price the moment anyone quotes it cosmologically. |
| `p_tt_ansatz` | assumed / **1** | **NO MOVE** | RULE L3. The ONE ESCAPE is a *trace*-correlator vanishing. A spin-2 pole is silent about the trace. This is the single largest thing outcome 1 does not buy. |
| `mu_linear` | derived-pending, `no_go_export` / **0** | **NO MOVE; TRIGGER DOES NOT FIRE** | The trigger needs *"Pi_0 != 0 established"*. A TT pole establishes nothing about Π₀ in either direction. It stays armed and unfired. |
| `rung5_gr_limit` | assumed / **2** | **NO MOVE**, statement acquires a problem | *"tau_c->0 collapses chi to its conservative local form"* — an isolated pole names τ_c = 1/Γ **finite**. [INFERENCE] If Γ sits at the register's own expected order (the *"razor-thin Lorentzian of width ~Gamma~G^2 H^5"*), τ_c is astronomically **long**, every accessible frequency has ω ≫ Γ, and the GR limit is recovered by coupling smallness, not Markovianity. The +2 (area entropy, Unruh T) is untouched; GR stays BORROWED. |
| `rung7_wz` | to-derive / **3** | **NO Δ MOVE**; `tier_note` amendment | A confirmed single pole settles that τ₂ ∼ 1/H₀ is **inserted**. Double-count check (4) already fences the +3 against rung3 inheritance. **Direction: this is a cost of the favourable outcome** — the sourced prediction hardens to w = −1 flat. |
| `rung7_w2_wa_sign`, `rung7_w3_nocrossing_export` | to-derive / **0** each | released from *this* conditionality; eligible for re-derivation, **not** for promotion | `NO_GO_LEDGER.md` entry 3 holds them because *"a no-go cannot outrank its anchor."* An anchor resolution removes that blocker only. The no-crossing remains **Vikman-generic**, not GRUT-structural; an active response is a named rescue. No FORBIDDEN is created. |
| `kk_static_transfer` | derived-pending / **0** | **NOT DISCHARGED** by classification alone | Its `sub_status` names *"the vanishing-chi_inf single-pole class"* as **one sufficient route** — sufficient only for the χ_∞ = 0 subclass. Its own banked counterexample is retarded-analytic, passive, KMS-consistent, sits **inside** outcome 1's class, and fails the transfer via a negative contact term. "Isolated pole" is blind to χ_∞. |
| `rung8_falsifier` | to-derive / **2** | **NO MOVE** (RULE L3) | [INFERENCE] An Ohmic Im K_R from a relaxation pole would, through the KMS lock, give S(ω→0) → 4Tη ≠ 0, retiring the reasoning leg behind "quiet". But rung8's dominant coupling is diagonal T⁰⁰ — the scalar sector — and the TT→scalar export is barred. The leg is *suspect*, not moved. |
| `rung4_love_kk` | shown / **0** | **NO MOVE**; entry 5 if anything strengthened | The named loophole is *"a bath resonance / collective IR mode lifting |chi| into the live window."* A relaxation pole at ω = −iΓ with Γ ≪ H is not a resonance in any live window. INVISIBLE-BY-SUPPRESSION stands. |
| `u5_constitutive_phases` | to-derive / **0** | rung3 **gate on placement released**; no Δ | *"the GRUT-VACUUM PLACEMENT… gates on rung3 (which class the actual vacuum sits in needs the kernel)."* With a kernel, the placement becomes executable. |
| `u2_kernel_universality` | to-derive / **0** | **NO MOVE**; blocker **renamed** | From "no GRUT kernel exists to compare" to "no competing UV completion's IR kernel has been computed." Smaller obstruction, different one; not progress on universality. |
| `arrow_of_time` | assumed / **1** | **NO MOVE** — stated because silence would read as a move | *"EXISTENCE of dissipation = intrinsic; DIRECTION = assumed"*, imported from `past_hypothesis`. A pole is an existence-and-rate statement. |
| `rung9b_bridge` | assumed, settled-negative / **0** | **NO MOVE** | Reopen condition is narrowly *"a genuinely new scalar->TT operator identity."* |
| `rung1_inin_action` | shown / **4** | **NO MOVE** | The fourth input retires *only* into `eft_operator_basis`'s KC5/Bardeen completion and that work's own graduation screen. |

**What it does NOT buy.**

- **THE CLOCK TRAP, first because it is the deepest.** A proved reduction most plausibly lives in
  static-Killing time; D4 is exact and adverse: e^{−Γt} read in the other clock is a **power law**,
  and *"any comparison of rates across more than O(1/H) of elapsed time is clock-dependent."*
  [INFERENCE] If Γ ∼ G²H⁵ then Γ⁻¹ ≫ 1/H by dozens of orders, so the conversion is invalid **exactly
  in the regime the pole lives**. The keystone could be discharged and still be un-exportable to
  rung7, to any w(z) statement, to any τ₂ comparison. D2 is the same wall in space: a static observer
  at r ≠ 0 is accelerated and not comoving, and *"w(z)… is not an origin-worldline quantity."*
- **It does not discharge the banked rung 3** — only a restated one (see §0.2, items 1–2).
- **It does not touch the deep inputs.** `p_tt_ansatz` +1 CHOSEN; `rung5_gr_limit` +2 (GR borrowed);
  `rung6_qm_limit` +2 (Born rule borrowed); `arrow_of_time` +1 (Past Hypothesis); `rung1`'s four.
  At most **one** ledger unit moves, at rung3, and RULE L2 blocks the second.
- **It does not make anything observable — it makes GRUT less observable.** It hardens w = −1 flat;
  it fails to lift |χ| into the live GW window; it converts rung8's leg from derived to owed without
  changing any magnitude verdict.
- **It does not establish IR screening.** Forward direction only, per the register.
- **It banks no FORBIDDEN**, and creates no structural impossibility anywhere.
- **It does not settle χ_∞**, hence does not discharge `kk_static_transfer`, whose banked
  counterexample lives inside this outcome's own class.

**Still owed.**

1. **The E7 statement repair**, owed *before* the result can be filed against the node at all.
2. Formal retirement of the `J~ω³` / DOS justification chain from rung3's text, recorded as its own
   event rather than absorbed into a graduation.
3. **Which clock** the stationary reduction used, stated on the face — decides exportability at all.
4. The **D4 rate-conversion price**, paid explicitly, for every downstream node quoting the rate
   beyond O(1/H).
5. **χ_∞** (sign and value), without which `kk_static_transfer` does not discharge.
6. The separately-tracked **P^(0,s)** report (RULE L3).
7. Establishment that **O(G²) is the leading nonzero order for graviton loops** — the manifest's own
   caveat.
8. Whether the pole is **gapped at k → 0** (a rate, hence a memory time) or a dispersion Γ(k) (not a
   memory time). "Isolated pole at fixed k" does not answer this, and the free family indexed by l is
   what must have collapsed.
9. Disambiguation of **relaxation pole** (ω = −iΓ, no propagating dof) from **propagating mass pole**
   — only the first is the registered mechanism; the second collides with Higuchi for spin-2 in dS
   and with the settled-negative propagating-pole fence at `rung9b`.
10. **A circularity audit of the assembly's own premises** — see "how it could mislead"; neither
    D4-Q5 nor D5-Q5 tests it.
11. Wall-B provenance: if the resummation was completed by a route other than the RG half, that
    route's own status.
12. Independent implementation and, separately, external reproduction.
13. The four-lens screen and the bank gate. **Plus** `calc/gw_tensor_friction.py`, still owed (see
    §5), and owner resolution of the two package discrepancies of §0.3.

**How it could mislead.**

- **The headline over-read: "the keystone is discharged, rung 3 is derived."** It is not the banked
  rung 3 that would be derived. Anyone quoting "rung3 derived" without "restated, scoped to the
  class-C object at O(G²)" has laundered a route change into a graduation.
- **The circularity over-read — the one to bet on.** The register's own note: *"The axiom that forces
  Class A is LOCALITY/FINITE-MEMORY of the influence functional == single-pole RESTATED. So the
  favorable lean and the assumption are the SAME object -> the lean carries ALMOST NO independent
  evidential weight."* A class-C assembly makes analyticity, locality, and iε choices at a dozen
  points. If any presupposes the analytic class, a pole comes out because a pole went in — and
  **neither frozen acceptance test catches it**: D4-Q5 tests gauge-independence, D5-Q5 tests
  scheme-independence, **neither tests premise-independence.** That is a hole in the wall contracts,
  named here before a result exists precisely so it cannot later be waved past on the strength of two
  passed tests that were never about this.
- **The match temptation, pre-registered now so it cannot be enjoyed later.** If Γ⁻¹ lands anywhere
  near the prior lineage's 41.9 Myr, that is grounds for **maximum suspicion**; the τ₀ prohibition
  bars it from setup, plots, fits, and framing. Symmetrically: if Γ comes back at order H, note that
  H is the only scale the framework has, so a rate of order H is nearly forced by dimensional
  analysis and lands on the free ladder spacing, where the E6 fence makes state-vs-dynamics acute.
- **The proxy-consistency over-read, which is this branch's own and is declined.** The executed
  worldline reduction returned Ohmic-thermal with a white floor, and rung3's decision rule reads
  *"Ohmic (Im G_R ~ eta*omega) -> single-pole holds"*; a white noise floor is also the KMS partner of
  an Ohmic retarded kernel. Two reasons this branch may not use it: the manifest lists the worldline
  proxy kernel and *"any scalar-surrogate spectrum exported as TT"* under `not_the_object`; and the
  RESULTS file's own fence reads the floor as **zero-memory**. Recorded as a live tension with two
  readings and no verdict; one branch does not get to overturn another file's fence.
- **The status over-read.** A pole is a fact about de Sitter gravity in the EFT. The GRUT consequence
  is a second inference and must be argued as one.
- **The instrument inverted.** "Class C will show X" is on the red list for any X. If this map is
  ever cited as though it predicted a pole, the instrument has been inverted.

**Kill conditions.**

1. Classification disagrees between the two gauges (D4-Q5) — void, not weakened.
2. Classification changes under the two schemes (D5-Q5) — the answer is "scheme-dependent existence",
   recorded as 6-adjacent.
3. The pole location tracks `k_min`, or a window parameter survives in τ_phys. **The most likely
   quiet failure**, given the measured 2.3× k_min amplitude sensitivity at class A.
4. Stationarity holds only inside an epoch window — in particular near W < 0.25 e-folds. A named
   window makes the result outcome **5**, not 1; an unnamed one fires prohibition 5.
5. The "pole" sits at ω_n = −2πinT. That is the state's coth (E6) — different object.
6. The structure is per-multipole with l-dependent location and no gap as k → 0 — then it is the
   dressed free family, i.e. outcome **2**, and the register's objection stands unanswered.
7. Any pole in the upper half plane, or ω·Im χ < 0 anywhere — non-passive; violates
   `x_no_pin_theorem`'s pointwise floor; unstable, not relaxing.
8. The assembly borrowed the scalar-probe construction (wall A; `not_the_object`).
9. The verdict was read off TTW Table 8 without the SK conversion (wall C) — wrong at the definition.
10. O(G²) shown not to be the first nonzero order for graviton loops.
11. The pole is a **propagating mass pole** rather than a relaxation pole.
12. A circularity audit shows the assembly presupposed analyticity/locality of the influence
    functional — the result is then the premise restated.
13. Only a SAME-CODE RERUN reproduces it. The provenance grades are not interchangeable and this one
    does not clear the bar for a keystone.

**Honest prior.** **Low**, and discounted rather than inflated because CHARTER §1.4 says the loop
over-claims worst on exactly this outcome — `RUNG3_KEYSTONE_MAP.md` §8 names it: *"Directional-
optimism rule (CHARTER §1.4) applies hardest to POLE — the outcome the program wants."*

*Against:* (1) D1's pre-written expectation names outcomes 5 and 7 structurally likely and says
*"the pole/cut question may be unreachable."* (2) The free TT channel is non-stationary at >134%
drift, and this outcome needs the *interacting* object stationary where the free one is not — a
burden no other outcome carries. (3) The free retarded response is pole-free and supplies a family,
so *"the escape still requires Sigma to manufacture zeros at n > l where the free theory has none,
l-dependently, to yield any single rate at all."* (4) Massless spin-2 in dS has no dS-invariant
state; secular/IR growth is the generic expectation. (5) Conditional on *some* pole structure
existing, a per-multipole family is the more natural landing, so outcome 2 takes much of the "pole"
wedge. (6) Wall A means reaching any verdict requires constructing an assembly that does not exist.

*For:* the IR-screening horn is a named, live, published position that would deliver stationarity and
the pole from one mechanism. And one non-trivial in-tree pointer, grep-verified at
`calc/mz_inheritance.py:258`: the exact sum rule `sum_{l>=0} (2l+1) A_l(x,x;w) = -w sinh^2(x)`,
*"verified below to 26+ digits"*, making the l-summed free **local spectral density exactly OHMIC
with no rung zeros** — against rung3's own decision rule. **Weighted lightly**: it is a free,
l-summed, *local spectral* object, not the interacting retarded dynamics, and the register's fence is
that the free level carries no evidence either way.

*Numbers, stated so they can be held against this document.* Conditional on the calculation being
completed at all: ~10% that the classification returned is a pole of some kind; **~1 in 20 to 1 in
30** for the clean version described here — single rate, gapped, regulator- and epoch-independent,
dual-gauge and dual-scheme agreeing. Unconditionally, the probability that this outcome exists in the
record within any near horizon is dominated by the walls and by §1.5, not by the physics.

---

### Outcome 2 — MULTIPLE POLES / LADDER

*Certificate token 2; banked class 2 ("Multiple poles / ladder").* The assembled `G_R^TT(ω)`,
continued to ω → 0, exhibits a discrete family of simple poles in the lower half plane — and the
family is demonstrated to be **Σ's and not the state's** (E6 fence cleared: poles in the LHP, not at
the Matsubara sampling points ω_n = −2πinT, residues not the uniform 2T = H/π, and the structure
moves when the interaction moves).

**Verdict in one line.** GRUT's finite-memory axiom survives in *shape* and its single-rate mechanism
does not: the vacuum relaxes as a discrete sum of exponentials rather than one, which refutes rung 3
as written, hands GRUT a spectrum it must now **choose** a memory time out of, and buys nothing
favourable on the ledger.

**What it would mean.** The consequent is falsified directly and independently of the antecedent.
What is *not* falsified is the thing rung 3 exists to protect: each pole is an exponential, so
relaxation is exponential and memory is finite. The Weinberg horn — power-law kernels, memory that
never ends — is the horn that dies. **GRUT's premise is compatible with the result; GRUT's registered
mechanism for it is not.**

The structural gain is elsewhere and larger than it looks. A pole set is a spectral statement, and a
spectral statement presupposes a stationary reduction, which D1 declares un-presumed precisely
because no global reduction is licensed. **An outcome-2 result therefore carries, as a precondition
it must have discharged, exactly the presupposition `background_time_translation_flow` books.** That
would be the one clean recovery here — except that RULE L2 blocks it on the declared patch.

The cost is a new admitted input. The node asserts *the* memory time; the free theory supplies a
family indexed by multipole; outcome 2 replaces one family with another. **Nothing in a pole set
nominates a member.** Either GRUT proves the slowest pole controls the observable and is
k_min-independent, or "the memory time" becomes a *chosen* functional of a computed spectrum — a
selection rule booked as an input. [INFERENCE] And a slowest rate at O(H) means GRUT's memory scale is
the horizon scale: the only scale in the problem, so not an independent prediction of anything.

**Register moves.**

| node | tier / Δ now | proposed | why |
|---|---|---|---|
| `rung3_single_pole` | derived-pending / **0** | **REFUTED-AS-STATED**; marker `refuted` in `sub_status` (CHARTER §7). Δ: **owner adjudication under RULE L1** — either 0 → **+1** (the framework keeps using a single memory time that is now shown not to exist, an unsourced input) or 0 → 0 (the cost surfaces downstream as void scopes instead). **The register prices neither in advance.** | Explicitly *not* quoting any register text as licensing a "+1 for a clean failure" — **no such text exists** (grep-verified: the strings "clean failure" and "costs +1" appear nowhere in the repository). The suspended −1 is **not** recovered under any reading: the node does not earn its derived credit by being interestingly wrong. |
| `background_time_translation_flow` | assumed / **1** | **NO MOVE** — the −1 is available-but-blocked (RULE L2) | Its statement is exactly *"kernels depend on the time DIFFERENCE alone and a kernel of a single frequency K_R(omega,k) is definable."* Outcome 2 cannot exist without establishing that — but the discharge route names a timelike Killing vector, and the declared patch is flat FLRW. Blocked, not earned. **Also strictly conditional on the stationarity being window-free**: obtained inside an epoch window, kill condition 3 fires and there is nothing to discuss. |
| `rung5_gr_limit` | assumed / **2** | **Δ UNCHANGED**; statement repair owed | With a discrete family there is no single τ_c; the local limit requires all τ_k → 0 uniformly, i.e. summability of residues over the pole index. [INFERENCE] The free zero structure is l-dependent, so residue growth with l is a live worry. The GR limit is not lost; it acquires a convergence proof it does not have. |
| `rung7_wz` | to-derive / **3** | **Δ UNCHANGED**; `boundary_condition` reworded, **mildly adverse** | Its fence's stated agent (*"the second bath scale that rung3's single-pole confirmation forbids"*) is gone — but the relief is illusory: a ladder spaced O(H) is **multiplicity without scale separation**, and rung7 needs τ₂ ∼ 1/H₀, some forty orders out. The +2 goes from "unsourced but not forbidden" to "positively absent from the computed pole inventory at O(G²)". Double-count check (4) fences the +3 independently. |
| `rung7_w2_wa_sign` | to-derive / **0** | **Δ UNCHANGED**; **SCOPE VOID** | Statement scoped *"for the passive … SINGLE-POLE vacuum."* The antecedent is false, so the no-crossing no-go is **unscoped**, not refuted: re-derive on a discrete-spectrum vacuum or re-scope. `rung7_w3_nocrossing_export` inherits one step out. |
| `p_tt_ansatz` | assumed / **1** | **NO MOVE** (RULE L3) | The ONE ESCAPE is about ⟨T^μ_μ T^ν_ν⟩_R. A TT pole family cannot reach P^(0,s). *"FOR THIS NODE: the +1 stays."* |
| `mu_linear` | derived-pending / **0** | **NO MOVE; trigger does not fire** (RULE L3) | Needs Π₀ ≠ 0 established — a P^(0,s) determination. Reading "rung3 resolved" as "trigger fires" crosses the channel policy. |
| `u2_kernel_universality` | to-derive / **0** | tier unchanged; **first well-posed target** | Sharp bifurcation: if the spacing is set by H alone, it is the state's temperature wearing a dynamics costume (E6 one level up) and the universality is trivial; if by Σ's coupling structure, it is a real dynamical claim and testable. Gains most in tractability, least in credit. |
| `u5_constitutive_phases` | to-derive / **0** | tier unchanged; **placement unblocked** | The kernel now exists; the placement becomes a computation rather than a blocked question. |
| `kk_static_transfer` | derived-pending / **0** | **UNCHANGED**; named sufficient route **not** taken | The vanishing-χ_∞ *single-pole* class was the named route, and this is not it. A convergent pole sum alone would give χ_∞ = 0, but `renormalization` is UNDECIDED-DISPATCH and wall C leaves contact terms scheme-dependent. |
| `rung4_love_kk` | shown / **0** | **UNCHANGED**; loophole populated and useless | *"Loopholes only via resonance/lower-cutoff/collective/IR mode."* A discrete family formally *is* resonance structure — at ω ∼ H, some 36+ orders below the meV–MeV window entry 5 requires. Populated, non-actionable. |
| `rung8_falsifier` | to-derive / **2** | **NO MOVE** (RULE L3); leg flagged | [INFERENCE] A convergent pole sum gives Im χ ∼ ηω, and N = coth(βω/2)·Im χ → 2Tη: a **finite white noise floor**, not S(0) = 0. But the coupling is diagonal T⁰⁰ — scalar sector. The quiet verdict's *leg* is suspect; the verdict does not move from a TT result. |
| `arrow_of_time` | assumed / **1** | **NO MOVE** | All poles in the LHP is a passivity/causality consequence of the imported KMS state, not independent evidence for direction. |
| `rung9b_bridge` | assumed / **0** | **NO MOVE** | Reopen condition is narrowly a scalar→TT operator identity. |
| `rung1_inin_action` | shown / **4** | **NO MOVE** on the fourth input — **but see the finite-memory clause below** | Its fourth input retires only into `eft_operator_basis`'s graduation screen. Separately: outcome 2 is the *only* one of 3–6 that does **not** contradict rung1's finite-memory clause, since exponential relaxation is finite memory. Stated explicitly so the contrast in outcomes 3–6 is visible. |
| **new draft node** | — | *"assembled TT discrete relaxation spectrum"*, tier `derived-pending`, Δ **0**, `sub_status` carrying the priced inputs (order + its caveat, gauge decision, scheme, review status of the constructed assembly) | DRAFT ONLY; may not be cited as content until banked. |
| `NO_GO_LEDGER.md` | — | **PROPOSE NO ENTRY ON ARRIVAL** (§1.4) | Not FORBIDDEN; and not SETTLED-NEGATIVE either on first arrival — that grade wants a strong structural obstruction, and one unreplicated in-house calculation at one order with three standing walls does not supply it. |

**What it does NOT buy.**

- **A memory time.** A set is not a number. Every downstream use of "the memory time" remains an
  insertion until a *forced* selection rule exists; "take the slowest pole" is a choice unless
  someone proves the slowest member controls the observable **and** ∂τ_phys/∂k_min = 0 for that
  functional.
- **The suspended −1 at rung 3.**
- **rung7's second scale.** Multiplicity at one scale is not scale separation across forty orders.
  Worse for rung7, not better.
- **`p_tt_ansatz`'s discharge or `mu_linear`'s trigger** (RULE L3).
- **Observability.** rung4's suppression is 10²¹–10⁶² orders; ω ∼ H sits ~36 orders below the meV
  floor. `rung9b` stays frozen.
- **Validity past O(G²)** — the manifest's caveat is on its own face.
- **A general refutation of the branch-cut horn.** It refutes it at this order, in this channel, in
  this scheme. Weinberg free-streaming remains the collisionless behaviour, and collisionality
  remains an order-of-magnitude estimate (Γ/H ∼ (H/M_Pl)⁴), never a computed rate.
- **Retirement of walls A, B, or C.** Credibility is capped by the review status of the assembly it
  had to construct.
- **Any GRUT standing on arrival** — the certificate calls the first result a discovery result
  carrying no favour.

**Still owed.**

1. **The E7 denotation repair, first and blocking.** Until fixed, "the kernel has multiple poles" is
   not a proposition — the symmetrised route inherits the ladder, Kubo–Mori has none, the GLE
   friction kernel is temperature-independent outright.
2. A **forced selection rule** picking one rate out of the family — or an explicit register statement
   that GRUT has no single memory time and every downstream use of one is an insertion. There is no
   honest third option.
3. **Uniform convergence of the pole sum** over the multipole index, without which rung5's
   collapse-to-local has no proof.
4. The **P^(0,s)** channel computed separately, before anything touches `p_tt_ansatz` or `mu_linear`.
5. The **renormalization** decision and a determination of the contact term, before χ_∞ is read off
   anything.
6. The **gauge** decision — also `UNDECIDED-DISPATCH` at freeze. An outcome-2 result presupposes a
   declaration the record does not contain: *"choosing a gauge before the assembly scheme exists
   would be selecting the answer's frame."*
7. Independent implementation and, separately, external reproduction (CHARTER §3).
8. Whether O(G²) is the first nonzero order for graviton loops.
9. Re-derivation or re-scoping of `rung7_w2_wa_sign` and its w3 export on a discrete-spectrum vacuum.
10. Owner resolution of the two §0.3 package items — this branch owns a class registered on **both**
    faces, so it does not turn on the discrepancy, but a result arriving against a package whose
    faces disagree needs the owner to say which face it answered.

**How it could mislead.**

- **"Multiple poles contains one pole, so single-pole was approximately right."** E8 blocks this
  hard: gap and spacing both O(H), ratio O(1), no small quantity; *"Separation comes only by WAITING…
  never by a parametric limit."* "Eventually negligible" and "parametrically suppressed" are
  different claims and only the first is available. A later citation of this branch as soft
  vindication of rung 3 is wrong.
- **"The second pole rung7 needs is sourced."** Multiplicity is not scale separation, and rung7's own
  founding premise decouples N from K_R out of equilibrium so it could not inherit the shape anyway.
  Two independent reasons — and the temptation will still be strong because the phrase "second pole"
  appears verbatim in rung3's `boundary_condition`.
- **"Finite memory is now derived."** It is corroborated in shape and it *was the input*; the
  `ledger_note` already warns the favourable lean is circular. **Corroborating your own axiom is not
  earning it.**
- **"The white floor is refuted."** Possibly the opposite: [INFERENCE] Ohmic Im χ from a convergent
  pole sum, weighted by the KMS coth, gives a finite white **noise** floor — which is what the scalar
  proxy exhibited. That reconciliation is post-hoc, cross-channel, and unlicensed by wall A. Flagged
  before someone deploys it as evidence.
- **"GRUT predicts a resonance at ω ∼ H"** — the match temptation, in the one band where a match
  would look impressive.
- **Structurally worst: "the vacuum has discrete structure, therefore responsiveness."** Bounded
  domains have discrete spectra for reasons that have nothing to do with GRUT. The standing guard
  says *do not manufacture responsiveness*; this is the branch that makes manufacturing it feel like
  reporting.

**Kill conditions.**

1. **E6 fence failure** — poles at ω_n = −2πinT, spacing exactly H under T = H/2π, uniform residue
   2T = H/π, not moving when J or the coupling moves. Then the calculation recovered the **state's**
   coth: 6-adjacent with a decoration, not outcome 2.
2. **Sign/inversion contamination** — the "poles" are the free **zeros** at |m| ≤ l re-read as poles.
   The 2026-08-19 adversarial pass already caught one favourably-directed miscount in that zero set.
   Any outcome-2 report must exhibit the zero set and the pole set side by side.
3. **Self-refuting resolution** — the assembly used an epoch window. Stationarity holds only for
   W < 0.25 e-folds, capping frequency resolution at Δω ∼ 1/W ≈ 4H. **A ladder spaced H apart is
   unresolvable in that window.** A windowed calculation cannot report this outcome.
4. **Regulator tracking** — spacing, count, or the slowest rate moves with `k_min`.
5. **Gauge disagreement** on the classification (D4-Q5).
6. **Scheme dependence** of the classification (D5-Q5).
7. **Wall C violation** — read off an in-out object without the SK conversion.
8. **Wall A violation** — assembly borrowed from the scalar-probe construction.
9. **Prohibited input** — `J~ω³` anywhere, a τ₀/desired-timescale target anywhere in setup, plots,
   fits or framing, or a single-pole ansatz assumed inside the test.
10. **Physicality failure** — any UHP pole, or negative spectral weight. A broken calculation, not a
    discovery.
11. **No definable τ_phys** — rates track l with no floor and the residue-weighted sum diverges. Then
    the discharge criterion cannot even be evaluated and this collapses toward outcome 7.
12. **Masked by a floor** — the object carries *both* a discrete ladder and a nonzero ρ(ω→0). Then
    the ω→0 verdict is the floor, and this branch does not own the result.

**Honest prior.** **Low — around 10%**, and among the least likely of the seven: below secular,
below ill-posed, below no-long-memory-structure, and at or below branch cut.

The reasons are specific and mostly arithmetic. (1) The free retarded response is **pole-free**
(E4); every pole here must be manufactured by Σ, and *"the escape still requires Sigma to
manufacture zeros at n > l where the free theory has none, l-dependently."* (2) The manufacturing
agent is extraordinarily weak: Γ/H ∼ (H/M_Pl)⁴, an order-of-magnitude estimate, not a computed rate.
Discrete poles are the **collisional** signature, and collisionality is precisely what is neither
demonstrated nor plausible at that suppression. (3) **The stationarity precondition is the sharpest
argument against this branch.** [INFERENCE] The free TT kernel drifts >130% within O(1) e-fold; for
interactions to restore stationarity they would have to act on a timescale competitive with that
drift, and (M_Pl/H)⁴ e-folds is not competitive by any margin. So outcome 2 requires the
non-stationarity to have been a **gauge artifact removed by the assembly** — the
Higuchi/Marolf–Morrison horn, live but unproven, and unsettled in the literature by its own
admission. This branch is conditional on an unproven horn, not merely on a calculation. (4) D1's own
pre-written expectation names other branches.

What keeps the prior from being lower: the static patch is a bounded domain, bounded domains produce
discrete spectra generically, and the free object already carries discrete structure at spacing
exactly H. That is a weak reason and is not dressed as a strong one — it is also exactly the
coincidence that makes a *contaminated* result look like this branch, which is why kill conditions 1
and 2 are the first two written.

---

### Outcome 3 — BRANCH CUT

*Certificate token 3; banked class 3 ("Branch cut / continuum") — **this branch owns one half of a
single registered class**, and outcome 4 owns the other.* The assembled, gauge-invariant, IR-resummed
retarded `G_R^TT(ω)`, continued to ω → 0, is **non-analytic at the origin with a locatable branch
point** (canonical forms: Im G_R^TT ∼ |ω| or ω² ln ω): Σ_R^TT carries a cut rather than an isolated
LHP zero of G0⁻¹ − Σ. Relaxation is power-law in time; there is no dynamical mass and no single rate.

**The discriminator against the other half of the class, stated explicitly:** a cut has a **nameable
branch point and an extractable exponent α with an error budget**; a continuum is a structureless
positive low-ω measure with no isolated non-analyticity to name. **If α is not extractable with an
error budget, the result is outcome 4, not this one.**

**Verdict in one line.** Rung 3 fails in exactly the way its own second boundary condition named —
the collisionless/free-streaming horn — and GRUT keeps a dissipative vacuum while losing the
**finite**-memory premise that made that vacuum a prediction rather than an observation about loops.

**What it would mean.** A cut answers the open anchor question in the negative, in the manner
rung3's `boundary_condition` pre-named verbatim: *"for a genuinely COLLISIONLESS free-streaming bath
(Weinberg 2004 nonlocal memory) the kernel is power-law… Sigma(omega) has a BRANCH CUT at omega->0
(~|omega| or omega^2 log omega), NOT a pole -> the single pole DISSOLVES into a continuum (no
dynamical mass, power-law not exponential relaxation)."*

Three consequences at three different strengths.

*First, and least glamorous:* GRUT keeps a dissipative gravitational vacuum. Im G_R^TT ≠ 0 at low
frequency is not nothing — outcome 6 would have denied it. But it buys almost no GRUT-specific
credit. [INFERENCE] The free retarded response is pole-free, so Σ manufactures every shape; and
manufacturing a cut is what a loop with massless intermediate states does by default, whereas
manufacturing an isolated pole requires resummation plus a dynamical mass. The result reads closer to
*"the theory is ordinary here"* than to *"the theory is vindicated here."*

*Second — the sharpest consequence, and one nobody reads off the headline:* **the premise dies, not
the phenomenon.** GRUT's stated core, in `rung1_inin_action`'s own `shown`-tier statement, is *"a
responsive medium with **finite memory**."* A cut is **more** memory — unbounded, characterized by an
exponent rather than a scale. Every downstream sentence written in the vocabulary of τ_c dies with
it; and [INFERENCE] a |ω| or ω²lnω term is absorbable into no finite derivative expansion, so GRUT's
gravitational sector becomes irreducibly **nonlocal** at low frequency. GR recovery is not refuted —
the remainder may be 21–62 orders down — but its stated mechanism is unavailable and owes a
replacement. **This contradiction with a clause inside a `shown`-tier, Δ4 node is a register event in
its own right and is handled below and in §3.**

*Third:* the anchor closes by dying, which is a loss of usable structure downstream rather than an
unlock. `rung7_w2_wa_sign` is scoped *"for the passive … SINGLE-POLE vacuum"*; its hypothesis is now
known false, and it goes scope-vacuous, taking `rung7_w3_nocrossing_export` with it.

**Register moves.**

| node | tier / Δ now | proposed | why |
|---|---|---|---|
| `rung3_single_pole` | derived-pending / **0** | **REFUTED**, marker `refuted` in `sub_status` (never `tier_note` — the resident cannot see a disposition filed there). Δ under **RULE L1: owner adjudication**, 0 → +1 or 0 → 0 | The suspended −1 is permanently extinguished. "Refuted at Δ0" **looks free and is not**: the cost migrates to rung5 and to the finite-memory premise and must be booked there rather than absorbed silently. **Statement repair is a precondition of the re-tier, not a follow-up** (E7): a node cannot be scored refuted against a phrase with no referent. |
| **`rung1_inin_action`'s finite-memory clause** | shown / **4** | **CHARTER §4 compound/omission test OWED AND BLOCKING** (see §2 preamble note and §3) | The statement contains *"a responsive medium with finite memory"*, which an unbounded power-law kernel contradicts. CHARTER §4's tell: *"if the candidate appears in the node's own statement, it is a split question."* Candidate repair = **split**, keeping `shown` and the Δ4 (including the KC5-reserved fourth input) with the SK influence-action **form** half — which `u1_form_universality` already grades generic and which discharges alone via Feynman–Vernon — and booking the constitutive half where this outcome can reach it. **This map does not execute the split**: the register's own history is that two of five pre-registered candidates were mislocated, and *"applying the wrong repair… manufactures a false dependency graph."* Run the test. The two tallies are never summed. |
| **new draft node** | — | *"the assembled O(G²) TT retarded response is non-analytic at ω→0 with branch exponent α"* — `derived` at the calculation's own grade **iff** D4-Q5 and D5-Q5 both pass; `derived-pending` otherwise. Δ **0** | It is a RESULT, not an input — and per the certificate a discovery result about de Sitter that *"carries no favour."* |
| `rung5_gr_limit` | assumed / **2** | **Δ UNCHANGED**; mandatory statement repair; one candidate +1 **flagged, not proposed** | The τ_c → 0 mechanism names a nonexistent object under a cut. Candidate new input — *"the irreducible nonlocal remainder is observationally negligible at solar-system and LIGO frequencies"* — is flagged rather than booked: booking it before the derivative-expansion check exists would be premature graduation. |
| `background_time_translation_flow` | assumed / **1** | **NO MOVE**; −1 available-but-blocked (RULE L2) | The discharge route names a timelike Killing vector; the declared patch is flat FLRW. A patch re-declaration is a new versioned dispatch. |
| `rung7_wz` | to-derive / **3** | **Δ UNCHANGED** — the delta reduction is **declined explicitly** | A continuum lifts the single-pole prohibition on a second scale, but **removal of a prohibition is not supply of a mode**: the +2 for the inserted τ₂ ∼ 1/H₀ stays inserted, and double-count check (4) already fences the inheritance. |
| `rung7_w2_wa_sign` | to-derive / **0** | add `moot` to `sub_status` (its OWN disposition: its hypothesis is known false); Δ unchanged | The *reference* to rung3's `refuted` marker goes in `tier_note`, never `sub_status` (CHARTER §7 corollary — the third free-text-regex near-miss of the program). Re-pose owed for a continuum kernel; note a continuum is **one** passive channel with continuous spectrum, so Vikman's single-DOF no-crossing plausibly **survives** re-posing. `rung7_w3_nocrossing_export` inherits by `tier_note` reference only. |
| `mu_linear` | derived-pending / **0** | **UNCHANGED; TRIGGER NOT FIRED** (RULE L3) | A TT-channel cut is silent on ⟨T^μ_μ T^ν_ν⟩_R. |
| `p_tt_ansatz` | assumed / **1** | **UNCHANGED**; one conditional sharpening, not a delta | If the same run reports a cut in the separately-tracked P^(0,s) channel, Π₀ ≠ 0 is established, the ONE ESCAPE closes permanently, and the +1 becomes irreversible rather than merely standing. |
| `kk_static_transfer` | derived-pending / **0** | **UNCHANGED** — pre-fenced against this exact branch | Its `overturning_computation` names it: rung3 resolving the UV/contact structure is what adjudicates; χ_∞ is a **reactive contact datum**, and passivity *"pushes the static modulus up FROM the instantaneous part chi_inf and never below it — the whole transfer question IS the sign of chi_inf."* A low-ω cut does not supply it. **The register wrote this branch's limit before the branch did; reported rather than routed around.** |
| `rung4_love_kk` | shown / **0** | **UNCHANGED**; loophole **not** opened | KK partnership holds for any causal χ. A |ω|-type cut **vanishes** at ω→0 rather than lifting |χ|, and nothing supplies the 21–62 orders entry 5 requires. |
| `rung8_falsifier` | to-derive / **2** | **UNCHANGED**; one banked reasoning leg **voided**, and the tempting win **refused** | The quiet verdict rests on S(0)=0 derived in the analytic bath class (`finite_T_exponent.py`); a cut destroys that premise, and under KMS a |ω| cut gives N(ω→0) → 2T·const ≠ 0. **But the coupling is diagonal T⁰⁰ — P^(0,s) — and RULE L3 bars the import.** The falsifier is not revived; one leg's derivation is voided in the wrong channel and must be recomputed in the right one. |
| `u5_constitutive_phases` | to-derive / **0** | Δ unchanged; **the gated half unblocks** | A cut with exponent α **is** the kernel datum: placement is non-Markovian, long-memory, power-law. The single most genuinely constructive consequence of this branch — and a placement datum, not a classification theorem. |
| `u2_kernel_universality` | to-derive / **0** | **UNCHANGED** | A free-streaming exponent fixed by *kinematics* rather than microphysics is universality-friendly **in flavour**. It is not evidence: u2 graduates only on ≥2 distinct completions flowing to the same IR-kernel class, and one EFT calculation is not one completion. |
| `NO_GO_LEDGER.md` | — | **candidate** entry at **SETTLED-NEGATIVE**, explicitly NOT FORBIDDEN — and per §1.4 **not on arrival** | *"The Markovian / short-memory single-pole gravitational memory mechanism as registered."* Obstruction: generic non-analyticity of a collisionless massless bath. **Named rescue** (what keeps it off FORBIDDEN): a genuine collisional channel at higher order, or an IR-screening resummation producing a dynamical mass that **coexists** with the cut. This rebuild banks no FORBIDDEN and this branch must not become the first. |

**What it does NOT buy.**

- **It does not refute the existence of a relaxation pole.** Poles and cuts coexist in ordinary
  analytic structures; a cut in the LHP excludes nothing on the second sheet. What a cut decides is
  **asymptotics**: any exponential from a coexisting pole dies while t^−α does not, so the cut owns
  the late-time memory regardless. The precise statement is *"single-pole as **the** memory structure
  fails"*, not "no pole exists" — and the second is what a careless reader will bank.
- **It does not fire `mu_linear`'s trigger, flip `p_tt_ansatz` to FORCED, retire its +1, or touch the
  μ=4/3 endpoint exclusion** (p_tt-independent, separate-universe + ISW).
- **It does not retire `kk_static_transfer`'s conditional floor** — that node names branch-cut kernels
  explicitly and says the conditional dies only with the **sign of χ_∞**.
- **It does not open rung4's magnitude loophole, does not move the GW invisibility entry, and does
  not revive rung8**: the S(0)=0 leg's *derivation* is voided, in a channel the result cannot reach.
- **It does not source rung7's τ₂**, and it does not overturn the no-crossing no-go. It removes a
  prohibition; it supplies no mode, no amplitude, no second degree of freedom.
- **It does not discharge rung1's fourth input, reopen `rung9b_bridge`, or discharge
  `background_time_translation_flow`** in the declared flat-FLRW patch.
- **It banks no FORBIDDEN**, and establishes nothing outside the declared order, state, and the
  gauge/scheme pair actually computed. *"No structure beyond the cut" at this order is not "no
  structure."*
- **Most importantly: it does not make the responsive vacuum a prediction.** [INFERENCE] Im G_R^TT ≠ 0
  with a cut is the default analytic behaviour of a loop with massless internal lines. The
  GRUT-specific content, if any, lives in α and in the amplitude — neither of which the
  classification alone delivers.

**Still owed.**

1. **The E7 statement repair, before the re-tier and not after it.** Name which MZ object the cut is a
   cut *of*.
2. **The exponent α with a full error budget**, plus the §1 criterion evaluated on it: ∂α/∂k_min = 0
   and no epoch/window parameter surviving.
3. **Dual-gauge (D4-Q5) and dual-scheme (D5-Q5) classification agreement**, mandatory, never averaged.
4. **The P^(0,s) report** — without it no trace-sector consequence is adjudicable in either direction.
5. **A second-sheet / coexisting-pole scan.** If a pole coexists and dominates numerically over every
   accessible epoch, the practical answer is outcome 1 wearing outcome 3's clothes.
6. **rung5's derivative-expansion check**: does the nonlocal remainder admit a local approximation at
   solar-system and LIGO frequencies, and at what price? That is where the +1 this branch declined
   may actually land.
7. **rung8's S(0) recomputation in the correct (P^(0,s)) channel.**
8. **An internal tension in `RUNG3_KEYSTONE_MAP.md` §1.2 this branch flags rather than resolves:**
   D1 derives T = t exactly *on the axis*, while D4 computes the global conversion using HT = e^{Ht}.
   If D4's relation is the operative one beyond O(1/H), then **pole-vs-cut is itself clock-dependent
   at late times**, and a cut result requires certification in a named clock before it means anything.
   Surfaced, not resolved; the repository was not modified.
9. The **CHARTER §4 test on rung1's finite-memory clause** (above).
10. Owner resolution of the two §0.3 package items — **this branch is the one most exposed to them**,
    since it owns half of one registered class.
11. **A rewrite of GRUT's own premise sentence.** *"Responsive vacuum with finite memory"* is the
    stated core; under this outcome the memory is unbounded and scale-free. That is a revision of the
    framework's founding sentence and should be made explicitly rather than absorbed by silence.

**How it could mislead.** In descending order of likelihood:

1. **"A cut is still dissipation, so the responsive vacuum is confirmed."** The deepest deflation this
   branch has to survive, stated against its own interest: a branch cut is the **generic** analytic
   structure of a loop with massless intermediate states. Reporting a cut is closer to reporting that
   the calculation behaved like a calculation than to reporting a GRUT signature.
2. **"Single-pole refuted ⇒ GRUT's memory refuted."** Backwards. A cut is **more** memory. What dies
   is finiteness and Markovianity — the premise, not the phenomenon.
3. **"A continuum contains all scales, so rung7's second scale is supplied and DESI's evolving w(z) is
   back."** Removal of a prohibition is not supply of a mode. The over-read with the strongest
   emotional pull, because it points at data.
4. **The consistency trap.** Under KMS a |ω| cut gives N(ω→0) → 2T·const — a white noise floor, which
   is exactly the class-A proxy's horizon-forced floor. That agreement will look like independent
   confirmation. It is more likely **leakage**: the proxy is scalar, class-A, and explicitly
   `not_the_object`. **Matching the proxy should raise suspicion of contamination before it raises
   confidence.**
5. **Grade inflation to FORBIDDEN.** "The cut structurally forbids single-pole" is one careless
   sentence away, and it would be this rebuild's first.
6. **The match temptation**: a measured exponent α is a free number begging to be fitted to a
   cosmological observable. Carry it free.
7. **"The anchor is settled, so downstream unlocks."** It settles by dying; rung7_w2 and its export go
   scope-vacuous. Structure lost, not gained.

**Kill conditions.**

1. Classification disagrees between the two mandated gauges (D4-Q5) — structural information about the
   assembly, not a cut, and not averageable.
2. Classification changes under the mandated scheme comparison (D5-Q5) — "scheme-dependent existence",
   6-adjacent, and this branch is void. [INFERENCE] Note that R², C² and Λ insertions contribute
   **analytic** ω² only, so a genuine ω²lnω or |ω| *should* be protected — which is exactly why a
   scheme-dependent result here would be diagnostic of the assembly rather than of the physics.
3. The branch structure was read off TTW Table 8's in-out object without the SK conversion **and**
   the x′ integration of eq. (109). Wrong at the definition.
4. The stationary reduction was **presumed** rather than proved. The free TT channel is non-stationary
   at >130%; if stationarity was imported, there is no ω and the cut is not posed. **This branch
   presupposes a reduction the register has never obtained.**
5. The cut's existence or exponent tracks `k_min` or the epoch window — a priced input, the same
   defect that closed class A.
6. The assembly borrowed the scalar-probe construction, or any scalar surrogate spectrum was exported
   as TT.
7. `J~ω³` entered anywhere in the chain.
8. A coexisting isolated pole dominates numerically across every accessible epoch, making t^−α
   unreachable in practice — then the operative classification is outcome 1 and this branch mislabels
   it.
9. The low-ω signature reproduces the class-A proxy white floor within its own uncertainty **and** the
   assembly cannot be shown independent of the proxy. Treat as contamination until proven otherwise.
10. The D1/D4 clock tension resolves toward D4 — then a cut certified in an unnamed clock is a
    coordinate artifact, not a classification.
11. The E7 kernel-phrase defect is left unrepaired and the re-tier proceeds anyway — the node was
    scored refuted against a phrase denoting no unique object, and **the re-tier is void regardless of
    what the calculation found.**
12. α is not extractable with an error budget — then this is **outcome 4**, not outcome 3, and the
    result must be filed there.

**Honest prior.** Split into two factors, neither inflated.

**Conditional on the pole/cut question being posed at all** — assembly exists (wall A), resummation
completed with its RG half (wall B), SK conversion performed (wall C), and a stationary reduction of
the **assembled** object **proved** — branch cut is the favourite among the spectral shapes {1, 2, 3}:
roughly **50–60%**. The reasons are physical. Graviton-graviton scattering in dS is suppressed at
Γ/H ∼ (H/M_Pl)⁴, so the bath is essentially collisionless, and rung3's own three-specialist
reconciliation puts a collisionless free-streaming bath squarely on the branch-cut horn. Loops with
massless internal lines produce cuts generically; the free response is pole-free so Σ must
manufacture everything, and manufacturing an isolated pole *additionally* requires collapsing the
free multipole family — a far heavier burden than producing a two-particle cut. TTW's graviton-loop
Table 8 carries ln(H²Δx²) in every row, and the SK conversion is documented to turn exactly that into
θ(Δη−r)·ln[H²(Δη²−r²)] — branch structure with causal support.

**Unconditionally**, the mass drains out of the conditioning event: roughly **15–20%**, behind
outcomes 5 and 7. Three reasons, all already in the record. First, D1's own pre-written consequence
names outcomes 5 and 7 structurally likely and the pole/cut question *"may be unreachable"* — that is
the register's expectation and not this branch's to argue away. Second, the free TT channel is
non-stationary by >130% and this outcome requires the **interacting** object to be stationary where
the free one is not. Third — the tension inside this branch a screener should press hardest — the most
plausible mechanism for interactions to restore stationarity is **IR screening generating a dynamical
mass**, which is precisely the mechanism rung3 names as producing a **pole**. The static-Killing route
restores stationarity without a mass, but requires a patch not currently declared. **So the route that
makes this outcome posable is disproportionately the route that makes a different outcome true.**

*Net:* physically the most likely spectral answer, structurally among the less likely things for this
calculation to be able to say at all.

---

### Outcome 4 — CONTINUUM

*Certificate token 4; banked class 3 ("Branch cut / continuum") — **the other half of outcome 3's
registered class**.* The assembled `G_R^TT(ω)` carries a continuous low-frequency spectral density
with **no isolated structure**: no relaxation pole, no ladder distinguishable from the state's
Matsubara sampling, and **no nameable branch point with a definite exponent**. The spectral weight is
distributed smoothly over a band whose only scale is H.

**Verdict in one line.** The assembled TT response would have a spectral **class** but no **rate** —
rung 3's single-pole implementation lands settled-negative-in-flavour, GRUT's memory becomes a
computed function instead of a conjectured pole, and the ledger does not improve.

**What it would mean.** Rung 3 would be decided against its implementation while leaving GRUT's
premise standing on different ground. Its `differentiator` field is *"tau_c>0 vs tau_c=0"*; a
featureless continuum answers neither horn cleanly, supplying a spectral class without a rate.

**The primary sub-case is the adverse one and must be stated first.** [INFERENCE] If the continuum's
low-frequency edge is Ohmic with finite η, the symmetrised noise floor S(0) = 4Tη is nonzero — the
same white-noise shape the class-A scalar proxy already produced, fenced there as *"contradicting the
FINITE-memory claim as much as it contradicts s = 3."* In that sub-case **rung 3's letter is
satisfied ("Markovian-like") while GRUT's premise fails**: τ_c = 0 is the GR side of the node's own
differentiator. Only the softer sub-case — continuum weight vanishing as ω→0 with a convergent first
moment ∫t K(t)dt — delivers genuine finite memory, and even then it delivers a memory **function**,
not a memory **time**.

What genuinely changes: memory stops being a conjectured pole and becomes an object with a computed
shape. Every downstream export written in terms of one τ — the GR limit, the no-crossing no-go, the
kernel-universality question, the falsifier's S(0)=0 premise — must be rewritten as a kernel statement
or withdrawn. **That is work created, not credit earned.**

**Register moves.**

| node | tier / Δ now | proposed | why |
|---|---|---|---|
| `rung3_single_pole` | derived-pending / **0** | **REFUTED-AS-REGISTERED at class-C scope**; `refuted` in `sub_status`. Δ under **RULE L1: owner adjudication** | The node asserts *the* memory time; a featureless continuum supplies a distribution of rates and no isolated singularity carrying a finite fraction of the low-ω weight. The suspended −1 is cancelled, not released. If a +1 is booked, it is the relocation booking: *"which continuum, with what edge behaviour"* becomes a named underived input. Strength flavour: settled-negative, **never FORBIDDEN** — the named rescue is isolated structure appearing above O(G²), left open by the manifest's own caveat and by D3's recorded consequence. |
| **COMPOUND SPLIT proposed at rung3** | — | **NEW `rung3a_transport_class`** — the low-ω spectral class of the assembled TT response — tier `derived` **at class-C scope**, Δ **0** (no credit: the derivation is the *negation* of the registered claim, and its reliability is capped by walls A–C). **NEW `rung3b_single_memory_time`** — the existence of one τ usable downstream — tier `refuted`, carrying whatever +1 RULE L1 adjudication assigns | CHARTER §4 test — *"can one part discharge alone?"* — passes: the class can be established without the rate. Compound and omission tallies are never summed. |
| **`rung1_inin_action`'s finite-memory clause** | shown / **4** | **CHARTER §4 test OWED** (as in outcome 3), in the Ohmic sub-case where τ_c = 0 | The adverse sub-case contradicts the clause; the softer sub-case does not. **The report must state which sub-case it is in before this move can be evaluated at all.** |
| `background_time_translation_flow` | assumed / **1** | **NO MOVE**; −1 available-but-blocked (RULE L2) | A continuum classification presupposes the reduction exists — but D1 requires that *"any one-clock spectral reduction requires its own proof for the assembled object"*, and the discharge route additionally names a timelike Killing vector the declared patch lacks. **This is the largest favourable ledger move available on this branch and the one most likely to be over-claimed; it is blocked.** |
| `rung5_gr_limit` | assumed / **2** | **UNMOVED**; statement repair owed | *"tau_c->0"* has no τ_c under a continuum. Re-pose as the limit in which the continuum's entire support recedes above every probe frequency. The limit survives as a kernel statement; the booked input is the collapse assumption, not the pole. |
| `rung7_wz` | to-derive / **3** | **UNMOVED**; `boundary_condition` amended | The single-pole prohibition on a second bath scale is **vacated** — a continuum forbids nothing — so the ~40-orders reconciliation becomes unnecessary. **But vacating a prohibition is not sourcing an input**: the +2 is not retired and the sourced prediction stays w = −1 flat. Reading a continuum as *supplying* weight at ω ∼ H₀ is the match temptation and is refused here in advance. |
| `rung7_w2_wa_sign` | to-derive / **0** | **UNMOVED**; `sub_status` records that its scope premise is no longer available | Re-derive for a continuum kernel or withdraw. `rung7_w3_nocrossing_export` loses its contingency support in the same step. |
| `NO_GO_LEDGER.md` entry 3 | held to-derive | **RE-GRADE DOWNWARD** to "premise withdrawn pending re-derivation" | Its own calibration says the no-crossing is *"conditional on the open rung3 (a no-go cannot outrank its anchor)."* Under this outcome the anchor is not merely open, it is adverse to the premise the entry uses. **A demotion. No entry is promoted; the ledger continues to bank zero FORBIDDEN.** |
| `u5_constitutive_phases` | to-derive / **0** | → `derived-pending`, Δ **0** | Its `sub_status` says the GRUT-vacuum placement *"gates on rung3 (which class the actual vacuum sits in needs the kernel)."* A continuum classification supplies exactly that gating input. **A gate opening, not a result.** |
| `u2_kernel_universality` | to-derive / **0** | **UNMOVED**; statement repair owed | Its statement asks about *"the low-omega pole structure"*; under a continuum that phrase has no referent and must become "the low-ω spectral class." Its `sub_status` calls it *"THE one place a real universality RESULT could live"* — that question becomes askable for the first time, because there is finally an object to be universal about. |
| `rung8_falsifier` | to-derive / **2** | **UNMOVED — the branch's most tempting apparent prize, refused** (RULE L3) | A nonzero continuum floor would lift the S(0)=0 leg — but T⁰⁰ is the **scalar** sector. Only a separately reported P^(0,s) floor could touch rung8, and even then the amplitude is set by T_dS = H/2π against entry 4's already-priced 10⁷× staking requirement. Grade stays INVISIBLE-BY-SUPPRESSION. |
| `rung4_love_kk` | shown / **0** | **UNMOVED in tier, and NARROWED ADVERSELY** | The named loopholes are *"resonance / lower-cutoff / collective / IR mode."* A continuum with **no isolated structure** supplies no resonance and no collective mode **by construction** — the outcome **closes two of the four sub-loopholes**. The lower-cutoff sub-loophole survives only as the k_min regulator, which the spec bars from carrying physics. **A favourable-sounding classification makes GRUT less observable, not more.** |
| `mu_linear` | derived-pending / **0** | **NOT MOVED BY THIS OUTCOME ALONE** (RULE L3) | If the same computation *separately* reports Π₀ ≠ 0 in the tracked scalar channel, the trigger fires and the node moves derived-pending → assumed at Δ0, executed and not re-litigated. Claiming it fires from a TT continuum is laundering across the channel policy. |
| `p_tt_ansatz` | assumed / **1** | **UNMOVED** | The ONE ESCAPE requires a **non-perturbative** vanishing of the trace correlator. *"FOR THIS NODE: the +1 stays."* |
| `kk_static_transfer` | derived-pending / **0** | **UNMOVED** | Its pending input is the **sign of χ_∞**, a UV/contact datum. A low-ω classification is silent on it, and the named sufficient route runs through outcome 1. **This branch must not claim this node.** |
| unmoved, explicitly | — | `rung9b_bridge`, `x_no_pin_theorem` (pending on `eft_operator_basis`'s KC5 completion, not on rung3), `eft_operator_basis`, `zeta_interior_family`, `arrow_of_time` (a continuum establishes *existence* of dissipation, already shown-grade; **direction** stays imported), `rung1_inin_action`'s fourth input | Stated because silence on any of these would read as a move. |

**What it does NOT buy.**

- **It does not derive rung 3.** The registered claim is single-pole/Markovian-like with a memory
  time; a continuum is neither, and no version of this converts the suspended −1 into a credit.
- **It does not supply a memory time.** At most a memory **function**. Whether any finite τ_mem exists
  requires ∫₀^∞ t K(t) dt to converge — an additional property of the edge that the classification
  does not deliver. Every downstream use of "one τ" remains unfunded.
- **It does not establish finite memory — GRUT's actual premise.** In the primary Ohmic sub-case
  S(0) = 4Tη ≠ 0, which is **zero** memory (τ_c = 0), the GR side of rung3's own differentiator — the
  same adverse shape the class-A proxy produced and was fenced for.
- **It does not establish responsiveness.** *"Do not manufacture responsiveness."* A spectral class is
  not a mechanism, and the FDT/KMS lock that would convert dissipation into GRUT's response structure
  is rung2's, already booked, not re-earned here.
- **It does not retire `p_tt_ansatz`'s +1, fire `mu_linear`'s trigger, discharge rung1's fourth input,
  reopen `rung9b_bridge`, or touch `kk_static_transfer`.**
- **It does not open rung4's observability loophole — it CLOSES two sub-loopholes.** GRUT does not
  become observable; the 10²¹–10⁶² orders are untouched.
- **It banks no FORBIDDEN**, and only reaches settled-negative flavour *after* both mandatory tests
  pass. Fail either and the answer is "gauge-dependent" or "scheme-dependent existence", recorded as
  6-adjacent — **not** "continuum".
- **It does not retire walls A, B, or C**, and does not settle the class-A white floor either way.
- **It does not resolve E7** — and makes it **worse**, since a memory *shape* is convention-sensitive
  in a way a dynamics pole would not have been.

**Still owed.**

1. **The E7 repair, before anything can be scored** — and under a continuum this is not cosmetic.
2. **D1's own required proof that a one-clock spectral reduction exists for the assembled object.**
   Without it, `background_time_translation_flow` cannot even become a candidate, and the
   cross-contract fallback applies instead (classification evaluated on the two-time object's
   late-time structure).
3. The mandatory **dual-gauge** report with classification agreement, amplitudes reported never
   averaged.
4. The mandatory **two-prescription scheme test** with classification agreement.
5. **An explicit statement of the continuum's low-frequency EDGE behaviour and its first moment.**
   "Continuum" without the edge is the classification without the consequence, and every downstream
   rewrite depends on which side of S(0) = 0 it lands. **This is the single most load-bearing owed
   item on this branch.**
6. The separately-tracked **P^(0,s)** report.
7. `rung5_gr_limit` restated as a kernel-support limit; `u2` restated off "pole structure";
   `rung7_w2_wa_sign` re-derived or withdrawn; `NO_GO_LEDGER` entry 3 re-graded.
8. **Independent replication of the wall-A assembly itself** — the graviton-probe source-vertex,
   observer-vertex, and external-mode-function corrections, *"none of which exist in the published
   corpus."*
9. The regulator-independence demonstration in the spec's own form.
10. The **CHARTER §4 test on rung1's finite-memory clause**, in the Ohmic sub-case.
11. Owner resolution of the two §0.3 package items — **acute here**, since this branch and outcome 3
    share one registered class.
12. The adversarial pre-screen and the bank gate.

**How it could mislead.**

1. **The central over-read is a sentence already sitting in the register.** rung3's `tier_note`:
   *"Ohmic (Im G_R ~ eta*omega) -> single-pole holds."* Under a continuum with an Ohmic edge, that
   line will be quoted as though the outcome **vindicates** rung 3. It does not — and naming this is
   the most useful thing this branch does. **The sentence classifies at the SELF-ENERGY level (an
   Ohmic friction kernel) and then asserts a conclusion at the RESPONSE level (a pole in
   G_R = 1/(G0⁻¹ − Σ)).** Those are the same object only when a small parameter separates the damping
   rate from the continuum's width. In pure-graviton de Sitter the only scale is H, so there is no
   such parameter — E8's fence restated. The dispatch's declared primary object is `G_R^TT` itself,
   and a continuum stated there means no pole, full stop. **Anyone reading "Ohmic" as "single-pole
   holds" has crossed levels.**
2. **"A continuum spans all frequencies, therefore τ₂ ∼ 1/H₀ is available and w(z) can evolve."** The
   match temptation in its purest form. A continuum of width O(H) contains no weight at 10⁻⁴⁰ H unless
   its edge is an unbroken power law all the way down — which is the **cut** sub-branch, a separate
   claim requiring its own exponent.
3. **"No isolated structure ⇒ no poles ⇒ the Higuchi/Marolf–Morrison stability horn is confirmed."**
   The stability horn is a claim about secular growth being a gauge artifact removed by the assembled
   observable; spectral featurelessness is a different statement and does not adjudicate the
   thirty-year dS-IR controversy.
4. **"Dissipation is continuous and real, so the responsive vacuum is confirmed."** A spectral class
   is not a mechanism.
5. **Structurally the worst: this outcome SOUNDS like the physically expected answer, which invites
   relaxed scrutiny — the exact inversion of CHARTER §1.4.** It is also the outcome most easily
   confused with the class-A proxy's already-computed white floor, which is `not_the_object`.
6. **Citing this sealed map as a prediction.**

**Kill conditions.**

1. Classification disagrees between the two mandatory gauges — *"a structural finding about the
   assembly, not a numerical discrepancy to average."* Not continuum; gauge-dependent.
2. Classification changes with renormalization scheme (Q5) — "scheme-dependent existence", 6-adjacent.
3. The reported low-frequency shape tracks the IR regulator. Note the TT results file already showed a
   **2.3× k_min dependence of the free amplitude**, and *"the regulator prices the NOISE LEVEL"* — so
   a floor that moves with k_min **is the regulator, not physics**.
4. Any epoch or window parameter survives in the final definition — in particular anything inheriting
   the W < 0.25 e-fold window.
5. The "continuum" is the class-A scalar proxy floor re-entering through a borrowed assembly.
6. **Higher-resolution continuation finds isolated structure on the second sheet** — a quasinormal
   tower or a hydrodynamic pole carrying a finite fraction of the low-ω weight. Then the outcome is 1
   or 2. **Given that de Sitter static-patch spectra generically carry discrete towers, this is the
   most likely way this branch dies.**
7. **A nameable branch point with a definite exponent appears** — then it is **outcome 3**, whose
   downstream consequence is *infinite* directional memory, not the reading this branch prices.
8. The result is reported in the static-Killing clock with no bridge to the cosmic clock — then the
   classification is about the static patch, and every cosmological export crosses the C1/C2 mismatch
   `PRIMITIVE_INVERSION_SCOPE.md` flags as *"where it most likely breaks."* An unpaid bill, not a
   discharge.
9. The floor is finite with divergent η (ρ(0) ≠ 0 rather than ρ ∼ ηω) — the free-streaming /
   infinite-viscosity reading, and this branch's finite-memory consequence inverts entirely.
10. The first moment ∫t K(t) dt diverges — then no memory time exists at all and "finite memory
    survives in a different form" must be **withdrawn**, not weakened.
11. The two-time object admits no stationary reduction after all — the classification was read off a
    spectrum that does not exist. Then outcome 5 or 7 owns the question.
12. O(G²) is not the first nonzero order for graviton loops. Featurelessness at a subleading order is
    not a classification of the theory.

**Honest prior.** **Low — roughly 5–10%** of the total outcome mass, below the merged "branch cut /
continuum" class it belongs to. Not defended higher.

Three things push it down. (1) The free-level starting point supplies nothing to build on: E4
establishes the free retarded response is **pole-free**, so a continuum must be manufactured entirely
by Σ, exactly like a pole must. **No free-level head start; the common floor is common.** (2) *"No
isolated structure"* is a strong **conjunctive negative**: absence of a quasinormal tower, absence of
a hydrodynamic pole, **and** absence of a nameable branch point, all at once. De Sitter static-patch
spectra are the textbook home of discrete towers. (3) Within the merged class, the **cut** sub-branch
has a named mechanism behind it — Weinberg free-streaming, banked in rung3's own
`boundary_condition` — while featurelessness has **no named mechanism at all**. A branch with no
mechanism proposed for it should not be assigned the mass of one that has.

One thing pushes it up, modestly: the closest already-computed object, the D3a-licensed scalar
worldline reduction, came back Ohmic-thermal with a white floor and s_eff → 0 — a featureless shape.
But that is the wrong channel, the wrong reduction, and explicitly `not_the_object`, so it is weak
evidence and is not treated as more.

There is also a hard ceiling above every spectral outcome including this one: the TT channel is
non-stationary at free level with >130% shape drift, and D1's recorded consequence names outcomes 5
and 7 structurally likely with *"the pole/cut question may be unreachable."* If the reduction does not
exist for the assembled object, **this branch was never posable.**

---

### Outcome 5 — SECULAR / NONSTATIONARY MEMORY

*Certificate token 5; banked class 4 ("Secular / nonstationary memory") — **the banked class name is
the manifest's, and must be used when filing**.* The assembled, gauge-invariant, resummed
`G_R^TT(x,x′)` admits **no stationary reduction in the clocks tested**; the two-time response grows or
drifts with epoch, and the memory it carries is **epoch-indexed** rather than characterized by a
single rate.

**Verdict in one line.** Rung 3 would not lose the pole-versus-cut argument — it would lose **the
object the argument was about**, leaving GRUT's finite-memory spine bracketed by two exhibited failure
modes (the proxy's zero-memory white floor below, epoch-indexed unbounded memory above) with the thing
the node actually claims produced by neither.

**What it would mean.** The registered mechanism loses its **object** rather than its truth value.
rung 3 asserts a statement about K_R(ω), a function of one frequency. If the assembled `G_R^TT`
admits no stationary reduction, there is no K_R(ω) **for the assembled object**, and "single pole" is
neither true nor false of it. In one respect that is worse for GRUT than a branch cut: a cut would at
least have decided the fork against the node; this leaves the fork **undecidable in the frame the
framework wrote it in**, while removing the frame's warrant.

**The damage is IR-localized, and that localization is the result's most useful feature.** Everything
stated at short separation and high frequency survives untouched — the contact/UV domain, χ_∞, the
WKB-valid H ≪ ω regime (rung3's own 2026-08-18 closure already concedes *"the WKB reading is valid in
the regime the single-pole conjecture does not live in, and invalid in the one it does"*), and the
Kramers–Kronig partnership as a structural fact about causal response functions. Everything stated
about **late-time memory** — the memory time, the ω → 0 transport coefficient η, the single-pole
spine — is left without a defined object.

GRUT's claim then sits between two now-exhibited failure modes: the proxy's horizon-forced white floor
(zero memory) below, epoch-indexed unbounded memory above. **Finite memory is precisely what neither
computation produces.**

Second, it converts a booked assumption from retirable to standing. `background_time_translation_flow`
is priced +1 with a named discharge, and if the static-Killing clock was among those tested and failed
for the assembled object, **that route closes**. The number does not move; the *expected* number does.

Third, constructively: it hands the program a well-posed replacement question — **classify the
growth** — which is publishable de Sitter physics independent of GRUT, and re-poses u2's universality
question on a growth exponent rather than a pole structure. **That is a smaller programme than the one
it replaces, and it should be described as smaller.**

**Register moves.**

| node | tier / Δ now | proposed | why |
|---|---|---|---|
| `rung3_single_pole` | derived-pending / **0** | → `assumed`; `moot` added to `sub_status`, **scoped in-field to the spectral predicate only**. Δ under **RULE L1: owner adjudication** | *"derived-pending"* means derived modulo a **named open input**; the named input (the transport self-energy Σ) was supplied and returned **no object for the predicate**, so nothing is pending. A +1 lands **only if** the framework continues downstream to use a single memory time — which then becomes an unsourced input. Explicitly **NOT `refuted`** and **NOT `settled-negative`** on the node itself: no pole is shown absent. Over-grading here is the failure mode this program exists to prevent. |
| `background_time_translation_flow` | assumed / **1** | **Δ UNCHANGED**; `sub_status` gains a settled-negative marker scoped **in-field to the discharge ROUTE, not to the claim** — **and only under a stated condition** | Its route is quoted: *"the declared background is one carrying a timelike Killing vector… this node retires into that declaration at zero."* This move is licensed **only if the static-Killing clock was among those tested and failed for the ASSEMBLED object**. If the computation ran only in the cosmic/worldline clock there is **no move here** — and the report must say which clocks were tested. Note RULE L2 already blocks the favourable direction independently. |
| `rung5_gr_limit` | assumed / **2** | tier and Δ **UNCHANGED**; statement repair owed | *"tau_c -> 0"* has no τ_c to send to zero if no single memory time exists. Restate as a short-separation / high-frequency limit, or retire the phrasing. A wording defect of the same class as E7 — **not a ledger event**. The +2 (area entropy, Unruh T) is untouched and entry 6's BORROWED grade is unaffected. |
| **`rung1_inin_action`'s finite-memory clause** | shown / **4** | **CHARTER §4 compound/omission test OWED AND BLOCKING** | Unbounded, epoch-indexed memory contradicts *"a responsive medium with finite memory"* as squarely as zero memory does. **This branch notices the premise failure and must route it, not merely note it** — that gap is exactly what §3 discloses. Run the §4 test; do not assume the repair. |
| `u2_kernel_universality` | to-derive / **0** | tier **UNCHANGED**; a **re-pose** owed in `tier_note` | Its statement asks about *"the low-omega pole structure"*, which on this outcome is not the object. The candidate universal becomes the **growth exponent / envelope class**. The one place this outcome opens genuinely new u0-charter-compliant work — and it is a **smaller** question than the one it replaces. |
| `u5_constitutive_phases` | to-derive / **0** | tier **UNCHANGED**; the rung3-gated **placement** acquires its first substantive constraint, recorded as a **live tension** in `tier_note`, not as a placement | [INFERENCE] A nonstationary/aging response sits outside the relativistic, passive, KMS-equilibrium viscoelastic-transport sector u5 banked as surviving, while rung2's KMS state fence still holds — **the state is KMS with respect to a flow the assembled response does not respect.** u5's own fence rides: exclusion is not uniqueness, and this is not the placement. |
| `kk_static_transfer` | derived-pending / **0** | **UNCHANGED** | One named sufficient route (the vanishing-χ_∞ single-pole class) closes — but the input lives in rung3's **UV/contact domain**, exactly the domain this outcome does **not** damage. Net: one fewer sufficient route, same tier, no delta. |
| `rung8_falsifier` | to-derive / **2** | tier and Δ **UNCHANGED**; a **scope marker owed on the "quiet" leg** | Entry 4's obstruction rests on the diagonal coupling sampling S(0) = 0; on this outcome S(0) is **undefined** rather than zero. *"Undefined"* is **weaker** than *"zero"*, so this **weakens a banked negative export rather than helping GRUT** — a cost to an export's defensibility, recorded as a cost. RULE L3 still bars any TT→scalar import. |
| `rung7_wz` | to-derive / **3** | **UNCHANGED in BOTH directions**, stated as net zero | The "single-pole forbids a second bath scale" coupling dissolves — but it was never binding (the node's own fence has the two coexisting by ~40 orders), and double-count check (4) blocks inheritance anyway. Against that, the node's statement *"a relaxing chi(omega) yields an effective w(z)"* loses its object exactly as rung3's does. The sourced prediction w = −1 flat is untouched. The tempting reading — that epoch-dependence could source w(z) drift without a second pole — is a **to-derive item only**, and it **inherits the background history as an input**: the priced-input-not-a-result shape. |
| `mu_linear` | derived-pending / **0** | **NO MOVE — and this branch declines it explicitly** | The trigger fires on *"Pi_0 != 0 ESTABLISHED"*. A nonstationary assembled response leaves Π₀ neither established nor refuted — arguably it makes "Π₀ = 0" *harder to define* for the same reason. Reading the trigger as fired here is a misreading of its predicate. The μ=4/3 endpoint exclusion is untouched. |
| `p_tt_ansatz` | assumed / **1** | **NO MOVE** (RULE L3) | No bath-microphysics commitment is supplied. The +1 stays. |
| `arrow_of_time` | assumed / **1** | **NO MOVE** | Its `boundary_condition` already pre-writes the non-KMS / NESS case: *"EITHER WAY the direction is state-dependent."* **Finding the disposition pre-written is evidence the node was well scoped; it is not a result of this branch and must not be reported as one.** |
| `rung4_love_kk` | shown / **0** | **UNCHANGED** | Its overturning computation is structural and is not met. The named loophole is **not** opened: [INFERENCE] ln-a-class growth across ~60 e-folds buys ~10²–10⁴ against a 10²¹–10⁶² deficit. **State the arithmetic rather than the hope.** |
| `rung9b_bridge` | assumed / **0** | **NO MOVE** | Reopen condition is narrowly a scalar→TT operator identity. |
| `rung1_inin_action` fourth input | shown / **4** | **NO MOVE** | Retires only into `eft_operator_basis`'s own graduation screen. |
| `NO_GO_LEDGER.md` | — | **candidate** entry at **SETTLED-NEGATIVE**, not on arrival (§1.4) | *"No parameter-free memory time exists in the assembled class-C gravitational response."* Obstruction: absence of a stationary reduction for the assembled two-time object. **Named rescue:** a formulation with the epoch window priced as a named input in the error budget, a different gauge-invariant assembly, or a higher order. **NOT FORBIDDEN.** |
| **new draft node** | — | *"the assembled class-C gravitational response is nonstationary; memory is epoch-indexed rather than single-rate"* — tier `derived-pending` **at best**, gated on D4-Q5 and D5-Q5 | A DISCOVERY RESULT about de Sitter; carries no favour. |

**What it does NOT buy.**

- **It does not refute the pole.** No pole is shown absent; the *predicate* is shown to have no
  referent in the assembled object. rung 3 becomes `assumed` + `moot`-on-the-spectral-predicate,
  never `refuted`, and never FORBIDDEN.
- **It does not establish the branch cut or Class B.** The register's own third/symmetric correction
  stands: *"our earlier 'secular => cut => REFUTED-leaning' over-identified a secular logarithm with a
  transport branch cut… the secular log is real but establishes NO cut."* The two are separated by
  exactly the ω → 0 continuation this outcome says does not exist. **Anyone converting outcome 5 into
  "Weinberg free-streaming confirmed" is recommitting a retracted error.**
- **It does not vindicate a responsive vacuum.** Epoch-indexed unbounded memory contradicts *finite*
  memory as hard as the proxy's white floor does, in the opposite direction. **GRUT's registered claim
  is produced by neither computation.**
- **It does not fire `mu_linear`'s trigger, reach `p_tt_ansatz`'s escape or retire its +1, discharge
  rung1's fourth input, move `arrow_of_time`, or satisfy `rung9b_bridge`'s reopen condition.**
- **It does not discharge `background_time_translation_flow`** — RULE L2 blocks it, and this outcome
  is the one that most plausibly *closes* its named route rather than opening it.
- **It does not rescue any observability.** rung4's deficit is 21–62 orders; rung8's off-diagonal
  wedge is 7–47 orders down. ln-a-class growth over the available history is ~10²–10⁴. **Nothing
  crosses.**
- **It does not damage the UV/contact domain.** χ_∞, short-separation statements, KK-as-structure, and
  the WKB-valid H ≫ ω regime all survive; the damage is IR-localized and should be reported as such.
- **It does not weaken the class-A fences it superficially resembles.** The free TT channel was
  *already* non-stationary; that is a class-A fact about the free object, and this outcome is a claim
  about the **assembled interacting** one. Reporting the second as though it inherited the first's
  evidential support is the inheritance error this branch's kill condition 3 exists to catch.
- **It does not give the framework a two-time formalism.** It creates the *obligation* to build one.
  Obligation is not capability, and an unbuilt formalism cannot carry a single downstream export.
- **It does not survive its own dispatch contracts by default.** Until D4-Q5 and D5-Q5 both pass this
  is a **candidate** classification, not a physical one — and it is **the outcome class most exposed
  to the gauge-artifact horn**, since the growth being gauge is precisely the live alternative.
- **It does not license retiring the class-A scope fences**, and it does not resolve the §0.3 package
  discrepancies.

**Still owed.**

1. **The D4 dual-gauge acceptance test**: the *classification* must agree between gauges. A
   disagreement is a structural finding about the assembly — and it would move this result **out of
   this class**.
2. **The D5 Q4/Q5 scheme-independence test.** If the classification changes with scheme the answer is
   "scheme-dependent existence", recorded as such — not this outcome.
3. **Classification of the growth itself**: exponent / envelope (power in a? polynomial in ln a?
   saturating?), and whether it is **bounded**. **A saturating growth is a long-but-finite memory time
   and belongs in a different outcome class entirely** — the report must distinguish these *before*
   the class name is written.
4. **Demonstration that the growth is Σ's and physical**, not the free-level epoch dependence already
   exhibited at class A re-entering under a new name. **This branch's burden is inverted relative to
   the pole branches**: the free theory already points here, so inheritance is the default suspicion.
5. **The x′ integration of TTW eq. (109)** — the step that converts a position-space ln(H²Δx²) into
   time-domain secularity, listed by that paper's own epilogue as not done. Without it, "secular" is
   not established even in the in-out object.
6. **The Schwinger–Keldysh conversion** (wall C).
7. **The E7 kernel-phrase repair** — the three candidate MZ objects will not behave alike under
   nonstationarity, so this repair becomes **blocking rather than tidy**.
8. **Restatement or retirement of rung5's "tau_c → 0" phrasing**, plus an audit of every downstream
   use of a single-frequency kernel K_R(ω,k) — restate on the two-time object or mark scope-limited.
9. **A named, priced epoch window in the final error budget** wherever a window was unavoidable, with
   the k_min dependence separated from the epoch dependence. **The two were conflated once already**,
   and the separation is the exact laundering shape the process catches.
10. **The CHARTER §4 test on rung1's finite-memory clause.**
11. Owner adjudication on the two §0.3 package items.
12. The four-lens screen and the bank gate on every move above.

**How it could mislead.**

1. **"The vacuum has MORE memory than GRUT claimed — the mechanism is stronger than registered."** The
   wish-list reading, and wrong: the node asserts **finite** memory with a **single rate**. The
   registered claim is bracketed, not vindicated.
2. **"Nonstationarity is a prediction of a responsive vacuum."** It is not.
   `background_time_translation_flow` was booked as an **OMISSION** — a presupposition the framework
   had been silently using (*"'stationar' occurs ZERO times in S_IF.md"*). **Retro-fitting a failed
   presupposition as a prediction is the precise laundering shape the register books omissions to
   prevent.**
3. **"Secular growth means branch cut means Class B means rung3 refuted."** Retracted in-register
   twice. This outcome delivers no cut and no Class B.
4. **"The keystone is settled; the dispatch can close."** Backwards. This is the class most exposed to
   the Higuchi/Marolf–Morrison horn, and the literature's own status is that this is unresolved. Until
   D4 passes, a class-5 report is a candidate, not a verdict.
5. **"τ_eff(t̄) is the derived memory time."** An epoch-indexed τ is a family, not a time, and it
   carries the epoch as an input. This is the class-A defect (0.40/0.33/2.40, non-monotonic)
   reproduced one level up.
6. **"This is the program's first FORBIDDEN no-go."**
7. **"Epoch-dependent memory explains cosmic aging / DESI's w(z) drift."** The match temptation, aimed
   at the one channel where a number could be made to land near an observed one. Any w(z) built from
   an epoch-dependent kernel **inherits the background history as an input**.
8. **THE MIRROR FAILURE, stated because this branch is adverse and CHARTER §1.4's asymmetry therefore
   does not protect it.** An author can *perform* rigour by inflating an adverse reading past what the
   computation gives — reporting "the question is malformed" when the computation showed only "one
   reduction failed," or sweeping nodes into the blast radius that the IR-localization argument
   explicitly spares. **Both directions need the screen**, and this branch's own DOES-NOT-BUY list is
   the instrument for the adverse direction.

**Kill conditions.**

1. **Dual-gauge disagreement on the classification** (D4 acceptance) — a structural finding about the
   assembly, 6-adjacent, not this outcome.
2. **The classification changes under a second renormalization prescription** (D5-Q5) —
   "scheme-dependent existence", and this branch dies.
3. **The growth vanishes, changes character, or becomes k_min-tracking as the IR regulator is
   removed** — the class-A regulator artifact re-entering, barred by `not_the_object`, and this branch
   dies as laundering.
4. **The growth is removable by a field redefinition, or is exhibited as a gauge mode** (the
   Higuchi/Marolf–Morrison horn) — artifact, not memory.
5. **A Sudakov / entire-function resummation exponentiates the logarithms** into a decaying or bounded
   envelope — the assembled object is effectively stationary after all, and the outcome moves to 1, 2
   or 3. (The register already fences the in-house version of this inference as ours-and-unverified;
   it must come from the computation.)
6. **The growth SATURATES.** A bounded envelope is a long-but-finite memory time — a different, and
   for GRUT more favourable, outcome, which must be reported as that outcome rather than filed here.
7. **A static-Killing reduction of the ASSEMBLED object is exhibited** even though the cosmic/worldline
   reduction fails — the spectral question is reposed there rather than abandoned.
8. **The two-time object admits no classifiable late-time structure at all, in any clock** — the result
   is outcome 7, and this branch must yield rather than claim the milder reading.
9. **O(G²) turns out not to be the leading nonzero order** for graviton loops.
10. **The growth is exhibited only inside an epoch window narrower than the phenomena described**, and
    no window-independent statement survives — then nothing was classified, and the honest report is a
    priced input, not a result.
11. **The nonstationarity is exhibited only for the free kinematics carried through the assembly**,
    with Σ's contribution consistent with zero at the achieved precision. Then the result restates
    class A at a new order and is not a class-C classification of anything.
12. **No growth exponent or envelope class can be extracted at all.** "It drifts" without a
    classification is not outcome 5; the spec's own requirement is *"classify the growth."* An
    unclassified drift routes to outcome 7 or to still-open, never here.

**Honest prior.** **High that the computation is REPORTED in this class; substantially lower that it
survives as a banked physical classification.** Roughly **40–50%** on the first and **15–25%** on the
second, and **the gap between those two numbers is the whole content of this field.**

*Why the first is high.* Three independent things already point here. (i) D1's own recorded
consequence — written before any result existed and therefore not a preference — makes this and
outcome 7 *"structurally likely paths."* (ii) The free TT-graviton geodesic kernel is **already
non-stationary in-house**: >130% shape drift across epochs, including a change of character, with
stationarity only for W < 0.25 e-folds. The minimally-coupled-like spin-2 sector has no de
Sitter-invariant state. (iii) The assembled object must inherit that free kinematics, and nothing in
the declared O(G²) order is obviously capable of restoring a stationarity the free theory lacks.

*Why the second is much lower — the part an author of this branch is most tempted to omit.* **The very
facts that make the outcome likely make it hard to CREDIT.** Σ is required to supply the **least** here
of any of the seven shapes, so the default explanation of any observed growth is that it is the free
epoch-dependence already known, or the k_min regulator, or gauge. The gauge half is unresolved by the
literature's own admission, and the Higuchi/Marolf–Morrison horn is precisely the claim that de Sitter
secular growth is a gauge artifact removed by the assembled observable. **D4's acceptance test is a
real test that this outcome is more likely to fail than the pole branches are.** A meaningful slice of
the mass also collapses into outcome 7 on close reading, since the line between "grows, classifiably"
and "admits no reduction in any clock" is thin and is decided by whether a growth exponent can
actually be extracted.

*Net:* plausibly the modal outcome of the dispatch and simultaneously one of the weakest outcomes to
bank. Neither half is inflated.

---

### Outcome 6 — NO LONG-MEMORY STRUCTURE

*Certificate token 6; banked class 5 ("No long-memory structure").* The fully assembled,
gauge-invariant, IR-resummed retarded `G_R^TT` carries **no low-frequency memory structure at all at
the declared order** — no relaxation pole, no ladder, no branch cut, no long tail, no secular growth
surviving assembly. ρ_TT(ω→0) is either **identically zero (case A: no dissipation)** or a
**featureless Ohmic-thermal white floor with no associated rate (case B: zero memory)**. The friction
kernel is contact/instantaneous; no τ_phys with ∂τ_phys/∂k_min = 0 exists because there is no
relaxation structure to extract one from.

**Verdict in one line.** Outcome 6 retires rung 3 exactly as the spec pre-wrote it — *"rung-3
mechanism fails as registered; retire and say so"* — and because "finite memory" sits inside
`rung1_inin_action`'s own `shown`-tier, Δ4 statement, **it lands on the foundation rather than the
frontier**: a settled-negative-flavoured result (never FORBIDDEN), scoped to the TT channel at O(G²)
in dS/BD, that buys the program a clean ending and nothing else.

**What it would mean.** The registered mechanism dies on its own terms. A null at ω→0 in the assembled
response says there is no structure to collapse to and no rate to name.

**The damage does not stop at rung 3, because "finite memory" is not only rung 3's word.** It sits
verbatim inside `rung1_inin_action`'s statement — *"The gravitational vacuum is a responsive medium
with finite memory"* — at tier `shown`, Δ4; and `u6_constitutive_order`'s own text already concedes
*"the single pole, which WAS the finite-memory premise renamed."* So outcome 6 **contradicts a clause
inside a shown-tier node.** By CHARTER §4's tell this is a **COMPOUND**, not an omission — the
candidate appears in the node's own statement — and rung1 carries two separately-dischargeable things:
the Schwinger–Keldysh influence-action **FORM** (discharges alone via Feynman–Vernon;
`u1_form_universality` already grades that form generic) and the **finite-memory constitutive
characterization** (never discharged alone; **rung 3 *was* its discharge**). **Repair is to split
rung1**, keep `shown` and the Δ4 — including the KC5-reserved fourth input — with the form-half, and
book the constitutive half where outcome 6 can reach it. *"Applying the wrong repair here manufactures
a false dependency graph."*

Physically, [INFERENCE] outcome 6 is the Higuchi/Marolf–Morrison IR-stability horn winning: the free
TT channel's secular, epoch-dependent, regulator-priced structure turns out to be **assembly-removable**,
and the observable is trivially analytic at ω→0. It also means the vacuum sits **at** rung5's τ_c → 0
GR limit in the TT channel — not near it — so GRUT's distinguishing low-frequency gravitational content
is zero at the computed order.

**A clean termination is first-class by this charter. It is still a loss.**

**Register moves.**

| node | tier / Δ now | proposed | why |
|---|---|---|---|
| `rung3_single_pole` | derived-pending / **0** | **REFUTED**, marker in `sub_status`, with a mandatory scope string on the face (TT channel, O(G²), dS/BD, dual-gauge and two-scheme agreement passed). Δ under **RULE L1: owner adjudication** — the suspended −1 is never earned, and a +1 lands only if the framework keeps using a memory time it now knows it does not have | **PRECONDITION**: the E7 statement repair must land **before** the refutation banks, so the record names **which object** was refuted. *"Retiring a non-denoting statement is not a result."* |
| `rung1_inin_action` | shown / **4** | **COMPOUND SPLIT** (CHARTER §4: split, do not add). `shown` and Δ4 — including the KC5-reserved fourth input — **stay with the FORM half**, untouched by class C | Test *"can one part discharge alone?"* passes for the form and fails for finite memory. |
| **new node from the split** (working id `finite_memory_constitutive`) | — | tier `refuted-in-scope`, `sub_status` `refuted`, **Δ candidate +1 rather than 0 — flagged as the branch's single largest proposed ledger consequence and the one most in need of hostile screening** | Outcome 6 does not merely leave finite memory underived, it **contradicts** it in the one channel where it has been computed — the same shape the proxy result already fenced. The framework must then either book it as a scoped input known false in its test channel, or drop it; **dropping it silently while retaining responsive-vacuum language is fiat exclusion.** Owner adjudication required. |
| `background_time_translation_flow` | assumed / **1** | **Δ HELD**; may become `derived-pending` **in scope** only if outcome 6 arrives via a *proven* stationary reduction — and the −1 is blocked regardless (RULE L2) | Even on the favourable reading the presupposition is framework-wide while the proof is TT/O(G²)/dS-BD only, and the register's own precedent is that a +1 retires only through the discharging work's own graduation screen. If outcome 6 instead arrives on the two-time object's late-time structure, this move does not apply at all. |
| `mu_linear` | derived-pending / **0** | **NO MOVE — recorded explicitly as a non-move** (RULE L3) | A no-structure verdict in TT establishes **neither** Π₀ ≠ 0 **nor** Π₀ = 0 (a contact/local trace correlator is structureless **and nonzero**). |
| `p_tt_ansatz` | assumed / **1** | **NO MOVE** | The ONE ESCAPE requires a **non-perturbative vanishing** — not delivered. The +1 stays; CHOSEN stays; the μ=4/3 endpoint exclusion untouched. |
| `rung5_gr_limit` | assumed / **2** | tier and Δ **UNCHANGED**; `tier_note` only | Outcome 6 **delivers** τ_c → 0 as a computed answer rather than as a taken limit. But its +2 is **area entropy (fixes G) and Unruh T (fixes ħ)** — the action-selection imports of entry 6 (BORROWED) — which outcome 6 does not touch. **The "GR is now derived" read is barred at the node.** |
| `rung4_love_kk` | shown / **0** | tier and Δ unchanged; entry 5's spec-for-completion **NARROWS** | The named *"bath resonance / collective IR mode"* rescue closes at O(G²) in the TT channel — the one channel LIGO measures — leaving only ω_c ∼ MeV–meV (grossly excluded). Candidate **new** ledger entry at SETTLED-NEGATIVE (not on arrival, §1.4; explicitly **not** a promotion of entry 5 and **not** FORBIDDEN): *"no collective IR mode in the assembled TT vacuum response at O(G²) in dS/BD"*, rescues named (higher order in G, other backgrounds/states, the P^(0,s) channel). **Also a candidate discharge of the owed `calc/gw_tensor_friction.py` obligation**: Γ_T = 0 at this order, computing rather than quoting the un-backed "few × H₀" inference. |
| `rung8_falsifier` | to-derive / **2** | **NO MOVE if TT-only**; **FLAGGED-REOPEN** if the mandated P^(0,s) tracking independently returns a nonvanishing white floor | rung8's quiet verdict rests on S(0) = 0 in the **diagonal (energy-density, scalar)** coupling. **Case A (η = 0) would corroborate that mechanism dynamically; case B (S(0) = 2Tη ≠ 0) would FALSIFY it** and reopen the magnitude question in the framework's favour on observability. **This is the one place outcome 6 could cut toward GRUT, and RULE L3 bars taking it from the TT verdict** — it must be earned in the scalar channel or not at all. |
| `kk_static_transfer` | derived-pending / **0** | stays derived-pending; its **named sufficient route closes** | Outcome 6 makes χ_∞ the **entire** low-frequency response rather than a vanishing contact piece, so the vanishing-χ_∞ route dies and the sign question becomes the whole content — **sharper, not resolved.** |
| `u5_constitutive_phases` | to-derive / **0** | general classification stays to-derive; the **GRUT-vacuum PLACEMENT** moves to `derived-pending` in scope | Outcome 6 supplies the kernel and the placement: the **trivial / Markovian-contact class**, admissible under u5's banked filter (passive, causal, KMS-compatible). **A placement delivered, not an exclusion.** |
| `u2_kernel_universality` | to-derive / **0** | no tier move; **the question survives with its object hollowed** | It becomes *"is triviality universal?"* — still first-class (its `sub_status` pre-authorizes under-determination), but **no longer the place a distinguishing prediction could live.** |
| `rung7_wz`, `rung7_w2_wa_sign`, `rung7_w3_nocrossing_export` | to-derive / **3, 0, 0** | **no arithmetic move**; scoped note only | Double-count check (4) fences rung7; τ₂ lives in the scalar sector where RULE L3 bars a TT export. What changes is prospective: the inserted second scale loses its last named route to being **sourced** by the vacuum's own TT dynamics. **`NO_GO_LEDGER` entry 3's *"conditional on the open rung3"* resolves VACUOUSLY, not favourably** — the anchor retires rather than confirming, so the no-crossing export inherits **no** strength from it and stays to-derive. |
| `arrow_of_time` | assumed / **1** | **no move**; scoped tension recorded **only under case A** | An exactly vanishing η in the TT channel at O(G²) sits in tension with *"EXISTENCE of dissipation = intrinsic (shown-grade)"* for that channel at that order. **That is a magnitude-at-an-order statement, not a non-existence proof: record as tension, refuse the move.** |

**What it does NOT buy.**

- **It does not refute GRUT.** It refutes **one clause**, in **one channel** (TT / P^(2)), at **one
  order** (O(G²)), on **one background**, in **one state**, under **one assembly**. Strength ceiling:
  SETTLED-NEGATIVE, and not on arrival (§1.4).
- **It does not reach the scalar sector by content** (RULE L3), so `mu_linear`, `p_tt_ansatz`,
  rung7's τ₂, rung8's S(0)=0, and the whole trace-correlator front are untouched unless the mandated
  P^(0,s) tracking independently returned the same null. **The single most-wanted discharge in the
  package — p_tt CHOSEN → FORCED — is exactly as open after outcome 6 as before.**
- **It does not decide the leading order.** *"whether O(G^2) is actually the first nonzero order FOR
  GRAVITON loops is UNESTABLISHED."* **A clean null at an order that was never leading is a null about
  nothing**, and D3's recorded consequence is explicit that higher orders are new physics inputs
  requiring their own pricing.
- **It does not retire rung1's KC5-reserved fourth input, reopen `rung9b_bridge`, touch rung4's KK
  structure** (which rests on causality and passivity, not memory), **or derive GR** (rung5's +2 is
  area entropy and Unruh T, not τ_c).
- **It does not establish that de Sitter has no IR physics.** Free-level secularity and
  non-stationarity remain real; outcome 6 says only that they are **removed by the assembled
  observable** — a statement about the observable, not about the spacetime.
- **It buys no empirical standing whatever.** There is no datum in this result; nothing here is
  EMPIRICALLY EXCLUDED, and nothing bears on the pre-registered termination channels, **which may
  never be reported on a subset.**

**Still owed.**

1. **The rung3 statement repair, BEFORE the refutation banks.** A retirement that does not name which
   object it retired is not a result.
2. **The two sub-cases reported DISTINCTLY, never merged into "no memory":** case A (η = 0, a verdict
   about **responsiveness**, reaching rung1 and `arrow_of_time`) and case B (Ohmic-thermal white floor,
   η ≠ 0 with no rate — a verdict about **memory** only, and the one that reopens rung8 in the scalar
   channel). **Their register consequences differ and the outcome class does not distinguish them.**
3. **The CHARTER §4 compound/omission adjudication on `rung1_inin_action`, run properly rather than
   assumed.** This branch reads it as a compound because the candidate appears in the node's own
   statement — but the register's own history is that two of five pre-registered candidates were
   mislocated. **Run the test.**
4. **The P^(0,s) channel result.** Outcome 6 in TT alone is a half-answer to a two-channel question.
5. **The higher-order question, explicitly priced.**
6. `gauge` and `renormalization` remain `UNDECIDED-DISPATCH`. Outcome 6 does not resolve them — it
   **presupposes** their resolution under D4/D5, and any report reading a null without them is reading
   a gauge-fixed, unrenormalized object.
7. **`calc/gw_tensor_friction.py`**, still owed; the un-backed "few × H₀" inference is still not
   banked. Outcome 6 makes it computable — **compute it, do not quote it.**
8. The four-lens screen and the bank gate.
9. **A written decision on whether the responsive-vacuum framing survives a refuted finite-memory
   clause without fiat exclusion** — and if it is rescoped out of the TT channel, the *physics* reason
   for the rescoping, not the convenience.
10. **A check of outcome 6 against the in-force termination pre-registration** (see §3): does a
    keystone retirement trip any channel, and does the no-subset-reporting rule bind here?
11. Owner resolution of the two §0.3 package items.

**How it could mislead.**

1. **The over-read this branch invites first and worst: rung 3's statement says "single-pole /
   Markovian-like," and a white floor IS Markovian.** Someone can report outcome 6 as **confirming**
   rung 3 by satisfying a disjunct — while the thing the disjunct existed to supply (a single named
   rate, a finite τ, *the* memory time) has been destroyed. **That is laundering in its purest form:
   confirming the sentence by killing its content.** It must be pre-barred on the face of any
   outcome-6 report, and it is why the statement repair is owed *before* the retirement banks.
2. **The proxy-agreement over-read.** Outcome 6 is precisely what the class-A proxy points to
   (Ohmic-thermal, white floor, s_eff → 0), and that agreement will *feel* like corroboration. It is
   not: the proxy is on `not_the_object` and the scalar-probe assembly is barred. **Agreement between
   a barred proxy and the assembled object is a coincidence to REPORT, never a corroboration to bank
   — and if anything it should raise suspicion that the proxy re-entered through the assembly.**
3. **"GRUT is dead."** A one-channel, one-order, one-background, one-state null read as global
   refutation.
4. **"GR is recovered, so GRUT derives GR."** Seductive, and barred at the node: GR is BORROWED and
   rung5's +2 does not move.
5. **"The de Sitter IR controversy is settled."** One assembled observable at one order is a real
   discovery result and is not the general theorem.
6. **Structural: a clean termination will feel like progress.** A program blocked on a keystone for
   months can let the *ending* substitute for the missing result and bank relief as content. It is not
   content. **And the mirror failure is live too** — because this outcome is adverse, CHARTER §1.4's
   asymmetry does not protect it, and an author can *perform* rigour by inflating an adverse reading
   past what the computation gives. **Both directions need the screen.**

**Kill conditions.**

1. **Dual-gauge classification disagreement** (D4-Q5) — a structural finding about the assembly, not
   outcome 6, and not averageable into one.
2. **Two-scheme classification change** (D5-Q5) — "scheme-dependent existence", **outcome-6-ADJACENT
   and explicitly a different, decisive structural result.** Not this branch.
3. **The null tracks `k_min`, or survives only inside a priced epoch window** — a priced input, not a
   result.
4. **Wall A undischarged**: the assembly was scalar-borrowed. Then the object computed is not the
   registered object and outcome 6 is a statement about nothing.
5. **Wall C undischarged**: the null was read off the in-out object without the SK conversion. An
   absence there is wrong at the definition.
6. **Wall B undischarged**: the RG half not done, so the "resummed" object is not resummed. A null
   before resummation is the un-resummed object's null.
7. **The mandated P^(0,s) tracking shows low-frequency structure.** Then this is a **channel-split**
   result — "no memory in TT, structure in the scalar sector" — a different and more interesting
   verdict, and one that reaches `mu_linear`, rung7 and rung8 where outcome 6 as written does not.
8. **O(G²) is shown NOT to be the first nonzero order for graviton loops.**
9. **The preserved physics-dependent gates fail**: the assembled response does not recover the correct
   H → 0 limit, or violates KMS, or has the wrong weak-coupling Σ limit. Then the object is not the
   physical one and the null is a bug. (These four gates are named on the freeze certificate's own
   face as *"blocked on class C execution"* — they come due exactly here.)
10. **The null is η = 0 exactly rather than an Ohmic white floor.** Then it is not "no MEMORY", it is
    **"no RESPONSE"**, bearing on rung1's responsiveness clause and on `arrow_of_time`'s
    dissipation-existence grade — a deeper verdict that must be reported under its own description,
    not folded into this class.
11. **Any stage of the chain FAILED rather than returned nothing.** A failed arrow routes to
    ill-posed-after-assembly. **"We could not find it" and "it is not there" are different results and
    only the second is this branch.**

**Honest prior.** Stated as calibrated judgment, not a computation — **subjective, non-consumable, and
not to be quoted downstream as a number** (this program's own every-load-bearing-number-has-a-calc
rule binds here).

**Conditional on the computation completing** — all three arrows succeeding and both agreement tests
passing — roughly **35–45%**, competing mainly with branch-cut/continuum. The case is real and mostly
on the record: the free retarded response is **pole-free**, so every shape must be manufactured by Σ
and none inherited; the O(G²) rate is suppressed as Γ/H ∼ (H/M_Pl)⁴, a structure so thin it is nearly
indistinguishable from nothing; the proxy reduction already returned Ohmic-thermal with s_eff → 0; the
frozen-TT fence keeps the trivial/no-response horn explicitly live (*"equally consistent with a
razor-thin pole or a trivial no-response; both horns stay live"*); and the IR-stability horn is a
mainstream, well-supported position. **The register's own base rate is also adverse to structure** —
every promising spectral shortcut so far (secular-log ⇒ cut, Matsubara ⇒ pole, gapped-tower ⇒ QNM) was
killed.

**Unconditionally, much lower — roughly 15–25%** — and that asymmetry belongs on the face of this
document, because it is where this branch is weakest. **To report "no structure at ω→0" you must have
SUCCEEDED at every arrow and found nothing.** Three walls stand. D1's own recorded consequence names
the nonstationary and ill-posed paths structurally likely — **and those are other branches.** The free
TT channel is non-stationary at >130% drift, so **the assembled object must be TAMER than its free
counterpart** for this branch to land: a strong demand, not a default. And the ln(H²Δx²) factors in
the graviton-loop Table 8, once SK-converted into θ(Δη−r)·ln[H²(Δη²−r²)], point toward **causal branch
structure rather than toward nothing** — un-renormalized and unintegrated, so establishing nothing, but
a hint pointing away from this branch.

One asymmetry note this branch will not hide behind: CHARTER §1.4 says the loop over-claims toward
strengthening GRUT, **so an adverse branch does not get its scrutiny discount automatically.** The
mirror failure — inflating an adverse reading, or inflating one's own prior, to perform rigour — is
equally available.

---

### Outcome 7 — ILL-POSED EVEN AFTER ASSEMBLY

*Certificate token 7; banked class **6** ("Ill-posed even after assembly") — **"outcome 7" is a token
that exists only in the immutable certificate's slash-list; the machine-readable face numbers this
class 6.** A result banked against "class 7" is banked against nothing (§0.3).*

The gauge-invariant graviton-probe assembly is constructed (wall A discharged), the RG half of the
resummation is closed (wall B), and the SK conversion is performed so the object is genuinely retarded
(wall C). **And then the registered question does not type-check**: the assembled `G_R^TT(x,x′)`
admits no reduction to a function of one time difference **in any clock** — not comoving-worldline
(D3a does not transfer), not static-Killing (the one global candidate, D3b), not any other — and no
de Sitter-invariant spectral decomposition either. ρ_TT(ω→0) and η are therefore **not objects**, and
"pole vs cut vs ladder vs floor vs none" is a question about a function that does not exist.

**Three distinct realizations land in this class and carry different grades, and they must be reported
separately, never merged:**
- **(7a)** the structural no-reduction-in-any-clock result — attaches to the **physics**;
- **(7b)** D4-Q5 returning a **classification disagreement between gauges** — *"a structural finding
  about the assembly, not a numerical discrepancy to average"* — attaches to the **assembly**;
- **(7c)** D5-Q5 returning **scheme-dependent existence**, which that contract pre-labels *"outcome
  class 6-adjacent"* — attaches to the **prescription**.

**Verdict in one line.** Rung 3 would not be refuted but **VOID** — its predicate has no referent in
the one channel GRUT's own kernel `K^R = αχ(ω)P^TT` lives in — and the earned strength is
settled-negative on the **one-frequency formulation** of the vacuum's gravitational response, not a
FORBIDDEN no-go, with no suspended credit recovered anywhere.

**What it would mean.** The failure would be in the **vocabulary**, not the answer. GRUT's entire
quantitative surface is written in one-frequency kernels: `p_tt_ansatz` states K^R = αχ(ω)P^TT; rung4
asserts a Kramers–Kronig partnership between Re[χ](ω) and Im[χ](ω); rung7 relaxes a χ(ω); rung8's
quiet verdict rests on S(0); rung5's GR limit takes τ_c → 0. Outcome 7 says that for the TT channel —
**the channel all of these are about** — none of those symbols denote. The node whose statement was
already flagged for not denoting a unique object (E7) turns out to sit inside a formalism **whose whole
ω-space layer does not denote either.** One defect, found twice, at two depths.

**This is worse for the register than a clean refutation.** A refutation settles physics and closes a
question at a price. Ill-posedness closes nothing: the suspended −1 becomes permanently unrecoverable
*in this formulation*, and the *"genuinely open, both leans live"* reasoning that holds rung 3 at Δ0
**collapses**, because neither lean is available for a proposition with no referent. GRUT still uses a
finite memory time — that is the founding premise — so under RULE L1 it becomes an unsourced input.

The one thing outcome 7 does deliver is a sharp, publishable structural fact about de Sitter graviton
response, and a precise construction order for whatever comes next:
`background_time_translation_flow` already names the rescue as its **second** overturning route — *"a
formulation is exhibited in which every banked kernel result is stated without a single-frequency
kernel (no K_R(omega,k) anywhere)."* Under outcome 7 that reformulation stops being an alternative and
becomes the only surviving road — with the honest label that **a reformulated program is a new ledger,
not a continuation of this one.**

**Register moves.**

| node | tier / Δ now | proposed | why |
|---|---|---|---|
| `rung3_single_pole` | derived-pending / **0** | → `assumed`; **`moot`** in `sub_status`, scoped to the gravitational TT channel. Δ under **RULE L1: owner adjudication** | `moot` is the register's own vocabulary and is the correct marker, **not `refuted`**, because the statement is not false. `derived-pending` means derived modulo a named open input; outcome 7 shows the named input **cannot be supplied**, because the object it would be about does not exist. The Δ0 rests explicitly on *"it is genuinely open (both Class A/survives and Class B/dissolves leans are live)"* — **void removes both leans.** The note's own 2026-06-26 history records this hinge running the other way, so the move is **contemplated by the node**, not imposed on it. |
| `background_time_translation_flow` | assumed / **1** | **Δ UNCHANGED** (charging again would double-count the same input); `sub_status` gains a settled-negative marker **on its FIRST discharge route** | Outcome 7a is precisely the failure of that retirement for the assembled object. **Its SECOND overturning route — a formulation with no K_R(ω,k) anywhere — is promoted from alternative to mandatory deliverable.** This is the node outcome 7 hits hardest and most directly: the +1 that was retirable becomes **permanent**. |
| `p_tt_ansatz` | assumed / **1** | **Δ UNCHANGED**; THE ONE ESCAPE marked **closed** | The escape runs through a bath commitment making ⟨T^μ_μ T^ν_ν⟩_R vanish non-perturbatively **at rung3**. Outcome 7 **voids that route rather than answering it** — Π₀ neither shown zero nor nonzero; the object in which it would be defined has no spectral reduction. **No favourable move is available in either direction.** Placement caveat: a marker referencing rung3's disposition belongs in `tier_note` (CHARTER §7 corollary); only p_tt's own terminal-CHOSEN disposition belongs in `sub_status`. |
| `mu_linear` | derived-pending, `no_go_export` / **0** | candidate → `assumed`, Δ **0**, **with an explicit flag that the armed trigger DOES NOT COVER THIS CASE** | The trigger fires on *"Pi_0 != 0 established"*, which outcome 7 does not establish. What it does is close the trigger's **other half** — *"graduation now runs ONLY through the rung3 dynamical route (Pi_0 = 0 forced…)"* — by voiding that route, making the graduation predicate unsatisfiable. **Same destination, different mechanism.** The trigger's wording (*"a future wave executes this, it does not re-litigate it"*) therefore does **not** authorize automatic execution here: **owner adjudication.** Δ stays 0 — as `assumed` it still adds no input directly, its input being p_tt's already-booked +1. |
| `rung5_gr_limit` | assumed / **2** | **Δ UNCHANGED**; **statement repair ORDERED** | *"tau_c->0"* — under outcome 7 there is no τ_c in the TT channel to take to zero: **the limit variable of the GR limit is undefined in the channel where gravity lives.** Identical defect class to E7, cheap to repair, owed before the node is cited again. No ledger movement: GR is already `assumed` at +2 and BORROWED. |
| `rung4_love_kk` | shown / **0** | **UNCHANGED**; scope marker in **`tier_note`**, not `sub_status` | Kramers–Kronig **as mathematics** is a theorem about causal response functions of one frequency and is untouched; the node's own overturning computation is not met. What narrows is **applicability**: whether the assembled TT response *is* such a function. The magnitude story is unaffected — **no reduction failure buys 21 orders of magnitude** — so entry 5 stands as written. |
| `kk_static_transfer` | derived-pending / **0** | **UNCHANGED**; one named sufficient route struck, **the pending input SURVIVES** | χ_∞ is a **local contact datum** — the δ(t−t′) piece — definable in a two-time formalism **without any spectral representation**. Recorded deliberately as a **NON-hit: the discipline is not to maximize the blast radius.** |
| `rung8_falsifier` | to-derive / **2** | **UNCHANGED, PENDING A CHANNEL AUDIT** | S(0) is a one-frequency object and looks contaminated — but the coupling is T⁰⁰ (spin-0 sector) probed along a **detector worldline**, and D3a licenses worldline-scoped stationarity for invariant fields (verified to 12 decimals). If its noise kernel is P^(0,s) and worldline-scoped it is **untouched**; if TT, it inherits the type error. `channel_policy` is the instrument that decides, and **until it is run the answer is genuinely unknown rather than adverse.** |
| `u2_kernel_universality` | to-derive / **0** | **UNCHANGED, SCOPE NARROWED** | Outcome 7 does not refute universality; it removes the object **on backgrounds without a reduction**. The question stays perfectly good in flat space and on backgrounds with a timelike Killing vector — i.e. everywhere **except where GRUT's cosmological exports actually live.** That is the sting. Its `sub_status` already treats under-determination as first-class, so no manufacturing is required. |
| `u5_constitutive_phases` | to-derive / **0** | **UNCHANGED**; general classification untouched, **GRUT-vacuum placement moves from rung3-gated to unaskable-as-posed** | Its `sub_status` already separates the two. **This is the one node where outcome 7 is close to neutral, and where the constructive successor question lives**: classify constitutive response for genuinely non-stationary backgrounds — a real GRUT-II classification problem with explicit failure states, not a rescue. |
| `rung7_wz` | to-derive / **3** | **UNCHANGED**, and recorded as **NOT a favourable move** | Outcome 7 removes the forbidding — and sources nothing. τ₂ remains **inserted**; the sourced prediction is w = −1 flat; double-count check (4) fences inheritance out. **Removing an obstruction to an inserted mode is not a derivation. Naming this as empty relief is the point of listing it.** |
| `NO_GO_LEDGER.md` | — | **candidate** entry at **SETTLED-NEGATIVE**, explicitly not FORBIDDEN, and **not on arrival** (§1.4) | *"The one-frequency formulation of the vacuum's gravitational response."* Ruled out at this strength: that K_R^TT(ω) — and therefore ρ_TT(ω→0) and η — is a well-defined object for the assembled dS response at the declared order. Obstruction: no time-difference reduction in any clock **plus** no residual dS-invariant spectral decomposition. **Named rescue** (what keeps it out of FORBIDDEN): the two-time restatement `background_time_translation_flow` already names. Scope: a statement about GRUT-as-written, not about nature. **If the realization is 7b or 7c the entry attaches to the ASSEMBLY or the SCHEME rather than to the physics** — a narrower and more honest grade, recorded as such rather than rounded up. |

**What it does NOT buy.**

- **It does not buy innocence.** *"The question was ill-posed"* is not *"GRUT was never wrong"* — **it
  is worse than a refutation for a program that shipped ω-space numbers.** Rung 3 asserted *the*
  memory time; a proposition whose predicate has no referent is not a proposition that survived
  scrutiny. **The suspended −1 is not recovered; it becomes permanently unrecoverable in this
  formulation.**
- **It does not buy a FORBIDDEN entry.** Scoped to one channel, one background, one state, one
  declared order — whose caveat is on the manifest's own face — and one newly-constructed assembly
  whose own status is unreviewed.
- **It does not void the walls; it PRESUPPOSES their discharge.** A result reaching this class without
  a graviton-probe assembly is not about the registered object at all and cannot be banked; a result
  reaching it **with** one inherits that construction's unreviewed status.
- **It does not excuse the owed repairs.** E7, the one-clock recomputation, and the channel audit are
  owed **more** under outcome 7, not less — *"ill-posed"* is rhetorical noise unless the object it
  fails to denote has first been named precisely.
- **It rescues no downstream node.** rung7's τ₂ still inserted; p_tt's +1 still stays; the μ=4/3
  endpoint exclusion untouched; GW dissipation still 21–62 orders below the live window; rung8 still
  quiet-or-faint; GR still borrowed; the Born rule still borrowed.
- **It does not touch causality, retarded support, the existence of dissipation, or the arrow's
  direction.** Causal structure supplies retarded support independently, and direction is imported
  from `past_hypothesis` either way. **Which is also to say: it produces no positive result anywhere.**
- **It does not establish that the assembled object has NO structure** — only that the structure is
  not a spectrum. Late-time two-time structure may be rich and is explicitly the cross-contract
  fallback; outcome 7 asserts the *stronger* claim that even that classification fails, which is a
  separate burden (see kill condition 4).
- **It does not deliver the replacement formalism.** It creates the obligation to build one, on a
  signed date; an unbuilt two-time restatement carries no export.
- **It does not settle nature**, and it answers **no** empirical channel of the termination
  pre-registration, so it buys no extension of that date (§3).

**Still owed.**

1. **THE UNIVERSALLY-QUANTIFIED NEGATIVE.** Outcome 7 requires *"no reduction in ANY clock"* — a
   negative over all clocks, not one exhibited failure. **One failure is outcome 5.** Without the
   universal step the report is misfiled, and misfiling it upward is the exact over-grade the charter
   names.
2. **THE STATIC-PATCH KILL, specifically.** De Sitter **has** a timelike Killing vector; thermal field
   theory in the static patch with the booked state is a well-posed stationary problem where ω exists
   **by symmetry, not by assumption** (D3b: *"only the static patch offers a global reduction"*).
   Outcome 7 must show **why the assembled object escapes it**, with the mechanism named: source- and
   observer-vertex corrections not confined to one Killing orbit, superhorizon IR resummation crossing
   the horizon, or horizon-boundary-sensitive IR structure at O(G²). **Absent a named mechanism this
   branch is an assertion.**
3. **THE dS KÄLLÉN–LEHMANN CHECK.** A dS-invariant Σ depends on the single invariant z, and dS field
   theory has an established spectral decomposition over principal/complementary series — a
   one-variable representation with discrete-vs-continuous structure that answers pole-vs-cut **in a
   different basis**. Outcome 7 must show the assembled object admits **neither** a time-difference
   reduction **nor** this decomposition, i.e. that the assembly breaks dS invariance without leaving
   residual stationarity. **The heaviest single burden on this branch, and not optional.**
4. **DUAL-GAUGE (D4-Q5) AND DUAL-SCHEME (D5-Q5) RESULTS REPORTED SEPARATELY, never merged.** 7a, 7b
   and 7c carry different grades and attach to different objects. **Collapsing them into one
   "ill-posed" headline over-grades two of the three.**
5. **The §0.3 six-vs-seven discrepancy resolved by the owner before banking** — acute for this branch,
   which is the one whose token number the machine-readable face does not carry.
6. **The E7 repair at rung3, plus the same repair at `rung5_gr_limit`** ("tau_c->0"). Both are
   statement-level defects of one class, and outcome 7 makes them prerequisites for stating the result
   precisely.
7. **The channel audit** (P^(2) vs P^(0,s) vs worldline-scoped) across every banked export written as
   K_R(ω,k). Without it the blast radius is guesswork **in both directions**; `rung8_falsifier` in
   particular is currently unresolved rather than adverse.
8. **The two-time restatement**, or an honest scope-conditional marking of every banked one-frequency
   result — `background_time_translation_flow`'s own second overturning route, no longer optional.
9. **Owner adjudications, three, each flagged rather than executed**: rung3's Δ under RULE L1; whether
   `mu_linear`'s armed trigger covers a void-by-ill-posedness (**as written, it does not**); and
   whether the `background_time_translation_flow` discharge-route closure is a `sub_status` move on
   that node's own disposition.
10. **Publication and attribution.** *"Every outcome is publishable stand-alone de Sitter physics
    regardless of consequence for this program."* Outcome 7 is a genuine structural result about
    assembled dS graviton response and is owed to that audience, with the first-result treatment
    honored.

**How it could mislead.**

1. **The frame-of-innocence read**, first and worst: *"the question was malformed, so the program was
   never refuted."* **An ill-posed keystone is a heavier indictment than a refuted one** — it means
   the formalism shipped quantitative exports in symbols that do not denote, and it settles nothing a
   refutation would have settled.
2. **Over-grading.** *"A structural no-go result about the question itself"* — the spec's own phrase
   for this class — **reads like FORBIDDEN**, and would be this rebuild's first.
3. **Scope inflation into a claim about nature.** *"de Sitter has no spectral reduction"* is not what
   this says; it says one assembled object at one order in one newly-built assembly does not reduce.
4. **Total blast radius.** Causality, retarded support, the existence of dissipation, KK-as-mathematics,
   the magnitude suppressions, the μ=4/3 exclusion, and probably rung8's worldline-scoped channel all
   survive intact. **A branch author who sweeps everything in is manufacturing drama** — and this
   document's own DOES-NOT-BUY list is the instrument against that.
5. **The mirror error**: reading rung7's relief (single-pole no longer forbids the second scale) as a
   gain. It sources nothing.
6. **The most dangerous, and the one this branch most invites: the infinitely deferrable frontier.**
   *"The real object is two-time; we are rebuilding the formalism"* can absorb unbounded work while
   producing no falsifiable number and never triggering a stop. That is exactly the shape the
   outcomes-first termination instrument exists against. **The honest response to outcome 7 is a signed
   date on the reformulation, not an open-ended reformulation.** And any narrative claiming GRUT *"was
   always a two-time theory"* is contradicted by the register's own evidence: *"'stationar' occurs
   ZERO times in S_IF.md"*, which is **precisely why the flow was booked as an OMISSION.**
7. **7b or 7c reported as 7a.** A gauge- or scheme-dependent classification is a finding about the
   assembly or the prescription. Reporting it as a structural fact about de Sitter physics is the
   single most likely mis-grade **inside** this class, and the reason the three realizations are
   separated on this document's face.

**Kill conditions.**

1. **A static-patch assembled computation returning a gauge-invariant, scheme-independent ρ_TT(ω)** —
   kills outcome 7 outright and hands the question to branches 1–4.
2. **A demonstration that the assembly's source-vertex, observer-vertex and external-mode-function
   corrections can be arranged on a single Killing orbit** without loss of gauge invariance — kills
   7a's principal mechanism, leaving only 7b/7c.
3. **A de Sitter Källén–Lehmann decomposition of the assembled Σ** over principal/complementary series
   — replaces the clock with the dS Casimir/dimension variable and makes the registered question
   well-posed in a different basis. **The most likely way this branch dies.**
4. **Exhibition of a clock-independent invariant τ_phys = F[R_C] built from the two-time object** (for
   instance a decay rate parametrized by the geodesic interval) satisfying ∂τ_phys/∂k_min = 0 with no
   window parameter. **"No ω" is not "no memory time"**, and the cross-contract note *mandates* that
   two-time fallback rather than treating its failure as automatic. This would convert outcome 7 into
   outcome 1 or 3 stated in another language.
5. **Dual-gauge AND dual-scheme tests both AGREEING on classification** — kills 7b and 7c, leaving 7a
   with its full double burden (items 2 and 3 of "still owed").
6. **Any demonstration that the free-level TT non-stationarity is removed by the assembled
   gauge-invariant observable** — the Higuchi/Marolf–Morrison horn, which has real advocates and would
   show free-level evidence does not transfer.
7. **A showing that the assembled object at the next order in G restores a reduction** — confining
   outcome 7 to O(G²) and to the manifest's own unestablished first-nonzero-order caveat, downgrading
   a structural result to an order-artifact.
8. **Discovery that the reported ill-posedness traces to the newly-constructed assembly rather than to
   the physics** — the finding is then about the construction (wall A's discharge failing its own
   review), and **nothing about rung 3 may be banked from it at all.**
9. **Only ONE clock was actually tested.** The claim is universally quantified; a single exhibited
   failure is outcome 5 wearing outcome 7's name, and the report must be re-filed rather than softened.
10. **The two-time object DOES admit a classifiable late-time structure** (a decay envelope, a growth
    exponent, a saturating tail) even without a spectrum. Then the cross-contract fallback applies and
    the question was answerable after all — outcome 5 or a two-time analogue of 1–4, not this.
11. **The reduction failure is traced to a declared regulator or to the epoch window** rather than to
    the assembled physics — then it is a priced input reproducing the class-A defect one level up, not
    a structural no-go.
12. **The preserved physics-dependent gates cannot even be evaluated** because the object is ill-posed,
    AND no alternative formulation of those gates is offered. Then the result fails its own
    acceptance conditions: an object that cannot be checked against the H→0 limit, KMS, or the
    weak-coupling Σ limit has not been shown to be the physical one, and "ill-posed" is indistinguish-
    able from "unverified."

**Honest prior.** Roughly **15%** for this class as a whole; **under 5% for the clean structural
version (7a)**. This is not the likely branch, and **the largest share of that 15% sits in 7b/7c** — a
gauge- or scheme-dependent classification — rather than in a theorem.

*What raises it:* D1's consequence is already in the record before any result, naming this and outcome
5 structurally likely; and D3b is **derived, not conjectured** — the full Σ(x;x′) does not reduce to a
time difference in any single global clock except the static patch. The TT results file exhibits >130%
shape drift with stationarity only for W < 0.25 e-folds, **and that is the right channel**. Wall B
leaves the RG half undischarged while the dS graviton self-energy is known gauge-dependent in the
relevant sector, with TTW §4.3 conceding the gauge effect on the logarithms is unknown — **which makes
a dual-gauge classification disagreement (7b) genuinely plausible rather than exotic.**

*What lowers it, hard.* First, **the static patch is a real escape**: dS has a timelike Killing vector,
and a static-patch computation in the booked state is stationary by symmetry. Second, and heavier: a
dS-invariant Σ depends on the single invariant z, and **dS Källén–Lehmann over principal/complementary
series is established technology** — a one-variable representation in which pole-vs-cut becomes
discrete-vs-continuous series content. **Outcome 7 must defeat both, a double negative burden almost
nobody proves.** Third, the scalar proxy cuts against it: the executed worldline reduction produced a
perfectly well-defined spectrum — a white floor is ρ(ω) = const, which is **well-posed** and
zero-memory. **The one channel where a reduction was actually verified (to 12 decimals) delivered
one**, so this branch needs the gravitational channel to differ **categorically**, not quantitatively,
from the proxy. Fourth, the Higuchi/Marolf–Morrison horn is a live scenario in which **assembly
RESTORES what the free calculation lacked.**

*One structural note that cuts both ways.* Outcome 7 is **not** the "nothing happens" branch. Its
mechanism — IR-induced breaking of dS invariance — is the **same antecedent** as the Tsamis–Woodard
screening horn, which per rung3's `boundary_condition` is the horn that yields a **pole**. Conditional
on IR screening being real, probability moves between outcome 1 and outcome 7 depending on whether the
breaking resums to a dynamical mass or leaves an irreducibly two-time object. **So this prior is not
independent of the pole branch's; it is carved from the same conditional.**

*A reporting asymmetry that should be priced into how any eventual result is read.* Even in worlds
where 7 is TRUE, the **reported** outcome is more likely to be 5 or "scheme-dependent, needs more
work", because exhibiting one nonstationarity is cheap and proving a universal negative over clocks is
not. **Outcome 7 is the class most likely to be true and reported as something else — and,
symmetrically, the class most likely to be reached for rhetorically when the honest label is 5.**

---

## Section 3 — The asymmetry disclosure

*A sealed map that hides its own bias audit is worth less than one that prints it. The seven branches
were drafted independently, then audited for advocacy shape. This section states what the audit found,
which branches were treated more generously, and what was changed. It is printed on the document face,
not in a companion file.*

### 3.1 The headline: the set was not advocacy-shaped, and on two metrics it ran the other way

Depth tracked **adversity**, not favourability — the opposite of what advocacy produces:

| branch | outcome | register-move bullets | distinct nodes named | kill conditions (draft) | still-owed (draft) |
|---|---|---|---|---|---|
| 1 | isolated pole | 15 | **16** | **13** | **15** |
| 2 | multiple poles | **19** | 16 | 12 | 10 |
| 3 | branch cut | 15 | 14 | 11 | 10 |
| 4 | continuum | 16 | **22** | 12 | 12 |
| 5 | secular | 15 | 13 | 10 | 11 |
| 6 | no structure | 13 | 15 | 11 | 11 |
| 7 | ill-posed | **12** | **11** | **8** | 10 |

The three **thinnest** branches on kill conditions were 7, 5 and 6 — **the three most program-adverse**
— while the two most favourable, 1 and 2, carried the most. Branch 1, the outcome CHARTER §1.4 says
the loop over-claims on hardest, was the longest, had the most kill conditions and the most owed items,
and contained the set's harshest self-indictment (the premise-independence hole in the wall contracts,
§2 outcome 1). Two of the three adverse branches named the **mirror** failure mode unprompted.

**The seven independent unconditional priors summed to ≈ 98–100%.** Seven advocating authors do not
produce a near-normalised distribution. Where the set erred, it mostly **under**-claimed.

**What was done:** branch 7's kill conditions were thickened from 8 to 12 and its DOES-NOT-BUY list
extended; branch 5's DOES-NOT-BUY was extended and the **mirror failure mode added**, which it alone
had omitted; branch 6's mirror note was retained. No favourable branch was thickened further, and none
was cut for being long — the fences in branches 1 and 2 are load-bearing.

### 3.2 The one clean directional asymmetry, and the rule that removes it

**The only ledger CREDIT available anywhere in seven consequence maps was taken by the favourable
branches and refused by every adverse one.**

`background_time_translation_flow`'s discharge route, verbatim: *"OVERTURNED / DISCHARGED IF: the
declared background is one carrying a timelike Killing vector -- the de Sitter static patch is the
named candidate."* But `CLASS_C_MANIFEST.json` declares `"patch": "flat FLRW"`, **which has no global
timelike Killing vector.**

- **Branches 1, 2 and 4 — the three most favourable — all booked the −1**, on conditions that did not
  include the patch (the clock used; window-free stationarity alone; a reduction proof). Branch 2
  called it *"THE ONLY CLEAN RECOVERY."*
- **Branch 3 alone caught the blocker** and booked the −1 as *available-but-blocked, not as earned.*
  Branch 3 was correct.
- **Branches 5, 6 and 7 — all adverse — declined the −1** on independent reasoning.

**What was done: RULE L2 (§2 preamble) now binds all seven identically.** No branch books it; the −1 is
available-but-blocked under every outcome; a patch re-declaration is a new versioned dispatch. **This
is the single item in the set that should be treated as advocacy pending owner adjudication, and it is
disclosed here rather than smoothed away.**

### 3.3 Three factual defects found in the drafts, and their repairs

**(i) A fabricated quotation — the more serious defect of the three.** Branch 2 wrote: *"The node's own
ledger_note prices this direction: 'a clean failure costs +1'."* **The strings `clean failure` and
`costs +1` appear nowhere in the repository** (grep-verified, whole tree, at HEAD `d006d01`). rung3's
actual `ledger_note` reads: *"The -1 'derived' credit stays SUSPENDED… but is NOT a +1 cost either: it
is genuinely open."* **A branch author manufactured register authority to license a ledger move.** The
move it licensed was a *cost*, so this was not directional advocacy — but it is the defect that most
needed removing.
**What was done:** the quotation is deleted; the real text is quoted; and **RULE L1** now states, once
and for all seven, that the register prices *neither* direction in advance and that both are owner
adjudications.

**(ii) A stale net, always in GRUT's favour.** Three branches hand-typed a net one unit below the
emitted figure — plausibly by reading `background_time_translation_flow`'s own `ledger_note` transition
as the current state. Every hand-typed net in the set understated, i.e. always favourably.
**What was done:** **no net figure is typed anywhere in this document.** Nets ride `validate.py` /
`emit_public_numbers.py` on their own faces, which is the `PUBLIC_NUMBERS.md` rule and is exactly the
rule these drafts broke. Per-node deltas are quoted from the register.

**(iii) A numbering slip, on the two favourable branches.** Branches 3–6 correctly translated D1's
recorded consequence — *"outcome classes 4 … and 6 …"* — into this map's seven-token numbering.
**Branches 1 and 2 quoted it untranslated**, where in the seven-token numbering it reads as *continuum*
and *no-long-memory* — pointing the register's own pre-written expectation **away from** the branches it
actually names. The surrounding argument survived either reading in both branches, so this is sloppiness
rather than manipulation, but it was the two favourable branches that left the ambiguity.
**What was done:** **§0.4 makes the translation once, on the document face.**

### 3.4 Two consequences no branch raised, or raised only once where they applied four times

**(a) Four of the seven outcomes contradict a clause inside a `shown`-tier, Δ4 node — and only one
branch routed it.** `rung1_inin_action`'s statement opens: *"The gravitational vacuum is a responsive
medium with **finite memory**…"* Outcomes 3 (unbounded power-law memory), 4 (Ohmic sub-case → τ_c = 0),
5 (epoch-indexed unbounded memory) and 6 (zero memory) each contradict it. **Branches 3, 4 and 5 all
noticed the premise failure and then routed it nowhere**, listing rung1 as untouched-by-class-C. Only
branch 6 ran CHARTER §4's tell and reached a repair. **Net effect: the single largest available ledger
consequence appeared in one of the four branches where it applies.**
**What was done:** the CHARTER §4 compound/omission test is now flagged as **owed and blocking** in
outcomes 3, 4, 5 and 6 alike — and **the test is flagged, not executed**, because the register's own
history is that two of five pre-registered candidates were mislocated and *"applying the wrong repair…
manufactures a false dependency graph."* The two tallies are never summed.

**(b) The in-force termination instrument's dispatch channel resolves on TWO of seven outcomes — and no
branch named it.** `provenance/prereg/PREREG_TERMINATION_V4_2026-08-10.txt`, C1, verbatim:

> "C1 THE DISPATCH (pole-vs-cut; DISPATCH_ONE_PAGE.md; node rung3_single_pole)… RESOLVED: (a) a reply
> asserts the POLE class in its own words, unconditionally; (b) a reply asserts the CUT class likewise
> (fires stop (iii))… Acknowledgments, caveats, conditions, conflicting replies, silence: STILL OPEN,
> words quoted."

**Five of the seven frozen outcomes — multiple poles, continuum, secular, no-long-memory-structure,
ill-posed — resolve C1 not at all.** The most program-adverse outcome in the set (6, retire rung 3)
**cannot fire the stop**, while the favourable one (1) can resolve the channel. That is an asymmetry
sitting inside a sealed instrument, and the consequence maps were the right place to catch it.

**AND A CORRECTION TO THE AUDIT ITSELF, made here because getting this wrong in either direction
matters.** The audit reported *"STATUS: UNSIGNED = NOT IN FORCE"* from the sealed file's on-face line.
**That line is superseded.** `provenance/prereg/RESULT_TERMINATION_events.txt`, 2026-08-10: *"SIGNED:
Ryan Graver DATE: 2026-08-10… the sealed file's on-face STATUS line ('UNSIGNED = NOT IN FORCE') is
superseded by this entry under that same rule. *** THE TERMINATION CONDITION v4 IS NOW IN FORCE from
this date. ***"* (Signatory name clerically corrected 2026-08-12 to D. Ryan Grover; the correction
touches no channel line.) **So C1 is live, and the asymmetry is binding rather than hypothetical.**

Three further facts belong with it, none of them resolved here:
- C1 names `DISPATCH_ONE_PAGE.md`, while `CLASS_C_DISPATCH_SPEC.md` §5 states *"This spec IS the
  re-pose of DISPATCH_ONE_PAGE.md."* **Whether a class-C reply is a C1 reply at all is an owner
  adjudication**, and it should be made before a result exists rather than after.
- R5's stop fires at the earliest of **2026-12-31**, both Part-7 fronts discharged, or a logged
  unconditional cut-class reply. Two of §5's in-house discriminators are Part-7 fronts, so **running
  them has a consequence beyond this map.**
- R1/R2 bind regardless: *"Still-open is never rounded into a resolved outcome"*, and *"a resolved
  outcome's consequences execute ONLY at the named register node."* **This document executes nothing.**

**(c) The dispatch has no recipient, and the register says so.** Recorded at §1.5 rather than left
inside one branch's prior: *"NO OUTSIDE HUMAN HAS EVER BEEN CONTACTED BY THIS PROGRAM: no transmission
is logged at any date."* Four branches listed external reproduction as owed; none noted that the
conditioning event has no base rate in-register.

### 3.5 Ranked by risk of over-encouraging a reader who wants GRUT to be right

1. **Outcome 1 (isolated pole) — highest.** It is the only branch that pre-authorises a **tier
   graduation and a ledger credit**. Sealing a graduation in advance is structurally the strongest
   advocacy artifact in the set regardless of how many fences surround it — and the fences are real and
   heavy. A motivated reader extracts "rung3 derived, −1" and drops the scope string. **Mitigation, not
   removal:** the restatement requirement is now stated as *mandatory and not cosmetic*, the
   alternative (stay derived-pending, rename the input) is given equal standing, and RULE L1 makes the
   credit conditional on a genuine derivation rather than on a route change.
2. **Outcome 2.** Contains the single most encouraging sentence in the set — *"GRUT's finite-memory
   axiom survives"* — inside a branch that **refutes** rung 3. Retained because it is true and
   load-bearing; immediately followed by *"Corroborating your own axiom is not earning it."*
3. **Outcome 3.** Carries a **50–60%** conditional number that will be quoted without its conditioning,
   and the line *"a cut is MORE memory, not less"*, which reads as survival. Both retained with their
   fences; the conditional/unconditional split is stated twice.
4. **Outcome 5.** "Bracketed, not refuted" plus a constructive replacement programme. **The mirror
   failure mode was missing and has been added.**
5. **Outcome 7.** Its genuine danger is the **deferrable frontier**, which it names itself.
6. **Outcome 4.** Net ledger goes *worse*; closes two of rung4's four observability sub-loopholes;
   refuses the tempting rung8 win on channel-policy grounds.
7. **Outcome 6 — lowest.** Proposes the largest cost, contradicts a `shown`-tier node, and names its
   own mirror failure.

### 3.6 One near-miss recorded in the set's favour

Outcome 1's sole FOR argument is grep-verified accurate: `calc/mz_inheritance.py:258` carries the exact
sum rule `sum_{l>=0} (2l+1) A_l(x,x;w) = -w sinh^2(x)` with its own comment *"verified below to 26+
digits"* and *"the l-summed local spectral density is exactly OHMIC and has NO Matsubara-rung zeros at
all."* Branch 1 cited it correctly, noted rung3's own decision rule, **and then weighted it down
itself.** Correct handling of the strongest in-tree pointer it had.

### 3.7 Three items requiring owner attention BEFORE this map seals

1. **The `background_time_translation_flow` −1** (§3.2). Adjudicate the node, or the seal preserves a
   directional error. RULE L2 is this document's interim answer, not the owner's.
2. **`rung1_inin_action`'s finite-memory clause** (§3.4a). Run CHARTER §4's compound/omission test
   **now**, not when a result arrives.
3. **PREREG_TERMINATION_V4 C1** (§3.4b). It resolves on two of seven outcomes, the most adverse outcome
   cannot fire the stop, and it names a document the class-C spec supersedes. **In force since
   2026-08-10.**

---

## Section 4 — What this map does NOT do

- **It does not make any outcome more likely.** Writing a favourable branch out in detail is not
  evidence for it. Detail is a function of how much register surface an outcome touches, not of how
  probable it is — and §3.1 shows depth in this set tracked adversity, not favourability.
- **It does not substitute for the dispatch.** Every branch conditions on a computation that does not
  exist, performed on an object (wall A) that does not exist, by a recipient who has never been
  contacted (§1.5). CHARTER §3 is unchanged: *"It is NOT an in-house calculation… Banking a resolution
  of this in-house is an automatic fail."*
- **It does not resolve walls A, B or C.** Every branch either presupposes their discharge or is void.
  Nothing written here advances any of them by a single step.
- **It does not resolve the two package discrepancies** of §0.3, the three owner adjudications of §3.7,
  or any `UNDECIDED-DISPATCH` field. `gauge` and `renormalization` remain undecided; the solver
  continues to refuse.
- **It banks nothing and moves nothing.** No tier, no `ledger_delta`, no `sub_status` marker, no
  `NO_GO_LEDGER` entry. `provenance/claims.json` is untouched by this file. Every move above is a
  candidate for the bank gate.
- **It may not be cited as content**, by this program or by any artifact in it, until the specific
  claim cited has been screened and banked on its own.
- **It is not a forecast, and its priors are not results.** They are calibrated judgments, subjective
  and non-consumable, and the program's own every-load-bearing-number-has-a-calc rule bars quoting
  them downstream as figures. *"Class C will show X"* is on the red list for any X. **If this document
  is ever cited as having predicted an outcome, the instrument has been inverted.**
- **It does not narrow the register's own commitment that no outcome is preferred.** All seven remain
  first-class; the freeze certificate governs; the first result is a discovery result about de Sitter
  and carries no favour.
- **It confers no strength.** Nothing here is banked at FORBIDDEN, and nothing here is banked at
  SETTLED-NEGATIVE either: §1.4 defers every candidate ledger entry until after independent
  implementation or external reproduction.

---

## Section 5 — The in-house discriminators

*What makes this map operational rather than contemplative: the already-runnable in-house work that
would shift weight between branches **before any class-C answer exists**. None of these answers class
C. Each is listed with what it would move and in which direction.*

**A caution that binds this whole section:** two of these are **Part-7 fronts** of the in-force
termination condition, whose R5(ii) stop fires when both are *"discharged (calc completed, or retired
with a statement naming what dies and why)."* **Running them therefore has a consequence beyond this
map**, and that consequence is a stop-clock consequence, not a physics one.

### D-1. `calc/gw_tensor_friction.py` — owed since 2026-08-02; SPEC written, code not

`calc/SPEC_gw_tensor_friction.md` exists with pass/fail pre-registered; the code does not. It is *"the
only queued item that produces a NUMBER rather than a map."* Its **Q-A** is the discriminator: *"Does
the tau_2 pole appear in the **P^TT** channel at all, or only in the scalar **P^(0s)** channel that
`p_tt_ansatz` excludes?"*

**What it would move.** A scalar-only answer says the register's own two-scale kernel has **no TT
content at the IR scale** — which sharpens what outcomes 1 and 2 could ever be quoted for
cosmologically (RULE L3 already bars the export; this would show there is nothing on the other side to
export), and makes outcome 6's TT null less surprising rather than more. A TT answer does the reverse
and makes the rung7/rung3 coupling live in the channel class C computes. **Either way it converts an
un-backed order-of-magnitude inference ("few × H₀") into a computed number** — which is also what
outcome 6 would independently deliver, and the two should not be allowed to confirm each other.
**Front C5 of the termination condition.**

### D-2. The one-clock recomputation — keystone map §9.1 (rows C1/C2)

*"Recompute rung3's tower-separation requirement and rung7's τ₂ requirement in one named coordinate;
file whichever way it lands."*

**What it would move.** This is the largest pre-result weight shift available. Outcome 3's own
still-owed list surfaced an unresolved tension in `RUNG3_KEYSTONE_MAP.md` §1.2: **D1 derives T = t
exactly on the axis, while D4 computes the global conversion using HT = e^{Ht}** — under which
e^{−Γt} is a **power law** in the other clock. If D4's relation is operative beyond O(1/H), then
**pole-vs-cut is itself clock-dependent at late times**, and every spectral branch (1–4) requires
certification in a named clock before it means anything. That moves weight toward outcome 7 and away
from 1–4 **before any class-C result exists**, and it is the one in-house item that could do so.

### D-3. The E7 repair — keystone map §9.2 — blocking on all seven

*"Name which MZ object the node means, before any ladder-based argument is filed against it again."*
`calc/mz_inheritance.py` already establishes the three candidates answer oppositely: the symmetrised
route inherits the ladder; Kubo–Mori has none (coth → 2/βω, one pole at ω = 0); the GLE friction kernel
is temperature-independent outright.

**What it would move.** It does not change any outcome's probability — **it changes what each outcome
would be scored against**, which is prior to probability. A ladder result read against the symmetrised
kernel and the same result read against Kubo–Mori are different findings. **Every branch above lists
this as owed, and four list it as blocking.** It is pure in-house work, no new physics, and it is
undone.

### D-4. The CHARTER §4 test on `rung1_inin_action`'s finite-memory clause

Compound (split) or omission (add)? The tell says the candidate appears in the node's own statement, so
**split** — but the register's own history is that two of five pre-registered candidates were
mislocated, one at medium-high confidence.

**What it would move.** It decides **the largest ledger consequence in this entire map**, and it is a
precondition for outcomes 3, 4, 5 and 6 rather than a consequence of them. Running it now removes a
result-shaped pressure from the adjudication later. In-house, runnable today.

### D-5. The channel audit — P^(2) vs P^(0,s) vs worldline-scoped

Classify **every banked export written as K_R(ω,k)** by channel. `channel_policy` is the instrument;
`rung8_falsifier` is the node whose disposition it decides (its coupling is T⁰⁰ — spin-0 — probed along
a **detector worldline**, where D3a licenses stationarity for invariant fields).

**What it would move.** It fixes the **blast radius in both directions** for outcomes 3, 5, 6 and 7 —
currently guesswork, and guesswork that can inflate an adverse reading as easily as it can protect a
favourable one. Under outcome 7 in particular, rung8 is *genuinely unknown rather than adverse* until
this is run.

### D-6. The dS Källén–Lehmann feasibility check

Does the assembled object — or, as a first step, its free limit in the declared patch — admit a
spectral decomposition over principal/complementary series, in which pole-vs-cut becomes a
discrete-vs-continuous series question?

**What it would move.** This is **outcome 7's own most likely killer**, named in its kill conditions.
Establishing that the decomposition exists for the free object would move weight off 7 pre-emptively
and back onto 1–4; establishing that the assembly's IR structure destroys it would do the reverse. It
is the only item here that bears directly on the *posedness* question rather than on the answer.

### D-7. Already run, and recorded so it is not re-discovered as new evidence

`calc/mz_inheritance.py:258` — the exact l-summed sum rule, 26+ digits, making the free l-summed
**local spectral density exactly Ohmic with no Matsubara-rung zeros**. Against rung3's own decision
rule this reads favourably to outcome 1. **It is weighted lightly and must stay weighted lightly**: it
is a free, l-summed, *local spectral* object, not the interacting retarded dynamics, and the register's
fence is that the free level carries no evidence either way. It is listed here so that a later
re-encounter cannot be reported as a new pointer.

### What none of these do

None answers class C. None discharges walls A, B or C. None licenses a tier move. Each shifts weight
between branches of a map that banks nothing — which is the whole of what "operational" means here.

---

## Seal block

**What this document is.** A consequence map for the seven permitted Class-C outcomes, written and
sealed **before any Class-C result exists**, so that when a result arrives its interpretation was fixed
in advance and cannot be selected after the fact.

**Repository state at authorship.** `/Users/mpg/Desktop/GRUT ResponsiveAI`, HEAD `d006d01`, clean;
opened read-only. **No file in the repository was modified.**

**What is sealed.** This file, in full, including Section 3's disclosure of its own bias audit and
Section 5's discriminator list. The seal covers the text as written; it does not cover, license, or
pre-approve any register edit named inside it.

**Immutability rule, adopted from the dispatch certificate's own terms.** Once hashed, this file is
never edited. Any necessary change is a **new versioned consequence map** that explicitly explains what
this one could not express, and the superseded version remains as unedited history.

**What remains with the owner, listed once so the seal does not swallow it:**

1. The three adjudications of §3.7 — the `background_time_translation_flow` −1; the CHARTER §4 test on
   `rung1_inin_action`'s finite-memory clause; and PREREG_TERMINATION_V4 C1's two-of-seven resolution
   asymmetry (in force since 2026-08-10).
2. The two package discrepancies of §0.3 — six-vs-seven outcome classes across certificate, spec and
   manifest; and the immutable certificate's disagreement with live manifest v1.1 on three declared
   fields.
3. Every RULE L1 adjudication — rung 3's Δ under each outcome. The register prices neither direction in
   advance, and this document proposes rather than executes.
4. Whether to run any of Section 5's discriminators, given that two are Part-7 fronts of an in-force
   stop clock.

**Standing fences, restated at the seal.** Nothing here banks. Nothing here may be cited as content
until independently screened and banked. No outcome is preferred. The first Class-C result is a
discovery result about the assembled gravitational response, is not a GRUT result, and carries no
favour.

**SEALED (hash to be recorded on the companion event line):** `________________________________`
**DATE:** `____________`
