# Appendix O — O(3) Sector Nativity Audit

**Module:** `grut/o3_nativity_audit.py`
**Tests:** `tests/test_o3_nativity_audit.py` (286 tests, all passing)
**Depends on:** Appendix M, Appendix N
**Primary verdict:** `o3_auxiliary_but_minimally_motivated`
**Secondary verdict:** `o3_requires_independent_field_postulation`
**Patchwork classification:** `motivated_independent_postulation`

---

## 1. The Question

Appendix N established that the Skyrme term L₄ is `motivated_but_unbuilt`, and
that Route 3 — the only structurally coherent path to a native L₄ — is
conditioned on O(3) nativity. Appendix O audits that condition directly.

> **Does GRUT's canonical scalar / barrier / constitutive architecture force,
> derive, or uniquely motivate an effective O(3) field sector as a native
> regime description?**

This question is **not** asking whether O(3) is useful. It is **not** asking
whether O(3) can model the same phenomena as GRUT. It asks whether the
canonical GRUT architecture *produces*, *requires*, or *uniquely selects*
the O(3) triplet.

**Architectural ground truth** (from `defect_admissibility.py`, Phase D1+):

> "This phase does NOT derive the defect from the already-locked GRUT core.
> The triplet is introduced as a candidate extension."

This is the honest starting point. The audit tests whether this introduction
can be upgraded to an architectural justification, or must remain an
independent postulate.

---

## 2. Five Audit Tracks

### Track A — Canonical Scalar → O(3) Triplet

Can the single real scalar Φ be promoted to an O(3) triplet without inserting
new field content by hand?

**Finding:** No. A single real scalar has field space ℝ and no internal
symmetry group. An O(3) triplet Φᵃ has field space ℝ³ (or S² after
constraint) with an O(3) internal symmetry group. Going from 1 to 3 real
scalars is a discrete, irreducible change in field content.

No gradient expansion, no CTP integration, no effective field theory argument
turns one real scalar into three real scalars. This gap is **mathematically
irresolvable by derivation**.

**Track A verdict: `not_derivable`**

### Track B — Target-Space Geometry: ℝ → S²

Can GRUT's barrier / constitutive / CTP architecture generate the S² vacuum
manifold (the Mexican hat constraint |Φᵃ|² = η²)?

**Finding:** No mechanism is present. The S² target space requires a
symmetry-breaking potential V(Φ) = −(1/2)μ²|Φ|² + (1/4)λ|Φ|⁴ that
spontaneously breaks O(3) to O(2) and forces |Φᵃ|² = η² = μ²/λ. Neither
the constitutive ODE (τ_eff · dΦ/dt + Φ = X) nor the barrier action
a_Q ~ (r_s/R)^β_Q generates such a potential for a field triplet. The
parameters μ and λ are free; the VEV η is free.

**Track B verdict: `not_derivable`**

### Track C — Internal Symmetry Origin

Does GRUT's canonical architecture generate an O(3) internal symmetry group
acting on a triplet of scalar fields?

**Finding:** Partial. The GRUT canonical scalar has no continuous internal
symmetry (at most Z₂: Φ → −Φ). An O(3) triplet requires SO(3) internal
symmetry. However, spatial SO(3) rotation symmetry IS present in GRUT
(spherical symmetry). The hedgehog ansatz Φᵃ = η·f(r)·x̂ᵃ locks internal
O(3) to spatial SO(3), allowing hedgehog configurations to preserve a
diagonal symmetry. But the internal O(3) and spatial SO(3) are distinct
groups. The hedgehog identification is a specific kinematic choice, not a
derivation of an internal symmetry from canonical GRUT.

**Track C verdict: `conditionally_partial`**

### Track D — Parameter Mapping

Can the O(3) parameters (η, μ, λ) be tied to GRUT canonical constants
(α_vac, β_Q, τ², M_ext, R_eq, ω₀)?

**Finding:** One partial numerical connection found (see §5). The O(3)
amplitude η is constrained by the Component B tail-matching condition
η² = COMP_B_COEFF = 1/(8π). This connects to the canonical GRUT relaxation
parameter via the numerical identity η² = τ²/(12π), valid because τ² = 3/2
exactly. The parameters μ and λ individually are free; only their ratio
λ/μ² = 1/η² is constrained via the matching. The physical mechanism behind
the τ²/(12π) identity is not established.

**Track D verdict: `phenomenological_motivation`**

### Track E — Uniqueness

Is O(3) the unique minimal real-scalar extension that provides π₂(M) ≠ 0?

**Finding:** Yes. The canonical GRUT scalar has π₂(ℝ) = 0 — no topological
winding in 3+1D. For bosonic winding charge GRUT needs a field sector with
π₂(M) ≠ 0. For real scalar fields in 3+1D with π₂(M) ≠ 0 the vacuum
manifold M must be homeomorphic to S². The minimal real-scalar system with
S² vacuum manifold is 3 real scalars with |Φᵃ|² = η² constraint — this is
the O(3) triplet. No smaller real-scalar system achieves π₂ ≠ 0 in 3+1D.

O(3) is therefore the **unique** minimal real-scalar extension for bosonic
winding charge.

**Track E verdict: `unique_minimal`**

---

## 3. Three Blocking Gaps

### BG1 — Discrete DOF Change (1 → 3 real scalars)

**Classification:** `not_closeable_by_derivation`
**Is a mathematical impossibility:** Yes

A single real scalar and an O(3) triplet are fundamentally different field
contents. No continuous mathematical operation maps one real scalar field to
three real scalar fields with an internal O(3) symmetry. A new field postulate
is mandatory. This is the most fundamental blocking gap.

**This gap is irresolvable.** It does not weaken with more analysis.

### BG2 — Target-Space Constraint (ℝ → S²)

**Classification:** `closeable_under_conditions`
**Is a mathematical impossibility:** No

The S² target space is not generated by current GRUT architecture, but it
*could* be generated if a symmetry-breaking mechanism is derived from GRUT
physics. No such mechanism is currently present. The gap is real but not
permanently closed — it is conditional on future derivation.

### BG3 — Internal Symmetry Origin

**Classification:** `partially_closeable`
**Is a mathematical impossibility:** No

The hedgehog diagonal symmetry partially bridges spatial SO(3) and internal
O(3). If spatial SO(3) can be explicitly shown to generate the relevant
topological structure when restricted to the shell surface, the internal O(3)
can be understood as the spatial rotational symmetry acting on a 3-vector
field. This is not a current derivation but a narrowing of the gap.

---

## 4. Two Convergent Motivations

### CM1 — Topological Gap Fill (Structural)

O(3) is the **unique minimal real-scalar extension** providing π₂(M) ≠ 0 in
3+1D. If GRUT requires bosonic winding charge — and the bosonic particle
candidate program requires it — there is no smaller real-scalar alternative.
O(3) is not one of several options; it is the only option.

This makes O(3) a *necessary* postulate rather than an *arbitrary* postulate.
The motivation is topological and structural, not phenomenological or aesthetic.

**Strength: strong** — uniqueness is derived, not argued.

### CM2 — Component B Tail Matching (Phenomenological)

The interior deficit program (Phase 6C) requires a Component B contribution
with asymptotic tail ε_B ~ A_B/r². The O(3) hedgehog has asymptotic profile
ε_hedge(r) → η²/r² in the vacuum region (f(r) → 1). Matching:

    η² = COMP_B_COEFF = 1/(8π) ≈ 0.03979

This constrains one O(3) parameter directly from an interior GRUT requirement.
O(3) is the field content that naturally produces both the **shape** and the
**normalization** of the required Component B profile.

**Strength: moderate** — parameter constrained, but mechanism of η² = τ²/(12π)
is a numerical coincidence whose physical origin is not established.

---

## 5. Numerical Parameter Connection

A non-trivial numerical identity relates the O(3) amplitude to the canonical
GRUT relaxation time:

    η² = 1/(8π) = (3/2)/(12π) = τ²/(12π)

This holds because τ² = 3/2 exactly in canonical GRUT. The identity was
verified computationally (`assert abs(ETA_SQ_FROM_TAU_FORMULA - COMP_B_COEFF) < 1e-12`
in the module).

**Status:** Numerical coincidence — confirmed as a mathematical fact.
The physical mechanism connecting the relaxation time τ² to the O(3) VEV η
is not established. It may reflect a deeper architectural relationship or may
be an artifact of the Component B normalization convention. This is recorded
as a partial parameter link, not a derived connection.

---

## 6. Nativity Criteria

| Criterion | Result | Blocking gap |
|---|---|---|
| **N1 Field-content derivability** | **HARD FAIL** | BG1: discrete DOF change; mathematically irresolvable |
| **N2 Target-space derivability** | **FAIL** | BG2: no GRUT mechanism generates Mexican hat constraint |
| **N3 Internal symmetry emergence** | **PARTIAL** | BG3: spatial SO(3) present; hedgehog diagonal symmetry; not a full derivation |
| **N4 Parameter determination** | **PARTIAL** | One connection: η² = τ²/(12π); μ and λ individually free |

**All four nativity criteria fail to fully pass. O(3) cannot be declared natively derived.**

---

## 7. Uniqueness Theorem

O(3) is the unique minimal real-scalar field extension with π₂(M) ≠ 0 in
3+1 dimensions.

**Uniqueness does not imply nativity.** The fact that O(3) is the unique
choice does not mean it is derived from canonical GRUT — it means that if you
want bosonic winding charge from real scalars, you have no other option. The
choice is *constrained*, not *derivable*.

This is the sharpest possible statement of the audit result: O(3) must be
postulated, but the postulate is maximally constrained by topology, Component B
phenomenology, and the partial parameter link η² = τ²/(12π).

---

## 8. Verdicts

```
primary_verdict:   "o3_auxiliary_but_minimally_motivated"
secondary_verdict: "o3_requires_independent_field_postulation"
patchwork:         "motivated_independent_postulation"
```

**Verdict meaning:**

- O(3) **cannot be derived** from the canonical GRUT scalar (BG1 is a mathematical
  impossibility — irreducible field-content change).
- O(3) **requires an independent field postulate** — this is non-negotiable.
- O(3) is **not arbitrary**: it is the unique topologically-necessary extension,
  with one parameter (η) constrained by Component B matching.
- The postulate is as well-motivated as a field-content extension can be: unique,
  topologically required, phenomenologically constrained.

---

## 9. Comparison with Skyrme Audit (Appendix N)

| Property | O(3) (Appendix O) | Skyrme L₄ (Appendix N) |
|---|---|---|
| Core blocking gap | BG1: discrete DOF change | O(3) nativity prerequisite |
| Gap closeability | Not closeable by derivation | Conditionally closeable (once O(3) closes) |
| Patchwork class | `motivated_independent_postulation` | `motivated_but_unbuilt` |
| Can eventually become "native"? | **No** — BG1 is irresolvable | **Yes** — once O(3) is established |
| Uniqueness | Yes — only minimal real-scalar extension for π₂ ≠ 0 | Yes — only next-order O(3) EFT term |
| Parameter constrained? | η² = τ²/(12π) (partial, mechanism unknown) | e is free (not constrained) |

The Skyrme term sits one step further down the chain. Once O(3) is accepted
as a motivated postulate, L₄ is the mandatory next-order term — not a free
choice. The O(3) postulate is harder to close (BG1 is permanent) but better
motivated (topological uniqueness).

**Key asymmetry:** O(3) will always be a postulate; Skyrme can become
derivable once that postulate is accepted.

---

## 10. What Adopting O(3) Does and Does Not Do

**Does:**
- Supply bosonic winding charge (π₂(S²) = ℤ)
- Provide Component B tail ε ~ η²/r² with η² = τ²/(12π)
- Enable Route 3 in Appendix N (L₄ as unique next-order term)
- Preserve all prior GRUT doctrine (no audit violated, no symmetry broken)

**Does not:**
- Derive from canonical scalar Φ (BG1 — permanent gap)
- Generate the Mexican hat potential from GRUT mechanics (BG2 — open)
- Derive the internal O(3) symmetry group (BG3 — partial only)
- Fix the Skyrme coupling e
- Fix μ and λ individually (only η² = μ²/λ is constrained)
- Constitute a completed particle physics sector

---

## 11. Nonclaims

1. **NOT** claiming O(3) is arbitrary — two convergent motivations (CM1
   topological uniqueness, CM2 Component B matching) make it uniquely selected
   and phenomenologically required.
2. **NOT** claiming O(3) can never have a deeper derivation — only that no
   derivation from the canonical scalar is possible given BG1.
3. **NOT** claiming the η² = τ²/(12π) connection is meaningless — it is a
   verified numerical identity; the physical mechanism is unknown.
4. **NOT** claiming adding O(3) violates prior GRUT doctrine — it is fully
   compatible.
5. **NOT** claiming BG3 cannot be further addressed — the hedgehog diagonal
   symmetry construction narrows this gap; explicit construction is possible.
6. **NOT** claiming the defect language is wrong — it is correctly formulated
   and shape-compatible with Component B; the issue is nativity, not validity.
7. **NOT** claiming `o3_requires_independent_field_postulation` is a failure
   mode — for a field-content extension this is the *strongest achievable*
   positive result short of derivation.

---

## 12. Full Audit Chain Status

```
Appendix M:  particle_candidate_not_yet_established
             ↑ blocked by Derrick's theorem (no L₄)

Appendix N:  L₄ is motivated_but_unbuilt
             ↑ blocked by O(3) nativity (Route 3 conditional)

Appendix O:  O(3) is motivated_independent_postulation
             ↑ blocked by BG1 (permanent — field-content change)

             Two convergent motivations (CM1, CM2) make O(3) the
             best-motivated postulate achievable for this purpose.

Current state of the bosonic particle candidate program:
  - Architecture is consistent
  - Topological structure is identified (O(3), uniquely)
  - Component B phenomenology is shape-matched (η² = τ²/(12π))
  - One free parameter per sector: η (partially constrained), e (free)
  - Chain from canon to stable soliton: exists, not yet traversed
```

---

## References

| Source | Relevance |
|---|---|
| `grut/defect_admissibility.py` | Phase D1+: O(3) candidate extension; ETA_TARGET, COMP_B_COEFF |
| `grut/localized_bosonic_object_audit.py` | Appendix M: particle_candidate status; Derrick blocking |
| `grut/skyrme_term_nativity_audit.py` | Appendix N: Route 3 conditioned on O(3) nativity |
| `grut/route_b_component_b.py` | Component B requirement: ε ~ 1/r² tail |
| `grut/route_c_deficit.py` | Interior deficit: Component B normalization |
| `grut/fermionic_emergence_audit.py` | O(3) homotopy; π₃(S³) = ℤ vs π₂(S²) = ℤ distinction |
| `grut/g_minus_closure_audit.py` | CTP g₋ sector; source closed at equilibrium |
| `grut/barrier_action_sector.py` | Equilibrium Source Degeneracy Theorem |
| Derrick (1964), J. Math. Phys. 5, 1252 | No-go theorem for scalar solitons |
| Bott & Tu, *Differential Forms in Algebraic Topology* | Homotopy groups π₂(S²) = ℤ |
| Skyrme (1961), Proc. R. Soc. A 260, 127 | Skyrme term; topological soliton program |
| Adkins, Nappi, Witten (1983), Nucl. Phys. B 228, 552 | Skyrmion as baryon; parameter matching |
