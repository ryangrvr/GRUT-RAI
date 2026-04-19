# GRUT-RAI Architecture

This document describes how the GRUT-RAI codebase is organized, the
layering principles behind it, and how to add new sectors as V8 tracks
mature. Read this before contributing to V8 work.

---

## The three-layer model

```
┌─────────────────────────────────────────────────────────────────┐
│  ui/                     Flask dashboard, AI chat, API routes   │
│  ├── app.py              Flask entry point                       │
│  ├── api/routes.py       REST API for foundations, sectors, etc. │
│  ├── ai/chat.py          Claude integration with computation tools│
│  └── static/             HTML, JS, CSS for the frontend          │
└─────────────────────────────────────────────────────────────────┘
                               ▲
                               │  calls into
                               │
┌─────────────────────────────────────────────────────────────────┐
│  grut/derived/           Sector-by-sector physics predictions    │
│  ├── cosmology/          Omega_L, Hubble tension, spectral index │
│  ├── decoherence/        Lambda_grav, competition, isotope tests │
│  ├── dark_matter/        U(1)_dark sector (Routes 1 & 2)         │
│  ├── baryogenesis/       eta_B via R_B anomaly ratio             │
│  ├── koide/              K = 2/3 mass formula                    │
│  └── quantum_gravity/    4/8 closure ladder                      │
│  grut/bridge/            Cross-sector bridge (tau_0)             │
└─────────────────────────────────────────────────────────────────┘
                               ▲
                               │  calls into
                               │
┌─────────────────────────────────────────────────────────────────┐
│  grut/foundation/        CTP axioms, constants, noise kernel     │
│  ├── constants.py        Physical constants (G, hbar, M_Planck…) │
│  ├── axioms.py           A0, A1, N0 — the CTP axioms             │
│  ├── constitutive.py     tau dz/dt + z = z_target                │
│  ├── noise_kernel.py     Diósi-AH noise kernel, Lambda_grav     │
│  ├── anomaly.py          3-loop anomaly: C_FINAL, R_anomaly      │
│  ├── anomaly_derived.py  1-loop Birrell-Davies baseline          │
│  └── way2_*.py           Osborn epsilon independent confirmation │
└─────────────────────────────────────────────────────────────────┘
```

**The rule**: higher layers depend on lower layers; lower layers never
import from higher layers. `grut/foundation/` never imports from
`grut/derived/` or `ui/`. This keeps the core calculation-engine
small, pure, and testable.

---

## Status-label discipline (critical)

Every numerical output in GRUT-RAI carries a status label. When you
add new code, label correctly. The discipline is what separates
GRUT's ledger from the overclaim failure modes that kill frameworks.

| Label | Meaning | Example |
|:---|:---|:---|
| DERIVED | Exact from published physics | Lambda_grav = Gm²S(l/R)/ℏl (Diósi-AH) |
| COMPUTED | Calculated from first-principles CTP construction | R_anomaly = 1.15428 (3-loop CTP on S⁴, V7 §26.2) |
| STRUCTURAL | Constrained by symmetry/topology but not numerically determined | f(R) = 2-R form, before numerical verification |
| CONDITIONAL | Depends on a separate calculation not yet complete | eta_B depends on baryonic-anomaly 3-loop |
| HYPOTHESIS | Conjectured, not yet tested | n_s = 0.9649 from constitutive dissipation |
| HONEST NEGATIVE | Tested and failed | Lithium-7 tension (+15%) |

**Never upgrade labels silently.** If you compute a HYPOTHESIS into
STRUCTURAL or STRUCTURAL into COMPUTED, note the transition in the
commit message and in the relevant docstring.

**Never downgrade labels silently either.** The "CONDITIONAL" reversal
of R_anomaly in April 2026 was caught and reverted via primary-source
audit — a documented event in the project history. See the session
log in `theory/derivation/PRIMARY_SOURCE_AUDIT.md`.

---

## How to add a new sector (V8 tracks)

When a V8 track matures enough to go from STRUCTURAL to COMPUTED,
here is the process:

### 1. Create the module

```
grut/derived/my_sector/
├── __init__.py
├── core.py         # Main calculation functions
└── crosscheck.py   # Comparison to observation
```

### 2. Follow the existing pattern

Each sector module should expose:

- A main compute function returning a `dict` with explicit keys
- Every numerical output carries a `"status"` field with the correct label
- A standalone self-test (optional) that prints the key numbers

Example from `grut/derived/cosmology/vacuum.py`:

```python
def vacuum_prediction(H_0_kms=70.0, R_choice="hand"):
    """Cosmological prediction.

    Args:
        H_0_kms: Hubble constant in km/s/Mpc.
        R_choice: "hand" for R_ANOMALY = 1.15428 (primary computation, ...).
    """
    # ... calculation ...
    return {
        "H_inf_Hz": H_inf,
        "Omega_Lambda": OL,
        "Planck_OL": 0.6889,
        "deviation_pct": (OL/0.6889 - 1) * 100,
        "R": R,
        "f_R": 2 - R,
        "status": "COMPUTED — ..."
    }
```

### 3. Write the tests FIRST

Every new sector needs a `tests/derived/test_my_sector.py` file.
Pattern:

```python
class TestMyPrediction:
    def test_returns_expected_keys(self):
        result = my_function()
        expected = {"key1", "key2", "status"}
        assert expected.issubset(result.keys())

    def test_key_V7_claim(self):
        """V7 §XX: the specific numerical claim."""
        result = my_function()
        assert abs(result["value"] - EXPECTED) < TOLERANCE
```

Every major numerical claim gets a test. If V7 says "M = 2.1 × 10⁹ GeV"
there should be a test locking that in. This is how we catch regressions
across V8 evolution.

### 4. Wire into the UI

Add to `ui/api/routes.py`:

```python
@api.route('/my_sector')
def get_my_sector():
    from grut.derived.my_sector.core import my_prediction
    return jsonify(my_prediction())
```

Add to `ui/ai/chat.py` tool list so the AI can call it.

### 5. Document in theory/

Add a section to the appropriate V7 appendix (or V8 if sector is new),
and update the cross-references in `theory/derivation/` with a log of
how the sector was derived.

---

## Patterns and conventions

### Module docstrings

Top of every module file should state STATUS in plain language,
referencing V7 sections:

```python
"""
Sector Name — Brief description.

STATUS (per V7 §XX.X):
    MainQuantity: COMPUTED. Specific claim and precision.
    SubQuantity: STRUCTURAL. What's needed to upgrade.

Cross-reference: theory/derivation/RELEVANT_LOG.md
"""
```

### Function return dicts

Prefer `dict` returns with explicit keys to bare tuples or floats.
Makes UI wiring trivial and tests self-documenting.

### No dynamic imports in hot paths

Keep imports at the top of files, not inside functions, unless there's
a specific reason (e.g., avoiding circular imports between `foundation`
and `derived`).

### Constants live in `grut/foundation/constants.py`

Don't hardcode G, ℏ, M_Planck, α_EM in sector modules. Import from
constants. This is enforced by the dimensional-consistency tests in
`tests/utils/test_utils.py`.

---

## Testing conventions

### Run before committing

```bash
pytest tests/                 # should be 150+ tests, all green
```

### Write tests that are readable

Every test should read like a V7 claim. Good:

```python
def test_H_inf_is_1p885e_minus_18_Hz(self):
    """V7 §26 equation (20): H_inf = 1.885e-18 Hz."""
    result = vacuum_prediction()
    assert abs(result["H_inf_Hz"] - 1.885e-18) / 1.885e-18 < 0.01
```

Bad:

```python
def test_vacuum(self):
    r = vacuum_prediction()
    assert r["H_inf_Hz"] > 0  # too loose — doesn't catch regression
```

### Test tolerances: tight for headline numbers, loose for edge cases

- Central claims (R_anomaly, Ω_Λ, Koide K, τ_0): tolerance ~0.01-0.1%
- Dimensional scaling tests: factor-of-a-few OK
- Utility function tests: just "doesn't crash" is often enough

---

## The V7 ↔ code consistency rule

**The code must tell the same story V7 tells.**

Any time you change a numerical claim in V7, update the corresponding
test tolerance and any relevant module docstring. Any time you fix a
bug in the code that changes a numerical output, check whether V7
quotes that number and update it there too.

The April 2026 "CONDITIONAL → COMPUTED" reversal across V7 and code
(commits 3120a36, 1b11b97, 9fdfc42) is the example of this pattern.
When V7 changes status labels, the code's docstrings and API responses
must change in the same commit or the next one.

---

## The AI chat system

`ui/ai/chat.py` integrates Claude with a set of computation tools. The
AI doesn't generate physics answers from memory — it calls the actual
code and returns the results.

### Adding a new tool

1. Add the tool to the `tools` list with a clear description
2. Add a handler case in the `elif name == "my_tool":` chain
3. Update the system prompt's "Status Tiers" and sector sections
4. Test by asking the chat about your sector and verify it calls the tool

### System prompt discipline

The system prompt in `chat.py` is long by design — it encodes GRUT's
status-label discipline and the V7 ↔ code consistency rule. When V7
changes, the system prompt must change.

---

## V8 track integration

When a V8 track produces a concrete derivation, the integration pattern
is:

1. **Module**: new directory in `grut/derived/` or extension of existing
2. **Tests**: new file in `tests/derived/` with V7 claims locked in
3. **API**: new endpoint in `ui/api/routes.py`
4. **AI**: new tool in `ui/ai/chat.py`
5. **Docs**: update V7 (or V8) appendix + add to README Key Results table
6. **Status label**: match the actual epistemic state honestly

Don't merge a track that hasn't completed all 6 steps. The sociology
of framework-building rewards consistency; each sector must ship
complete or not at all.

---

## History and ledger

This codebase has caught 12 corrections to its own claims without
making external overclaims. That track record is the most valuable
thing the project has. Preserve it by:

- Writing honest commit messages (say what you broke, not just what you added)
- Updating docstrings when your understanding changes
- Flagging corrections explicitly ("Correction #13: ...")
- Never silently fixing an overclaim — document it

See `theory/derivation/*_LOG.md` for the session-by-session corrections
record.

---

## Questions to ask before adding code

- Does this output have a status label?
- Does the status label match the actual epistemic state?
- Is there a test locking in the claimed value?
- Does the module docstring state what V7 section this relates to?
- If a V7 value changes, will the test catch it?
- Did I import constants from `grut.foundation.constants` (not hardcode)?

If any answer is "no," fix before committing.

---

*GRUT-RAI Architecture reference. Last updated: April 2026.*
