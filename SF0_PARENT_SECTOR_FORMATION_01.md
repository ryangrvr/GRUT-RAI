# SF-0 — PARENT-SECTOR FORMATION / LAW-SELECTION: definitions (pre-registered) and record audit

**STATUS: §§0–3 PRE-REGISTERED.** They are committed **before any candidate is inspected**, per
the owner's direction ("The audit must define the equivalence relation before inspecting a
candidate"). The §4 audit and the §5 outcome are added in a later commit.
- **Authority:** `SF0_CAMPAIGN_OWNER_DIRECTION_01.md` (Issue #2 comment `5903141169`).
- **No new numerical physics.**
- **Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

## §0 H-SF (verbatim from the direction)

> There exists a declared parent system X with fixed microscopic degrees of freedom, locality
> structure, generator, couplings and numerical parameters, for which two or more dynamically
> stable / asymptotically persistent sectors S_A, S_B, … are selected only by admissible state,
> history or boundary data, and the sectors possess inequivalent effective-law structure.

## §1 The coarse-graining map 𝓔 (declared before inspection)

For a candidate parent X with admissible states ρ, the effective law is L_eff = 𝓔[X, ρ]. 𝓔 must be
**declared per candidate class, before its sectors are examined,** and must use only X and ρ. The
default constructions, one of which each candidate must use:

- **𝓔-lin (linearization about a persistent state).** Let ρ* be the persistent limit or stable
  invariant state reached from ρ (a stable fixed point, periodic orbit or invariant sector).
  L_eff = the linearized generator of fluctuations about ρ*, restricted to the declared retained
  observables, together with its low-frequency response of the retained observables.
- **𝓔-sector (restriction to an exact invariant sector).** If X has an exact invariant sector 𝒮
  selected by ρ (a conserved charge value, a topological sector, a reachable invariant subspace),
  then L_eff = the generator restricted to 𝒮 (or its linearization about the persistent state in
  𝒮), with the same retained-observable response.
- **𝓔-RG (a declared coarse-graining).** Only if the record already contains an explicit,
  pre-declared RG/block map for that class.

**Forbidden:**
- choosing 𝓔 differently for different sectors of the same candidate;
- selecting the retained observables per sector;
- any 𝓔 that uses a parameter not in X.

## §2 The structural invariants (pre-registered list)

A difference in L_eff counts as **law-level** only if at least one of the following differs, each
read off L_eff at identity/theorem grade or by an exact criterion:

| # | Invariant | How it is read off L_eff |
|---|---|---|
| I-z | Dynamic exponent z (ω ~ k^z of the lowest excitation branch) | dispersion of the linearized generator |
| I-s | Low-frequency response exponent/class s of the retained kernel (e.g. exponential/gapped vs power-law ~ t^{−s}) | the pole-sensitive memory class (O-5 corrected form) |
| I-pc | Pole vs branch-cut structure of the retained response G(z) | analytic structure of the reduced resolvent |
| I-gap | Gapped vs gapless | spectral gap of L_eff = 0 or > 0 (exact) |
| I-q | Quasiparticle / statistics content (number of gapless branches; occupation structure where a lift is declared) | branch count; Sym vs Λ structure |
| I-c | Causal/propagation cone class (finite maximal group velocity vs none; light-cone vs diffusive) | support growth of the retained response |
| I-d | Effective dimensionality / topology (spectral dimension; topology of the effective coupling graph) | spectral density exponent; graph invariants |
| I-sym | Exact symmetry / conservation algebra of L_eff | commutant / conserved quantities of L_eff |

**A value difference inside one class is NOT law-level.** Examples: a different gap *value*, a
different velocity *value*, a different amplitude, or continuous reweighting of a fixed support.
This is binding per `L0_ACCESS_BRIDGE_OWNER_RULING_01.md` §2 and the direction.

## §3 The equivalence relation ≃ (pre-registered)

L_eff^A ≃ L_eff^B iff every invariant in §2 coincides after applying any composition of:

1. **basis change / invertible field redefinition** that preserves the declared locality structure;
2. **relabeling** by an automorphism of the parent's site net (a permutation preserving X);
3. **constant rescalings** of time, space, field amplitude or units;
4. **parent symmetry:** mapping ρ_A to ρ_B by a symmetry g of X (g X g⁻¹ = X). Symmetry-copy vacua
   are **equivalent by definition**;
5. **representational lift change** that preserves every effective observable (per
   `L0_LIFT_SELECTION_EVALUATION_01.md`: Λ-K, Λ-KvN and Liouville-δ are representational).

**Law-inequivalence (≄)** holds iff, after the quotient above, at least one §2 invariant differs at
identity/theorem grade. **"Different value, same class" ⇒ ≃.**

**Candidate classification (seven questions, per the direction):**
- (1) same generator;
- (2) same parameters;
- (3) selection by state/history only;
- (4) persistence (an invariant set is stable or exactly invariant under X);
- (5) a §2 invariant differs;
- (6) not reducible by §3;
- (7) sector not declared in the inputs.

H-SF-positive requires **yes** on all seven.

**Mechanical outcome rule (frozen in the direction):** the strongest surviving candidate decides.
The ordering is:

> ALREADY-DEMONSTRATED > FORMULABLE-IN-EXISTING-CLASS > STATE-NOT-LAW / SECTOR-SMUGGLED >
> REQUIRES-NEW-PARENT > UNFORMULABLE

**Tie-break note (declared now):** if every candidate is STATE-NOT-LAW or SECTOR-SMUGGLED and no
existing class contains the ingredients for a clean test, the gate outcome is
**REQUIRES-NEW-PARENT**, with the per-candidate labels recorded. The reason: the direction's
REQUIRES-NEW-PARENT means "current substrate classes cannot host the test", and that is the
operative gate fact.

## §4 Record audit

*(Added in a later commit, after the candidate audits.)*

## §5 Outcome

*(Added in a later commit.)*
