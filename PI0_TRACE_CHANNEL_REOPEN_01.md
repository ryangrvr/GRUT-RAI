# Π₀ TRACE CHANNEL — REOPEN 01: Phase Π0-0 current-scope feasibility / object audit

**STATUS: AUDIT. No new numerical physics was run.** The proposed Π0-0 outcome is for owner review.
- **Authority:** `PI0_CAMPAIGN_OWNER_DIRECTION_01.md` (Issue #2 comment `5899711204`).
- **Sources:** three read-only record audits (object history; machinery inventory; the declared
  branch and threshold history), adjudicated by the operator. File:line citations are to the
  record as audited.
- **Date:** 2026-09-29 · **Branch:** `master-w25bu9`.

> **Scope fence (binding, carried on the face).** The earned Level-0 core does not select
> gravitational coupling, spin, universal reach, causal cone, or physical lift. This campaign asks
> what follows **if the already-declared gravitational branch is adopted**. A positive Π₀ result
> is a conditional prediction of that branch; it does not retroactively derive gravity from
> Level-0. Lift selection stays IRREDUCIBLE/SUPPLIED; GR2 is not upgraded; nothing here is "Level-0
> predicts gravity".

**Observability firewall (item 7, applied throughout).** No Planck, DESI, TT-auto or other
observational number was used to define, normalize, regularize or scope anything below.

## §0 Proposed Π0-0 outcome

> **FRONTIER-BLOCKED** for the declared target Π₀(ω → 0, k → 0).

**Two principal blockers** (either alone is sufficient):
- **B-1 · Gauge-invariant spin-0 assembly is unavailable.**
  - The validated pipeline is gauge-safe **only because** P^TT annihilates gauge modes and the
    trace together (`PHYSICS_LEDGER/WALL_KR_D4…` audit :46: P^TT[i(k_iξ_j + k_jξ_i) + λδ_ij] = 0).
    For a trace channel that mechanism is unavailable by definition.
  - The one scalar-type leg the pipeline has tried (Tier-3 "ward" configuration) gives a
    **nonzero Ward residual at H⁰ in flat space** (Tier-3 verdict :94-99; D4 internal-line
    obstruction (7/2)iω²q(X0 ± X3)(t11 − t22), D4 audit :75).
  - The record contains **no** ghosts, no non-TT internal graviton lines, no gauge-fixed
    (de Donder/background-field) propagator, and no conserved-source on-shell J = 0 cut.
  - The matter-loop analogue's Ward diagnostic is itself **UNRESOLVED** (`wall_a4_ward_diag`,
    verdict C).
- **B-2 · The target limit lies outside every certified domain.**
  - The flat (H⁰) graviton-loop contribution scales as ω⁴·log (Tier-3 anchor −3ω⁴/1280π in the
    TT channel; dimensional analysis gives the same leading power in any channel). **It vanishes at
    ω → 0.**
  - So any non-zero Π₀(ω → 0) must come from the de Sitter IR region ω ≲ H, and the pipeline
    **refuses** that region by design: the Tier-4 evaluator refuses ε_H ≥ 1, i.e. ω ≲ 3.4H; paper
    §7 items 1 and 8 record the ω → 0 transport class as undetermined.
  - The record's own assessment of that region: "gauge-dependent sector, contested secular growth,
    no assembled scalar observable in the literature" (`X_FLOOR_MAP.md:19`).
  - The finite-k_ext loop, needed to separate P⁽⁰ˢ⁾ from P⁽⁰ʷ⁾, has never been computed; all
    loops are at k_ext = 0.

**Auxiliary blockers** (they would still block a *value* even if B-1 and B-2 were solved):
- **A-1** the renormalization scheme is an open owner ruling;
- **A-2** no order of limits is declared for Π₀ itself;
- **A-3** no spin-0 probe coupling is declared (every declared probe object is TT);
- **A-4** the x = f(Π₀/Π₂) map was never written, and x → μ carries α.

See §§2–6.

**Why the other outcomes do not apply, against the frozen definitions:**

| Outcome | Why not |
|---|---|
| **FORMULABLE-IN-HOUSE** | No gauge/scheme-clean calculable target exists with current machinery (B-1, B-2). |
| **FORMULABLE-CONDITIONAL** | It would need declarations **not already present** in the record: a gauge-invariant assembly procedure with ghosts or non-TT lines; a spin-0 probe coupling beyond the TT representation; a Π₀ order of limits; a scheme ruling (pending, not present). It would also need constructions that do not exist (the finite-k_ext loop; the ω ≲ H regime). |
| **LOCAL/SCHEME-ONLY** | Not established. The flat part vanishes at the target limit, and the surviving local slots (c0, c2) were certified zero only for the TT channel in MS at H⁰ (D5). Whether the dS IR contribution is wholly local/scheme-movable is exactly what cannot be assessed (B-2). This is a live risk, not a finding. |
| **UNFORMULABLE** | Not selected. The owner's direction fixes the bath ("pure-dS graviton environment"). The projector convention is fixed (§1). The missing pieces (the assembly procedure, the limits order) are *blocking constructions and declarations*, not an absence of a target. |
| **IDENTITY-ZERO-CANDIDATE** | No identity is identified. The symmetry route to "forced zero" is recorded closed (`p_tt_ansatz.boundary_condition`; linearized Weyl invariance unavailable, `S_IF.md:36`). A Ward/constraint lock to the GR ratio is only listed as a possibility (`SPECIALIST_BRIEF_rung3_spine.md:138`), not exhibited. |

**Consequence (per the direction):** the outcome is not FORMULABLE, so **no Π0-1 charter is
drafted or frozen. STOP.**

## §1 Object definition (item 1)

- **Recorded definition** (`X_FLOOR_MAP.md:19`; repeated in `PREDICTION_UNIQUENESS_MAP_01.md:39-40`):

  > "Π₀(ω→0, k→0): the P⁽⁰ˢ⁾ coefficient of the gauge-invariantly assembled retarded influence
  > kernel of the pure-dS graviton sector — ⟨[T^μ_μ, T^ν_ν]⟩_R of exactly what GRUT integrates out".

- **Retarded vs noise:** fixed. K_R = c₂P⁽²⁾ + c₀P⁽⁰ˢ⁾ (retarded/dissipative), and
  N = n₂P⁽²⁾ + n₀P⁽⁰ˢ⁾ (noise), with a per-channel KMS lock n_i = coth(βω/2)·Im c_i
  (`S_IF.md:44-56`). **Π₀ is the commutator/response object.** The noise channel is
  state-dependent; the retarded channel is state-independent only in linear/quadratic structure,
  which does not hold for a graviton loop.
- **Projectors:** fixed. 4d Barnes–Rivers, signature (−+++), θ_μν = η_μν − k_μk_ν/k²,
  P⁽⁰ˢ⁾ = ⅓θθ, where "the ⅓ is load-bearing" (`SPECIALIST_BRIEF_rung3_spine.md:130`).
  - GR reference: linearized Einstein–Hilbert gives P⁰ˢ/P² = −2 exactly (`:124`), and "the EH
    P⁽⁰ˢ⁾ piece *is* the constraint sector" (`:136`).
  - **Caveat:** P⁽⁰ˢ⁾ is invariant only under the spatial subgroup at fixed slicing. Its 4d-covariant
    status needs the Bardeen completion (`calc/RESULTS_operator_basis.md:29`).
- **Order of limits: NOT declared for Π₀.** The K_R contract declares D1 = k → 0 first, ω → 0
  last, but for the TT-class route (`PHYSICS_LEDGER/K_R_CONTRACT_OWNER_RULING.md:14-53`). Adopting
  it for Π₀ would be a new declaration (A-2).
- **Π₂:** never defined independently. It appears only inside "x = f(Π₀/Π₂)".
- **Name collisions to fence:**
  - **Symbol "Π₀".** `program/CANDIDATE_MINING_02.md:168` uses it for a different partition
    candidate.
  - **Name "c₀".** It is used for three objects: the P0s modulus; the Tier-4 local slot certified
    zero in D5; and a historical name for the P^TT coefficient (`calc/RESULTS_operator_basis.md:31`).

## §2 Conditional physical inputs (item 2): all SUPPLIED

| Input | Status | Record |
|---|---|---|
| Coupling class L_int = −(κ/2)h_ijT^ij (minimal universal) | **SUPPLIED** | paper :1284-1286, :1808 (I3); `GR1_CP1_OWNER_RULING_01.md:21-24`; `GR2A_OWNER_RULING_01.md:71` |
| κ = 1/M_Pl | imported (amplitude only) | `GR1_GRAVITY_VERDICT_01.md:79` |
| Spin-2 | **SUPPLIED / not selected** | `GR2B_OWNER_RULING_01.md:19-20`; `CC1_CCONS_VERDICT_01.md:99-117` |
| Universal reach | **SUPPLIED** (I4) | paper :1810 |
| Causal cone | **SUPPLIED** (I6, seam S2) | paper :1815 |
| de Sitter background, flat patch, constant H | declared (contract) | `CLASS_C_MANIFEST.json:15-19` |
| Graviton state | declared as a **Bunch–Davies analogue** (adiabatic Option-B), not exact BD | `K_R_CONTRACT_OWNER_RULING.md:42-44`; paper :105-108 |
| Gauge | contract: unfixed, orbit-tracked (2a). **Class C: UNDECIDED-DISPATCH** | `K_R_CONTRACT_OWNER_RULING.md:34`; `CLASS_C_MANIFEST.json:22` |
| Renormalization scheme | **OPEN** (the D5 ruling among α/β/γ is pending) | `WALL_KR_D5_RENORMALIZATION_AUDIT.md:18-49` |
| Quantum graviton lift | IRREDUCIBLE/SUPPLIED at Level-0. Used de facto (one-loop); no graviton-specific quantization declaration found | `L0_LIFT_SELECTION_OWNER_RULING_02.md` |

**Beyond the declared branch, a Π₀ calculation would need:**
- **(A-3)** a spin-0 / trace probe. Every declared probe is TT (CP1: "the TT projector kills the
  η-terms … collapses to a single TT tensor"). `CLASS_C_MANIFEST.json:26` also forbids exporting a
  scalar result as TT;
- a gauge-fixing + ghost sector, or a conserved-source cut prescription;
- non-TT internal states;
- a Π₀ order of limits (A-2);
- a scheme ruling (A-1);
- the covariant (Bardeen/Riegert–Paneitz) completion (named frontier-reserved,
  `RESULT_KAPPA_2026-08-08.txt:28-29`).

## §3 Gauge / constraint firewall (item 3)

- **What would count as a genuinely gauge-invariant trace-channel spectral contribution:** a
  J = 0 absorptive weight from **either**
  - (i) an on-shell two-graviton unitarity cut sourced by a **conserved** external source; **or**
  - (ii) a fully gauge-fixed one-loop self-energy including ghosts and all internal polarizations,

  shown gauge-parameter-independent after projection, and **separated** from the EH constraint
  piece (the local k²P⁰ˢ term at ratio −2) and from contact terms supported at Δ = 0.
- **Not admissible:**
  - "O(G) ln a secular growth in the gauge-dependent sector ⇒ Π₀ ≠ 0" (the SECULAR-SHORTCUT kill,
    `X_FLOOR_MAP.md:57`);
  - any TT-internal-line trace weight, since it fails Ward at H⁰ (§0, B-1);
  - DOF counting ("no spin-0 graviton propagates ⇒ 0"), which is refuted by the EH counterexample
    (`SPECIALIST_BRIEF_rung3_spine.md:136`).
- **Status:** no construction of type (i) or (ii) exists in the record.

## §4 Renormalization / scheme firewall (item 4)

- **Local, scheme-movable pieces:**
  - the EH k²P⁰ˢ (constraint);
  - the R², Ric² and Riem² counterterms, which all reach P⁰ˢ (C² does not;
    `calc/RESULTS_anomaly_c0_map.md:22-30`);
  - any H⁴-scaled constant in dS at ω → 0 (a Λ-renormalization-type local term). The last is
    operator judgment from dimensional reasoning, to be verified if the campaign ever resumes.
- **Which part could be scheme-independent:** only a **nonlocal/spectral** J = 0 weight
  (discontinuity across the cut) can be scheme-immune. At the target limit that weight's
  ω → 0 behaviour is the B-2 frontier.
- **The target, restated at the only scheme-clean level:**

  > the gauge-invariant J = 0 spectral density of the retarded graviton-environment kernel, and
  > its ω → 0 behaviour in dS, relative to the J = 2 density.

  This restatement is **not calculable** with current machinery (B-1, B-2).
- **Scheme choice:** the D5 ruling (α/β/γ) is pending (A-1). Per the direction, **no downstream
  observable may fix it.**
- Recorded precedents that the campaign must avoid:
  - SCHEME-LAUNDERING (`X_FLOOR_MAP.md:55`);
  - the free, unbounded scheme piece in the anomaly route (`:48`).

## §5 Existing machinery inventory (item 5)

| Instrument | Reusable for Π₀? |
|---|---|
| Tier-1 dS cubic vertex (full, unfixed h; 26,032 terms; gauge gate G6 on shell) | **Yes.** A trace/scalar external leg can be substituted directly. |
| Tier-2 BD-analogue massless TT bath | Partly. Non-TT internal states are missing. |
| Tier-3 one-loop two-graviton cut, H⁰ anchor, three-route cross-check, `EXTS` dict | **Yes, as tooling.** A config e1_ij = δ_ij can be added. It is TT-internal only, and 3 of 4 mutants were killed (M4 unfinished). |
| Tier-4 retarded K_R, log completion, local slots | TT-scoped. It refuses ω ≲ 3.4H. |
| D4 gauge-orbit apparatus, D5 MS machinery | Tooling. D4-A is not yet owner-accepted; the D5 scheme is pending. |
| T3 chain (H³–H⁶), banked 2026-09-21; the frozen dS absorptive-response paper | TT only, k_ext = 0. |
| `calc/operator_basis.py`, `anomaly_c0_map.py` | Flat, local projector algebra. |

**Does the newer validated pipeline lower the old ceiling?** Yes on **construction cost** (the
vertex and cut tooling exist). **No** on the **gauge-dependent spin-0 sector** (its gauge safety is
TT projection) and **no** on the **ω → 0 limit** (outside its certified domain). **Net:** the
ceiling moves from "frontier-blocked on construction" to **"blocked on gauge-invariant spin-0
assembly and the deep-IR limit".**

**Smallest missing construction (verdict-bearing):** a **flat (H⁰), gauge-invariant two-graviton
J = 0 absorptive cut**, via a conserved-source on-shell cut or a gauge-fixed loop with ghosts and
non-TT lines, at **finite k_ext** (so P⁰ˢ and P⁰ʷ separate), normalized against the existing
spin-2 anchor −3ω⁴/1280π.
- It is in-house-tractable as a **diagnostic.** The flat sector is scale-free and IR-clean.
- **It is not the target:** its ω⁴ scaling vanishes at ω → 0. It could establish or refute a
  gauge-invariant J = 0 spectral weight (a Π0-NONZERO-type statement at flat scope). It cannot
  reach Π₀(ω → 0, k → 0).

## §6 Normalization map (item 6)

- **The x = f(Π₀/Π₂) map was never written.** No formula exists in the record. It is described
  only as "convention-level bookkeeping, ledger 0, explicitly NOT R1 closure"
  (`X_FLOOR_MAP.md:47`, `:70`). The adjective "banked" at `:29` is **unsupported.**
- **An α dependence sits downstream, which is a separate blocker for any μ/Σ prediction:**
  - μ(x) = 1 + xα, with η = 1/(1+xα) and Σ = 1 + xα/2, "INHERITED-CONDITIONAL"
    (`GRUT_II_What_Survived.md:47`);
  - the x = 1 endpoint is defined through α (`calc/mu_linear.py:39`, α = 1/3 as the "repo no-go
    value");
  - η = 1/μ is postulated from one-sidedness (`calc/RESULTS_mu_slip_interior.md:13`).

  The ALPHA-BACKDOOR rule bans α from the Π₀ → x step only. **Every x → (μ, Σ) conversion still
  carries α.**
- **Consequence:** even a Π0-VALUE-COMPUTED would **not** yield a pinned μ/Σ without an α-free,
  audited x → (μ, Σ) map. So the "percent-level μ/Σ prediction" route
  (`PREDICTION_UNIQUENESS_MAP_01.md:37, :63, :177, :188`) is blocked at the map as well as at Π₀.
- **Status of the map:** convention-level only, and **insufficient** to convert an invariant Π₀
  into a physical scalar-response coefficient.

## §7 Observability firewall (item 7) and contamination history

- **Downstream only:** Planck low-ℓ TT (via a same-pipeline ΛCDM proxy), DESI Σ₀ (x < ~0.59), and
  the TT-auto edge.
- The TT-auto numbers remain **insertion-contaminated** at the κ-filter level
  (`calc/RESULTS_isw_tt_auto.md:52, :67-69`; `RESULT_KAPPA_2026-08-08.txt:65-95`; A8 stands after
  A6).
- **Past levers the campaign must not reuse:**
  - the κ activation filter;
  - α normalization and "x = α² as a natural point";
  - anomaly-route scheme choice;
  - the p_tt c₀ = 0 choice;
  - a DESI-tuned kernel;
  - the constant-Σ ↔ DESI Σ₀ mapping.
- **Guarded precedent to reuse:** "No numerical value for μ may be selected by optimizing … or
  matching" (`WALL_KR_MU_OWNER_DECISION_PACKAGE.md:12-14`).
- **Pre-registration hygiene carried forward:** motive quantities (tension sigmas) go in a separate
  citing file, never in a hashed charter (`RESULT_KAPPA:98-106`).

## §8 Governance notes (for the owner)

1. **The in-house stop.** `V4_DEPOSIT_01.md:20` says "In-house physics calculation stopped
   2026-09-28". `GRUT_PROGRAM_REOPEN_02.md` resumed in-house calculation **for the Level-0
   successor only.** Π₀ is not Level-0. The owner's direction authorizes Π0-0 (no physics), and
   would authorize Π0-1 only after charter and review.
   - **If** any Π₀ physics is ever run, a one-line owner statement that the direction supersedes
     the v4 stop for this campaign would keep the record clean.
2. **The fence.** Pre-existing documents carry "Λ_R, Matsubara, Π₀, U5 remain fenced" (e.g.
   `NONSTATIONARITY_CHARTER_01.md:13`). The owner's direction effectively lifts the Π₀ fence for
   this campaign; an explicit note would record that.

## §9 What the owner may choose next (not executed; not ranked)

- **(a) Accept FRONTIER-BLOCKED and stop.** The last credible percent-level route is cleanly
  recorded as not calculable from the present branch (B-1, B-2), with the map/α blocker (A-4)
  also standing. This meets the direction's second alternative ("establish cleanly that the last
  credible percent-level prediction route is not calculable from the present GRUT gravitational
  branch").
- **(b) Charter the diagnostic sub-target** (§5): the flat gauge-invariant J = 0 two-graviton cut.
  - It would need its own direction, since it is not licensed by this audit's outcome.
  - It could only establish a flat-scope nonzero or zero J = 0 spectral weight. **It cannot
    unblock Π₀(ω → 0).**
  - It would need new declarations: the gauge-fixing/ghost or conserved-source prescription, and
    the spin-0 probe.
- **(c) Separately address A-4**, i.e. whether an α-free x → (μ, Σ) map can exist at all. This is
  a bookkeeping audit, with no physics.

**HARD STOP** for owner review. No Π0-1 charter, no Π₀ physics run, no empirical fitting, no S-5,
no EA-1, no GR2-e.
