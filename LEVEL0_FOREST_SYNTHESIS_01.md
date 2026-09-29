# LEVEL-0 FOREST SYNTHESIS 01 — access, distinguishability, equivalence classes, selection

**STATUS: SYNTHESIS / HYPOTHESIS GENERATION — NOT A NEW RESULT.**
- No computation was run. The work was four read-only record audits, plus the operator's own
  adjudication of what they found.
- Nothing here changes any label, ruling or deposit. It is a separate post-floor task and does
  not modify the floor (`L0_1_FLOOR_DEPOSIT_01.md`).
- **Authority:** owner direction of 2026-09-29 (`L0_1_FLOOR_O7_OWNER_RULING_01.md` §5).
- **Date:** 2026-09-29 · **Branch:** `master-w25bu9` · **State:** `CURRENT_STATE.json`.

**Binding posture (owner):**
- Test the cross-program hypotheses; do not assume them.
- The access/equivalence idea must **not** become the new thing we protect. Its first job is to
  explain the record more economically than competing readings. Its second job is to expose a
  falsifiable next dependency. **If it cannot do both, discard it.**
- Keep five kinds of statement separate: established results, theorem identities, scoped
  counterexamples, cross-program synthesis, and new hypotheses.
- No retroactive rescue. No renaming of GRUT.

## §0 Bottom line (read this first)

1. **H-PROJ is NOT SUPPORTED in its cross-program form, and is discarded as an explanation.**
   The hypothesis: *"many underdeterminations arise because the effective description is a
   projection; distinctions erased by the access map cannot be selected by dynamics in the
   projected description."*
   - Only two of ten campaigns SUPPORT it (P-5, GS-1), and both hold largely by construction.
   - Two are COUNTEREXAMPLES (Experiment P, GR2), and GR2 carries the program's four largest
     non-selections.
   - Three records show the *opposite* mechanism: distinctions dropped by a truncated
     description were **recovered** by dynamics (D-1 E2, P-3 κ₄, GS-1 Y–Δ).
   - The narrow core ("at a fixed declared access map, the physical content is the equivalence
     class") survives. But it is **already banked** (the D-1/P-2 ruling; P-5), and it is close
     to definitional.
   - H-PROJ therefore fails the owner's first job: it does not explain the record more
     economically than the plain reading below (§1.4).
2. **H-ADM survives as a description of the record, not as a discriminating claim about GRUT.**
   The hypothesis: *"GRUT derives admissible classes far more often than it selects members."*
   - 12 of 15 targets end admissible-but-unselected.
   - The three selections (partition, geometry, temporal order) each succeed **only relative to
     a supplied input.**
   - It is non-discriminating because several targets (ħ, spin, coupling, Born weights) are not
     selected by any known effective framework, and several "derived" admissible classes are
     borrowed-standard mathematics.
3. **What the audit actually exposes** is not a single projection mechanism. It is **five
   distinct causes of underdetermination (§1.4)**, plus **one shared supplied input: the access
   seed.**
   - GS-1's geometry reach, CA-1's carrier, and GR2's inherited "access supplied" premise all
     reduce to the seed (P-6).
   - That shared input is the concrete, falsifiable dependency. H-PROJ was not needed to find it.
4. **The GR2 / endogenous-access distinction is proved from the record (§3).**
   - Every GR2 fork held the recovered geometry fixed "by construction", took the access seed
     as supplied (from P-6), and used fixed states.
   - Across GR1, GR2 and CP1 there is no backreaction and no state-dependent access or
     geometry.
   - **The honest limit:** an endogenous-access experiment would address GR2 only through
     GR2's inherited premise. It **cannot** resolve GR2's four non-selections, which have a
     different cause (admissibility too weak).
5. **Leading candidate charter: EA-1, an endogenous-access / state-exclusion falsification fork
   (§5).**
   - It is leading because it addresses the shared seed dependency across P-5/P-6, GS-1/CA-1,
     GR2's premise and Level-0. By the owner's criterion it qualifies on three of four fully and
     on GR2 partially.
   - It has a clean death condition.
   - **One identity must be front-run:** in the linear/quadratic class, response geometry is
     state-independent by construction. A quadratic run can only be a control, never the
     attack.
6. **HARD STOP** for owner review. No new physics runs until then.

## §1 Audit of H-PROJ (the projection/equivalence-class hypothesis)

**The formal candidate (owner):**
- F_𝒳 : Ω → 𝓘_𝒳, with ω₁ ∼_𝒳 ω₂ ⟺ F_𝒳(ω₁) = F_𝒳(ω₂).
- The candidate physical object at a fixed interface is [ω]_𝒳.

**The tautology trap, stated first.**
- If 𝓘_𝒳 is taken to be "whatever description was used", H-PROJ absorbs every result. Any
  non-selection becomes an "erasure" after the fact.
- The owner already warned against this (`EQ1_S41_OWNER_RULING_01.md:38-39`: against "choosing
  observables that quotient away precisely the differences to be tested").
- So this audit fixes **𝒳 = the declared access map of each record** (sites, channels,
  observables, seed), before looking at outcomes. Under that reading H-PROJ has content, and
  that content can fail.

### §1.1 Per-campaign classification

**Legend for the cause column:**
- **proj:** a distinction erased by a fixed access map.
- **trunc:** a truncated description that dynamics later recovers.
- **adm:** admissibility constraints too weak, or no selection mechanism.
- **supp-X:** the access seed itself is supplied.
- **cons:** the dynamical class conserves the quantity.
- **supp:** another input is supplied.

| # | Campaign (records) | Class | Cause of its underdetermination | Why, and the strongest argument against the class |
|---|---|---|---|---|
| 1 | **D-1** (`DISCRIMINATOR_*`, `D1_P2_OWNER_RULING_01.md`) | CONSISTENT BUT NON-DISCRIMINATING | proj (E1) · trunc (E2) | E1's equivalence is by construction: W-B′ adds *decoupled* modes, and Feynman–Vernon makes the S-dynamics a function of (K,N). E2 is the reverse case: N, absent from K, is recovered by S-access. *Against:* D-1 is the origin of the banked statement "equivalence at fixed influence data"; one could call that SUPPORT. But it is support for a definition the ruling already adopted, not for the cross-program claim. |
| 2 | **P-3** (`P3_NC_LIFT_*`, `P3_P4_OWNER_RULING_01.md`) | CONFOUNDED | trunc | κ₄ was dropped by the description (K,N) and **recovered** by probe dynamics (coherence split 0.338). *Against:* κ₄ was never erased by the access map (the probe sees the full influence functional), so H-PROJ survives if 𝓘_𝒳 means "what access preserves". The result cannot discriminate between the two readings. Q5 restates D-1 and is not counted. |
| 3 | **P-4** (`P4_HIERARCHY_*`; accepted in `P5_ACCESS_CHARTER_01.md:4-12`) | CONSISTENT BUT NON-DISCRIMINATING | proj (by construction) · supp (ħ, realized point) | Interface-completeness holds by construction; the charter says so ("BY CONSTRUCTION"). **Record-quality note:** the descriptiveness attack is a hardcoded `check(True, …)` at `calc/p4_hierarchy.py:251`. No non-trivial matched-hierarchy pair was built, so the attack was **asserted, not tested.** The order-4 rung reuses P-3's pair, and full matching is P-3 Q5 (= D-1); only the order-6/8 rungs are new. The remainders P-4 names ("which hierarchy point reality realizes", ħ, the access structure) are **non-projection** underdeterminations. |
| 4 | **P-5** (`P5_ACCESS_*`; accepted in `P6_SEED_SELECTION_CHARTER_01.md:4-9`) | **SUPPORTS** (weakly) | proj | The split is "invisible forever under fixed access, and consequential exactly when access changes". Recovery comes from **changing F_𝒳** (the quench B → B + 0.4σ_x²), never from dynamics within 𝓘_𝒳. This is the one construction that directly exhibits the H-PROJ mechanism. *Against:* the hidden sector is dynamically decoupled by construction, so no alternative could have predicted otherwise. Where the quench sits (in Ω or in 𝒳) is a modelling choice. |
| 5 | **P-6** (`P6_SEED_SELECTION_*`; accepted in `G1_GEOMETRY_CHARTER_01.md:4-9`) | IRRELEVANT to the fixed-𝒳 mechanism; CONFOUNDS its "fixed interface" | supp-X | The main result is that **𝒳 itself is underdetermined**: the seed is supplied, minimal sufficient seeds are nonunique and order- or path-dependent, and closure is non-injective (L-B/E: identical closures, different physics, gap 0.287). H-PROJ presupposes a declared 𝒳, so it cannot explain this without regress. The L-C diagnostic (not promoted) says seed distinctions are physical only relative to the **state's reachable sector**. The equivalence class would then depend on the state, not on F_𝒳 alone. |
| 6 | **GS-1** (`GS1_GEOMETRY_*`; inherits G-2) | **SUPPORTS** (single-site leg; counted once with G-2) | proj · supp-X | "Determined exactly as far as access reaches." Under single-site access, 3600 non-isometric rotations give identical data. *Against:* in the Y–Δ leg, **dynamic data at the same sites recover what static data erase** (49.7 vs 2e-16). If access means "sites", that is a counterexample. H-PROJ survives only if 𝒳 specifies observable *channels*, which is the reading fixed above. |
| 7 | **CA-1** (`CA1_CARRIER_*`; accepted in `GS1_GEOMETRY_SELECTION_CHARTER_01.md:6-9`) | CONSISTENT BUT NON-DISCRIMINATING | supp-X · adm | P, M and T carry identical geometry because they are built on the same K ("close to an identity", verdict:70). The carrier's supplied status **reduces to P-6's seed** and is not counted separately. The classical carrier is cut by a constraint at a *different* interface (the ν cone). |
| 8 | **Experiment P** (TestingGRUT laboratory records: `program/EXPERIMENT_P_*`, `program/REALITY_CHECK_04_EXPERIMENT_P_ADJUDICATION.md`; not a chartered fork with an owner ruling) | **COUNTEREXAMPLE** (weak) | cons · supp | The weights are **not erased**: they are visible in the reduced state (p₀). Changing the partition (the access choice, Control E) changes nothing. Non-selection is a **theorem of the dynamical class**: branch-preserving unitaries conserve |α_i|² (hostile replication, DERIVED algebraic). *Against:* whether an outcome is "definite" is posed relative to a declared partition, so there is a projection flavour. But that is the textbook improper-mixture fact, independent of GRUT's access map. **Correction to the brief:** the record is narrower than "not identifiable from the available reduced structure". It says decoherence observables alone do not determine weights; the full reduced state does contain them (`ADJUDICATION.md:138-142`). |
| 9 | **GR2** (`GR1_*`, `CP1_*`, `GR2A`–`GR2D2`, `GR2_L6`, `GR2_CAMPAIGN_SYNTHESIS_01`, rulings) | **COUNTEREXAMPLE** (coupling, spin, reach); the cone is CONSISTENT BUT NON-DISCRIMINATING | adm | For coupling, spin and reach, the unselected distinctions are **visible** in the declared description: class labels measured, and non-universality "detected… not a selection principle" (`GR2C_OWNER_RULING_01.md:23-24`). What fails is selection by constraints that are too weak (convex positivity; a rank-1 PSD identity). Nothing is erased. GR2 also contained no selection dynamics; it was static admissibility testing. For the cone, the frequency battery is exactly blind under ω(λq), a genuine projection erasure; but front speeds are measurable in the same substrate. *Against:* take the "projected description" to be the earned battery and every GR2 non-selection becomes an erasure. That is the tautology trap. |
| 10 | **L0 floor** (`L0_1_FLOOR_DEPOSIT_01.md`) | CONSISTENT BUT NON-DISCRIMINATING (main findings IRRELEVANT) | supp (generator, S-5) · proj (two identity-grade items) | Two floor items are projection-type, both identities of a declared interface: O-2's P-1 (state-norm growth invisible at the retained site) and S-1 (primitive vs derived noise is equivalent at second order). The floor's main result (properties factor across distinct boundaries; O-7) is about property boundaries, not access. The generator is supplied (S-5). |

### §1.2 Independence accounting (no double counting)

| Reused finding | Origin | Also appears in | Counted once, as |
|---|---|---|---|
| Equivalence at fixed influence data | D-1 | P-3 Q5, P-4 full-matching control, P-5 citation | D-1 |
| Order-4 κ₄ mismatch | P-3 | P-4 order-4 rung | P-3 |
| Single-site geometric collapse | G-2 | GS-1 L-P, CA-1, GR2-a/b/c/d | GS-1 (with G-2) |
| "The access seed is supplied" | P-6 (from P-5) | GS-1, CA-1, GR2-b, GR2-c, the program synthesis | P-6 |
| The ħ floor located, not generated | P-2 | P-3, P-4 | P-2 |
| The Born-weight wall | Experiment P **and** NO_GO §7 | — | **two independent routes** (`program/EC01_PILOT_REPORT.md:79`), counted separately |
| EQ-1 (Sel-4; truncation-relative underdetermination) | EQ-1 | — | separate from D-1; not in the ten |

### §1.3 Tally, after independence

| Class | Campaigns |
|---|---|
| SUPPORTS | P-5, GS-1 (both largely by construction) |
| CONSISTENT BUT NON-DISCRIMINATING | D-1, P-4, CA-1, L0 floor |
| CONFOUNDED | P-3 |
| IRRELEVANT (and confounding) | P-6 |
| COUNTEREXAMPLE | Experiment P, GR2 |

### §1.4 The competing reading, and why it is more economical

Read without H-PROJ, the record's underdeterminations sort into **five mechanically distinct
causes**:

| Cause | What it is | Records | Relation to H-PROJ |
|---|---|---|---|
| **C1 proj** | Erasure by a fixed access map | P-5 L-D; GS-1 single-site; O-2 P-1; S-1; D-1 E1 | the H-PROJ mechanism; mostly by construction |
| **C2 trunc** | A truncated description, then **recovered** by dynamics or a richer channel | D-1 E2 (N); P-3 (κ₄); P-4 ladder; GS-1 Y–Δ; EQ-1 ("underdetermined at any finite order … not in principle") | the **opposite** of H-PROJ |
| **C3 adm** | Admissibility too weak; no selection mechanism in the class | GR2 coupling/spin/reach/cone; CA-1 (F survives); GS-1 LocPos; P-1 X3; Sel-4 | not an erasure |
| **C4 supp** | Inputs never derived | the access seed (P-6; GS-1 reach and CA-1 carrier reduce to it); ħ (P-2); the generator (S-5); C_cons (CC-1); a common c (U-1/TT-1) | the seed is *upstream* of any 𝒳, so H-PROJ cannot contain it |
| **C5 cons** | The dynamical class conserves the quantity | Born weights (Experiment P theorem) | not an erasure |

This reading uses **no new principle.** It explains every row of §1.1, including the
counterexamples and the recoveries that H-PROJ must explain away.

**Verdict on H-PROJ:**
- **Discarded as a cross-program explanation.**
- Its narrow core (C1) stays in the record where it already was: the D-1/P-2 ruling and P-5.
- It is **not** promoted to a principle, and no claim is made that access, information or
  equivalence classes are fundamental.

## §2 Admissibility vs selection (H-ADM)

**Column key:**
- **Earned:** structure already earned.
- **Remaining:** equivalence or degeneracy still open.
- **Discriminator:** what was attempted.
- **Result:** whether the discriminator succeeded or failed.
- **Needed:** the additional information that would be required.
- **Info status:** derived / supplied / empirical / unknown / unformulable.

| Target | Earned | Remaining | Discriminator | Result | Needed | Info status |
|---|---|---|---|---|---|---|
| Microscopic realization | Equivalence at fixed (K,N) / full hierarchy (D-1, P-4) | Non-isomorphic realizations | S-access metrics, probe | Failed at fixed data (by construction); N discriminated (E2) | A different access map, or a framework constraining (K,N) | unknown |
| Subsystem / partition | Trichotomy (P-1): emergent / representational / unselected | Tie-orbits; nothing selects generic worlds; criteria disagree | C1–C4 intrinsic criteria | **Succeeded in the structured regime (X2)**; failed in X1, X3 | An anchor or a criterion choice | derived (structured) / supplied (generic) |
| Access seed | Canonical closure given a seed; blocks of reducible dynamics (P-5, P-6) | Nonunique, path-dependent, degenerate orbits; closure non-injective | Minimality, causal graph + conservation, symmetry, sufficiency | Failed (except block level) | The seed | **supplied**; derivation from the state **unformulable-yet** |
| Geometry | Selected up to relabeling under full access; dynamic data beat static (GS-1) | Non-isometric family under single-site access; topology horizon | Site-resolved, ω² hierarchy, LocPos | **Succeeded under full / boundary-dynamic access**; failed single-site; LocPos narrows only | Access reach | supplied (reduces to the seed) |
| Carrier | Classical carrier cut by the ν cone (CA-1) | P, M, T equivalent; F not excluded | Cone, locality, hop recovery | Partial | Probe-seed coincidence | supplied (reduces to the seed) |
| Response / kernel | (K,N) as the Gaussian label; cone 𝔠_Gauss (P-2, borrowed-standard realizability) | Which kernel reality realizes | Noise, probe | Discriminates between kernels; does not select | Microscopic data | unknown / empirical |
| Full influence hierarchy | In-class interface (P-4) | Which hierarchy point is realized per sector | Ladder; finite matching | Ladder succeeds; finite matching never certifies; realized point unselected | Beyond the class | unknown |
| ħ scale | The floor ν ≥ ħJ/2 **located** (P-2) | Any floor height | Register attempt, P-2 | Failed: "located, not generated" | The value of ħ | supplied / empirical |
| Outcome | Decoherence derived, in class (Experiment P) | Global superposition | Controls B, F, G; E&C-BORN R5–R8 | Failed | A selection or collapse rule | supplied / unknown |
| Born weights | Weight-inheritance theorem | Any \|α\|² with the same decoherence observables | C, H (narrowed), M01–M09 | Failed (inherited) | A probability measure | supplied / imported (NO_GO §7 BORROWED) |
| Coupling | 5-channel family admissible (GR2-a) | Classes 0/4/8/12; the +4 plane | Locality, cone, geometry | Failed | C_cons | supplied (CC-1) |
| Spin | All six representations admissible (GR2-b) | {scalar, vector, spin-2} | Positivity, access, geometry, locality | Failed | Universal attraction, light bending | empirical (firewalled) |
| Universal reach | Joint cone PSD for any g; non-universality observable (GR2-c) | 14 non-universal assignments | J, E, G, O legs | Failed | Gauge structure + exchange membership | supplied (U-1) / empirical |
| Causal cone | Fronts, supports, exchange composition (GR2-d/d2) | 7 + 1 different-cone systems | N, Q, X, K, M legs | Failed (the quantum leg is thin) | A common c | supplied (U-1/TT-1) / empirical |
| Temporal order | Derived order under strict-Lyapunov structure; recurrence obstructs (O-5) | Orientation (the generator's sign); conservative classes (O-6) | Lyapunov, Conley, lag distinguishability | **Succeeded in the dissipative classes, given the generator**; failed strict in the conservative split | The generator | **supplied** (S-5) |

**Tally:** 15 targets.
- An admissible class is earned in 15 of 15.
- A member is selected in **3** (partition, geometry, temporal order), and each selection is
  **relative to a supplied input**: the anchoring structure, the access reach, the generator.
- **No target has been selected without a supplied input.**

**Verdict on H-ADM: SURVIVES as a description of the record. It is NOT a discriminating finding
about GRUT.**
- (a) Several targets (ħ, spin, coupling, Born weights) are unselected in every known effective
  framework, so failing to select them is not specific to GRUT.
- (b) Several "derived" admissible classes are borrowed-standard mathematics: Gaussian
  realizability, bicommutant closure, improper mixtures.
- (c) The sharp form that carries information is narrower: **every selection GRUT achieved was
  conditional on a supplied input, and the most frequently inherited supplied input is the
  access seed.**

## §3 The GR2 / endogenous-access distinction, proved from the record

**The owner's requirement:** GR2 held the relevant interface architecture fixed while asking
whether influence structure selected gravitational properties. The candidate route asks instead
whether localized state changes modify the relational/access structure from which geometry is
reconstructed.

**What GR2 held fixed (verbatim from its own charters):**
- **Geometry.** "geometry consumed ONLY as the G-2-recovered substrate"
  (`GR1_GRAVITY_CHARTER_01.md:27-28`). The same holds throughout:
  - "recovered geometry is member-blind **by construction**" (`GR2A_COUPLING_CHARTER_01.md:130-132`);
  - "probe-blind by construction" (`GR2B_PROBE_CHARTER_01.md:94-95`);
  - "the recovered hop geometry is blind" (`GR2C_REACH_CHARTER_01.md:126-129`);
  - "the interaction graphs of H_A and H_B are equal" (`GR2D_CONE_CHARTER_01.md:154-155`).
- **Access.** P-6's "the seed is a supplied input" is "cited, not re-adjudicated"
  (`GR2B_PROBE_CHARTER_01.md:76-77`) and "cited, not re-run" (`GR2C_REACH_CHARTER_01.md:164-165`).
  GR2-b's access leg varied seeds only to show that every seed closes to sp(6)
  (`GR2B_PROBE_VERDICT_01.md:40-45`).
- **States.** Fixed ground states, or a single impulse; probe coupling small (h = 0.05).
- **No state-dependent structure anywhere.** Searches for backreaction, state-dependent,
  endogenous, exclusion, self-consistent and metric response across the GR1, GR2 and CP1 files
  return **no hits**. The nearest item is CP-1's L-M leg, and that is a *supplied* external
  metric perturbation, i.e. a probe.

**The owner's prior recorded distinction** (`STATE_EXCLUSION_DIRECTION_01.md:15-29`): GR2 is "a
selection question over supplied candidates"; the state-exclusion route is "a production
question".

**Proved, with three caveats:**
1. The fixing was by construction and inheritance, not a deliberate control. What is proved is
   that GR2 **never let access or geometry respond to state**, not that it tested and excluded
   such a response.
2. The access seed was *supplied* in GR2, not held at a single value (GR2-b varied it for the
   closure check).
3. **Consequence for scope:** an endogenous-access result could replace GR2's *inherited
   premise* (supplied access). It **cannot** reopen or resolve GR2's four non-selections, whose
   cause is C3 (admissibility too weak), not C4. The route stays inside the owner's rule that
   GR2 is not relitigated. The direction record's failure state D4(iv) ("the route is GR2 in
   disguise and closes") stays in force.

## §4 Reversal / chiasm diagnostic (not evaluated; methodological note only)

- **Status unchanged:** pre-registered (`L0_STRUCTURAL_DIAGNOSTIC_REVERSAL_01.md`), not
  evaluated, **neither supported nor refuted.**
- The floor is acyclic because deletion instruments cannot create a property → ingredient edge
  (§4 there).
- **The methodological implication only:** a constructive endogenous-access experiment could in
  principle produce an edge of the form *state/property → access/geometry ingredient*. That is
  the kind of edge the diagnostic requires. So the next architecture may need to be
  **constructive** rather than another deletion sweep.
- **This is not evidence that a cycle exists.** If EA-1 (§5) produced such an edge, the
  diagnostic would still be evaluated under its own frozen criteria, and nothing here
  pre-judges it.

## §5 Candidate successor charters, ranked by dependency (not by preference)

**Dependency rule:** an item ranks above another only if the other needs its output.

### Tier 0 — prerequisites (non-computational; blocks everything in Tier 1's EA-1)

**EA-0: the endogenous-access formulation document.** It settles, before any charter, the
design obligations already recorded in `STATE_EXCLUSION_DIRECTION_01.md` §4 (D1–D4), restated
in access terms:

- **(i) A mechanical definition of state-dependent access,** 𝒳(ρ): a map from a declared state
  to an access/relational structure, computed **without a supplied seed.**
  - Candidates already on the record: P-6's closure cl(S;H) restricted to the **reachable
    sector of ρ** (the L-C diagnostic, never promoted); and P-1's functional 𝔖[𝒜,𝒞,ρ] (never
    tested by varying ρ).
  - Until one is fixed, EA-1 is UNFORMULABLE-YET.
- **(ii) The recovered relational geometry as a function of ρ,** G_𝒳(ρ), using the G-2/GS-1
  machinery with the access reach set by (i), not supplied.
- **(iii) Identities front-run.**
  - In the **quadratic class**, commutators of the canonical fields are c-numbers. Response
    (susceptibility) data, and any geometry recovered from them, are therefore
    **state-independent by identity.**
  - Correlation-derived data *can* vary with the state (e.g. a Fock excitation). So the charter
    must declare which channel reconstructs G_𝒳, and must not let a state-dependent correlation
    readout pose as state-dependent access.
  - A quadratic-class member read through its response channel can only be the **negative
    control** (it must show no change), never the attack.
  - The attack needs a class where occupancy constrains available states. Candidates:
    exclusion statistics (hard-core/fermionic occupancy), or a nonlinear substrate.
  - This must be shown formally before a charter, so that no "result" is a restated identity.
- **(iv) No-smuggling** (carried whole from D3): no member of GR2's supplied quadruple
  {coupling, spin, reach, cone} may enter; no probe may be re-supplied (D2); the empirical
  firewall holds.
- **(v) Failure states named first** (from D4), including D4(iv), "GR2 in disguise → closes".

### Tier 1 — the leading candidate (depends on EA-0)

**EA-1: the endogenous-access / state-exclusion falsification fork.** In a declared class
beyond the quadratic identity: does changing a localized state alter the recoverable
access/relational structure G_𝒳(ρ), other than through externally supplied coupling structure?

- **Clean death condition (fixed in advance):** *changing a localized state does not alter the
  recoverable access/relational geometry except through externally supplied coupling structure*
  → the route is **CLOSED at the tested scope.**
- **Further death states:**
  - (a) any change found is fully accounted for by the ordinary state-dependence of a supplied
    Hamiltonian term;
  - (b) the change reproduces the influence-kernel structure exactly (D4(iv));
  - (c) the change exists but does not compose across sources (D4(i)). This one is only
    reachable later, in Tier 2.
- **Not allowed:** an outcome whose only possible reading is "interesting". Every branch of the
  frozen battery must map to CLOSED, CLASS-SPLIT or SURVIVES-TO-TIER-2.
- **Why it leads, by the owner's criterion** (it must address a shared unresolved dependency
  across P-5/P-6, GS-1/CA-1, GR2 and Level-0):

| Record | Does EA-1 address its dependency? |
|---|---|
| P-5 / P-6 | **Yes.** The seed is exactly the supplied input under test. |
| GS-1 / CA-1 | **Yes.** Geometry reach and carrier both reduce to the seed (§1.2). |
| Level-0 | **Yes.** It is the first constructive fork after a floor whose instruments could not create a property → ingredient edge (§4). It also inherits L0-1b's result that locality is necessary for geometry, which bounds where the relational distance in (ii) can come from. |
| GR2 | **Partially.** Only GR2's inherited "access supplied" premise. **Not** its four non-selections (§3, caveat 3). |

  So EA-1 qualifies on three of four fully and on GR2 partially. **The owner decides whether
  "partially" meets the criterion.**

### Tier 1, independent — lower shared dependency (not ranked against EA-1, which none of them need)

- **S-5**, derive the generator. It addresses O-5's supplied generator and temporal order (§2).
  Currently has no formulation route on the record.
- **S-1 / S-2**, primitive vs derived noise; the hard D-DET. Local to the floor.
- **S-3**, the crossed generator → correlation cell. It would separate the O-1/O-4 confound.
- **S-6**, the coarse-grained arrow. Local to O-6.
- **S-7 / S-8**, local follow-ups, explicitly **not** the priority front (O-7 ruling).
- **Housekeeping, record quality, not physics:** P-4's descriptiveness attack was asserted by a
  hardcoded `check(True, …)` (`calc/p4_hierarchy.py:251`) rather than tested. Its accepted
  standing ("NULL-AS-NEW-PRINCIPLE", "CANDIDATE interface characterization") does not rest on
  it, but the verdict text reads as if a test ran. **The owner may wish** to append a correction
  note (no re-run, no status change).

### Tier 2 — only if EA-1 SURVIVES (depends on EA-1)

- **EA-2:** composition/additivity of the access deficit across sources, and its fall-off with
  relational distance (the direction record's D5(b)).
- **EA-3:** geometric representability, and a probe-free response of *other* excitations to its
  gradients (D5(c), D2). This is where a property → ingredient edge could first appear, to be
  judged by the reversal diagnostic's own frozen criteria.

## §6 What this document does not claim

- It does not claim that access, information, distinguishability or equivalence classes are
  fundamental.
- It does not rename GRUT.
- It does not promote H-PROJ: that is discarded as an explanation. Its core stays where it was
  banked.
- It does not upgrade H-ADM beyond a description.
- It does not relitigate GR2. It does not modify the floor.

**The strongest permissible working interpretation (owner's wording, which the audit leaves
intact):**

> The current record repeatedly places the unresolved information at interfaces of access,
> distinguishability, and selection, suggesting that the next Level-0 attack should target
> whether those interfaces are themselves derivable or dynamical.

**The audit's refinement of that sentence:** the unresolved information sits at **five
distinct kinds of interface failure** (§1.4), not one. The single interface that recurs as a
*shared supplied input* is the **access seed**. That is why EA-1 is the leading candidate, and
not because the projection story is true.

## §7 Sources

Four read-only audits (subagents) of the records named in §1.1, each instructed to refute its own
classification.

**Operator corrections applied to the audits:**
- P-4 **is** owner-accepted. The acceptance is recorded in `P5_ACCESS_CHARTER_01.md:4-12`; one
  audit reported "not found".
- The Experiment P paraphrase was narrowed to what its record states.

**HARD STOP** for owner review before any new physics run.
