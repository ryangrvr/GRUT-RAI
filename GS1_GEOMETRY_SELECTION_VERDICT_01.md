# GS-1 — CAN GEOMETRY BE SELECTED FROM INFLUENCE/ACCESS DATA? VERDICT

**Date:** 2026-09-25 · **Charter:** `GS1_GEOMETRY_SELECTION_CHARTER_01.md`
(frozen at `7837fb2` before the run) · **Authority:** GitHub Issue #2,
owner comment 5837643174 · **Instrument:** `calc/gs1_geometry.py` ·
**Artifact:** `GS1_GEOMETRY_RESULT.json` (sha `a1a3fdf9da72b6b7…`) ·
**Battery 19/19, zero failures, zero halts.** Halt-grade identities
held: full-access reconstruction 2e-15, Y–Δ static identity 2e-16, and
the single-site family data identity 8e-14. One labeled post-hoc
diagnostic **corrects the reading** of a reported (ungated) quantity.
It is stated below.

## VERDICT

> **CLASS-SPLIT by access. The owner's bar is met.** Influence/access
> data **eliminate genuinely different geometric candidates**, but only
> as far as access reaches:
>
> | Access | Result |
> |---|---|
> | full site-resolved | **SELECTED-IN-CLASS** (unique up to relabeling); even an isospectral candidate is eliminated |
> | boundary (multi-site), dynamic | **the dynamic hierarchy eliminates Δ**, which static data cannot; the interior geometry remains CONSTRAINED-NONUNIQUE |
> | boundary, static only | **Y–Δ blind**: G-2's resistance geometry alone is insufficient |
> | single site | **UNDERDETERMINED**: a non-isometric family with identical data survives every earned test |
> | topology | invisible below the circumference order (the horizon, carried) |
>
> Geometry is **not** derived as an absolute. It is determined **exactly
> as far as access reaches**, and the access boundary itself is supplied
> (P-5, P-6).

## WHAT THE RUN SHOWED

**1. Full access selects, and more than global spectra can.** A 3×3
grid's full site-resolved response reconstructs it exactly. This is
machinery, not the finding. The finding: an **isospectral** candidate,
whose global trace moments match the grid's to 2e-16 at every order
tested, is **eliminated** by the site-resolved data (difference 1.59).
A degree-preserving rewire is eliminated too (0.52; its global spectra
first differ at trace order 3). Local access selects geometry that
global spectral data cannot.

**2. Static geometry is not enough; the dynamic hierarchy is.** On the
boundary {a, b, c}, a hidden Y network and its star–mesh Δ have
**identical static data** (2e-16). **G-2's resistance geometry cannot
tell them apart.** The dynamic influence data separate them (49.7 at
ω = 0.3). The first distinguishing invariant is the **ω² coefficient**
of the boundary response: order 0 agrees to 4e-16, and order ω² differs
by 0.1975, exactly the analytic ‖K_AI K_II⁻² K_IA‖. The dynamics detect
the interior node's inertia. **This is an earned elimination of a
genuinely different geometry**, and it is new relative to G-2.

**3. Single-site access leaves a non-isometric family (G-2's collapse,
carried).** All 3600 interior rotations of the hidden path produce
identical single-site data (8e-14). They are genuinely different graphs:
at θ = 0.4, site a couples to both interior nodes. They are all
𝔠_full-admissible.

**4. The passivity candidate (LocPos) does not rescue single-site
selection, and the frozen mechanical line overstates it.**
- *As frozen and reported:* only θ = 0 was LocPos-admissible, so the
  frozen rule emitted *"selected only by LocPos (candidate)."*
- **Labeled post-hoc diagnostic:** the hidden path has zero interior
  pins, which puts it exactly on the LocPos boundary. With interior
  pins of 0.1, LocPos admits 96 members, **94 of them non-isometric**
  (a band θ ≈ 0.002–0.083).
- **Corrected reading:** the apparent LocPos uniqueness was a boundary
  artifact of the chosen hidden network. **LocPos narrows the family but
  does not select a unique geometry in general.**
- The mechanical line stays recorded as emitted, with this correction
  beside it.

**5. Topology stays behind the horizon.** The prism and Möbius ladders
have local closed-walk counts that agree as exact integers below order
8 and first differ at **order 8 = n**, as predicted. This is the same
invariant-order ladder as G-2's C40/C80.

## STRENGTH AND LIMITS (stated plainly)

- **The machinery is standard:** inverses, Schur complements, walk
  counts and spectral matching (NULL-REDUNDANT). The findings are the
  eliminations and non-eliminations.
- **The hidden networks generated the data.** The tests ask what the
  data rules out; they never feed a K into a reconstruction as input.
- **The full-access selection is up to relabeling,** since site labels
  come from the access declaration.
- **Scope:** small quadratic (Gaussian) networks, where the two-point
  data are the full hierarchy (P-4). Non-Gaussian sectors could carry
  more.
- **The interior-rotation family is one explicit non-uniqueness
  mechanism.** It is not an exhaustive classification of the
  single-site realizations.

## LEDGER

- **κ:** discharged.
- **C_cons:** irreducible, reduced to the supplied massless
  gauge/Lorentz probe.
- **Universality:** derived under exchange; universal reach supplied.
- **Retained sector:** conditional on CARRIER plus the supplied probe;
  the class is selected.
- **CARRIER:** an access-seed coincidence, supplied.
- **Geometry:** CLASS-SPLIT by access. It is selected under full access
  (up to labels); the dynamic hierarchy beats static geometry under
  boundary access; it is underdetermined under single-site access; the
  topological horizon stands. The access boundary is supplied.
- GeoInv and Sel-4x unearned. LocPos is a candidate that narrows but
  does not select. **Class-4 OPEN.**

ω⁷ not used. GR-1 3D red. ℏ located. D = 4 TT/ξ and operator ordering
fenced.

## HARD STOP

Per the owner: hard stop after the geometry verdict. Geometry is now
classified: **access-relative, not absolute**, with the dynamic
hierarchy as the earned element that goes beyond G-2's static geometry.
That meets the owner's gate for D = 4 TT/ξ or Sel-4x when the owner
rules.
