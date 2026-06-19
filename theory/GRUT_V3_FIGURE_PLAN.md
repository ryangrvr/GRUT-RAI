# GRUT ToE v3 — Figure Plan (for the next pass)

Proposed figures/diagrams/graphs to add to `uploads/GRUT_TOE_V3_upload.md`. 27 total, by chapter. Noted during the technical-brief pass; NOT yet rendered.

## Foreword + The Question

1. **The Three Pillars and Their Standing: Epistemic Hierarchy Diagram** — *schematic diagram*  
   - Shows: A triangle or hierarchical pyramid showing Q (proven, base) at the strongest level, F (postulated/anchored) at intermediate level, and D (partial bridge) at the weakest level, with arrows showing how F breaks D observed through Q. Boxes label each pillar with its status and role. Placement: immediately after 'The Three Pillars and Their Standing' section heading, before the detailed prose expansion.  
   - Placement: after 'The Three Pillars and Their Standing' section heading
2. **Memory Breaking the Adiabatic Rescaling: Phase-Space Illustration** — *schematic diagram*  
   - Shows: A coordinate rescaling transformation (a → ae^λ) applied to spacetime, with two side panels: left panel shows memoryless GR where the rescaling is unobservable (redundant), right panel shows GRUT where the absolute scale L₀ makes the rescaling observable through the (L₀k_phys)² term. Arrows indicate the breaking. Placement: after 'How Memory Breaks the Redundancy' subsection, before the pool analogy.  
   - Placement: before the swimming-pool analogy in 'How Memory Breaks the Redundancy'
3. **Response Regime Map: Frequency Dependence of the Single-Pole Susceptibility** — *plot*  
   - Shows: A log-log plot of |χ(ω)| vs. ωτ₀, showing the characteristic behavior of the Lorentzian response χ(ω) = 1/(1 − iωτ₀): flat (≈1) at low frequency (ωτ₀ ≪ 1), and falling as 1/(ωτ₀) at high frequency (ωτ₀ ≫ 1). Horizontal line marks ωτ₀ = 1 transition. Annotations identify 'memory regime' (left) and 'no-memory regime' (right). Include the solar system and cosmological structure-formation regimes on the frequency axis. Placement: in the Technical Brief, after the susceptibility formula, to visualize the GR recovery.  
   - Placement: Technical Brief, after susceptibility definition

## The Three Pillars

1. **CTP Contour and Response Structure** — *schematic diagram*  
   - Shows: The closed-time-path contour with forward (+) and backward (−) branches, illustrating how $S_{IF}$ vanishes on the diagonal $h_+ = h_-$ and how the response $\delta S_{IF}/\delta h_q|_{q=0}$ emerges from deviations. Clarifies the geometric meaning of 'response to realized differences.'  
   - Placement: After the statement of Pillar Q, before discussion of causality
2. **Single-Pole Susceptibility and Regime Boundaries** — *plot*  
   - Shows: A log-log plot of $|\chi(\omega)|$ vs $\omega\tau_0$ showing the transition from low-frequency in-phase response ($\chi \approx 1$) to high-frequency suppression ($\chi \propto 1/\omega\tau_0$). Overlaid on the frequency axis: regimes for solar-system timescales, galaxy-cluster dynamics, and CMB scales. Emphasizes when GRUT differs from GR.  
   - Placement: In the discussion of Pillar F, after introduction of the Mori–Zwanzig equation
3. **Breaking of the Adiabatic Dilation Redundancy** — *flow diagram*  
   - Shows: A two-panel illustration: (left) the exact redundancy at $L_0 \to 0$ where dilation $a \to ae^\lambda$ leaves physics unchanged; (right) the controlled breaking for $L_0 > 0$ where the memory scale $(L_0 k_{\text{phys}})^2$ is not invariant under the dilation. Includes the scaling transformation $k_{\text{phys}} \to e^{-\lambda} k_{\text{phys}}$ to make the mathematical breaking transparent.  
   - Placement: In the discussion of Pillar D, illustrating the core theorem of controlled symmetry breaking

## The One Idea

1. **Dilatation transformation and physical wavenumber response** — *schematic diagram*  
   - Shows: A two-panel diagram showing (left) the adiabatic rescaling a → a·e^λ with comoving k fixed, and (right) how physical k_phys = k/a transforms as e^{-λ}·k_phys. Illustrates why an absolute scale L₀ breaks the coordinate redundancy D. Strengthens the intuition in 'Why the breaking is controlled' by making the transformation concrete.  
   - Placement: After the 'Memory breaks the redundancy' section, before the quantitative derivation
2. **Susceptibility χ(ω) and memory-argument scaling** — *plot*  
   - Shows: A log-log plot of the magnitude |χ(ω)| versus ωτ₀ for the single-pole susceptibility χ(ω) = 1/(1 − iωτ₀), showing the transition from low-frequency (ωτ₀ ≪ 1) where χ ≈ 1, to high-frequency (ωτ₀ ≫ 1) where χ → 0. Overlay the static susceptibility χ_eq(k_phys) = 1/[1 + (L₀k_phys)²] in a secondary inset, showing how the memory scale L₀ sets a natural wavenumber cutoff. Illustrates why the framework is 'causal, bounded, GR-recovering' and justifies the postulate of finite memory.  
   - Placement: At the start of the Technical Brief, when introducing the susceptibility for the first time
3. **Non-invariance of (L₀k_phys)² under adiabatic rescaling** — *flow diagram*  
   - Shows: A three-step flow: (1) Start state: physical wavenumber k_phys = k/a and memory argument (L₀k_phys)². (2) Apply rescaling: a → a·e^λ, so k_phys → e^{-λ}·k_phys. (3) Result: (L₀k_phys)² → e^{-2λ}(L₀k_phys)² — not invariant. Boxes indicate 'Diffeomorphism (unit Jacobian)' and 'No anomaly', emphasizing why the breaking is classical not quantum. Concretizes the central mathematics of why D breaks.  
   - Placement: In the Technical Brief section 'How finite memory breaks the dilatation redundancy', adjacent to the calculation

## The Responsive Vacuum

1. **The Keldysh contour and the influence action S_IF(h_a)** — *schematic diagram*  
   - Shows: A time-contour diagram showing the forward (+) and backward (−) branches of the CTP, with the separation h_a marked between them. Visual representation of how S_IF[h_a = 0] = 0 on the diagonal, and how the physical response emerges from deviations in h_a. This clarifies the topological origin of the CTP principle.  
   - Placement: After the opening paragraphs on the CTP formalism, before 'The Constitutive Law'
2. **Susceptibility χ(ω) and the regime structure of GRUT** — *plot*  
   - Shows: A plot of |χ(ω)| = 1/√(1 + ω²τ₀²) vs. log₁₀(ωτ₀), with labeled regions: low-ω (memory-full, χ ≈ 1), cross-over near ωτ₀ = 1, high-ω (memory-free, χ → 0). Overlaid: the frequency scales of solar system (ωτ₀ ≈ 10⁷), galactic (ωτ₀ ≈ 1), and cosmological (ωτ₀ ≈ 10⁻³). Clarifies why different physical scales experience different 'versions' of gravity.  
   - Placement: After 'The Constitutive Law' subsection, accompanying the frequency-dependent discussion
3. **The CTP action S_CTP decomposition and Φ_μν emergence** — *flow diagram*  
   - Shows: A box diagram showing the four terms of S_CTP (EH, matter, constitutive, noise) and arrows indicating which term contributes to the classical equation G_μν^(1) − Φ_μν = 8πG T_μν. Shows visually how Φ_μν is extracted from the constitutive term S_const via the h_a variation. Helps readers see the 'derivation' of the response as a structural necessity, not a postulate.  
   - Placement: In the Technical Brief, immediately before or after the 'Derivation of Φ_μν' section

## The Universe That Falls Out

1. **Separate-Universe Invariance vs. Conformal Response** — *flow diagram*  
   - Shows: Visual depiction of the no-go collision at k→0: on the left, the separate-universe mode (adiabatic rescaling) with zero response demanded; on the right, the conformal refractive response demanding maximal response (μ → 1+α). The diagram illustrates why both cannot be satisfied simultaneously, making the physical constraint visible.  
   - Placement: After the statement of the no-go theorem (§ 'Conformal Mode and Separate-Universe Invariance No-Go'), before the projector-structure explanation.
2. **Terminal Velocity Balance: Instability vs. Memory Drag** — *schematic diagram*  
   - Shows: A two-force balance diagram showing the Gibbons–Hawking geometric instability (driving runaway expansion, arrow pointing upward) opposed by the memory-kernel dissipative drag (arrow pointing downward). The equilibrium point at H_inf is marked, showing how the cosmological constant emerges as the terminal expansion rate rather than as a bare constant.  
   - Placement: In the Technical Brief, after introducing the terminal-velocity formula, to illustrate the physical mechanism behind H_inf.
3. **Ω_Λ as a Function of τ₀: The Terminal-Velocity Scaling** — *plot*  
   - Shows: A graph of Ω_Λ (y-axis) versus τ₀ in millions of years (x-axis), showing the monotonic dependence Ω_Λ ∝ H_inf², with the observed value from Planck 2018 marked as a horizontal band, and the GRUT-anchored τ₀ ≈ 41.9 Myr marked as a vertical band. The intersection shows why τ₀ is uniquely constrained by Ω_Λ and why measuring τ₀ from laboratory decoherence experiments pins the dark-energy fraction.  
   - Placement: In the Technical Brief, after the numerical evaluation of H_inf and Ω_Λ, to show the quantitative connection between the two.

## The Dark-Matter Detective Story

1. **The K⁽²⁾ Four-Stage Investigation Diagram** — *flow diagram*  
   - Shows: A flowchart showing the progression through stages A (operator uniqueness: W² is sole dynamic channel), B (scale determination: forced to L₀), C (magnitude test: O(1-100) viable), and D (shape test: 1/r⁴ too steep). Each stage includes the key verdict and the tier. Shows the logical pathway from initial assumption (dark sector exists) to final conclusion (no derived DM mechanism).  
   - Placement: After 'The final mechanism' subsection heading, before 'Stage 1: Operator uniqueness'
2. **Radial Profile Comparison: W² Weyl Response vs. Observable Dark Halos** — *plot*  
   - Shows: A log-log plot showing radial density profiles. Three curves: observed isothermal dark-matter halo (ρ ∝ 1/r², slope = −2), the W² Weyl-squared response (slope −4 interior, −6 exterior, labeled as 'too steep'), and rotation velocity v(r) for each (flat for observed, declining for W²). Shaded region marks the region of observational constraint (r = 0.1–100 kpc). Illustrates why ρ_eff ∝ W² cannot sustain flat rotation curves.  
   - Placement: In 'Stage 4' subsection, after the explanation of 1/r⁴ scaling
3. **The Locality Theorem: Why 1/∇² Cannot Survive in a Local Kernel** — *schematic diagram*  
   - Shows: A three-panel schematic. Left: the spatially-local, k-independent kernel K⁽²⁾(ω,k)—shown as a box with temporal memory χ(ω) and dimensionless P^TT projector, no k-dependence. Middle: the source W² ~ (∂²h)², yielding k⁴ in Fourier space (polynomial). Right: their product—still polynomial, never 1/k² (a pole). A red X through a proposed 1/k² term illustrates that no differentiation or integration can turn polynomial k⁴ into pole 1/k². Caption: 'Locality forbids the inverse Laplacian that would be needed to shallow the 1/r⁴ profile to 1/r².'  
   - Placement: In the 'The verdict and its implications' section, after 'The deeper constraint is that...' paragraph

## How To Kill It

1. **Decoherence Rate vs. Mass and Size** — *plot*  
   - Shows: Two-panel figure showing: (left) Λ_grav as a function of object mass m for fixed separation R (emphasizing the m⁴ scaling that makes the 1-μm gold sphere special), with marked benchmark at m ≈ 80.8 pg giving 689 Hz; (right) contours of constant Λ_grav in the (m, R) plane, overlaid with experimental reach windows for matter-wave interferometry and entanglement-separation tests. This illustrates the parameter space GRUT constrains and which regimes are laboratory-accessible.  
   - Placement: After the section 'The Gravitational Decoherence Plateau at ~689 Hz', to ground the prediction in observable space.
2. **Z₃ Neutrino Mass Spectrum: Normal vs. Inverted** — *schematic diagram*  
   - Shows: A diagram showing the mass-matrix eigenvalue structure in the (M₀, θ) plane. Display both the normal-hierarchy branch (generic interior, continuous curve) and the inverted-hierarchy boundary (the m₃ → 0 degenerate limit, a single point or knife-edge). Annotate the NH solution (m₁ ≈ 0.8, m₂ ≈ 8.7, m₃ ≈ 50 meV) and the IH boundary. Include a marginal overlay showing the allowed region from current NuFIT data and future JUNO/DUNE sensitivity bands. This makes visually clear why IH is fine-tuned and NH is robust.  
   - Placement: After the section 'The Neutrino Mass Hierarchy is Normal, Not Inverted', to show the Z₃ algebra geometry.
3. **Falsifiability Summary: Three Independent Tests** — *flow diagram*  
   - Shows: A flow chart or table showing the three falsifiers as independent branches: (1) Lab decoherence (689 Hz) → fails if Λ ≠ 689 ± 20 Hz; (2) Neutrino hierarchy (normal) → fails if inverted hierarchy confirmed at >5σ; (3) Linear μ (= 1) → fails if μ > 1.02 at >2σ from large-scale structure. Include timescales (5–7 years for decoherence, ~2030 for JUNO/DUNE, ~2025–2030 for DESI/Euclid). Emphasize that a failure in any one does not automatically sink the others, but success in all three strengthens the framework's credibility.  
   - Placement: After 'The Falsifiability Landscape' section, summarizing the architecture of tests.

## The Rest of the World

1. **Black-Hole Saturation Diagram: Interior Ricci Scalar vs. Matter Density** — *schematic diagram*  
   - Shows: A cross-section of a black hole showing the event horizon, with the interior region marked to show how the Ricci scalar R saturates at R_max independent of the hole's total mass. A secondary axis plots the matter density profile ρ(r) approaching ρ_max at the core. The diagram illustrates the key point that saturation is a *mechanism* of finite-memory response, not a classical singularity.  
   - Placement: After the section 'Black holes and finite-curvature saturation', to provide spatial intuition for the saturation concept.
2. **Two-Route Convergence of the Deep-Infrared Refractive Index** — *plot*  
   - Shows: A bar plot or convergence diagram showing the two computed values: Path G (tree-level conformal anomaly) at R = √(4/3) ≈ 1.15470 and Path Osborn (one-loop SM running at M_Z) at R ≈ 1.15367. The plot includes error bands (0.1% agreement) and labels for the input sectors (conformality vs. full SM particle content). Demonstrates independent confirmation of the conformal-mode identification.  
   - Placement: After the section 'The deep-infrared refractive index: convergence by two independent routes', to visually reinforce the robustness of the R-value prediction.
3. **Decoherence-Rate Hierarchy in Measurement: Apparatus Dominance** — *flow diagram*  
   - Shows: A schematic showing the decoherence timescales τ_dec = 1/Λ for three systems: (1) macroscopic apparatus, (2) quantum object (atom/ion), (3) joint system. The diagram shows that Λ_apparatus ≫ Λ_object, and their coupling produces joint decoherence dominated by the apparatus. Arrows indicate information flow and the emergence of the pointer basis. Clarifies why apparent wave-function collapse is a consequence of coupling-induced decoherence rate acceleration.  
   - Placement: After the section 'The measurement problem resolves into physics', to provide visual intuition for the faster-crystallizer mechanism and the Wigner–friend resolution.

## The One Assumption & the Honest Frontier

1. **The Axiom and the Conditional Theorem** — *schematic diagram*  
   - Shows: A flowchart showing the logical structure: the antecedent (gravitational conformal mode = IR carrier) leads via the Komargodski–Schwimmer theorem to the consequent (a/c = 1/3), which GRUT adopts as the axiom α = 1/3. A branch shows the open problem (Riegert/Paneitz computation) that would prove the antecedent. This visualization clarifies that α is adopted because the conditional is verified, but the full first-principles derivation remains open.  
   - Placement: After the section on α = 1/3, before the discussion of the scale τ₀.
2. **The Breaking of the Adiabatic Redundancy by Finite Memory** — *flow diagram*  
   - Shows: A left-hand column showing the memoryless limit (L₀ → 0): a uniform rescaling of coordinates leaves physics unchanged (D is a symmetry). A right-hand column shows finite memory (L₀ ≠ 0): rescaling changes the combination L₀ k_phys, breaking the symmetry at order (L₀ k_phys)². A central arrow labeled 'Finite Memory F breaks D' shows the transition. Across the bottom, a scale bar shows the magnitude of the breaking at different ωτ₀ regimes (galactic, cosmological, tabletop).  
   - Placement: In the subsection on 'The One Scale, and the Breaking of Symmetry,' immediately after the explanation of L₀.
3. **The Open-Negative Ledger: Load-Bearing Gaps** — *data comparison*  
   - Shows: A two-column table: left column lists the eight most critical open negatives (α derivation, L₀ redundancy proof, R-route 3, dark sector closure statement, Born rule, flavor amplitude, Ricci saturation beyond WKB, φ_μν covariance). Right column shows for each: the closure condition (what would close it), the estimated effort level (low/medium/high), and the tier if not closed (open-negative). A horizontal bar at the bottom indicates which are load-bearing for cosmological predictions vs. which are refinements. This makes the frontier transparent and scope-bounded.  
   - Placement: After the list of open negatives, in the subsection 'The Honest Frontier.'
