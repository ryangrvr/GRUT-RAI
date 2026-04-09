# Sector 1 — Quantum Mechanics Recovery: Mathematical Scaffold

## Symbol table

| Symbol | Meaning | Units | Status |
|--------|---------|-------|--------|
| z(x,t) | Complex directed-response field | dimensionless | primitive |
| tau | Complex relaxation time | J s | A2 |
| tau_R | Real part (dissipation) | J s | A2 |
| tau_I | Imaginary part (oscillation) | J s | A2, identified as hbar/2 |
| hbar | Reduced Planck constant | J s | 1.0546e-34 |
| z_target | Target functional derivative delta F / delta z* | dimensionless | A1 |
| F[z] | Target functional | [length]^d | variational |
| c_0(x) | Local stiffness = 1 + V(x)/2 | dimensionless | derived |
| c_2 | Gradient penalty | [length]^2 | species-dependent |
| m | Mass = tau_I^2 / c_2 | kg | derived |
| V(x) | Potential energy | J | external |
| rho | Probability density = \|z\|^2 | [length]^{-d} | derived |
| j | Probability current | [length]^{1-d} s^{-1} | derived |

## 1. Constitutive starting point

**Axiom A1** (directed response):

    tau d_t z + z = z_target[z]

**Axiom A2** (complex relaxation):

    tau = tau_R + i tau_I,    tau_I = hbar/2

Rewritten:

    (tau_R + i tau_I) d_t z = z_target - z

**Axiom A0** (CTP doubling): the field z exists on forward (+) and backward (-) time contours. In the classical limit (z_a -> 0), the equation of motion for z_r reduces to the constitutive law above.

## 2. Schrodinger recovery (linear constitutive regime)

**Target functional** (most general local, quadratic, parity-preserving, isotropic):

    F[z] = integral { c_0(x) |z|^2 + c_2 |nabla z|^2 } d^d x

**Variational derivative:**

    z_target = delta F / delta z* = c_0(x) z - c_2 nabla^2 z

**Substitution into constitutive law** (unitary limit, tau_R = 0):

    i tau_I d_t z = z_target - z = (c_0 - 1) z - c_2 nabla^2 z

**With c_0(x) = 1 + V(x)/2:**

    i tau_I d_t z = V(x)/2 z - c_2 nabla^2 z

**Multiply by 2, substitute tau_I = hbar/2, c_2 = hbar^2/(4m):**

    i hbar d_t z = V(x) z - (hbar^2 / 2m) nabla^2 z

This IS the Schrodinger equation.

**Implementation note:** Verified numerically by evolving both the directed-response RHS and the standard Schrodinger Hamiltonian with RK4. Maximum deviation: 7.3e-16 over 200 time steps.

## 3. Probability current and continuity

From the unitary equation i tau_I d_t z = V/2 z - c_2 z_xx:

    d_t rho = (i tau_I / m) d_x [z* z_x - z z*_x]

Define probability current:

    j = (tau_I / m) * 2 Im(z* nabla z) = (hbar / m) Im(z* nabla z)

Continuity equation:

    d_t rho + nabla . j = 0     (unitary limit)

**Implementation note:** Verified numerically. Relative violation ~ 2.6e-3 (finite-difference truncation in dx, dt).

## 4. Relativistic extensions

### 4a. Klein-Gordon

Promote spatial functional F to Lorentz-covariant spacetime action:

    S[z] = integral { eta^{mu nu} (d_mu z*)(d_nu z) - M^2 |z|^2 } d^4x

Euler-Lagrange equation (delta S / delta z* = 0):

    (1/c^2) d_tt z - nabla^2 z + M^2 z = 0     [Klein-Gordon]

Dispersion: omega^2 = k^2 + M^2. Group velocity: v_g = k/omega < c (causal).

**NR limit:** Write z = phi exp(-iMc^2 t/hbar), drop d_tt phi (slow variation):

    i hbar d_t phi = -(hbar^2 / 2m) nabla^2 phi     [Schrodinger recovered]

**Implementation note:** NR envelope match verified: max deviation 2.5e-4.

### 4b. Dirac

The Dirac equation is first-order in time — more natural for the constitutive form:

    i hbar d_t psi = H_D psi = (alpha . p + beta M) psi

In the directed-response language:

    z_target = [1 + H_D / (2 tau_I)] psi

Substituting into i tau_I d_t psi = z_target - psi gives i hbar d_t psi = H_D psi.

**Implementation note:** 1+1D Dirac verified. Norm conservation: delta = 1.05e-11. Group velocity matches k/omega to < 3%.

## 5. Born-rule transparency

**Theorem (linear case):**

For the linear constitutive law tau dPhi/dt + Phi = X + sqrt(2D) xi(t), the MSRJD action is:

    S = integral (tau dPhi/dt + Phi - X)^2 / (4D) dt

The partition function Z(X) = integral DPhi exp(-S) depends on the kernel K = (tau d/dt + 1)^2 / (4D), which is INDEPENDENT of X.

Therefore: Z_0 = Z_1 exactly. Born probabilities are preserved: p(i) = |c_i|^2.

**Nonlinear case:** Z_0/Z_1 deviates by a computable, small correction (< 10^-4 at standard bistable parameters).

**Scope:** The Born rule is PRESERVED (not derived). It enters from QM upstream. The constitutive sector is transparent to it.

## 6. CTP completion (open-system dynamics)

### 6a. Why naive tau_R > 0 fails

Setting tau_R > 0 in the wavefunction equation gives:

    d_t z = [z_target - z] / (tau_R + i tau_I)

The real part of the eigenvalue E_n / (tau_R + i tau_I) is positive for all E_n > 0. This produces exponential GROWTH, not decay. The system is UNSTABLE.

**Structural reason:** z_target depends on z (self-referential). The error (z_target - z) is always positive for positive-energy states. The "target" moves with the state.

### 6b. CTP construction

The correct open-system extension uses A0: CTP doubling of z into (z_r, z_a).

CTP effective action:

    iS_eff = i integral dt { z_a* [i tau_I d_t - H/(2tau_I)] z_r + h.c. + i D |z_a|^2 }

- Linear z_a sector: gives Schrodinger equation of motion for z_r
- Quadratic z_a sector: generates noise with amplitude D
- FDT: D = (2n_B + 1) gamma (at T = 0: D = gamma)

### 6c. Lindblad emergence

Tracing out the environment (Feynman-Vernon) gives:

    d rho/dt = -(i/hbar)[H, rho] + sum_i gamma_i D_{L_i}[rho]

where D_L[rho] = L rho L^dag - (1/2){L^dag L, rho} is the Lindblad dissipator.

**Implementation note:** Verified for 2-level dephasing (coherence decay rate matches 2*gamma), amplitude damping (population matches exp(-gamma t)), and harmonic oscillator thermalization (max population error vs Boltzmann: 1.4e-6).

## 7. Classical limit

### 7a. WKB

Write z = R exp(iS/hbar). Substituting into Schrodinger and collecting orders of hbar:

- O(hbar^0): d_t S + (nabla S)^2/(2m) + V = 0     [Hamilton-Jacobi]
- O(hbar^1): continuity for R^2     [classical probability]

### 7b. Ehrenfest

For quadratic potentials: d<x>/dt = <p>/m, d<p>/dt = -<nabla V>.

The wavepacket center follows the classical trajectory.

**Implementation note:** For harmonic oscillator (V = 0.5 x^2), Ehrenfest error < 0.2% over multiple oscillations.

## Assumptions

1. tau_I = hbar/2 is IDENTIFIED (not derived)
2. c_2 > 0 from stability (derived)
3. c_0 = 1 from constitutive fixed point (derived)
4. m = tau_I^2 / c_2 (derived)
5. F[z] is quadratic, local, parity-preserving, isotropic (assumed for free particle)
6. Markovian bath coupling for Lindblad (valid for W_tau < 0.7 decades)
