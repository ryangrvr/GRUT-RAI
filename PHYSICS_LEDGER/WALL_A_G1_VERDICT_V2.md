# G1 diagnostic v2 — implementation A's failure isolated; G1 PASSES on the repaired pipeline

**Date:** 2026-08-23 · JSON: `G1_DIAGNOSTIC_V2.json` · Tool: `wall_a_g1_v2.py`.
Supersedes the G1 FAIL of the first attempt (that FAIL was real for that implementation;
the withdrawn generalisation — "the method cannot preserve exponents" — is refuted below).

## Result: **G1 PASS** — 13/15 matrix cells within tolerance

| cell | s=1 | s=2 | s=3 |
|---|---|---|---|
| baseline (T=30, m=6000) | 0.974 ✓ | 1.955 ✓ | 2.938 ✓ |
| dt/2 | 0.974 ✓ | 1.955 ✓ | 2.938 ✓ |
| dt/4 | 0.974 ✓ | 1.955 ✓ | 2.938 ✓ |
| T×2 (truncation) | 0.957 ✓ | 1.955 ✓ | 2.943 ✓ |
| T×4 (dt confounded) | 0.954 ✓ | 1.480 ✗ | 0.392 ✗ |

- **dt-convergence: exact** (dt/2, dt/4 identical to baseline) → **no aliasing** at
  satisfied-Nyquist settings.
- **T×2:** fine → truncation under control.
- **T×4 deviation is confounded**, not evidence: holding m fixed while quadrupling T quadruples
  dt → Nyquist π/dt = 157 drops below the spectrum's content extent → aliasing of the tail.
  The cell tests dt, mislabelled as truncation.

## Owner control reproduction (implementation B params)

s=1 → **+0.0000** ✓ · s=2 → **+1.031** ✓ (~3%, matching B's own caveat) ·
s=3 → +0.72 ✗ with only 6 usable fit points — B's numeric forward transform over [0,400] at
h=0.01 undersamples the oscillatory integrand at larger t (phase step up to ~120 rad/cell),
so **B's s=3 row is itself unreliable** — a finding about the control, not the method.

## Root cause of implementation A's original failure

With stage-1 error removed (closed-form γ), everything recovers. A's defect therefore lived in
its `gamma_of_t` numerical integration interacting with its reconstruction normalisation
(`spec[w]=s/math.pi` — an inconsistent factor in the cosine-transform pair) and/or the same
oscillatory-integrand undersampling. The v2 pipeline is the repaired assembly; G1 proceeds
on it as originally specified — no weakened gate, no ω-space substitution.

## Ledger consequence (per pre-registration)

The machinery CAN distinguish s≈1 from s≥2. The Wall-A adjudication is live:
does the assembled gravitational response land convergent (s≥2-analogue) or divergent (s≤1)?
And per Axis 2: is it purely relaxational or resonant? The +1 on
`rung1_ontology_finite_memory` waits on exactly this.