# Priority 1b rerun — passive Lorentz oscillatory kernel

**Date:** 2026-08-23 · JSON: `PRIORITY1B_RERUN.json` (authoritative). No banking.

## Outcome: **A — the passive oscillatory response crosses**

Prior verdict RESTORED, now resting on an admissible object. The prior cos-kernel result is
moved to an inadmissible-kernel test case and is not evidence.

## Convention anchoring (ADD-2, done first)

Registered single-pole Debye run through the passivity test under the frozen convention:
min Im χ = +0.009999 > 0 → **passive; convention frozen**. (Had it failed both ways: STOP.)

## Three kernels, same map, same frozen criterion

| kernel | passive | KMS gate | elastic framing | dissipative framing |
|---|---|---|---|---|
| registered Debye (control) | ✓ | ✓ passed | APPROACH | APPROACH |
| **cos-kernel (prior run)** | **✗ INADMISSIBLE** | ✓* | APPROACH | "crossing" ← from ACTIVITY |
| **PASSIVE LORENTZ** (γ=0.5, ω₀=2) | ✓ | ✓ passed | **TRUE CROSSING** | APPROACH |

*KMS gate passes trivially for FDT-constructed noise; its substantive content here is the
positivity of Im χ, which is exactly what the cos-kernel fails.

## The exact mathematical condition responsible

- cos-kernel χ ∝ ½[1/(γ−i(ω+Ω)) + 1/(γ−i(ω−Ω))]: Im χ goes NEGATIVE above resonance — an active
  medium supplying energy. Its crossing came from **activity**, which GRUT's positivity axiom
  independently forbids.
- Lorentz χ = ω₀²/(ω₀²−ω²−iγω): Im χ = γω₀²ω/denominator > 0 ∀ω>0 (strictly passive), Re χ
  changes sign at ω=ω₀ — a genuine resonant dispersion inside the probed band [1, 3.9].
  Its crossing comes from **resonant elastic dispersion**, fully admissible.

## [ADD-3] checked, not assumed

GRUT's DOS/super-Ohmic argument (J~ω³) constrains LOW-ω scaling only. A finite-frequency
resonance ω₀ is NOT excluded by it. However, no known vacuum ingredient supplies such a mode —
the register's own §2.3 records that the finite-T factor "could have manufactured a slow second
pole and does not." So the oscillatory family is **unexcluded but unsupplied**: admissible within
the constraint set, absent from the derivation set. This is a third reading beyond A/B/D and it
is the one that holds: the no-crossing is definition-as-target at the single-pole level *unless*
rung3's microscopic calculation independently derives pure-relaxation structure.

## Final state of the three claims

| claim | status |
|---|---|
| finite memory does not imply no crossing | **TRUE** (Lorentz has finite memory AND crosses) |
| single-pole ⇒ observable distinction | UNSUPPORTED (Category 3 empty) |
| purely-relaxational ⇒ no-crossing | TRUE within the tested family |

**Correction applied (18th defect, wording):** the earlier "iff" phrasing over-reached —
the tested Lorentz resonance produces a crossing and the tested real-pole relaxors do not;
an iff theorem over the full admissible space was NOT established. Earned statement:
*within the tested response family, the crossing is associated with a sign change in Re χ,
which the passive Lorentz resonance supplies and the tested positive real-pole relaxors do not.*

## Defect ledger

Seventeenth defect closed out: the crossing result previously reported rested on an inadmissible
kernel; the passivity table entry was wrong for the kernel named. Root cause: admissibility was
asserted rather than gated per-kernel before phenomenology. Repair: convention anchored first,
every kernel gated (passivity grid + KK residual + kms.gate) before entering results. The
surviving finding — real relaxational modes don't cross — is unaffected (those kernels were
genuinely passive).