# P-2 — THE CONSTRAINT STRUCTURE OF 𝔠: CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Date:** 2026-09-25 · **Chartered by:** owner (`D1_P2_OWNER_RULING_01.md`
§4): discover **the minimal constraint structure on realizable (K, N)**;
subsystem-criterion unification is **one diagnostic, not the objective**;
**do not assume the criteria must unify** — their plurality may be part of
the theory, and the question is whether it produces different realizable
influence-data classes or different coordinatizations of one class.

**Scope:** the Gaussian class (scalar S channel), where 𝔠 is decidable:
the influence functional is the pair (K, N), i.e. spectral data
(J(ω), ν(ω)) with K(t) = Σ J_μ sin(ω_μ t)/ω_μ and
N(t) = Σ J_μ s_μ cos(ω_μ t)/ω_μ per mode (s = symmetric occupation;
vacuum s = ½). ħ = 1 units, with ħ's position in the structure tracked
explicitly. Matrix-valued (multichannel) S and non-Gaussian cumulants:
OUT OF SCOPE, named as the extension boundary. **Provenance honesty,
declared now:** the candidate cone below is borrowed-standard Gaussian
open-system mathematics (Caldeira–Leggett-class realizability), treated
the way the record treats Feynman–Vernon (borrowed, U1-style); P-2's
contribution is instrument-grade verification within the program's
discipline, the minimality probes, the criterion-plurality diagnostic,
and the mapping onto the record. Register untouched; ledger 0; fenced
routes untouched; Cherenkov inheritance guard carried.

## 1. THE CANDIDATE CONE (stated before any number exists)

> **𝔠_Gauss = { (J, ν) : J(ω) ≥ 0 and ν(ω) ≥ ħ·J(ω)/2 pointwise }**

- **C-pos** (classical/passivity half): the dissipation measure is
  nonnegative.
- **C-floor** (quantum half): the fluctuation spectrum sits above the
  vacuum floor — **the constant in the floor is ħ**; the record's "ℏ is an
  irreducible input" verdict reappears as the cone's floor scale.
- **Conjectured minimality:** nothing else is universal. KMS
  (ν = J·coth(ω/2T)/2), FDT, stationarity, single-pole structure are
  STATES/SECTORS inside 𝔠, not constraints on 𝔠.

## 2. INSTRUMENT P-2 LEGS (all constructive or detecting; frozen)

- **L-A (interior realizability, constructive):** for a declared family of
  admissible targets (J_μ, s_μ ≥ ½) on an M = 8 frequency grid — including
  a **non-KMS profile** (s_μ not fitting coth(ω_μ/2T)/2 for any T on a
  declared T-grid, residual reported) and a **boundary point** (s_μ = ½
  exactly) — construct the star-bath realizer and verify the target (K, N)
  is reproduced on the time grid to 1e-10.
- **L-B (floor violation, detecting):** a target with s_μ = 0.3 < ½ at one
  mode: the required single-mode Gaussian state violates the uncertainty
  bound (symplectic eigenvalue < ½) — must be DETECTED by the state-
  positivity check; the **classical branch** (positivity of σ alone, no
  ħ-floor) must ADMIT the same target — establishing that C-floor is
  exactly the quantum content and ħ its scale.
- **L-C (positivity violation, detecting):** a target with J_μ < 0 at one
  mode: no coupling c_μ realizes it (c² ≥ 0) — detected structurally.
- **L-D (criterion-plurality diagnostic, the owner's question):** for
  every partition in the P-1 family (55 per testbed × X1/X2/X3, the P-1
  worlds re-used unchanged) compute the sector's influence data under the
  factorized E-ground preparation: verify **cone membership** (J_μ ≥ 0
  for all; s = ½ exactly) for every partition, and report the spread of
  J-shape moments (total weight, mean frequency, participation rank)
  across the criteria's P-1 winners. **Pre-registered verdict rule:**
  DIAGNOSTIC-COORDINATE if all sectors of all criteria lie in the same
  cone (plurality changes *where in 𝔠 you sit*, never *what 𝔠 is*);
  DIAGNOSTIC-CLASS-SPLIT if any criterion's sector generates data outside
  the cone the others satisfy (report which constraint splits).
- **L-E (minimality probes):** (i) boundary saturation realized exactly
  (the vacuum); (ii) interior filled at declared points including non-KMS;
  (iii) a declared FALSE-CONSTRAINT battery: candidate extra constraints
  that the cone conjecture says are NOT universal — "ν must be
  KMS-representable", "J must be monotone", "s must be
  frequency-independent" — each must be VIOLATED by an explicitly
  constructed realizable pair (three constructive counterexamples), else
  the cone is not minimal as conjectured and the run reports which
  candidate survives.

## 3. OUTCOME CLASSES (frozen)

- **CONE-CONFIRMED:** L-A/L-B/L-C all behave as required AND every L-E
  false-constraint is counterexampled AND L-D returns a verdict.
- **CONE-VIOLATED:** any admissible target fails construction (the cone
  has more structure than C-pos + C-floor; report the obstruction).
- **CONE-TOO-TIGHT:** any inadmissible target is realized (a constraint
  is not real; report).
- L-D's verdict (COORDINATE vs CLASS-SPLIT) is reported alongside,
  never merged into the cone verdict.

## 4. CONTROLS AND FENCES

Reconstruction exactness gates (1e-10) on every constructed realizer;
the L-B detector and L-C detector are halt-grade controls (a missed
violation halts the run); the P-1 worlds and criteria are re-used
byte-identical (no retuning); NO-UNIFICATION-ASSUMPTION fence: no step
scores criteria against each other or seeks a master functional — P-2
measures what their plurality does to 𝔠, nothing more. No prediction
campaign; Λ_R/Matsubara/Π₀/U5 fenced; class-4 gate unpassed; sealed-ledger
and adjudicator-track rules standing.

## 5. DELIVERABLES AND STOP

1. `calc/p2_influence_cone.py` (pure stdlib; emits
   `P2_INFLUENCE_CONE_RESULT.json`, sha-hashed).
2. `P2_INFLUENCE_CONE_VERDICT_01.md` — the cone verdict, the L-D
   diagnostic, ħ's position in the structure, and the extension boundary
   (matrix channels, higher cumulants, the type-III lift) stated.
3. **HARD STOP at the verdict** (waiting decision: the owner reads the
   structure of 𝔠 and directs the next layer — the gravity sector's
   (K, N)_grav, the P-3 quantum lift, or the geometry leg).
