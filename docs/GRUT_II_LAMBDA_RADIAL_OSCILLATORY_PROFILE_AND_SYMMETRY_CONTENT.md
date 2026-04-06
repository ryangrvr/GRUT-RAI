# GRUT II Lambda — Radial Oscillatory Profile and Symmetry-Content Audit

## Is the Oscillatory Phase Gravitationally Quiet by Structure?

---

## Part I — Radial Oscillatory Profile

### The Setup

The oscillatory regime has Phi(t) and tau(t) oscillating at frequency omega_c ~ 1/Delta. On a gravitational background, tau_local(r) varies with radius via Level-1:

```
tau_local(r) = tau_0 * t_dyn(r) / (tau_0 + t_dyn(r))
```

where t_dyn(r) = sqrt(r^3 / (2GM)).

The DDE at each radius:

```
tau_local(r) * dPhi(r,t)/dt + Phi(r,t) = X(r) + beta*(tau_field(r,t) - tau_star)
tau_meta * d(tau_field(r,t))/dt + tau_field(r,t) = tau_star + h(Phi(r, t - Delta) - X(r))
```

### The Oscillation at Each Radius

At each r, the system has the same DDE structure but with DIFFERENT tau_local(r). The Hopf bifurcation condition depends on tau_local:

```
Hopf condition: beta * gamma > critical_gain(tau_local, tau_meta)
```

Since tau_local varies with r, the Hopf condition is met at SOME radii and not others. There is a CRITICAL RADIUS r_Hopf where the oscillatory instability first appears:

- For r < r_Hopf: tau_local is small (strong field); oscillation possible
- For r > r_Hopf: tau_local is large (weak field); stable (no oscillation)

### The Oscillation Envelope

The oscillation amplitude A(r) varies with radius:

- Near the compact object (small r): tau_local small → strong constitutive dynamics → oscillation amplitude determined by the local DDE parameters
- Far from the object (large r): tau_local → tau_0 → Hopf condition NOT met → A(r) → 0

The envelope A(r) is NOT uniform. It is concentrated near the compact object and decays outward. The transition from oscillating to non-oscillating occurs at r_Hopf.

### Key Structural Result

**The oscillatory envelope A(r) has RADIAL STRUCTURE.** It is not a uniform l=0 perturbation at all radii. The oscillation exists inside r_Hopf and vanishes outside. This creates a SHELL of oscillatory constitutive activity with finite radial extent.

---

## Part II — Symmetry Decomposition

### Is the oscillatory phase purely l = 0?

**YES, on a spherically symmetric background.**

The DDE system at each radius depends only on r (through tau_local(r) and X(r) = M/r^2). On a SPHERICALLY SYMMETRIC background:

- The oscillation Phi(r,t) depends on (r, t) only — no angular dependence
- delta_rho(r,t) = d(rho)/d(Phi) * delta_Phi(r,t) + d(rho)/d(tau) * delta_tau(r,t)
- Both delta_Phi and delta_tau depend only on (r, t)
- Therefore delta_rho(r, t) is a function of (r, t) only
- Its spherical-harmonic decomposition is PURELY l = 0

**No l >= 1 content arises from the DDE on a spherically symmetric background.**

This is a structural result, not an approximation. The constitutive equation has no mechanism to generate angular dependence from radially symmetric sources. The oscillation is purely radial.

### What about the oscillation ENVELOPE?

The envelope A(r) varies with r. But it is still spherically symmetric — it depends on r, not on (theta, phi). The envelope creates a radially structured l = 0 perturbation (a pulsation), not an l >= 2 perturbation.

### Consequence for Gravitational Radiation

**Birkhoff's theorem:** A spherically symmetric perturbation (l = 0) of a spherically symmetric spacetime produces NO gravitational radiation. This is exact in GR.

The oscillatory phase, on a spherically symmetric background, is gravitationally SILENT at all multipoles. No GW emission. Not from quadrupole, not from any higher multipole. The monopolar pulsation changes the mass function m(r, t) but not in a way that radiates.

---

## Part III — Source of Nonsphericity Audit

### What extra structure would generate l >= 2?

| Source | Classification | l >= 2 Content |
|--------|---------------|----------------|
| **Rotation** (Kerr background) | Admissible extension (+0P; real BHs rotate) | YES — frame dragging couples l = 0 oscillation to l = 2 through Coriolis-like term |
| **Binary companion** | External perturbation | YES — tidal field provides l = 2 seed |
| **Nonradial perturbation of the oscillatory mode** | Internal instability analysis needed | POSSIBLE — if the l = 0 oscillation is unstable to nonradial perturbations, l >= 2 content grows spontaneously |
| **Background metric perturbation** (l >= 2) | External | YES (trivially) |
| **Defect sector anisotropy** | Bridge-level (O(3) hedgehog has angular structure) | YES — the hedgehog ansatz Phi^a = eta f(r) r_hat^a BREAKS spherical symmetry through the r_hat direction. If the constitutive oscillation couples to the defect via portal, the angular structure of the defect could imprint l >= 2 content |
| **Mode coupling via portal** | Already in architecture (D8 portal: g_p Phi^2 |vec_Phi|^2) | CONDITIONAL — if scalar Phi oscillates and couples to the defect field via portal, the defect's angular gradient (eta^2 f^2/r^2) acquires time-dependent modulation. This modulation IS l = 2 through the hedgehog's angular structure |

### The Most Promising Route: Portal-Mediated Defect Coupling

The O(3) hedgehog field vec_Phi = eta f(r) r_hat has INTRINSIC angular structure. The function r_hat(theta, phi) = (sin theta cos phi, sin theta sin phi, cos theta) contains l = 1 spherical harmonics. The ENERGY DENSITY of the hedgehog:

```
eps_defect = (1/2) eta^2 (f')^2 + eta^2 f^2/r^2 + ...
```

The angular gradient term eta^2 f^2/r^2 is l = 0 (spherically symmetric in the hedgehog). BUT the hedgehog field itself is NOT spherically symmetric — it only produces a spherically symmetric ENERGY DENSITY by the hedgehog ansatz.

If the constitutive scalar Phi(t) oscillates and couples to the defect via portal:

```
Portal: g_p Phi(r,t)^2 |vec_Phi|^2 = g_p Phi(r,t)^2 eta^2 f(r)^2
```

This is STILL spherically symmetric (Phi and f are functions of r only).

**The portal coupling does NOT generate l >= 2 content on a spherically symmetric background.** Even though the hedgehog field has internal angular structure, the energy density is l = 0 by the hedgehog ansatz.

### The Only Routes to l >= 2

1. **Rotation (Kerr):** The spinning background couples l = 0 constitutive oscillation to l = 2 metric perturbation through frame dragging. This is PHYSICAL (real compact objects rotate) but is an EXTENSION (Kerr background not yet in the GRUT II formalism).

2. **Nonradial instability:** If the spherical l = 0 oscillation is unstable to nonradial perturbations (like a pulsating star can be unstable to bar-mode or other deformations), l >= 2 content grows. This requires a stability analysis of the oscillatory phase against nonradial perturbations — NOT yet done.

3. **Binary tidal field:** In a binary system, the companion's tidal field provides an l = 2 seed. The oscillatory constitutive phase could RESONANTLY COUPLE to the tidal field if the cycle frequency matches the orbital frequency. This is speculative but physically natural.

---

## Part IV — Gravity Follow-Up Decision

### On a spherically symmetric background:

**GW route structurally closed at leading order.**

The oscillatory phase is purely l = 0. Birkhoff's theorem prevents GW emission. No quadrupolar content arises from the constitutive DDE alone on a spherically symmetric background.

### On a rotating (Kerr) background:

**GW route open with explicit symmetry breaking.**

Rotation couples l = 0 oscillation to l >= 2 metric perturbation. This is a real physical effect but requires extending GRUT II to Kerr backgrounds.

### From nonradial instability:

**Unknown.** The stability of the l = 0 oscillatory phase against nonradial perturbations has not been analyzed. If the spherical oscillation is unstable to bar-mode deformation, l = 2 content grows spontaneously.

---

## Part V — Final Verdict

### oscillatory_phase_strictly_spherical.

On a spherically symmetric background, the GRUT II oscillatory constitutive phase is purely l = 0. No quadrupolar or higher-multipole content arises from the constitutive DDE, the Level-1 tau modulation, or the portal coupling to the defect sector. Birkhoff's theorem makes the oscillatory phase gravitationally silent.

The oscillatory phase IS a real constitutive phase of the theory (distinct from the settled phase in spectral content, average field values, and relaxation rate). But it does not radiate gravitational waves on a spherically symmetric background.

### Public-Facing Paragraph

GRUT II Lambda establishes that the oscillatory constitutive scaling phase — one of two coexisting phases in the delayed scaling theory — is purely spherically symmetric (l = 0) on a spherically symmetric gravitational background. The radial oscillation profile varies with radius through the Level-1 tau reduction, creating a shell of constitutive activity concentrated near the compact object. But this shell is spherically symmetric: Birkhoff's theorem prevents gravitational-wave emission. The oscillatory phase is a real dynamical phenomenon of the constitutive vacuum — it represents a distinct scaling regime with different average field values, different relaxation rates, and different spectral content from the settled phase — but it is gravitationally quiet by structure. Nonspherical content (l >= 2), required for gravitational radiation, would require additional ingredients: rotation (Kerr background), tidal interaction (binary systems), or nonradial instability of the oscillatory mode.

### What Survives If Strictly Spherical

Even with the GW route closed on spherical backgrounds, the GRUT II scaling phase theory retains:

1. **Two coexisting constitutive phases** (settled vs oscillatory) — first multi-basin deterministic result in the program
2. **History-dependent regime selection** — the outcome depends on the constitutive history
3. **Kernel-derived delay architecture** (Kappa: gamma kernel → effective DDE)
4. **Distinct constitutive signatures** (17% Phi difference, 16% tau, qualitative spectral difference)
5. **A concrete scaling phase structure** for the responsive vacuum

These are real theoretical results. They describe a vacuum with constitutive memory that can exist in two qualitatively different dynamical states. This is new physics in the constitutive vacuum sector — even if it is gravitationally quiet.

### The Single Next Forced Move

**Determine whether the oscillatory phase is stable against nonradial perturbations.** If the l = 0 oscillation is unstable to l >= 2 deformations (bar-mode or higher), nonspherical content grows spontaneously and the GW route reopens without external ingredients. This is a linear stability analysis of the periodic orbit in the DDE system, extended to include angular perturbations — a well-defined mathematical problem.

If the oscillation is nonradially stable: the GW route is closed on spherical backgrounds, and the oscillatory phase is a constitutive phenomenon only.

If it is nonradially unstable: the most important instability in the GRUT II program.

---

*GRUT II Lambda complete. Oscillatory phase: strictly spherical on spherical background. GW route: closed at leading order. Constitutive phase structure: intact and physically distinct. Next: nonradial stability analysis.*
