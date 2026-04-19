# Contributing to GRUT-RAI

GRUT-RAI is a research codebase with a specific discipline: every
numerical output carries a status label, every claim has a test, and
every correction is documented. Contributions are welcome, but the
discipline isn't negotiable — it's what makes the framework trustworthy.

Read `ARCHITECTURE.md` before contributing code. Then read this.

---

## Before you start

1. **Run the tests**: `pytest tests/` should give 150/150 passing in
   under a second. If it doesn't, stop and diagnose.
2. **Read V7**: `theory/GRUT_V7.md` or `theory/GRUT_V7_FULL.md`.
   You should know what's COMPUTED, what's STRUCTURAL, what's
   CONDITIONAL, and what's HYPOTHESIS before you touch the code.
3. **Read the ledger**: `theory/derivation/*_LOG.md` shows the 12
   corrections caught during derivation. The project's credibility
   depends on continuing that pattern.

---

## What kinds of contributions are welcome

### Highly welcome

- **New sector implementations** that extend existing V8 tracks
- **Test coverage expansion** for underneath-tested modules
- **Performance improvements** to slow computations (profile first)
- **Documentation clarifications** that increase precision
- **Bug fixes** with regression tests locking the fix in place
- **Corrections to overclaims** — the most valuable kind of contribution

### Welcome with discussion

- **New API endpoints** — open an issue first so we can agree on shape
- **Dependency additions** — motivate why; prefer zero new deps
- **Refactors** — small and focused, not sweeping

### Not welcome

- **Overclaims** — don't upgrade a HYPOTHESIS to COMPUTED without derivation
- **Silent fixes to bugs that affected a published V7 claim** — document them
- **Scope creep in commits** — one commit, one logical change
- **Secret-embedding changes** — no API keys, no paths, no personal data
- **Removing tests** to avoid breakage — fix the code, not the test

---

## The status-label commitment

Every sector module's output must carry a `"status"` key with a correct
label:

| Label | When to use |
|:---|:---|
| DERIVED | The result is exact from published physics |
| COMPUTED | The result is calculated from first principles in the framework |
| STRUCTURAL | The form is constrained but numerical value isn't pinned |
| CONDITIONAL | Depends on a specific separate calculation not yet done |
| HYPOTHESIS | Conjectured; not yet tested |
| HONEST NEGATIVE | Tested and failed (e.g., lithium-7 BBN tension) |

**When you add a new prediction**, pick the label that matches the
actual epistemic state. If you're unsure, default to the stricter label
(HYPOTHESIS is safer than STRUCTURAL; STRUCTURAL is safer than COMPUTED).

**When you upgrade a label**, document the derivation that justifies
the upgrade. The commit message should say "Upgrade X from STRUCTURAL
to COMPUTED because [specific reason]."

**When a claim is wrong**, document it honestly. Not "fixed a bug" —
"Correction #N: claim X was wrong because Y; the correct value is Z,
with revised status W."

---

## Test discipline

### Every new function needs at least one test

If it's in `grut/derived/` or `grut/bridge/` or `grut/foundation/`,
it needs a test. No exceptions.

### Every V7 numerical claim needs a test

If V7 §X says "K = 2/3 to 0.005%," there should be a test that locks
that in with a 0.01% tolerance. If the value drifts in any future
refactor, the test catches it before it ships.

### Test tolerances

- **Central claims** (R_anomaly, Ω_Λ, η_B, K, M_dark, τ_0): 0.1% or tighter
- **Scaling laws** (m², l^N, etc.): factor-of-2 OK, exact when the law is exact
- **Structural tests** (does it return a dict? are expected keys present?):
  exact shape assertions

### Test readability

Each test should name the V7 claim it locks in. Good:

```python
def test_Koide_K_matches_2_over_3_to_percent(self):
    """V7 §29: Koide identity K = 2/3 to 0.005% for charged leptons."""
```

Bad:

```python
def test_koide_works(self):
    ...
```

---

## Commit message conventions

The project's commit history is part of its audit trail. Keep it honest.

### Format

```
<scope>: <what changed in one line>

<Detailed explanation>

<Why this change was needed>

<What tests/checks were run>

Co-Authored-By: ...
```

### Good example

```
foundation/anomaly: R_anomaly docstring updated to COMPUTED status

Primary-source audit (V7 §26.2, theory/derivation/PRIMARY_SOURCE_AUDIT.md)
confirmed R_anomaly = 1.15428 is computed from 3-loop CTP on S^4 with
no coupling inputs. Reverted the earlier "CONDITIONAL hand-constructed"
language throughout the docstring.

Tests: 22/22 still passing; no numerical values changed.
```

### Bad examples

- `Fix stuff` — no scope, no what-why
- `Update anomaly.py` — no why
- `Fixed a bug in R_anomaly` — if it affected a V7 claim, the bug needs
  to be flagged as a correction with its number and description

---

## The correction protocol

If you find an error in an existing claim:

1. **Don't hide it.** The project's value depends on catching errors
   in public.
2. **Document it as a numbered correction.** Search existing docs for
   "Correction #12" to find the current count, and add yours.
3. **Commit message should say**:
   - What was wrong
   - What the correct value/claim is
   - How you verified the correction
   - What downstream changes follow
4. **Update both code and docs** in the same commit (or adjacent ones).
   Don't leave V7 and the code saying different things.

Example:

```
Correction #13: S_CTP should be 108π, not 108 (missing π factor)

Discovered during dimensional-consistency audit of ui/api/routes.py
test. grut/foundation/anomaly.py:S_CTP already had the correct 108π
formula, but the UI was displaying 108 in the response. The test
`test_S_CTP_numerical_value` was passing because it used the same
wrong value from the UI.

Corrected:
  - ui/api/routes.py: now returns S_CTP = 108π ≈ 339.29
  - tests/foundation/test_foundation.py: tolerance tightened to 0.1%
  - No change to V7 docs (they always said 108π)

Tests: 150/150 pass.

Honesty ledger: 13 corrections caught, 0 hallucinations.
```

---

## Questions? Unsure?

Open an issue. Say what you're trying to do and why. The project's
discipline is collaborative — asking is always better than silently
getting it wrong.

---

*GRUT-RAI Contributing guide. Last updated: April 2026.*
