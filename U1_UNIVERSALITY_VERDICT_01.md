# U-1 — CAN CLOCK UNIVERSALITY FOR GENUINELY NON-INTERACTING SECTORS BE DERIVED? VERDICT

**Date:** 2026-09-25 · **Charter:** `U1_UNIVERSALITY_CHARTER_01.md`
(frozen at `f31ab7d` before the run) · **Authority:** GitHub Issue #2,
owner comment 5835886532 · **Instrument:** `calc/u1_universality.py` ·
**Artifact:** `U1_UNIVERSALITY_RESULT.json` (sha `72fa5e55ca16559d…`) ·
**Battery 23/23, zero failures, zero halts, single run, no defects.**
The halt-grade identities held: C_cons-compatibility 3.6e-15, the
universal-probe discriminator 1.8e-14, and the clock-only probe's
[H_A, H_full] = 8.9e-16.

## VERDICT

> **CLASS-SPLIT.**
> - **For genuinely non-interacting sectors, clock universality is an
>   IRREDUCIBLE INPUT.** Nothing earned forces it, and the supplied
>   gauge structure does not force it either.
> - **For sectors that exchange energy-momentum, it is
>   DERIVED-IN-CLASS, conditional on the supplied massless
>   gauge/Lorentz structure.** That includes exchange mediated by the
>   probe itself, whenever the probe carries non-conserved (T_xx-type)
>   components.
>
> **The residual is named exactly:** *whether every sector couples to a
> dynamical probe through exchange-carrying (non-conserved)
> components.* That is supplied.

## WHAT THE RUN SHOWED

**1. Genuinely decoupled sectors: nothing forces equal clocks.** At
g = 0, the non-universal clock coupling O = H_A + 0.6 H_B:
- is C_cons-compatible (commutator 3.6e-15);
- is 𝔠_full-admissible (Gram PSD);
- is invisible to G-2 hop geometry (graph unchanged);
- is a pure unit change *inside each sector* (spectrum shapes
  unchanged to ~1e-16).

Yet it is **observable by joint access.** The cross-sector correlation
differs by Δ = 0.049 even after optimizing the single common time
rescaling, while the universal coupling reads 1.8e-14. The only
units-fixing step was that one common rescaling. No per-sector
rescaling was allowed, because that would *be* the universality
assumption. No earned symmetry relates the two (different) sectors.
For identical sectors, swap covariance of the probe would force
equality only if it were supplied (the P-6 lesson).

**2. The supplied gauge structure forces equality only under
exchange.** This is the soft-emission gauge variation, D = 4, over 100
random configurations per class.
- **Class I, genuinely decoupled** (each sector conserves its own
  momentum): the variation is exactly 0 for κ_A ≠ κ_B. **Not forced.**
- **Class II, sectors exchange momentum:** the variation is ≥ 0.13 for
  κ_A ≠ κ_B, and ≤ 9e-16 for κ_A = κ_B. **Forced.**

This is Weinberg's soft-emission argument: standard, and NULL-REDUNDANT
as a new principle. Its content here is the exact boundary it draws:
gauge consistency needs a shared conservation law to act on, and
genuinely decoupled sectors don't have one.

**3. The probe can itself become the exchange channel.** Two sectors
and a dynamical probe oscillator, exact diagonalization (80-dim):
- **Coupled only through clocks** (O_s = H_s): [H_A, H_full] = 0
  (9e-16), and ⟨H_B⟩(t) is constant to 7.5e-15. The probe mediates
  *no* energy exchange, the sectors stay genuinely decoupled, and
  equality is **not** forced (class I).
- **Coupled through non-conserved components** (the T_xx type):
  [H_A, H_full] = 2.17, and ⟨H_B⟩(t) varies by 0.30. The probe **is**
  an exchange channel, the sectors now interact through it, and
  equality **is** forced (class II, given the supplied gauge
  structure).

GR-1's gravitational channel is exactly such a non-conserved T_xx
coupling. So any sector coupled to a probe of that kind is not
genuinely decoupled from the others, and universality follows,
conditionally.

**4. The g → 0 issue, tested separately as required.**
- ‖[O, H]‖/‖O‖ is **exactly linear in g** (deviation 6.5e-13): 2.09e-3,
  6.26e-4, 2.09e-4, and 0 at the endpoint.
- The observable non-conservation of the non-universal coupling is
  1.03e-2, 3.04e-3, 1.00e-3, and 0 at the endpoint, with log-slopes
  1.016 and 1.008.

C_cons forces universality exactly for any g ≠ 0. But the violation it
forbids is proportional to g, is visible only on timescales ~1/g, and
vanishes continuously. The "singularity" at g = 0 belongs to treating
C_cons as an exact constraint, not to the physics.

## STRENGTH AND LIMITS (stated plainly)

- **The gauge leg is linear algebra.** It is Weinberg's identity. The
  finite model cannot itself show gauge forcing: the forcing comes from
  the supplied structure applied to processes with exchange.
- **The "T_xx-type" probe in L-D is an analogue.** It is a
  non-conserved local coupling (ΣXᵢ), not the literal stress
  component. The claim it supports is structural: non-conserved probe
  couplings make the probe an exchange channel.
- **Dependency, stated:** the class-II derivation for gravity needs
  the probe to couple to each sector's **full** stress tensor,
  including the non-conserved components. That is part of the supplied
  massless spin-2 field structure, and its spatial form traces back to
  the Sel-4x/geometric-coupling chain, which is irreducible (EQ-1).
- **Scope:** finite sectors; D = 4 soft-emission algebra; a single
  non-universal ratio (0.6).

## THE ARCHITECTURE AFTER U-1

**Earned layer:** influence/access geometry. It forces nothing about
cross-sector clocks.

**Supplied probe field structure:** massless, gauge/Lorentz redundant,
coupled to the full stress tensor. This yields:
- (a) current conservation (C_cons, clock component), from CC-1;
- (b) clock universality for any sectors that exchange energy-momentum,
  including through the probe itself, from U-1.

**Irreducible residual:** a sector coupled to the probe *only* through
its conserved clock charge, with no exchange-carrying component, would
escape universality. So would a sector outside the probe's reach. On
this record, nothing earned forbids either.

## LEDGER

- κ discharged.
- Minimal stress → geometric coupling → Sel-4.
- Sel-4 clock component → C_cons → supplied massless gauge structure.
- Universality: CLASS-SPLIT, derived under exchange (conditional),
  irreducible for genuinely decoupled sectors.
- Sel-4x (length part): irreducible.
- GeoInv: unearned.
- Retained sector: separate.
- **Class-4: OPEN.**

ω⁷ occupancy only. GR-1 3D red. ℏ located. D = 4 TT/ξ, operator
ordering and geometry selection fenced.

## HARD STOP

Per the owner: hard stop after the universality verdict. The
irreducible core is now sharply localized. The remaining named supplied
structures are:
1. the probe's field content (massless, gauge/Lorentz redundant, full
   stress coupling);
2. universal reach, i.e. every sector couples through exchange-carrying
   components;
3. the length part, Sel-4x;
4. the retained-sector choice.

The owner rules.
