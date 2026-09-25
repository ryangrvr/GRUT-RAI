# FS-1 — CAN THE UNIT-CHANGE RESULT BE SELECTED FOR A GENUINELY FREE GAPLESS SECTOR? VERDICT

**Date:** 2026-09-25 · **Charter:** `FS1_FREE_SECTOR_CHARTER_01.md`
(frozen at `19fd85f` before the run) · **Authority:** owner ruling
recorded in `S41_FS1_OWNER_RULING_01.md` · **Instrument:**
`calc/fs1_free.py` · **Artifact:** `FS1_FREE_RESULT.json` (sha
`698ba9b526e04cb6…`) · **Battery 31/31, zero failures, zero halts,
single run, no defects.** [H, H] = 0.0 exactly. The explicit charges
were conserved to 0.0. Amplitude invariance held to 4e-16.
**Everything below is conditional on C_cons, an unresolved import per
the owner's ruling.**

## VERDICT

> **SELECT: IRREDUCIBLE INPUT, reduced to one candidate: GeoInv.**
> Nothing earned selects O = H in the free sector. Every member of
> its conserved tower is admissible. With one non-earned addition,
> *"a constant probe must not rewire the sector's recovered geometry"*,
> O = H is selected exactly.
>
> **DISTINGUISH:**
> - **dynamic influence data: NO** (UNDERDETERMINED, identically);
> - **static multi-temperature influence data: YES**;
> - **G-2 hop geometry: YES.**
>
> **The free-sector exception is STRUCTURAL**, not an artifact of
> S4-1's spin models.

## WHAT THE RUN SHOWED

**1. The exception is structural.** The exact phonon ring (N = 20,
gapless, the class GR-1's retained sector belongs to) carries
**exactly 2R independent local conserved quadratic charges within range
R**: 2, 4, 6, 8 for R = 1..4, matching the prediction exactly. The
tower grows without bound: H, an even family Q_n (weights cos nk) and
an odd family P_n. This is a property of the free phonon sector itself.

**2. 𝔠_full selects nothing.** A constant probe along any tower member
leaves the Hamiltonian bounded below. That holds for H, Q₂, P₁ and all
six R = 3 tower directions (min eigenvalue ≥ −3e-16).

**3. The probe's dynamic influence data cannot tell O = H from any
conserved charge, and this is exact.** For every conserved coupling the
vacuum connected correlator is **identically zero**, and at any
temperature it is time-independent, so J(ω ≠ 0) ≡ 0. Consequence for
GR-1: **conserved clock couplings contribute nothing to its
zero-momentum pair channel.** GR-1's dynamic construction is therefore
*insensitive* to this ambiguity. That is not the same as the ambiguity
being *resolved*.

**4. Richer access does distinguish.**
- **Static, multi-temperature data (amplitude-free):** the ratio
  Var(T = 0.5)/Var(T = 2) is 0.03724 for H, 0.03790 for Q₁ and 0.04704
  for P₁. The Q₁ separation (1.8%) is thin against the 1% gate; the
  P₁ separation (26%) is not.
- **G-2 hop geometry of the probe-modified sector:** a unit change
  (O = H) leaves the recovered hop distances at exactly 1.000, 2.000,
  3.000, 4.000. The Q₂ probe **rewires** the geometry: distance-2 sites
  read as adjacent (d̂ = 0.002). The P₁ probe moves nearest neighbours
  to d̂ = 0.505. By contrast, static resistance at distance 8 barely
  separates H from Q₂ (0.952 vs 0.962): the IR geometry is nearly
  blind, and the difference lives at short range.

**5. What would select O = H.** On the R = 3 tower, the candidate
**GeoInv** ("a constant probe preserves the G-2-recovered hop
geometry") leaves a null space of **dim 1**, and the survivor is **H
itself** (residual 4e-16). For free sectors, therefore:

> given C_cons, **clock equivalence ⇔ the constant probe does not
> rewire the recovered geometry.**

GeoInv is not earned. It was chartered as a candidate, exactly as Sel-4
was in EQ-1.

## STRENGTH AND LIMITS (stated plainly)

- **Conditional on C_cons.** The tower *is* the set of conserved
  couplings; without C_cons the family is larger still. GeoInv does
  **not** replace C_cons: S4-1 showed a non-conserved coupling (Σ Xᵢ)
  that preserves the interaction graph. For the free sector the
  selection is C_cons + GeoInv ⇒ O ∝ H. Neither constraint is earned.
- **The influence leg is mode-space analytic.** The vacuum zero is an
  identity of conservation, not an independent numerical discovery.
  The static discriminator's Q₁ margin is thin.
- **Scope:** quadratic, translation-invariant charges up to range 4, on
  a finite periodic ring. Non-quadratic conserved charges and
  non-translation-invariant couplings were not examined.
- **GeoInv is a restatement risk.** It is weaker than Sel-4 (it demands
  invariance of recovered geometry only, not of all intrinsic data).
  But like Sel-4 it is a constraint imposed on the probe, not derived
  from the sector.

## LEDGER

- κ discharged.
- Minimal stress → geometric coupling → Sel-4.
- Sel-4 conditional on C_cons, an **unresolved import**.
- In the **free retained sector**: structural non-uniqueness. Selection
  requires C_cons + **GeoInv**, both supplied.
- GR-1's dynamic channel is **insensitive** to the free-sector clock
  ambiguity.
- Non-interacting universality is the next-next attack.
- **Class-4 OPEN.**

ω⁷ occupancy only (not upgraded by the insensitivity statement). ℏ
located. GR-1 3D red. D = 4 TT/ξ, operator ordering and geometry
selection separate. No Einstein equations.

## HARD STOP

The decisions this puts before the owner:
- **(1) GeoInv's status.** It is a new, sharper candidate import for
  the free sector. Rule on it, or attack it.
- **(2) Next attack.** The standing plan is non-interacting
  universality, now cleaner because the free class is characterized.
  The alternative is attacking C_cons itself: can conservation of the
  probe coupling be earned from 𝔠_full + access?
- **(3) The separate forks,** unchanged.

The owner rules.
