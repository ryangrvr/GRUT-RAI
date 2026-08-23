# R3 forensic — CORRECTION

> Supersedes the conclusion of `provenance/R3_FORENSIC_RESULT.md`. That file is left
> untouched: it is the record of what was concluded, and the correction is a separate
> citing file per the program's own pre-registration discipline.
>
> **NOTHING BANKED.** `provenance/claims.json` untouched. Three code fixes applied, each
> verified by re-execution; all are calc-layer defects in CHECKS, not in physics.

## 1. The forensic conclusion was wrong, and its own number shows it

`R3_FORENSIC_RESULT.md` states: *"The control implementation successfully integrated the
canonical equation … giving |v(-1)| = 1.000005 (stable across step counts). This proves:
… **The ICs are correct** … The earlier 10^17 blow-up was an implementation defect in the
specific `class_c_stage_c1.py` code path."*

**`|v(-1)| = 1.000005` is the signature of the BUGGY seed, not evidence against it.**

| seed | \|v(-1)\| | rel err | stable across 50k/100k/200k steps |
|---|---|---|---|
| analytic truth | 1.000000 | — | — |
| as coded (buggy) | **1.000005** | **1.483** | yes — identical at all three |
| corrected | 1.000000 | **8.3e-11** | yes |

The control tested **magnitude**. The two independent solutions of v'' + (k² − 2/η²)v = 0
share magnitude in the subhorizon regime, so a magnitude test cannot separate them. The
as-coded seed is nearly **antiphase**: arg(numeric) = −2.8272 rad against
arg(analytic) = +1.7854 rad, a 4.61 rad error. **The check could not fail in the direction
that mattered** — the failure class this program already names.

## 2. Root cause: the seed derivative, in `C1_GROUND_TRUTH_MODE.py`

For v = (1 − i/(kη))·exp(−ikη)/√(2k),

    dv/dη = exp(−ikη)/√(2k) · [ i/(kη²) − i k (1 − i/(kη)) ]

verified symbolically (`sympy.diff(v,eta) − this = 0` exactly). The code seeded with
`1j*k*(1 - 1j/(k*eta0)) - 1/(k*eta0**2)` — **sign flipped** on the dominant term and
**missing the factor i** on the 1/(kη²) term. Fixed; `C1_GROUND_TRUTH_MODE.py` now reports
**ALL PASS (5/5)**, R3 at rel = 8.33e-11.

## 3. The blamed file did not carry this defect, and has no integrator

`class_c_stage_c1.py` contains no integration path at all — only `eta`, `u`, `mu`. Nothing
in it can produce a 10^17 blow-up, and the planned remedy ("replace its integration path
with the proven control") **has no target**. Its two real failures are of a different
character, and both are defective CHECKS over correct physics:

- **C1.3** integrated `2|u|² dk` — a log-divergent quantity, ln(60/20) = 1.0986 — against a
  `want` that is quadratic in k. Two different objects. Restoring the 3D mode measure gives
  **324.45 vs want 324.23, rel 6.9e-4**. *Flagged for the author:* the factor (2/π²)
  reproduces the stated `want`, but the standard ⟨h²⟩ = ∫k²dk/(2π²)·2|u|² differs by 4, so
  the normalisation convention of `u` should be confirmed. The dimensional defect is fixed
  either way.
- **C1.4** tested the canonical variable μ = a·u against the STRAIN's frozen value.
  Superhorizon the strain freezes while μ grows as a: |μ|²/want = **403.4292** against
  e^{2t} = **403.4288** — the discrepancy *is* the scale factor, exactly — while
  |u|²/want = **1.0000009915**. The label "canonical amplitude freezes" was itself wrong
  physics. Now tests the strain and says so.

`class_c_stage_c1.py` now reports **3/3 passed**.

## 4. What this changes for the next session

The plan recorded in `R3_FORENSIC_RESULT.md` — *replace `class_c_stage_c1.py`'s integration
path with the proven control, then rerun the five C1 gates* — would have installed a control
carrying the wrong seed into a file that has no integration path, to fix a defect that lived
in a third file. All three C1-layer defects are now fixed and re-executed. **What remains
genuinely open is unchanged: the TT quarantine and the Class-A suspension are decisions about
physics, and nothing here touches them.**

## 5. Standing note

Three separate checks in this layer passed or failed for reasons unrelated to what they were
testing (a magnitude test blind to phase; a log compared to a quadratic; a growing variable
compared to a frozen value). None was a physics error. The common shape is a check whose
comparand does not match its target's type — which no amount of re-running catches, because
re-running reproduces it exactly. That is the same defect class as the assert-and-check
observation already recorded against the calc layer.
