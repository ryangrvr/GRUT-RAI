# Appendix Q-B: GRUT-Native Quantum State Space

**Status:** bounded_structural_result (BSR)
**Depends on:** Q0 (inventory complete), Q-A (charter authorized)
**Primary verdict:** `density_matrix_or_functional_state_required`
**Commutation verdict:** `quantization_route_currently_blocked`
**Mapping verdict:** `compatible_only`

---

## 1. The Question

Q-B asks the narrowest possible honest question about GRUT and quantum mechanics:

> **What state-space structure does GRUT natively support for microphysical description?**

This is prior to — and independent of — any question about reproducing quantum mechanics. It does not ask whether GRUT can be extended to accommodate quantum states. It asks what GRUT *already contains*, classified with Appendix P status throughout.

The question divides into seven audit tracks, each interrogating a specific structural feature of the GRUT architecture.

---

## 2. Track A — Closed vs Open Microphysical Ontology

**Verdict: `open_at_effective_level`** (native_canon at native level)

At its native level, GRUT is a **closed, deterministic classical field theory**:

```
τ dΦ/dt + Φ = X
```

The scalar field Φ evolves via a first-order dissipative ODE. No stochastic forcing, no environmental coupling, no probability distribution — fully closed and deterministic.

At the effective (Galley CTP) level, an implicit bath drives the retarded influence kernel. The Keldysh decomposition:

- **Φ₊ = (Φ₁ + Φ₂)/2** — the physical (average) field; satisfies the correct GRUT equation
- **Φ₋ = Φ₁ − Φ₂** — the difference field; encodes the open-system coupling

The Φ₊ equation at the physical limit (Φ₋ → 0) recovers τ dΦ/dt + Φ = X — demonstrating that the effective description is an open-system extension of the same closed native structure.

This matches the Caldeira–Leggett / influence-functional paradigm for open quantum systems. The architecture is *architecturally similar* to the formal apparatus used for open quantum systems — but similarity to the formalism is not derivation of the physics. See Track E and Track G.

**Appendix P:** native_canon (for the deterministic ODE as the closed native structure)

---

## 3. Track B — Native State Object

**Verdict: no native quantum state space established** (bounded_structural_result)

Six candidates were audited:

| ID | Candidate | Status in GRUT | Appendix P |
|----|-----------|----------------|------------|
| SS1 | Pure ket \|ψ⟩ ∈ ℋ | absent | compatible_but_ad_hoc |
| SS2 | Density matrix ρ̂ | absent | compatible_but_ad_hoc |
| SS3 | CTP kernel ρ(Φ₁,Φ₂) | formally_compatible (not derived) | compatible_but_ad_hoc |
| SS4 | Wigner / phase-space W(Φ,Π) | absent (no Π, Track D) | compatible_but_ad_hoc |
| SS5 | Influence functional F\[Φ₁,Φ₂\] | present as dynamics object | effective_reduction |
| SS6 | No native quantum state | **primary null result** | **bounded_structural_result** |

**SS1 — Pure ket:** Requires a complex Hilbert space. GRUT has only a real scalar configuration space. No complex structure J with J² = −1 is present (Q0 items D1, D3). FFM2 (wavefunction_from_real_scalar) from the Q-A charter explicitly prohibits the promotion of a real scalar to a wavefunction.

**SS2 — Density matrix:** Requires an operator algebra acting on a Hilbert space. Neither the Hilbert space (D1) nor the operator algebra (D2) is present in the Q0 inventory. The constitutive ODE is deterministic — no probability mixture is defined.

**SS3 — CTP kernel:** The doubled-field structure (Φ₁, Φ₂) from the Galley truncation is formally compatible with the notation ρ(Φ₁, Φ₂) = ⟨Φ₁|ρ̂|Φ₂⟩. This notation is standard in the quantum field theory CTP formalism. However, the identification requires a *prior Hilbert space* to give meaning to ⟨Φ₁|ρ̂|Φ₂⟩. GRUT does not supply that Hilbert space. Additionally, Φ₋ = Φ₁ − Φ₂ satisfies dΦ₋/dt = +Φ₋/τ (ghost mode, growth rate sign = +1), which disqualifies the CTP structure as a complex quantum structure. See Track E for the full Φ₋ analysis. FFM6 applies.

**SS4 — Wigner function:** Requires a canonical momentum Π so that the phase space (Φ, Π) is defined. Track D establishes that Π is degenerate for GRUT's first-order Lagrangian. No phase space, no Wigner function.

**SS5 — Influence functional:** Present in GRUT's effective description as effective_reduction (Q0 item C4). However, the influence functional is a *dynamics* object — it specifies how the system transitions, not what state it is in at a time. It does not constitute a state space.

**SS6 — Null result:** The honest architectural finding. No native quantum state space is established. The gap is precisely identified:

> **Missing ingredient:** A complex structure J: real_config_space → real_config_space with J² = −1.
> J would promote the real linear space to a ℂ-linear space, enabling the construction of a Hilbert space inner product and Born-rule normalization.
> J is absent. Its addition would require motivated_independent_postulation (MIP) classification minimum.

The null result is a **bounded structural result** (BSR) — the gap is documented and bounded, not vague. It is not a claim that quantum mechanics cannot be added to GRUT; it is a precise statement of what is currently absent.

---

## 4. Track C — Pure vs Mixed State Mandate

**Verdict: `not_natively_supported`** (for both quantum pure and quantum mixed states)

At the native level, the GRUT state is a definite real scalar field configuration Φ(x,t) — **classically pure** in the sense that there is no probability distribution over configurations.

For quantum mechanics:

- **Quantum pure state |ψ⟩:** Requires complex Hilbert space (absent, Track B). Not natively supported.
- **Quantum mixed state ρ̂:** Requires operator algebra and Hilbert space (absent, Track B). Not natively supported.

The open-system character of the effective (Galley) description (Track A) *motivates* a mixed state / density matrix approach for any quantum extension — the bath implicit in the retarded kernel would cause decoherence in a quantum treatment. But motivation is not presence. Both quantum state types are classified as not_natively_supported.

**Appendix P:** bounded_structural_result (the analysis is complete and bounded; neither quantum state type is present or obstructed-with-resolution-path — they are architecturally absent).

---

## 5. Track D — Canonical Momentum and Commutation Audit

**Verdict: `quantization_route_currently_blocked`** (bounded_structural_result)

Standard canonical quantization requires:
1. A second-order Lagrangian L(Φ, ∂ₜΦ) containing a kinetic term ½(∂ₜΦ)²
2. A canonical momentum Π = ∂L/∂(∂ₜΦ) ≠ 0
3. The commutation relation [Φ(x), Π(y)] = iℏ δ(x−y)

**GRUT fails the first condition:** The constitutive ODE τ dΦ/dt + Φ = X is first-order in time. No natural Lagrangian for this equation contains a (∂ₜΦ)² term. Therefore Π = ∂L/∂(∂ₜΦ) = 0 or is degenerate — the canonical momentum is not defined.

**The Bateman/Galley doubled system:** For dissipative first-order systems, the standard approach is to introduce a doubled Lagrangian (analogous to the Galley CTP construction):

```
L = τ (∂ₜΦ₁) Φ₂ − Φ₁ Φ₂
```

This yields the correct equation of motion for Φ₁. The canonical momentum in this doubled system is:

```
Π₁ = ∂L/∂(∂ₜΦ₁) = τ Φ₂
```

This is the **shadow field** Φ₂, scaled by τ — not a momentum derived from the physical field Φ₁ alone. Quantization via this route would require the commutation relation [Φ₁, τΦ₂] = iℏ, coupling the physical field to its CTP partner. This is non-standard and would require a new postulate: MIP minimum classification.

No alternative symplectic structure is established in canonical GRUT. The standard CCR quantization route is currently blocked.

**Appendix P:** bounded_structural_result — the obstruction is precisely documented; it is not claimed to be permanent.

---

## 6. Track E — Doubled-Field to State Mapping ⟨Φ₁|ρ|Φ₂⟩

**Verdict: `compatible_only`** (compatible_but_ad_hoc)

**The formal compatibility:** In the quantum field theory CTP formalism, the density matrix is represented as:

```
ρ(Φ₁, Φ₂, t) = ⟨Φ₁| ρ̂(t) |Φ₂⟩
```

The CTP (Φ₁, Φ₂) structure in GRUT's Galley truncation is formally compatible with this notation. The mathematical structure of a two-field kernel is present.

**The Φ₋ ghost disqualification:** The difference field Φ₋ = Φ₁ − Φ₂ satisfies:

```
dΦ₋/dt = +Φ₋ / τ
```

This is an **exponentially growing ghost mode**. The growth rate is real and positive (+1/τ). For a complex quantum structure, the imaginary part Im(Ψ) must evolve with an imaginary growth rate (oscillation, rotation), not a real positive one (exponential growth). Therefore:

```
PHI_MINUS_GROWTH_RATE_SIGN = +1   (positive → growing, not oscillating)
PHI_MINUS_CAN_BE_IMAGINARY_PART = False
```

Φ₋ cannot serve as the imaginary part of a complex wavefunction. The CTP doubling does not supply the complex structure J.

**The prior Hilbert space requirement:** Even setting aside the ghost-mode disqualification, the formal identification ρ(Φ₁,Φ₂) = ⟨Φ₁|ρ̂|Φ₂⟩ requires a prior Hilbert space to give meaning to |Φ₁⟩ and |Φ₂⟩ as basis states. GRUT does not supply that Hilbert space (Track B, SS6). The identification is therefore not a derivation — it is a formal compatibility at best.

**Appendix P:** compatible_but_ad_hoc — the CTP mapping is compatible with quantum notation, but not derived from GRUT architecture. The why-not-motivated reason is explicit: no prior Hilbert space, and the Φ₋ ghost mode disqualifies the complex structure interpretation (QA-R6 compliance).

---

## 7. Track F — Appendix P Status Per Result

Every Q-B finding carries an explicit Appendix P status class (QA-R1 compliance):

| Track | Finding | Appendix P Class |
|-------|---------|-----------------|
| A | Deterministic ODE is native closed structure | native_canon |
| B | No native quantum state space established | bounded_structural_result |
| C | Quantum pure/mixed states not natively supported | bounded_structural_result |
| D | Standard CCR route currently blocked | bounded_structural_result |
| E | CTP-to-density-matrix mapping compatible only | compatible_but_ad_hoc |
| **Q-B overall** | Bounded null result on quantum state space | **bounded_structural_result** |

**Adherence to Q-A charter discipline rules:**

- **QA-R1:** All quantum claims carry explicit Appendix P status classes ✓
- **QA-R2:** No native_canon assigned to any quantum claim ✓ (Track A NC is for classical ODE, not quantum claim)
- **QA-R4:** Bounded negative results preserved as BSR, not promoted to open questions ✓
- **QA-R5:** The Track E compatible_but_ad_hoc claim includes explicit statement of why not motivated ✓ (no prior Hilbert space, Φ₋ ghost) (QA-R6 compliance)
- **FFM6** (hilbert_space_from_ctp_doubling): explicitly identified and blocked ✓

---

## 8. Track G — Nonclaim Firewall

Seven explicit nonclaims registered at Q-B entry:

1. **NOT claiming** quantum mechanics cannot be added to GRUT — only that no native quantum state space is established in the current architecture.

2. **NOT claiming** CTP doubling is equivalent to Hilbert space structure — FFM6 from the Q-A charter explicitly prohibits this inference.

3. **NOT claiming** the first-order Lagrangian structure permanently blocks quantization — only that the standard CCR route ([Φ,Π]=iℏ via ∂L/∂(∂ₜΦ)) is currently blocked.

4. **NOT claiming** the bounded null verdict means GRUT is wrong — it is a BSR preserving the architectural gap with precision.

5. **NOT claiming** ρ(Φ₁,Φ₂) notation constitutes a derived density matrix — it is formally compatible only (CAH, compatible_only mapping verdict).

6. **NOT claiming** Φ₋ being a ghost permanently prevents all quantum extensions — it disqualifies the CTP structure as a complex structure J; other quantum extensions may be possible via MIP postulation.

7. **NOT claiming** a complex structure J cannot be consistently postulated — only that J is currently absent, and its addition requires motivated_independent_postulation classification minimum.

---

## 9. Architecture of the Quantum Gap

The Q-B audit confirms and refines the Q0 quantum gap assessment. The gap is architectural and well-defined:

**What GRUT has (quantum-adjacent):**
- Real linear configuration space (NC) — correct classical substrate
- CTP doubled field structure with retarded kernel (ER, Galley regime)
- Integer topological winding numbers (conditionally present, MIP)
- Z₂ reflection symmetry (NC)
- Scale selection via τ-ω₀ coupling (WCH)

**What GRUT lacks (quantum-essential):**
- Complex structure J with J² = −1 (absent — MIP if postulated)
- Hilbert space inner product (absent — requires J first)
- Born rule / probability normalization (absent)
- Operator algebra (absent)
- Canonical momentum Π (degenerate for first-order ODE)
- Complex amplitude wavefunction (absent — Φ is real)

**The precise missing element:** A complex structure J. Without J, the real linear space cannot become a complex Hilbert space. J is the single most fundamental absent ingredient. Once J is available (via MIP postulation), a Hilbert space inner product can in principle be defined, and the quantum program can proceed to Q-C (microdynamics).

**Why the gap is not vague:** The gap is not "we don't know how to do quantum mechanics in GRUT." It is the precise statement: GRUT has the real linear space; it needs J to proceed. This is a bounded structural result (BSR), not an open question.

---

## 10. What the Three Verdicts Mean

### Primary Verdict: `density_matrix_or_functional_state_required`

Pure state Hilbert space is architecturally ruled out: no complex amplitude, no normalization mechanism, no inner product. If quantum mechanics is to be embedded in GRUT, the minimum compatible structure is **density matrix / influence functional** — the open-system effective description already uses the same formal language. Even this minimum requires importing a Hilbert space not supplied by GRUT.

This verdict does not endorse the density matrix approach as "available" or "motivated" — it means: of all the state-space options audited, the functional/density-matrix approach is the least incompatible with what GRUT actually contains, and it is the minimum that could accommodate quantum descriptions of open systems.

### Commutation Verdict: `quantization_route_currently_blocked`

The standard canonical quantization route — which requires a second-order Lagrangian, a well-defined canonical momentum Π = ∂L/∂(∂ₜΦ), and the commutation relation [Φ,Π] = iℏ — is blocked by the first-order structure of the GRUT equation of motion. The Bateman/Galley doubled route gives a non-standard CCR involving the shadow field. No quantization route is currently available without a new structural postulate.

### Mapping Verdict: `compatible_only`

The CTP (Φ₁,Φ₂) structure is formally compatible with the quantum density matrix notation ρ(Φ₁,Φ₂) = ⟨Φ₁|ρ̂|Φ₂⟩. The mapping is not derived — it requires a prior Hilbert space that GRUT does not supply, and the Φ₋ ghost mode disqualifies the CTP structure as a complex quantum structure. The identification is compatible but ad hoc.

---

## 11. Readiness for Q-C

Q-B completes with a bounded structural result. The findings establish:

1. **The precise architectural gap:** J with J² = −1 is the missing ingredient.
2. **Why pure Hilbert space is ruled out:** no complex structure, no canonical momentum.
3. **Why density matrix / functional approach is the minimum compatible structure:** open-system character + CTP formal compatibility.
4. **Why standard canonical quantization is blocked:** first-order Lagrangian structure.

For Q-C (quantum microdynamics), the question becomes: assuming a complex structure J is postulated (MIP), what microdynamic law governs the resulting quantum-adjacent objects? Q-C must carry at minimum motivated_but_unbuilt or motivated_independent_postulation classification for any positive result, per QA-R3. If no microdynamic law can be identified, the Q-C success criterion is `bounded_negative` (BSR).

The Q-A charter authorizes proceeding to Q-C on the basis of Q-B completing with a well-documented BSR.

---

*Appendix P class: bounded_structural_result*
*Authorized by: Q-A quantum conceptual charter (quantum_program_authorized_and_staged)*
*Depends on: Q0 inventory (inventory_complete__quantum_gap_fully_documented)*
*Implemented in: grut/qb_quantum_state_space.py*
*Tests: tests/test_qb_quantum_state_space.py*
