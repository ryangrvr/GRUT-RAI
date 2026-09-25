# S4-1 — CAN Sel-4 BE SELECTED WITHOUT DEFINING GRAVITY AS Sel-4? VERDICT

**Date:** 2026-09-25 · **Charter:** `S41_SEL4_CHARTER_01.md` (frozen at
`e83b6f0` before the run) · **Authority:** owner ruling recorded in
`EQ1_S41_OWNER_RULING_01.md` · **Instrument:** `calc/s41_sel4.py` ·
**Artifact:** `S41_SEL4_RESULT.json` (sha `19bfd954de32a492…`) ·
**Battery 28/28, zero failures, zero halts, single run, no defects.**
Symbolic commutants are exact. [H, H] = 0 in the Pauli algebra. The
dense-matrix commutator of the extracted charge was 0.0. The
universal-probe discriminators were 8.4e-14 and 1.8e-14.

## VERDICT

> **Sel-4 as a whole is NOT derived. It splits.** The earned structure
> does not select Sel-4 by itself: 𝔠_full and G-2 geometry are NULL as
> selectors. The single inherited constraint **C_cons** (*the probe's
> constant limit couples to a conserved local charge*) does derive two
> parts of Sel-4, but only in specific classes:
>
> | Part | Result |
> |---|---|
> | **Sel-4t** (one sector's clock) | DERIVED-IN-CLASS for **generic** sectors · NOT forced for **integrable/free** sectors |
> | **Sel-4U** (universality of clocks) | DERIVED-IN-CLASS for **interacting** sectors · **IRREDUCIBLE** for **non-interacting** sectors |
> | **Sel-4x** (length part) | IRREDUCIBLE (EQ-1, carried) |
>
> Every "derived" entry is **conditional on C_cons**, and C_cons does
> all of the selecting.

## WHAT THE RUN SHOWED

**1. For a generic sector, conservation forces the clock coupling to be
a unit change.** In the non-integrable mixed-field Ising chain, the only
operator in the 48-operator local basis (range ≤ 3, L = 8) that commutes
with H is H itself (commutant dim 1). If the probe's constant limit must
couple to a conserved local charge, it must be O ∝ H, which is exactly a
time-unit change.

**2. For integrable and free sectors it does not.** The transverse-field
Ising chain has commutant dim 4 and the free XX chain dim 5: extra local
conserved charges exist. These are **genuinely distinct alternatives**,
not reparameterizations. A constant probe along the extracted TFIM
charge O₂ changes the unit-invariant normalized spectrum shape by
5.8e-2, while the unit-change probe leaves it unchanged to 1.6e-15.
**The GR-1 retained sector is free (phonons), so it falls in this
non-derived class.** An interacting (anharmonic) retained sector would
fall in the derived class.

**3. Without C_cons, nothing earned selects anything.** The
non-conserved coupling O = Σ Xᵢ changes the intrinsic spectrum shape
(7.5e-3), yet 𝔠_full admits it (Gram PSD) and G-2's hop geometry cannot
see it (identical interaction graph). C_cons is the only thing that
excludes it.

**4. Universality is derived exactly where sectors interact.** Two
generic chains coupled by a rung interaction (g = 0.3) leave only
H_total in the commutant (dim 1), so the clock coupling is forced to be
universal. Decoupled (g = 0), H_A and H_B are separately conserved
(dim 2), so C_cons allows ε_A ≠ ε_B.

**5. The discriminator the owner required.** It asks whether
non-universal clocks can hide behind a choice of units. The observable
is the cross-sector correlation ⟨Z_{a0}Z_{b0}⟩(t), with the best common
time rescaling optimized away.
- **Universal clocks** are indistinguishable from a unit change:
  Δ = 8e-14 (coupled) and 2e-14 (decoupled).
- **Non-universal clocks** are visible in the full accessible dynamics:
  Δ = 0.095 (coupled) and **0.118 (decoupled)**.

So for non-interacting sectors, non-universal clocks are invisible to
each sector's own internal data, *observable* by joint access, and
*not forbidden* by any earned constraint. **That is where Sel-4 is
irreducible**, and it is exactly the owner's quotient worry made
concrete: an observable set restricted to one sector would have defined
universality into existence.

## STRENGTH AND LIMITS (stated plainly)

- **C_cons carries all of the weight.** 𝔠_full and G-2 geometry are
  NULL throughout. The derived parts use standard physics:
  - the absence of extra local conserved charges in non-integrable
    chains;
  - the fact that interactions leave only the total energy conserved,
    the finite-system analogue of Weinberg's universality argument.

  By the program's redundancy rule these are **NULL-REDUNDANT as new
  principles.** Whether C_cons is legitimately "earned" is the owner's
  ruling. It was inherited from CP-1/EQ-1's acceptance of conservation.
  If it is not earned, every part of Sel-4 is IRREDUCIBLE.
- **The commutant scans are range-limited** (range ≤ 3 on L = 8;
  range ≤ 2 legs plus rungs on the ladder). "No other local charge" is
  established only within that basis.
- **The limit of vanishing interaction is singular.** Any g ≠ 0 forces
  universality algebraically, and g = 0 releases it. Small-g
  robustness, i.e. how weakly-interacting sectors behave on finite
  timescales, was not tested.
- **Scope:** finite spin chains; clock (temporal) parts only. The
  spatial part is carried from EQ-1 and was not re-tested.

## THE ARCHITECTURE STATEMENT (the owner's stakes, at recorded strength)

The owner asked what it would mean if Sel-4 were irreducible. The
answer is sharper than yes or no:

> Given conservation (C_cons), the program generates **clock
> equivalence for any sector that is generic and interacts**. It does
> **not** generate (a) why free/integrable sectors couple only through
> their energy, (b) **why sectors that do not interact with each other
> must share the same unit change**, or (c) the length part. Item (b)
> is the universality of free fall in its purest form, and on this
> record it is a genuine boundary of the theory.

## LEDGER AND FENCES

- **κ:** discharged (GR-1).
- **Minimal stress:** reduced to geometric coupling (CP-1).
- **Geometric coupling:** reduced to Sel-4 (EQ-1).
- **Sel-4 (S4-1):** split into
  - clock parts, derived-in-class given C_cons for generic, interacting
    sectors;
  - universality across non-interacting sectors, IRREDUCIBLE;
  - the length part, IRREDUCIBLE.
- **Retained sector:** untouched.
- **Class-4:** OPEN.

ω⁷ occupancy only. ℏ located. The GR-1 3D red stands. D = 4 TT/ξ,
operator ordering and geometry selection remain separate. No Einstein
equations were used.

## HARD STOP

Verdict recorded. The decisions this puts before the owner:
- **(1) The status of C_cons.** Is zero-momentum conservation earned,
  or itself an import? Everything derived here hangs on it.
- **(2) Next attack.** The candidates are:
  - universality across non-interacting sectors (the irreducible core);
  - the free/integrable class (which includes the GR-1 retained
    sector);
  - the spatial part of Sel-4.
- **(3) The separate forks** as before: retained sector, D = 4 TT/ξ,
  geometry selection.

The owner rules.
