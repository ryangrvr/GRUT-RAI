# Appendix N — Skyrme Term Nativity Audit

**Module:** `grut/skyrme_term_nativity_audit.py`
**Tests:** `tests/test_skyrme_term_nativity_audit.py` (235 tests, all passing)
**Depends on:** Appendix M (`localized_bosonic_object_audit.py`)
**Primary verdict:** `no_native_skyrme_support_found`
**Secondary verdict:** `effective_skyrme_analog_possible`
**Patchwork classification:** `motivated_but_unbuilt`

---

## 1. The Question

Appendix M established that GRUT's current architecture supports a
`particle_candidate_not_yet_established` verdict for bosonic localized objects.
The single blocking gap between that verdict and a **stable** bosonic localized
object is Derrick's theorem: in D = 3, a configuration with only a kinetic term
plus Mexican hat potential satisfies

    dE/dλ = E₂ + 3E_V > 0   for all λ

and therefore collapses. The only known classical stabilizer is the Skyrme
gradient-quartic term L₄. This appendix asks:

> **Does L₄ arise naturally from GRUT's constitutive / barrier / CTP
> architecture, or would adding it be external patchwork?**

The question has a precise meaning:
- **Native:** L₄ can be *derived* from current GRUT mechanisms without new free parameters.
- **Patchwork:** L₄ must be *imported* as an additional postulate or free-parameter term.
- **Motivated-but-unbuilt:** L₄ is the natural next-order term in a derivation chain that GRUT is structurally positioned to complete, but that chain is not yet built.

---

## 2. The Skyrme Term

    L₄ = (1/16e²) [∂_μΦᵃ × ∂_νΦᵃ]²

This is a **quartic-in-gradients** O(3)-invariant term in the O(3) nonlinear
sigma model. Under Derrick rescaling r → λr in D = 3:

| Energy component | Scaling |
|---|---|
| E₂ (kinetic gradient) | λ¹ |
| E_V (Mexican hat, field-space quartic) | λ³ |
| E₄ (Skyrme, gradient quartic) | λ⁻¹ |

Stationarity condition for a stable soliton:

    dE/dλ|_{λ=1} = E₂ − E₄ = 0   →   E₄ = E₂

Only E₄ opposes collapse. The parameter e (Skyrme coupling) sets the soliton
radius and binding energy.

---

## 3. Critical Distinction: λ|Φ|⁴ ≠ L₄

**This must be stated clearly and is frequently confused.**

Phase D1+ (`defect_admissibility.py`) contains the Mexican hat potential:

    V(Φ) = −(1/2)μ²|Φ|² + (1/4)λ|Φ|⁴

This term is **quartic in field-space**, not quartic in gradients.

Under Derrick rescaling: E_V ~ λ³ — the **same positive sign** as E₂.

Therefore:

    dE/dλ|_{λ=1} = E₂ + 3E_V > 0   always

**The Mexican hat potential does NOT stabilize against Derrick collapse.**
The hedgehog in Phase D1+ remains Derrick-unstable whether or not V(Φ) is
included. The λ|Φ|⁴ potential breaks O(3) to O(2) and selects the vacuum
manifold S² — it does not function as a topological stabilizer.

These are structurally distinct objects:

| Term | Type | Derrick exponent (D=3) | Stabilizes? |
|---|---|---|---|
| λ\|Φ\|⁴ | Field-space quartic | +3 | No |
| L₄ | Gradient quartic | −1 | Yes |

---

## 4. Five Derivation Routes Audited

### Route 1 — Constitutive ODE Gradient Expansion

The GRUT relaxation equation τ_eff · dΦ/dt + Φ = X is first-order and linear.
The Burnett expansion introduces higher temporal corrections but not the
specific anisotropic quartic spatial gradient structure required for L₄.

**Status: `not_established`**

### Route 2 — Galley CTP Effective Action

Integrating out the g₋ sector in the CTP formalism can generate
higher-derivative effective terms. At equilibrium the g₋ source vanishes
(Appendix K / `g_minus_closure_audit.py`). Whether the fluctuation-level CTP
computation around GRUT equilibrium generates L₄ is an open computation —
in fluid EFT this procedure produces viscous terms; in scalar EFT it can
produce (∇Φ)⁴ terms at one loop.

**Status: `open_but_unbuilt`**

### Route 3 — O(3) Derivative Expansion

The O(3) nonlinear sigma model is the leading-order term in a systematic
derivative expansion of an O(3)-symmetric EFT. The unique next-order
(4-derivative) O(3)-invariant term, up to total derivatives and equations of
motion, **is** the Skyrme term L₄. This is a structural fact of the O(3) EFT.

**Condition:** O(3) must first be established as canonical GRUT. In the current
state, the O(3) triplet is a Phase D1+ candidate extension (not canon).

**This is the structurally strongest route.** If O(3) nativity closes, L₄
is not a free addition — it is the mandatory next-order term.

**Status: `conditionally_open`** — conditioned on O(3) nativity (Appendix O)

### Route 4 — Phase D1+ Mexican Hat Potential (Field-Space Quartic)

The λ|Φ|⁴ term is a field-space quartic, not a gradient quartic (see §3 above).
Under Derrick scaling its contribution is positive and proportional to λ³.
It cannot function as a Skyrme analog and does not generate one.

**Status: `not_skyrme_analog`**

### Route 5 — Barrier Action Underdetermination

The Equilibrium Source Degeneracy Theorem (`barrier_action_sector.py`) states
that the equilibrium constitutive primitives alone do not identify a unique
barrier action. This underdetermination means L₄ is **compatible** with the
barrier action space but is not **required** by it. The theorem permits without
generating.

**Status: `compatible_but_undetermined`**

---

## 5. Nativity Criteria

All three must pass for a native verdict.

| Criterion | Result | Notes |
|---|---|---|
| **N1 Derivability** | **FAILS** | No route is established; Route 3 requires O(3) nativity prerequisite |
| **N2 Parameter-free** | **FAILS** | Skyrme coupling e is a new free parameter not fixed by α_vac, β_Q, τ², M_ext, R_eq, ω₀ |
| **N3 Architectural origin** | **FAILS** | Route 3 is a general O(3) EFT argument; L₄ is the next-order term in ANY O(3) sigma model, not specifically in GRUT's O(3) |

**All three nativity criteria fail.**

---

## 6. Verdicts

```
primary_verdict:   "no_native_skyrme_support_found"
secondary_verdict: "effective_skyrme_analog_possible"
patchwork:         "motivated_but_unbuilt"
```

**Verdict meaning:**

- L₄ is **not natively derived** from current GRUT mechanisms.
- L₄ is **compatible** with prior GRUT doctrine (no audit violated, no symmetry broken).
- L₄ is **motivated but unbuilt**: the derivation chain exists structurally (Route 3),
  but it requires completing the O(3) nativity step first.
- **Adding L₄ now**, before O(3) nativity is established, would be classified
  `compatible_but_ad_hoc` — the coupling e floats freely and is not anchored.
- **Adding L₄ after O(3) nativity is established**, with e expressible in GRUT
  parameters, would be `motivated_but_unbuilt` → achievable-not-patchwork.

---

## 7. The Conditional Path to a Native Skyrme Term

The unique coherent path is:

```
GRUT canon
    ↓
Appendix O: establish O(3) as motivated_independent_postulation
    ↓
Route 3 closes: L₄ is the unique next-order O(3) EFT term
    ↓
Match e to GRUT parameters (open — not yet done)
    ↓
L₄ becomes motivated + parameter-constrained (not ad hoc)
    ↓
Appendix M verdict upgrades: particle_candidate → stable_bosonic_localized_object
```

This path exists. It is not closed. None of its steps are impossible. The
current status is that the path is **structurally identified but not traversed**.

---

## 8. Doctrine Compatibility

Adding L₄ to the O(3) sector would:

| Property | Status |
|---|---|
| Preserve O(3) symmetry | Yes |
| Preserve spherical symmetry | Yes (L₄ in hedgehog ansatz is spherically symmetric) |
| Introduce spinors | No |
| Introduce gauge fields | No |
| Violate τ_eff domain | No (L₄ is a static term) |
| Violate β_Q hypothesis | No |
| Change theory class | No (Skyrme model is O(3) sigma model + L₄) |
| Introduce new free parameter | **Yes** — Skyrme coupling e (unfixed by GRUT) |
| Compatible with prior doctrine | **Yes** |

---

## 9. Nonclaims

1. **NOT** ruling out that GRUT can eventually derive L₄ — Route 3 is a coherent
   constructive path.
2. **NOT** claiming the Mexican hat potential in Phase D1+ is a Skyrme-type
   stabilizer. λ|Φ|⁴ is field-space quartic; L₄ is gradient quartic.
3. **NOT** claiming the Skyrme coupling e cannot eventually be expressed in GRUT
   parameters — this is open, not negated.
4. **NOT** claiming L₄ is incompatible with prior doctrine — it is compatible.
   The verdict is about nativity, not compatibility.
5. **NOT** claiming CTP cannot generate L₄ — Route 2 is open but unbuilt.

---

## 10. Bridge to Appendix O

The hinge of the entire bosonic particle candidate chain is now O(3) nativity.

- Appendix M: `particle_candidate_not_yet_established` — blocked by Derrick
- Appendix N (this): L₄ is `motivated_but_unbuilt` — blocked by O(3) nativity
- **Appendix O:** Does O(3) close? That is the decisive question.

If O(3) closes as a motivated postulate → L₄ is no longer ad hoc → Derrick
stabilization is achievable → Appendix M verdict upgrades.

If O(3) does not close → L₄ remains ad hoc and the particle candidate remains
unestablished.

---

## References

| Source | Relevance |
|---|---|
| `grut/localized_bosonic_object_audit.py` | Appendix M: Derrick analysis, primary blocking mechanism |
| `grut/defect_admissibility.py` | Phase D1+: O(3) hedgehog, Mexican hat potential, Component B |
| `grut/barrier_action_sector.py` | Equilibrium Source Degeneracy Theorem |
| `grut/g_minus_closure_audit.py` | CTP g₋ sector: source closed at static equilibrium |
| `grut/fermionic_emergence_audit.py` | O(3) homotopy content, Hopf absent |
| Skyrme (1961), Proc. R. Soc. A 260, 127 | Original Skyrme term |
| Adkins, Nappi, Witten (1983), Nucl. Phys. B 228, 552 | Skyrmion quantization |
| Derrick (1964), J. Math. Phys. 5, 1252 | No-go theorem for scalar solitons in D≥2 |
| Weinberg (1979), Physica A 96, 327 | EFT derivative expansion systematics |
