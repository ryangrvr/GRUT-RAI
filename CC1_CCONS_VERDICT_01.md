# CC-1 — CAN C_cons BE DERIVED FROM EARNED STRUCTURE? VERDICT

**Date:** 2026-09-25 · **Charter:** `CC1_CCONS_CHARTER_01.md` (frozen at
`86a839f` before the run) · **Authority:** GitHub Issue #2, owner comment
5835662238 · **Instrument:** `calc/cc1_ccons.py` · **Artifact:**
`CC1_CCONS_RESULT.json` (sha `7c1ca609dce0d639…`) · **Battery 29/29,
zero failures, zero halts, single run, no defects.** The halt-grade
identities held at machine precision: the unit-change spectrum to
2e-15, conserved-source residues equal to their physical polarization
sums to 4e-15 and 1e-12, and the driven-weight/commutator equivalence
exact on all four operators.

## VERDICT

> **C_cons is NOT derived. IRREDUCIBLE INPUT**, reduced to one named
> supplied structure: **the probe is a massless gauge field**.
> 𝔠_full positivity forces conservation *only* for such a probe.
>
> Components:
> - **Constant level:** NOT selected. A non-conserved coupling
>   survives every earned selector.
> - **Static regularity:** CONSTRAINED-NONUNIQUE. It cuts IR-singular
>   couplings only.
> - **Stationarity under driving:** equivalent to C_cons, a
>   restatement.
> - **A blanket C_cons contradicts GR-1's own channel.**
> - **Positivity:** CLASS-SPLIT by probe field content.

## WHAT THE RUN SHOWED

**1. A non-conserved coupling passes every earned constant-level
selector.** The phonon **mass modulation** O_M = ½Σpᵢ² is not conserved
(commutator residual 2.0). Yet:
- 𝔠_full admits it (PSD);
- G-2 hop geometry is unchanged (exactly 1/2/3/4);
- G-2 static resistance is unchanged (ratio 1 to 15 digits);
- it is spectrally a pure unit change: ω′ = √(1+h)ω, with the shape
  equal to 2e-15;
- it is static-limit regular (extensive susceptibility, ratio 2.003);
- it even satisfies **GeoInv**.

At the constant level it is **unitarily equivalent** to the conserved
unit change: a squeeze composed with a time rescaling. It differs only
once the probe is switched on or driven. **C_cons is therefore not
selected by anything earned.**

**2. Static regularity cuts some couplings, but not the survivor.** The
pinning modulation ½Σuᵢ² is IR-singular: its susceptibility grows as
~N³, with ratio 7.84 for N = 40 over N = 20. It is excluded, but the
mass modulation is not, so this constraint is CONSTRAINED-NONUNIQUE. In
the generic interacting chain, ΣXᵢ is non-conserved, 𝔠_full-admissible,
graph-preserving and static-regular. Only the unearned Sel-4 objects to
it (shape change 7.5e-3).

**3. The owner's separation: stationarity versus fundamentality.**
- **"Stationary under driving" is C_cons restated.** The
  nonzero-frequency spectral weight vanishes exactly when [O, H] = 0,
  on all four test operators, a halt-grade identity. It adds no
  independent ground.
- **A constant probe needs no conservation to be stationary.** Under
  the constant non-conserved probe H + hΣXᵢ, two-time correlators
  depend only on the time difference (4e-15).
- Hence "conservation is dynamically necessary for stationary behaviour
  under driving" is true, but **it does not imply the fundamental
  coupling must be conserved.** It *is* the conservation condition, not
  a reason for it.

**4. A blanket C_cons would delete GR-1's channel.** On the phonon ring,
the conserved H has zero pair amplitude, while the geometric T_xx
vertex that carries GR-1's gravitational channel has dynamic weight
12.3. It is non-conserved by construction: it creates pairs. So C_cons
can at most be **component-specific** (the clock/energy component). It
cannot be a principle about the probe as a whole.

**5. The positivity route: conservation from 𝔠_full, at a stated
price.** These are D = 4 exchange residues, used as an algebraic
positivity test only, not the TT/ξ question.
- **Massless vector and massless spin-2:** conserved sources give
  non-negative residues that equal the physical polarization sums.
  Non-conserved sources give **negative** residues (−10.6 and −17.8).
  That is ghost exchange, a 𝔠_full violation.
- **Massive vector (Proca) and massive spin-2 (Fierz–Pauli):**
  non-conserved sources are **always positive**.

**𝔠_full forces conservation if and only if the probe is a massless
gauge field**, meaning covariant, with redundant polarizations. That
field content is **supplied**, so C_cons reduces to it. What it yields
is *current* conservation (k_μT^{μν} = 0). Its zero-momentum time
component is exactly S4-1's clock C_cons, while T_xx remains a
non-conserved flux, consistent with finding 4. This is standard physics
(the Weinberg/Gupta–Bleuler-type argument), so it is
**NULL-REDUNDANT as a new principle.** The instrument's contribution is
the dependency map, not new mathematics.

## STRENGTH AND LIMITS (stated plainly)

- **The stationarity leg is an identity.** It shows equivalence; it is
  not a discovery.
- **The positivity leg rests on Lorentz-covariant propagators.** Lorentz
  covariance is itself a supplied symmetry: G-2's recovered geometry is
  not Lorentzian. The masslessness of the probe is also supplied.
- **The constant-level survivor is special.** The mass modulation is a
  representation of a unit change at the constant level, so its
  non-conservation is visible only dynamically (pair creation, the base
  class). It remains a legitimate non-conserved survivor: every earned
  constant-level selector admits it.
- **Scope:** free phonon ring (N = 20/40) and finite generic chain
  (L = 6). Exchange positivity in D = 4 with 200 random sources per
  case.

## LEDGER AFTER CC-1

- **κ:** discharged.
- **Minimal stress → geometric coupling → Sel-4:** as before.
- **Sel-4 is conditional on C_cons.**
- **C_cons is IRREDUCIBLE**, reduced to the supplied premise **"the
  probe is a massless gauge field"**. It is component-specific at most:
  the clock component. A blanket version is inconsistent with GR-1.
- **GeoInv:** unearned. It does not imply C_cons: the mass modulation
  satisfies GeoInv without being conserved.
- **Retained sector:** separate.
- **Class-4:** OPEN.

ω⁷ occupancy only. GR-1 3D red. ℏ located. D = 4 TT/ξ, operator
ordering and geometry selection fenced.

**The architecture statement this completes:** the dependency chain
behind the gravitational coupling now bottoms out in two supplied
structures:
1. **the probe is a massless gauge field**, which gives C_cons via
   positivity;
2. **cross-sector universality for non-interacting sectors** (S4-1's
   irreducible core).

Everything between them and the ω⁷ class has been localized, derived
conditionally, or shown to be standard structure.

## HARD STOP

Per the owner: **hard stop after the C_cons verdict.** C_cons is now
explicitly classified as **irreducible, reduced to supplied probe field
content**. That satisfies the owner's gate ("resolved or explicitly
classified as irreducible") for advancing to universality, the retained
sector or geometry selection, if and when the owner rules.
