"""
GRUTipedia v4 Expansion — Topics from the Beyond-GRUT rewrite,
12-sector program, 9 applications, and key results.

Import and extend DEFAULT_TOPICS in main.py.
"""

V4_TOPICS = [

    # ================================================================
    # FOUNDATIONAL AXIOMS
    # ================================================================
    {
        "slug": "axiom-a0-ctp-doubling",
        "title": "Axiom A0 — CTP Doubling",
        "definition_md": (
            "Every dynamical degree of freedom exists on forward (+) and backward (−) "
            "time contours of a Schwinger-Keldysh closed-time-path integral. This is "
            "the formal backbone for open-system dynamics, noise generation, and the "
            "fluctuation-dissipation theorem within GRUT."
        ),
        "equations_md": "Z = ∫ Dz₊ Dz₋ exp(iS[z₊] − iS[z₋] + noise terms)",
        "edition": 1,
        "tags": ["axiom", "foundation", "ctp"],
    },
    {
        "slug": "axiom-a1-directed-response",
        "title": "Axiom A1 — Directed Response",
        "definition_md": (
            "The dynamics of any field z is governed by a constitutive equation: "
            "τ d_t z + z = z_target[z], where z_target = δF/δz* is the variational "
            "derivative of a target functional F[z]. The field relaxes toward its target "
            "on timescale τ."
        ),
        "equations_md": "τ d_t z + z = z_target[z]\nz_target = δF/δz*",
        "edition": 1,
        "tags": ["axiom", "foundation", "constitutive"],
    },
    {
        "slug": "axiom-a2-complex-relaxation",
        "title": "Axiom A2 — Complex Relaxation Time",
        "definition_md": (
            "The relaxation time is complex: τ = τ_R + iτ_I, with τ_I = ℏ/2 identified "
            "as the imaginary relaxation time of the vacuum medium. The imaginary part "
            "generates quantum oscillation (Schrödinger); the real part generates "
            "dissipation (classicality). τ_I = ℏ/2 is identified, not derived."
        ),
        "equations_md": "τ = τ_R + iτ_I\nτ_I = ℏ/2 = 5.273×10⁻³⁵ J·s",
        "edition": 1,
        "tags": ["axiom", "foundation", "hbar", "identified"],
    },

    # ================================================================
    # CORE DERIVED STRUCTURES
    # ================================================================
    {
        "slug": "schrodinger-recovery",
        "title": "Schrödinger Equation Recovery",
        "definition_md": (
            "Setting τ_R = 0 (unitary limit) in the constitutive law and using the "
            "quadratic target functional F[z] = ∫{c₀|z|² + c₂|∇z|²}d³x recovers "
            "the Schrödinger equation exactly. Verified numerically: max deviation "
            "between constitutive and standard evolution is 9.2×10⁻¹⁶."
        ),
        "equations_md": "iℏ ∂_t z = [−ℏ²/(2m)∇² + V(x)]z\nVerified: max dev = 9.2×10⁻¹⁶",
        "edition": 1,
        "tags": ["sector-1", "recovered", "qm"],
    },
    {
        "slug": "mass-structural-ratio",
        "title": "Mass as Structural Ratio",
        "definition_md": (
            "Mass is not a free parameter inserted into the Laplacian. It is the ratio "
            "of the temporal response scale τ_I² to the spatial rigidity c₂ of the "
            "target functional: m = τ_I²/c₂. Heavy particles have small c₂ (weak "
            "spatial rigidity); light particles have large c₂."
        ),
        "equations_md": "m = τ_I²/c₂ = ℏ²/(4c₂)\nc₂ > 0 from stability\nc₀ = 1 from constitutive fixed point",
        "edition": 1,
        "tags": ["sector-1", "derived", "mass"],
    },
    {
        "slug": "target-functional",
        "title": "Target Functional F[z]",
        "definition_md": (
            "The most general local, quadratic, parity-preserving, isotropic functional "
            "of the complex response field z. Its variational derivative δF/δz* defines "
            "z_target. For a particle in a potential: c₀(x) = 1 + V(x)/2 gives the "
            "potential through the target multiplier."
        ),
        "equations_md": "F[z] = ∫{c₀(x)|z|² + c₂|∇z|²}d³x\nz_target = c₀(x)z − c₂∇²z",
        "edition": 1,
        "tags": ["sector-1", "variational", "foundation"],
    },
    {
        "slug": "born-rule-transparency",
        "title": "Born Rule Transparency",
        "definition_md": (
            "For the linear constitutive law, the MSRJD partition function Z(X) is "
            "independent of the stimulus X. Therefore Born probabilities are preserved: "
            "p(i) = |c_i|². The Born rule enters from QM upstream; the constitutive "
            "sector is transparent to it. Nonlinear corrections are < 10⁻⁴."
        ),
        "equations_md": "Z₀/Z₁ = 1 (exact, linear case)\nToken: born_rule_upstream_of_constitutive",
        "edition": 1,
        "tags": ["sector-1", "demonstrated", "born-rule"],
    },
    {
        "slug": "tau-r-instability",
        "title": "τ_R Instability (Structural Finding)",
        "definition_md": (
            "Naive addition of a real part τ_R > 0 to the wavefunction equation produces "
            "exponential GROWTH, not decay. All eigenvalues of (z_target − z) are positive "
            "(Hamiltonian eigenvalues), giving positive real parts when divided by "
            "(τ_R + iτ_I). Dissipation requires Lindblad/CTP noise structure, not just τ_R."
        ),
        "equations_md": "Re[E_n / (τ_R + iτ_I)] > 0 for all E_n > 0\n→ Growth, not decay",
        "edition": 1,
        "tags": ["sector-1", "structural", "failed-route", "ctp"],
    },
    {
        "slug": "ctp-lindblad-completion",
        "title": "CTP → Lindblad Open-System Completion",
        "definition_md": (
            "The correct open-system extension uses CTP doubling (A0): z → (z_r, z_a). "
            "The Gaussian noise kernel generates Lindblad dynamics for the density matrix. "
            "FDT-consistent: at T=0, D = γ (quantum noise floor). Thermalization verified: "
            "max population error vs Boltzmann = 1.4×10⁻⁶."
        ),
        "equations_md": "dρ/dt = −(i/ℏ)[H,ρ] + Σᵢ γᵢ 𝒟_Lᵢ[ρ]\nFDT: D = (2n_B + 1)γ",
        "edition": 1,
        "tags": ["sector-1", "demonstrated", "open-system", "lindblad"],
    },

    # ================================================================
    # RELATIVISTIC / GAUGE / ELECTROWEAK
    # ================================================================
    {
        "slug": "klein-gordon-recovery",
        "title": "Klein-Gordon Equation Recovery",
        "definition_md": (
            "Promoting the spatial target functional F to a Lorentz-covariant spacetime "
            "action S[z] gives the Klein-Gordon equation: (□ + M²)z = 0. Lorentz invariance "
            "forces temporal and spatial gradient costs equal, reducing two NR parameters "
            "(c₀, c₂) to one relativistic parameter (M)."
        ),
        "equations_md": "S = ∫{η^μν(∂_μz*)(∂_νz) − M²|z|²}d⁴x\nω² = k² + M² (dispersion)\nv_g = k/ω < c (causal)",
        "edition": 1,
        "tags": ["sector-1", "recovered", "relativistic"],
    },
    {
        "slug": "dirac-recovery",
        "title": "Dirac Equation Recovery",
        "definition_md": (
            "The Dirac equation is a first-order spinor directed-response equation: "
            "iℏ ∂_t ψ = H_D ψ = (α·p + βM)ψ. More natural than Klein-Gordon for "
            "the constitutive framework (first-order in time). Norm conserved to 10⁻¹¹."
        ),
        "equations_md": "iℏ ∂_t ψ = (α·p + βM)ψ\nz_target = [1 + H_D/(2τ_I)]ψ",
        "edition": 1,
        "tags": ["sector-1", "recovered", "relativistic", "spinor"],
    },
    {
        "slug": "gauge-coupling",
        "title": "Gauge Coupling (U(1))",
        "definition_md": (
            "The gradient in the target functional is promoted to a covariant derivative: "
            "D_μ = ∂_μ + ieA_μ. This is the unique minimal modification preserving local "
            "U(1) gauge invariance. Lorentz force verified to 1.4%. Aharonov-Bohm phase "
            "is linear in A."
        ),
        "equations_md": "F[z,A] = ∫{|z|² + c₂|Dz|²}\nD_μ = ∂_μ + ieA_μ",
        "edition": 1,
        "tags": ["sector-2", "recovered", "gauge"],
    },
    {
        "slug": "electroweak-structure",
        "title": "SU(2) × U(1)_Y Electroweak Structure",
        "definition_md": (
            "The response field z is promoted to an SU(2) doublet Z = (z₁, z₂)ᵀ with "
            "non-abelian covariant derivative. Charge quantization Q = T³ + Y/2 reproduces "
            "all SM fermion charges. All three anomaly cancellation conditions are exactly zero."
        ),
        "equations_md": "D_μ Z = ∂_μ Z + ig(σᵃ/2)W_μᵃ Z + ig'(Y/2)B_μ Z\nQ = T³ + Y/2\nΣY = ΣY³ = ΣY(doublets) = 0",
        "edition": 1,
        "tags": ["sector-2", "recovered", "electroweak", "anomaly"],
    },
    {
        "slug": "higgs-mechanism",
        "title": "Higgs Mechanism",
        "definition_md": (
            "The Higgs field H is an SU(2) doublet directed-response field with a "
            "Mexican-hat target functional. VEV v = 246 GeV breaks SU(2)×U(1)_Y → U(1)_EM. "
            "W±, Z⁰ massive; photon massless (Q⟨H⟩ = 0 exactly). ρ = 1.000000 at tree level. "
            "Fermion masses M_f = y_f v/√2 (Yukawas are FREE)."
        ),
        "equations_md": "V(H) = −μ²|H|² + λ|H|⁴\nv = μ/√λ = 246 GeV\nm_W = gv/2 = 80.3 GeV\nm_Z = √(g²+g'²)v/2 = 91.1 GeV\nρ = 1.000000",
        "edition": 1,
        "tags": ["sector-2", "recovered", "higgs", "ssb"],
    },

    # ================================================================
    # NOVEL SECTOR: GRAVITATIONAL DECOHERENCE
    # ================================================================
    {
        "slug": "universal-scaling-law",
        "title": "Universal Scaling Law (USL)",
        "definition_md": (
            "The flagship GRUT prediction. Gravitational decoherence rate with ZERO free "
            "parameters: Λ = Gm²S(l/R)/(ℏl). Derived from the tree-level gravitational "
            "self-energy in the CTP influence functional. Spans 120 orders of magnitude "
            "in decoherence rate. Standard QM predicts Λ = 0."
        ),
        "equations_md": "Λ = Gm²S(l/R)/(ℏl)\nZero free parameters\nReference: Λ(10 pg, 100 nm) = 632.9 Hz",
        "edition": 1,
        "tags": ["sector-3", "predictive", "usl", "flagship"],
    },
    {
        "slug": "extended-body-correction",
        "title": "Extended-Body Suppression S(l/R)",
        "definition_md": (
            "For a uniform-density sphere of radius R with superposition separation l: "
            "S = 1 for l ≥ 2R (point-mass limit); S = (l/R)³/6 for l < 2R (near field). "
            "At l/R = 0.1: suppression is 6,000×. Point-mass Diósi-Penrose models miss this."
        ),
        "equations_md": "S(l/R) = min(1, (l/R)³/6)\nAt l/R = 0.1: S = 1.67×10⁻⁴",
        "edition": 1,
        "tags": ["sector-3", "predictive", "geometry", "diosi"],
    },
    {
        "slug": "pressure-plateau",
        "title": "Pressure Plateau Prediction",
        "definition_md": (
            "As gas pressure P → 0, the decoherence rate should plateau (GRUT) or "
            "vanish (standard QM). The crossover pressure P* where gravity equals gas "
            "decoherence is computed exactly. For 10 pg at 100 nm: P* ≈ 4×10⁻⁹ Pa. "
            "This is the primary experimental discriminant."
        ),
        "equations_md": "GRUT: Λ → Λ_grav > 0 as P → 0\nStandard QM: Λ → 0\nP* = 4.05×10⁻⁹ Pa (reference)",
        "edition": 1,
        "tags": ["sector-3", "predictive", "experiment", "falsifiable"],
    },
    {
        "slug": "bell-state-protection",
        "title": "Bell-State Entanglement Protection",
        "definition_md": (
            "Anti-correlated Bell states |LR⟩ + |RL⟩ decohere SLOWER than product states "
            "because the center of mass is fixed, reducing the gravitational self-energy "
            "difference. At d = 200 nm: Bell is 17% slower. This is a three-way discriminant: "
            "QM (both 0), CSL (equal), GRUT (Bell protected)."
        ),
        "equations_md": "Λ_Bell < Λ_product\nAt d = 200 nm: 17% protection\nGHZ N=10: 67% suppression",
        "edition": 1,
        "tags": ["sector-3", "predictive", "entanglement", "many-body"],
    },
    {
        "slug": "geometric-kink",
        "title": "Geometric Kink at l ≈ 1.8R",
        "definition_md": (
            "The decoherence rate Λ(l) has a peak at l ≈ 1.8R. Near field: Λ ~ l² "
            "(increases). Far field: Λ ~ 1/l (decreases). A single power-law fit fails "
            "with residual 0.56 dex (265%). The peak location is set by R with zero free "
            "parameters — a geometric fingerprint."
        ),
        "equations_md": "Peak at l = 91.2 nm for R = 50 nm\nΛ_peak = 694.1 Hz\nPower-law failure: 0.56 dex",
        "edition": 1,
        "tags": ["sector-3", "predictive", "geometry", "signature"],
    },
    {
        "slug": "six-signature-discriminant",
        "title": "Six-Signature Discriminant Framework",
        "definition_md": (
            "Six independent experimental signatures: (1) pressure plateau, (2) geometry "
            "193× span, (3) entanglement −17%, (4) l-scaling slope −1, (5) kink at 1.8R, "
            "(6) mass-squared ratio. No tested alternative model reproduces all six "
            "simultaneously."
        ),
        "equations_md": "Sig1: plateau | Sig2: geometry | Sig3: entanglement\nSig4: 1/l | Sig5: kink | Sig6: m²",
        "edition": 1,
        "tags": ["sector-3", "predictive", "kill-framework", "falsifiable"],
    },
    {
        "slug": "kill-framework",
        "title": "Adversarial Kill Framework",
        "definition_md": (
            "The solver programmatically tests whether alternative models (constant floor, "
            "power-law floor, CSL, DP point-mass) can mimic GRUT's signatures. No tested "
            "alternative with ≤ 2 free parameters fits all six. The power-law degeneracy "
            "on mass scan alone was caught; geometry + entanglement break it."
        ),
        "equations_md": "solver.try_kill('all')\nConstant floor: fails geometry + entanglement\nCSL: fails entanglement\nDP: fails geometry",
        "edition": 1,
        "tags": ["sector-3", "adversarial", "methodology"],
    },
    {
        "slug": "quantum-classical-boundary-surface",
        "title": "Quantum-Classical Boundary Surface",
        "definition_md": (
            "The boundary where Λ_total × t_obs = 1 is a computed surface in (m, l, t) "
            "space: m* = √(ℏl/Gt). Not postulated (Copenhagen), not absent (many-worlds), "
            "not deferred (standard decoherence). Computed with zero free parameters."
        ),
        "equations_md": "m* = √(ℏl/(Gt))\nAt l = 100 nm, t = 1 s: m* = 0.40 fg",
        "edition": 1,
        "tags": ["sector-3", "predictive", "boundary"],
    },

    # ================================================================
    # KEY CONSTANTS AND NUMBERS
    # ================================================================
    {
        "slug": "c-final-anomaly",
        "title": "C_Final — 3-Loop Gravitational Anomaly Coefficient",
        "definition_md": (
            "Scheme-protected nonlocal operator from 3-loop gravitational anomaly. "
            "C_Final = 3(99 + 2π² + 576ln2·ζ(3))/(16384π⁶) = 1.14021×10⁻⁴. "
            "Verified to 15 significant figures."
        ),
        "equations_md": "C_Final = 1.14021054×10⁻⁴\nR = |C_Cosmo/C_Final| = 1.15428\nAnomaly channel: Λ_anom/Λ_grav ~ 10⁻⁸",
        "edition": 1,
        "tags": ["constant", "anomaly", "scheme-protected"],
    },
    {
        "slug": "emergent-41-9-myr",
        "title": "41.9 Myr Emergent Timescale",
        "definition_md": (
            "The USL evaluated at t_coh = 41.9 Myr gives m = 20,818 amu at l = 1 μm "
            "— the mass of a large protein. This marks the macromolecular boundary: "
            "below it quantum coherence persists cosmologically; above it decoherence "
            "is rapid. Not fundamental — an emergent crossover in the scaling hierarchy."
        ),
        "equations_md": "m = √(ℏl/(G·t)) at t = 41.9 Myr, l = 1 μm\nm = 20,818 amu ≈ 3.5×10⁻²³ kg",
        "edition": 1,
        "tags": ["emergent", "timescale", "crossover"],
    },
    {
        "slug": "diamond-lock",
        "title": "Diamond Lock (τ² = 3/2)",
        "definition_md": (
            "The pre-rewrite GRUT vacuum constant. Reinterpreted as the classical "
            "constitutive sector's relaxation parameter. τ_R/τ_I = 2.449 in natural "
            "units. Connected to the quantum sector through the CTP high-temperature limit."
        ),
        "equations_md": "τ² = 3/2 (classical sector, LOCKED)\nτ_R/τ_I = √(3/2)/(1/2) = 2.449",
        "edition": 1,
        "tags": ["constant", "classical", "locked", "phase-i"],
    },
    {
        "slug": "ward-residual",
        "title": "Ward Residual (α = 1.177)",
        "definition_md": (
            "The self-consistent T-matrix violates the particle-hole Ward identity at "
            "leading order: α = 1.177 ± 0.043. Exchange correction does NOT restore it. "
            "Total constitutive systematic: 3.6%. The gravitational sector (USL) is "
            "structurally insensitive to this error."
        ),
        "equations_md": "ΔW ~ κ₀^α with α = 1.177\nδ_total = 3.6% (quadrature)\nGravitational sector: immune",
        "edition": 1,
        "tags": ["systematic", "ward", "program-h"],
    },
    {
        "slug": "markovian-validity-envelope",
        "title": "Markovian Validity Envelope",
        "definition_md": (
            "The USL derivation assumes Markovian bath coupling. Valid below W_τ* = 0.7 "
            "decades (ε_M < 5%). Invalid above W_τ** = 1.8 decades (full memory kernel "
            "required). Lab nanoparticle experiments: W_τ ~ 0.3 decades → VALID."
        ),
        "equations_md": "W_τ* = 0.7 decades (VALID boundary)\nW_τ** = 1.8 decades (INVALID boundary)\nε_M ≈ 0.55(1 − exp(−W_τ/4.5))",
        "edition": 1,
        "tags": ["validity", "markov", "program-g"],
    },

    # ================================================================
    # SECTORS 4-12 (STATUS ENTRIES)
    # ================================================================
    {
        "slug": "sector-4-gravity-status",
        "title": "Sector 4 — Gravity (Partial)",
        "definition_md": (
            "GRUT operates as matter within standard Einstein gravity. The static "
            "scalar-only TOV gives f = −17.71 (WORSENS interior, LOCKED). All 10 "
            "singularity-resolution routes are frozen. Weak-field correction: 10⁻¹⁶ "
            "(observationally silent). No graviton, no backreaction closure."
        ),
        "equations_md": "f(R_eq) = −17.71 (LOCKED negative)\nSingularity routes: 0/10 succeeded\nδ_beta ~ 10⁻¹⁶",
        "edition": 1,
        "tags": ["sector-4", "partial", "gravity", "negative-result"],
    },
    {
        "slug": "sector-5-cosmology-status",
        "title": "Sector 5 — Cosmology (Partial/Conditional)",
        "definition_md": (
            "Dark-energy replacement PERMANENTLY FAILED: ρ_eq < 0 is anti-accelerating. "
            "Significant computational infrastructure exists (H(z), growth, lensing, "
            "rotation curves). Screening length is a FREE PARAMETER (naturalness problem)."
        ),
        "equations_md": "ρ_eq = −M²/(2τ²r⁴) < 0 → ANTI-ACCELERATING\nDark energy: PERMANENTLY FAILED\nScreening length: FREE",
        "edition": 1,
        "tags": ["sector-5", "partial", "cosmology", "failed-claim"],
    },
    {
        "slug": "sector-6-qcd-entry",
        "title": "Sector 6 — QCD Entry Point",
        "definition_md": (
            "SU(3) color gauge structure implemented: Gell-Mann generators, structure "
            "constants, covariant derivatives, field strength — all validated to machine "
            "precision. Wilson loop scaffolded (toy lattice). Confinement, asymptotic "
            "freedom, hadron spectrum: all OPEN."
        ),
        "equations_md": "[Tᵃ, Tᵇ] = ifᵃᵇᶜTᶜ (err < 10⁻¹⁶)\nC_F = 4/3 (exact)\nConfinement: OPEN",
        "edition": 1,
        "tags": ["sector-6", "open", "qcd", "su3"],
    },
    {
        "slug": "d7-d8-sign-error",
        "title": "D7/D8 Sign Error Correction",
        "definition_md": (
            "The original strong-field program claimed 12.7× constructive amplification. "
            "Book XVI Alpha discovered m_eff = M + Σ is wrong (Birkhoff); correct is "
            "m = M − Σ. Actual A_eff = 0.11, not 2.0. All conditional surpluses collapsed. "
            "Corrected result is LOCKED."
        ),
        "equations_md": "WRONG: m_eff = M + Σ → A_eff ≈ 2.0\nCORRECT: m = M − Σ → A_eff = 0.11\nAll routes: FROZEN",
        "edition": 1,
        "tags": ["failed-route", "sign-error", "locked", "gravity"],
    },

    # ================================================================
    # APPLICATIONS
    # ================================================================
    {
        "slug": "app-interferometry-catalog",
        "title": "Application: Matter-Wave Interferometry Catalog",
        "definition_md": (
            "GRUT predictions for 7 published interferometry experiments (C60 through "
            "25 kDa molecules). Gravitational signal: 10⁻¹⁵ to 10⁻¹⁸ Hz at these masses. "
            "Completely undetectable. GRUT survives all published data. Mass frontier "
            "for detection: ~0.1 fg at P = 10⁻¹³ Pa."
        ),
        "equations_md": "V_grav = exp(−Λ_grav × t_flight)\nAll 7 experiments: V_drop < 10⁻¹⁵\nMass frontier: m > 7.6×10¹⁰ amu",
        "edition": 1,
        "tags": ["application", "interferometry", "experiment"],
    },
    {
        "slug": "app-bullet-cluster",
        "title": "Application: Bullet Cluster (Null Result)",
        "definition_md": (
            "The Bullet Cluster (1.5×10¹⁵ M_sun) is classical by 54 orders of magnitude. "
            "Λ_grav = 10⁹¹ Hz. Weak-field lensing correction: 10⁻¹⁶. GRUT adds nothing "
            "to cluster lensing beyond GR. Dark-matter inference unchanged. NULL RESULT."
        ),
        "equations_md": "Λ_grav = 1.58×10⁹¹ Hz\nClassical by 10⁵⁴\nLensing modification: NONE",
        "edition": 1,
        "tags": ["application", "null-result", "cluster"],
    },
    {
        "slug": "app-observer-dynamics",
        "title": "Application: Observer/Measurement Dynamics",
        "definition_md": (
            "The 'observer' is the fastest decoherence channel. Electron: gas (28 s). "
            "Virus: gas (10 fs). Baseball: gas (20 zs). Earth: GRAVITY (10⁻⁶⁷ s). "
            "Schrödinger's cat: decohered in 10⁻²⁷ s. The QC boundary is smooth, "
            "computed, not postulated."
        ),
        "equations_md": "Observer = fastest Λ channel\nCat: t_total = 1.2×10⁻²⁷ s\nEarth: gravity-only at 10⁻⁶⁷ s",
        "edition": 1,
        "tags": ["application", "measurement", "observer"],
    },
    {
        "slug": "app-early-universe",
        "title": "Application: Early-Universe Decoherence",
        "definition_md": (
            "In the hot early universe, thermal scattering dominates gravity by up to "
            "10⁹⁹ (at T_Planck). Gravity wins only after the universe cools below "
            "~1400 K (z ~ 500, after recombination). Today gravity dominates by 10²⁴. "
            "Lab experiments at millikelvin are deep in the gravity-dominated regime."
        ),
        "equations_md": "Λ_grav = 632.9 Hz (constant, T-independent)\nCrossover: T ~ 1400 K for 10 pg\nToday: gravity/thermal = 10²⁴",
        "edition": 1,
        "tags": ["application", "cosmology", "thermal"],
    },
    {
        "slug": "app-solar-system-formation",
        "title": "Application: Solar System Formation Crossover",
        "definition_md": (
            "During planetary formation, gravitational decoherence first dominates "
            "above the centimeter pebble scale (R ~ 2 mm). Below: nebular gas "
            "classicalizes everything. Above: gravity alone suffices. Earth is "
            "classical by 10⁶⁰+ orders."
        ),
        "equations_md": "Crossover: R ~ 2 mm (dust-to-pebble transition)\nEarth: Λ_grav = 1.8×10⁶⁶ Hz",
        "edition": 1,
        "tags": ["application", "solar-system", "formation"],
    },
    {
        "slug": "app-biology",
        "title": "Application: Biology in the Classical Regime",
        "definition_md": (
            "Water thermal bath beats gravitational decoherence by 10¹⁵ to 10³³ at "
            "every biological scale — from amino acids to organisms. Life operates "
            "entirely in the thermally-decohered classical regime. This is why "
            "biology works: classical, reliable, reproducible."
        ),
        "equations_md": "Tubulin: t_grav ~ 10⁶ yr, t_water ~ 10⁻¹⁵ s\nRatio: 10²⁸ (water wins)\nAll biology: water dominates",
        "edition": 1,
        "tags": ["application", "biology", "classical"],
    },
    {
        "slug": "app-consciousness-microtubule",
        "title": "Application: Consciousness / Microtubule Calculation",
        "definition_md": (
            "The closing calculation. Λ_grav per tubulin dimer = 2.69×10⁻¹⁴ Hz "
            "(t ~ 1.2 Myr). Linear scaling: 38,000 neurons for 40 Hz gamma — "
            "a striking mathematical coincidence. Water decoherence: 10⁻¹⁵ s. "
            "Gap: 28 orders. The thermal wall kills the Orch-OR hypothesis."
        ),
        "equations_md": "Λ/dimer = 2.69×10⁻¹⁴ Hz\nN for 40 Hz = 38,000 neurons\nt_water = 9.86×10⁻¹⁶ s\nGap: 10²⁸",
        "edition": 1,
        "tags": ["application", "consciousness", "orch-or", "closing"],
    },
    {
        "slug": "app-structure-formation",
        "title": "Application: Cosmological Structure Formation",
        "definition_md": (
            "The quantum-classical boundary evolves with the universe. At recombination: "
            "protons are quantum, dust grains are classical. Boundary mass m* = 35 ng "
            "at the horizon scale. Gravity is the observer that classicalizes the universe."
        ),
        "equations_md": "m*(recombination) = 35 ng\nProton: quantum (t_decoh = 18 Myr)\nDust grain: classical (t_decoh = 0.16 ms)",
        "edition": 1,
        "tags": ["application", "cosmology", "structure-formation"],
    },

    # ================================================================
    # EXPERIMENTAL PLATFORMS
    # ================================================================
    {
        "slug": "platform-mu-prime",
        "title": "Mu-Prime Operating Point",
        "definition_md": (
            "The GRUT-II hardware-verified reference platform: 196 fg diamond sphere, "
            "R = 237 nm, l = 474 nm (= 2R, point-mass boundary), T = 4 K, P = 10⁻¹³ Pa. "
            "USL/gas ratio ~ 2.9. T2 gap 125×, mass gap 700× from current tech."
        ),
        "equations_md": "m = 196 fg, R = 237 nm, l = 474 nm\nΛ_USL = 5.1×10⁻² Hz\nTimeline: 5-15 years",
        "edition": 1,
        "tags": ["experiment", "platform", "reference"],
    },
    {
        "slug": "platform-nanodiamond",
        "title": "Levitated Nanodiamond Platform",
        "definition_md": (
            "The primary near-term experimental target: m = 10 pg, R = 50 nm, "
            "l = 100 nm, T = 10 mK, P = 10⁻¹⁰ Pa. GRUT predicts Λ = 632.9 Hz. "
            "Standard QM predicts Λ → 0. Coherence time: GRUT = 1.6 ms vs QM = 0.6 s."
        ),
        "equations_md": "Λ_grav = 632.9 Hz\nt_coh(GRUT) = 1.6 ms\nt_coh(QM) = 0.6 s\nRatio: 406×",
        "edition": 1,
        "tags": ["experiment", "platform", "nanodiamond"],
    },

    # ================================================================
    # METHODOLOGY
    # ================================================================
    {
        "slug": "grut-solver",
        "title": "grut_solver Package",
        "definition_md": (
            "The computational engine implementing the entire GRUT framework. "
            "46 modules across 12 sectors. 122 validated tests. 9 application modules. "
            "2 publication figures. Adversarial kill framework. CLI interface. "
            "Zero free parameters in the gravitational decoherence sector."
        ),
        "equations_md": "from grut_solver import GRUTSolver\nsolver = GRUTSolver()\nresult = solver.decoherence(m, R, l, T, P)",
        "edition": 1,
        "tags": ["software", "solver", "infrastructure"],
    },
    {
        "slug": "status-taxonomy",
        "title": "Status Taxonomy",
        "definition_md": (
            "Every result is classified: Recovered (matches known physics), "
            "Predictive (zero-parameter new prediction), Partial (some results, "
            "key closures missing), Open (entry point only), Failed (tested, did not work), "
            "Nonclaim (explicitly not claimed)."
        ),
        "equations_md": "Recovered | Predictive | Partial | Conditional | Open | Failed | Nonclaim",
        "edition": 1,
        "tags": ["methodology", "taxonomy", "discipline"],
    },

    # ================================================================
    # SECTORS 7-12 (FRONTIER ENTRIES)
    # ================================================================
    {
        "slug": "sector-7-flavor-masses",
        "title": "Sector 7 — Flavor / Masses (Open)",
        "definition_md": (
            "Yukawa couplings y_f are free parameters (same as SM). Mass hierarchy "
            "y_top/y_electron = 338,552 is documented but not explained. CKM mixing "
            "angles are input data, not derived. No flavor prediction from GRUT."
        ),
        "equations_md": "M_f = y_f v/√2\ny_top/y_electron = 338,552\nCKM: V_us=0.225, V_cb=0.041, V_ub=0.004",
        "edition": 1,
        "tags": ["sector-7", "open", "flavor", "yukawa"],
    },
    {
        "slug": "sector-8-neutrinos",
        "title": "Sector 8 — Neutrinos (Open)",
        "definition_md": (
            "Dirac and Majorana/seesaw mass entry points documented. PMNS mixing angles "
            "and oscillation observables scaffolded. No neutrino mass mechanism derived. "
            "Mass ordering and CP phase remain open."
        ),
        "equations_md": "m_Dirac = y_ν v/√2 (y ~ 10⁻¹²)\nm_seesaw ~ (y_ν v)²/(2M_R)\nΔm²₂₁ = 7.53×10⁻⁵ eV²\nθ₁₂ = 33.4°",
        "edition": 1,
        "tags": ["sector-8", "open", "neutrino", "pmns"],
    },
    {
        "slug": "sector-9-dark-matter",
        "title": "Sector 9 — Dark Matter (Open)",
        "definition_md": (
            "Candidate viability criteria defined: stable, neutral, weakly coupled, "
            "relic-compatible. No GRUT dark-matter candidate identified. No relic density "
            "calculation. No detection prediction. Search framework provided."
        ),
        "equations_md": "Ω_DM h² = 0.120 (target)\nσ_SI < 10⁻⁴⁶ cm² (direct detection bound)\nCandidate: NONE identified",
        "edition": 1,
        "tags": ["sector-9", "open", "dark-matter", "search"],
    },
    {
        "slug": "sector-10-baryogenesis",
        "title": "Sector 10 — Baryogenesis (Open)",
        "definition_md": (
            "CTP/nonequilibrium structure (A0) provides structural support for Sakharov "
            "condition 3 (departure from equilibrium). Conditions 1 (B-violation) and 2 "
            "(CP-violation) remain open. No baryogenesis mechanism claimed."
        ),
        "equations_md": "η_B = (n_B − n_B̄)/n_γ ~ 6.1×10⁻¹⁰ (target)\nSakharov 1: OPEN\nSakharov 2: OPEN\nSakharov 3: STRUCTURAL (CTP)",
        "edition": 1,
        "tags": ["sector-10", "open", "baryogenesis", "sakharov", "ctp"],
    },
    {
        "slug": "sector-11-coupling-unification",
        "title": "Sector 11 — Coupling Unification (Open)",
        "definition_md": (
            "One-loop running diagnostics for α₁, α₂, α₃. SM couplings do NOT unify "
            "(miss by ~3% at ~10¹⁵ GeV). Whether GRUT modifies the running is an "
            "open question. No unification result claimed."
        ),
        "equations_md": "1/α_i(μ) = 1/α_i(M_Z) − b_i/(2π) ln(μ/M_Z)\nSM: does NOT unify\nGRUT modification: OPEN",
        "edition": 1,
        "tags": ["sector-11", "open", "unification", "rg-flow"],
    },
    {
        "slug": "sector-12-quantum-gravity",
        "title": "Sector 12 — Quantum Gravity (Open)",
        "definition_md": (
            "The deepest open gate. Five closure conditions enumerated, zero met: "
            "(1) graviton, (2) UV completion, (3) backreaction, (4) black-hole information, "
            "(5) classical GR recovery. CTP provides a formal connection point. "
            "Current interface is semiclassical only."
        ),
        "equations_md": "Closure conditions: 0/5 met\nα_grav = r_S/λ_C ~ 4×10⁻¹³ (unmeasurable)\nGraviton: NONE\nUV completion: NONE",
        "edition": 1,
        "tags": ["sector-12", "open", "quantum-gravity", "closure-gate"],
    },

    # ================================================================
    # ADDITIONAL KEY CONCEPTS
    # ================================================================
    {
        "slug": "crossover-pressure",
        "title": "Crossover Pressure P*",
        "definition_md": (
            "The pressure at which gas decoherence equals gravitational decoherence. "
            "Below P*, the GRUT gravitational signal dominates. Above P*, gas collisions "
            "mask the signal. For 10 pg at 100 nm: P* ≈ 4.05×10⁻⁹ Pa."
        ),
        "equations_md": "P* ≈ 4.05×10⁻⁹ Pa (reference platform)\nBelow P*: gravity dominates\nAbove P*: gas dominates",
        "edition": 1,
        "tags": ["predictive", "experiment", "crossover"],
    },
    {
        "slug": "probability-current",
        "title": "Probability Current",
        "definition_md": (
            "j = (ℏ/m) Im(z* ∇z). Matches standard QM exactly. The continuity equation "
            "∂_t ρ + ∇·j = 0 holds in the unitary limit. Verified numerically."
        ),
        "equations_md": "j = (ℏ/m) Im(z* ∇z)\n∂_t ρ + ∇·j = 0 (unitary limit)\nRelative violation: 0.0046 (FD-limited)",
        "edition": 1,
        "tags": ["sector-1", "derived", "continuity"],
    },
    {
        "slug": "ehrenfest-theorem",
        "title": "Ehrenfest Theorem / Classical Limit",
        "definition_md": (
            "For quadratic potentials, ⟨x⟩(t) follows the classical trajectory. "
            "The WKB limit recovers the Hamilton-Jacobi equation. Verified: relative "
            "error < 0.5% over multiple oscillation periods."
        ),
        "equations_md": "d⟨x⟩/dt = ⟨p⟩/m\nd⟨p⟩/dt = −⟨∇V⟩\nWKB: ∂_t S + (∇S)²/(2m) + V = 0",
        "edition": 1,
        "tags": ["sector-1", "demonstrated", "classical-limit"],
    },
    {
        "slug": "charge-quantization",
        "title": "Charge Quantization Q = T³ + Y/2",
        "definition_md": (
            "Electric charge is quantized because it is the sum of two discrete quantum "
            "numbers. All 7 SM fermion charges reproduced exactly: ν_e (0), e (-1), "
            "u (+2/3), d (-1/3), etc."
        ),
        "equations_md": "Q = T³ + Y/2\nν_eL: Q = +1/2 + (-1)/2 = 0\ne_L: Q = -1/2 + (-1)/2 = -1\nu_L: Q = +1/2 + (1/3)/2 = +2/3",
        "edition": 1,
        "tags": ["sector-2", "recovered", "charge", "exact"],
    },
    {
        "slug": "anomaly-cancellation",
        "title": "Anomaly Cancellation",
        "definition_md": (
            "Three conditions verified for one complete SM generation: ΣY = 0 "
            "(gravitational), ΣY³ = 0 (cubic), ΣY over doublets = 0 (mixed). "
            "Requires N_c = 3 colors and specific hypercharge assignments. "
            "All three are exactly zero."
        ),
        "equations_md": "ΣY = 0 (exact)\nΣY³ = 0 (exact)\nΣY(doublets) = 0 (exact)\nRequires N_c = 3",
        "edition": 1,
        "tags": ["sector-2", "recovered", "anomaly", "exact"],
    },
    {
        "slug": "n-particle-diosi-functional",
        "title": "N-Particle Diósi Functional",
        "definition_md": (
            "The gravitational decoherence rate for N particles: "
            "Λ = (G/ℏ) Σᵢⱼ mᵢmⱼ [1/d_LL + 1/d_RR − 1/d_LR − 1/d_RL]. "
            "Self-terms give the single-particle USL; cross-terms depend on quantum "
            "state (entangled vs product). Implemented for arbitrary configurations."
        ),
        "equations_md": "Λ = (G/ℏ) Σᵢⱼ mᵢmⱼ [kernel]\nSelf-terms (i=j): standard USL\nCross-terms (i≠j): state-dependent",
        "edition": 1,
        "tags": ["sector-3", "predictive", "many-body", "diosi"],
    },
    {
        "slug": "ghz-suppression",
        "title": "GHZ Suppression Scaling",
        "definition_md": (
            "For N-particle GHZ states |LL...L⟩ + |RR...R⟩ at d = 200 nm spacing: "
            "N=2: 33% suppression, N=5: 58%, N=10: 67%, N=20: 72%. Entangled "
            "multi-particle states are progressively more protected."
        ),
        "equations_md": "N=2: GHZ/product = 0.667\nN=5: 0.417\nN=10: 0.325\nN=20: 0.277",
        "edition": 1,
        "tags": ["sector-3", "predictive", "ghz", "many-body"],
    },
    {
        "slug": "decoherence-budget",
        "title": "Multi-Channel Decoherence Budget",
        "definition_md": (
            "For any (m, R, l, T, P), the framework computes ALL decoherence channels: "
            "gravitational, gas collision, blackbody, trap recoil, charge noise, "
            "vibrational, readout backaction, and anomaly. The binding constraint "
            "is identified. Uncertainty propagation included."
        ),
        "equations_md": "Λ_total = Λ_grav + Λ_gas + Λ_BB + Λ_trap + ...\nBinding constraint: identified per platform\nSolver: solver.decoherence(m, R, l, T, P)",
        "edition": 1,
        "tags": ["sector-3", "predictive", "budget", "solver"],
    },

    # ── Sector 13: Consciousness and 1 Space ─────────────────
    {
        "slug": "sector-13-consciousness-1space",
        "title": "Sector 13 — Consciousness and 1 Space",
        "definition_md": (
            "The first speculative sector in GRUT. Extends the Application 9 thermal-wall result "
            "into a new direction: consciousness as an edge state at the quantum-classical boundary, "
            "with coupling to the universal target functional (1 Space). Tagged Speculative / Pre-formal. "
            "7 computed results, 4 model-dependent estimates, 5 speculative claims, 7 kill conditions."
        ),
        "equations_md": "Status: Speculative / Pre-formal\nModules: 7\nTests: 15 (all passing)\nThermal wall: NOT breached (~25 orders remain)",
        "edition": 1,
        "tags": ["sector-13", "speculative", "consciousness"],
    },
    {
        "slug": "one-space-target-functional",
        "title": "1 Space — The Universal Target Functional",
        "definition_md": (
            "1 Space is the totality of F[z] — the universal target functional of the GRUT framework. "
            "Every physical system is a configuration of z relaxing toward F[z]. Before decoherence "
            "carves classical branches, everything sits in 1 Space: undifferentiated quantum information. "
            "Holographic bound: ~10^124 bits for the observable universe."
        ),
        "equations_md": "F[z] = integral{c_0|z|^2 + c_2|grad z|^2 + ...}\nS_holo = A/(4 L_P^2) ~ 10^124 bits\nBekenstein: S_Bek <= 2pi R E/(hbar c)",
        "edition": 1,
        "tags": ["sector-13", "speculative", "1-space", "information-theory"],
    },
    {
        "slug": "crystalline-boundary",
        "title": "The Crystalline Boundary",
        "definition_md": (
            "The classical world as the outer structure where z has relaxed into definite configurations. "
            "In GRUT, the quantum-classical boundary is where the constitutive response completes: "
            "z reaches z_target and superposition collapses. The crystalline boundary is the edge "
            "of 1 Space — where quantum becomes classical."
        ),
        "equations_md": "tau dz/dt + z = z_target[z]\nClassical: z = z_target (response complete)\nQuantum: z != z_target (response ongoing)",
        "edition": 1,
        "tags": ["sector-13", "speculative", "boundary", "classical-limit"],
    },
    {
        "slug": "consciousness-edge-state",
        "title": "Consciousness as Edge State",
        "definition_md": (
            "Speculative proposal: consciousness is neither fully quantum nor fully classical. "
            "It is an edge state at the quantum-classical boundary — a system that maintains a "
            "live connection to 1 Space while existing as classical structure. A rock is fully "
            "decohered; a photon is fully coherent; a conscious brain sits at the transition."
        ),
        "equations_md": "Edge condition: Lambda_total * t_process ~ O(1)\nFor gamma oscillation: Lambda = 40 Hz, t = 25 ms\nRequires: ~38,000 neurons (biologically feasible)",
        "edition": 1,
        "tags": ["sector-13", "speculative", "consciousness", "edge-state"],
    },
    {
        "slug": "ordered-water-correction",
        "title": "Ordered Water Correction",
        "definition_md": (
            "Water confined in microtubule channels (~15 nm diameter) has reduced density and "
            "mobility compared to bulk water. This module computes the corrected thermal decoherence "
            "time. Physical estimate: improvement of ~0.01 orders. Even extreme confinement (factor 0.001) "
            "only improves by ~3 orders. The 25-order thermal wall is NOT breached."
        ),
        "equations_md": "Lambda_confined = f * Lambda_bulk\nf = density_factor * sqrt(mobility_factor)\nPhysical f ~ 0.97 (MT channel)\nGap at f=0.001: ~25.6 orders remain",
        "edition": 1,
        "tags": ["sector-13", "computed", "ordered-water", "thermal-wall"],
    },
    {
        "slug": "pattern-survival-decoherence",
        "title": "Pattern Survival Under Decoherence",
        "definition_md": (
            "Can collective information survive when individual quantum states decohere? "
            "Three analyses: (1) Mutual information I(A:B) in coupled chains decays at ~same rate "
            "as local coherence. (2) Topological winding number on 13-site ring: WORSE than local "
            "for uncorrelated noise (ratio 0.70x). (3) GHZ entanglement entropy decays N times "
            "faster than single qubit. All three DISFAVOR naive pattern survival."
        ),
        "equations_md": "Mutual info: I(A:B) = S(A) + S(B) - S(AB)\nGHZ t_half = ln2/(2*N*gamma)\nWinding number error: delta_nu ~ sqrt(N)*sigma/(2pi)",
        "edition": 1,
        "tags": ["sector-13", "computed", "pattern-survival", "lindblad"],
    },
    {
        "slug": "neural-resonance-condition",
        "title": "Neural Resonance Condition",
        "definition_md": (
            "The 38,000-neuron number: at tubulin mass (110 kDa), conformational displacement (0.7 nm), "
            "linear scaling gives N = 40 Hz / (Lambda_single * dimers_per_neuron) ~ 38,064 neurons. "
            "This is ~0.5 cortical columns — a biologically realistic localized network. The resonance "
            "extends to other brainwave bands: theta (6 Hz) needs ~253,000 neurons, alpha (10 Hz) needs "
            "~152,000."
        ),
        "equations_md": "N = f_target / (Lambda_grav * N_dimers_per_neuron)\nGamma (40 Hz): N ~ 38,000\nAlpha (10 Hz): N ~ 152,000\nTheta (6 Hz): N ~ 253,000",
        "edition": 1,
        "tags": ["sector-13", "computed", "resonance", "consciousness"],
    },
    {
        "slug": "antenna-coupling-1space",
        "title": "Antenna Coupling to 1 Space",
        "definition_md": (
            "Information-theoretic upper bound on brain-to-1-Space coupling. A 38,000-neuron network "
            "has ~10^15 binary degrees of freedom. The universe (holographic bound) has ~10^124 bits. "
            "Coupling fraction: ~10^-108. Impedance matching at the gamma resonance is exact "
            "(by construction — this is the resonance tautology made explicit)."
        ),
        "equations_md": "eta = D_sub / D_total ~ 10^-108\nD_sub = N_neurons * N_dimers * log2(2)\nD_total = S_holo ~ 10^124 bits\nZ_mismatch = |tau_brain - tau_grav|/tau_brain ~ 0.002",
        "edition": 1,
        "tags": ["sector-13", "model-dependent", "antenna", "information-theory"],
    },
    {
        "slug": "structural-shielding-topology",
        "title": "Structural Shielding and Topology",
        "definition_md": (
            "Speculative proposal: the shielding mechanism for consciousness is not physical "
            "(blocking water molecules) but structural — the microtubule lattice creates a collective "
            "topology where pattern-level information survives thermal noise. Analogies: impedance "
            "matching, redundancy, topological protection. Our own computations show topology does NOT "
            "help for uncorrelated thermal noise. Correlated noise could change this, but no mechanism "
            "is known."
        ),
        "equations_md": "Uncorrelated noise: topology HURTS (ratio 0.70x for N=13)\nCorrelated noise: potentially protective (uncomputed)\nRequired mechanism: unknown",
        "edition": 1,
        "tags": ["sector-13", "speculative", "topology", "shielding"],
    },
    {
        "slug": "sector-13-falsifiability",
        "title": "Sector 13 Falsifiability",
        "definition_md": (
            "Seven kill conditions for Sector 13: (1) bulk-like water in MT channels, "
            "(2) no lattice topological protection, (3) no network significance of 38K neurons, "
            "(4) gamma frequency uncorrelated with tubulin mass, (5) anesthetics don't bind MT, "
            "(6) consciousness survives MT disruption, (7) mutual info decays at local rate. "
            "Five experimental predictions with specific numerical values."
        ),
        "equations_md": "Kill conditions: 7 (all testable)\nPredictions: 5 (with numerical values)\nAdversarial summary: 7 computed, 4 model-dependent, 5 speculative\nVerdict: thermal wall NOT breached",
        "edition": 1,
        "tags": ["sector-13", "falsifiability", "kill-conditions", "adversarial"],
    },
]
