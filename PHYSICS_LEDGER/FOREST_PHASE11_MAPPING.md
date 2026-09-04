# FOREST — PHASE 11: EXPANSION / UNMAPPED-SECTOR MAPPING

**Date:** 2026-09-04 · **Instrument:** `forest_phase11_mapping.py` ·
**Artifact:** `FOREST_PHASE11_MAPPING.json` · **Base:** b34cb24 (H¹ FROZEN; Phase 10
FOREST-EMPTY; Phases 1–10 untouched). **Battery: 50/50, zero failures (post-reconciliation).**
**STATUS: `FOREST-EMPTY (UNCHANGED)` · `MAP-EXPANDED-BY-2` — two additions, both
`MAPPED-UNRESOLVED`.**

**Both adversarial legs returned findings that changed this record.** Leg A: **FAILED** —
it caught that I missed a *second* live item and that my sweep never left the working
tree or the `.md/.json/.py` file types. Leg B: **CONFIRMED with mandatory corrections** —
`FOREST-EXPANDED` overstated, and the suppression expectation needed a channel fence.
All corrections are applied at source below.
A mapping campaign: no physics computation, **no target selected**, **no register
mutation**. Register sha256 identical pre/post; A–F unselected; W-0.

**Scope correction carried from the owner's Phase-10 reading:** the defensible statement
is *"no surviving discriminator in the present mapped pool"* — not "nowhere yet," which
overreached past the pool actually examined. This phase widens the pool.

## A · MAPPED SECTORS — every sector the order names, resolved against repository text

| sector | resolution | evidence |
|---|---|---|
| **flavor** | **MAPPED-ABSENT — no repository content** | every occurrence is colloquial ("generic-flavored", "authority-flavored", "universality-friendly in flavour", "strength flavour"); no Yukawa/CKM/PMNS claim exists |
| **strong CP** | **MAPPED-ABSENT — no repository content** | occurs in **exactly one file**, `provenance/merge_criterion.py`, as a *methodological exemplar* (θ̄ and the electron Yukawa illustrating a merge-counting flaw) |
| neutrino | NOT-A-SECTOR | appears only as an **explicitly forbidden** proxy ("no neutrino loops", rung3 specialist brief) |
| dark matter | RETIRED + DECLARED GAP | "an entire dark-matter substrate line" died with the superseded book; also in `KNOWN_GAPS` |
| quantum gravity | DECLARED GAP | `coverage.py KNOWN_GAPS` |
| black-hole interior | DECLARED GAP | `KNOWN_GAPS` |
| early universe / inflation | DECLARED GAP | `KNOWN_GAPS` |
| baryogenesis | DECLARED GAP | `KNOWN_GAPS` |
| coupling unification | RESOLVED NEGATIVE | "Zero novel positive predictions — no channel examined produced one" (`GRUT_II_What_Survived.md`) |
| QCD | NOT-A-SECTOR | vacuum-energy condensate bookkeeping only |
| gravitational decoherence | REGISTERED, self-disqualified | rung8 falsifier: quiet-or-faint, 7–47 orders below detectability |
| cosmological perturbations | REGISTERED | Phase-10-classified STANDARD-PARAMETERIZATION |
| memory-vacuum phenomenology | REGISTERED | the rung ladder |

**The repository already maintains an honest gap list.** `coverage.py` declares
`KNOWN_GAPS` — five known-physics areas GRUT has **no node** for — with the standing rule
**"absent != covered"**. A declared gap is not an unmapped candidate: it has no claim, no
observable, and no mechanism to map. Naming absences does not expand a forest.

## B · CANDIDATE CLUSTERS

No duplicate-claim inflation was found: the sectors above collapse to *declared gaps*,
*retired lines*, *explicit prohibitions*, and *already-registered nodes*. Exactly one
cluster is a genuine map addition — see §M.

## C · PROVENANCE

`provenance/coverage.py` (gap list), `provenance/merge_criterion.py` (the strong-CP /
Yukawa exemplar), `SPECIALIST_BRIEF_rung3_spine.md` (neutrino prohibition),
`handover/SUPERSEDING_NOTE.md` + `docs/WHERE_IT_STOPS.md` (dark-matter line retired),
`GRUT_II_What_Survived.md` (zero novel positive predictions), `SIGNATURE_AUDIT.md` (the
prior four-domain hunt and its one soft spot), `POSTULATE_MAP.md` (M6),
`RUNG3_KEYSTONE_MAP.md` (the retracted QNM reading), `GRUT_ToE.md` §2.6 and §4.2.

## D · OBSERVABLES

**Two** items terminate in observables not already adjudicated: **BH quasinormal-mode
frequencies / ringdown damping times**, and **cosmological tensor friction Γ_T / the
standard-siren amplitude channel** (both GW-detector observables). All other entries are
gaps (no observable), prohibitions, or retired lines.

## E · PARAMETERS

The QNM item's parameter status is **UNKNOWN pending a dedicated calculation** — the
repository does not establish it. Per §7 of the order this is recorded as UNKNOWN, not
guessed, and it is explicitly **not** labelled parameter-free.

## F · STANDARD SUBTRACTION

Unchanged from Phase 10 and re-affirmed: CTP/open-system machinery, FDT/KMS, Kramers–
Kronig and passivity, the Bardeen μ–Σ parameterization, TT projection, EFT bookkeeping,
H¹/EH recovery — all standard, none counted as novelty. **The program's own top-level
document already reaches this conclusion:** `GRUT_ToE.md` §4.2 is titled *"GRUT's
novel-physics-prediction column is empty — and that is reported straight,"* and §2.6
records that of four differentiators *"none survived as a parameter-free observable
wedge."* Phases 10 and 11 are **consistent with, not corrective of,** that account.

## G · DEPENDENCY FIREWALL

H¹ quarantined and unused as evidence. The QNM item's dependency is `rung4` (dissipative
tidal response, tier `shown`, itself classified **FAILS-DIFFERENTIATION —
real-but-invisible**). That ancestry is the precise reason its expected disposition is
"confirms invisible": it would inherit rung4's suppression.

## H · FLAVOR BRANCH

**MAPPED-ABSENT as a sector in the v4 working tree** — with my first draft's evidence
sentence **corrected**. "No Yukawa … anywhere" was **false as written**: `Yukawa` occurs
in `provenance/prereg/RESULT_KAPPA_2026-08-08.txt`, invisible to a sweep that walked only
`.md/.json/.py`. Those uses are **Yukawa-screened-potential** physics, not flavour
structure, so the *sector* verdict survives while the *evidence claim* is repaired.
Classification: **NOT-ENOUGH-EVIDENCE**.

**Scope, now declared rather than assumed:** this map covers the **v4 working tree**. Leg
A found strong-CP and flavour **content in archived branches** (`origin/v1-retired`'s
`grut_solver/sectors/qcd/strong_cp.py`; a "Conjecture SCP" carrying an explicit falsifier
— *"predicts NO axion … detection of an axion would falsify"*). That is
**scope-contested, not scope-free**: the README declares the earlier lineage is not
certified by this repository. **Recorded as an owner question, not resolved here.**

**A sixth declared absence, outside `coverage.py`:** `EMERGENCE_CHAIN.md` records that
*"The Standard Model — its spectrum, its couplings, its three generations — appears
NOWHERE in the register … the chain's matter link is SILENT."* This is the strongest
in-tree corroboration of flavour-absence — **and it shows flavour and strong-CP are
UNDECLARED absences** (not in `KNOWN_GAPS`), so the "a declared gap is not a candidate"
rule does not by itself cover them.

## I · STRONG-CP BRANCH

**MAPPED-ABSENT**, on the same footing: one file, one methodological exemplar, zero
physics claims. Classification: **NOT-ENOUGH-EVIDENCE**.

## J · COMPLETENESS AUDIT

The searches were content-based across all `.md`/`.json`/`.py` in the repository (this
phase's own outputs excluded to prevent self-confirmation). **My sweep was too narrow and is corrected at source:** it walked only `.md/.json/.py`
(blind to 42 `.txt` files — *all* of `provenance/prereg/` — plus `.log` files and an
archived 73-node register `.bak`), used a substring self-exclusion that wrongly dropped
six unrelated `WALL_D2_PHASE11_*` files, and never declared its working-tree scope. **A
prior expansion already exists and is a standing record:** `SIGNATURE_AUDIT.md`, a pre-registered four-domain
external hunt (GW propagation, cosmology, lab/analogue, transport) with verdict
**EMPTY** — *"No admissible, dedicated, parameter-free signature survives."* Phase 10's
FOREST-EMPTY therefore **confirms an earlier finding by an independent route rather than
discovering it**, and this phase's job was to test whether that audit's coverage was
complete. It was, with one stated exception, which the audit itself names.

## K · LEG A — COMPLETENESS

[[LEGA]]

## L · LEG B — NOVELTY

[[LEGB]]

## M · FINAL FOREST STATUS

**`FOREST-EMPTY (UNCHANGED)` · `MAP-EXPANDED-BY-2`.**

**Why the token changed (Leg B, adopted):** Phase 10's `FOREST-EMPTY` is a statement about
the **register** — and the register is byte-identical here, so that verdict stands
untouched and untested by this phase. Putting `EXPANDED` in the slot that read `EMPTY`
one commit earlier would manufacture the appearance of movement in the *differentiator
set* where none occurred. Worse, the first draft's token was `status = "FOREST-EXPANDED"
if not FAILURES else "INCONCLUSIVE"` — a **pass-label no evidence configuration could
move**. It is now derived from the count of genuine map additions.

### Addition 1 — `bh_ringdown_qnm` (UNREGISTERED)

> **`bh_ringdown_qnm` (UNREGISTERED).** Black-hole quasinormal modes / ringdown damping.
> **Source:** `SIGNATURE_AUDIT.md` — "The one soft spot", the single observable the audit
> *"could not fully close by a dedicated calculation"*; corroborated by
> `POSTULATE_MAP.md` M6, which names "a dedicated QNM/ringdown calc" as the missing item.
> **Why it qualifies:** discussed in the repository, **absent from `claims.json`** (the
> only node mentioning QNM at all is `rung3_single_pole`, in passing) — precisely the
> Phase-11 definition of unmapped.
> **Classification: `MAPPED-UNRESOLVED`** — *not* MAPPED-POTENTIALLY-NOVEL.
> **Expected disposition: "confirms invisible"** — flagged *invisible-by-inheritance*,
> expected to inherit `rung4`'s ~22+ orders of Planck suppression. The audit states
> plainly that until the calc exists, its EMPTY verdict carries this one caveat.
> **Cautionary history, mapped with it:** a prior QNM reading in this neighbourhood was
> **RETRACTED** ("gapped-tower ⇒ QNM — the boundary check tested the wrong thing"). The
> area has already produced one false positive that the machinery caught. **This raises
> the evidentiary bar for the item; it does not lower it.**

### Addition 2 — `gamma_T_siren_amplitude` (UNREGISTERED) — **the item I missed**

> **Cosmological tensor friction Γ_T at ω∼H₀ / the standard-siren amplitude channel.**
> **Verified independently by me, not taken on the leg's word:** `GRUT_ToE.md` lists it as
> item **(1)** of *"the current frontier set (the parked queue)"*;
> `calc/SPEC_gw_tensor_friction.md` **exists** (pre-registered pass/fail) while
> `calc/gw_tensor_friction.py` **does not**; and the register itself says verbatim
> *"GRUT's OWN induced Γ_T at ω∼H₀ is **NOT YET COMPUTED** (calc/gw_tensor_friction.py
> staged; NO number banks until it exists)"*, with the |Γ_T| ≲ few×H₀ figure fenced as an
> **un-computed order-of-magnitude inference — "do not quote as a bound."**
> **Absent from `claims.json` as a node** — the *same* evidentiary situation I used to
> admit the QNM item, which is exactly why omitting it was an error rather than a scope
> choice. **Classification: `MAPPED-UNRESOLVED`.** Note the register's own deflation: the
> dissipative Γ_T + noise *form* is U1-GENERIC published open-EFT — **no validation
> credit for the form**.

**Two Leg-A citations REJECTED after direct check** (the finding adopted, its supports
repaired): a *"Gate to re-admit"* quote attributed to `SIGNATURE_AUDIT.md:68` — that
string appears **nowhere** in that file; and `GRUT_II_What_Survived.md`'s *"Two items
remain live, not one"* — which I verified refers to **rung3's Π₀ and the κ
activation-scale question**, not to QNM/Γ_T. The Γ_T finding stands on the three gated
facts above; the misquotes are not propagated.

**THE SUPPRESSION FENCE (Leg B, mandatory).** Neither addition may be called
*invisible-by-inheritance* without its channel condition: rung4's "22–62 orders below" is
a **dephasing-branch** statement, and `calc/gw_dissipation_bounds.py`'s own scope fence
records that **the amplitude channel is NOT covered by it** — the IR-pole friction
Γ = B·H₀/2 (~0.2 H₀ at the staked B) sits *inside* the quoted slot bound, not orders
below it. **QNM damping time and siren amplitude are both amplitude-channel
observables.** The "confirms invisible" prior is an **inheritance argument, not a
computation**, and it is channel-conditional.

**No target selected. No physics computed. No register mutation.** Whether either item is
worth a dedicated calculation is reserved for a later explicit phase.

## GOVERNANCE EXIT

H¹ frozen; Phases 1–10 byte-identical; `claims.json` unchanged (no register mutation);
A–F unchanged; **no target selected**; no physics computation launched; HEAD ==
origin/v4.

## W-0 STATUS — forest mapped and expanded by one unresolved item; nothing banked; nothing computed.
