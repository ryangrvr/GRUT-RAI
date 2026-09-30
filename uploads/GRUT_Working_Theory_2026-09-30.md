# GRUT Working Theory: Certified Structure, Conditional Emergence, and Open Primitives
## A working-theory / program-status synthesis of the GRUT research program

## Abstract

This release is a working-theory / program-status synthesis of the GRUT research program. GRUT is currently a
theory-construction / conditional-emergence research program with a certified dependency map over explicitly supplied
physical layers; it is not currently a fundamental theory. The release states, with citations into the frozen
repository record: the small set of structural relations derived from the program's core within declared model
classes; the larger set of emergence results that hold only conditionally, after an explicitly supplied parent,
sector, environment, preparation or lift is admitted; the primitives that remain supplied (among them the physical
quantum lift, ħ, outcome selection, and the gravitational branch); the routes that failed or are blocked (among them
ħ emergence, Born-weight derivation at the tested model class, gravity forcing, the Π₀ cosmological route, the strict
pointwise arrow, and the reversal hypothesis); and the frontiers that remain unresolved rather than failed (the
physical origin of noise, and endogenous access). Every result carries its recorded model-class scope, and nothing in
this release upgrades any recorded terminal.

**Mandatory public statements: zero confirmed novel quantitative predictions · no external human peer review.**

## Release provenance

| Field | Value |
|---|---|
| Repository / branch | `ryangrvr/grut-rai` · `master-w25bu9` |
| Frozen content boundary | commit `404f2cd` (publication-ready state; 5/5 editorial cross-check) |
| Release / packaging commit | the metadata-only descendant of `404f2cd` recorded in `CURRENT_STATE.json` and cited in the release notes |
| Version lineage | next version on concept DOI 10.5281/zenodo.19803663; prior paper version DOI 10.5281/zenodo.22983638 (snapshot `6abbf31`, 2026-09-26) |
| Authorization | Owner rulings SYN1-01 (Issue #2 comment `5916545551`) and SYN1-02 (comment `5918358573`) |
| Deposit status | Publication authorized; **publication is not claimed until the returned DOI/version is recorded in the canonical state** |

This document renders three repository files with no content changes; in each part the file's title line is replaced
by the part heading. The repository snapshot at the release commit remains the deeper technical source; the
supporting provenance documents (`GRUT_WORKING_THEORY_SYNTHESIS_01.md`, `GRUT_RECORD_RECONCILIATION_INDEX_01.md`,
`GRUT_SUCCESSOR_STATUS_01.md`, `SYN1_READINESS_VERDICT_01.md`, `SYN1_OWNER_RULING_01.md`) are part of the release
package in their Markdown form.

# Part I — Working Theory Brief

*(renders `GRUT_WORKING_THEORY_PUBLIC_BRIEF_01.md`)*

*A conservative public summary of where the GRUT research program stands. It is based only on results the program's
owner has accepted. The canonical record is `GRUT_WORKING_THEORY_DEPOSIT_01.md`; every statement below traces there.*

**Status of this brief:** publication authorized (owner ruling SYN1-02, Issue #2 comment `5918358573`); deposit
pending. Publication is not claimed until the returned DOI/version is recorded in the canonical state.

---

## What GRUT is, today

GRUT (historically, the Grand Responsive Universe Theory) set out to find a complete physical theory. After a long sequence
of pre-registered, adversarially checked tests, its honest current form is narrower:

> **GRUT is a theory-construction research program. Its main product is a certified map of which assumptions produce
> which effective physical structures, where those derivations work only conditionally, and where they stop. It is not
> a fundamental theory.**

The program describes its current architecture as a small set of **supplied layers**, each an input that the program
does not derive. **Derivations run only downward** from these layers to effective laws and observables.

**The supplied layers:**
- a static substrate;
- a time-evolution law (the "generator");
- how observations access the system;
- the state and preparation;
- an environment;
- the physical quantum realization (the "lift");
- Planck's constant ħ;
- a rule for measurement outcomes;
- the gravitational sector.

**This layering is bookkeeping, not a claim about how nature is built.** It records where the current derivations stop.

## What is derived

A small set of results follows from the program's core assumptions alone. Each holds within a specific declared model
class.

**Core-derived:**
- A spectral gap is necessary for the memory property studied.
- Passivity is necessary for the positivity property studied.
- Locality is necessary for the recovered geometric property in the tested class, but is not needed for the memory
  property.
- Linearity is what makes the exact reduction to linear spectral methods available. This one is definitional.
- The time-ordering found is a relabeling of the assumed time-evolution law, not an independent derivation of time.
- Two certified **non-implications**:
  - locality is not needed for the memory property;
  - the program's earned static structure does not select a unique time-evolution law.

  Further non-implications hold only in other declared model classes. One example is "emergent dissipation does not
  imply a strict ordering in time".

## What is conditional

These are genuine mathematical results, but each holds **only after a supplied layer is admitted**. None of them is
"derived from nothing."

- **Sector-conditioned laws.** Given a fixed microscopic law and a supplied conserved sector, different sectors lead to
  inequivalent large-scale effective laws. This was shown in a free-fermion model.
- **Emergent Markov behaviour.** Given a conservative microscopic model plus a controlled weak-coupling limit, a Markov
  (memoryless) law emerges. It is a *different* one from the law the program originally assumed.
- **Noise versus uncertainty.** In a declared nonlinear stochastic model, ongoing random forcing can be told apart
  observationally from uncertainty confined to the initial condition.
  - In the linear-Gaussian class the two remain equivalent.
  - The only exact deterministic re-description on record encodes the whole noise history in an enlarged hidden
    state. That is a mathematical representation, not a physical origin.
  - No declared physical environment reproduces it.
- **An integrated arrow of time.** In a declared infinite conservative chain with a declared initial temperature
  difference:
  - the system returns to equilibrium;
  - two declared bookkeeping measures each keep a net forward direction, even though microscopic reversals recur
    arbitrarily late:
    - the integrated bath self-energy transfer, which carries an interaction-energy offset and is not a unique heat
      current;
    - a reduced-state entropy-reference measure;
  - for the declared temperature pairs whose measure starts forward, cumulative forward progress is never erased.

  This arrow is integrated, ensemble-level and preparation-relative. It is **not** a restored pointwise monotonic law,
  and it is not a derivation of a fundamental thermodynamic arrow.
- **Influence geometry.** Given ħ and a Gaussian model class, the realizable influence data form a specific convex
  "cone".
- **Gravity sector.** Some gravitational results follow once the gravitational branch is supplied, but not before. The
  branch comprises the coupling class, spin-2, universal reach and a universal causal cone.
- **Cosmological kernel transport.** This is computable from admitted inputs.

## What failed, or is blocked

These are the program's recorded terminal outcomes, stated without softening:

- **The attempt to derive ħ failed.** ħ is an irreducible input: the program located where ħ enters its structure, but
  not its value. This terminal rests on multiply recorded verdicts; no standalone computation file survives.
- **Measurement outcomes and Born-rule weights were not derived** by the model class tested. This is not a disproof of
  the Born rule.
- **Gravity is underdetermined.** The program's core does not select the gravitational coupling, spin-2, universal
  reach or a universal causal cone.
- **The proposed Π₀ cosmological route is blocked** at current scope. Π₀ is a proposed trace-channel response
  quantity. No calculable path to its prediction exists in the present record.
- **The physical quantum realization is not uniquely selected** by anything the program has earned. The program treats
  it as an irreducible supplied input, and it will not invent a new selector to rescue uniqueness.
- **The time-evolution law itself is not derived.** A conservative parent model yields a different law.
- **A strict, pointwise arrow of time is falsified** in the conservative model class. Only the integrated arrow above
  survives.
- **A hypothesized "reversal" structure** was not supported, meaning earned properties feeding back to become new
  ingredients.

## What is unresolved (not failed)

- **The physical origin of noise.** Within the declared nonlinear model class, ongoing noise is distinguishable from
  initial uncertainty; in the linear-Gaussian class they remain equivalent. Whether a physical deterministic environment
  could produce it remains open: no declared candidate exists yet.
- **Whether observational access can be derived from the classical substrate.** The question cannot yet be posed at the
  program's classical core level. It has not been answered negatively.

## What remains supplied

These enter as inputs, not results:
- the substrate;
- the time-evolution law and its direction;
- how access and readout are defined;
- the conserved sector and the initial preparation;
- the environment and coarse-graining;
- the physical quantum realization and its structures (statistics, complex structure, and so on);
- ħ;
- the measurement-outcome rule;
- the gravitational sector;
- the cosmological transport inputs.

## What is experimentally predictive today

**The program currently has zero confirmed novel quantitative predictions, and its results have not had external peer
review.**

- The conditional calculations above are internal mathematical results, not empirical predictions.
- The one cosmological route proposed as a percent-level prediction (Π₀) is blocked at current scope.
- An earlier set of candidate observational channels (the "v4" set) was closed with its channels still open, not
  confirmed.

## Where this leaves the program

GRUT does not currently claim a final theory. It has a defensible working account:
- a small core of earned structural relations;
- a larger set of conditional emergence theorems built on explicitly supplied physical layers;
- a clear record of where the derivations stop.

An architecturally central gap is the step from a classical substrate to the state/observation structure that quantum
physics requires. That gap is recorded, not closed.

*For sources and exact wording, see `GRUT_WORKING_THEORY_DEPOSIT_01.md`, `GRUT_WORKING_THEORY_SYNTHESIS_01.md` and the
owner rulings they cite.*

# Part II — Canonical Working-Theory Deposit

*(renders `GRUT_WORKING_THEORY_DEPOSIT_01.md`, SYN-1 D-1)*

**STATUS: DEPOSIT.** This freezes the current theory boundary.

**Rules:**
- **No new analysis and no synthesis beyond SYN-0.** Every entry is a pointer into accepted records.
- **Authority:** `SYN0_OWNER_RULING_01.md` (Issue #2 comment `5915940892`).
- **Governing synthesis:** `GRUT_WORKING_THEORY_SYNTHESIS_01.md` at `91eaefd`.
- **Companion files:**
  - `GRUT_RECORD_RECONCILIATION_INDEX_01.md` (stale wording → the governing record);
  - `GRUT_SUCCESSOR_STATUS_01.md` (live successor status).

**Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

## A. Current identity

> **GRUT is presently a theory-construction program whose accepted product is a certified dependency map of effective
> structure over an explicitly supplied, multi-layer foundation. It is not a fundamental theory, and it is not only an
> EFT.** (`SYN0_OWNER_RULING_01.md` §2, verbatim)

**Fence:** the nine-layer architecture (§E) is the **minimal bookkeeping architecture supported by the current record**,
not a claim that nature is fundamentally partitioned into exactly nine layers (`SYN0_OWNER_RULING_01.md` §2).

## B. Supplied ledger (by reference)

See SYN-0 §1, **Ledger A (A-1 … A-16)**, where each entry is cited to the ruling that leaves it supplied.

**Summary:**
- the static substrate and the local net;
- the temporal generator, its orientation, and the declared nonlinear drift;
- the access seed, readout and access sets;
- the conserved sector, statistics, initial preparation and partition;
- the physical environment (noise origin) and coarse-graining;
- the physical quantum lift and its prices;
- physical ħ;
- the outcome-selection / Born rule;
- the gravitational branch (coupling class, spin-2, universal reach, universal causal cone);
- the cosmological transport inputs.

**Price rule:** "Lorentz/gauge, symplectic, complex structure, statistics, noise law and physical ℏ distinguish classes
only after they are supplied" (`S5_OWNER_RULING_01.md:85-86`).

## C. Earned ledger

### C-1 Core-derived (accepted; `SYN0_OWNER_RULING_01.md` §3)

| Item | Scope / grade | Source |
|---|---|---|
| gap → memory | LOAD-BEARING | `L0_1A_OWNER_RULING_01.md` |
| passivity → positivity | LOAD-BEARING | `L0_1A_OWNER_RULING_01.md` |
| locality → geometry | NECESSITY-CERTIFIED | `L0_1B_OWNER_RULING_01.md` |
| linearity → exact reduction | NECESSITY-CERTIFIED (definitional) | `L0_1C_OWNER_RULING_01.md` |
| locality ⇏ memory | — | `L0_1B_OWNER_RULING_01.md` |
| the O-5 clock/order | a relabeling of the supplied generator | `L0_1F_OWNER_RULING_01.md` |
| end-site observability | identity-grade (TRIVIAL/IDENTITY) | `L0_ACCESS_BRIDGE_OWNER_RULING_02.md` |
| earned static structure ⇏ unique temporal generator | — | `S5_OWNER_RULING_01.md:81` |

All of these hold on the declared C1-a class, at recorded scope.

**Class-scoped floor results (not core-alone):**
- cycle affinity → ¬P^resp_CM (L0-1d ring);
- linearity ⇏ memory (L0-1c convex-quartic class). This is the accepted content of the "nonlinear relaxation class": a
  **deletion** result, transient-limited, and not a selected class;
- emergent dissipation ⇏ strict ordering (O-6 conservative parent);
- the remaining floor non-implications (`L0_1_FLOOR_DEPOSIT_01.md:95-102`), excluding locality ⇏ memory, which is
  core.

### C-2 Conditionally emergent: derived given explicitly supplied upstream structure

| Result | Terminal | Supplied upstream | Record |
|---|---|---|---|
| Sector-conditioned law formation | SF-1 = FORMATION-OF-LAW-CLASS | conserved sector, free-fermion parent, statistics | `SF1_OWNER_RULING_02.md` |
| Underdamped Markov emergence | S5-1 = MARKOV-LIMIT-OTHER-CLASS | conservative parent + admitted L-vH | `S5_OWNER_RULING_03.md` |
| Nonlinear stochastic discriminator | S2-1 = FULL-DISCRIMINATOR-CONFIRMED | L0-1c drift + declared additive noise | `S2_OWNER_RULING_03.md` |
| Return to equilibrium; integrated arrow | S6-1 = NET-ARROW-CONFIRMED (NO-ERASURE-ON-OPEN-MEMBERS) | conservative parent + declared preparation; J = bath self-energy flux | `S6_OWNER_RULING_02.md` |
| Influence-cone geometry | P-2 CONE-CONFIRMED (Gaussian class) | ħ / quantum class | `P2_S1_OWNER_RULING_01.md` |
| Gravity-sector results (U-1, RS-1, TT-1, ω⁷ occupancy) | conditional | the supplied quadruple | `GR2_SYNTHESIS_OWNER_RULING_01.md`; `GR2A_OWNER_RULING_01.md` |
| FRW kernel transport | computable | admitted inputs | `KERNEL_TRANSPORT_OWNER_RULING_01.md` |

**Also recorded, but not in the owner's §3 list:** branch-class selection, PROVISIONAL (in class). See
`GRUT_RECORD_RECONCILIATION_INDEX_01.md`, item 10.

**These are not "derived from GRUT from nothing."**

## D. Hard negative ledger (exact terminals)

### Failed / blocked / falsified

| Terminal (exact) | Record |
|---|---|
| ħ emergence: **FAILED**, ħ is an irreducible input ("located, not derived"; P-2: "Located, not generated") | `program/GRUT_REALITY_CHECK_01.md:44`; `GRUT_WORKING_THEORY_01.md:311`; `P2_S1_OWNER_RULING_01.md:37-43` |
| **EXPERIMENT_P_FRONTIER = CLOSED_AT_TESTED_MODEL_CLASS** ("not a universal disproof of the Born rule"); outcome selection / Born weights not derived | `GRUT_PROGRAM_CLOSURE_01.md:38-43` |
| **GRAVITY_UNDERDETERMINED** | `GR2_SYNTHESIS_OWNER_RULING_01.md:13-14` |
| **Π0-0 = FRONTIER-BLOCKED** | `PI0_TRACE_CHANNEL_OWNER_RULING_01.md:11-12` |
| **L0 ACCESS BRIDGE = NONUNIQUE-LIFT**; **L0 LIFT SELECTION = IRREDUCIBLE/SUPPLIED** | `L0_ACCESS_BRIDGE_OWNER_RULING_02.md:10`; `L0_LIFT_SELECTION_OWNER_RULING_02.md:9` |
| **REV-0 = NOT SUPPORTED at recorded scope** | `L0_STRUCTURAL_DIAGNOSTIC_REVERSAL_OWNER_RULING_01.md:9` |
| **O-6 = FALSIFIED** (strict pointwise arrow) | `L0_1G_OWNER_RULING_02.md:9-10` |
| **O-2 = FALSIFIED**; **O-7 = FALSIFIED** | `L0_1H_OWNER_RULING_03.md:8`; `L0_1_FLOOR_O7_OWNER_RULING_01.md:10` |
| **S5-0 = GENERATOR-IRREDUCIBLE/SUPPLIED**; the conservative parent does not derive the Level-0 G-D generator | `S5_OWNER_RULING_01.md:9`; `S5_OWNER_RULING_03.md:117-120` |
| **SFG-0 = CLASS-SPLIT** (Tier E: no formation variable; "NO CURRENT CANDIDATE") | `SFG0_OWNER_RULING_01.md:60,73` |
| **S3-0 = FORMULABLE-ONLY-WITH-CHANGE** (the crossed cell is not in the theory at fixed invariants) | `S3_OWNER_RULING_01.md:9` |

The full list is in SYN-0 §4.

### Unresolved (not failed)

| Terminal (exact) | Record |
|---|---|
| Physical origin of the noise: **S2-HB = UNRESTRICTED-REALIZATION-ONLY**, sub-label NO-PHYSICAL-BATH-CANDIDATE | `S2_HB_OWNER_RULING_02.md:9,47` |
| Endogenous access: **EA-0 = UNFORMULABLE at the earned Level-0 scope** ("not negatively answered") | `EA0_OWNER_RULING_02.md:11-21` |

### Prediction status

**Zero confirmed novel quantitative predictions; no external human peer review**
(`GRUT_PROGRAM_STATE_SYNTHESIS_01.md:164-165`). v4 is DEPOSITED_CLOSED, with its channels "STILL OPEN"
(`V4_DEPOSIT_01.md`).

## E. Minimal architecture (accepted; `SYN0_OWNER_RULING_01.md` §5)

> substrate + generator + access + state/sector/preparation + environment + physical lift → effective
> observables/laws

ħ, the outcome rule and the gravitational branch are carried as separately supplied structures where required.

- **The nine supplied layers** are listed in `SYN0_OWNER_RULING_01.md` §2. They are **mutually non-selecting** on the
  record. The only cross-layer relations are possibility without selection (NONUNIQUE-LIFT) and conditional supply
  (statistics → sector, SFG-0 Tier C). Physical ħ is also one of the lift's prices, so those two layers overlap.
- **Arrow grades** are DERIVED / CONDITIONAL / SUPPLIED / BLOCKED / FALSIFIED-NON-IMPLICATION: 14 graded arrows and 18
  graded non-arrows, in SYN-0 §5.2.
- **Direction:** all derivations run downward, and no property → ingredient edge exists (REV-0, recorded scope).
- **No reversal/self-duality diagram.**
- **Architecturally central seam:** classical local substrate **?** state/access algebra (`EA0_OWNER_RULING_02.md:110-112`).
  **It is not an open campaign.** L0 LIFT SELECTION = IRREDUCIBLE/SUPPLIED stands. The preserved faithful-representation
  audit could only constrain, not select.

## F. Claim fence

**GRUT currently claims:**
- a small core of certified ingredient → property relations and non-implications, in declared classes;
- a set of conditional emergence theorems, each valid given its explicitly supplied upstream structure;
- a hard, cited map of what failed, what is blocked, and what remains unresolved;
- the minimal bookkeeping architecture above.

**GRUT does not currently claim:**
- to be a fundamental theory, or a theory of everything;
- to derive ħ, the physical quantum lift, the Born rule or outcome selection, or gravity (coupling, spin-2, universal
  reach, causal cone);
- a Π₀-based cosmological prediction;
- that noise is primitive, or that it is not;
- a fundamental thermodynamic arrow, or broken microscopic reversibility. The S6 arrow is integrated, ensemble-level
  and preparation-relative;
- that J is a unique heat current (it is the bath self-energy flux);
- that any earned property constructs a supplied ingredient;
- that nature consists of exactly nine layers;
- any confirmed novel quantitative prediction;
- that the temporal generator or the L0-1c drift is derived;
- that coarse-graining is dynamically derived;
- that O-6 is repaired;
- that GRUT has a formation variable;
- a disproof of the Born rule;
- that reality is nonlocal.

# Part III — Publication Manifest

*(renders `GRUT_PUBLICATION_MANIFEST_01.md`)*

**Authority:** `SYN1_OWNER_RULING_02.md` §8 (Issue #2 comment `5918358573`). **This manifest contains no new
scientific analysis.**

| Field | Value |
|---|---|
| **Public title** | **GRUT Working Theory: Certified Structure, Conditional Emergence, and Open Primitives** |
| **Release identity** | Working-theory / program-status synthesis (not a ToE claim, not a prediction paper, not peer-reviewed) |
| **Manifest date** | 2026-09-30 |
| **Publication date** | Assigned at deposit; recorded with the returned DOI/version |
| **Repository** | `ryangrvr/grut-rai` |
| **Branch** | `master-w25bu9` |
| **Frozen content boundary (exact commit)** | **`404f2cd`** — the publication-ready state (5/5 editorial cross-check) |
| **Release / packaging commit** | The descendant of `404f2cd` that adds only this manifest, the publication rulings and state bookkeeping. `git log -1 -- GRUT_PUBLICATION_MANIFEST_01.md` identifies it; the release notes must cite it explicitly. |
| **Version lineage** | The next version in the existing GRUT public record lineage, **concept DOI 10.5281/zenodo.19803663**. Prior paper version: DOI 10.5281/zenodo.22983638 (snapshot `6abbf31`, 2026-09-26, with the dated update of 2026-09-27). Software concept lineage: DOI 10.5281/zenodo.18993689. |

## Included documents

**Primary public documents:**
1. `GRUT_WORKING_THEORY_DEPOSIT_01.md` — the canonical working-theory deposit
2. `GRUT_WORKING_THEORY_PUBLIC_BRIEF_01.md` — the public-facing brief

**Supporting provenance / navigation:**
3. `GRUT_WORKING_THEORY_SYNTHESIS_01.md` — the accepted SYN-0 synthesis (five ledgers; architecture)
4. `GRUT_RECORD_RECONCILIATION_INDEX_01.md` — canonical pointers for stale/conflicting historical wording
5. `GRUT_SUCCESSOR_STATUS_01.md` — the live successor-status index
6. `SYN1_READINESS_VERDICT_01.md` — the readiness verdict, with the editorial cross-check appendix
7. `SYN1_OWNER_RULING_01.md` — the owner ruling fixing the A-1 … A-4 statuses

The repository snapshot at the release commit remains the deeper technical source; the documents above point readers
into it.

## Scope statement

This release is a working-theory / program-status synthesis of the GRUT research program. GRUT is currently a
theory-construction / conditional-emergence research program with a certified dependency map over explicitly supplied
physical layers; it is not currently a fundamental theory. The release states, with citations into the frozen
repository record: the small set of structural relations derived from the program's core within declared model
classes; the larger set of emergence results that hold only conditionally, after an explicitly supplied parent,
sector, environment, preparation or lift is admitted; the primitives that remain supplied (among them the physical
quantum lift, ħ, outcome selection, and the gravitational branch); the routes that failed or are blocked (among them
ħ emergence, Born-weight derivation at the tested model class, gravity forcing, the Π₀ cosmological route, the strict
pointwise arrow, and the reversal hypothesis); and the frontiers that remain unresolved rather than failed (the
physical origin of noise, and endogenous access). Every result carries its recorded model-class scope, and nothing in
this release upgrades any recorded terminal.

## Mandatory public statements

> **zero confirmed novel quantitative predictions**

> **no external human peer review**
