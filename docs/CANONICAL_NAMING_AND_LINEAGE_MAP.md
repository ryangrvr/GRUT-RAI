# GRUT Canonical Naming and Lineage Map

## Purpose

Resolve the naming/lineage ambiguity between two entities that have both been called "GRUT-II" at different points in the program. This document is the single authoritative reference for all GRUT naming going forward.

---

## The Conflict

Two distinct bodies of work carry the label "GRUT-II":

### Entity A: The Stochastic Noise Branch (O4a-Falsified)

- **Original name:** GRUT-II (Alpha through Terminal)
- **Content:** Added a constitutive noise parameter D to the GRUT equation: tau dPhi/dt + Phi = X + xi(t). Fokker-Planck derivation, stochastic telegrapher spectrum, near-horizon coupling, LIGO O4a confrontation.
- **Result:** Universal D falsified by O4a at 23 orders of magnitude. Sector CLOSED.
- **Renamed to:** GRUT-I Part 2 (Stochastic Sector Audit)
- **Documents:** GRUT_II_ALPHA_SUCCESSOR_CHARTER_AND_PRIMITIVE_CONSTITUTIVE_NOISE.md, GRUT_II_TERMINAL_UNIVERSAL_D_FALSIFICATION_AND_GRUT_III_BOUNDARY.md, GRUT_I_PART_2_STOCHASTIC_SECTOR_AUDIT_ZENODO_BRIEFING.md
- **Code:** grut/grut_ii_fokker_planck.py, grut/stochastic_telegrapher.py, grut/coupling_problem.py, grut/ligo_confrontation.py

### Entity B: The Theory of Scaling (Current Active Program)

- **Original name:** GRUT II (the "real" GRUT-II, post-renaming)
- **Content:** Promotes tau from parameter to field. Bistability via cubic saturation + delay. Far-field equivalence. QNM/tidal analysis. USL quantum prediction. CTP influence-functional derivation. Extended-body correction. Full experimental roadmap audit.
- **Result:** Active through Nu-Prime (quantum sector now terminally closed at prediction level).
- **Charter:** GRUT_II_OPENING_CHARTER_THEORY_OF_SCALING.md
- **Documents:** All GRUT_II_[GREEK]_*.md and GRUT_II_[GREEK]_PRIME_*.md files from Alpha onward
- **Code:** grut/dynamical_tau_system.py, grut/grut_ii_bifurcation_symbolic.py, grut/grut_ii_general_coupling.py, grut/grut_ii_static_bistability.py, grut/grut_ii_phase_response.py, grut/grut_ii_regge_wheeler_qnm.py, grut/grut_ii_tidal_love.py, grut/grut_ii_usl_nanoparticle_prediction.py, grut/grut_ii_blueprint_environmental_budget.py, grut/grut_ii_mass_window_optimization.py, grut/grut_ii_robustness_audit.py, grut/grut_ii_ctp_influence_functional.py, grut/grut_ii_extended_body_usl.py, grut/grut_ii_geometry_optimization.py, grut/grut_ii_sg_nanodiamond_audit.py

---

## The Renaming Event

A renaming was executed (documented in RENAMING_MANIFEST.md) that:

1. Demoted the original GRUT-II, III, IV to sub-parts of GRUT-I (they were sector audits, not independent theories)
2. Reserved the name "GRUT-II" for a genuinely new successor theory (Theory of Scaling)

| Before Renaming | After Renaming | Content |
|---|---|---|
| GRUT (Books IV-XXI) | **GRUT-I Part 1** | Deterministic constitutive framework |
| GRUT-II (Alpha-Terminal) | **GRUT-I Part 2** | Stochastic sector audit (D falsified by O4a) |
| GRUT-III (Alpha) | **GRUT-I Part 3** | Position-dependent noise audit (no viable D(r)) |
| GRUT-IV (Alpha-Beta) | **GRUT-I Part 4** | Self-consistent multiplicity audit (artifact) |
| *(new)* | **GRUT-II** | Theory of Scaling in a Responsive Reality |

---

## The Residual Ambiguity

### In code files

Several Python files in `grut/` carry the prefix `grut_ii_` but belong to **Entity A** (the stochastic branch, now GRUT-I Part 2):

- `grut_ii_fokker_planck.py` → GRUT-I Part 2
- `grut_ii_fokker_planck.py` is the only one with this specific conflict; other `grut_ii_*` files belong to Entity B

### In documents

Several documents carry the prefix `GRUT_II_` but describe Entity A:

- `GRUT_II_ALPHA_SUCCESSOR_CHARTER_AND_PRIMITIVE_CONSTITUTIVE_NOISE.md` → Entity A (GRUT-I Part 2 Alpha)
- `GRUT_II_TERMINAL_UNIVERSAL_D_FALSIFICATION_AND_GRUT_III_BOUNDARY.md` → Entity A (GRUT-I Part 2 Terminal)

These coexist with Entity B documents that also carry `GRUT_II_`:

- `GRUT_II_OPENING_CHARTER_THEORY_OF_SCALING.md` → Entity B (the real GRUT-II)
- `GRUT_II_ALPHA_DYNAMICAL_TAU_FIELD.md` → Entity B
- All `GRUT_II_*_PRIME_*.md` → Entity B

### In program_state.py

The identity statement says: "GRUT-II: D falsified by O4a." This refers to **Entity A** (the stochastic branch), using the **old** naming convention. It does not acknowledge Entity B at all.

---

## Canonical Resolution

### Rule 1: The name "GRUT-II" now refers EXCLUSIVELY to Entity B

The Theory of Scaling in a Responsive Reality. Stages Alpha through Nu-Prime. CTP influence functional. USL prediction. This is the active, current GRUT-II.

### Rule 2: Entity A is canonically "GRUT-I Part 2"

The stochastic noise branch. Fokker-Planck. D parameter. O4a falsification. It is a CLOSED sector audit within GRUT-I, not an independent theory.

### Rule 3: Disambiguation by context

When a document or file uses "GRUT-II" and context is ambiguous, the following test applies:

- If it discusses **D, noise, Fokker-Planck, stochastic telegrapher, O4a** → it means **GRUT-I Part 2** (Entity A, old naming)
- If it discusses **dynamical tau, bistability, scaling, USL, CTP, influence functional** → it means **GRUT-II** (Entity B, current)

### Rule 4: program_state.py must be updated

The identity statement should read:

```
"GRUT-I Part 2 (formerly GRUT-II): D falsified by O4a.
 GRUT-I Part 3 (formerly GRUT-III): no viable D(r).
 GRUT-I Part 4 (formerly GRUT-IV): multiplicity was artifact.
 GRUT-II (Theory of Scaling): quantum sector terminally closed at Nu-Prime.
   USL derived from CTP influence functional. Hardware-limited, not theory-limited."
```

### Rule 5: File-level disambiguation

The following Entity A files retain their `grut_ii_` prefix as historical artifacts but are understood to belong to GRUT-I Part 2:

- `grut/grut_ii_fokker_planck.py` — GRUT-I Part 2 Alpha

All other `grut_ii_*` files belong to the current GRUT-II (Entity B).

No files will be renamed. The disambiguation is by this document, not by filename changes.

---

## Canonical Alias Map

| Canonical Name | Aliases (may appear in documents/code) | Status |
|---|---|---|
| **GRUT-I Part 1** | "GRUT" (Books IV-XXI), "the main theory" | CLOSED |
| **GRUT-I Part 2** | "GRUT-II" (pre-renaming), "stochastic sector", "noise branch" | CLOSED (O4a) |
| **GRUT-I Part 3** | "GRUT-III" (pre-renaming), "position-dependent noise" | CLOSED |
| **GRUT-I Part 4** | "GRUT-IV" (pre-renaming), "multiplicity audit" | CLOSED |
| **GRUT-II** | "Theory of Scaling", "new GRUT-II", "GRUT II" (post-renaming) | **QUANTUM SECTOR CLOSED (Nu-Prime). Strong-field + foundational sectors open.** |
| **GRUT-III** | *(not yet opened)* | **AUTHORIZED but not yet started** |

---

## Lineage Diagram

```
GRUT-I Part 1 (Books IV-XXI)
├── Part 2 (Stochastic Sector) ←── formerly "GRUT-II" ←── CLOSED (O4a, 23 orders)
├── Part 3 (Position Noise)    ←── formerly "GRUT-III" ←── CLOSED (no viable D(r))
└── Part 4 (Multiplicity)      ←── formerly "GRUT-IV"  ←── CLOSED (artifact)

GRUT-II: Theory of Scaling (Alpha → Nu-Prime)
├── Classical Sector (Alpha → Nu)
│   ├── Bistability (Nu: two stable fixed points)
│   ├── Far-field equivalence (Rho)
│   ├── QNM: 0.002% effect → collapses (Upsilon)
│   ├── Tidal: compactness-suppressed (Sigma)
│   └── Transfer function discriminator (Xi, Pi)
├── Quantum Sector (Alpha-Prime → Nu-Prime) ←── TERMINALLY CLOSED
│   ├── USL derived from CTP influence functional (Theta/Iota-Prime)
│   ├── Extended-body correction (Kappa-Prime)
│   ├── Geometry optimization (Lambda-Prime)
│   ├── SG hardware audit (Mu-Prime)
│   └── Terminal closure (Nu-Prime)
└── Foundational Sector ←── OPEN (handed to GRUT-III)
    ├── tau derivation problem
    ├── Level-1 connection
    ├── UV structure
    ├── Gravitational-bath closure
    └── Covariance promotion

GRUT-III: Foundational Closure Phase ←── AUTHORIZED, NOT YET STARTED
```

---

## Application

This document is the canonical reference for all naming questions. Any future stage, document, or code file should use the names as defined here. When citing earlier stages that used pre-renaming conventions, the canonical name should be given with the alias in parentheses:

> Example: "GRUT-I Part 2 (formerly GRUT-II) established the Fokker-Planck framework..."

> Example: "GRUT-II Alpha (Theory of Scaling) promoted tau to a dynamical field..."

---

*Canonical Naming and Lineage Map established. The name "GRUT-II" now refers exclusively to the Theory of Scaling (Entity B). The stochastic noise branch is "GRUT-I Part 2" (Entity A). GRUT-III is authorized but not started.*
