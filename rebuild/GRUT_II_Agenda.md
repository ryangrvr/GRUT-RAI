# GRUT II — the universality agenda

*The forward program after the Version I close. Version I crystallized "how far is the responsiveness bet forced to reach?" (`GRUT_I_What_Survived.md`). Version II's question has been **sharpened and inverted** (referee-adjudicated 2026-07-02): stop asking "does GRUT generalize?" and ask —*

> **Central question:** *Why do **constitutive / response descriptions** (susceptibility, memory, linear response) appear in every successful effective field theory — thermodynamics, hydrodynamics, transport? What is universal about **constitutive structure itself**, before any microscopic ontology?*

*This is the stronger question precisely because it **does not require GRUT to be right**: GRUT becomes a **probe of the universality/microscopic boundary**, not a candidate to validate. That boundary is where the deepest developments in physics have lived — thermodynamics vs statistical mechanics, hydrodynamics vs molecular dynamics, EFT vs UV-completion. V2 is **structural, not empirical** (signature-null persists); modal outcome = structural-clarification + under-determination, not a universality theorem. Six entry claims are posed (`u1_`–`u6_`, ledger 0 each; gate GREEN at net +13, 45 nodes — 34 GRUT claims + 11 borrowed/open-field scaffold; posing open questions adds no underived input).*
<!-- REGISTER-SYNC: 49 nodes, net +13 -->
<!-- REGISTER-TOTAL: 70 = 49 grut + 21 vacuum-cluster; nets +13 grut, +0 cluster -->

> **The GRUT II charter (`u0`, governing rule — also `CHARTER.md` §8):** *The purpose of GRUT II is not to derive a Theory of Everything. It is to determine whether constitutive response possesses mathematical structures universal across microscopic realizations. **Every branch is a constrained classification problem with explicit failure states — never an ontology to defend.*** (The central object it classifies — "constitutive organization" — is defined provisionally in `GLOSSARY.md`.)

---

## The two deep foundational frontiers (both fenced)

The central question and its prerequisite are the two deepest frontiers — **distinct in kind, do not collapse them:**

### U4 — Origin of the constitutive form (`u4_constitutive_origin`, `to-derive`, **FENCED both directions**) — the central question, the deepest
Given coarse-graining, **why** does the effective description take a *response* form rather than an arbitrary functional? Deriving coarse-graining does **not** hand you linear response — that follows only under extra conditions (weak coupling, Gaussianity, near-equilibrium, timescale separation). U4 asks why those conditions hold / why constitutive structure is generic. **Strictly deeper than U1** (which presupposes them). Foundations-of-EFT; the *least* tractable of the frontiers.

### U3 — Origin of coarse-graining (`u3_split_origin`, `to-derive`, **FENCED**) — the setup
Why is there a system/bath split *at all*? U1's Feynman–Vernon universality *presupposes* it. Sits *below* `rung1`.

> **⚠ HARD FENCE (machine-checkable, in each claim's `sub_status`):** do **not** pre-answer — "emergent" for U3, and **"emergent" *or* "forced"** for U4. These are hypotheses to test, never banked conclusions; a screen returning "looks emergent"/"looks forced" does **not** bank it — only an *exhibited derivation* graduates them. The fence lives in `sub_status` (the machine-watched field), so any pass trying to soften it trips the resident's substantive-change firewall flag. **U3 and U4 are distinct** (setup ≠ constitutive form) and must not be collapsed.

## The u4 classification tree (how U4 is worked, under the u0 charter)

U4 is one frontier with **three coupled facets in a fixed order** — assumption-space (III) → theorem (VIII) → interpretation (II); **interpretation cannot precede the theorem.** It is operationalized as a **classification tree**, each branch a classification exercise with first-class success *and* failure conditions:

```
                 u4  (why is effective physics constitutive?)
                 /                                    \
   u5 constitutive PHASES                    u6 constitutive ORDER
   classify universality classes             order parameter w/ RG significance
   of χ(ω,k) — RG flows, stability,           (monotone = corollary, not theorem)
   Hohenberg–Halperin analogue                Landau / c-/a-theorem relation
                 \                                    /
                    → an observable effective field theory
                      (if classes / order structure exist, they carry EFT consequences)
```

- **U5 — constitutive phases** (`u5_constitutive_phases`, `to-derive`, ungated `depends_on []`). Enumerate the admissible χ(ω,k) universality classes (RG flows, stability, observable distinctions; Hohenberg–Halperin dynamic-class analogue). **First-class failure:** if only **one** stable class exists → responsiveness is *unique* (a real result, still publishable). The **GRUT-vacuum placement** within the classes is downstream and gates on `rung3`; do not conflate classification with placement.
  - **Opening survey banked 2026-07-04 (firewalled amber→green) — a two-sector *exclusion*.** The responsive-vacuum constraints exclude (a) the far-from-equilibrium/driven-dissipative Keldysh sector (KMS/detailed-balance; Sieberer–Buchhold–Diehl) and (b) the *literal* (frame-fixed, non-relativistic) Hohenberg–Halperin model equations A–J (Lorentz/diffeo + T_μν-conservation) — **not** their universality classes, whose scaling survives relativistic covariantization. What survives: the **relativistic, passive, KMS viscoelastic-transport** sector (candidate internal classes = rel. analogs of the reversible-mode-coupling subset E/F/G/H/J, Model H the T_μν-analog). **Fenced hard: exclusion only — not uniqueness, not phase structure.** The **count** inside the surviving sector (one class = rigid vs a family = phase structure) is **open and load-bearing on `u6`** (the order parameter that labels the classes). Consistency check: GRUT's own rung1/2/4 sit *inside* the admissible sector. See `provenance/claims.json` → `u5_constitutive_phases.boundary_condition`.
- **U6 — constitutive order** (`u6_constitutive_order`, `to-derive`, `depends_on []`). Does constitutive organization admit an **order parameter** with RG significance? The RG monotone is a *corollary, not the theorem* — aim at the order parameter (relation to entropy / information / anomaly coefficients / response kernels). **First-class failure:** if it reduces entirely to existing RG monotones → info_i2-adjacent (still useful, not new). **Guard:** the monotone is generic; do **not** re-import `info_i2`'s dissolved beyond-standard machinery.
  - **Opening survey banked 2026-07-04 (firewalled amber→green) — an EXISTS-side *candidate*, not a result.** The info_i2 traps (a/c, α, η/ζ, continuous entanglement) were **rejected** as monotone/coupling, and the survey landed on a **discrete candidate: the {reversible mode-coupling / Poisson-bracket structure + conserved-charge-content} pair** (separates HH A–D from E/F/G/H/J; Model H from Model J). **Independent-definition guard PASSED** — the bracket is fixed by the symmetry algebra (a kinematic input computed before the class, genuinely unlike the single-pole's renamed premise) — *conditional on the slow-variable/coarse-graining choice* (the fenced input one layer down, rung3-shaped). **Fenced hard: candidate identified, NOT established** — whether it is a *real* order parameter is the **open sharpness proof** (non-deformability of the covariantized bracket-classes); F3 gets a handle, not a resolution. **u5↔u6 convergence:** that *same* deformability computation settles both — sharp ⇒ real order parameter + u5 phase-structure count; deformable ⇒ collapse + u5 rigid. In-house-attemptable; **the next move is that proof, not a third survey.** See `provenance/claims.json` → `u6_constitutive_order.boundary_condition`.

## The two GRUT-specific instances (of the central question)

### U1 — Form-universality (`u1_form_universality`, `shown`-generic/BORROWED)
*Given* the constitutive conditions, is the *form* universal? **Yes — standard physics, not a GRUT result** (Feynman–Vernon / Caldeira–Leggett / non-eq Keldysh EFT). GRUT adopts a universal IR language; it does not own the universality. A GRUT-specific **instance** of the central question — and it *presupposes* what U4 asks.

### U2 — Kernel-universality (`u2_kernel_universality`, `to-derive`, default-BROKEN)
Is GRUT's *specific* response kernel (L₀, the low-ω pole structure) UV-completion-independent across QG completions (string / asymptotic-safety / causal-set / LQG)? The one place a GRUT-specific universality *result* could live — but **tightly coupled to `rung3`** (the pole structure is itself open), so likely **under-determined out of the gate**. A GRUT-specific **instance**; graduates only if ≥2 completions flow to the same IR-kernel class; refuted if different; under-determined is a first-class outcome, not to be manufactured into universality.

---

## The three-frontier stack (the forward-uncertainty localization)
`why-split` (**F2**, `u3`) → `why-constitutive` (**F3**, `u4`) → `which-kernel` (**F1**, `rung3`). Three distinct layers; the earlier map had two (F2 and F3 were collapsed). F1 (`rung3`, where the V1 spine test and U2 meet) is gated on the dS-IR controversy. **Finding the third frontier is a truer map, not a new move** — F3 is the least tractable, so forward-gating is unchanged. See `STATE.md`, `POSTULATE_MAP.md`.

## The governing analogy — a goal, not a claim
The intended shape is **thermodynamics**: universal because a vast range of microscopic systems flow to the same macroscopic laws.

> **⚠ HARD GUARD — the thermodynamics analogy is the GOAL, not a current claim.** Thermodynamics earned its universality through actual micro→macro derivations (statistical mechanics, the RG). GRUT has **no such micro→response universality derivation yet** — U2/U4 are the demand for one. Asserting "responsiveness is universal like thermodynamics" as established is the precise over-claim the discipline blocks.

## The no-gos as boundaries (standing note)
`NO_GO_LEDGER.md` records what the responsiveness hypothesis *forbids* — the **walls of the universality class** (μ=4/3 excluded; phantom-divide crossing without an inserted mode; the conformalon unification; the α→TT bridge). Knowing what *cannot* emerge constrains what *is* universal.

## Discipline carried forward
- Every V2 result enters the register **default-BROKEN**, `to-derive`, **firewalled** before graduation.
- **No universality claim, no "emergent"/"forced" verdict, no "under-determined" result is banked** until derived/computed. The agenda holds *questions*; the register holds only *answers that survived the gate*.
- The first probe points at **U1 + U2** (form vs kernel); **U3 and U4 stay fenced** until a derivation, not a screen, is in hand.
- The **method itself** still owes its novelty screen's falsifier — independent external validation (`method_novelty`); the "Provenance Problem" paper is the agreed submission vehicle (framed as a synthesis of prior art, not an invention).
