# Book IV — Target Alpha: Configuration-Space Topology and Collective-Coordinate Quantization

## Formal Derivation Memo

**Predecessor:** Book IV Target Alpha — Native Fermion-Emergence Audit
**Relation:** Advances the same physical question via a distinct mathematical lens (Finkelstein–Rubinstein collective-coordinate quantization) rather than field-level transformation law.

---

## 1. Executive Verdict

The Finkelstein–Rubinstein mechanism sharpens the fermionic obstruction from "build spinorial structure from scratch" to "select the fermionic quantization sector of an already-existing moduli space with π₁ = ℤ₂."

The single-defect moduli space M₁ = ℝ³ × SO(3) has fundamental group ℤ₂. By the Finkelstein–Rubinstein theorem, quantum mechanics on M₁ admits two inequivalent quantization sectors: a bosonic sector (wavefunctions single-valued on SO(3)) and a fermionic sector (wavefunctions double-valued on SO(3), single-valued on the universal cover SU(2)). The two-defect exchange space has a nontrivial exchange loop, and the Finkelstein–Rubinstein extension links the single-defect quantization choice to the exchange sign: fermionic single-defect quantization implies antisymmetric exchange.

However, the GRUT architecture provides no mechanism to select the fermionic sector. The topology permits it. The dynamics do not force it. The τ₁ dissipative structure, far from helping, is plausibly hostile to the mechanism: contractive dynamics on the orientational moduli space tends to trivialize the non-contractible loops that the Finkelstein–Rubinstein mechanism would exploit. No Wess-Zumino-Witten term, no Berry phase, and no equivalent selection mechanism is present in the current architecture.

The obstruction is therefore sharpened and reorganized, not removed. Under the Finkelstein–Rubinstein framework, the three-layer fermionic obstruction (spinorial structure / antisymmetrization / spin-statistics) becomes conditionally downstream of a single gap — quantization-sector selection — provided that such selection can actually be justified. Until it is, the fermionic sector remains topologically available but physically unselected.

**Classification:** Bounded structural result (BSR). Advances the structural characterization of the fermionic obstruction. Does not resolve it.

---

## 2. Single-Defect Moduli-Space Setup

### 2.1 The Raw Configuration Space

The O(3) sigma model places a triplet field Φᵃ(x) (a = 1, 2, 3) on ℝ³, with the constraint |Φᵃ|² = η² defining the target manifold S². The raw field configuration space is the space of all smooth maps from ℝ³ to S² satisfying appropriate boundary conditions — an infinite-dimensional function space.

### 2.2 The Fixed-Winding Finite-Energy Sector

Finite-energy configurations with Φᵃ → η v̂ᵃ as |x| → ∞ (for some fixed vacuum direction v̂ᵃ) are classified by their topological winding number n ∈ π₂(S²) = ℤ. For fixed n, the space of finite-energy maps decomposes into disjoint sectors labeled by n. We focus on n = 1, the minimal nontrivial winding sector.

### 2.3 The Hedgehog Family and Collective Coordinates

Within the n = 1 sector, the spherically symmetric hedgehog ansatz takes the form:

Φᵃ(x) = η f(|x − X₀|) Rᵃ_b (x − X₀)ᵇ / |x − X₀|

where:
- X₀ ∈ ℝ³ is the center position of the defect
- R ∈ SO(3) is a global internal rotation applied to the hedgehog
- f(r) is the radial profile function solving the boundary-value problem f(0) = 0, f(∞) = 1

For fixed boundary conditions and fixed winding number, the profile f(r) is determined by the field equation (it is not a free modulus — it is the solution of the radial ODE inherited from the sigma-model energy functional). The free parameters are:

- **Position:** X₀ ∈ ℝ³ (3 translational degrees of freedom, corresponding to spatial translation symmetry)
- **Orientation:** R ∈ SO(3) (3 rotational degrees of freedom, corresponding to the diagonal action of spatial SO(3) × internal O(3) on the hedgehog)

The profile modulus is absent because the radial equation admits a unique solution (up to the discrete choice of winding number) for the given boundary conditions.

### 2.4 The Moduli Space

The moduli space of physically distinct single-defect configurations of winding number n = 1 is therefore:

**M₁ = ℝ³ × SO(3)**

with dim(M₁) = 3 + 3 = 6.

Since ℝ³ is contractible (it deformation-retracts to a point), all topological content of M₁ resides in the SO(3) factor. The position degrees of freedom provide spatial localization of the defect but contribute nothing to the rotation or spinorial analysis.

### 2.5 What SO(3) Is Topologically

SO(3) is diffeomorphic to RP³ (real projective 3-space) — the space of lines through the origin in ℝ⁴, or equivalently the 3-sphere S³ with antipodal points identified:

SO(3) ≅ RP³ ≅ S³ / {±1}

This identification is not incidental. It is the geometric statement of the double-cover relation SU(2) → SO(3). The group SU(2) is topologically S³ (simply connected). The map SU(2) → SO(3) identifies each g ∈ SU(2) with −g, producing the quotient S³/{±1} = RP³ = SO(3).

---

## 3. Single-Defect π₁ Analysis

### 3.1 Computation

The fundamental group of a product space is the product of the fundamental groups:

π₁(M₁) = π₁(ℝ³ × SO(3)) = π₁(ℝ³) × π₁(SO(3)) = 0 × ℤ₂ = **ℤ₂**

This is exact. The computation relies on two standard results:
- π₁(ℝ³) = 0 (ℝ³ is contractible)
- π₁(SO(3)) = π₁(RP³) = ℤ₂ (the fundamental group of real projective space in any dimension n ≥ 2 is ℤ₂)

### 3.2 Geometric Meaning

A loop in M₁ that rotates the hedgehog orientation by 2π (one full turn in SO(3)) is **non-contractible**: it represents the nontrivial element of ℤ₂. It cannot be continuously deformed to a constant loop while remaining in SO(3).

A loop that rotates by 4π **is contractible**: it represents the identity in ℤ₂ (since 1 + 1 = 0 in ℤ₂). This is the "belt trick" — a belt twisted by 720° can be untwisted without moving its endpoints, but a 360° twist cannot.

### 3.3 Critical Distinction: Loop Topology vs. Field Endpoint

The non-contractibility of the 2π loop is a property of the **path space** of the moduli manifold. It says: two paths in SO(3) that differ by a 2π rotation are topologically inequivalent — they cannot be continuously deformed into each other.

It does **not** say: the hedgehog field configuration at the endpoint of a 2π rotation is different from the starting configuration. The hedgehog field Φᵃ is a vector (a section of the adjoint bundle of SO(3)). Under a 2π rotation R(2π) = I ∈ SO(3), the field returns to itself exactly:

Φᵃ → R(2π)ᵃ_b Φᵇ = δᵃ_b Φᵇ = Φᵃ

The field sees no sign flip. The topology lives in the **loop**, not in the **value**.

This distinction is the entire substance of the Finkelstein–Rubinstein mechanism: whether a quantum-mechanical wavefunction defined on M₁ must be single-valued (returning to the same value after traversing a non-contractible loop) or may be double-valued (acquiring a sign −1 after traversing the non-contractible loop).

---

## 4. Finkelstein–Rubinstein Spinorial Activation Test

### 4.1 The Theorem

**Finkelstein–Rubinstein (1968), Sorkin (1983):** Let M be the configuration space of a classical soliton, and suppose π₁(M) = ℤ₂. Then quantum mechanics on M admits two inequivalent quantization sectors, classified by the group homomorphisms Hom(π₁(M), ℤ₂):

- **Trivial homomorphism** (sends the generator of ℤ₂ to +1): Wavefunctions are single-valued on M. The soliton transforms under integer-spin representations of the rotation group. Statistics: bosonic.

- **Nontrivial homomorphism** (sends the generator of ℤ₂ to −1): Wavefunctions are double-valued on M — they acquire a factor of (−1) when transported around the non-contractible 2π loop. Equivalently, these wavefunctions are single-valued on the universal cover of M. The soliton transforms under half-integer-spin representations. Statistics: fermionic.

### 4.2 Mathematical Framework

The two quantization sectors correspond to two inequivalent flat complex line bundles over M₁. Flat line bundles on M₁ are classified by the holonomy representation:

Hom(π₁(M₁), U(1))

The ℤ₂ subgroup of U(1) — the group {+1, −1} — provides the two physically distinct choices. The trivial holonomy (+1 around every loop) gives the bosonic bundle. The nontrivial holonomy (−1 around the non-contractible 2π loop) gives the fermionic bundle.

Wavefunctions in the bosonic sector are ordinary functions on SO(3), expandable in Wigner D-matrices D^j_{mm'}(R) with integer j = 0, 1, 2, .... These represent spin-0, spin-1, spin-2, ... solitons.

Wavefunctions in the fermionic sector are sections of the nontrivial flat line bundle, expandable in Wigner D-matrices with half-integer j = 1/2, 3/2, 5/2, .... These represent spin-1/2, spin-3/2, ... solitons.

Both sectors are mathematically well-defined. Both are consistent with the topology of M₁. The topology does not select between them.

### 4.3 What Selects the Sector in the Skyrme Model

In the standard Skyrme model, the selection is made by a topological term in the action: the Wess-Zumino-Witten (WZW) term, proportional to an integer N_c (identified physically with the number of quark colors):

Γ_WZW = (N_c / 240π²) ∫_{B⁵} ω₅

where ω₅ is the Wess-Zumino 5-form and B⁵ is a five-dimensional ball whose boundary is the spacetime history of the soliton. The coefficient N_c determines the quantization sector:

- N_c odd → fermionic sector (skyrmions are fermions)
- N_c even → bosonic sector (skyrmions are bosons)

For QCD with N_c = 3 (three colors), the skyrmion is a fermion — reproducing the fact that baryons (protons, neutrons) are fermions despite being composed of three quarks in an antisymmetric color singlet.

### 4.4 GRUT Status

The GRUT architecture contains:
- The O(3) sigma model with hedgehog configurations → provides M₁ = ℝ³ × SO(3) with π₁ = ℤ₂ ✓
- No Wess-Zumino-Witten term → no selection mechanism ✗
- No analogue of N_c → no integer that could determine the sector ✗
- No other topological term in the effective action that could serve as a substitute ✗

**Verdict:** The Finkelstein–Rubinstein fermionic quantization sector is topologically permitted by the structure of M₁. It is not selected by any dynamical or topological mechanism in the current GRUT architecture.

The gap is precisely characterized: it is a **quantization-sector selection problem**, not a "build spinorial structure" problem. The spinorial structure (the nontrivial flat line bundle over M₁) already exists as a mathematical object. What is missing is a physical reason to place the wavefunction on it rather than on the trivial bundle.

---

## 5. Two-Defect Exchange Topology

### 5.1 The Two-Defect Configuration Space

Consider two identical hedgehog defects, both with winding number n = 1. Each defect has position Xᵢ ∈ ℝ³ and orientation Rᵢ ∈ SO(3). The configuration space before imposing identity is:

C̃₂ = {(X₁, R₁, X₂, R₂) ∈ (ℝ³ × SO(3))² : X₁ ≠ X₂}

The condition X₁ ≠ X₂ excludes coincident positions (where the two-defect description breaks down). For identical defects, the physical configuration space is the quotient by the symmetric group S₂ exchanging the two particles:

C₂ = C̃₂ / S₂

### 5.2 Exchange Loops in Three Dimensions

An exchange path is a continuous path in C₂ that starts at (X₁, R₁, X₂, R₂) and ends at the same physical configuration but with the labels swapped: what was defect 1 is now defect 2 and vice versa. In the quotient C₂, this is a closed loop.

In three spatial dimensions, the fundamental group of the position-exchange space is:

π₁(Conf₂(ℝ³) / S₂) = S₂ = ℤ₂

An exchange loop is non-contractible, but performing the exchange twice is contractible. This is the symmetric group, not the braid group. (The braid group, which supports anyonic statistics, arises only in two spatial dimensions where Conf₂(ℝ²)/S₂ has π₁ = ℤ, the infinite cyclic group.)

### 5.3 The Finkelstein–Rubinstein Extension to Exchange

The Finkelstein–Rubinstein framework extends naturally to the multi-soliton setting. The key result is:

**If the single-soliton wavefunction lives in the nontrivial (fermionic) quantization sector, then the two-soliton wavefunction acquires a factor of (−1) under exchange.**

This is not an independent postulate. It follows from the topology: the exchange path in C₂ can be continuously deformed into a path that rotates one of the two solitons by 2π while keeping the other fixed. If the single-soliton wavefunction picks up a (−1) under 2π rotation (fermionic sector), then the exchange also produces (−1).

This provides a soliton spin-statistics connection: spin-1/2 solitons automatically have fermionic exchange statistics, and spin-0 solitons automatically have bosonic exchange statistics. Importantly, this connection does **not** require Lorentz invariance — it follows from the topology of the configuration space alone.

### 5.4 GRUT Status

The two-defect exchange loop exists and is non-contractible. The Finkelstein–Rubinstein extension links exchange statistics to the single-defect quantization-sector choice. But:

- If the single-defect quantization sector is bosonic (the default in the absence of a selection mechanism), then the exchange sign is +1 (bosonic statistics).
- If the single-defect quantization sector is fermionic (selected by a WZW term or equivalent), then the exchange sign is −1 (fermionic statistics, antisymmetry, exclusion).

**The exchange sign is not independently determined.** It inherits whatever the single-defect quantization choice produces. Since the current architecture makes no selection, the exchange sign is also unselected.

---

## 6. Role of τ₁ Dissipative Dynamics

### 6.1 Dissipation on the Moduli Space

The GRUT constitutive equation τ dΦ/dt + Φ = X generates a forward contraction semigroup S(t) = exp(−t/τ) on the field space. When projected onto the finite-dimensional moduli space M₁, this dynamics becomes a dissipative flow on the collective coordinates.

On the orientational factor SO(3), which is compact and connected, the character of this flow is constrained by elementary dynamical-systems theory. A smooth dissipative flow on a compact connected manifold generically converges to an attractor set — typically a finite collection of fixed points (equilibria).

### 6.2 Contractive Dynamics Tends to Trivialize Topology

The Finkelstein–Rubinstein mechanism requires non-contractible loops in M₁ to be dynamically accessible. A quantum-mechanical wavefunction must be able to explore the full SO(3) orientational space, including paths that wind around the non-contractible 2π loop.

Dissipative flow acts against this. As the orientational dynamics contracts toward fixed-point attractors, the dynamically accessible region of SO(3) shrinks. In the long-time limit, the effective configuration space collapses toward a neighborhood of the attractor set. The fundamental group of a point (or a finite set of points) is trivial. The non-contractible loops that the FR mechanism would exploit become dynamically inaccessible.

This is a strong indication — though not a rigorous theorem in full generality — that dissipation is topologically hostile to the Finkelstein–Rubinstein mechanism. The constitutive semigroup does not enrich the configuration-space topology. It degrades it.

### 6.3 Caveats

Two caveats prevent stating this as a theorem:

First, the projection of the infinite-dimensional field dynamics onto the finite-dimensional moduli space is itself an approximation (the collective-coordinate approximation). The fidelity of this projection for GRUT's dissipative dynamics has not been rigorously established.

Second, the dissipative dynamics on M₁ depends on the source term X. If X drives the system persistently (rather than decaying), the orientational dynamics may not converge to a fixed point. However, persistent driving requires continuous external input, which is not a feature of the isolated-defect problem.

### 6.4 Summary

Dissipation appears topologically hostile to the Finkelstein–Rubinstein mechanism. Contractive dynamics tends to trivialize the non-contractible loops that the mechanism would exploit. No dissipative selection of the fermionic quantization sector is found. This strengthens the Target Alpha finding from "dissipation is irrelevant to the spinorial obstruction" to "dissipation is plausibly antagonistic."

---

## 7. SU(2) / Hopf / Qubit Track C Audit

### 7.1 Quantization on SO(3) and the SU(2) Lift

Quantum mechanics on SO(3) is well-understood. The Hilbert space of square-integrable functions on SO(3) decomposes into irreducible representations labeled by integer spin j = 0, 1, 2, ..., spanned by the Wigner D-matrices D^j_{mm'}(R).

To access half-integer representations (j = 1/2, 3/2, ...), one must work on the universal cover SU(2) = S³. The Wigner D-matrices for half-integer j are well-defined on SU(2) but double-valued on SO(3): they satisfy D^j_{mm'}(−g) = (−1)^{2j} D^j_{mm'}(g), so for half-integer j they change sign under the ℤ₂ identification g ~ −g that defines SO(3) = SU(2)/ℤ₂.

Both quantizations — on SO(3) (integer spin only) and on SU(2) (integer and half-integer spin) — are mathematically consistent. The choice between them is the Finkelstein–Rubinstein quantization-sector selection.

### 7.2 The Hopf Fibration

The Hopf fibration

S³ →^{S¹} S²

provides the geometric relationship between SU(2) and the structures already present in the O(3) sigma model. Here:
- The total space S³ = SU(2)
- The base space S² is the target manifold of the sigma model (the vacuum manifold)
- The fiber S¹ = U(1) carries the phase redundancy distinguishing SU(2) from SO(3)

The physical content of the Hopf fiber is precisely the sign ambiguity ±1 in the double-cover SU(2) → SO(3). If the hedgehog's orientation is parameterized by a point in SO(3), then lifting to SU(2) introduces an additional S¹ = U(1) degree of freedom. The ℤ₂ ⊂ U(1) subgroup is the "spinorial sign" that distinguishes bosonic from fermionic wavefunctions.

### 7.3 The Qubit / C² Sector

The extension-level SU(2) observable algebra from Appendix Q-II.D provides a C² state space carrying the fundamental (spin-1/2) representation of su(2). The operators σ_z, σ_x, σ_y are the generators of su(2) acting on the qubit Hilbert space.

This C² sector is an observable algebra — it describes what can be measured on a two-state quantum system — not a collective-coordinate wavefunction on the defect moduli space. The Target Alpha audit identified a Track C conjecture: could the qubit C² sector be identified with the Hopf fiber of the O(3) defect sector?

### 7.4 Is SU(2) Forced by the Topology?

**No.** The topology of SO(3), with π₁ = ℤ₂, *admits* the SU(2) universal cover. It does not *require* quantization on SU(2). Quantization on SO(3) with single-valued wavefunctions is perfectly consistent — it simply restricts to the integer-spin (bosonic) sector.

The question "is SU(2) forced?" would have a positive answer only if some physical consistency condition — unitarity, locality, anomaly cancellation, or equivalent — demanded the fermionic sector. No such condition has been identified within the GRUT architecture.

### 7.5 Track C Status

The qubit–Hopf identification conjecture remains at Track C (exploratory). It is:
- Geometrically suggestive (the Hopf fiber carries exactly the representation that the qubit sector provides)
- Not demonstrated (no mechanism connects the collective-coordinate orientation space to the qubit observable algebra)
- Not forced (no consistency condition requires the identification)

---

## 8. Minimal Bridge Diagnosis

### 8.1 Candidate Bridge Mechanisms

Three candidate mechanisms could select the fermionic quantization sector. They are ranked by structural motivation, from strongest to weakest:

**Candidate 1: Wess-Zumino-Witten Topological Term**

The WZW term is the unique next-order topological term in the derivative expansion of the O(3) sigma model, just as the Skyrme term L₄ is the unique next-order dynamical (4-derivative) term (documented in Appendix N, Route 3). In the standard Skyrme model, the WZW term with integer coefficient N_c selects the fermionic (N_c odd) or bosonic (N_c even) quantization sector, and simultaneously determines the exchange statistics via the Finkelstein–Rubinstein extension.

- **What it adds:** A topological term in the effective action, parameterized by one integer.
- **Classification:** Bridge-level (Track B). The WZW term is identified as the strongest candidate. It is not derived from GRUT-native structure. It is not yet installed. Its nativity would need a dedicated audit.
- **Scope:** Selects both the single-defect spin and the two-defect exchange sign. This is the only candidate that resolves spin and statistics simultaneously with a single postulate.
- **Postulate cost:** 1 topological term + 1 integer parameter.

**Candidate 2: Berry Phase from Coupling Structure**

If adiabatic transport of a quantum state around a 2π orientational loop accumulated a geometric phase of exactly π, this would select the fermionic sector without an explicit action-level topological term. Such a Berry phase could in principle arise from the coupling between the defect's collective coordinates and the quantum kinematic package.

- **What it adds:** A derived geometric phase from existing coupling structure.
- **Classification:** Track C (exploratory). No GRUT-native coupling structure has been shown to generate the required Berry phase. The dissipative dynamics (Section 6) works against this route.
- **Scope:** Would select spin. Exchange-statistics link would follow from FR extension.
- **Postulate cost:** 0 (if derived), but derivation has not been achieved and dissipation is hostile.

**Candidate 3: Explicit SU(2) Lift Postulate**

Simply declare that physical wavefunctions on the defect moduli space are defined on SU(2) rather than SO(3) — i.e., postulate the fermionic quantization sector directly.

- **What it adds:** A discrete choice (quantize on SU(2) rather than SO(3)).
- **Classification:** Track B (bridge), minimal motivation. Pure declaration with no dynamical justification.
- **Scope:** Would select spin. Exchange-statistics link follows from FR extension.
- **Postulate cost:** 1 discrete postulate. No dynamical content.

### 8.2 Updated Bridge Cost Comparison

| Framework | Bridge Items | What Is Resolved | Conditional On |
|-----------|-------------|-----------------|----------------|
| Target Alpha (field-level) | 3: SU(2) cover + spinor field ψ_α + antisymmetrization rule | Spin + exchange + exclusion independently | Nothing beyond the postulates |
| FR + WZW (this memo) | 1: WZW topological term (+ integer N_c) | Spin + exchange simultaneously via topology | Collective-coordinate quantization (requires quantum kinematic package at MIP level) |
| FR + explicit lift | 1: SU(2) lift postulate | Spin + exchange via topology | Same |

The Finkelstein–Rubinstein framework offers a more economical bridge: one topological term (or one discrete postulate) rather than three independent items. The economy arises because the FR mechanism automatically links spin to exchange statistics through topology, eliminating the need for independent antisymmetrization and spin-statistics postulates.

However, this economy is conditional. It requires that collective-coordinate quantization on M₁ is a valid description of the defect's quantum mechanics. This in turn requires the quantum kinematic package (complex structure J, compatible inner product g) from Appendices Q-B and Q-B.5, which stands at MIP (motivated independent postulation) level — not native canon.

---

## 9. Hard-Gated Verdict Table

| Test | Verdict | Reason |
|------|---------|--------|
| One-defect nontrivial π₁ | **YES** | π₁(M₁) = π₁(SO(3)) = ℤ₂, exact computation |
| 4π topology physically active | **NO** | Non-contractible 2π loop exists in moduli space; no mechanism activates it as physical sign change |
| Native spinorial transformation law | **NO** | Hedgehog is spin-1; field returns to itself after 2π; wavefunction defaults to single-valued |
| FR fermionic quantization sector permitted | **YES** | Hom(ℤ₂, ℤ₂) = ℤ₂ provides exactly two quantization sectors; fermionic sector is mathematically well-defined |
| FR fermionic quantization sector selected | **NO** | No WZW term, no Berry phase, no equivalent selection mechanism in current architecture |
| Two-defect nontrivial exchange loop | **YES** | π₁(Conf₂(ℝ³)/S₂) = ℤ₂; exchange loop is non-contractible in 3D |
| Exchange-sign / antisymmetry precursor | **NO** | Exchange sign inherits from single-defect quantization choice, which is unselected |
| Dissipative topology restriction | **HOSTILE** | Contractive dynamics on SO(3) tends to trivialize non-contractible loops; strong indication, not rigorous theorem |
| SU(2) forced by topology | **NO** | Topology permits SU(2) lift; does not require it; quantization on SO(3) alone is consistent |
| Minimal bridge needed | **1 topological term (WZW)** | Would select both spin and statistics; conditional on prior quantum kinematic package (MIP level) |

---

## 10. Nonclaims

1. NOT claiming π₁ = ℤ₂ therefore fermions derived — topological prerequisite is not dynamical selection; two quantization sectors exist but neither is preferred by the architecture.

2. NOT claiming Finkelstein–Rubinstein theorem applies therefore GRUT has fermions — the theorem establishes the existence of two sectors, not the selection of the fermionic one.

3. NOT claiming fermionic quantization sector permitted therefore fermionic sector selected — permission is weaker than selection; selection requires a dynamical or topological input not yet present.

4. NOT claiming two-defect exchange loop exists therefore antisymmetry established — the exchange loop is non-contractible, but the exchange sign is determined by the single-defect quantization choice, which is unselected.

5. NOT claiming WZW term identified as bridge candidate therefore WZW term derived or native — identification of the candidate is not derivation from GRUT structure; nativity audit remains future work.

6. NOT claiming obstruction sharpened and reorganized therefore obstruction resolved — the three-layer obstruction becomes conditionally downstream of one gap under FR, but that conditionality is itself unresolved.

7. NOT claiming dissipation is hostile therefore fermionic program blocked — hostility is a strong indication from attractor analysis, not a rigorous impossibility theorem; driven systems may behave differently.

8. NOT claiming collective-coordinate quantization analyzed therefore quantization justified as native GRUT description — the FR framework is analyzed as a candidate bridge mechanism; its validity as a GRUT-native description of defect quantum mechanics has not been established.

---

## 11. Three-Layer Obstruction Update

| Layer | Pre-Alpha Status | Post-Alpha Status | Post-This-Memo Status |
|-------|-----------------|-------------------|----------------------|
| Layer 1: Spinorial structure | blocked (no Hopf/spinor) | refined: π₁(SO(3)) = ℤ₂ identified as topological prerequisite | **further refined:** FR mechanism identifies the exact gap as quantization-sector selection (WZW or equivalent) |
| Layer 2: Antisymmetrization | blocked (no mechanism) | unchanged | **conditionally linked:** FR extension shows exchange sign follows automatically from single-defect quantization choice |
| Layer 3: Spin-statistics bridge | blocked (no Lorentz → no standard theorem) | unchanged | **conditionally absorbed:** FR soliton spin-statistics connection operates without Lorentz invariance, via configuration-space topology |

**Precise characterization of the advance:**

Under the Finkelstein–Rubinstein framework, Layers 2 and 3 become conditionally downstream of Layer 1, provided a fermionic quantization-sector selection is actually justified. If such a selection mechanism (WZW term or equivalent) were installed, the antisymmetrization rule and spin-statistics connection would follow automatically from the topology of M₁ and C₂, without independent postulation.

This is a structural reorganization of the obstruction, not a resolution. The reorganization is valuable because it reduces the apparent complexity from three independent gaps to one gap with two conditional downstream consequences. But the one remaining gap — quantization-sector selection — is itself unresolved.

---

## 12. Complementarity with Wilczek–Zee / Hopf Route

The existing fermionic emergence analysis in the sealed program (documented in `grut/fermionic_emergence_audit.py` and Appendix R-E) approaches the spinorial question through the **Wilczek–Zee / Hopf-term** lens:

- π₃(S²) = ℤ provides a topological invariant (the Hopf invariant)
- A θ-term with θ = π in the O(3) sigma-model action would endow solitons with fermionic statistics
- This is a **Lagrangian-level** (action-level) mechanism: a topological term in the action determines the quantum statistics

This memo uses the **Finkelstein–Rubinstein / collective-coordinate** lens:

- π₁(SO(3)) = ℤ₂ provides two quantization sectors on the moduli space
- Selection of the nontrivial sector endows solitons with fermionic statistics
- This is a **Hamiltonian-level** (quantization-level) mechanism: the choice of Hilbert-space bundle over M₁ determines the quantum statistics

These two approaches are not in conflict. They are dual descriptions of the same physical question:

- The Wilczek–Zee θ-term in the action **is** the Lagrangian-level mechanism that, when translated to the Hamiltonian picture, selects the nontrivial quantization sector on M₁
- The Finkelstein–Rubinstein quantization-sector choice **is** the Hamiltonian-level consequence of having (or not having) the θ-term in the action

Both approaches agree on the conclusion: the topology permits fermionic statistics; the current GRUT architecture does not provide the mechanism (θ-term / WZW term / equivalent) that would force the selection. The two frameworks provide complementary perspectives on the same gap.

---

## 13. Next Derivation Recommendation

The quantization-sector selection gap is the single remaining obstruction under the Finkelstein–Rubinstein reorganization. The direct assault on this gap is a dedicated **WZW-term existence and nativity audit**, which should determine:

1. **Does the O(3) sigma-model EFT admit a WZW-like topological term in the GRUT context?** The WZW term requires the field to take values in a group manifold (or coset space) with π₃ ≠ 0. For the O(3) sigma model on S², the relevant homotopy is π₃(S²) = ℤ (the Hopf invariant). The topological term exists mathematically. The question is whether the GRUT architecture's effective action naturally includes it.

2. **Is the WZW term unique?** In the standard O(3)/Skyrme context, the WZW term is the unique topological term at the relevant order in the derivative expansion. Is this uniqueness preserved in the GRUT context with its dissipative constitutive structure?

3. **Can a GRUT analogue of the selecting integer N_c be constrained?** In QCD, N_c = 3 (number of colors). GRUT has no color degrees of freedom. Is there a structural integer in the GRUT architecture that could play the role of N_c? Candidates: the winding number n = 1 of the hedgehog; the dimensionality of the O(3) triplet (= 3); other structural integers from the sealed program.

4. **What is the exact postulate cost?** If the WZW term must be independently postulated, what does it add to the Z-B accounting baseline (7/3/0/0)?

5. **Does the WZW term select both spin and exchange statistics?** In the Skyrme model, yes — via the Finkelstein–Rubinstein extension. Confirm this carries over to the GRUT O(3) context.

This audit would be the most direct possible test of whether the fermionic quantization sector can be activated within the GRUT architecture at acceptable postulate cost.

---

*Configuration-space topology memo complete. The Finkelstein–Rubinstein mechanism sharpens the fermionic obstruction to a single quantization-sector selection gap. The topology permits. The dynamics do not force. The next direct assault is a WZW-term nativity audit.*
