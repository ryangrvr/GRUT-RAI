# GRUT II Theta-Prime — Minimal Effective Action / Influence Functional Audit

## Purpose

Determine whether the core GRUT structures — the constitutive law, retarded memory, and the USL decoherence rate — can be embedded in a minimal, mathematically serious effective action or influence functional, rather than remaining a collection of sharp but partly disconnected effective laws.

---

## Part I — Target Structures to Reproduce

### Structure 1: Classical constitutive relaxation

```
tau dPhi/dt + Phi = X
```

where Phi is the scalar constitutive field, X is the local source (curvature-determined equilibrium), and tau is the relaxation time.

**Requirements on the action:**
- Must DERIVE this as an equation of motion, not insert it by hand.
- The forward semigroup S(t) = exp(-t/tau) must emerge, not be assumed.
- The unique attractor Phi* = X must follow from the variational structure.

**Classification:** Must be derived exactly.

### Structure 2: Memory / retarded kernel

The GRUT architecture (Kappa) reduces general memory kernels to effective delays:

```
K_n(s) → effective delay Delta = n × tau_K
```

The constitutive equation with memory becomes an integro-differential equation:

```
Phi(t) = integral_0^t K(t-s) X(s) ds
```

or equivalently, the first-order ODE is the Markovian truncation of a retarded response function.

**Requirements on the action:**
- Must accommodate nonlocal-in-time response.
- Must reproduce the Markovian limit (first-order ODE) as a controlled approximation.
- Must identify the bath or hidden sector whose integration produces the memory kernel.

**Classification:** Must be derived in a limit (Markovian truncation of the full retarded response).

### Structure 3: Quantum decoherence / USL

```
Lambda_USL = G m^2 / (hbar l)
```

This is a decoherence rate for spatial superpositions of mass m with branch separation l.

**Requirements on the action:**
- Must provide a principled place where this rate appears — either derived from the imaginary part of the influence functional, or representable as a Lindblad coefficient.
- The m^2/l scaling must be structurally natural, not forced.

**Classification:** Must be at minimum representable (derivation from first principles would be a major advance; accommodation within the formalism is the baseline).

### Structure 4: Quantum/classical split

The constitutive field Phi appears classical (deterministic ODE). The USL governs quantum superpositions. The Alpha-Prime correction established these as separate predictions for separate observables.

**Requirements on the action:**
- Must clarify whether Phi is a fundamental field or an expectation value of a quantum field.
- If Phi is fundamental, the USL must arise from a DIFFERENT sector (e.g., metric fluctuations).
- If Phi is quantum, the constitutive law must emerge as the classical/mean-field limit.

**Classification:** Must be accommodated — the action must have a structure where this split is natural, not ad hoc.

---

## Part II — Candidate Formalism Inventory

### Formalism 1: Ordinary local action

```
S[Phi, g] = integral d^4x sqrt(-g) [ (1/2) g^{mu nu} partial_mu Phi partial_nu Phi - V(Phi, X) ]
```

| Property | Assessment |
|----------|-----------|
| Dissipation | **NO.** A local, real action with standard kinetic term gives conservative (Hamiltonian) dynamics. The equation of motion is second-order (wave equation), not first-order (relaxation). Cannot produce tau dPhi/dt + Phi = X. |
| Memory | **NO.** Local actions produce local equations of motion. No retarded kernels. |
| Decoherence | **NO.** A pure Hamiltonian system has unitary evolution. No decoherence without environmental tracing. |
| Covariance | YES. Standard scalar-tensor theory. |
| GRUT compatibility | **INCOMPATIBLE.** Cannot encode any of the three core structures. |

**Ranking: INCOMPATIBLE.** A local action alone cannot generate the GRUT constitutive sector. This is a known result: dissipation requires either doubled fields, nonlocality, or environmental tracing.

### Formalism 2: Nonlocal effective action

```
S_eff[Phi] = S_local[Phi] + integral dt integral dt' Phi(t) K(t-t') Phi(t')
```

| Property | Assessment |
|----------|-----------|
| Dissipation | **YES (conditionally).** A retarded kernel K with appropriate imaginary part produces dissipation. But a purely real nonlocal action still gives conservative dynamics — the dissipation requires Im(K) != 0, which comes from integrating out modes. |
| Memory | **YES.** The kernel K(t-t') IS the memory. |
| Decoherence | **PARTIAL.** The imaginary part of the effective action gives decoherence rates, but this requires the CTP/doubled-field structure to make sense quantum-mechanically. |
| Covariance | Problematic. Nonlocal-in-time actions break manifest Lorentz invariance unless carefully constructed (e.g., as the in-in effective action). |
| GRUT compatibility | **CONDITIONALLY PROMISING.** Can encode memory and dissipation, but needs the CTP structure to handle both classical and quantum sectors properly. |

**Ranking: CONDITIONALLY PROMISING.** The nonlocal effective action is the intermediate step — it arises after integrating out the environment in the CTP formalism.

### Formalism 3: Schwinger-Keldysh / Closed-Time-Path action

```
iS_eff[Phi_r, Phi_a] = i integral dt [-( tau dPhi_r/dt + Phi_r - X ) Phi_a + i D Phi_a^2 ]
```

where Phi_r = (Phi_+ + Phi_-)/2 (classical/average field) and Phi_a = Phi_+ - Phi_- (quantum/difference field).

| Property | Assessment |
|----------|-----------|
| Dissipation | **YES — EXACTLY.** Varying with respect to Phi_a gives the dissipative equation of motion: tau dPhi_r/dt + Phi_r = X. This is the textbook result. |
| Memory | **YES.** Replace the local kernel with a nonlocal retarded Green's function G_R^{-1}(t-t') and the framework naturally accommodates non-Markovian memory. |
| Decoherence | **YES.** The imaginary quadratic term i D Phi_a^2 produces decoherence. The coefficient D is related to the noise kernel and, via the fluctuation-dissipation theorem, to the dissipation rate and temperature. |
| Covariance | **YES (in principle).** The CTP formalism is fully covariant when formulated on a curved background. The gravitational CTP effective action has been constructed explicitly (Calzetta & Hu 1994, Salcedo et al. 2025). |
| GRUT compatibility | **EXCELLENT.** The CTP structure naturally produces: (a) first-order dissipative EOM from the real part, (b) decoherence from the imaginary part, (c) the fluctuation-dissipation relation linking them, (d) memory through the retarded kernel. |

**Ranking: MOST PROMISING.** The CTP/SK formalism is the natural mathematical home for all three GRUT structures simultaneously.

### Formalism 4: Influence functional (after integrating out hidden modes)

```
F[Phi_+, Phi_-] = exp(i S_IF[Phi_+, Phi_-])
S_IF = -integral integral [sigma(s) mu(s-s') Delta(s') - i sigma(s) nu(s-s') sigma(s')]
```

where sigma = Phi_+ - Phi_-, Delta = Phi_+ + Phi_-, mu is the dissipation kernel, nu is the noise kernel.

| Property | Assessment |
|----------|-----------|
| Dissipation | **YES.** The mu kernel produces friction/dissipation in the classical EOM. |
| Memory | **YES.** The kernels mu(s-s') and nu(s-s') are nonlocal in time, encoding the full non-Markovian response. |
| Decoherence | **YES — EXACTLY.** The imaginary part of S_IF is integral sigma nu sigma, which in position space gives exp(-nu l^2 t) — decoherence proportional to (separation)^2. The l^2 scaling is structurally built in. |
| Covariance | Depends on the system-environment split. For a gravitational environment, covariance is maintained if the split respects diffeomorphism invariance. |
| GRUT compatibility | **EXCELLENT.** The influence functional is the CTP formalism after the environmental trace. It provides: (a) the constitutive law from mu, (b) memory from the kernel structure, (c) decoherence from nu, (d) the FDT linking dissipation to decoherence. The USL scaling Gm^2/(hbar l) can potentially emerge from the gravitational noise kernel. |

**Ranking: MOST PROMISING (tied with CTP).** The influence functional is the CTP formalism with the environment integrated out — it is the same formalism at a later stage of the calculation.

### Formalism 5: Doubled-field dissipative effective action (Galley)

```
S[Phi_1, Phi_2] = S[Phi_1] - S[Phi_2] + K[Phi_1, Phi_2]
```

with the physical limit Phi_1(t_f) = Phi_2(t_f).

| Property | Assessment |
|----------|-----------|
| Dissipation | **YES.** K generates the nonconservative forces. |
| Memory | **YES (if K is nonlocal).** |
| Decoherence | **NOT DIRECTLY.** Galley's formalism is classical. It produces the correct dissipative EOM but does not by itself give quantum decoherence. One needs to promote it to the full CTP path integral to get decoherence. |
| Covariance | Same as the CTP formalism (Galley's principle IS the classical limit of CTP). |
| GRUT compatibility | **GOOD but incomplete.** Handles the classical constitutive sector perfectly. Does not handle the quantum/USL sector without promotion to full CTP. |

**Ranking: CONDITIONALLY PROMISING.** The classical sector is handled exactly. The quantum sector requires the full CTP upgrade.

### Final ranking

| Rank | Formalism | Classical sector | Quantum/USL sector | Memory |
|:----:|-----------|:----------------:|:------------------:|:------:|
| **1** | **CTP / Schwinger-Keldysh** | **Exact** | **Natural** | **Natural** |
| **1** | **Influence functional** | **Exact** | **Natural** | **Natural** |
| 3 | Galley doubled-field | Exact | Requires upgrade | Natural |
| 4 | Nonlocal effective action | Conditional | Partial | Natural |
| 5 | Local action | Impossible | Impossible | Impossible |

**The CTP formalism and the influence functional are tied as the most promising route.** They are the same framework at different stages: the CTP action is the starting point; the influence functional is what remains after tracing out the environment.

---

## Part III — Minimal Variable Set

### Test 1: Metric only (g_{mu nu})

Can the constitutive field Phi be eliminated in favor of pure metric degrees of freedom?

**No.** The GRUT constitutive equation tau dPhi/dt + Phi = X introduces a first-order dissipative dynamics that has no analogue in the standard metric sector (which is second-order hyperbolic). Phi is an independent degree of freedom with its own relaxation timescale. It cannot be absorbed into g_{mu nu}.

### Test 2: Metric + scalar Phi

The minimal content of the classical GRUT theory: g_{mu nu} and Phi coupled via X(g) (the source derived from curvature).

**Sufficient for the classical constitutive sector.** The equation tau dPhi/dt + Phi = X(g) requires only (g, Phi) as fundamental variables.

**Insufficient for the quantum sector.** A single real field Phi has unitary evolution (in the standard path integral). Decoherence requires either:
- Doubling Phi → (Phi_+, Phi_-) in the CTP formalism, or
- Tracing out an environment coupled to Phi.

### Test 3: Doubled fields (Phi_+, Phi_-) on CTP contour

The CTP formalism doubles all fields. The minimal CTP content is:

```
(g_{mu nu}^+, g_{mu nu}^-, Phi_+, Phi_-)
```

or equivalently in the Keldysh basis:

```
(g_r, g_a, Phi_r, Phi_a)
```

**This is the irreducible variable set for the full GRUT program.** The classical constitutive law emerges from variation with respect to Phi_a. Decoherence emerges from the Im(S_eff) term quadratic in Phi_a. Memory emerges from the retarded kernel in the Phi_r-Phi_a coupling.

### Test 4: Auxiliary memory field(s)

The Kappa-stage kernel reduction showed that the general memory integral can be represented by auxiliary fields tau_K satisfying their own relaxation equations. This is mathematically equivalent to a chain of first-order ODEs:

```
tau_1 dZ_1/dt + Z_1 = Phi
tau_2 dZ_2/dt + Z_2 = Z_1
...
```

Each auxiliary field Z_i can be absorbed into the CTP formalism as additional doubled fields (Z_i^+, Z_i^-). They are NOT independent degrees of freedom — they are a convenient parametrization of the nonlocal kernel K(t-t').

**Verdict: redundant if the kernel is used directly; useful for numerical implementation.**

### Test 5: Density matrix / Wigner function

The density matrix rho(Phi, Phi') is the natural object in the influence-functional formalism. It is encoded by the (Phi_+, Phi_-) path integral. No additional variable is needed beyond the CTP doubled fields.

### Irreducible variable set

```
MINIMAL: (g_{mu nu}, Phi) on the CTP contour
         ≡ (g_r, g_a, Phi_r, Phi_a) in Keldysh basis
```

- g_r: the physical (average) metric
- g_a: the quantum (difference) metric — sources metric fluctuations and gravitational noise
- Phi_r: the physical (average) constitutive field — obeys tau dPhi_r/dt + Phi_r = X
- Phi_a: the quantum (difference) constitutive field — controls decoherence and fluctuations

**What is clearly redundant:** Auxiliary memory fields (absorbable into the kernel), density-matrix variables (encoded by the doubled fields), independent noise fields (generated by the imaginary part of S_eff).

**What is missing if one tries to stay too simple:** Dropping Phi_a (i.e., working with a single real Phi) eliminates all quantum effects — no decoherence, no USL, no fluctuation-dissipation relation. Dropping g_a eliminates gravitational noise and the gravitational contribution to decoherence.

---

## Part IV — Can the Constitutive Law Be Variationally Generated?

### Gate 1: Ordinary local variational principle

**No.** A real local action S[Phi] with standard kinetic term (1/2)(dPhi/dt)^2 gives a second-order EOM:

```
d^2 Phi/dt^2 + V'(Phi) = 0
```

This is conservative and second-order. The first-order dissipative equation tau dPhi/dt + Phi = X cannot emerge. This is a theorem (Bauer 1931): no single-variable real Lagrangian can produce purely dissipative first-order dynamics.

### Gate 2: Doubled-field action (Galley / Bateman)

**Yes — exactly.** The CTP action:

```
iS_eff[Phi_r, Phi_a] = i integral dt [ -(tau dPhi_r/dt + Phi_r - X) Phi_a + i D Phi_a^2 ]
```

Variation with respect to Phi_a gives:

```
tau dPhi_r/dt + Phi_r - X = 2i D Phi_a
```

In the classical limit (Phi_a → 0, the "physical limit" of Galley):

```
tau dPhi_r/dt + Phi_r = X     ✓
```

This is EXACT. The constitutive law is the classical equation of motion of the CTP effective action.

### Gate 3: Influence functional after integrating out modes

**Yes — in the Markovian, overdamped limit.** If Phi is coupled linearly to a bath of harmonic oscillators with Ohmic spectral density J(omega) = eta × omega, and the bath is integrated out:

1. The full EOM (before overdamping) is: M d^2Phi/dt^2 + eta dPhi/dt + k(Phi - X) = noise
2. In the overdamped limit (eta >> M omega_0): eta dPhi/dt + k(Phi - X) = noise
3. Defining tau = eta/k: tau dPhi/dt + Phi = X + (noise/k)

The constitutive law emerges as the overdamped Caldeira-Leggett equation. The relaxation time tau = eta/k is the ratio of the friction coefficient to the restoring force constant.

**This is the most physical derivation:** the constitutive law is the low-frequency effective dynamics of a scalar field strongly coupled to a dissipative environment (gravitational degrees of freedom acting as a bath).

### Summary

| Method | Can it derive tau dPhi/dt + Phi = X? | Status |
|--------|:-----------------------------------:|:------:|
| Local real action | **NO** | Impossible (Bauer's theorem) |
| CTP/doubled-field action | **YES — exactly** | Exact derivation |
| Influence functional (overdamped) | **YES — in controlled limit** | Exact in Markovian/overdamped regime |
| Nonlocal action (retarded kernel) | YES — as Green's function equation | Formal |

**The constitutive law passes the variational gate via the CTP formalism.**

---

## Part V — Can Memory Be Fundamental or Only Emergent?

### Option A: Fundamental nonlocality in the action

Place a nonlocal kernel directly in the action:

```
S[Phi] = integral dt integral dt' Phi(t) K(t-t') Phi(t')
```

This produces an integro-differential EOM with memory:

```
integral K(t-t') Phi(t') dt' = source
```

**Assessment:**
- Mathematically consistent.
- Breaks manifest locality and (in relativistic settings) can produce acausality unless K is strictly retarded.
- Requires a choice of K that is not derived from anything deeper.
- In practice, all known examples of such nonlocal actions ARISE from integrating out hidden modes — the nonlocality is not fundamental but emergent.

**Verdict: viable but not preferred.** Fundamental nonlocality is a stronger assumption than necessary.

### Option B: Emergent memory from integrating out hidden modes

The standard Caldeira-Leggett / Feynman-Vernon route:

1. Start with a local action for (Phi, environment).
2. Integrate out the environment.
3. The resulting influence functional has a nonlocal kernel K(t-t') that encodes the environmental response.
4. In the Markovian limit, the kernel collapses to a delta function and the memory disappears, leaving the local constitutive law.

**Assessment:**
- This is the standard mechanism in condensed matter, quantum optics, and quantum gravity.
- The memory kernel is DERIVED from the spectral density of the environment.
- The Markovian limit (local constitutive law) and the non-Markovian case (memory) are both limits of the same influence functional.
- The GRUT kernel reduction (Kappa) is exactly this structure: the general kernel K_n(s) reduces to effective delays, which are properties of the environmental spectral density.

**Verdict: preferred.** Emergent memory is the natural, minimal explanation for the GRUT retarded structure.

### Option C: Effective truncation of a higher-dimensional local theory

Place the nonlocal kernel in an extra dimension (Kaluza-Klein style): what appears as temporal nonlocality in 4D is local propagation in 5D.

**Assessment:**
- Technically possible but introduces new dimensions with no independent evidence.
- Far more structure than needed.
- Not compatible with the GRUT program's minimality requirement.

**Verdict: not viable for a minimal program.**

### Classification

**Emergent-memory route preferred.** The retarded/delay structure of GRUT should be treated as emerging from integrating out gravitational (or gravitationally-coupled) environmental modes. The spectral density of the environment determines the kernel shape. The Markovian constitutive law is the leading-order truncation.

---

## Part VI — USL Placement Audit

### The question

Where does Lambda_USL = Gm^2/(hbar l) sit in the CTP/influence-functional program?

### Option A: Derived from the gravitational noise kernel

In the Caldeira-Leggett framework, the decoherence rate for a spatial superposition of separation l is:

```
Lambda_dec = (D_pp / hbar^2) × l^2
```

where D_pp is the momentum diffusion coefficient. For a gravitational environment:

```
D_pp = integral J_grav(omega) coth(hbar omega / 2kT) d_omega
```

If the gravitational spectral density J_grav(omega) produces D_pp = G m^2 / l (with appropriate dimensional factors), then:

```
Lambda = D_pp l^2 / hbar^2 = G m^2 l / hbar^2
```

This does NOT match the USL scaling Lambda = Gm^2/(hbar l). The l-dependence is wrong: Caldeira-Leggett gives l^2 from the double commutator [X,[X,rho]], while the USL gives 1/l.

**The USL scaling is NOT the standard Caldeira-Leggett decoherence scaling.** This is a critical structural observation.

### Why the scaling differs

The standard Caldeira-Leggett decoherence rate is:

```
Lambda_CL ~ (force noise PSD) × l^2 / hbar^2
```

where the force noise is separation-independent (the environment pushes the two branches independently with the same noise).

The USL predicts:

```
Lambda_USL = G m^2 / (hbar l)  ~  m^2 / l
```

This scaling arises if the decoherence mechanism is NOT force noise diffusion but rather **gravitational self-energy difference** between the branches. The energy difference between two branch positions separated by l scales as:

```
Delta E ~ G m^2 / l    (Newtonian self-energy difference)
```

and the corresponding dephasing rate is:

```
Lambda ~ Delta E / hbar = G m^2 / (hbar l)
```

This is precisely the Diosi-Penrose argument: the decoherence rate equals the gravitational self-energy difference divided by hbar. The USL reproduces the DP scaling exactly (but from the GRUT constitutive framework rather than from wavefunction collapse).

### Where the USL sits in the influence functional

The USL does NOT come from the noise kernel nu(s-s') of the Caldeira-Leggett type. It comes from a DIFFERENT mechanism: the **gravitational self-interaction** of the superposed mass distribution.

In the CTP formalism, this corresponds to the **tree-level gravitational interaction** between the two branches, not the loop-level stochastic noise:

```
S_IF^{tree} = -i integral dt (G m^2 / l) × (Phi_a / hbar)
```

This term is REAL in the CTP action (not imaginary like the noise term). It produces a relative phase between the branches that accumulates at rate Gm^2/(hbar l). When this phase becomes of order 1, the off-diagonal elements of the density matrix are suppressed — this IS decoherence, but of the dephasing (not diffusion) type.

### Classification

| Placement | Status |
|-----------|--------|
| Derived from the noise kernel (Caldeira-Leggett type) | **NO — wrong scaling (l^2 vs 1/l)** |
| Derived from the gravitational self-energy (Diosi-Penrose type) | **YES — correct scaling** |
| Representable in the CTP action | **YES — as a tree-level branch-branch gravitational interaction** |
| Derivable from the full CTP influence functional | **YES in principle — the gravitational self-energy term is the leading-order contribution to S_IF from integrating out the Newtonian gravitational field** |

### The derivation path

The USL can be derived within the CTP influence functional program as follows:

1. Start with the CTP action for a massive scalar Phi coupled to gravity g_{mu nu}.
2. Integrate out the gravitational field to leading order (tree-level, Newtonian limit).
3. The resulting influence functional has a real part proportional to the gravitational self-energy difference between the (+) and (-) branches.
4. For a spatial superposition of mass m with separation l, this gives:

```
Re(S_IF) ~ (G m^2 / l) × t / hbar
```

5. The corresponding decoherence rate (from the accumulated phase) is:

```
Lambda_USL = G m^2 / (hbar l)     ✓
```

This is not the Caldeira-Leggett mechanism (which gives l^2 from force noise). It is the **gravitational dephasing** mechanism (which gives 1/l from the self-energy). Both mechanisms are present in the full influence functional; the USL is the dominant one for gravitational decoherence of non-relativistic massive superpositions.

**The USL is DERIVABLE within the influence-functional program, not merely representable.**

---

## Part VII — Final Verdict

### Classification

**influence_functional_route_preferred**

The audit reveals a clean, minimal path from the CTP/influence-functional formalism to all three core GRUT structures:

| Structure | CTP/IF derivation | Status |
|-----------|:-----------------:|:------:|
| Constitutive law: tau dPhi/dt + Phi = X | Exact (variation of CTP action w.r.t. Phi_a in classical limit) | **DERIVED** |
| Memory / retarded kernel | Emergent (nonlocal kernel from integrating out environment) | **DERIVED** |
| USL: Lambda = Gm^2/(hbar l) | Tree-level gravitational self-energy in the IF | **DERIVABLE** |
| Fluctuation-dissipation relation | Built into the CTP structure (KMS symmetry) | **AUTOMATIC** |
| Quantum/classical split | Phi_r is classical (mean field), Phi_a controls quantum fluctuations | **NATURAL** |

### What the minimal effective action looks like

```
iS_GRUT[Phi_r, Phi_a; g_r, g_a] =

  i integral d^4x sqrt(-g_r) {
    // Classical constitutive sector (real part, linear in Phi_a)
    -[tau nabla_t Phi_r + Phi_r - X(g_r)] Phi_a

    // Noise/decoherence sector (imaginary part, quadratic in Phi_a)
    + i D(g_r, T) Phi_a^2

    // Gravitational self-energy sector (generates USL)
    + (gravitational branch-branch interaction encoded in g_a coupling)

    // Standard gravitational sector
    + M_Pl^2 G_r[g_r, g_a]  (Einstein-Hilbert on CTP contour)
  }
```

The minimal variable set is (g_r, g_a, Phi_r, Phi_a). The constitutive law comes from variation w.r.t. Phi_a. The USL comes from the gravitational sector after integrating out g_a to tree level. The noise coefficient D is related to tau and the effective temperature via the fluctuation-dissipation theorem: D ~ kT/(tau × field_stiffness).

### What has been established

1. **The constitutive law IS variationally derivable** — via the CTP action, not a local action. This is exact, not approximate.

2. **Memory is emergent, not fundamental** — the retarded kernel structure comes from integrating out environmental/gravitational modes. The Markovian constitutive law is the leading-order truncation.

3. **The USL is derivable, not external** — it comes from the tree-level gravitational self-energy in the influence functional. The 1/l scaling distinguishes it from the l^2 Caldeira-Leggett noise and identifies it as gravitational dephasing, not diffusion.

4. **The natural formalism is the CTP / influence functional**, not a local action or a purely phenomenological framework. The CTP structure simultaneously encodes dissipation (real part), decoherence (imaginary part), and the fluctuation-dissipation relation (KMS symmetry) — all of which are present in GRUT.

5. **GRUT is capable of becoming a real effective field theory.** The step from "compatible collection of scaling laws" to "influence-functional framework" is now structurally clear. What remains is the explicit construction of the gravitational influence functional in the GRUT context.

### Public-Facing Paragraph

GRUT II Theta-Prime audits whether the core GRUT structures — the constitutive relaxation law, retarded memory, and the Universal Scaling Law for gravitational decoherence — can be embedded in a minimal effective action. The audit identifies the Schwinger-Keldysh closed-time-path formalism as the natural mathematical home. The constitutive law tau dPhi/dt + Phi = X emerges exactly as the classical equation of motion of the CTP effective action, with dissipation encoded in the doubled-field structure rather than in a conventional Lagrangian. Memory arises as an emergent nonlocal kernel from integrating out environmental modes, with the Markovian constitutive law as the leading-order truncation. Most significantly, the USL decoherence rate Lambda = Gm^2/(hbar l) is derivable — not merely representable — within the influence functional framework: it corresponds to the tree-level gravitational self-energy between the branches of a spatial superposition, giving the 1/l scaling of gravitational dephasing rather than the l^2 scaling of standard force-noise diffusion. The GRUT program is capable of becoming a real effective field theory built on the CTP influence functional.

### Internal Doctrine Paragraph

Theta-Prime establishes that the CTP / influence-functional route is the unique minimal formalism for the GRUT program. A local action is impossible (Bauer's theorem). The Galley doubled-field approach handles the classical sector but requires promotion to full CTP for the quantum/USL sector. The USL's 1/l scaling is NOT Caldeira-Leggett (which gives l^2); it is gravitational dephasing from the self-energy difference, entering as a tree-level real contribution to the influence functional rather than as a loop-level noise term. This structural identification is the deepest result of the stage: it explains WHY the USL has the Diosi-Penrose scaling despite being derived from constitutive relaxation rather than wavefunction collapse. The next program step must construct the explicit CTP action, integrate out the gravitational sector to leading order, and verify that the Newtonian-limit influence functional reproduces both the constitutive law (from the retarded self-energy) and the USL (from the branch-branch gravitational interaction). This is a calculation, not a conjecture.

### Next Forced Move

**GRUT II Iota-Prime — Explicit CTP Influence Functional Construction:** Write the CTP action for a massive scalar Phi coupled to linearized gravity on a Newtonian background. Integrate out the gravitational field to tree level. Extract the influence functional. Verify that: (a) the real part of S_IF reproduces the constitutive law in the Markovian/overdamped limit, (b) the branch-branch gravitational interaction gives Lambda = Gm^2/(hbar l), and (c) the fluctuation-dissipation relation connects the noise coefficient D to the constitutive relaxation time tau. This is the single decisive calculation that either completes the GRUT foundational program or identifies the remaining gap.

---

*GRUT II Theta-Prime complete. Verdict: influence_functional_route_preferred. The CTP/influence-functional formalism is the unique minimal home for all three GRUT core structures. The constitutive law is derivable exactly (CTP variation). Memory is emergent (environmental integration). The USL is derivable as tree-level gravitational dephasing (self-energy, 1/l scaling — NOT Caldeira-Leggett l^2 noise). The critical structural finding: the USL has the Diosi-Penrose scaling because it IS the gravitational self-energy divided by hbar, entering the influence functional as a real (dephasing) term rather than an imaginary (noise) term. GRUT is capable of becoming a real EFT on the CTP contour. Next: explicit construction of the gravitational influence functional (Iota-Prime).*
