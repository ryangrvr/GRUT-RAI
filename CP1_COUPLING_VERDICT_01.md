# CP-1 — CAN THE MINIMAL-STRESS COUPLING BE SELECTED WITHOUT INSERTING IT? VERDICT

**Date:** 2026-09-25 · **Charter:** `CP1_COUPLING_CHARTER_01.md` (frozen
at `d78f9a4` before the run) · **Authority:** owner ruling recorded in
`GR1_CP1_OWNER_RULING_01.md` · **Instrument:** `calc/cp1_coupling.py` ·
**Artifact:** `CP1_COUPLING_RESULT.json` (sha `86616b0638b11874…`) ·
**Battery 39/39, zero failures, zero halts, single run, no defects.**
The matched control reproduced GR-1's recorded canonical slope
(8.005420) to 2.0e-12. The verdict string was computed mechanically
from the measurements by the frozen outcome rule.

## VERDICT

> **CLASS-SPLIT.** The minimal-stress coupling is **not** selected
> uniformly by anything already in 𝒯. Conservation alone leaves it
> **CONSTRAINED-NONUNIQUE**; the admissible hierarchy is **NULL as a
> selector**; IR Weyl symmetry **selects it in D = 2 and selects a
> different, off-locus coupling in D = 4**; for transverse-traceless
> probes the question is **vacuous**. The import is **not discharged**.
> It **reduces** to a single named principle: *geometric
> (proper-distance) coupling of the retained sector, at ξ = 0* — which
> is not already in 𝒯. **Class-4 stays open.**

## WHAT EACH CANDIDATE SELECTOR DID

| Selector | Result | Class |
|---|---|---|
| The exponent itself (L-F) | +4 holds on a plane of couplings; the non-canonical (0,1,1,0) gives 8.005 too | does not identify the coupling |
| 𝔠_full admissibility (L-H) | all four couplings PSD (canonical, improved, contact, material) | NULL as selector |
| Conservation (L-C) | nullity 2 in D = 2 and D = 4: canonical + ξ·improvement | CONSTRAINED-NONUNIQUE |
| Conservation + IR Weyl (L-W) | nullity 1 in both D; D = 2 → canonical (slope 8.005, on-locus); D = 4 → (2,−1,−1,0), the improved tensor (slope 4.004, off-locus) | CLASS-SPLIT by dimension |
| TT access class (L-TT) | the TT image of the entire family has rank 1 | coupling form forced; import vacuous |
| Geometric coupling, chartered candidate (L-M) | +4 on both dispersions; material modulations give 0 or base | reduction, not discharge |

## THE FINDINGS THAT MATTER

**1. The exponent does not identify the coupling.** The +4 locus
{c = 0, a − g + b = 0} is a plane. A non-conserved, non-canonical
coupling (0,1,1,0) produces the same 8.005 slope as minimal stress.
GR-1 showed the exponent is selected *given* the coupling class. CP-1
shows the converse fails: the exponent cannot be run backward to
recover minimal stress.

**2. Conservation cuts the family to exactly one free parameter.** In
both D = 2 and D = 4 the conserved couplings are canonical plus ξ times
the improvement term, with both vectors in the null space to 3e-16.
ξ = 0.2 lands in the base class, so the free parameter spans on-locus
and off-locus members.

**3. IR Weyl symmetry fixes ξ, but to different values in different
dimensions.** Weyl symmetry is the tracelessness of the gapless retained
sector, a symmetry already in the class rather than an import. It
removes the last freedom in both dimensions (nullity 1). In D = 2 it
lands exactly on canonical minimal stress, which is on the +4 locus. In
D = 4 it lands on the conformally improved tensor (2,−1,−1,0), which in
strain-probe kinematics sits in the base class. **The same principle
that derives minimal stress in 1+1 selects a different coupling in
3+1.** That is the class split.

**4. For transverse-traceless probes, the coupling form is not an input
at all.** The TT projector kills the η-terms (b, c) and maps
g → −a exactly (both halt-grade at ~1e-14), so the whole declared family
collapses to a single TT tensor up to amplitude. Kinetic/gradient
weighting, contact terms and the improvement ambiguity are all
invisible. Whether the TT channel then carries the +4 is a kinematic
question in the v3 record's convention and was **not** re-adjudicated.

**5. The minimal-stress import reduces to geometric coupling.** The
candidate principle was chartered as a hypothesis: *the probe couples to
the retained sector only through proper distance*, i.e. metric variation
of the retained dispersion, V = ½[q²D′ − D]. It gives +4 on both the
continuum dispersion (coefficient −0.049994 vs predicted −α) and the
nearest-neighbour lattice (−0.041660 vs −1/24). In the IR it equals
canonical minimal stress up to normalization (ratio 0.499969). The
material counterfactuals fail to produce +4:
- mass-only and stiffness-only modulations give the base class (4.002
  each);
- the impedance-preserving combination μ = −κ gives a vertex that is
  exactly zero.

Among {mass, stiffness, proper-distance} modulations, **only geometric
coupling produces the +4.** This is the sharpest reformulation of the
import on record: the minimal-stress postulate is the equivalence
principle (coupling through geometry only) at ξ = 0.

## STRENGTH AND LIMITS (stated plainly)

- **Most gates confirm analytic predictions.** Every exponent, null
  space and identity was predicted in closed form in the charter before
  the run, and the instrument confirmed them numerically, from the
  actual tensors, to machine precision. The new content is the
  **division of labor among principles**: what conservation does, what
  Weyl symmetry does, what access class does, and what geometric
  coupling does. The run does not add any new mathematics.
- **The family is declared, not exhaustive:** symmetric, local,
  bilinear, at most two derivatives. The TT rank-1 collapse in
  particular is a property of this family; higher-derivative couplings
  would enlarge the TT image.
- **The metric covariantization of a dispersive operator,
  D(g^{xx}q²) with √g, is itself a choice** (operator-ordering
  ambiguity). L-M tested the natural choice; it did not derive that the
  choice is unique.
- **L-H is weak by design:** real couplings always give PSD Grams, so
  the NULL result was expected. It is recorded because the owner's
  question named 𝔠_full explicitly.
- **D = 4 is tested only in strain-probe kinematics** (zero net spatial
  momentum). The physical-graviton question lives in the TT class, where
  the form is vacuous and the exponent is kinematic, which is v3
  territory.

## CLASS-4 CONSEQUENCE (frozen rule)

The minimal-stress import is **not discharged**. It stays load-bearing,
restated in reduced form:

> **geometric (proper-distance) coupling of the retained sector at
> ξ = 0**, where ξ = 0 is selected by IR Weyl symmetry in D = 2, is
> **not** selected by it in D = 4 strain kinematics, and is invisible
> to TT probes.

The ledger now reads: κ discharged (GR-1). Minimal-stress reduced to
equivalence plus ξ, class-split by dimension and access (CP-1).
Retained-sector untouched, held fixed per the owner ruling. **Class-4
remains OPEN.**

## FENCES

ω⁷ not reopened or relabeled (v3 20/20 by hash only); GR-1's 3D red
untouched; exponents compared as classes inside GR-1's own instrument
convention only; no Einstein or field equations; ℏ
located-not-generated; retained-sector import held fixed and not
attacked; geometry-selection not touched; Λ_R, Matsubara, Π₀, U5
fenced; type-III boundary map only.

## HARD STOP

Verdict recorded. The record now presents these forks for the owner:
- **(a) Attack the equivalence principle itself.** Can "couples only
  through geometry" be derived from 𝔠_full + access + the G-2-recovered
  geometry, or is it the definition of what gravity means in this
  program? This is the reduced form of the import.
- **(b) Attack the D = 4 ξ question in the physical TT class**, where
  CP-1 shows the form is vacuous and the exponent is kinematic.
- **(c) The retained-sector import.**
- **(d) Geometry-selection.**

(c) and (d) remain separate per the ruling. The owner rules.
