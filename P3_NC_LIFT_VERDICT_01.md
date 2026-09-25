# P-3 — THE NONCOMMUTATIVE LIFT: VERDICT

**Date:** 2026-09-25 · **Authority:** GitHub Issue #2 + owner guidance ·
**Charter:** `P3_NC_LIFT_CHARTER_01.md` (frozen at `78b188e` before the
run) · **Instrument:** `calc/p3_nc_lift.py` · **Artifact:**
`P3_NC_LIFT_RESULT.json` (sha `781c094a028ee6b9…`) · **Battery 24/25 — the
one failure is a FROZEN GATE PRESERVED AS FOUND, and it is the run's most
important result.** Posture honored: this was an attack, and the attack
landed twice.

## QUESTION A — the admissibility geometry:
## SURVIVES-AS-GEOMETRY + NULL-AS-NEW-PRINCIPLE

On an exact 3-spin thermal bath with **genuinely noncommuting channels**
([B₁,B₂] ≠ 0 at norm 1.22; spectral matrices noncommuting across
frequencies at 0.097 — no fixed channel basis exists):

- The candidate lift **ν(ω) ± J(ω)/2 ⪰ 0 (operator order)** holds at
  every frequency, is Hermitian, is covariant under non-orthogonal channel
  congruence with truth-value invariance, and reduces to the scalar
  ν ≥ |J|/2 on the commuting restriction. **The cone survives
  quantization as geometry, with ≥ becoming ⪰.**
- It is **strictly stronger than the scalar theory**: a declared pair
  passing every channelwise scalar check has ν − J/2 eigenvalue −0.80 and
  is certified non-realizable. Off-diagonal structure carries real
  constraint content.
- **But — per the redundancy rule, applied without flinching:** every
  spectral matrix reconstructs exactly (5.6e-17) from Gram vectors
  √p_n⟨n|B_a|m⟩, i.e. the matrix admissibility condition **is bath-state
  positivity written in influence-data language. NULL-AS-NEW-PRINCIPLE.**
  And CP (Choi PSD verified at both declared times) is
  dilation-guaranteed — the (b) leg adds no data constraint beyond (a).
  No new foundational inequality emerged; P-3 did not become a proof of
  quantum mechanics.

## QUESTION B — the counting law:
## MODIFIED (matrix channels) + CLASS-SPLIT (beyond Gaussian)

**The attack's first hit — a genuine matrix-level modification:**

- H1 survives exactly: multiplying all vertices by q shifts **both**
  eigen-slopes by +2.000.
- **The frozen H3 eigenvalue-level gate FAILED and is preserved as
  found:** the cancellation shifted the dominant eigen-slope by +2.216,
  not +4. The post-hoc diagnostic (a measurement, labeled, not a rescue)
  shows the +4 increment survives **per branch** exactly (+3.999 on the
  affected species' spectral weight). What fails is the increment's
  commutation with eigenvalue ordering: **in matrix channels a cancelled
  branch can be MASKED by another channel — min-dominance hands the
  observable exponent to the masking channel's class.** The Gaussian
  scalar theory was hiding exactly this: eigenvalue-level counting and
  branch-level counting coincide only when one channel exists.
- The convention-laundering null control fired as designed: an
  ω-dependent channel rescaling fakes a +2 slope shift (+1.002 → +3.004),
  demonstrated and excluded by the ω-independent-basis freeze.

**The attack's second hit — the class split, now demonstrated
noncommutatively:**

- Two genuinely different spin baths with **exactly matched two-point
  data** (⟨B²⟩ equal to 1e-12; C(t) = 2g²e^{−iω₀t} both; third cumulants
  zero by symmetry) and **different connected fourth cumulants**
  (κ₄ = −4g⁴ vs −8g⁴, both matching the analytic values) produce probe
  coherence curves differing by **0.338** — with the matched control at
  0.0. **(K, N) is a projection of the influence functional; the first
  noncommutative/non-Gaussian obstruction is κ₄.** Higher cumulants were
  not forced into (K, N), per the guidance.

## REPRESENTATION INVARIANCE (Q5) — D-1 extends to the matrix level

A bath-local rotation commuting with the bath Hamiltonian and state gives
a microscopically re-labeled realization with identical **full** influence
data: probe trajectories agree to 1.1e-14. Microscopic differences at
fixed full influence data remain representational; **the quantity that
does distinguish realizations is exactly the cumulant data** (Q3's κ₄) —
which names, at matrix level, what D-1's equivalence-class label enlarges
to beyond Gaussianity.

## THE TYPE-III EXTENSION MAP (Q6 — map, not claims)

At the type-III boundary the following finite-type-I ingredients must
generalize or fail: discrete Gram sums → operator-valued spectral measures
(Bochner-type positivity — the operator-order cone's natural continuum
form); **factorized preparations become unavailable** without the
split-property collar (the same seam the partition/D3b line already
carries); Choi/CP tomography requires normal states; eigenvalue-ordering
(the masking phenomenon) becomes spectral-projection flow. The recorded
III₁ obstruction remains the boundary marker.

## DEFECT HISTORY (disclosed)

Run 1 had three failures; diagnosis separated instrument from physics:
(i) the Q5 discrepancy was provably numerical (the rotated realization is
analytically identical) — a non-power-of-two divisor in the matrix
exponential, repaired to exact scaling-and-squaring (post-fix 1.1e-14);
(ii) the null control had rescaled the subdominant channel — repaired;
(iii) the H3 cancellation had been applied to one vertex component —
repaired to act on the whole species vertex, **after which the
eigenvalue-level failure persisted and was recognized as the finding**,
with the frozen gate kept red on the artifact face.

## WHAT THIS DOES TO 𝒯 (for the owner's ruling)

The candidate theory statement survives its first quantization contact,
sharpened three ways: (1) the admissibility geometry lifts (operator
order), but its content at this level is quantum state positivity — the
cone is a **representation of quantum admissibility, not an addition to
it**; the generative question (why the floor?) stands exactly where the
ruling left it. (2) Beyond Gaussianity the fundamental object is the
**full influence functional — the cumulant hierarchy — of which (K, N)
is the two-point face**; the admissibility structure of that hierarchy
(complete positivity of the hierarchy, Bochner-type) is the next open
object, named and not developed here. (3) The selection arrow is refined:
counting is **per-branch**, and observable exponents follow
**min-dominance over branches** — a matrix phenomenon invisible in every
scalar instrument this program has run.

## HARD STOP

Verdict recorded; a closing comment is posted to Issue #2. The waiting
decision: **the owner rules on what the lift's outcome does to 𝒯** — the
cumulant-hierarchy admissibility object, the gravity sector's consumption
of the per-branch/masking refinement, or the geometry leg. Λ_R, Matsubara,
Π₀, U5 remain fenced; ω⁷/class-4 untouched, as ordered.
