# GRUT ONTOLOGY RECONSTRUCTION 01 — what the calculations force reality to be

**Date:** 2026-09-25 · **Charter:** `ONTOLOGY_RECONSTRUCTION_CHARTER_01.md`
(owner instruction verbatim; fences binding). **Status: RECONSTRUCTION,
NOTHING BANKED.** Register untouched; ledger 0. Every statement below carries
the grade its source records; sources are cited inline. Built from four
independent evidence sweeps over the committed record, the RRT-0 primaries
(fetched from `origin/rrt0-phase2` and read at source), and a TestingGRUT
cross-check. **This document does not assume the present GRUT architecture is
correct, and where the record says it is not, it says so.**

Status classes (owner-fixed): **DERIVED** · **CONDITIONALLY DERIVED** ·
**EMPIRICAL INPUT** · **OPEN** · **DISDERIVED**. One extra class was forced
by the evidence itself: **EXTERNAL-RECORD** — a result the instruction or the
RRP synthesis cites whose primary computation is NOT committed in this
repository. Nothing in that class is treated as banked here.

---

## 0. PROVENANCE GAPS FOUND DURING MINING (owner action available)

Three cited results have no committed primary source:

1. **`u3_continuum_origin.py`** — the finite-substrate → continuum
   investigation, with its C6 conditional gravity-as-bath viability estimate
   and its flagged t^(−d) vs t^(−d/2) internal inconsistency. Exists only in
   an external copy (`grut vs code builder copy/calc/`;
   `rrp/RRP_PROGRAM_SYNTHESIS_01.md:176-183`).
2. **The ℏ-emergence attempt's computation.** The verdict is multiply and
   consistently recorded ("hbar-emergence attempt failed; hbar is an
   irreducible input" — `program/GRUT_REALITY_CHECK_01.md:44,59`; confirmed
   in TestingGRUT's `program/GRUT_REALITY_CHECK_01.json` and
   `REALITY_CHECK_02_MATRIX.json`), but no computation file exists in either
   repository.
3. **The gravity-as-bath "spectrally viable" / acoustic-Cherenkov
   disderivation record** — appears only in the owner's instruction and,
   plausibly (inference, not stated), as the external file's C6.

The reconstruction below marks every dependence on these EXTERNAL-RECORD.
**Committing the external files (and correcting #1's inconsistency) would
convert three of this document's weakest citations into ordinary ones.**

---

## A. ONTOLOGY — what exists, on the record

**The honest answer: the record does not establish a substrate ontology. It
establishes a constraint system that any substrate ontology must satisfy —
and that constraint system is the actual content.**

The audits are explicit that nothing sits beneath the effective level:

- "**There is no sub-QFT ontology in this repository.** The layer that
  exists is standard QFT — microscopic *relative to the kernel* … the
  repository *assumes* the answer and prices it"
  (`ROOT0_FOUNDATION_AUDIT.md:73-77`; instrument retired, findings kept).
- The bath is "the gravitational vacuum's non-metric degrees of freedom,
  **integrated out and NOT specified**" (`S_IF.md:21`); "degrees of freedom
  | E — GENUINELY UNRESOLVED"; "the whole that U3 partitions is nowhere
  registered" (`WALL_KR_U3_PROGRAM.md:34,39`).
- The one ontological bet — "the gravitational vacuum IS a responsive medium
  with finite memory" — is "a STANCE, explicitly not derived," carried at
  +1, **with REVERSED history on its face**: exact dS free-field theory
  forces **infinite scale-free memory**, the negation of the strongest form
  (`rung1_ontology_finite_memory`; `BOOK_I_FOUNDATIONS.md:110-115`;
  `GRUT_PROGRAM_FREEZE.md:110-112`).

**Verdict on the old ontology, per the charter's own fence ("if the scalar
vacuum field was the wrong ontology, say so"):** the finite-memory
single-pole vacuum is **DISDERIVED in its strongest form**; the
responsive-medium reading survives only as a priced stance; and the
constitutive kernel is **secondary, not primitive** — ROOT-1's verdict is
KERNEL-STANDARD: "derived given the declared inputs; **forced by no
principle**" (`ROOT1_KERNEL_ORIGIN.md:15-16,49`). The deep object is not the
kernel; it is whatever supplies the kernel's inputs.

**What any candidate ontology X must satisfy** (each item at its recorded
grade — this is section A's positive content):

| # | constraint on X | grade / source |
|---|---|---|
| A1 | X's effective description must **contain a single universally coupled helicity-2 sector with EH+Λ dynamics** at leading derivative order | O-grade, five pinned data legs (`RRP_00_REQUIREMENTS_PICTURE_01.md:44-52`); "pins the effective sector only, never the substrate" |
| A2 | If X's graviton is emergent, X must **name its exit from a Weinberg–Witten hypothesis** | condition, R8.3′ (ibid.:61-66) |
| A3 | X must satisfy **gauge-anomaly consistency by some declared mechanism**; the observed fermion content cancels anomalies generation by generation (O-grade datum) | R6.1′ (ibid.:55-61) |
| A4 | X must **derive or price**: its subsystem decomposition and state selections (contentful: SJ ≠ BD, formalism-fixed), its probability rule and branch weights, its time-asymmetric boundary data, and G and Λ | M/D-grade, the derive-or-price core (ibid.:33-42,141-149); CPR's uniqueness-given-existence is the lone recorded conditional alternative |
| A5 | X **need not be local, Lorentz-invariant, tensor-structured, or arrow-carrying at substrate level** — none of these is forced ("preferred-frame EFTs pass every bound; effective cones only"; substrate structural claims "analytic … or counterexampled") | RRP-00 not-in-core list (ibid.:94-102); `RRP_PROGRAM_SYNTHESIS_01.md:50-53` |
| A6 | If X is a **finite closed system under linear dynamics**, it cannot express the record's surviving influence datum: raw Φ is fully reducible, "for ALL linear dynamics — unitary, dissipative, non-invertible, Lindblad alike; **escaped only by nonlinearity**" — and the finite type-I arena cannot host the half-sided modular (III₁) structure the surviving time-datum lives in | DERIVED, model-class-scoped (`rrt0/MODEL_CLASS_VERDICT.md` read at source on `origin/rrt0-phase2`; `GRUT_PROGRAM_FREEZE.md:74-76`; `CROSS_WORKSTREAM_RRT0_RAI_AUDIT.md:70,80`) |
| A7 | X must supply **one relative Z₂ time-datum** (the alignment of a spectral half-line with the decaying side of a KMS weight) or derive it; every audited closure consumed it, none produced it | X1: ESTABLISHED per-case, SUPPORTED as generalization (`RAI_DIALECTIC_CHAMBER.md:57-65`; `RAI_FINAL_BOSS.md:61-72`) |
| A8 | X must reproduce **persistence-for-free on dS** (the H²/4π constant tail, "the surviving fixed point of every deletion test") while **paying explicitly for forgetting and direction** | clause 1 controlled-derivation-conditional-on-background; clause 2 induction, not theorem (`GRUT_PROGRAM_FREEZE.md:160-164`) |
| A9 | X's cosmological-sector response must be a **two-time kernel K(t,t′)**; stationary K(Δt) only on states with the warranting symmetry (measured: best Δt-only approximation leaves R = 0.516 on the frozen grid; local dS transport valid only for lags ≲ 0.25/H₀) | this session's chain (`KERNEL_TRANSPORT_VERDICT_01.md`; `NONSTATIONARITY_RESULT_01.md` incl. CORRECTION 01) |

**Whether finite-dimensional local state spaces suffice (charter Q1):** OPEN
as a general question; in the one tested arena the answer was **no for the
surviving datum** (A6). Locality at substrate level is **not forced** (A5);
operationally, in the effective theory, "locality" meant polynomial
derivative structure in (ω², k²) (`WALL_A_A3_DECLARATIONS.md:32`).

## B. DYNAMICS — what X does, at recorded strength

1. **Linearity is a fork, and the record prices both tines.** Linear
   dynamics of any kind cannot generate the tested classes of irreducible
   emergence (A6) and "dynamically generated Born weights [are] IMPOSSIBLE
   without breaking a class premise"
   (`program/REALITY_CHECK_05_BOUNDARY_MAP.md`). The named escape is
   nonlinearity — "named, fenced, and expensive (Gisin signalling)"
   (`BOOK_III_QUANTUM_REALITY.md:449-453`). So X's dynamics is either
   linear-plus-priced-selections (the audited pattern) or nonlinear with the
   signalling price confronted. No third audited option exists.
2. **Openness or the thermodynamic limit is required for irreversibility.**
   With finitely many modes coherence "returns to exactly 1" at t_rec ∝ N;
   monotone decay exists "*only* in the many-mode/thermodynamic limit"
   (`ARROW_OF_TIME.md:43-44`; `calc/arrow_origin.py`). Closed finite
   dynamics recurs. DERIVED in the tested model class.
3. **Dissipation existence/magnitude is dynamics-intrinsic; direction is
   state-supplied** — three guises (contour, KMS β>0, factorization), "three
   faces of one: a low-entropy, uncorrelated, passive past-boundary state,"
   with the anti-laundering rider that even the intrinsic half is relative
   to a passive reference state (`ARROW_OF_TIME.md:11-32,64`;
   `calc/RESULTS_arrow.md:6-24`). M-grade, RRP-audited.
4. **Passivity is channel-diagonal and pins nothing:** the admissible
   response cone gives "no amplitude ceiling, no ratio pin … the structural
   reason no number ever came out" (`x_no_pin_theorem`;
   `GRUT_PROGRAM_FREEZE.md:72-73`). Dynamics constraints of this class
   classify; they do not select.

## C. EMERGENCE MAP — the dependency graph, arrow by arrow

Format: **arrow · status · evidence · the calculation that distinguishes it
from a philosophical story** (owner requirement).

| arrow | status | evidence (recorded strength) | distinguishing calculation |
|---|---|---|---|
| finite local dynamics → continuum | **OPEN** (EXTERNAL-RECORD partial attempt) | `u3_continuum_origin.py`: FAIL-forward, outside adjudication, internally inconsistent (t^−d vs t^−d/2) | commit + correct the file; decide the K_env tail exponent; test which continuum structures survive changes of microscopic detail |
| continuum (many modes) → effective irreversibility | **DERIVED (model class)** for existence; **EMPIRICAL INPUT** for direction | recurrence at finite N vs monotone decay in the limit (`arrow_origin.py`); direction = past-boundary state | already run; the open half is whether any dynamics-intrinsic direction exists outside the KMS class (scoped, not universal — `ARROW_OF_TIME.md:59-64`) |
| dS geometry → persistent memory | **DERIVED** (conditional on background) — but the memory is **infinite and scale-free**; finite single-pole memory **DISDERIVED** across all seven surveyed mechanisms | `RAI_GORILLA_T1.md:122-158`; freeze KILLED list | the H²/4π tail survives every deletion test; a finite-memory rescue must exhibit an eighth mechanism and survive the same battery |
| declared inputs (vertex, bath, state, scheme, limits, projector) → K | **DERIVED-GIVEN-INPUTS** ("forced by no principle") | ROOT-1 KERNEL-STANDARD, 42/42 | the u2 theorem ROOT-1 names and does not supply: the same IR kernel from ≥2 distinct microscopic completions — that would convert given-inputs to forced |
| K(t,t′) → stationary K(Δt) | **CONDITIONALLY DERIVED** (worldline scope on dS, D3a) and otherwise **not established, with the obstruction measured** | R = 0.516 on the frozen grid; local transport dead by lag 0.8/H₀; FRW-specific excess 0.17→0.54 | a proved stationary reduction in a declared representation (the named, untaken smearing instrument) |
| memory/correlations → geometry | **OPEN**, with one recorded definitional failure | no in-repo test; prior attempt: "1Space: UNDEFINED — all seven candidate definitions failed non-circularity" (`GRUT_PROGRAM_FREEZE.md:103-106`); metric never derived from deeper structure (ROOT-0) | a non-circular reconstruction of distance/causal structure from substrate correlations that does not consume the metric it outputs — none exists on record |
| memory → quantum structure | **DISDERIVED as tested** | interference-from-memory "rejected as an explanation of interference"; "no phase-carrying memory variable" (`REALITY_CHECK_03.md:84-99`); ℏ routes failed | the four named requirements for a carrier variable (carrier, locality/causality, phase capacity, decay law) — exhibit one or prove the class empty |
| substrate → matter | **OPEN / SILENT**, one derived minimality constraint | "the chain's matter link is SILENT"; R3-1/R3-2 REFUTED as stated; residue: persistent excitations need "SOME conserved structure bounding the accessible state space … NOT necessarily a bounded-below Hamiltonian (KdV)"; "stable pattern ≠ particle" | classify X's stable excitations against the SM's actual content — currently no instrument exists |
| substrate → gauge structure | **OPEN**; audited derivation routes **relocate** | RRP-02: SO(10) = type-local COMPRESSION "paid back at every other type"; compactification = RELOCATION; the gauge group is Φ-defining (specification input) | a gauge-structure derivation that survives the (II′) conversion audit — i.e., reduces net suppliedness; zero such exist across the audited record |
| decoherence (given partition + coupling) → classical suppression | **CONDITIONALLY DERIVED** | suppression, pointer stability, record robustness established *given the partition*; "classical ontology: NOT established" (`EC01_PILOT_HOSTILE_AUDIT.md`) | an in-house pointer-basis computation for a concrete system (none exists — BOOK III:551) |
| decoherence → outcomes / Born weights | **DISDERIVED (in class)** | "suppression only — no outcomes, no branch weights"; weights INHERITED (initial-state data); selection "requires an irreducible additional structure for this model class" (Experiment P) | the class-escape itself: name the additional structure and its price (GRW-type, Bohm-type, nonlinearity) — every audited option is POSTULATED / ADDITIONAL-INPUT / CONTESTED |
| the partition itself (U3) → everything above it | **EMPIRICAL INPUT (undeclared, load-bearing)** | subsystem structure "available-under-conditions, not canonical" (AQFT split property, intermediate type-I factor not unique); "a load-bearing input is undeclared" (ROOT-1:170-172); U3-REQUIRES-DEFINITION, graph isolate; CPR the one recorded genuine derivation (finite type I, existence measure-zero generically) | the deletion test the AQFT audit specifies: "remove every partition-valued object from the inputs; if the derivation still runs, it is a candidate" |
| substrate → observers | **OPEN — UNPOSED** | "never been POSED in the register"; the observer is "the name of the slot into which the framework's deepest undischarged input was moved"; CLPW "runs FROM a supplied observer and never derives one" (BOOK VIII) | define observer = persistent information-processing subsystem and run the same derive-or-price audit on it; no consciousness primitive is forced by anything on record |

**The graph's shape, read honestly:** every arrow that terminates in
structure we experience (geometry, quantum, matter, gauge, outcomes,
observers) is OPEN or DISDERIVED-as-tested; every arrow that is DERIVED is
either conditional on a background/limit or terminates in *constraints and
suppressions*, not in selections. The audited world is one in which
**structure is always cheaper than selection**: suppression, persistence,
cones, and consistency conditions come out of the mathematics; outcomes,
directions, partitions, constants, and content always go in.

## D. FREE INPUTS — what cannot currently be derived (the priced inventory)

At recorded tier: **ℏ** (irreducible; emergence FAILED) · **the Born
measure** (Bin-1; form derivable via Gleason given the lattice — the input
relocates upstream, "consumed-not-produced stands") · **outcome selection**
(NOT_DERIVED; class-impossible dynamically) · **the Past Hypothesis /
time-direction datum** (the one relative Z₂) · **the system/bath partition**
(undeclared, load-bearing) · **G and Λ** (underived in every audited
formulation) · **the SM gauge group + matter content** (specification input;
anomaly-consistency the only structural tie) · **the state and scheme
selections** (BD-analogue, order of limits, gauge, TT projector CHOSEN,
kernel Lorentz covariance +1, background time-translation flow +1) · **the
responsive-medium stance itself** (+1) · **the measured constants** (ρ_Λ, v,
M_Pl excluded from GRUT-specific content as data every theory must
reproduce).

## E. DISDERIVED STRUCTURES — what the program has ruled out (not softened)

The finite-memory / single-pole vacuum in its strongest form (dS forces
scale-free memory) · s = 3 (the actual kernel is s = 5) · memory as an
explanation of interference · every attempted ℏ-emergence route ·
dynamically generated Born weights within the tested class · irreducible
emergent influence under ANY linear dynamics (the broadened RRT-0 no-go;
escape only by nonlinearity) · μ = 4/3 · the economical evolving w(z) (not
earned) · the α→TT bridge (settled-negative) · G-STRONG (region-free
counterexamples; capped) · the conformalon double-duty unification · all
seven non-circular definitions of emergent space attempted ("1Space
UNDEFINED") · the "689 Hz parameter-free" falsifier · R3-1/R3-2 as stated
(discrete conserved sector labels are not necessary for stable excitations)
· local dS→FRW substitution rules over cosmological lags (this session) ·
the acoustic Cherenkov channel (EXTERNAL-RECORD; preserved per owner
instruction, primary uncommitted) · the rung3/rung7 adverse comparison as a
physical contradiction (unreachable: premises disjoint).

## F. OPEN DERIVATIONS — the smallest set of problems that must be solved

Ordered so that each unlocks the ones after it; every one is a calculation,
not a stance:

1. **The partition problem (U3's well-posed residue).** Exhibit one genuine
   derivation of a system/bath split from dynamics (the choice-of-slow-
   variables problem), or extend CPR's uniqueness-given-existence to the
   relevant class, or prove the class-impossibility. Everything from
   decoherence to the kernel consumes this input; it is the record's
   deepest undeclared dependency.
2. **The continuum leg.** Commit `u3_continuum_origin.py`, resolve
   t^(−d) vs t^(−d/2), and grade what actually survives of
   finite-substrate → continuum emergence — including which continuum
   structures are universal.
3. **The FRW state/KMS structure** (the transport verdict's three
   relocation items: state choice, temperature structure, proved stationary
   reduction). Required before any cosmological-sector claim about ladders,
   relaxation times, or low-ω response is even well-posed.
4. **The interference carrier.** Either exhibit a substrate variable
   satisfying the four recorded requirements (carrier, locality/causality
   structure, phase capacity, decay law) that is not quantum mechanics
   restated — or prove that the class of classical substrates cannot supply
   one, which would establish the missing-primitive claim at theorem grade.
5. **The selection structure.** Name the irreducible addition that produces
   outcomes (the class-escape), with its price paid openly (nonlinearity /
   signalling, collapse postulate, additional variables) — or record that
   X's ontology carries selection as a primitive, priced.
6. **The u2 two-completions theorem** (ROOT-1's named unlock): the same IR
   kernel from two distinct microscopic completions would convert the
   kernel from given-inputs to forced, and would simultaneously bear on
   what the bath is.
7. **U5/U6 KNOB 1** (the fixed-point RG of the reversible couplings): the
   one route whose failure condition is a uniqueness theorem
   ("only-one-class → responsiveness unique").

## G. MINIMUM CORE — the shortest candidate statement of GRUT as a theory of reality

Stated as an axiom-schema with its free slots visible, because the record
forces the slots more firmly than it forces any filling:

> **There exists a substrate X** — not necessarily local, not necessarily
> Lorentz-invariant, not necessarily tensor-factored, not necessarily
> finite-dimensional, and (if the tested emergence classes are to be
> nonempty) not closed-finite-linear — **whose effective description at
> accessible scales necessarily contains:**
> (i) a single universally coupled helicity-2 EH+Λ sector, with a named
> Weinberg–Witten exit if that sector is emergent;
> (ii) anomaly-consistent chiral matter;
> (iii) retarded, passive, KK-causal response organized by **two-time
> kernels K(x,t;x′,t′)**, whose stationary reductions exist exactly on
> states carrying the warranting symmetry;
> (iv) irreversibility only in open/thermodynamic limits, with its
> direction supplied by boundary data;
> **and which either derives or carries as explicitly priced inputs:** its
> subsystem decompositions, its state selections, its probability rule and
> outcome structure, its time-orientation datum, ℏ, G, Λ, and its
> gauge/matter specification.
>
> On the present record the priced list is irreducible: **every audited
> closure consumed at least one such input, and no audited framework —
> GRUT included — has ever eliminated one** (zero strict reductions in 19
> comparable pairs; supplied content is relocated or converted, never
> destroyed). GRUT becomes a theory of reality, rather than a constrained
> frame for one, on the day any single item of section F discharges a
> single item of section D.

**What this core is NOT:** it is not a claim that X exists as described, not
a derivation of any slot's filling, and not a rehabilitation of the retired
responsive-medium strongest form. It is the intersection of everything the
calculations force, written so that each remaining freedom is a named,
attackable problem rather than an ambient assumption.

---

## CLOSING HONESTY BLOCK

- The chain the charter starts from has **never been computed as one
  chain**; its links live in separate artifacts at separate grades, two of
  them uncommitted (EXTERNAL-RECORD). This document is the first place they
  are assembled, and the assembly itself is new work at synthesis grade —
  one round, in-house, single-author, unreviewed.
- The strongest genuinely new statement this reconstruction adds beyond its
  sources is the graph-shape observation (structure cheap, selection dear),
  and it is an induction over the audited record, not a theorem — exactly
  the grade of the freeze's second clause, and subject to the same one-sided
  apparatus caveat.
- Fenced routes (Λ_R, Matsubara, Π₀, U5) were not touched. No register
  field changed. The F-list is a menu for the owner, not an opened campaign.

---

## ADDENDUM 01 (2026-09-25) — PROVENANCE DISCHARGE + CHERENKOV RE-STATUS (directive-executed; governs over §0 rows 1/3 and the corresponding E-list entry)

Executed under `DIRECTIVE_TO_CLAUDE_CLOUD_01.md` (owner-relayed). The
adjudicator track `origin/adjudicator-track` (head `90218f5`; repair-set
`5f5395e`; seal `d2da3a5`) discharges two of §0's three provenance gaps:

- **Row 1 DISCHARGED:** `calc/u3_continuum_origin.py` +
  `calc/U3_CONTINUUM_ORIGIN_RESULT.json` (6/6) are now committed primaries
  on `adjudicator-track`. The t^(−d) vs t^(−d/2) inconsistency this
  document carried is **fixed at source** (stale docstring corrected; the
  body always derived −d/2).
- **Row 3 DISCHARGED AND PARTLY SUPERSEDED:** committed primaries
  `calc/u3_gravity_bath_spectral_match.py` + RESULT (8/9 — the one FAIL,
  `B3_discrete_box_kernel_matches_continuum_in_accessible_window`, is
  banked in the RESULT as a box-floor instrumentation limit and travels
  with any citation of the 8/9) and `calc/u3_resistive_graviton_coupling.py`
  + RESULT (v3, 20/20). **The Cherenkov-disderivation half of this row is
  SUPERSEDED**: see `CHERENKOV_RECORD_CORRECTION_01.md` — the disderivation
  was refuted post-charter (`U3_COUPLING_ADJUDICATION_03`).
- **Row 2 (ℏ-emergence attempt): remains EXTERNAL-RECORD** — no primary on
  `adjudicator-track` either.

**E-list re-status (supersedes the entry "the acoustic Cherenkov channel
(EXTERNAL-RECORD; preserved per owner instruction, primary uncommitted)"):**
the acoustic-coupling entry LEAVES the DISDERIVED list. New status:
**CONDITIONALLY DERIVED** — acoustic channel OPEN, J ~ ω⁷ (measured
ω^7.008; coefficient ratio 1.0005), kernel class t⁻⁸; conditions = the
ledgered imports (κ = 1/M_Pl, retained-sector structure, minimal-stress
postulate); annotated "derived within the minimal-stress class; class-4
gate unpassed"; citation pairing mandatory:
`calc/u3_resistive_graviton_coupling.py` v3 RESULT, 20/20,
`origin/adjudicator-track`. Fence acknowledgment: this is a
refutation-with-certificate under named owner authorization, not a
softening of a DISDERIVED entry. **What stays on the DISDERIVED/citable
list from the old record:** same-sign channel closure at all ω;
aligned-channel TT death (e_xx = 0); gapped-sector threshold emptiness
(J ≡ 0 below 2Ω).

Consequent touch to §A row A1/gravity context: "gravity-as-bath currently
only spectrally viable" weakens as a premise — the coupling arrow now has a
conditionally derived open channel with a measured exponent; the A-table's
constraint rows (helicity-2 containment, Weinberg–Witten exit) are
unaffected.
