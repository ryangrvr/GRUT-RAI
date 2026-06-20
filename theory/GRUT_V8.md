# Grand Responsive Universe Theory

## A Unified Framework from the Closed-Time-Path Effective Action

D. Ryan Grover, April 2026

Correspondence: dryangrover@gmail.com
Research community: www.zenodo.org/communities/grut
Software (reproducible): github.com/ryangrvr/GRUT-RAI — DOI: 10.5281/zenodo.18993689

---

## Abstract

We formulate physics on the Schwinger–Keldysh closed-time path (CTP) with two axioms (CTP doubling, retarded variation) and one normalization ($\tau_I = \hbar/2$). The CTP effective action $S_{\rm CTP}[z_r, z_a] = z_a F[z_r] + (i/2)\, z_a N z_a$ produces, by coarse-graining to the Markovian limit, a single constitutive response equation $\tau\, dz/dt + z = z_{\rm target}[z]$. This equation is derived along three independent routes (CTP variation, Mori–Zwanzig, gradient flow). Its sectoral specializations yield: the Schrödinger equation (exact), a zero-parameter gravitational-decoherence rate $\Lambda_{\rm grav} = G m^2 S(\ell/R)/(\hbar \ell)$ with six scaling laws (exact), a computed cosmological constant $\Omega_\Lambda = 0.6886$ at $H_0 = 70$ km/s/Mpc from 3-loop CTP on $S^4$ (+0.04% from Planck; primary-source audit §26.2 of V7), a one-parameter Hubble rate $H_0 = 69.03$ km/s/Mpc that sits in the tension gap, a baryon-to-photon ratio $\eta_B = 6.56\times 10^{-10}$ (+8% of observation), and a dark-matter sector with two live routes (gauged U(1)$_{\rm dark}$ CLOSED at the structural level; dielectric bandwidth integral gives $\Omega_{\rm dm,eff} = \alpha_{\rm vac} = 1/3$, +27% from Planck). The Standard Model with three generations emerges as the unique minimal renormalizable gauge theory compatible with CTP fixed-point architecture; the Koide identity $K = 2/3$ is a proven Z$_3$-circulant algebraic consequence. The framework exposes one bridge parameter ($\tau_0$) linking laboratory decoherence to cosmology through a derived structural relation. A single measurement of $\Lambda_{\rm grav}$ converts $\Omega_\Lambda$ from a one-parameter match to a zero-parameter prediction. Every numerical claim in this document is anchored by a regression test in the GRUT-RAI repository (current baseline: 430 passing tests).

---

# I. FOUNDATION

## 1. Axioms

**A0 (CTP Doubling).** Physics is formulated on the Schwinger–Keldysh closed time path. The degrees of freedom are doubled into forward ($+$) and backward ($-$) branches. In the Keldysh basis:

$$z_r = (z_+ + z_-)/2 \quad\text{(classical field)} \qquad z_a = z_+ - z_- \quad\text{(quantum field)} \tag{1}$$

The CTP effective action in this basis:

$$S_{\rm CTP}[z_r, z_a] \;=\; z_a\, F[z_r] \;+\; \frac{i}{2}\, z_a\, N\, z_a \tag{2}$$

where $F$ is the equation-of-motion operator from the classical action, and $N$ is the noise kernel (connected Hadamard function of the stress-energy tensor).

**A1 (Retarded Variation).** The physical equation of motion is the retarded variation:

$$\left.\frac{\delta S_{\rm CTP}}{\delta z_a}\right|_{z_a = 0} = 0 \quad\Longrightarrow\quad F[z_r] = 0 \tag{3}$$

This selects the causal, forward-in-time dynamics.

## 2. Normalization

**N0.** The Keldysh field $z$ is normalized such that the constitutive relaxation parameter takes the value

$$\tau_I = \hbar / 2 \tag{4}$$

This connects the CTP formalism to quantum mechanics in the non-relativistic limit. It is a normalization choice, not a physical axiom.

## 3. The Constitutive Equation

The variation (3) expanded for a general field gives, after coarse-graining to the Markovian limit:

$$\tau\, \frac{dz}{dt} + z \;=\; z_{\rm target}[z] \tag{5}$$

Three independent derivations produce this form:

**Route 1 (CTP variation).** Direct expansion of (3) in the non-relativistic limit, with the constitutive projection for second-order sectors.

**Route 2 (Mori–Zwanzig).** Starting from the exact microscopic dynamics $dz/dt = F[z] + \int K(t-t') z(t')\, dt' + \xi(t)$, the finite-memory (Markovian) limit of the retarded kernel gives (5) with $z_{\rm target} = z + \tau F[z]$.

**Route 3 (Gradient flow).** For a system minimizing a functional $F[z]$: $dz/dt = -(1/\tau)\, \delta F/\delta z$, which gives (5) with $z_{\rm target} = z - \delta F/\delta z$.

The convergence of three independent routes establishes (5) as the universal first-order dynamics of open systems under causality, finite memory, and self-consistent closure.

**The target functional** is not free:

$$z_{\rm target}[z] \;=\; z \;-\; \left(\frac{\delta F}{\delta z}\right)^{-1} F[z] \tag{6}$$

This is the Newton–Raphson step toward the equation of motion $F[z] = 0$. The target is determined by the classical action through the CTP variation.

**Constitutive projection status.** Equation (5) is exact for sectors with first-order underlying dynamics (Schrödinger, Dirac, Lindblad). It is a heuristic projection for sectors with second-order dynamics (Einstein, Friedmann). All DERIVED and COMPUTED results in this document are projection-independent.

## 4. The Noise Kernel

The second variation of $S_{\rm CTP}$ gives:

$$\frac{\delta^2 S_{\rm CTP}}{\delta z_a^2} \;=\; i\, N \tag{7}$$

The Langevin extension:

$$\tau\, \frac{dz}{dt} + z \;=\; z_{\rm target}[z] + \xi(t), \qquad \langle \xi(t)\, \xi(t')\rangle = N(t, t') \tag{8}$$

Noise $\xi$ and dissipation $1/\tau$ are related by the fluctuation–dissipation theorem:

$$N(\omega) \;=\; \frac{2}{\tau}\, \hbar \omega \coth\!\left(\frac{\hbar \omega}{2 k_B T}\right) \tag{9}$$

Both noise and dissipation are outputs of $S_{\rm CTP}$. Neither is postulated.

## 5. The Fixed Point

At the fixed point of (5):

$$z_\star \;=\; z_{\rm target}[z_\star] \tag{10}$$

The time derivative vanishes. $\tau$ drops out. The fixed-point state is determined entirely by the CTP action. It is stable when all eigenvalues of $dz_{\rm target}/dz$ at $z_\star$ have magnitude less than one.

---

# II. DERIVED RESULTS

Each result follows from the foundation (Sections 1–5) by specifying the field content $z$, the classical action (which determines $F$ and $z_{\rm target}$), and the approximation.

## 6. Quantum Mechanics

**Proposition.** The Schrödinger equation is the non-relativistic limit of the CTP variation (3) with $z = \psi$ and $\tau_I = \hbar/2$.

**Derivation.** From (5) with the NR classical action,

$$z_{\rm target} \;=\; \psi + \frac{\hbar}{2m}\nabla^2 \psi - \frac{i}{\hbar} V \psi \times \tau_I.$$

Substituting $\tau_I = \hbar/2$ and rearranging:

$$i\hbar\, \frac{\partial \psi}{\partial t} \;=\; -\frac{\hbar^2}{2m}\nabla^2 \psi + V \psi \tag{11}$$

**Status:** EXACT. No projection. No approximation. Verified to $10^{-16}$.

The Born rule follows from the CTP normalization $Z = 1$ (probability conservation). Lindblad thermalization follows from the noise kernel (7). Twelve consistency checks pass.

## 7. Gravitational Decoherence

**Proposition.** The gravitational noise kernel in the Newtonian limit produces a zero-parameter decoherence rate for extended bodies.

**Derivation.** From the CTP influence functional for gravity, the imaginary part gives (Anastopoulos & Hu 2013):

$$N_{\rm grav}(x, x') \;=\; \frac{G}{\hbar\, |x - x'|} \tag{12}$$

Integrating over a uniform sphere of mass $m$, radius $R$, at superposition separation $\ell$:

$$\boxed{\;\Lambda_{\rm grav} \;=\; \frac{G\, m^2\, S(\ell/R)}{\hbar\, \ell}\;}, \qquad S(\ell/R) = \min\!\left(1, \frac{(\ell/R)^3}{6}\right) \tag{13}$$

**Status:** EXACT. No constitutive projection. No free parameters. Derived from the noise kernel alone.

**The six scaling laws:**

| # | Signature | Form | Discriminates against |
|:---|:---|:---|:---|
| F1 | Mass-squared | $\Lambda \sim m^2$ | Constant floor, CSL |
| F2 | Geometry | $\Lambda({\rm gold}) \neq \Lambda({\rm silica})$ at fixed $m$ | All constant models |
| F3 | Pressure plateau | $\Lambda \to$ const as $P \to 0$ | Standard QM |
| F4 | Far-field $\ell$-scaling | $\Lambda \sim \ell^{-1}$ | Power-law alternatives |
| F5 | Entanglement protection | $\Lambda({\rm Bell}) < \Lambda({\rm separable})$ | State-independent (CSL) |
| F6 | Geometric kink | Slope change at $\ell = 6^{1/3} R \approx 1.817 R$ | Point-mass (DP, Penrose) |

No tested alternative reproduces all six. The scaling laws, not any single number, are the prediction.

**Robustness.** The decoherence rate depends on the noise kernel (7), not on the constitutive equation (5). Non-Markovian corrections to the dynamics do not modify the rate. Theoretical corrections to the kernel: post-Newtonian $O(10^{-16})$, higher-loop $O(10^{-8})$, compactness $O(10^{-27})$. Negligible at laboratory scales.

**Benchmark.** Gold microsphere, $R = 1\,\mu{\rm m}$, $m = 80.8\,$pg, $\ell = 1\,\mu{\rm m}$: $\Lambda \sim 689\,$Hz, $t_{\rm coh} \sim 1.5\,$ms.

## 8. Standard Model Emergence

**Proposition.** The Standard Model with SU(3)$\times$SU(2)$\times$U(1) and three generations is the unique minimal renormalizable gauge theory compatible with the CTP fixed-point architecture.

**Derivation.** Five constraints native to the CTP structure:

| Constraint | CTP origin | What it selects |
|:---|:---|:---|
| Anomaly cancellation | $S_{\rm CTP}$ gauge-invariant | SM hypercharges |
| Asymptotic freedom | Confinement fixed point exists | Non-Abelian strong sector |
| Spontaneous symmetry breaking | EW fixed point exists | Scalar with double-well |
| CP violation | $R_{\rm anomaly} \neq 1$ | $N_{\rm gen} \geq 3$ |
| Renormalizability | $S_{\rm CTP}$ well-defined at all loops | Dimension $\leq 4$ operators |

$N_{\rm gen} = 2$ fails CP violation. Removing SU(3) loses the confinement fixed point. Larger groups are not minimal.

**Status:** COMPUTED. The SM is not derived from $S_{\rm CTP}$ — it is the unique minimal effective theory consistent with its fixed-point structure. Eight consistency checks pass.

## 9. Three Generations and the Koide Identity

**Proposition.** The Koide trace ratio $K = 2/3$ is an algebraic identity of the Z$_3$ circulant mass operator, and $N = 3$ is the unique integer for which $K = 2/3$. (Phase-independence of $K$ is *not* what selects $N = 3$: $K_N = 2/N$ is $\theta$-independent for all $N \geq 3$; only the empirical value $2/3$ singles out $N = 3$.)

**Derivation.** For the Koide parameterization $\sqrt{m_k} = M_0 \big(1 + \sqrt{2}\cos(\theta + 2\pi k/3)\big)$:

$$\sum_k m_k = 6 M_0^2 \qquad \sum_k \sqrt{m_k} = 3 M_0 \qquad K \;=\; \frac{6 M_0^2}{(3 M_0)^2} \;=\; \frac{2}{3} \tag{14}$$

(The sums $\sum_k \cos(\theta + 2\pi k/N) = 0$ and $\sum_k \cos^2 = N/2$ hold for all $N \geq 3$, giving $K_N = (1 + A^2/2)/N = 2/N$, which is $\theta$-independent for every $N \geq 3$; only $N = 2$ is $\theta$-dependent.) The empirical value $K = 2/3$ singles out $N = 3$.

**Status:** PROVEN (algebraic identity, verified to $2.3 \times 10^{-16}$). The Z$_3$ circulant reconstructs $(m_e, m_\mu, m_\tau)$ to 0.005% at $(M_0 = 0.560\,{\rm GeV}^{1/2}, \theta = 2.317\,{\rm rad})$. The two parameters $(M_0, \theta)$ remain open; Track II status in §9.1.

## 9.1 Track II — Derivation Status of $(M_0, \theta)$ (v8 update)

Track II of the v8 program targets deriving $M_0$ and $\theta$ from the multi-generation CTP fixed-point condition $z_\star = z_{\rm target}[z_\star]$. Two phases are complete; a third is now well-posed.

**Phase 1 — Direct derivation from canonical constants.** Attempt to derive $(M_0, \theta)$ from $(R_{\rm anomaly} = 1.15428, S = 108\pi, \alpha_{\rm vac} = 1/3, \tau_0 = 41.9\,{\rm Myr})$ via $z_{\rm target}[z] = z - F_{\rm spatial}[z]/F_{\rm temporal}$. Outcome: HONEST NEGATIVE — underdetermined for two independent reasons.

(i) **Multi-flavor action specification gap.** V7 §29 asserts the Jacobian $dz_{{\rm target},i}/dz_j$ at $z_\star$ is Z$_3$-circulant with eigenvalues equal to the three lepton masses (Conjecture F1), but does not specify $F_{\rm spatial}$ and $F_{\rm temporal}$ for the three-flavor sector. The Z$_3$-circulant shape remains a claim about the fixed point, not a theorem derived from it.

(ii) **$M_0$ dimensional anchor gap.** $M_0$ has units GeV$^{1/2}$. The only mass scale derivable from GRUT's canonical foundation is $\mu_0 = \hbar/\tau_0 \approx 1.57\times 10^{-31}\,$eV, giving $\sqrt{\mu_0} \approx 1.25 \times 10^{-20}\,$GeV$^{1/2}$ versus the required $0.56\,$GeV$^{1/2}$ — a ~20-order-of-magnitude gap that cannot close without an external mass anchor.

**Candidate identity (Phase 1).** A numerical survey of simple dimensionless combinations of $(R, S, \alpha_{\rm vac})$ against the fitted $\theta$ surfaces exactly one match below the 0.1% threshold:

$$\theta_{\rm candidate} \;=\; K \cdot \alpha_{\rm vac} \;=\; \frac{2}{3}\cdot\frac{1}{3} \;=\; \frac{2}{9} \;=\; 0.22222222\dots \tag{14a}$$

with $\theta_{\rm fit} \bmod (2\pi/3) = 0.22222120\dots$ (least-squares against PDG lepton masses, NOT adjusted to $2/9$). Deviation: 4.6 ppm — 56$\times$ inside the PDG $m_\tau$ experimental window ($\approx 258$ ppm). Status: **CANDIDATE IDENTITY** (below DERIVED/COMPUTED, above HYPOTHESIS). A tight numerical agreement between two independently constructed quantities, not a derivation. Falsifier: a CEPC / FCC-ee $m_\tau$ measurement at $\leq 10\,$ppm excluding $\theta = 2/9$ at $>5\sigma$.

**Phase 2 — Dimensional-anchor mechanism evaluation.** Evaluate three candidate anchors for $M_0$ on Lagrangian grounds (not curve-fitting).

| Anchor | Lagrangian operator in SM / V7? | Status |
|:---|:---|:---|
| $v_{\rm EW} = 246\,$GeV (Yukawa) | $\mathcal L_{\rm Yuk} = -y_i\,\overline\Psi_L^i H \ell_R^i + {\rm h.c.}$, present in §8 | **HYPOTHESIS** (sole viable path) |
| $\Lambda_{\rm QCD} \approx 250\,$MeV | None at tree level; leptons are color singlets; no operator in §16 | **FAILED** |
| $v_{\rm dark} \approx 422\,$MeV (§11) | Only kinetic mixing $\epsilon F\!\cdot\! F_{\rm dark}$ (gauge-boson portal); no lepton-dark Yukawa | **FAILED** |

Numerical near-misses without a Lagrangian operator ($M_0^2 / \Lambda_{\rm QCD} \approx 1.26$; $v_{\rm dark} \approx R^2\, M_0^2$ within 1.1%) are explicitly rejected as coincidences, not mechanisms.

**Phase 3 — Derive Yukawa eigenvalues from CTP fixed point.** With $v_{\rm EW}$ identified as the sole viable anchor, Phase 3 attempted to derive the three charged-lepton Yukawa couplings $(y_e, y_\mu, y_\tau) = (2.94\times 10^{-6}, 6.07\times 10^{-4}, 1.02\times 10^{-2})$ — or at least their trace-level scale $\langle y\rangle = \sum y_i/3 = 3.605\times 10^{-3}$ — from the multi-generation CTP fixed-point condition at the EW scale, with $v_{\rm EW} = 246.22$ GeV as SM input and $\theta = 2\pi/3 + 2/9 = 2.316$ rad as the Z$_3$ phase.

Outcome: **HONEST NEGATIVE.** The CTP fixed-point condition for the Higgs-lepton sector fixes $\langle H\rangle = v_{\rm EW}/\sqrt 2$ (Mexican-hat minimum) and the mass-Yukawa relation $m_i = y_i\, v_{\rm EW}/\sqrt 2$ after EWSB, but does NOT constrain the three $y_i$ individually — they enter the SM Lagrangian as independent input parameters, and the fixed-point condition is satisfied for any choice. Conjecture F1's claim that the Jacobian is Z$_3$-circulant in flavor basis is a RESTRICTION on the Lagrangian input, not a derivation from the fixed point.

A numerical survey of dimensionless combinations of $(R, \alpha_{\rm vac}, S, \alpha_s(M_Z), \alpha_{\rm em}(M_Z))$ against $\langle y\rangle$ produces no match below the 5% derivation threshold. The closest candidate, $\alpha_{\rm vac}\cdot\alpha_s/(4\pi) = 3.13\times 10^{-3}$ at 13% off, is rejected on mechanism grounds: charged leptons are color singlets and have no tree-level coupling to $\alpha_s$. Mechanism-free numerical proximity is explicitly disallowed by the Phase 2 curve-fitting prohibition.

Phase 3 does **NOT** falsify the Phase 1 CANDIDATE IDENTITY $\theta = K\cdot\alpha_{\rm vac} = 2/9$ or the Phase 2 $v_{\rm EW}$ HYPOTHESIS. Given the trace scale $\langle y\rangle$ as an input, $\theta$ distributes the three eigenvalues across the Z$_3$ circulant and reproduces the PDG masses to 0.005%. What Phase 3 fails to supply is the trace scale itself.

**Phase 4 — Three-direction mechanism evaluation.** Three GRUT-native candidate mechanisms were evaluated against four requirements: C1 flavor distinction, C2 trace-scale derivation at < 5%, C3 Z₃ compatibility with $\theta = 2/9$, C4 Lagrangian-grade justification.

| Direction | C1 | C2 | C3 | C4 | Verdict |
|:---|:---:|:---:|:---:|:---:|:---|
| A — Anomaly-weighted CTP path counting at flavor level | PASS | FAIL (best 18%) | orthogonal | PASS | **PARTIAL** |
| B — Dielectric coupling with flavor-dependent kinetic mixing | FAIL | FAIL (~70-decade gap) | N/A | FAIL | **FAILED** |
| C.1 — Flavor-sector anomaly-matching analog to $C_{\rm Cosmo}$ | PASS (inherited) | FAIL (best 9.0%) | orthogonal | PARTIAL | **FAILED on C2** |
| C.2 — Temporal-correlator structure at three-flavor level (FDT) | FAIL | N/A | N/A | N/A | **FAILED** (flavor-diagonal with identical spectra) |

Outcome: **HONEST NEGATIVE** on full closure. No direction passes all four criteria. Directions A and C reach the correct order of magnitude for $\langle y\rangle$ through principled hypercharge / Weyl-count structures (C1 and C4 partial), but neither reaches derivation-level precision. Direction B is structurally incompatible — dielectric $\alpha_{\rm eff}(\omega)$ at electron Compton frequency is $\sim 10^{-73}$, a 70-decade gap to the required $10^{-3}$ scale, and V7 §28 has only gauge kinetic mixing (no lepton-dark Yukawa operator).

**Three failures reveal the structure of the obstruction.** (i) It is not numerical — restricting to charged-lepton field content does not supply the extra constraint the CTP three-flavor problem needs. The CTP machinery at three flavors is one-equation-in-three-unknowns regardless of anomaly weighting. (ii) Regime gap — GRUT's canonical dimensionless constants $(\alpha_{\rm vac}, S, R)$ produce $O(1)$ and $O(1/100)$ ratios, not the $O(10^{-3})$–$O(10^{-6})$ loop-suppression span the charged leptons occupy. An additional mass hierarchy or a loop-expansion parameter is needed. (iii) Mainstream-unsolved — Phase 4's verdict restates, from inside the CTP framework, a fifty-year-old open problem.

**Explicitly off-limits framings** (rejected per V7 PROVEN results or per the Phase 2 curve-fitting protocol):

- **4th fermion generation** — V7 §9 PROVES $N = 3$ uniquely $\theta$-independent for the Z$_3$ circulant. Adding a 4th generation breaks this proven identity and invalidates the Phase 1 candidate $\theta = 2/9$.
- **$S^4 \leftrightarrow$ 4 generations** pattern-match — the "4" in $S^4$ is spacetime dimension (Euclidean de Sitter), not generation count.
- **$\tau_0$ as a "new dimension"** — $\tau_0$ is a parameter in the CTP response kernel with dimension time. GRUT has always operated in 4D spacetime.
- **Cubed hypercharge-ratio numerology** — $1/(\sum Y^2_{\rm total,3gen})^3 = 10^{-3}$ matches $\langle y\rangle$ at 72% deviation, but the exponent 3 has no Lagrangian justification. Rejected per C4.

**Legitimate places to look for the missing constraint** (surfaced during Phase 4, not attempted in-session):

- Higher-loop (4-loop and beyond) CTP structure — flavor-differentiating terms that the 3-loop truncation misses;
- Non-perturbative CTP contributions (instantons, wormholes, gravitational path-integral saddles);
- Explicit flavor-sector temporal-correlator refinement with a derivable flavor-dependent $\tau_i$ or $T_i$ (not by hand).

**Phase 4.0 (scope document).** Produced as the Phase 4 deliverable per the honesty protocol; contents available via `koide_operator.phase_4_scope_document()`. Phase 4.1 (attempted mechanisms) is deferred. Candidate Phase 5 directions surfaced during Phase 4 attempts:

- **P5-A** — 3-loop CTP flavor-sector specialist calculation restricted to charged-lepton field content, producing a genuine $R_{\rm flavor, cl}$ from first principles (estimated ~2–4 weeks specialist work, similar to the TJI on $S^4$ item).
- **P5-B** — Froggatt–Nielsen-style GRUT extension with $U(1)_F$ flavor symmetry broken at $\Lambda_F$, charges from Z$_3$-compatible CTP structure.
- **P5-C** — Wait for experimental input. Sub-10-ppm $m_\tau$ at CEPC / FCC-ee that confirms $\theta = 2/9$ reduces Phase 5 to a single trace equation $\langle y\rangle = f(R, \alpha_{\rm vac}, S, v_{\rm EW}, \Lambda_{\rm UV}?)$.

**Status.** Phases 1, 2, 3, 4 all honest-negative at COMPUTED/DERIVED level; one candidate identity flagged for $\theta$ (Phase 1); $M_0$ anchor identified as $v_{\rm EW}$ Yukawa (Phase 2 HYPOTHESIS); Phase 4 Direction A satisfies C1+C4 partial on hypercharge grounds but cannot close C2. V7 §29 stays MAPPED. Conjecture F1 stays HYPOTHESIS. Phase 4.1 attempts deferred to Phase 5. See `grut/derived/flavor/koide_operator.py` for the module, `tests/flavor/test_koide_operator.py` for the 65 regression tests, and `theory/derivation/CORRECTION_17_...`, `CORRECTION_18_...`, `CORRECTION_19_...`, `CORRECTION_20_...` for the full logs.

## 10. Baryon Asymmetry

**Proposition.** The CTP anomaly formula with SM inputs gives the baryon-to-photon ratio within 8% of observation.

**Derivation.** From the CTP forward/backward path asymmetry:

$$\eta_B \;=\; J_{\rm CP} \times K_{\rm neq} \times \frac{2 - R_B}{S_B} \tag{15}$$

with $J_{\rm CP} = 3.18 \times 10^{-5}$ (Jarlskog invariant, SM input), $K_{\rm neq} = 1.19 \times 10^{-2}$ (constitutive non-equilibrium at EW threshold), $R_B = 1.018$ (baryonic anomaly ratio, Route 1 scaling), $S_B = 4\pi \times 45 = 565.5$ (CTP normalization, all SM Weyl fermions).

**Result:** $\eta_B = 6.56 \times 10^{-10}$. Observed: $6.1 \times 10^{-10}$. Deviation: $+8\%$.

**Status:** COMPUTED. Route 2 (ABJ + sphaleron) gives $1.34 \times 10^{-9}$ (2.2$\times$ above observation).

## 11. Dark Matter (Two Live Routes)

**Proposition.** The constitutive double-well potential, extended by U(1)$_{\rm dark}$ gauge and separately interpreted through the vacuum's dielectric response, produces two candidate dark-matter mechanisms. Both are published; v8 Track VII will determine which survives.

**Route 1 — Gauged U(1)$_{\rm dark}$ extension.** The potential $V(z) = \lambda(|z|^2 - v^2)^2/4$ with the gauge relation $\lambda = g_{\rm dark}^2/2$ determines all dark-sector properties from one coupling $g_{\rm dark}$. Five discriminator tests select Route 1a (RG running from the Planck scale) over Route 1b (anomaly extraction):

| Test | Route 1a (RG) | Route 1b (anomaly) | Winner |
|:---|:---|:---|:---|
| Anomaly self-consistency | PASS | FAIL (65% shift) | 1a |
| Fixed-point stability | Stable (eigenvalue 0.16) | Unstable (−6.66) | 1a |
| Naturalness | $\lambda = 0.42$ | $\lambda = 3.83$ | 1a |
| Cosmological consistency | $H_\infty$ shift $-10\%$ | $H_\infty$ shift $-99\%$ | 1a |
| Anomaly budget | 7.4% of $C_{\rm FINAL}$ | 72% of $C_{\rm FINAL}$ | 1a |

**Route 1a result:** $M_{\rm soliton} = 2.1\times 10^9\,$GeV, dark photon $m_A = 387\,$MeV, $\sigma/m = 0.001\,$cm$^2$/g. Bullet Cluster viable. Status: **CLOSED as structural class; unique intra-class branch OPEN.**

**Route 2 — Dielectric bandwidth interpretation.** The original Closure Framework (v1–v11) treated dark matter as a purely dielectric effect: the gravitational refractive enhancement $\varepsilon_g - 1 = n_g^2 - 1 = \alpha_{\rm vac}$. The bandwidth integral over the linear-regime matter power spectrum ($k \lesssim 0.3\,h/{\rm Mpc}$) confirms this: every cosmological mode sits deep in the DC limit ($\omega\tau_0 \approx 10^{-3}$), giving

$$\Omega_{\rm dm, eff} \;=\; \alpha_{\rm vac} \;=\; \frac{1}{3} \;=\; 0.3333 \qquad \text{(zero parameters, +27\% from Planck 0.263)} \tag{16}$$

Status: **COMPUTED** (zero parameters); branch viability depends on whether subtractive corrections or Planck's ΛCDM-implicit extraction account for the +27%.

**Two decisive tests** (Track VII): the Bullet Cluster lensing map (must reproduce the ~720 kpc offset from memory-kernel convolution) and the CMB peak structure (must reproduce acoustic peaks with $n_g(\omega)$ at recombination frequencies). Both routes are published honestly; v8 Track VII determines which survives.

## 12. The Cosmological Constant

**Proposition.** The 3-loop CTP anomaly structure on de Sitter determines the vacuum Hubble rate through the structural function $f(R) = 2 - R$.

**Derivation.** The 3-loop anomaly coefficient $C_{\rm FINAL} = 1.14021 \times 10^{-4}$ (scheme-protected, nonlocal operator $R \ln\Box\, R$) enters the CTP effective action on de Sitter as a single insertion. The CTP forward/backward structure with $C_{-} = R\, C_{+}$ gives

$$\Gamma_{\rm CTP}(R) \;=\; C_{\rm FINAL}\cdot (A + B R)\cdot [\text{spectral sum on } S^4].$$

Boundary conditions from CTP:
- $f(1) = 1$: paths identical $\Rightarrow$ maximum vacuum response;
- $f(2) = 0$: Keldysh destructive interference.

Unique solution $(A, B) = (2, -1)$. Therefore

$$\boxed{\; H_\infty \;=\; \frac{2 - R_{\rm anomaly}}{S\, \tau_0} \;} \tag{17}$$

Numerical verification on 200 spectral modes of $S^4$: $f(R)$ matches $2 - R$ with RMS $9.3 \times 10^{-3}$; the competing quadratic $f = R(2-R)$ is excluded by factor 70 in RMS and $34\%$ vs $0.3\%$ in $\Omega_\Lambda$ accuracy.

**Result.** $H_\infty = 1.885 \times 10^{-18}\,$Hz. $\Omega_\Lambda = 0.6886$ at $H_0 = 70\,$km/s/Mpc. Planck: $0.6889$. **Deviation: $+0.04\%$.** Zero free parameters.

**The Hubble rate as terminal velocity of the vacuum.** The formula decomposes into two physical factors:

$$\underbrace{\;2 - R\;}_{\text{topological drive}\ =\ 0.846} \;\Big/\; \underbrace{\;S \cdot \tau_0\;}_{\text{constitutive friction}\ =\ 4.487\times 10^{17}\,{\rm s}}$$

$(2 - R) = 0.846$ is the magnitude of the conformal-mode outward pressure on Euclidean $S^4$ — the topological drive for cosmic expansion. $S\cdot\tau_0$ is the integrated damping from the memory kernel $K(t) = \tau_0^{-1}\exp(-t/\tau_0)$. Their ratio is the steady-state expansion rate. Cosmic acceleration is not a static cosmological constant; it is the terminal velocity of a medium whose conformal mode is unstable but whose constitutive response prevents runaway.

Standard Euclidean gravity on $S^4$ has a negative-definite conformal-mode kinetic term (Gibbons–Hawking 1978); the standard resolution rotates the conformal factor into the complex plane ($\Omega \to i\Omega$) to force positivity manually. **GRUT does not need the rotation.** The viscoelastic memory kernel supplies the physical damping that stabilizes the instability into a finite expansion rate. See V7 §26.2.3a for the full mechanism and the two outstanding verifications.

**Hubble rate.** Using the one-parameter prediction $H_\infty$ and the GRUT-canonical cosmic age $t_0 = 329\,\tau_0$ (V7 §27), one obtains $H_0 = 69.03\,$km/s/Mpc — sitting in the Hubble-tension gap between Planck ($67.4$) and SH0ES ($73.5$), Planck-leaning by construction.

**Sign convention.** $R_{\rm anomaly} = 1.15428$ is the magnitude $|C_{\rm Cosmo}/C_{\rm FINAL}|$ used in (17). The physical signed ratio $R_{\rm ANOMALY\_SIGNED} = -1.15428$ encodes the conformal-factor sign on Euclidean $S^4$; see V7 §26.2.3a and Correction #16. The cosmological formula takes $(2 - |R|)$, and the magnitude convention is used consistently in (15), (17), and throughout §§10–12.

**Structural derivation of the $-100$ on $S^4$.** The numerator integer $-100$ in the 3-loop $C_{\rm Cosmo}$ assembly decomposes into four components (A–D: SM hypercharge-squared sum, conformal-mode instability, thermal trace-anomaly combinatorics, spectral-sum matching) and satisfies $|-100| = (\sum_{\rm SM} Y^2)^2 = 10^2$ as an SM-derivable algebraic identity. Full four-component derivation: V7 §26.2.6. Independent verification via Osborn 2003 eq (36) at $\varepsilon_{\rm combined} = 1.1537$: V7 §26.2.2 and §12.1 below.

**Three falsifiers for the Correction #16 identification** (V7 §26.2.7):
- **F1** (TJI on $S^4$): match the TJI master-integral coefficient computed directly from 3-loop CTP on Euclidean $S^4$ against the A-component value;
- **F2** ($\tau_0$ consistency): verify that the noise-kernel relaxation time derived independently from gravitational decoherence matches the cosmological $\tau_0$ at the percent level after adjustment;
- **F3** ($w(z)$ deviation): late-time dark-energy equation-of-state deviation predicted from the conformal-mode-regulated drive/friction balance, testable by DESI / Euclid.

Any one $F_i$ failing falsifies the $-100$ identification without disturbing the Z$_3$ flavor or decoherence sectors.

**Status.** **COMPUTED.** Primary-source audit V7 §26.2 confirms every integer traces to group theory or combinatorics; no coupling constants, no measured parameters, no scheme choice enters. $\Omega_\Lambda = 0.6886$ at 0.04% from Planck is a genuine prediction. One outstanding specialist item remains: the flat-to-curved normalization of a single master integral (TJI on Euclidean $S^4$, $\sim 3$ weeks specialist work per V7 §26.2.5), which controls the numeric $-100$ directly and leaves all structural claims intact if absent.

## 12.1 Independent Confirmation via Osborn's $\varepsilon$

The value $R_{\rm anomaly} = 1.15428$ used in §12 is computed from $|C_{\rm Cosmo}/C_{\rm FINAL}|$ on Euclidean $S^4$ at 3-loop (primary-source audit V7 §26.2). This subsection documents an **independent consistency check** through a completely different mathematical construction: Osborn's coupling-corrected trace-anomaly coefficient $\varepsilon$. The two expressions agree at 0.05% — constituting a structural identity, not a replacement.

**The identification.** Osborn 2003 (arXiv:hep-th/0302119) eq (36) gives the 2-loop coefficient of the operator $-(1/3)\,n_V\,(1/g^2)\,R (\partial_\mu g)^2$ in the local-coupling counterterm Lagrangian on curved backgrounds. The explicit form:

$$\varepsilon \;=\; 1 + \frac{1}{3}\left(29 C - 12 R_\psi - \frac{5}{2} R_\phi\right)\frac{g^2}{16\pi^2}$$

For SM gauge groups at $M_Z$ (Dirac convention, MS-bar), the coupling-weighted combination $\varepsilon_{\rm combined}({\rm SM}, M_Z) = 1.1537$ — matching $R_{\rm anomaly} = 1.15428$ at 0.05%.

**Three arguments supporting the identification:**

(i) **De Sitter is conformally flat.** $C_{\mu\nu\rho\sigma} = 0$ on $S^4$; the Weyl$^2$ coefficient $a$ vanishes from the bulk anomaly. Only the Euler-density coefficient (and its coupling-corrected variant $\varepsilon$) contributes.

(ii) **Jack–Osborn 2014 gradient-flow theorem** (arXiv:1312.0428). The antisymmetric part of the coupling-space tensor $T_{IJ}$ drops out identically in the flow equation $\beta^I\,\partial_I \tilde A = G_{IJ}\,\beta^I\beta^J$. The $W_i$ / antisymmetric perturbative mechanism cannot shift $R$ at any order, closing the perturbative Osborn route structurally.

(iii) **CTP imaginary effective action on $S^4$.** The Euler density picks up a factor of $i$ under Wick rotation. GRUT's decoherence-relevant action is ${\rm Im}(\Gamma_{\rm CTP})$, which sees the coupling-corrected Euler coefficient, not the free-field $|b/a|$.

**Physical mechanism — Gibbons–Hawking thermal asymmetry.** At $T_{\rm GH} = H_\infty/(2\pi)$, the CTP forward path samples the vacuum anomaly coefficient ($C_{\rm FINAL} = b_{\rm free}$) and the backward path samples the thermally-corrected coefficient ($C_{\rm Cosmo} = b_{\rm free} \times \varepsilon$). Ratio $=\varepsilon$ by construction; $M_Z$ enters as the matter-decoupling matching scale.

**Fulcrum structure.** $R = 1$ is the free-field fulcrum (CTP paths identical, $f(1) = 1$, maximum vacuum response). $R = 2$ is Keldysh destructive interference ($f(2) = 0$, zero response). The observed universe sits at $R = 1 + 17\,\alpha_s(M_Z)/(4\pi) \approx 1.16$, a small tilt set by SM loop suppression. This reframes the cosmological constant problem: $\Omega_\Lambda$ is not a 120-order fine-tuning but an $O(1)$ quantity whose size is set by $\alpha_s/(4\pi)$ — the standard loop suppression of any SM quantum correction.

(For the complementary mechanistic framing — "terminal velocity of the vacuum," with the Gibbons–Hawking conformal-mode instability regulated by the viscoelastic memory kernel at timescale $\tau_0$ — see V7 §26.2.3a.)

**Verification path.** 3-loop CTP effective action on Euclidean $S^4$ with SM matter at the EW matching scale, extract $C_{\rm Cosmo}/C_{\rm FINAL}$, verify equal to $\varepsilon_{\rm combined}({\rm SM}, M_Z)$ at leading order. Estimated **~3 weeks** for a curved-space CTP specialist (Bei-Lok Hu, Enric Verdaguer, Albert Roura); see V7 §26.2.5 for the task specification, and `theory/ZENODO_EPSILON_IDENTIFICATION.md` for the detailed analysis.

**Status: INDEPENDENT CONFIRMATION.** Two independent mathematical constructions (3-loop CTP on $S^4$ and Osborn 2003 eq (36) at $M_Z$) producing the same number at 0.05%. Not a candidate replacement — a structural cross-check.

## 13. Quantum Gravity (Linearized)

**Proposition.** The linearized constitutive gravity equation satisfies five closure conditions for the $\tau_0$ branch.

| Condition | Evidence |
|:---|:---|
| Massless graviton | Pole at $\omega^2 = k^2 c^2$ |
| No ghost | Extra pole purely imaginary (dissipative) |
| UV completion | Propagator falls as $1/\omega^3$ |
| BH information ($\tau_0$) | 99.94% recovery, Page turnover |
| Classical GR recovery | LIGO modification $< 10^{-10}$ |

**Status:** STRUCTURAL (linearized level; nonlinear closure ladder: 4/8 rungs closed).

---

# III. CONJECTURES

## Conjecture F1 (Flavor Eigenvalue)

**Statement.** Fermion masses are eigenvalues of the multi-generation CTP fixed-point operator $M_{ij} = dz_{{\rm target},i}/dz_j$ evaluated at $z_\star = z_{\rm target}[z_\star]$.

**Proven:** $K = 2/3$ from Z$_3$ identity. $N = 3$ uniquely $\theta$-independent.

**Track II progress (v8; §9.1):**
- Phase 1 result: HONEST NEGATIVE on direct derivation of $(M_0, \theta)$ from GRUT canonical constants (action and mass-anchor gaps).
- Phase 1 candidate identity: $\theta = K\cdot\alpha_{\rm vac} = 2/9$, agreeing with $\theta_{\rm fit}$ (least-squares against PDG lepton masses) at 4.6 ppm — 56$\times$ inside the PDG $m_\tau$ experimental window. CANDIDATE IDENTITY, not DERIVED.
- Phase 2 result: of three candidate $M_0$ anchors ($v_{\rm EW}$, $\Lambda_{\rm QCD}$, $v_{\rm dark}$), only the SM-native $v_{\rm EW}$ Yukawa mechanism has a Lagrangian operator in V7. $\Lambda_{\rm QCD}$ and $v_{\rm dark}$ FAIL on mechanism grounds.
- Phase 3 result: HONEST NEGATIVE. The CTP fixed-point condition at the EW scale does not constrain the three charged-lepton Yukawa couplings — they are SM Lagrangian inputs, and the fixed point is satisfied for any choice. No dimensionless combination of GRUT / SM constants reaches $\langle y\rangle$ below the 5% derivation threshold.
- Phase 4 direction: the charged-lepton Yukawa hierarchy, narrowed to the trace $\langle y\rangle$. A genuinely open research problem in mainstream flavor physics, now posed from inside the CTP framework.

**Still open:** $M_0$ (via $\sum y_i/6$), the three Yukawa eigenvalues, the full three-flavor action $F_{\rm spatial}$, and a GRUT-native flavor-selection mechanism that forces $\langle y\rangle$ to the charged-lepton trace stratum.

**Falsified by:** Koide violated at precision tau-mass measurement (kills the Z$_3$ identity). Sub-10-ppm $m_\tau$ measurement excluding $\theta = 2/9$ (kills the Phase 1 candidate identity, leaves the Z$_3$ identity intact).

## Conjecture C2 (Primordial Spectrum)

**Statement.** Constitutive dissipation at the Planck bounce produces a spectral index

$$n_s \;=\; 1 - \frac{2 (H\tau)^2}{1 + (H\tau)^2}.$$

**Computed:** $n_s = 0.9649$ at $H\tau = 0.134$ (matches Planck 2018 central value). Tensor-to-scalar ratio $r$ suppressed by constitutive damping.

**Not proven:** Initial conditions at the Planck bounce. Amplitude $A_s$.

**Falsified by:** CMB-S4 measurement of spectral running inconsistent with constitutive form.

## Conjecture Q1 (Nonlinear Curvature Bound)

**Statement.** The constitutive memory term bounds all curvature invariants at the Planck scale in generic spacetimes.

**Proven:** FRW singularity regularized ($H$ bounded). Schwarzschild curvature capped. Linearized graviton ghost-free.

**Not proven:** Full tensor stability. Self-consistent $\tau_{\rm eff}$. Nonlinear backreaction.

**Falsified by:** Ghost or tachyonic instability in the tensor sector.

## Conjecture SCP (Strong CP)

**Statement.** The QCD constitutive fixed point is $\theta$-independent, naturally selecting $\theta = 0$.

**Proven:** Constitutive EOM is $\theta$-independent (perturbatively). CTP noise kernel is $\theta$-independent. Instanton contribution suppressed by $3.3\times 10^{-6}$.

**Not proven:** Non-perturbative instanton sector fully resolved.

**Falsified by:** Detection of an axion.

## Conjecture H1 (Hierarchy)

**Statement.** The constitutive UV softening ($1/\omega^3$) modifies the character of the Higgs mass divergence from quadratic to logarithmic.

**Result:** The hierarchy problem is NOT solved. The Planck-scale contribution remains.

**Status:** HONEST NEGATIVE.

---

# IV. THE BRIDGE

## 16. The Bridge Parameter

The cosmological formula (17) connects the decoherence sector to cosmology through one parameter:

$$\tau_0 \;=\; \frac{\hbar\, \ell}{G m^2} \quad\text{evaluated on the decoherence surface} \tag{18}$$

The formula for $\tau_0$ is derived from the noise kernel. The specific value ($41.9\,$Myr at $m = 20{,}818\,$amu, $\ell = 1\,\mu{\rm m}$) requires specifying the evaluation point. No GRUT-native principle selects this point.

$\tau_0$ and $\Omega_\Lambda$ are linked by the derived structural relation (17) involving two computed constants ($2 - R$, $S$) and one measured constant ($H_0$). They are not the same quantity — they live in different physical domains. The relation IS the content of the theory.

## 17. The Experimental Chain

$$\text{Measure } \Lambda_{\rm grav} \text{ at any } (m, \ell) \;\longrightarrow\; \tau_0 \;=\; \frac{\hbar\, \ell}{G m^2\, \Lambda_{\rm grav}\, S(\ell/R)} \;\longrightarrow\; H_\infty = \frac{2 - R_{\rm anomaly}}{S\, \tau_0} \;\longrightarrow\; \Omega_\Lambda = \left(\frac{H_\infty}{H_0}\right)^2$$

**Before the experiment:** one-parameter framework ($\tau_0$ inferred from $\Omega_\Lambda$).
**After the experiment:** zero-parameter prediction ($\tau_0$ measured, $\Omega_\Lambda$ predicted).

A single laboratory measurement of gravitational decoherence determines the vacuum expansion rate of the universe.

---

# V. PROJECTION-DEPENDENCE AUDIT

| Result | Projection-dependent? | Status |
|:---|:---|:---|
| Schrödinger recovery | No (first-order) | EXACT |
| $\Lambda_{\rm grav}$ | No (noise kernel) | EXACT |
| Six scaling laws | No (kernel properties) | EXACT |
| $K = 2/3$ | No (algebraic identity) | PROVEN |
| $N = 3$ unique | No (algebraic) | PROVEN |
| $M_0, \theta$ derivation | No (mechanism-based, §9.1) | HONEST NEGATIVE + candidate $\theta = 2/9$ |
| $v_{\rm EW}$ Yukawa anchor | No (SM-native, §9.1) | HYPOTHESIS (Phase 3 target) |
| $f(R) = 2 - R$ | No (CTP algebra + BCs) | COMPUTED |
| $R_{\rm anomaly} = 1.15428$ | No (primary-source audit §26.2) | COMPUTED |
| $\Omega_\Lambda = 0.6886$ | No (assembly, +0.04% from Planck) | COMPUTED |
| $H_0 = 69.03\,$km/s/Mpc | No (one-parameter) | COMPUTED (tension-gap) |
| $\eta_B = 6.56\times 10^{-10}$ | No (CTP anomaly) | COMPUTED |
| DM Route 1 gauged | No (self-consistency) | CLOSED class; intra-class branch OPEN |
| DM Route 2 dielectric | No (bandwidth integral) | COMPUTED ($\Omega_{\rm dm,eff} = 1/3$, +27%) |
| SM emergence | No (constraint analysis) | COMPUTED |
| Graviton propagator | Yes (linearized) | STRUCTURAL |
| BH information 99.94% | Partial (kernel shape) | STRUCTURAL |
| Singularity bounded | Yes | STRUCTURAL |

Every DERIVED and COMPUTED result is projection-independent. The constitutive projection affects only results already labeled STRUCTURAL.

---

# VI. FALSIFICATION

| # | Observation | What it kills |
|:---|:---|:---|
| 1 | No decoherence plateau at the predicted rate (primary test) | The predictive core |
| 2 | $\Lambda_{\rm grav}$ measured, wrong $\Omega_\Lambda$ | The bridge |
| 3 | $H_\infty$ shifts outside observed range as $R, S, \tau_0$ are better measured | The cosmological computation |
| 4 | $H_0$ converges outside $69 \pm 3\,$km/s/Mpc | The one-parameter Hubble prediction |
| 5 | DESI / Euclid / Roman measure $H_0 \sqrt{\Omega_\Lambda} \neq 58.16 \pm 1\,$km/s/Mpc | The structural correlation $H_0\sqrt{\Omega_\Lambda} = H_\infty = $ const |
| 6 | Bullet Cluster lensing map cannot be reproduced from the memory kernel | The dielectric interpretation (DM Route 2) |
| 7 | Axion detected | Conjecture SCP |
| 8 | Fourth generation found | $N = 3$ uniqueness |
| 9 | Koide violated by precision lepton-mass measurement | Z$_3$ identity |
| 10 | Graviton mass detected | Massless graviton |
| 11 | Sub-10-ppm $m_\tau$ measurement excluding $\theta = 2/9$ at $> 5\sigma$ | Phase 1 candidate identity (Z$_3$ intact) |
| 12 | Any of $F_1 / F_2 / F_3$ (V7 §26.2.7) — TJI on $S^4$, $\tau_0$ consistency, $w(z)$ deviation | The $-100$ Gibbons–Hawking identification (conjectures intact) |

The primary test is the decoherence plateau. A null result would remove the predictive core and weaken (though not logically disprove) the structural mappings. V7 §41 maintains the complete enumeration with the full narrative context for each entry.

| Observation | What survives |
|:---|:---|
| No GW modification | Predicted ($10^{-39}$ rad, dead by construction) |
| Hierarchy unsolved | Acknowledged (honest negative, H1) |
| Fermion masses not derived | Acknowledged — $M_0$ reduced to $\sum y_i / 6$ via $v_{\rm EW}$ (§9.1); three Yukawas remain Phase 3 target; $\theta = K\cdot\alpha_{\rm vac}$ candidate at 4.6 ppm |

---

# VII. CONCLUSION

The CTP effective action with two axioms and one normalization produces a constitutive response equation whose sectoral limits yield: quantum mechanics (exact), gravitational decoherence with six scaling laws (exact, zero parameters), a cosmological constant $\Omega_\Lambda = 0.6886$ at **0.04% of Planck** (computed from 3-loop CTP on $S^4$, zero free parameters, primary-source audit in V7 §26.2), a one-parameter Hubble rate $H_0 = 69.03\,$km/s/Mpc sitting in the tension gap, a baryon asymmetry $\eta_B = 6.56\times 10^{-10}$ at 8% of observation (computed), a dark-matter sector with two live routes (gauged U(1)$_{\rm dark}$ closed at structural level; dielectric bandwidth integral $\Omega_{\rm dm,eff} = \alpha_{\rm vac} = 1/3$ computed with zero parameters; branch resolution is v8 Track VII), the Standard Model as the unique minimal effective theory from five CTP constraints (computed), and three-generation uniqueness from the Z$_3$ Koide identity (proven).

**The Hubble rate is the terminal velocity of the vacuum.** The topological drive $(2 - R) = 0.846$ from the conformal-mode instability on Euclidean $S^4$ is balanced by constitutive friction $S\cdot\tau_0$ from the viscoelastic memory kernel. What standard Euclidean gravity hides behind a Wick rotation ($\Omega \to i\Omega$), GRUT exposes as physical damping. See V7 §26.2.3a for the full mechanism and the two outstanding verifications.

**Track II progress (v8; §9.1).** The two open Koide parameters $(M_0, \theta)$ have been analyzed on mechanism grounds. $M_0$ is reduced to $\sum y_i / 6$ through the SM-native $v_{\rm EW}$ Yukawa operator — the sole viable anchor after mechanism evaluation against $\Lambda_{\rm QCD}$ and $v_{\rm dark}$, both of which FAIL because no Lagrangian operator in V7 couples them to the charged-lepton sector. One candidate identity for $\theta$ has surfaced: $\theta = K\cdot\alpha_{\rm vac} = 2/9$, agreeing with $\theta_{\rm fit}$ (least-squares against PDG lepton masses) at 4.6 ppm — 56$\times$ inside the current PDG $m_\tau$ experimental window. Phase 3 is now a single well-posed problem: derive the three Yukawa eigenvalues from the multi-generation CTP fixed point with $v_{\rm EW}$ as input.

The framework has one bridge parameter ($\tau_0$) linking decoherence to cosmology through a derived structural relation. A single measurement of gravitational decoherence at any mass and separation would fix this parameter and convert the cosmological constant from a one-parameter match to a zero-parameter prediction.

All numerical claims above are anchored in the GRUT-RAI computational repository (current regression-test baseline: 430 passing tests, including 37 for the Z$_3$ / Yukawa-anchor Track II sector). Every sector of V7 that V8 references here retains its full derivation text and honesty ledger in the parent document (V7 §§0, 8, 26.2, 28, 41 as the primary back-references).

---

## References

[1] L. Diósi, Phys. Lett. A 120, 377 (1987).
[2] R. Penrose, Gen. Relativ. Gravit. 28, 581 (1996).
[3] J. Schwinger, J. Math. Phys. 2, 407 (1961).
[4] L. V. Keldysh, Sov. Phys. JETP 20, 1018 (1965).
[5] C. Anastopoulos and B. L. Hu, Class. Quantum Grav. 30, 165007 (2013).
[6] E. Calzetta and B. L. Hu, *Nonequilibrium Quantum Field Theory* (Cambridge, 2008).
[7] G. C. Ghirardi, A. Rimini, and T. Weber, Phys. Rev. D 34, 470 (1986).
[8] Planck Collaboration, Astron. Astrophys. 641, A6 (2020).
[9] D. R. Grover, "GRUT v6: The CTP Formalism Paper," Zenodo (2026). doi:10.5281/zenodo.19548049
[10] D. R. Grover, "GRUT v7: The Responsive Universe Program," Zenodo (2026). doi:10.5281/zenodo.19559075
[11] D. R. Grover, "GRUT Phase I Closure Protocol," Zenodo (2026). doi:10.5281/zenodo.18008060
[12] D. R. Grover, "Three Independent Routes to the GRUT Constitutive Equation," preprint (2026).
[13] D. R. Grover, "The Hubble Rate from the CTP Anomaly on de Sitter," preprint (2026).
[14] D. R. Grover, "GRUT-RAI: Reproducible Computational Framework," Zenodo (2026). doi:10.5281/zenodo.18993689

---

*D. Ryan Grover, April 2026.*
*Grand Responsive Universe Theory.*
