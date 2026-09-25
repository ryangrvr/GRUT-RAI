# RS-1 — IS THE GAPLESS PHONON SECTOR SELECTED, OR MERELY CHOSEN? VERDICT

**Date:** 2026-09-25 · **Charter:** `RS1_RETAINED_SECTOR_CHARTER_01.md`
(frozen at `1f18205` before the run) · **Authority:** GitHub Issue #2,
owner comment 5837437988 · **Instrument:** `calc/rs1_retained.py` ·
**Artifact:** `RS1_RETAINED_RESULT.json` (sha `45e12855a539ccc7…`) ·
**Battery 27/28.** The one failure is a frozen gate preserved red,
because my prediction for it was wrong; a labeled diagnostic
characterizes it. Zero halts. The exact ring identity held to 7e-13,
the Lindhard density-of-states limit held to 0.01%, and FS-1's tower
was reproduced. **ω⁷ was never consulted.**

## VERDICT

> **CLASS-SPLIT across layers. The owner's bar is met, conditionally.**
>
> - **Earned layer**, conditional on the declared bridging premise
>   **CARRIER** (*the retained sector is the one whose local static
>   response carries the G-2-recovered additive metric*): it
>   **eliminates two genuinely different gapless candidates**, free
>   fermions under local access and the flexural chain, plus the
>   gapped control. Survivors: {phonon, ferromagnetic magnon}.
>   **CONSTRAINED-NONUNIQUE.**
> - **Earned + supplied probe structure** (a massless spin-2 probe
>   needs an IR boost-compatible symmetric stress): the magnon is
>   eliminated. Survivor: **{phonon}**. **SELECTED-IN-CLASS, relative
>   to the tested candidate set.**
> - **Stress coupling:** the gauge structure **permits** full-stress
>   coupling but **does not force** it (nullity 2: canonical plus the
>   ξ-improvement term).

**What is actually selected is a class, not "the phonon".** The class
is gapless, with linear infrared dispersion (z = 1), and a locally
accessible Goldstone field (static response ~ 1/q²). The phonon is its
representative in the tested set. Any sector in that class (for
example a Luttinger liquid accessed through a local bosonic field)
would pass the same selectors.

## WHAT EACH SELECTOR DID

| Candidate | Additivity A = R(0,16)/R(0,8) (earned, given CARRIER) | IR v_g·v_p ratio (supplied) | Status |
|---|---|---|---|
| **P** phonon | **1.936** (additive) | **0.999** (boost-compatible) | **survives both** |
| **M** magnon (z = 2) | 1.936 (additive) | 3.993 (∝ k²) | eliminated by the supplied layer |
| **F** free fermions | 1.020 (saturating, local density) | 0.995 | eliminated by the earned layer (local access) |
| **B** flexural (z = 2) | 3.744 (N-dependent) | 3.993 | eliminated by both |
| **G** gapped control | 1.019 (screened) | 0.999 | eliminated by the earned layer |

**The fermion elimination is access-relative.** The fermions' non-local
bosonized phase field is additive (A = 1.896): it passes. It is the
local access of G-2 that excludes them. This is the same
access-relativity found in P-5, G-1 and G-2.

**Gaplessness is now partly grounded, given CARRIER.** The gapped
control fails the additive-metric requirement (it is screened at long
range). So "gapless" is no longer a bare choice. It follows from
requiring that the bath carry the recovered long-range geometry.

## THE RED GATE, PRESERVED

**Frozen gate:** "flexural A > 4 (cubic growth)." **FAILED at 3.744**
and stays red. **Labeled diagnostic:** A matches the exact ring form
d²(N−d)² (ratio 3.746). The 1/q⁴ kernel gives R ~ N·d², which is
quadratic and system-size dependent (R(0,8) grows 2.06× from N = 256
to 512), not the cubic growth I predicted. The flexural sector is still
eliminated, because the frozen adjudication uses the additivity window
[1.8, 2.2] and B sits at 3.74. The diagnostic shows it fails even
harder than predicted: it carries no local metric at all.

## STRENGTH AND LIMITS (stated plainly)

- **CARRIER is load-bearing and not earned.** Without it, the earned
  layer eliminates nothing: every candidate is 𝔠_full-admissible and
  locally recoverable. CARRIER identifies the gravitational bath with
  the carrier of the recovered geometry. It is the natural bridge, but
  it is a new named premise, not a result.
- **The supplied layer does the final cut.** The magnon falls to the
  supplied Lorentz/gauge probe structure (CC-1's dependency), not to
  anything earned.
- **Finite candidate set.** Five sectors were tested. "Selected" means
  selected relative to them, and the selection identifies the class
  (gapless, z = 1, local Goldstone), not a unique microscopic model.
- **All statements are infrared.** The lattice phonon's boost
  compatibility holds only as k → 0.
- **Per-sector v = c is a units choice.** Cross-sector light cones are
  U-1 territory.

## LEDGER

- **κ:** discharged.
- **C_cons:** irreducible, reduced to the supplied massless
  gauge/Lorentz probe.
- **Universality:** derived under exchange; irreducible for decoupled
  sectors; universal reach supplied.
- **Retained sector:**
  - *given CARRIER:* the class is constrained to {phonon, magnon};
  - *given CARRIER plus the supplied probe structure:* selected-in-class
    as gapless, z = 1, local Goldstone, with the phonon as
    representative;
  - *stress coupling:* permitted, not forced.
- GeoInv and Sel-4x unearned. **Class-4 OPEN.**

ω⁷ occupancy only, never used to select. GR-1 3D red. ℏ located. D = 4
TT/ξ, operator ordering and geometry selection fenced. The FS-1 tower
and dynamic insensitivity are preserved.

## HARD STOP

Per the owner: hard stop after the retained-sector verdict. The
decisions this puts before the owner:
- **(1) The status of CARRIER.** It is the one new premise, and it is
  what connects the earned geometry to the bath.
- **(2) The next fork:** attack CARRIER, geometry selection, the D = 4
  TT/ξ question, or the length part (Sel-4x).
