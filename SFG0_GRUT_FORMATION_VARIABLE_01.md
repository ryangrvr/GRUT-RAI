# SFG-0 — GRUT FORMATION-VARIABLE AUDIT (audit only; no new physics run)

**STATUS: §§0–3 PRE-REGISTERED** before any candidate is audited. §4 (the audit) and §5 (the
outcome) will be added in a later commit.
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

*(Added in a later commit.)*

## §5 Outcome

*(Added in a later commit.)*
