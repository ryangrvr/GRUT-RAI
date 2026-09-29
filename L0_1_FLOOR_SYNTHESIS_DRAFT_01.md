# L0-1 FLOOR — O-7 SYNTHESIS: PROVISIONAL DRAFT 01

**STATUS: PROVISIONAL. NOT ADJUDICABLE YET.** By T5 of the adopted
termination condition, O-7 is adjudicated only once O-1 … O-6 are all
terminal, and **O-2 is still open.** This draft assembles what the
terminal results earn, adjudicates the frozen hypothesis *provisionally*
clause by clause, and marks every place O-2's result could change the
reading. Nothing here is a terminal label, and no new computation was
run.

**Authority:** the owner's direction (`L0_1G_OWNER_RULING_02.md`):
"combine the terminal floor results and ask what structural
ingredients are actually surviving, **without turning any of these
failures into a patched theory.**"

## §0 The terminal record this synthesis rests on

| Obligation | Label | What it earned, at its recorded scope | Ruling |
|---|---|---|---|
| O-1 D-HERM-a | **CLASS-SPLIT** | On one ring with one symmetric part: asymmetry with zero cycle affinity is reducible to a reciprocal twin, so the retained-site response stays completely monotone (CM). Cycle affinity breaks response CM exactly at every declared member. The memory envelope survives. | `L0_1D_OWNER_RULING_01.md` |
| O-2 D-HERM-b | **OPEN** | Accretivity vs spectral stability at the retained site. The candidate is the attached directed ring. F-7 is an observability result, not a verdict. | — |
| O-3 D-DET-a | **DISCHARGED** | With the fluctuation–dissipation relation (FDT) held, determinism is not load-bearing for any tested predicate on either object (identity-grade). Primitive vs derived noise is indistinguishable at second order (S-1). | `5888965691` |
| O-4 D-DET-b | **CLASS-SPLIT** | Correlation CM is a convex cone in temperature-profile space with FDT in its interior. Profiles non-increasing away from the retained site stay CM. Far-end heating breaks CM beyond a threshold. **The size of the detailed-balance break does not predict the outcome.** | `5893630527` |
| O-5 D-ORD-a | **DISCHARGED** | The primitive time parameter is removed; the generator is presupposed (S-5). Strict-Lyapunov structure is **sufficient** for derived order, and recurrence (α∩ω) is an **obstruction** (Conley boundary). In the stationary OU class, the lag directions are distinguishable iff detailed balance is broken, and only through cross-correlations. | `5893871264` |
| O-6 D-ORD-b | **FALSIFIED** | In the conservative split: no pointwise state-function ordering (I-1 … I-4). The past hypothesis produces an anti-arrow at switch-on (I-5). Band-edge memory forces perpetual sign alternation of the ensemble heat and entropy trends (D-1). **Emergent dissipation/memory ≠ emergent strict ordering.** Coarse arrow: open (S-6). | `5895858851` |

## §1 Provisional adjudication of the frozen hypothesis (wording unchanged)

**The frozen hypothesis** (design §2, verbatim):

> "the floor's three formulability obligations reduce to two deeper
> structural properties: **dissipation (for ordering)** and **detailed
> balance (for the generator and noise structure).**"

**Frozen companion (design §3, H-ORD):**

> "ordering is derivable from static substrate data exactly in the
> dissipative classes; in conservative classes it is derivable only
> through emergent dissipation, and then only window-relatively."

### Clause D: "dissipation (for ordering)"

| Evidence | Direction |
|---|---|
| O-5: in every declared dissipative relaxational class (symmetric, accretive, spectrally stable, gradient), a strict Lyapunov function is exhibited and order is derived. | **Supports**, for *primitive* dissipative generators. |
| O-5: the recurrence obstruction, plus stable limit cycles (dissipative and recurrent), show "exactly in the dissipative classes" fails in general. This lies outside the record's classes. | **Against the "exactly" wording**, outside scope. |
| O-6: in a conservative split, dissipation *emerges* (memory, continuum, decay), yet strict ordering fails through the initial slip and band-edge reversals. | **Refutes H-ORD's second clause** in its strict form. |

**Provisional reading: CLASS-SPLIT.**
- Within the record, "dissipation" is **not one property.**
- What carries derivable order is **primitive strict-Lyapunov
  structure of the generator.**
- **Emergent** dissipation (decay and memory from a conservative split)
  does not carry strict order.

The frozen wording stays as it is. Whether it should be *re-worded*
(S-4) is not decided here, and would need a T4 ruling.

**O-2 cannot change this clause.** O-2 concerns positivity at the
retained site, not ordering. Clause D is therefore stable against O-2.

### Clause DB: "detailed balance (for the generator and noise structure)"

| Evidence | Direction |
|---|---|
| O-1: generator route. Cycle affinity (broken detailed balance) breaks response CM, and zero-affinity asymmetry does not. **"Asymmetry ≠ the relevant distinction."** | **Supports**, generator route, response object. |
| O-4: noise route. Broken detailed balance does **not** break correlation CM near FDT. **Its magnitude does not predict CM**; the placement of heat relative to the retained site does. | **Refutes a universal detailed-balance → positivity link**, noise route, correlation object. |
| O-3: FDT-held determinism is not load-bearing. | Neutral (identity-grade). |
| O-5 D-5: the stationary lag directions are distinguishable iff detailed balance is broken. | **Supports**, as an *orientation* role in stationarity, not a positivity role. |

**Provisional reading: CLASS-SPLIT by route and object.**
- Detailed balance is decisive on the **generator/response** route.
- It is **not** decisive on the **noise/correlation** route, where
  geometry (where the heat sits) decides.
- The contrast is **confounded** across object, substrate, and route
  (the reversal diagnostic's caution). **S-3, the crossed generator →
  correlation cell, is what would separate them.**

**O-2 could change this clause.** O-2 tests generator-side positivity
under a *different* generator property (accretivity vs spectral
stability) on a non-reciprocal ring. A result there would add a second
generator-route entry, and could either strengthen or complicate "on
the generator route, detailed balance is what matters". **This clause's
reading is provisional in a way that clause D's is not.**

### The hypothesis as a whole

Provisionally, **"two properties" survives only as a split at the
recorded scope:**
- one property (strict-Lyapunov structure) carries ordering;
- the other (detailed balance) carries generator-route positivity;
- **neither is the single deep property its name suggested,** and each
  failed exactly where it was stretched: emergent dissipation for D,
  the noise route for DB.

Under T2 that pattern is a **CLASS-SPLIT**, proposed provisionally and
not assigned.

## §2 What survives: the structural ingredients, at recorded scopes

This is the owner's question. It is answered **only from certified
lines**; interpretations are kept apart in §3.

| Ingredient | Earned role | Grade | Source |
|---|---|---|---|
| spectral gap | → P_memory (finite-memory decay) | necessity-certified | L0-1a |
| passivity / accretivity | → P_positivity | necessity-certified (symmetric case; the non-normal distinction is **O-2**) | L0-1a; R-4 |
| locality | → P_geometry, **not** response | split certified | L0-1b |
| linearity | → exact reduction only | certified | L0-1c |
| cycle affinity | → loss of reciprocal response CM (generator route) | class-split certified | O-1 |
| noise geometry (heat placement relative to the retained site) | → correlation CM; **detailed-balance magnitude does not decide** | class-split certified | O-4 |
| strict-Lyapunov structure | → derivable order (sufficient; recurrence obstructs) | theorem-grade, discharged | O-5 |
| the generator | **presupposed**; carries the clock and the orientation | on the face of O-5 | S-5 |
| a restricted initial class (past hypothesis) | **forced** for any nontrivial ordering in conservative classes (I-1), yet **not sufficient** (I-5 slip; O-6 reversals) | identity + falsified | O-6 |

**Distinctions the floor earned** (each certified, each preventing a
conflation the program had been making):
- **response ≠ correlation:** they respond to different ingredients
  (O-1 vs O-4; F-5 separates them);
- **order ≠ orientation:** the generator's sign carries the orientation
  (O-5);
- **emergent dissipation ≠ emergent ordering** (O-6);
- **asymmetry ≠ irreversibility-relevant structure** (O-1);
- **detailed-balance magnitude ≠ positivity outcome** (O-4);
- **primitive vs derived noise:** unformulable at second order (S-1).

## §3 What must not be done (the owner's no-patching rule, made concrete)

- **O-6's falsification may not be rescued** by redefining "ordering"
  to mean the coarse arrow. That is S-6, a *separate* question with its
  own pre-registration, and it is not evidence for H-ORD.
- **O-4 may not be read as "detailed balance matters after all"** by
  moving to a different measure of its break. The record says the
  magnitude does not decide.
- **The two-property hypothesis may not be re-worded** to fit (S-4)
  without a T4 ruling, and a re-wording would be a *new* hypothesis,
  not a vindication.
- **No certified line here is a property → ingredient edge.** The
  reversal diagnostic's graph is still acyclic; that diagnostic is
  Level-0 synthesis work and is not evaluated here.

## §3a The owner's reading of the provisional synthesis (recorded 2026-09-29, in-session; hedges preserved)

**On what the floor has done.** The substrate is "looking less like a
bundle of axioms and more like a factorization of functions: different
structural ingredients doing different jobs." The original simple
story (gap + passivity + locality + linearity → memory + positivity +
geometry + reduction, then dissipation + detailed balance as the deeper
pair) has been **systematically split apart.**

**On time.** "Dissipation produces time" is too crude. There are at
least two kinds of dissipation:
- dissipation **already present in the effective generator**, which
  can supply a Lyapunov ordering (O-5);
- dissipation **emerging from coarse-graining a conservative system**,
  which supplies memory and irreversible-looking behavior yet no strict
  arrow (O-6).

The descent "has not simply found 'the source of time.' It has found
**conditions under which ordering can and cannot be reconstructed.**"

**On detailed balance.** The story has fractured: cycle affinity
breaks response CM, and noise-side detailed-balance breaking does not
break correlation CM. The system asks "how is the nonequilibrium
structure positioned relative to the observable/access point?" rather
than "how far from equilibrium?". The owner flags, *"very carefully"*,
a possible common theme with the earlier access-relative geometry
result: **structure is relational rather than scalar.** Recorded as a
live interpretive theme, **not** a result.

**On method (binding for O-7).**
- **The direction is O-2 result → O-7 synthesis, never O-7
  hypothesis → interpretation of O-2.**
- Once O-2 closes, O-7 is **an accounting exercise**: *given
  everything actually earned, what is the smallest structural statement
  that survives all of the deletions and counterexamples?*
- It is **not** "what theory accommodates everything?".

**On the failures.** The owner reads the "not ⇒" results as possibly
the deepest content, "exactly what a minimality program ought to do":
- linearity ⇏ memory;
- locality ⇏ memory;
- asymmetry ⇏ irreversibility;
- noise nonequilibrium ⇏ correlation failure;
- effective dissipation ⇏ strict ordering;
- past hypothesis ⇏ arrow at t = 0.

Each holds at its recorded scope.

**On O-2.** Don't rush it. Let the one-way ring attack the question as
hard as possible. The valuable outcome is a clean separation between
what is genuinely necessary and what merely happened to work in the
earlier construction. O-2 is allowed to fail.

**Operator notes on this reading (for the owner to correct or accept):**
1. **O-2's frozen content is H-HERM-2**, accretivity vs spectral
   stability, not the generalization of the cycle-affinity result. The
   one-way ring also carries maximal affinity, so a *separately
   pre-registered* affinity line is possible, but it must not be folded
   into O-2's terminal verdict.
2. **No floor obligation can produce a property → ingredient edge.**
   Each deletes an ingredient and reads a property. The reversal
   diagnostic's positive outcome needs *constructive* post-floor work,
   so it will not come from O-2.
3. **O-4's "placement over magnitude" has a local mechanism:** the
   odd-moment hierarchy (the retained site sees near temperatures
   first). The "relational rather than scalar" theme must not rest on
   O-4 alone, because part of it reduces to locality plus a distance
   hierarchy.

## §4 What is needed to finish O-7

1. **O-2 must reach a terminal label** (T5). Two routes:
   - charter its named candidate (the attached directed ring), within
     the one-re-charter budget and with O-1's exact machinery; or
   - an owner ruling on another terminal label with a documented reason.
2. After that, this draft becomes the adjudication. **Clause DB is the
   part O-2 can move.**
3. Then the floor ledger is filed as a deposit (T5), together with the
   successor list S-1 … S-6.
