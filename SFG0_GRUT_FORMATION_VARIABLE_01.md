# SFG-0 — GRUT FORMATION-VARIABLE AUDIT (audit only; no new physics run)

**STATUS: AUDIT COMPLETE.**
- §§0–3 were pre-registered at `0d8aafd` and are unchanged.
- §4 (the audit) and §5 (proposed mechanical outcome: **CLASS-SPLIT**, heavily qualified; see §5)
  have been added.
- Awaiting owner ruling. **HARD STOP.**
- **Authority:** `SF1_OWNER_RULING_02.md` §9 (Issue #2 comment `5903593151`).
- **Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

**Disclosure.** While drafting these definitions, the auditor already held one preliminary
expectation: the U(1) number of the complex boson/fermion lifts may play the SF-1 role, but it
belongs to a *supplied* lift. The tier rule in §2 is written so that this expectation cannot decide
the outcome by wording. Wherever a candidate sits, its tier must be reported.

## §0 Question (verbatim, ruling §9)

> Does the earned/current GRUT substrate contain a conserved, topological, boundary, occupancy,
> realization, or other persistent sector variable Q such that one unchanged GRUT-relevant parent
> can be restricted to distinct Q-scalings and thereby yield inequivalent effective-law classes?

It must satisfy the SF-1 structure. **No new variable may be invented.** A Q counts only if it
already exists in a declared record: named there, or an exact conserved quantity or symmetry
charge of a declared generator.

## §1 Carried definitions

- **SF-0 §§1–3 unchanged:**
  - 𝓔-lin / 𝓔-sector / 𝓔-RG, declared per class before its sectors are examined;
  - the invariants I-z … I-sym;
  - the quotient ≃;
  - "a value difference inside one class is NOT law-level".
- **R-F = (b):** under 𝓔-sector, invariants are read from the excitation/response structure of the
  sector-restricted generator about the sector's persistent/reference state. Reading (a) is not
  used. Per `SF0_CORRECTIONS_01.md` SC-1, linearity of the equations of motion does not by itself
  imply STATE-NOT-LAW.
- **SF-1 structural template:**
  - a fixed parent (same generator, couplings, statistics, BC and readout);
  - Q is conserved/boundary/state data, not a generator parameter;
  - the sectors are exact and persistent;
  - one common retained observable and one common coarse-graining;
  - a declared thermodynamic/IR sequence if an IR exponent is claimed.
- **The six questions (ruling §9):**
  - **G1** Is Q a state/boundary/conserved datum, not a generator parameter?
  - **G2** Is the parent unchanged across Q?
  - **G3** Are the sectors exact/persistent?
  - **G4** Is there one common retained observable/coarse-graining?
  - **G5** Does Q alter a structural IR invariant, not only a value?
  - **G6** Is the change already known, formulable, or absent?
- **Scope of G4 (declared now):** the retained observable must be one **already declared** for that
  class (linear or quadratic). Adopting an undeclared observable to manufacture a difference counts
  as inventing, and is labelled SECTOR-SMUGGLED (readout). G6 must say whether the relevant declared
  observable is linear (SC-1: sector-blind) or quadratic.

## §2 Tiers (declared before inspection; every candidate is reported with its tier)

| Tier | Contents | Why separate |
|---|---|---|
| **E: earned core** | The earned classical substrate (EA-0: deterministic ẋ = −Kx on the declared site net) and its record classes 𝒞₁ (Hurwitz-linear), 𝒞₂ (L0-1c convex gradient) and 𝒞₃ (OU); K, pin and couplings of L0-1a/b/c | Owner: "earned/current GRUT substrate" |
| **C: declared conservative/quantum classes** | O-6 𝒦_N conservative chain; FS-1 harmonic ring and its conserved tower; P-6 spin models; CA-1 carriers on the ring K | Declared GRUT-relevant parents that are not the earned dissipative core |
| **L: supplied lifts** | Lift-selection survivors (cotangent, Sz.-Nagy, complex boson, complex fermion) and the representational lifts (Koopman/KvN, Liouville) | IRREDUCIBLE/SUPPLIED (post-floor). Any Q they carry is conditional on a supplied lift. |
| **X: other declared records** | U3 (realization dimension, continuum modes); P-1 relational partitions; access seeds (EA-0 / bridge); G-2 / geometry carriers; any topological/winding labels in the repo | Must be screened; may be parameters in disguise |

## §3 Candidate labels and mechanical outcome rule (frozen before inspection)

**Per-candidate label:**
- **CLEAN:** G1–G4 are yes, and G5 is either
  - already known different on record, or
  - formulable, meaning a declared thermodynamic/IR sequence exists or is already in the record,
    and no identity forces the invariants to coincide.
- **STATE-NOT-LAW:** G1–G4 are yes, and an identity or record result forces every structural
  invariant to coincide across Q.
- **SECTOR-SMUGGLED:** G1 or G2 fails, meaning Q is really a parameter (generator, substrate
  dimension, coupling, access declaration, lift) or needs an undeclared readout.
- **NOT-PERSISTENT:** G3 fails.
- **UNFORMULABLE:** G4 fails, meaning no common map exists.

**Gate outcome (first matching step decides):**
1. **GRUT-CANDIDATE-FOUND** if some Tier-E candidate is CLEAN.
2. **CLASS-SPLIT** if no Tier-E candidate is CLEAN, but some Tier C, L or X candidate is CLEAN,
   **and** Tier E is shown (identity/record grade) to have no CLEAN candidate. The label must name
   the tier(s) that host the candidate and every conditionality (for example "conditional on the
   supplied complex-fermion lift").
3. **STATE-NOT-LAW** if no candidate is CLEAN, but at least one candidate is persistent-sector and
   STATE-NOT-LAW.
4. **SECTOR-SMUGGLED** if no candidate is CLEAN or STATE-NOT-LAW, and some apparent sector needs a
   parameter/generator change.
5. **NO-CANDIDATE-IN-EARNED-CORE** if no persistent sector variable of any kind is found.
6. **UNFORMULABLE** if no common structural map can be stated for any candidate.

**Tie note:** if a CLEAN candidate exists in Tier C, L or X but Tier-E absence is not shown, the
outcome is **not** CLASS-SPLIT. It is reported as "GRUT-CANDIDATE-FOUND (non-E tier; Tier-E open)"
for owner ruling. The rule does not default either way.

**Fences:**
- No new physics run and no new variable.
- G5 is answered from identities or the record. A "formulable" G5 is **not** a claimed result.
- No SF-2, no S-5, no cosmology.

## §4 Audit

**Method.**
- Two independent read-only audits: Tier E+C, and Tier L+X.
- No computation was run on any declared member.
- **[AA]** marks auditor-derived identities. These are standard mathematics built on record
  theorems, but they are not themselves record claims.
- The load-bearing citations were spot-checked:
  - `calc/feasibility/bridge_verify/s3_lifts.py:7-10`;
  - `L0_1G_CHARTER_01.md:81-93`;
  - `CA1_CARRIER_CHARTER_01.md:51`.

### §4.1 Tier E: earned dissipative core (no CLEAN candidate; absence shown)

- **Substrate and readout:**
  - The substrate is classical deterministic ẋ = −Kx, together with the L0-1c gradient flow
    (`EA0_OWNER_RULING_02.md`; `L0_1F_DORD_THEOREM_01.md:42-59`).
  - The retained observable is **linear**: x₁, with kernel e₁ᵀe^{−Kτ}e₁
    (`L0_ACCESS_RANKDROP_THEOREM_01.md:29`). x₁² appears there only as an unearned readout.
- **Absence identity [AA]:**
  - **𝒞₁:** x(t) → 0 for every x₀. So any continuous first integral is constant, and {0} is the
    only compact invariant set.
  - **𝒞₂:** strictly convex, radially unbounded, with a strict Lyapunov function, so there is a
    unique fixed point.
  - **𝒞₃:** Hurwitz OU has a unique stationary law.

  The earned core therefore has **no nontrivial conserved quantity and one persistent state.**
- **Record corroboration:**
  - SC-2 (`SF0_CORRECTIONS_01.md`);
  - bridge ruling 02: direct classical branch TRIVIAL/IDENTITY;
  - RANK-CONSTANT at the earned output.

| Candidate | Label | Why |
|---|---|---|
| 𝒞₁ / 𝒞₂ / 𝒞₃ as declared | STATE-NOT-LAW (single sector) | There is no persistent Q |
| Spectral/Krylov invariant subspaces, singular orbit labels | NOT-PERSISTENT | Every sector shares the attractor 0. The readout is linear, so the response is a c-number (SC-1). The gap is ≥ pin everywhere. |
| pin, springs, β, epochs, T_i, end conditions | SECTOR-SMUGGLED | They are generator parameters |
| Retained site / probe e₁ | SECTOR-SMUGGLED | It is an access declaration |
| Initial data x₀ | NOT-PERSISTENT | It decays to 0 |
| L0-1a pin = 0 member (Σxᵢ conserved) | STATE-NOT-LAW | Shift-symmetry copies with a linear readout. It is also outside 𝒞₁ by name. |

### §4.2 Tier C: declared conservative/quantum classes

| Candidate | Q (record status) | Readout (declared) | Sequence | Label |
|---|---|---|---|---|
| **CA-1 F** free fermions on ring K | N_F, exactly conserved | quadratic density (T = 0 Lindhard; `RS1_RETAINED_SECTOR_CHARTER_01.md:50`; `calc/rs1_retained.py:59-71`) | SF-1 sequences | **CLEAN (already known; it is the SF-1 parent).** **Tier contested:** the CA-1 charter calls F a "non-carrier contrast" (`CA1_CARRIER_CHARTER_01.md:51`), and fermionic statistics is the supplied complex-fermion lift. |
| O-6 𝒦_N energy shells | H | quadratic J = g⟨p₂q₁⟩, S₁ (`L0_1G_CHARTER_01.md:81-93`) | N ∈ {23, 47, 95} | STATE-NOT-LAW (amplitude rescaling, §3(3)) |
| O-6 full tori | actions I_k | same | same | STATE-NOT-LAW (isochrony [AA]: same support {ω_k ± ω_l}, only the weights differ) |
| O-6 sub-torus occupancy S = {k : I_k > 0} | derived from the exact actions | same (site-local, no momentum resolution) | parent sequence yes; **S-family undeclared** | **CONTESTED: formulable at most.** No identity forcing equality was found. Against it: S is non-generic and a small excitation restores full support; no sector family is declared; the declared states are Gibbs ensembles, not tori; the site-local readout cannot give I-z. |
| FS-1 tower (H, Q_n, P_n) | named | conserved O (zero response), q = 0 quadratic, linear | **none** (N = 20) | STATE-NOT-LAW (q = 0 pair-channel identity [AA]: support {2ω_k}, weight > 0 in every sector). A q ≠ 0 density would be SECTOR-SMUGGLED (readout). |
| FS-1 as recorded (H + hO) | coupling | — | — | SECTOR-SMUGGLED |
| P-6 parity blocks | P = Πσ_z | probe coherence | none | STATE-NOT-LAW (finite; SC-2 qualifier) |
| CA-1 P, M | no number declared; single-mode linear carriers | linear | N = 256/64 | STATE-NOT-LAW. A second-quantized N would be SECTOR-SMUGGLED (lift), and even then the **boson condensation identity [AA]** holds: every N-sector ground state is (b†_{k₀})^N\|0⟩, so the support is ε(k₀+q) − ε(k₀) for all N. |
| CA-1 T; the CA-1 set as a whole | — | — | — | SECTOR-SMUGGLED |
| CA-1 D | Σn (zero mode) | linear | — | STATE-NOT-LAW (shift copies) |

### §4.3 Tier L: supplied lifts (all conditional on the named supplied lift)

**Record facts:**
- The only explicit lifted generator is **quasi-free Lindblad loss with no Hamiltonian**
  (`calc/feasibility/bridge_verify/s3_lifts.py:7-10`: "loss never raises number"). Covariance
  evolves as C(t) = TC₀T†, and ⟨dΓ(P)⟩ is strictly decreasing.
- **[AA]** d⟨N⟩/dt = −2⟨dΓ(K_b)⟩ < 0 off the vacuum. So N is **not conserved**, and the unique
  stationary state is the Fock vacuum. That is the analogue of the earned δ₀.
- The declared lift readouts are linear or c-number. The one exception is ⟨n₁⟩ = k² under a
  one-particle probe.
- N = 23 is fixed, with no thermodynamic sequence.
- K_b is an **open**, pinned chain.
- V-7: particle number "need[s] complexification", which is supplied structure.

| Lift | Q | Label |
|---|---|---|
| Cotangent (H = pᵀf) | the actions x̃_k p̃_k [AA]; non-compact | STATE-NOT-LAW. Record identity: the x-projection commutes with the flow, so the linear readout is sector-blind. |
| Sz.-Nagy dilation | none (one-particle) | STATE-NOT-LAW. Bath preparation used as Q would be SECTOR-SMUGGLED (preparation). |
| Complex boson | N (named, LS-9) | **NOT-PERSISTENT** (the Lindblad loss does not conserve N). Under a non-record conservative reading it would still be STATE-NOT-LAW, by the condensation identity. |
| Complex fermion, declared CP/Lindblad reading | N | **NOT-PERSISTENT** |
| Complex fermion, e^{−t·dΓ(K_b)} as a Fock contraction [AA] | N (commutes) | Not a declared state dynamics. At finite N = 23 with no sequence it is at most STATE-NOT-LAW. Adopting a Hamiltonian reading, an N → ∞ sequence or a ρ_q readout would each be SECTOR-SMUGGLED. **This is the only lift where an SF-1-type contrast is conceivable, and it needs three non-record ingredients.** |
| Koopman / KvN / Liouville (representational) | none persistent | STATE-NOT-LAW (single sector: δ₀) |

### §4.4 Tier X: other declared records

| Candidate | Label | Why |
|---|---|---|
| U3 realization dimension N; continuum d | SECTOR-SMUGGLED | "N is a free structural input". d selects a different lattice. |
| U3 S4 double well | STATE-NOT-LAW | Z₂ copy (carried from SF-0) |
| P-1 relational partitions | SECTOR-SMUGGLED | A readout choice, or three different V |
| Access seeds (EA-0 / P-6 / bridge) | SECTOR-SMUGGLED | They are access declarations. EA-0 C-6/Γ(ρ) stays UNFORMULABLE at earned scope. |
| G-2 winding (C40 vs C80); GS-1 prism vs Möbius | SECTOR-SMUGGLED | Different graphs |
| Flux / twisted BC | SECTOR-SMUGGLED | No flux is declared anywhere. L0-1d affinity and the RS-1 antiperiodic grid are generator/BC parameters. |
| Lift C₀ covariance (state data) | NOT-PERSISTENT | It decays to the vacuum |

### §4.5 Structural reasons (what the earned core lacks for the SF-1 mechanism)

Relative to SF-1, the earned core lacks every ingredient that made the mechanism work:

| SF-1 ingredient | Earned core | Where the record has it |
|---|---|---|
| (i) An exactly conserved charge | None: dissipation kills every first integral [AA] | Conservative classes (O-6, FS-1, CA-1 F) and the Fock number of a *supplied* lift |
| (ii) A family of distinct persistent reference states | One attractor | — |
| (iii) A declared quadratic retained observable | Linear x₁ only | O-6 J and S₁ (site-local); the CA-1 F / RS-1 density |
| (iv) Pauli statistics, so that the conserved charge selects a region of the band | None; the boson route collapses by the condensation identity [AA] | Only the complex-fermion lift or the CA-1 F contrast, both supplied |

This is a description of what is missing. **No model is proposed, and no variable is invented.**

## §5 Outcome

**Mechanical application of §3:**
1. Step 1: no Tier-E candidate is CLEAN, so the outcome is not GRUT-CANDIDATE-FOUND.
2. Step 2:
   - **A CLEAN candidate exists outside Tier E:** CA-1 F conserved-N filling sectors. It is Tier C
     or Tier L (contested), and the difference is already known from SF-1.
   - **Tier-E absence is shown** at identity grade [AA], corroborated by the record (SC-2, bridge
     TRIVIAL/IDENTITY, RANK-CONSTANT).
   - So the outcome is **CLASS-SPLIT**.

> **SFG-0 OUTCOME (proposed, mechanical): CLASS-SPLIT.**
> - **Tier E (earned core): provably no formation variable.** There is no nontrivial conserved
>   quantity, one persistent state, a linear readout, and no statistics.
> - **The only CLEAN candidate is CA-1 F** (conserved fermion number on the ring K). This is
>   **the SF-1 parent itself**, and it is **conditional on supplied fermionic statistics** (the
>   complex-fermion lift / CA-1's declared non-carrier contrast).
> - **Contested and formulable at most:** O-6 conservative-chain sub-torus occupancy.

**Qualifications that bear on your ruling:**

- **Q-A. Circularity.** The CLEAN candidate is not a new GRUT variable. It is SF-1's own parent
  re-found in the record. SFG-0 therefore finds **no GRUT-native formation variable beyond the one
  SF-1 already used.**
- **Q-B. GRUT's own fermion lift does not carry it.** The complex-fermion lift declared **for the
  earned substrate** (K_b) is Lindblad loss. N is not conserved there, so the sectors are
  NOT-PERSISTENT. CA-1 F is a *conservative hopping contrast* on the ring K. It is not the lift of
  the earned dynamics.
- **Q-C. If you rule CA-1 F out of scope** (as circular or as a non-GRUT contrast), the mechanical
  outcome falls to:
  - **STATE-NOT-LAW**, if O-6 sub-torus occupancy is not accepted as CLEAN. Persistent sectors
    exist (O-6 tori, FS-1 tower, P-6 blocks), but all are forced equal or undeclared.
  - **CLASS-SPLIT (Tier C: O-6 sub-torus, formulable only)**, if it is accepted.
- **Q-D. [AA] grade.** The Tier-E absence and the boson condensation identity are auditor-derived
  standard identities resting on record theorems. They are not record theorems themselves.

**Reading for the S-5 question.** Answering the owner's framing honestly:

> **GRUT's earned core does not presently contain a formation variable.** The SF-1 mechanism is
> real, but in the current record it is hosted only by conservative, number-conserving
> fermionic structure that is supplied (lift or contrast), not earned.

This strengthens the case that GRUT's supplied selections sit upstream, in the generator,
statistics and lift. **That is the S-5 question.** The one non-S-5 alternative left is the
contested O-6 sub-torus case.

**Fences:**
- No new physics was run and no variable was invented.
- No SF-2, no S-5, no cosmology.

**HARD STOP for owner ruling.** The rulings needed:
1. the CA-1 F scope/tier;
2. the O-6 sub-torus case;
3. the SFG-0 terminal;
4. the next step (S-5 or otherwise).
