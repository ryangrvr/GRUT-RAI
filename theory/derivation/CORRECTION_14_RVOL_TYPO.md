# Correction #14 — R_vol = 1.5428 was a typo of R_anomaly = 1.15428

**Date:** April 2026
**Status:** Typo identified, corrected, blast radius confirmed non-critical.

## The catch

During the N_total derivation attempts (`N_TOTAL_APPROACH_2.md`), approach
#4 found that `329/215 = 1.5302` is within 0.82% of a hardcoded constant
`R_vol = 1.5428` in `grut/derived/cosmology/vacuum.py`. The closeness
suggested a structural relationship worth hunting for.

On closer inspection:

```
R_anomaly = 1.15428   (3-loop CTP on S⁴, V7 §26.2 — fully derived)
R_vol     = 1.5428    (hardcoded in vacuum.py, no derivation visible)
```

**The digits 5-4-2-8 are identical.** Only difference: a missing leading
`1` in R_vol.

Two independent fundamental constants of a theory sharing four consecutive
digits has vanishing prior probability. **R_vol = 1.5428 was a typo of
R_anomaly = 1.15428** — someone dropped a '1' while hardcoding.

## The smoking-gun disclaimer

V7 `GRUT_V7_FULL.md` line 1108 contained:

> Note: R_anomaly = 1.15428 is the anomaly ratio. R_volumetric = 1.5428
> is a different quantity (the volumetric ratio in the cosmological map).
> These are NOT the same and must not be confused.

This disclaimer is the fingerprint of the typo's propagation: someone
noticed the digit similarity during editing and defensively added the
"these are NOT the same" note rather than investigating whether
R_volumetric was actually a distinct concept. **No structural derivation
of R_volumetric exists anywhere in V7 or the codebase.**

The disclaimer tried to paper over the confusion. Correction #14 fixes
the underlying cause.

## Locations of the typo

| File | Line | Status |
|:---|:---:|:---:|
| `grut/derived/cosmology/vacuum.py` | 51 | FIXED — uses R_ANOMALY constant |
| `ui/static/viz/viz.js` | 383 | FIXED — uses R_ANOMALY = 1.15428 |
| `theory/GRUT_V7_FULL.md` | 593 (parameter table) | FIXED |
| `theory/GRUT_V7_FULL.md` | 1108 (disclaimer) | SUPERSEDED with correction note |
| `theory/derivation/N_TOTAL_APPROACH_2.md` | (documentation of the hunt) | Preserved as audit trail |

## Blast radius — non-critical

The typo appeared only in `era_map()`'s sigmoid sharpness:

```python
k = 2 * π / (R_vol - 1)  # was: 2π/0.5428 = 11.58
                          # now: 2π/0.15428 = 40.73 (3.52× sharper)
```

**Effect on era map:**
- Old k = 11.58: sigmoid transitioned over ~4 eras
- New k = 40.73: sigmoid transitions in essentially 1 era (step function)

**Effect on main cosmological prediction:**
- Ω_Λ = 0.6904 at H_0 = 70 km/s/Mpc: **UNCHANGED** (uses R_ANOMALY directly, not R_vol)
- H_inf = 1.885 × 10⁻¹⁸ Hz: **UNCHANGED**
- H_0 first-principles prediction = 69.03 km/s/Mpc: **UNCHANGED**
- All 173 tests pass after the fix.

The typo was contained in a non-critical exploratory code path. The
main V7 §26 predictions were never affected.

## What this refutes

**Approach #4 in N_TOTAL_APPROACH_2.md is definitively RULED OUT.**

The "near-miss" structural relationship `N_total/N_threshold ≈ R_vol`
(0.82% off) was hunting for a physical origin of a keystroke error.
329/215 = 1.5302 was being compared to 1.5428 (a typo) — the 0.82% gap
wasn't a perturbative correction, it was the distance between a real
ratio and a corrupted constant.

There is no structural relationship `N_total = N_threshold × R_vol`
because R_vol doesn't exist as a distinct physical quantity.

## What this does NOT refute

**H_0 = 69.03 km/s/Mpc one-parameter prediction**: UNCHANGED. This
uses R_ANOMALY and observed age; doesn't depend on R_vol.

**Ω_Λ = 0.6886 at 0.04% from Planck (V7 §26.2)**: UNCHANGED. Uses
R_ANOMALY directly.

**The overall H_0 prediction chain**: still requires either R_vol
clarification (now closed — R_vol doesn't exist) OR Ω_dm from Track
VII. Path A is dead; Path B is the remaining route to zero-parameter.

## Test regression

Added a regression test in `tests/derived/test_cosmology.py`:

```python
def test_no_R_vol_typo(self):
    """Correction #14: ensure era_map doesn't re-introduce the typo."""
    import inspect
    src = inspect.getsource(vacuum_module.era_map)
    assert "1.5428" not in src
    assert "R_ANOMALY" in src
```

This ensures future refactors don't re-introduce the typo.

## Honesty ledger

**14 corrections caught, 0 hallucinations.**

This catch went deeper than all the previous ones. Correction #11 was a
structural misidentification (matching convention). Correction #12 was
a documentation claim (99 = d.o.f. count). **Correction #14 is a
keystroke that masqueraded as a fundamental constant, survived code
review, was defended by a disclaimer in the theory document, and nearly
spawned a derivation program trying to explain its origin.**

The type of error that historically kills frameworks — not because the
physics is wrong but because a wrong number propagates through code and
papers, gets defended as "a different quantity," and then someone tries
to publish it.

Caught in the session. 173 tests pass after fix. Ledger clean.

## Path forward

With R_vol revealed as a phantom:

- **Approach #4** (N_total = N_threshold × R_vol): RULED OUT
- **Approach #6** (Ω_b + Ω_dm bridge): now the cleanest remaining path

To get a zero-parameter H_0 prediction, V8 Track VII (dark sector
completion) must compute Ω_dm from freeze-out. GRUT's baryogenesis sector
already gives Ω_b = 0.053 (within 9% of Planck). If Ω_dm can be derived
with similar precision, Ω_m = Ω_b + Ω_dm becomes COMPUTED and H_0 follows
from H_inf via flat ΛCDM Friedmann.

That's the real path. No shortcuts via phantom constants.
