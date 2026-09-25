# EQ-1 — CAN GEOMETRIC-ONLY COUPLING BE SELECTED FROM EARNED STRUCTURE? VERDICT

**Date:** 2026-09-25 · **Charter:** `EQ1_EQUIVALENCE_CHARTER_01.md`
(frozen at `708a31b` before the run) · **Authority:** GitHub Issue #2,
owner comment 5834587876 · **Instrument:** `calc/eq1_equivalence.py` ·
**Artifact:** `EQ1_EQUIVALENCE_RESULT.json` (sha `560f439b588a68b1…`) ·
**Battery 45/46.** The one failure is a frozen gate preserved red; a
labeled diagnostic shows its premise was wrong. Zero halts. The matched
control reproduced CP-1's recorded slope exactly.

## VERDICT

> **Geometric coupling is NOT derived.** Every earned constraint
> admits a non-geometric coupling alongside it
> (**CONSTRAINED-NONUNIQUE**). It is selected uniquely only when one
> further, non-earned principle is added (**IRREDUCIBLE INPUT**):
>
> **Sel-4: a constant probe must act on each retained sector as a pure
> change of units, invisible to the sector's own intrinsic data.**
>
> This is the operational weak-equivalence statement. The import is
> not discharged. It is reduced to Sel-4. **Class-4 stays open.**

The mechanical rule also emitted **UNDERDETERMINED under pair access**
and **CLASS-SPLIT**. Both flags are recorded as emitted, but both rest
on the mis-premised gate below. What they actually establish is stated
in that section.

## WHAT EACH SELECTOR DID

| Selector | Earned? | Result |
|---|---|---|
| The exponent itself (L-X) | — | a non-geometric shape coupling gives 8.006 / 8.005, the same +4 class; a tuned member gives 12.008, a +8 class |
| 𝔠_full (L-H) | yes | all five couplings admissible: NULL |
| G-2 recovered geometry (L-G2) | yes | proper distance ≡ stiffness (2.2e-16); shape invisible (2e-15): NULL |
| IR conservation + IR Weyl in 2D (L-C) | yes | nullity 3; geometric and non-geometric both pass (residuals ≤ 6e-13); vertex rank **2** |
| **Sel-4** (L-I) | **no, candidate** | mass, stiffness, proper distance and improvement are exact unit changes (≤ 6e-13); shape changes Π (−0.27, −0.59); with Sel-4 the vertex rank is **1** and the survivor slope is 8.005 / 8.004 |

### Three findings the owner's boundaries asked for

**1. Recovered geometry is not the coupling ansatz.** Everything
G-2-recoverable at IR level (resistance density, IR speed) responds to
a proper-distance modulation exactly as it responds to a stiffness
modulation. It does not see a dispersion-shape modulation at all.
G-2's recovered geometry cannot tell geometric coupling from material
coupling, so it cannot be the selector.

**2. The exponent selects neither the coupling nor, strictly, its own
class.** A purely material shape coupling lands in the same +4 class as
geometric coupling, on both species. A fine-tuned geometric-plus-shape
member lands in a +8 class (slope 12). Earned structure makes +4
generic, not forced.

**3. Earned structure stops one principle short.** IR conservation and
2D Weyl symmetry, both earned in CP-1, cut the family to three
directions. That leaves geometric and non-geometric couplings with
distinct vertices (rank 2). Adding Sel-4 removes the non-geometric
direction exactly. The geometric vertex is then the unique survivor,
up to amplitude and a pair-invisible time rescaling. Sel-4 is not
derivable from 𝔠_full, conservation, Weyl symmetry or recovered
geometry. The shape coupling satisfies every one of them and violates
only Sel-4.

## THE RED GATE, AND WHAT IT CORRECTED

**Frozen gate (FAILED, stays red):** "the species-A material mimic's
constant limit changes the intrinsic shape (|dΠ/dh| > 1e-3)." Measured:
2.7e-10.

**Labeled diagnostic:** the "material mimic" σQ² + σ₂Q³ equals
D − QD′ to 8.8e-13. On a polynomial dispersion, that shape combination
acts on the sector exactly as stiffness minus proper distance. It
differs from the geometric coupling only by a pair-null time
rescaling. So the "mimic" was the geometric coupling in material
clothing, and its constant limit is a unit change. The gate's premise
was wrong, not the instrument.

**What this corrects, stated plainly:**
- **"Geometric" versus "material" is not a sector-intrinsic
  distinction.** On a single sector, proper-distance coupling can be
  rewritten exactly as a combination of material modulations. What
  Sel-4 actually selects is the **unit-change class**, whatever it is
  called.
- **My charter claim "static access separates what pair access
  cannot" is withdrawn.** Within this family, two couplings with
  identical complete pair data act identically on the dispersion, so
  they have the same constant limit. Complete dynamical data therefore
  do decide Sel-4 compliance. Only **finite-order** data cannot: on the
  lattice, a 1-term shape fit leaves a residual that grows as Q (ratio
  4.035) and a 2-term fit leaves one that grows as Q² (ratio 16.65).
  The separation enters at the first unmatched order, the same ladder
  as P-4 and G-2.
- **The UNDERDETERMINED flag** fired because of the species-A "exact
  mimic", which is not an alternative. The grounded statement is:
  underdetermined at any finite order of pair data (species B ladder),
  not underdetermined in principle.
- **The CLASS-SPLIT flag** fired because species A (polynomial
  dispersion) admits an exact finite rewrite and species B (lattice)
  only a ladder. That is one fact seen on two dispersion types. It is
  not a physical split of the selector result. Selection behaved
  identically on both species (rank 2 earned, rank 1 with Sel-4).

## THE IMPORT LEDGER AFTER EQ-1

- **κ:** discharged (GR-1).
- **Minimal stress:** reduced to geometric coupling at ξ = 0 (CP-1).
- **Geometric coupling:** reduced to **Sel-4, constant-probe
  unit-change invisibility**, in 1+1 given earned IR conservation and
  2D Weyl. Sel-4 is a falsifiable physical statement: a constant probe
  that changed a sector's intrinsic dispersion shape would violate it.
  Complete dynamical pair data can detect such a violation; finite-order
  data cannot.
- **Retained sector:** untouched.
- **Class-4:** OPEN.

## SCOPE AND FENCES

1+1 only. The D = 4 strain/TT split and the ξ question stay open. The
operator-ordering ambiguity stays open: uniform zero-momentum probes
cannot see it. The five-direction family is declared, not exhaustive.
No Einstein equations were used. ω⁷ and v3 were not reopened. The GR-1
3D red remains red. ℏ located-not-generated. Retained sector held
fixed. Λ_R, Matsubara, Π₀, U5 fenced.

## HARD STOP

Per the owner ("HARD STOP after the next geometry/equivalence
verdict"). The forks now on the record:
- **(a′)** Attack Sel-4 itself. Is "a constant probe acts as a unit
  change" derivable from anything earned, or is it where this
  program's gravity is simply defined?
- **(b)** The physical D = 4 TT channel and ξ.
- **(c)** The retained-sector import.
- **(d)** Geometry selection.

The owner rules.
