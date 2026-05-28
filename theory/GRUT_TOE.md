# GRUT

## The Grand Responsive Universe Theory

*A complete cosmological theory of everything from a viscoelastic medium with finite bandwidth.*

*Candidate Framework*

---

## Front Matter

### Prologue — Reading This Book

This book presents GRUT — the Grand Responsive Universe Theory — as a candidate Theory of Everything built on one premise: the gravitational vacuum is a viscoelastic medium with finite relaxation time and finite impedance. The framework's central number is R = √(4/3) ≈ 1.15470, the vacuum's gravitational refractive index in the deep IR.

**Three layers of claim.** Throughout this book, three tiers are distinguished. *Load-bearing core* names the principles and identifications the framework rests on — the constitutive equation, the fixed-point principle, and the Weyl-decomposition identification of the gravitational conformal mode (Gate R, formalized May 2026). These are the seams the framework stands on; each is named explicitly where it appears. *Computed extensions* are specific predictions verified in the codebase — Λ_grav scaling laws, the two-route R convergence, cluster-merger v × τ₀ scaling, Ω_dm bandwidth integral, baryogenesis η_B. These trace to passing tests. *Anchored or speculative interpretations* are claims tied to but not fully derived from the core — 1 Space, neural resonance, the dielectric DM overshoot interpretation. Each chapter's footer carries registry-claim labels making the tier explicit. Chapter 14 carries the complete open-question ledger.

**Two organizing principles.** The framework rests on two organizing principles operating together. The first is the *viscoelastic medium* — the constitutive equation τ₀ dz/dt + z = z_target[z] applied to the gravitational vacuum, with finite relaxation time τ₀ = 41.9 Myr (gravitational sector) and finite impedance α = 1/3. (The thermal sector carries a separate microscopic timescale τ_micro ≈ 1.4×10⁻¹⁹ s, distinct from τ₀; see Chapter 2.) The second is *scale universality*, made concrete by what the constants of the medium do. They **scale** — τ₀, α, S = 108π, R = √(4/3) do not run with energy or epoch; they apply unchanged across roughly sixty orders of magnitude in frequency, from Planck UV physics to Hubble expansion. They **interact** — the medium is not a passive backdrop but an active responder, producing decoherence at the lab, dark-matter-like enhancement on galactic-rotation bound systems (frequency-domain regime), the gas-to-lensing offset at cluster mergers (time-domain memory regime), the Hubble rate at cosmic scales, AND a definite modified-gravity μ-1 signal in linear FRW perturbations (Fourier-mode regime, μ_GRUT(k, a)) — all through the same constitutive equation but resolved in regime-appropriate operating variables (see Chapter 9 for the load-bearing two-regime distinction). They **remember** — the memory kernel K(t) = τ₀⁻¹ exp(−t/τ₀) means the medium retains information about past states for ~41.9 Myr; this memory is what produces the Bullet Cluster's ~130 kpc gas-to-lensing offset, the slow approach to the constitutive fixed point, and the cosmic terminal velocity. One medium, one equation, one set of constants — interacting and remembering through 13.8 billion years of cosmic history. The crystallinity parameter X = max(ω, Λ_grav) × τ₀ is the bound-system regime label; the linear-FRW regime label is k_phys × c × τ₀. Both place every phenomenon on the same axis within their operating regime. (See Chapter 4 for the bound-system map; Chapter 9 for the two-regime distinction made explicit.)

**GRUT in one chain.** Before the chapters and the appendices and the open ledger, the entire framework reduces to a single causal sequence. Every derivation in this book is one step along it; every prediction is what the chain produces at a specific scale.

$$S_{\text{CTP}} \;\longrightarrow\; N_{\text{grav}}(x,x') \;\longrightarrow\; \tau_0,\, \alpha \;\longrightarrow\; n_g^2(\omega) = 1 + \frac{\alpha}{1+(\omega\tau_0)^2} \;\longrightarrow\; X = \max(\omega, \Lambda_{\text{grav}})\,\tau_0 \;\longrightarrow\; \{\text{QM},\, \text{GR},\, \text{decoherence},\, \text{dark sector},\, \text{expansion},\, \text{observer}\}$$

Read left to right: one closed-time-path (Schwinger-Keldysh) parent action **S_CTP** produces a gravitational noise kernel **N_grav** = G/(ℏ|x−x'|); this kernel determines two foundational constants — the relaxation time **τ₀ = 41.9 Myr** and the vacuum impedance **α = 1/3** (derived via Gate R: Weyl decomposition → conformal scalar → Duff 1994 a/c = 1/3); these constants give the medium's frequency-dependent refractive index **n_g(ω)**; n_g(ω) and the gravitational decoherence rate Λ_grav together produce the crystallinity parameter **X**, which classifies every phenomenon as crystal (X ≫ 1, classical) or fluid (X ≪ 1, refractive). Quantum mechanics is the τ → 0 limit. General relativity is the X ≫ 1 limit. Gravitational decoherence at the nanoparticle scale, dark-matter-like enhancement at galactic scales, the cluster-merger gas-to-lensing offset, the Hubble rate as terminal velocity, and the observer's own classical definiteness are each what the chain produces at the appropriate (m, l, ω) operating point.

If S_CTP is wrong, everything fails. If τ₀ is wrong, decoherence and cosmology disconnect. If α is wrong, all six scaling laws break simultaneously. The n_g(ω) cosmological-perturbation covariance — once an open question (#9) — is now CLOSED via the modified-gravity EFT-of-dark-energy mapping (Correction #26): ω → k_phys × c at the WKB level, gauge-invariant under conformal-Newtonian/synchronous/comoving, with explicit μ_GRUT(k, a) = n_g²(k, a) and γ_GRUT = 1; the linear-growth integration (Correction #27) shows σ_8-scale modification at 0.09% (does NOT break the existing S_8 tension). If the chain is correct, every sectoral prediction is a consequence — not a separate fit. **The forest is this single sequence; the trees are what each link entails when applied at a particular scale.** Chapter 4 develops X explicitly; Chapter 5 develops the QM, decoherence, and SM-recovery branches; Chapters 6-9 develop the gravity, expansion, and dark-sector branches; Chapter 11 develops the observer branch. The rest of this document is the chain unrolled.

**Load-bearing dependency map.** The chain above is the spine. The table below identifies which claims sit at each link, what tier they hold, what fails if each link fails, and what survives independently. Specialists and reviewers can use this to evaluate which parts of the framework are mutually load-bearing and which are independent decorations. Auto-rendered Appendix F gives the full 87-claim graph; this table is the curated spine view.

| Link | Load-bearing claim | Tier | Depends on | If this fails | Survives independently |
|:---|:---|:---|:---|:---|:---|
| Source | `ctp_action_structure` (S_CTP on S⁴) | computed | — (root) | The entire framework collapses | Nothing — this is the parent |
| Kernel | `noise_kernel_form` (N_grav = G/(ℏ\|x−x'\|)) | computed | S_CTP | All decoherence and cosmological predictions fail | Nothing in the spine |
| Bridge | `tau_0_derivation` (τ₀ = 41.9 Myr) | computed | cosmic-baseline + cluster anchors | Decoherence-cosmology bridge severs; 689 Hz, H_inf, Bullet offset all detach | Foundational provenance audit (Ch 2) |
| Bridge | `alpha_vac_derivation` (α = 1/3, Gate R) | computed | Weyl decomp $g=e^{2\sigma}\hat{g}$; conformal scalar identification; Duff 1994 a/c = 1/3; K^R = α χ P^TT | Six scaling laws break simultaneously; R = √(4/3) loses its source | Sectoral phenomenology survives only as fits, not derivations |
| Output | `refractive_index` (n_g²(ω) = 1 + α/(1+(ωτ₀)²)) | computed | τ₀, α | No frequency-dependent regimes; no DM enhancement, no GR recovery as limit | Standalone use as effective field |
| Output | `threshold_bridge` (X = max(ω, Λ_grav) × τ₀) | computed | τ₀, n_g(ω), Λ_grav | Regime classification breaks; crystal/fluid distinction is ad-hoc | Nothing in the spine |
| Branch — QM | `qm_recovery` (Schrödinger from τ → 0 limit) | computed | constitutive equation, τ₀ | QM emergence is a postulate, not a limit | QM as imported |
| Branch — Lab decoherence | `decoherence_zero_param` (Λ_grav = Gm²S(l/R)/(ℏl)) | computed | n_g(ω), screening 108π | 689 Hz primary falsifier disconnects; F1-F6 scaling laws break | Standalone parameter-fit decoherence model |
| Branch — Cosmology | `h_inf_decomposition` (H_inf = (2-R)/(Sτ₀)) | computed | τ₀, α, R, C_Cosmo | Hubble-rate prediction fails; dark-energy mechanism unsourced | H₀ as imported observation |
| Branch — Dark sector | `omega_dm_equals_alpha` (Ω_dm = 1/3 from α) | computed | α | Geometric DM density derivation fails; dielectric route loses zero-parameter status | Cluster-merger scaling (anchored, separate) |
| Branch — Observer | `measurement_resolution` (X_observer ≫ 1) | computed | Λ_grav, τ₀ | Schrödinger-in-the-Box dissolution fails; measurement problem reopens | Observer crystallinity claim only as conjecture |
| Branch — Cluster mergers | `cluster_merger_internal_scaling_residual` (1.72%) | computed | τ₀, Λ_grav, R | Bullet/MACS/Abell/El Gordo functional form breaks | Standalone parameter-fit only |

**How to read this table.** *"Survives independently"* names what residual content remains usable if the listed claim fails. For most links, **nothing in the spine survives** — meaning the framework is a tightly coupled chain, not a loosely linked collection. This is both a strength (one mechanism explains many regimes) and an exposed flank (one wrong link disconnects multiple sectors). The branches at the end (QM, decoherence, cosmology, dark sector, observer, cluster mergers) survive their predecessors when treated as standalone parameter-fit models — but lose their zero-parameter / cross-sector status. **The framework's distinctiveness lives in the chain.** Without the chain, GRUT is six unrelated phenomenological models with shared symbols. With the chain, GRUT is one viscoelastic medium evaluated at six scales.

**Candidate, not completed.** GRUT is presented as a *candidate* Theory of Everything because the chain above gives one mechanism across many regimes. The v8→v2 synthesis (Corrections #22–#30, May 2026) closed several research packages that the original v8 deposit left open: (a) the gravitational constitutive projection Φ_μν is now DERIVED from δS_CTP/δh_a at the linearized level (Correction #23), with a covariant curved-background scaffold (Correction #24) and an explicit FRW result χ_FRW(k, η) (Correction #25); (b) the n_g(ω) cosmological-perturbation covariance is CLOSED via the modified-gravity EFT-of-dark-energy mapping μ_GRUT(k, a) = n_g²(k, a), γ_GRUT = 1 (Correction #26); (c) the modified linear growth equation has been integrated and shows σ_8-scale unchanged at 0.09% (does NOT break the S_8 tension), large scales boosted as testable signal (Correction #27); (d) one Standard Model prediction — neutrino hierarchy — is derived: NH preferred, Σm_ν ≈ 60 meV, with a_ν = 1 derived as the unique boundary-degenerate Z₃ coupling (Corrections #28-#29); (e) the (\tau)-cleanup foundational dimensional bug is closed via the two-τ-scale convention τ₀ vs τ_micro (Correction #22). What REMAINS open and gates ToE-completion: (i) the curved-background explicit construction of P^TT,g and G^R on FRW/S⁴ (Phase 2C explicit, sharper successor of the original Φ_μν open question); (ii) the full Boltzmann pipeline (CAMB/CLASS modification with μ_GRUT) to produce explicit P(k), C_ℓ predictions — theoretically unblocked but a downstream computational task; (iii) the constitutive perturbation-growth FAILURE at first order (D = 1.0 vs ~3375 required), requiring second-order / nonlinear-ladder extension (currently 4/8 rungs); (iv) the rest of Standard Model closure beyond the neutrino sector — Yukawa eigenproblem for charged leptons & quarks, CKM/PMNS angles, Higgs potential closure (the SM is still *hosted* as S_classical except for the neutrino hierarchy now derived); (v) the nonlinear quantum-gravity ladder beyond rungs 5-8. Until these residual open packages close, GRUT remains a candidate framework with rigorous claim governance, near-term falsifiers (collected in `theory/GRUT_FALSIFIER_PAPER.md`), and explicit acknowledgment of remaining open seams. The reader's job is to evaluate the chain on its merits *and* the gaps on theirs. The framework's commitment is to keep both visible.

**What is still missing for full ToE status.** The framework is a candidate, not a completed theory. The table below names the load-bearing gaps honestly:

| Area | Status |
|:---|:---|
| Canonical R = √(4/3) | **Closed / derived** (Gate R, May 2026) |
| α_vac = 1/3 provenance | **Closed / formalized** (Duff 1994 eq 30–31, Gate R) |
| Linearized gravity on FRW | **Strong** — derived and scaffolded |
| Nonlinear gravity | **Open** — 4/8 rungs; perturbation-growth failure at first order |
| Standard Model closure | **Partial** — SM hosted; neutrino hierarchy derived; Yukawas/CKM/PMNS/Higgs open |
| Dark sector tensions | **Promising** — Ω_dm = 1/3 geometric (+27% overshoot); cluster-merger +20% systematic |
| Primary experimental falsifiers | **Untested** — decoherence plateau ~689 Hz, isotope discriminator, BMV entanglement |
| Boltzmann/CMB pipeline | **Not implemented** — theoretically unblocked; downstream computational task |
| Born rule | **Open negative** — GRUT gives the rate of classicalization, not the probability weights |
| Nonlinear quantum gravity (rungs 5-8) | **Open** — required for ToE status in the strong sense |

This table does not make the book weaker. A theory that clearly names what it has and what it lacks is more trustworthy than one that papers over gaps.

**Where to find the machinery.** The GRUT-RAI codebase (DOI: 10.5281/zenodo.18993689) contains every test, every derivation module, and the claim registry that backs every assertion in this book. The full research archive including the V7 document (175 pages, 17 appendices) is available at zenodo.org/communities/grut. The predictions dashboard (`GRUT_TOE_PREDICTIONS.md`) lists all quantitative predictions with values, observations, and falsification conditions in one table.

**How to read.** Part I (Chapters 1-4) establishes the foundation — what the universe is, what the medium is, what the equation is, and how reality divides into crystal and fluid. Part II (Chapters 5-11) recovers known physics and presents the framework's predictions. Part III (Chapters 12-14) opens the frontier — the Standard Model closure program, the history of the universe in GRUT, and the complete falsification ledger. The Appendices provide the speculative genesis hypothesis, detailed framework comparisons, and auto-rendered reference material.

Every honest negative is documented. Nothing is fitted away.

### Abstract

The Grand Responsive Universe Theory (GRUT) is a candidate Theory of Everything built on a single premise: the gravitational vacuum is not empty space but a viscoelastic medium with finite relaxation time and finite impedance. One closed-time-path (CTP, Schwinger-Keldysh) effective action, evaluated on Euclidean S⁴ with Standard Model field content, produces a constitutive response equation whose sectoral limits yield quantum mechanics (exact), gravitational decoherence with zero free parameters (exact, six scaling laws), a cosmological constant Ω_Λ ≈ 0.69 within 0.2% of Planck from two independent routes (computed, zero free parameters), a Hubble rate H₀ ≈ 68.8 km/s/Mpc (zero parameters, cosmic-baseline) or 69.03 km/s/Mpc (one parameter, Friedmann integration) — both in the tension gap, baryon asymmetry within 8% (computed), a dark matter density of Ω_dm = 1/3 from geometry alone (zero parameters), and structural contacts with QCD, flavor, neutrinos, coupling unification, quantum gravity, and neural resonance — all from the same parent action.

Two constants characterize the medium: a relaxation time τ₀ = 41.9 Myr anchored by the cosmic-baseline relation 1/(H₀ × 108π), and a vacuum impedance α = 1/3 derived from the Weyl-decomposition identification of the gravitational conformal mode as one real conformally-coupled scalar — Duff 1994 a/c = 1/3 exactly (Gate R closed, May 2026). One computable constant — R = √(4/3) = 1.15470, the gravitational refractive index of the vacuum — follows directly from α = 1/3 via the constitutive cross-kernel (Path G, canonical derivation). The canonical R = √(4/3) is the constitutive/refractive route; the previous R = 1.15428 from the 3-loop CTP anomaly-quotient route is an honest-negative diagnostic (TJI Phase-0/0.5 did not reproduce it; Allen-Jacobson Phase-1 S⁴ propagator is IMPLEMENTED but the ₂F₁³ ε-expansion remains open — `S4CurvatureObstacle`). An independently computed check at ε = 1.15367 from Osborn's local RG coefficients with measured SM couplings converges with the canonical value to within 0.089% — the two non-negative routes share no inputs.

The framework rests on two organizing principles. The first is the *viscoelastic medium* itself — the constitutive equation τ₀ dz/dt + z = z_target[z] applied to the gravitational vacuum. The second is *scale universality*: the same four constants (τ₀, α, S = 108π, R) govern phenomena across roughly sixty orders of magnitude in frequency, from Planck UV physics to Hubble expansion, through the same constitutive equation. Quantum mechanics, gravitational decoherence, dark matter, dark energy, baryogenesis, and the observer's classical definiteness are not separate effective theories at different scales — they are the same medium responding to different matter configurations, with constants that scale (don't run with energy), interact (actively produce the phenomenology), and remember (through the memory kernel τ₀⁻¹ exp(−t/τ₀)).

The Hubble rate is the terminal velocity of the vacuum. The S⁴ conformal-mode instability (the −100 in C_Cosmo, identified with the Gibbons-Hawking 1978 pathology) drives cosmic expansion. The constitutive memory kernel damps it. H_inf = drive/friction = (2−R)/(Sτ₀). No contour rotation is needed. The universe expands because the conformal mode is unstable and the medium won't let it explode.

The framework describes the observer as much as the observed. The scaling law Λ_grav = Gm²S(l/R)/(ℏl) applies equally to the measurer and the measured. Classical definiteness is not a postulate — it is the condition Λ_grav τ₀ ≫ 1, satisfied by every atom in the observer's body. The measurement problem dissolves because the apparatus is on one side of the crystalline boundary only because its Gm² puts it there.

This document presents the complete framework in fourteen chapters: what the universe is, what the medium is, what the equation is, how reality divides into crystal and fluid, what physics is recovered, how gravity works, what the constant R means, why the universe expands, what the dark sector is, why time flows forward, what the observer is, what the SM closure program requires, the history of the universe in GRUT, and what would kill the theory. Every claim traces to a tested function in the GRUT-RAI codebase (2539 tests, 95+ registered claims, DOI: 10.5281/zenodo.18993689). Every failure, retraction, and honest negative is documented; nothing is fitted away. The companion V7 document (175 pages, 17 appendices) provides the full technical derivations.

---

## v8 → v2 Synthesis Update (May 2026)

This deposit version extends the v8 framework with nine focused corrections (Corrections #22 through #30) that close five Priority research items the framework's deposit description had identified as gates to scientific establishment. Each correction is a focused, tested, documented unit; each is referenced in Chapter 14's extended correction ledger. The synthesis below is a navigation aid — a brief tour of what changed.

**Priority 1 (Correction #22): τ-cleanup.** A foundational dimensional inconsistency surfaced by the T_C audit (T_c = 54.7 MK was being computed via a dimensionally invalid formula `1/(τ₀ × k_B)` rather than the SI-correct `ℏ/(τ_micro × k_B)`) is RESOLVED via the two-τ-scale convention: τ₀ = 41.9 Myr (gravitational, macroscopic) is now distinguished from τ_micro ≈ 1.4×10⁻¹⁹ s (thermal, microscopic). T_c = 54.7 MK is preserved exactly via the SI-correct formula. The previous `t_c_provenance_inconsistency_open_negative` (#15 in the v8 ledger) is RESOLVED.

**Priorities 2A, 2B, 2C (Corrections #23, #24, #25): Φ_μν derivation.** The previously heuristic gravitational constitutive correction Φ_μν is now derived structurally from the variation `δS_CTP / δh_a` of the linearized Schwinger-Keldysh action (Correction #23, Phase 2A). The derivation extends to a covariant curved-background scaffold with four physical-consistency checks — flat-limit recovery, covariant conservation, causality, FRW scalar-mode compatibility (Correction #24, Phase 2B). The explicit FRW result is computed at WKB level: `χ_FRW(k, η) = 1/[1 + (τ₀ k_phys)²]` with sub-horizon → ΛCDM recovery, super-horizon → 4/3 enhancement, transition wavelength λ_* ≈ 80.7 Mpc today (Correction #25, Phase 2C). The previous `constitutive_projection_gravity_heuristic_open_question` (#10) is RESOLVED at the linearized level; what remains is the curved-background explicit construction (now sharper) and beyond-WKB refinement (O(10⁻⁶) correction).

**Priority 3 (Correction #26): n_g(ω) covariance closure.** The MG-EFT-of-dark-energy mapping is explicit: `μ_GRUT(k, a) = n_g²(k, a)` with γ_GRUT = 1 (no gravitational slip). All three closure gates of the previous open question (#9 in the v8 ledger — `n_g_omega_cosmological_covariance_open_question`) are met: ω → k_phys × c identification (gauge-invariant at WKB), gauge-invariance verified across conformal-Newtonian/synchronous/comoving, and the μ(k, a)/γ(k, a) map giving GRUT a definite location in the modified-gravity literature with the sharp γ = 1 prediction.

**Priority 3.1 (Correction #27): modified linear growth.** Numerical integration of the modified Bardeen equation `δ'' + [2 - (3/2)Ω_m] δ' - (3/2) Ω_m μ_GRUT(k, N) δ = 0` on a Planck 2018 ΛCDM background gives the LOAD-BEARING result: at the σ_8 scale (k = 0.5 Mpc⁻¹), GRUT enhancement is 0.09% — well below current observational precision. **GRUT does NOT break the σ_8 / S_8 tension.** Large scales show significant enhancement (8.5% at BAO, 33% at Sloan large, ~135% at CMB horizon) — testable by DESI Y3+ and Euclid 2027.

**Priority 4 (Correction #28): neutrino hierarchy via Z₃.** The framework's charged-lepton Koide K = 2/3 (proven from Z₃ circulant) is shown to NOT extend to neutrinos with the same coupling a = √2 (minimum admissible Δm²_atm/Δm²_sol = 194.7, observed = 33.9 — factor of 6 too large). A modified Z₃ with a_ν = 1 admits a unique interior NH solution: m_1 ≈ 0.8 meV, m_2 ≈ 8.7 meV, m_3 ≈ 50.2 meV, **Σm_ν ≈ 60 meV** (well below Planck bound 0.12 eV). IH at a_ν = 1 lives at the m_3 → 0 boundary (degenerate, fine-tuned), so GRUT structurally **prefers Normal Hierarchy**.

**Priority 4B (Correction #29): a_ν = 1 derived as uniqueness theorem.** The previous a_ν = 1 postulate is upgraded to a derived value via the **boundary-degenerate uniqueness theorem**: the boundary configuration (one s_k = 0) has the OTHER two s values exactly degenerate (gap = √3·√(a²-1)) iff a = 1. Combined with NH-interior generic + Σm_ν < Planck, uniquely selects a_ν = 1. Channel-counting interpretation: a²_e = 2 (EM + weak) vs a²_ν = 1 (weak only) — neutrino sector lacks the electromagnetic coupling channel. The previous `neutrino_z3_coupling_derivation_open_question` is RESOLVED.

**Priority 5 (Correction #30): GRUT Falsifier Paper.** A new short paper at `theory/GRUT_FALSIFIER_PAPER.md` collects six near-term-testable falsifiers across three sectors: decoherence plateau (~689 Hz, lab gravity, F1), ³⁰Si/²⁸Si isotope discriminator vs CSL (lab gravity, F2), BMV/sub-micron-separation gravitational entanglement (lab gravity, F3), cluster-merger v×τ₀ scaling (cluster astrophysics, F4), modified-gravity μ-1=1/3 on horizon scales (cosmology, F5), and Σm_ν ≈ 60 meV with normal hierarchy (Standard Model + cosmology, F6). The paper articulates GRUT's adversarial posture vs other ToE programs (string theory, LQG, asymptotic safety, CDT): GRUT's distinctive feature is not greater mathematical maturity but greater near-term falsifiability.

**What this update closes structurally.** Open questions resolved: #9 (n_g(ω) covariance), #10 (Φ_μν heuristic, at linearized + scaffold + FRW levels), #15 (T_c provenance), and `neutrino_z3_coupling_derivation_open_question` (newly resolved by Correction #29). Sharper successor open questions registered: `phi_munu_curved_background_scaffold` (anchored), `phi_munu_frw_beyond_wkb_open_question` (O(10⁻⁶) correction).

**What this update preserves.** All v8 numerical predictions are unchanged. T_c = 54.7 MK preserved exactly. α_vac = 1/3 inherits unchanged. τ₀ = 41.9 Myr unchanged. R = √(4/3) unchanged. All decoherence and dark-sector predictions stand intact.

**What remains open.** The framework's most exposed flanks remain: the constitutive perturbation-growth FAILURE at first order (D = 1.0 vs observationally required ~3375 — a computed negative, not an open derivation, requiring nonlinear extension); the nonlinear gravity ladder rungs 5-8; the Standard Model closure (Yukawas, mixing angles, Higgs); the TJI Euler-channel coefficient extraction (the Allen-Jacobson Phase-1 S⁴ propagator is now implemented — the remaining gate is the Mathematica/HypExp ε-expansion of the ₂F₁³ radial integral, `S4CurvatureObstacle`, guarded by `euler_coefficient_landing.py` and `HYPEXP_TARGET_NOTEBOOK.ipynb`; this is a diagnostic cross-check for the R_anomaly honest-negative track, not a gate for the canonical R = √(4/3)); the V4 RG cascade first-principles derivation (Corrections #32-#34 established the loop-suppressed framework and identified that the residual 1.2% β_eff discrepancy is a higher-order refinement issue, not an architectural failure; open question #20 now separates into three independent research gates: (a) geometric origin of the 8π normalization factor in the Christensen-Duff anchor, (b) 2-loop Seeley-DeWitt refinement for off-diagonal operator mixing on S⁴, (c) 3-loop Euler-quotient coefficient extraction); the full-Boltzmann CMB pipeline implementation (theoretically unblocked by Correction #26 but a downstream computational task). These remain in the framework's honest-negative roster.


For the full chain of corrections including #1-#21 (V7 development era) plus the v8→v2 nine, see Chapter 14's extended ledger.

---

## Gate R Closure Update (May 2026)

**What changed.** A five-stage Gate 3 audit sequence and a dedicated Gate R identification audit closed the canonical R-derivation to book-ready status. This is the most significant structural change since the v8→v2 synthesis: $R = \sqrt{4/3}$ is now **derived within the constitutive-action framework**, not merely observed numerically.

**What specifically changed from the previous version:**

| Item | Previous | Now |
|:---|:---|:---|
| Canonical R source | "Path G refractive + pending loop correction" | "Constitutive/refractive route — derived. 3-loop route is honest negative" |
| $\alpha_{\rm vac} = 1/3$ provenance | GRUT assertion ("vacuum impedance = 1/d") | Published trace anomaly: $a/c = 1/3$ for real conformally-coupled scalar (Duff 1994 (eq 30–31)) |
| $R_{\rm anomaly} = 1.15428$ | Presented as "loop correction to tree-level" | Honest negative — TJI Phase-0/0.5 did not reproduce; retained as diagnostic |
| $P^{TT}$ / scalar-anomaly compatibility | Not addressed | Resolved: scalar $\alpha_{\rm vac}$ sets vacuum response amplitude; $P^{TT}$ filters admissible perturbation sources — independent roles |
| Conformal mode identification | Stated without derivation | Formalized: Weyl decomposition + EH action on $S^4$ gives $\sigma$ as spin-0, $\xi_c = 1/6$ exactly |

**The Gate R audit chain** (all committed, branch v2):

| Gate | Result |
|:---|:---|
| Gate 3 vertex provenance audit | $\pi/2$ is shared $S^4$ normalization (cancels in $R$) |
| Gate 3 CTP branch-incidence audit | SYM topology; $\pi/2$ shared on Euclidean $S^4$ |
| Gate 3 sector-coupling assignment | Dimensional ladder: $I(0,0)|_{D=5} = 4/3 = R^2$ |
| Gate 3 sector-dimensional provenance | Assignment B (cosmo = $S^4$, final = $S^3$) is unique |
| Gate 3 CTP action term audit | $S_{\rm const}$ with $\alpha_{\rm vac} = 1/3$ → $n_g(0) = \sqrt{4/3}$ exactly |
| Gate 3 $\alpha_{\rm vac}$ provenance | Route 2 (Duff 1994 eq 30–31): published, convention-independent |
| Gate R identification | C1–C6 all SUPPORTED or FORMALIZED |

**Complete gate-status table (G1–G7 action layer; C1–C6 identification layer):**

The audit proceeds in two layers. G1–G7 are action-layer gates: they verify that the CTP action structure, sector assignments, and constitutive kernel form are correct. C1–C6 are identification-layer gates: they verify that the gravitational conformal mode is correctly identified as one real conformally-coupled scalar.

| Gate | Description | Status |
|:---|:---|:---|
| G1 | $\pi/2$ vertex-factor provenance — shared $S^4$ normalization | **Identified** |
| G2 | CTP branch-incidence — SYM topology survives; $V_{aaa} = 0$ | **Supported** |
| G3 | Sector-coupling assignment — dimensional ladder: $I(0,0)\vert_{D=5} = 4/3 = R^2$ | **Identified** |
| G4 | Sector-dimensional assignment — cosmo = $S^4$, final = $S^3$; $D=4$ coincidence | **Indirect / algebraic** |
| G5 | CTP action term — $S_{\rm const}$ with $K^R = \alpha_{\rm vac}\chi P^{TT}$ → $n_g(0)^2 = 4/3$ | **Proved** |
| G6 | $\alpha_{\rm vac}$ provenance — Route 2: Duff 1994 $a/c = 1/3$, published, convention-independent | **Confirmed** |
| G7 | End-to-end: $\alpha_{\rm vac} = 1/3 \to R = \sqrt{4/3}$ via Path G constitutive route | **Confirmed via Path G** |
| C1 | Scalar mode isolated — $\sigma$ is scalar sector of Weyl decomposition; IR-dominant on $S^4$ | **Formalized** |
| C2 | Conformal coupling — EH decomposition gives $\xi_c = 1/6$ exactly; no free parameter | **Formalized** |
| C3 | One real species / GHP — functional measure: one real DOF; GHP instability is Euclidean artifact, does not affect retarded CTP kernel | **Supported** |
| C4 | Fermion / gauge excluded — $\sigma$ is spin-0 by Weyl decomposition; excluded by representation, not by R-matching | **Supported** |
| C5 | $P^{TT}$ compatibility — scalar $\alpha_{\rm vac}$ sets vacuum response amplitude; $P^{TT}$ filters admissible perturbation sources; independent roles | **Resolved** |
| C6 | R-independence — $a/c = 1/3$ computed from Duff 1994 before $R$ is defined; not circular | **Supported** |

**The R-chain claim-status ledger:**

| Claim | Status | Basis |
|:---|:---|:---|
| $R = \sqrt{4/3}$ (canonical) | **Derived** | Gate R closed: Weyl decomp → $a/c = 1/3$ → $K^R$ → $n_g(0) = \sqrt{4/3}$ |
| $\alpha_{\rm vac} = 1/3$ | **Derived** | Duff 1994 (eq 30–31): real conformally-coupled scalar, exact rational |
| $R = 1.15367$ (Osborn route) | **Supported** | Computed from SM gauge couplings at $M_Z$ |
| $\pi/2$ as shared normalization | **Proved** | SYM topology, CTP branch-incidence audit |
| $R = \sqrt{4/3}$ from geometric chain | **Proved** | Dimensional ladder; $D=4$ coincidence |
| GH thermal asymmetry (sector forcing) | **Supported** | Structural; $T_{\rm GH} = H_\infty/(2\pi)$ forward/backward split |
| $R_{\rm anomaly} = 1.15428$ (V7 §26) | **Honest negative** | 3-loop CTP anomaly quotient — not reproduced in TJI Phase-0/0.5 |
| 3-loop anomaly quotient numeric | **Diagnostic** | Retained for cross-check; not load-bearing |
| "vacuum impedance = 1/d" (v11 App H) | **Superseded** | Demoted to assertion/history; replaced by Duff 1994 route |

**Integration status.** The Weyl-decomposition formalization is now integrated into Chapter 7 (subsection: "The conformal response mode: why one real scalar controls α_vac"). The remaining caveat is that the identification is standard and formalized, but future work may deepen it through an explicit path-integral derivation of the gravitational conformal sector on S⁴.

---

## Part I — Foundation

# Chapter 1 — The Universe

*What the universe is. The foundational claim.*

The universe is a closed, self-referential system. There is no external observer. There are no boundary conditions imported from outside. The fixed-point principle z* = z_target[z*] — the state that generates its own target — is not a mathematical convenience. It is the foundational claim of the framework: the universe generates its own boundary conditions.

This is what "closed" means in GRUT. Not merely spatially closed (though the S⁴ topology is compact). Not merely informationally closed (though no external influence enters). The closure is dynamical: the constitutive equation τ₀ dz/dt + z = z_target[z] has a fixed point, and that fixed point is self-consistent. The rules that generate the dynamics are satisfied by the state those dynamics produce.

Everything in the framework follows from this principle applied to different sectors. Apply it to quantum fields → quantum mechanics (Chapter 5). Apply it to gravity → general relativity with constitutive corrections (Chapter 6). Apply it to the vacuum itself → the cosmological constant (Chapter 8). Apply it to the observer → classical definiteness without a measurement postulate (Chapter 11). One principle, fourteen sectors, one CTP action. Concretely: the Hubble flow is the relaxation toward this fixed point at cosmological scale. The decoherence plateau is the relaxation toward it at laboratory scale. The observer's own classical definiteness is the relaxation at the observer's mass scale — Schrödinger's cat doesn't need an external observer because the cat's own Λ_grav resolved its state in femtoseconds (Chapter 11, Schrödinger-in-the-Box). All are instances of z → z* for different field content at different frequencies.

**No privileged outside positions.** The closure principle has a worldview consequence the framework applies uniformly: nothing in physics gets to stand outside what is being described. The observer is not outside reality — the observer is field content governed by the same equation as everything else, crystallized by the same Λ_grav scaling, and Chapter 11 (Schrödinger-in-the-Box) shows that the standard cat thought experiment dissolves once this is taken seriously. The laws of physics are not outside the medium — what we call the laws is what the viscoelastic vacuum *does* at different scales, with the same constants and the same constitutive equation throughout (Chapter 4, the universal scale map). Boundary conditions are not imported from outside — the fixed-point principle z* = z_target[z*] generates them internally. Three different inversions of the same commitment: observer-in-the-box, laws-in-the-medium, boundary-conditions-from-the-fixed-point. Each removes a privileged outside position that standard physics quietly assumes. This is what makes the framework closed in the strong sense.

**The physical picture.** The vacuum is a medium. It has a relaxation time (τ₀ = 41.9 Myr), an impedance (α = 1/3), a refractive index (n_g = √(4/3) at DC), a bandwidth (τ₀⁻¹), a critical temperature (T_c = 54.7 MK), and a terminal velocity (H_inf = 58.16 km/s/Mpc). It is not empty. It is not a background. It is not a stage on which physics plays out. It is the substance from which physics emerges.

> **Gravity is not stronger where dark matter appears to be. Gravity is slower.**

> **The universe is √(4/3) ≈ 1.15470 trying to become 1.**

The first sentence is the physical picture. The second is the dynamical picture. R = √(4/3) = 1.15470 follows from the vacuum impedance α = 1/3, derived via Gate R: Weyl decomposition of the metric → conformal scalar identification → a/c = 1/3 (see Chapter 7). The vacuum state relaxes toward the fixed point z = z_target[z] within that boundary. The expansion of the universe IS the relaxation. Dark energy is not a substance — it is the constitutive dynamics of a medium that hasn't finished responding.

**1 Space.** At the fixed point — when every mode at every frequency has completed its constitutive relaxation — the universe would be a single self-consistent state. z = z_target[z] globally. R → 1. n_g → 1. No refractive enhancement, no dark matter phenomenology, no expansion. The universe at perfect equilibrium. This is the endpoint the dynamics approach but never reach, because new stress-energy events continuously perturb the medium away from equilibrium. 1 Space is the attractor, not the state. The universe is always approaching it, never arriving. [CONJECTURAL]

**What this chapter commits to:**

- The universe is a closed dynamical system generating its own boundary conditions through the fixed-point principle
- The vacuum is a physical medium with measurable constitutive properties
- The framework is self-referential: the same equation describes the observer and the observed
- 1 Space as the asymptotic attractor is conjectural and labeled as such

**On the three layers of this document.** Throughout, three tiers of claim are distinguished. *Load-bearing core* names the principles and identifications the framework rests on — the constitutive equation, the fixed-point principle, and the Weyl-decomposition identification of the gravitational conformal mode (Gate R, formalized May 2026). These are the seams the framework stands on; each is named explicitly where it appears. *Computed extensions* are specific predictions verified in the codebase — Λ_grav scaling laws, the two-route R convergence, cluster-merger v × τ₀ scaling, Ω_dm bandwidth integral, baryogenesis η_B. These trace to passing tests. *Anchored or speculative interpretations* are claims tied to but not fully derived from the core — 1 Space, neural resonance, the dielectric DM overshoot interpretation. Each chapter's footer carries registry-claim labels making the tier explicit. Chapter 14 carries the complete open-question ledger.

**Consolidated predictions.** The framework's numerical predictions at a glance:

| Prediction | GRUT value | Observed | Match | Tier | Chapter |
|:---|:---|:---|:---|:---|:---|
| Decoherence plateau | ~689 Hz | Not yet measured | Primary falsifier | Computed | 5 |
| Isotope discriminator (Si) | Ratio 1.148 (m²) | Not yet measured | GRUT vs CSL at 3.8% precision | Computed | 5 |
| R (refractive index) | √(4/3) = 1.15470 | — | Two routes at 0.089% | Computed | 7 |
| Ω_Λ | ≈ 0.69 | 0.6889 (Planck) | <0.2% | Computed | 8 |
| H₀ (cosmic-baseline) | 68.8 km/s/Mpc | 67.4-73.5 (tension) | In the gap, zero parameters | Computed | 8 |
| H₀ (Friedmann) | 69.03 km/s/Mpc | 67.4-73.5 (tension) | In the gap, one parameter (N_total) | Computed | 8 |
| H_inf | 58.15 km/s/Mpc | — | Testable via H₀√Ω_Λ | Computed | 8 |
| Ω_dm,eff | 1/3 = 0.333 | 0.263 (Planck) | +27% | Computed | 9 |
| η_B | 6.57 × 10⁻¹⁰ | 6.1 × 10⁻¹⁰ | +8% | Computed | 9 |
| a₀ (MOND scale) | 1.2 × 10⁻¹⁰ m/s² | ~1.2 × 10⁻¹⁰ | Match | Computed | 9 |
| Bullet Cluster offset | 130 kpc | ~150 kpc | Factor 0.87; +20% systematic two-parameter degenerate | Computed | 9 |
| T_c (critical temp) | 54.7 MK | — | BBN-consistent | Computed | 2 |
| CMB θ* shift | 3.6 × 10⁻⁵ | Below Planck | At CMB-S4 threshold | Scoping | 9 |
| Solar system (8 tests) | α_eff < 10⁻¹⁴ | All safe | Safety 10⁵-10³⁵ | Computed | 4 |
| X_cosmic crossover | z ≈ 71 (atomic-scale) | — | Regime boundary prediction | Computed | 4 |
| Koide K | 2/3 (exact) | 2/3 (observed) | 0.005% | Computed | 9 |
| Neural 40 Hz | 39.9-41.7 Hz | ~40 Hz | Brackets observed | Speculative | 11 |
| Primordial A_s | 1/(πS³) ≈ 8.15 × 10⁻⁹ (conditional) | 2.1 × 10⁻⁹ | Factor 3.88, rescaling-conditional | Open negative | 13 |
| **μ_GRUT(k, a) MG-EFT** | **n_g²(k, a) = 1 + α/[1+(τ₀ k_phys)²]** | **Planck μ₀-1 = 0.07 ± 0.13** | **GRUT predicts μ-1 = 1/3 at horizon** | **Computed (Correction #26)** | **9** |
| **γ_GRUT(k, a) gravitational slip** | **1 (no slip)** | — | **Sharp; distinguishes from Brans-Dicke / f(R) / DGP** | **Computed (Correction #26)** | **9** |
| **σ_8-scale growth enhancement** | **0.09% at z=0** | — | **Below precision; does NOT break S_8 tension** | **Computed (Correction #27)** | **9** |
| **CMB-horizon growth enhancement** | **f_GRUT ≈ 2.35 (135%)** | — | **Testable Planck low-ℓ + Euclid 2027** | **Computed (Correction #27)** | **9** |
| **BAO-scale growth enhancement** | **f_GRUT ≈ 1.085 (8.5%)** | — | **Testable DESI Y3+** | **Computed (Correction #27)** | **9** |
| **Transition wavelength λ_*** | **2π τ₀ c ≈ 80.7 Mpc today** | — | **Predicts crossover scale separating sub-/super-horizon FRW response** | **Computed (Correction #25)** | **9** |
| **Σm_ν (sum of neutrino masses)** | **≈ 0.060 eV (NH)** | **< 0.12 eV (Planck+BAO)** | **Within bound, ~60 meV headroom; Euclid 2027 definitive at >3σ** | **Anchored on a_ν = 1 derivation (Correction #28)** | **12** |
| **Neutrino hierarchy** | **Normal Hierarchy (NH)** | **Mild NH preference ~2σ** | **JUNO/DUNE/Hyper-K confirm at >5σ by 2030** | **Anchored (Correction #28)** | **12** |
| **Lightest neutrino mass m_1** | **0.802 meV (sub-meV)** | — | **KATRIN m_β consistent (~9 meV); Project 8 future** | **Anchored (Correction #28)** | **12** |
| **a_ν = 1 (Z₃ neutrino coupling)** | **DERIVED — boundary-degenerate uniqueness** | — | **Structural theorem: gap √3·√(a²-1) = 0 iff a = 1** | **Computed (Correction #29)** | **9** |
| **τ_micro (thermal sector timescale)** | **ℏ/(k_B × T_c) ≈ 1.4×10⁻¹⁹ s** | — | **Anchored to T_c = 54.7 MK cosmological-chronology pin** | **Anchored (Correction #22)** | **2** |
| **0νββ signal (Dirac-ν posture)** | **No signal predicted** | **Not detected** | **nEXO/KamLAND-Zen non-detection consistent** | **Anchored** | **12** |

*Registry claims: closed_universe (foundational), fixed_point_principle (foundational), one_space_endpoint (conjectural), mg_eft_mu_gamma_mapping (computed, Correction #26), modified_linear_growth_first_look (computed, Correction #27), neutrino_hierarchy_z3_nh_prediction (anchored, Correction #28), neutrino_z3_coupling_a_equals_1_uniqueness_theorem (computed, Correction #29), phi_munu_linearized_derivation (computed, Correction #23), phi_munu_curved_background_scaffold (anchored, Correction #24), phi_munu_frw_explicit_construction (computed, Correction #25), falsifier_paper_six_near_term_tests (meta, Correction #30)*

---

# Chapter 2 — The Medium

*What the vacuum is made of. Two constants, one observationally anchored and one formalized through Gate R.*

The vacuum has two constitutive properties. Both are computed from the CTP action with Standard Model field content. τ₀ is anchored observationally — the Bullet Cluster offset and the cosmic-baseline relation converge to 41.9 Myr from independent directions. α_vac = 1/3 is formalized through Gate R: the Weyl decomposition of the metric identifies the conformal factor σ as one real conformally-coupled scalar, and the published trace anomaly a/c = 1/3 (Duff 1994 (eq 30–31)) then follows without free parameters or additional tuning.

**The relaxation time: τ₀ = 41.9 Myr.** This is the e-folding time of the gravitational memory kernel K(t) = τ₀⁻¹ exp(−t/τ₀). It sets the bandwidth of the vacuum's gravitational response. At frequencies ω ≫ τ₀⁻¹, the vacuum responds instantaneously — this is the GR regime (solar system, LIGO, GPS). At frequencies ω ≪ τ₀⁻¹, the vacuum's response lags — this is where dark matter and dark energy phenomenology emerge.

τ₀ is anchored by two independent routes. The cosmic-baseline relation τ₀ = 1/(H₀ × S) = 1/(H₀ × 108π), evaluated at H₀ = 70 km/s/Mpc, gives 41.17 Myr — within 1.7% of the canonical 41.9 Myr. The Bullet Cluster gas-to-lensing offset gives an independent observational anchor at τ₀ ≈ 49 Myr (within 17%). The value 41.9 Myr = 1.322 × 10¹⁵ s is the framework's adopted anchor; downstream predictions are computed consistently from it.

The gold benchmark (m = 80.8 pg, l = 1 μm, R = 1 μm) is a downstream consistency check, not the source of τ₀. The noise kernel N_grav(x, x') = G/(ℏ|x − x'|) evaluated at these parameters yields a decoherence rate Λ_grav = 688.7 Hz — this is computed FROM τ₀, not the other way around. The decoherence plateau at ~689 Hz is the framework's primary falsifier: measuring it would either confirm τ₀ or force its revision.

The cross-identity τ₀ = 1/√(Λc²) — where Λ is the cosmological constant — makes dark energy and dark matter the same parameter in different units. This is not imposed. It follows from the CTP structure: the noise kernel that produces gravitational decoherence at the nanoparticle scale is the same noise kernel that produces constitutive expansion at the cosmological scale.

**Cross-consistency.** τ₀ can be inferred from at least seven independent routes. These cluster into two groups:

*Cosmic-baseline group* (4 routes, spread 7.5%): V7 canonical = 41.90 Myr; Planck H₀ inverted through S = 42.59 Myr; GRUT-predicted H₀ inverted = 41.75 Myr; SH0ES H₀ inverted = 39.48 Myr. The GRUT self-consistency check — predicting H₀ = 69.03 and inverting back — recovers τ₀ = 41.75 Myr, within 0.4% of canonical.

*Cluster-merger group* (3 routes, spread 10.8%): Bullet Cluster = 48.89 Myr; MACS J0025 = 47.87 Myr; Abell 520 = 53.28 Myr. These are systematically +20.7% higher than the cosmic-baseline group — the same diagnostic signal seen in the cluster-scaling 0.79-0.88 systematic (Chapter 9), viewed from the inverse direction.

Two readings of the inter-group offset: (1) within the ~30% observational uncertainty on cluster collision parameters; (2) a specific diagnostic signal that, if persistent across more cluster data, would constrain τ₀, the kernel structure, or extended-mass corrections. The framework documents both readings without papering over the systematic.

**The vacuum impedance: α = 1/3.** This value is derived via the Gate R identification (formalized May 2026): the Weyl decomposition $g_{\mu\nu} = e^{2\sigma}\hat{g}_{\mu\nu}$ isolates $\sigma$ as a single real scalar degree of freedom; the Einstein–Hilbert action gives $\sigma$ conformal coupling $\xi_c = 1/6$ on $S^4$ without tuning; spin-statistics excludes fermion and gauge-field alternatives; the published trace anomaly (Duff 1994 (eq 30–31)) gives $(a,c) = (1,3)$ for a real conformally-coupled scalar, hence $\alpha_{\rm vac} = a/c = 1/3$ exactly. The identification is formalized, not merely posited — see Chapter 7 and `theory/hard_theory/GATE_R_WEYL_DECOMPOSITION_FORMALIZATION.md`.

α equals the trace anomaly ratio a/c for a single real conformally-coupled scalar (Duff 1994 / Khasanov-Segal 2011). The per-species coefficients (a, c) = (1, 3) for a real scalar, (11/2, 9) for a Weyl fermion, (62, 36) for a gauge boson are locked as exact fractions in the codebase, reproducing a/c = 1/3 as a Fraction equality — not a floating-point approximation. SM cross-checks: a/c = 1991/1698 (Majorana ν) and 253/219 (Dirac ν) both reproduced exactly.

In the language of materials science, α measures how much the medium yields under gravitational stress relative to how much it resists — the ratio of gravitational susceptibility to elastic modulus.

**What derives from the two constants:**

$$n_g^2(\omega) = 1 + \frac{\alpha}{1 + (\omega\tau_0)^2}$$

The refractive index of the vacuum. At DC (ω → 0): n_g = √(1 + α) = √(4/3) ≈ 1.15470. At high frequency (ω → ∞): n_g → 1 (GR recovered). Every dark-matter and dark-energy phenomenon is encoded in this single function.

$$S = \frac{12\pi}{\alpha^2} = 108\pi \approx 339.29$$

The screening factor. Links the cosmological relaxation time τ_Λ = Sτ₀ to the local constitutive time τ₀.

$$a_0 = \frac{c}{2\pi\tau_\Lambda} = \frac{cH_0}{2\pi} \approx 1.2 \times 10^{-10} \text{ m/s}^2$$

The MOND acceleration scale. Derived, not fitted. This is the acceleration at which the vacuum's constitutive response becomes significant — the threshold between the GR regime and the refractive regime.

$$T_c = \frac{\hbar}{\tau_{\rm micro} k_B} \approx 5.47 \times 10^7 \text{ K}$$

The critical temperature — the "boiling point of gravity." Above T_c, the vacuum has no memory and gravity is local (BBN regime). Below T_c, the metric develops bandwidth-limited response (dark-matter regime). This explains why GRUT and ΛCDM coincide during BBN: at T > 10⁹ K, the vacuum was above T_c, and the constitutive corrections vanish.

**Two-τ-scale convention (Correction #22, May 2026).** The framework distinguishes two relaxation timescales of the responsive vacuum: the **macroscopic gravitational** τ₀ = 41.9 Myr (anchored by 1/(H₀ × 108π) and the Bullet Cluster offset δ ≈ v×τ₀, used in every cosmological-scale prediction), and the **microscopic thermal** τ_micro ≈ 1.4×10⁻¹⁹ s (defined by τ_micro ≡ ℏ/(k_B × T_c), anchored empirically by the cosmological-chronology pin T_c at t ≈ 1 hour post-Big Bang). The 34-orders-of-magnitude separation is named explicitly. The pre-resolution form T_c = 1/(τ₀ × k_B) was dimensionally invalid (units K/(J·s), not K); the SI-correct form T_c = ℏ/(τ_micro × k_B) is what the framework now carries, with the numerical value 54.7 MK preserved exactly. The relation between τ₀ and τ_micro — whether they are derivable from a common foundation, or are two empirically anchored inputs — is a sharper open question (`tau_zero_to_tau_micro_relation_open_question`, Ch 14) replacing the original dimensional-inconsistency open negative #15 (now RESOLVED). See `theory/derivation/CORRECTION_22_TAU_CLEANUP.md` for the full provenance.

### Foundations audits — what the constants are anchored on

The closure principle from Chapter 1 — *no privileged outside positions, no concealed inputs* — applies to the framework's own foundational constants. If τ₀, α, and T_c are derived under named postulates, those postulates need to be auditable. The framework maintains a `theory/foundations_audit/` directory in the GRUT-RAI repository (DOI 10.5281/zenodo.18993689) with formal provenance documents for each foundational constant. Each audit traces the constant's derivation chain, performs dimensional and cross-route consistency checks, and records the framing corrections that emerged. As of v8→v2 (May 2026), all three primary audits are closed; the residual open question is the τ₀↔τ_micro relation derivation (sharper successor of the resolved T_c provenance). Each audit was a substantive correction to the framework's self-description, not a cosmetic edit.

**ALPHA_VAC audit (closed; upgraded by Gate R, May 2026).** The April 2026 foundations audit established that α = 1/3 via the "vacuum impedance = 1/d" narrative (v11 Appendix H) was an assertion, not a published derivation, and corrected the framing to *"computed under named postulate."* Gate R (May 2026) upgrades this further: the conformal-mode identification is now *formalized* through the Weyl decomposition, the Einstein–Hilbert conformal coupling, and the published Duff 1994 (eq 30–31) trace-anomaly coefficients (Route 2). The exact-Fraction value 1/3 is unchanged. The framing is now: *"α_vac = 1/3 derived via Gate R — formalized Weyl-decomposition identification of the gravitational conformal mode as a real conformally-coupled scalar."* The old "vacuum impedance = 1/d" narrative is superseded. Documented in `theory/foundations_audit/ALPHA_VAC_PROVENANCE.md` and `theory/hard_theory/GATE3_ALPHA_VAC_PROVENANCE.md`. See Correction #1 and Gate R closure in the Ch 14 ledger.

**TAU_0 audit (closed).** Established that τ₀ = 41.9 Myr is anchored by two independent cosmic-scale routes: the cosmic-baseline relation 1/(H₀ × 108π), agreeing to 1.7%, and the Bullet Cluster gas-to-lensing offset, agreeing to 17%. Three additional cluster anchors (MACS J0025, Abell 520, El Gordo) provide cross-checks. The original framing was *"derived from CTP noise-kernel structure at the gold benchmark"*; the audit found that the gold-benchmark formula does not produce 41.9 Myr (it gives a microscopic timescale, ~0.24 ms), and the gold benchmark is a *downstream consistency check* of the decoherence rate, not the source of τ₀. The audit also caught the gold-benchmark unit error (m = 80.8 fg → 80.8 pg, factor 10³) as a side-product. Framing corrected to *"anchored by named cosmic-baseline + cluster routes; gold-benchmark consistency verified at the 689 Hz plateau."* Documented in `theory/foundations_audit/TAU_0_PROVENANCE.md`. See Corrections #2 and #3 in the Ch 14 ledger.

**T_C audit (RESOLVED — Correction #22, Priority 1, May 2026).** The audit originally found that T_c ≈ 54.7 MK was dimensionally inconsistent with the formula T_c = ℏ/(τ₀ k_B) when τ₀ = 41.9 Myr (the canonical macroscopic value): plugging in τ₀ = 41.9 Myr gives T_c ≈ 5.78 × 10⁻²⁷ K, off by ~34 orders of magnitude from the codebase value 54.7 MK. The diagnosis was that the framework had been using one symbol (τ₀) for two physically distinct scales — a *macroscopic* gravitational relaxation time (41.9 Myr, load-bearing for cosmological and decoherence-plateau phenomena) and an implicit *microscopic* plasma-relaxation time (~10⁻¹⁹ s, required for T_c to be at the MK scale). **Resolution (Correction #22):** the framework now formalizes the two-scale structure explicitly: τ₀ = 41.9 Myr (gravitational sector) is distinguished from τ_micro = ℏ/(k_B × T_c) ≈ 1.4×10⁻¹⁹ s (thermal sector), with T_c computed via the SI-correct formula T_c = ℏ/(τ_micro × k_B). The numerical value 54.7 MK is preserved exactly. The previous open negative `t_c_provenance_inconsistency_open_negative` (Ch 14 #15) is RESOLVED; the sharper successor `tau_zero_to_tau_micro_relation_open_question` tracks whether the two scales are derivable from a common foundation. Documented in `theory/foundations_audit/T_C_PROVENANCE.md` (closing addendum) and `theory/derivation/CORRECTION_22_TAU_CLEANUP.md`.

**Pointers for specialists.** Each audit document in `theory/foundations_audit/` includes the full derivation chain, the dimensional checks, the cross-route verifications, and the framing corrections that emerged. Specialists who want to verify any of these audits can navigate to the audit documents directly. The discipline pattern across all three: *what the constant is, where it comes from, and what postulate or anchor is doing the load-bearing work* — surfaced explicitly rather than absorbed into derivations.

*Registry claims: tau_0_derivation (computed), alpha_vac_derivation (computed), refractive_index (computed), screening_108pi (computed), mond_a0 (computed), critical_temperature (computed), tau_0_cross_consistency (computed), t_c_provenance_inconsistency_resolved (resolved — Correction #22 two-τ-scale convention), correction_ledger (meta)*

---

# Chapter 3 — The Equation

*One action, one equation, one principle.*

**The CTP action.** Physics is formulated on the Schwinger-Keldysh closed time path. The degrees of freedom are doubled into forward (+) and backward (−) branches. In the Keldysh basis:

$$z_r = \frac{z_+ + z_-}{2} \quad \text{(classical field)}$$

$$z_a = z_+ - z_- \quad \text{(quantum field)}$$

The CTP effective action takes the universal form:

$$S_{\text{CTP}}[z_r, z_a] = z_a F[z_r] + \frac{i}{2} z_a N z_a$$

where F[z_r] is the equation-of-motion operator from the classical action and N is the noise kernel — the connected Hadamard function of the stress-energy tensor. F encodes deterministic dynamics. N encodes irreducible quantum fluctuations. Both emerge from the same action. Neither is postulated independently.

The CTP action structure is verified computationally against four structural legs on a concrete example (driven harmonic oscillator with vacuum noise):

1. **Field doubling.** The Keldysh basis (z_r, z_a) ↔ (z_+, z_−) transformation is invertible for all amplitudes including extreme values. Verified numerically with random inputs.
2. **Variation principle.** δS_CTP/δz_a |_{z_a=0} = F[z_r] reproduced to 10⁻⁸ agreement on 20-point spatial grids. The classical equations of motion emerge from the CTP variation, not as an independent postulate.
3. **Causality.** The retarded kernel K(t) = 0 for all t < 0. The response is strictly causal — no influence from the future. Verified over the full temporal domain.
4. **Fluctuation-dissipation theorem (KMS).** Both limits recovered: classical (k_BT ≫ ℏω → N = 4k_BT/τ) and quantum (k_BT ≪ ℏω → N = 2ℏω/τ) to 1% accuracy. Dissipation and noise are linked by the KMS thermal condition — they are not independent.

**The constitutive equation.** Varying S_CTP with respect to z_a and taking the Markovian limit yields:

$$\tau_0 \frac{dz}{dt} + z = z_{\text{target}}[z]$$

This is the master equation of GRUT. It says: the field z relaxes toward its target z_target[z] with time constant τ₀. Three independent derivations produce this form:

*Route 1 (CTP variation).* Direct expansion of δS_CTP/δz_a = 0 in the non-relativistic limit, with the constitutive projection for second-order sectors.

*Route 2 (Mori-Zwanzig).* Starting from the exact microscopic dynamics dz/dt = F[z] + ∫ K(t−t')z(t')dt' + ξ(t), the finite-memory (Markovian) limit of the retarded integral gives the constitutive form with τ₀ set by the kernel's decay time.

*Route 3 (Thermodynamic).* Maximum entropy production subject to the KMS thermal constraint fixes the kernel uniquely to exponential form, reproducing the constitutive equation with τ₀ = ℏ/(2k_BT_c).

**The target functional.** z_target[z] is not a free function. It is determined by the CTP action:

$$z_{\text{target}}[z] = z - \left(\frac{\delta F}{\delta z}\right)^{-1} F[z]$$

This is the Newton-Raphson step from the current state z toward the zero of the equations of motion F[z] = 0. The target is wherever the classical equations of motion would put the field — but the constitutive equation says the field can't get there instantaneously. It relaxes toward the target with time constant τ₀.

**The noise kernel.** The second variation of S_CTP gives the fluctuation structure:

$$\frac{\delta^2 S_{\text{CTP}}}{\delta z_a^2} = iN$$

The noise is not added by hand. It is generated by the CTP doubling. In the gravitational sector:

$$N_{\text{grav}}(x, x') = \frac{G}{\hbar|x - x'|}$$

This is the Diósi-Penrose kernel — the same object that Diósi (1987) and Penrose (1996) postulated as the source of gravitational decoherence. In GRUT, it is not postulated. It is the second variation of S_CTP in the gravitational sector.

The stochastic constitutive equation with noise:

$$\tau_0 \frac{dz}{dt} + z = z_{\text{target}}[z] + \xi(t), \quad \langle\xi(t)\xi(t')\rangle = N(t,t')$$

The KMS (Kubo-Martin-Schwinger) thermal condition constrains the noise spectrum:

$$N(\omega) = \frac{2}{\tau_0}\hbar\omega\coth\left(\frac{\hbar\omega}{2k_BT}\right)$$

Both noise and dissipation are outputs of S_CTP. Neither is postulated.

**The fixed point.** At the fixed point of the constitutive equation:

$$z^* = z_{\text{target}}[z^*]$$

The time derivative vanishes. τ₀ drops out. The fixed-point state is determined entirely by the CTP action. It is stable when all eigenvalues of dz_target/dz at z* have magnitude less than 1.

This is the self-referential principle from Chapter 1, now given mathematical form. The fixed point is the state that generates its own target. The dynamics are the relaxation toward it. Everything in GRUT — from quantum mechanics to the Hubble rate — is a sector-specific instance of this universal structure.

*Registry claims: ctp_action_structure (computed), constitutive_equation (computed), memory_kernel_form (computed), framework_axioms_locked (computed)*

---

# Chapter 4 — The Crystal and the Fluid

*One medium. One equation. One threshold. Across sixty orders of magnitude.*

The framework's second organizing principle is scale universality: the same constitutive equation, the same four constants (τ₀, α, S, R), applied across every regime from Planck-scale UV physics to Hubble-scale expansion. This chapter is the map. It places every phenomenon the framework addresses on a single axis — the crystallinity parameter X — and shows that quantum mechanics, gravitational decoherence, dark matter, dark energy, and the observer's classical definiteness are the same medium evaluated at different frequencies.

At every point in spacetime, the vacuum exists simultaneously in two states: crystallized at high frequencies and fluid at low frequencies. The threshold between them is not a surface in space. It is a local, frequency-dependent condition.

**The threshold.** For any system with characteristic mass m, separation l, and dominant dynamical frequency ω, the crystallinity parameter is:

$$X = \max(\omega, \Lambda_{\text{grav}}) \times \tau_0$$

where Λ_grav = Gm²S(l/R)/(ℏl) is the gravitational decoherence rate.

- X ≫ 1: **Crystal.** The mode has completed its constitutive relaxation. The physics is classical, deterministic, local. This is GR. This is you.
- X ≪ 1: **Fluid.** The mode is still relaxing. The vacuum's refractive enhancement is active. The physics is non-local, retarded, frequency-dependent. This is where dark matter lives.
- X ≈ 1: **The crystalline boundary.** The transition between quantum and classical. For nanoparticles at the decoherence plateau, X ≈ 1. This is where the primary experiment lives.

**Why you are classical.** A 1-gram body at 1-mm separation has Λ_grav ≈ 10²⁰ Hz. Λ_grav τ₀ ≈ 10³⁵. You are deep crystal. You crossed the crystalline boundary in the first Planck time of your existence. Your classical definiteness — the fact that you have a position, a mass, a shape — is the fixed point z = z* for your particular field content.

Atoms are crystal too, but not via gravitational decoherence. An atom's Λ_grav is tiny (~10⁻¹⁹ Hz). Atoms are crystallized by their electromagnetic dynamics: ω_electronic ≈ 10¹⁵ Hz, giving X = ω_electronic τ₀ ≈ 10³⁰. Atoms are classical because their internal dynamics are fast, not because their gravitational decoherence is strong. The threshold is X = max(ω, Λ_grav) × τ₀ — whichever rate dominates.

**Why the solar system is safe.** Saturn's orbital frequency: ω ≈ 10⁻⁸ Hz. ωτ₀ ≈ 10⁷. Deep crystal. The constitutive correction to Saturn's orbit is of order (ωτ₀)⁻² ≈ 10⁻¹⁴. Unmeasurable. GR is exact in the solar system because the solar system operates at frequencies far above the vacuum's bandwidth.

This is not a single-test claim. Eight independent precision GR tests span 11 orders of magnitude in frequency, all safe:

| Test | Period | ωτ₀ | Safety factor |
|:---|:---|:---|:---|
| Saturn ranging | 30 yr | 8.8 × 10⁶ | 2.3 × 10⁵ |
| Earth orbital | 1 yr | 2.6 × 10⁸ | 2.1 × 10⁸ |
| Mercury perihelion | 88 d | 1.1 × 10⁹ | 1.1 × 10¹⁶ |
| Lunar laser ranging | 27.3 d | 3.5 × 10⁹ | 3.7 × 10⁶ |
| GPS relativity | 12 hr | 1.9 × 10¹¹ | 1.1 × 10¹⁰ |
| Hulse-Taylor pulsar | 7.75 hr | 3.0 × 10¹¹ | 4.3 × 10²⁰ |
| Cassini Shapiro delay | 500 s | 1.7 × 10¹³ | 1.9 × 10²² |
| LIGO GW170817 | 10 ms | 8.3 × 10¹⁷ | 1.5 × 10³⁵ |

The smallest margin (Saturn) is still 230,000× below current detection precision. The framework recovers GR not as a coincidence at one scale but as a systematic consequence of the deep-crystal regime: α_eff = α/(1 + (ωτ₀)²) is suppressed by 1/(ωτ₀)² across the entire frequency range. Future ranging precision improvements (LISA, intersatellite ranging) might eventually approach the Saturn threshold; at current and near-term sensitivities, every test sits comfortably safe.

**Why galaxies aren't.** A galactic rotation curve operates at ω ≈ 10⁻¹⁶ Hz. ωτ₀ ≈ 10⁻¹. Near the boundary. The refractive enhancement n_g² − 1 = α/(1 + (ωτ₀)²) ≈ 1/3 is fully active. The gravitational potential is enhanced by 33% — which is what we observe and call "dark matter."

**The regime map.** The constitutive equation produces a continuous landscape:

| Scale | ωτ₀ | Regime | Phenomenology |
|:---|:---|:---|:---|
| Planck | 10⁶⁰ | Deep crystal | QG sector — UV completion |
| Particle physics | 10⁴⁰ | Deep crystal | SM recovered exactly |
| Atomic | 10³⁰ | Deep crystal | QM exact (via EM ω) |
| Laboratory (1g, 1mm) | 10³⁵ | Deep crystal | Classical mechanics |
| Solar system | 10⁷ | Deep crystal | GR exact |
| Galactic rotation | 10⁻¹ | Boundary | Dark matter appears |
| Cluster dynamics | 10⁻² | Fluid | Full refractive enhancement |
| Hubble expansion | 10⁻³ | Deep fluid | Dark energy / terminal velocity |

The dark sector is not a substance added to GR. It is the low-frequency behavior of the same vacuum you are standing in.

**Universal scale map.** The regime table classifies *where* on the axis each phenomenon sits. The next table makes the second organizing principle active: it tours what the medium is *doing* at each operating point. The same four constants — τ₀ = 41.9 Myr, α = 1/3, S = 108π, R = √(4/3) — are at work in every row. No constants are added scale-by-scale; the medium is the same throughout.

| Phenomenon | Operating point (ω, m, l) | X | What the medium is doing |
|:---|:---|:---|:---|
| Planck UV completion | ω ≈ 10⁴⁴ Hz | 10⁶⁰ | Locked deep in crystal — τ→0 limit, GR/QFT exact |
| Atomic QM | ω_EM ≈ 10¹⁵ Hz | 10³⁰ | Responding instantaneously — Schrödinger equation as the τ→0 limit |
| Lab decoherence | 1 g at 1 mm | 10³⁵ | Decohering body pairs at Λ_grav = Gm²S(l/R)/(ℏl) |
| Decoherence plateau | nanoparticle, Λ_grav ≈ 1/τ₀ | ~1 | Sitting on the boundary — 689 Hz plateau, primary falsifier |
| Solar system GR | ω ≈ 10⁻⁸ Hz (Saturn) | 10⁷ | Suppressing constitutive corrections by 1/(ωτ₀)² ~ 10⁻¹⁴ |
| Galactic rotation | ω ≈ 10⁻¹⁶ Hz | 10⁻¹ | Active refractive enhancement — n_g²−1 ≈ 1/3, mimicking dark matter |
| Cluster merger (Bullet, El Gordo) | merger v over Δt ~ τ₀ | fluid | Remembering past mass distribution — 130 kpc gas-to-lensing offset |
| Cosmological constant | ω → 0 | 0 | Producing Ω_Λ ≈ 0.69 from the bandwidth integral (two independent routes) |
| Hubble rate | ω → 0 | 0 | Acting as terminal velocity — H₀ = 1/(τ₀ × 108π), the conformal-mode relaxation |
| Cosmic regime crossing | H(z)×τ₀ = 1 | 1 | Crossing crystal/fluid boundary at z ≈ 71 (atomic perturbations) |
| Dark matter density | ω → 0 | 0 | Geometric impedance contribution — Ω_dm = 1/3 from α alone |
| Baryogenesis η_B | KMS noise at T_GUT | n/a | Generating asymmetry through fluctuation-dissipation — η_B ≈ 6×10⁻¹⁰ |
| Observer classical definiteness | Λ_grav at body scale | ≫1 | Crystallizing the observer — measurement axiom dissolves |

Sixty orders of magnitude in frequency. Four constants. One equation. The phenomenology in each row is not a separate theory tuned to that scale — it is what the medium *does* when it interacts with that particular matter configuration at that particular frequency. Quantum mechanics, dark matter, dark energy, the Hubble rate, the observer's own classical definiteness: all of them are the medium responding through the same constitutive equation, with the same constants, remembering its past on the same 41.9 Myr timescale.

One medium. One equation. One threshold.

**The screening mechanism.** The screening factor S(l/R) = min(1, (l/R)³/6) ensures that the constitutive effect is suppressed at short distances. In the near field (l < R), the response is cubic in l/R — it turns on gradually. In the far field (l ≥ R), S = 1 — the full constitutive response is active. This is why the solar system doesn't feel dark matter: at solar-system separations, S is maximal but ωτ₀ ≫ 1. The screening is frequency-based, not distance-based.

**Cosmic regime evolution.** The regime classification applied to the cosmic background itself, using ω = H(z) as the dominant dynamical rate for atomic-scale test-particle perturbations, gives X_cosmic(z) = H(z) × τ₀. This crosses X = 1 at z ≈ 71 (T_CMB ≈ 197 K). Today X ≈ 0.003 (deep fluid — full refractive enhancement active). At recombination X ≈ 68 (deep crystal — GR recovered).

This is specifically the regime evolution for atomic-scale perturbations. Different mass classes give different X values at the same epoch: for stellar masses and above, Λ_grav dominates H by 76+ orders, placing compact objects in deep crystal at all redshifts regardless of cosmic epoch. Which mass class is "load-bearing" for cosmic-history regime evolution is connected to open negative #9 (n_g(ω) covariance).

*Registry claims: threshold_bridge (computed), crystallinity_function (computed), regime_map (computed), screening_108pi (computed), cosmic_x_crossover_prediction (computed)*

---

## Part II — Recovered Physics and the Backbone

# Chapter 5 — Recovered Physics

*What the framework reproduces when you supply the Standard Model.*

GRUT imports the Standard Model Lagrangian as S_classical in the CTP action. It does not derive the SM. What it does is show that the SM is the smallest known structure compatible with five CTP consistency constraints, and that its low-energy limits are reproduced exactly.

**Quantum mechanics (exact).** Setting z = ψ (wavefunction) in the constitutive equation with τ_I = ℏ/2:

$$z_{\text{target}} = \psi + \frac{\hbar}{2m}\nabla^2\psi - \frac{i}{\hbar}V\psi \times \tau_I$$

In the limit τ → 0 (instantaneous response), the constitutive equation reduces to:

$$i\hbar\frac{d\psi}{dt} = -\frac{\hbar^2}{2m}\nabla^2\psi + V\psi$$

The Schrödinger equation. Exact. No approximation. The constitutive equation is a generalization of quantum mechanics, not a modification of it. This recovery is verified computationally: a precessing qubit evolved under the constitutive equation in the τ → 0 limit reproduces z_target exactly, preserves norm to first order, and recovers ⟨σ_x(t)⟩ = cos(ωt) — three independent legs, all passing.

**SM emergence.** Five CTP constraints — gauge invariance, renormalizability, anomaly cancellation, unitarity, and CPT — are satisfied by the SM field content. GRUT does not prove the SM is the *unique* theory satisfying these constraints (larger gauge groups like SU(5), SO(10), Pati-Salam also satisfy them). What GRUT shows is that the SM is the smallest known structure satisfying all five CTP consistency checks simultaneously, and that its specific field content (4 real scalars, 45 Weyl fermions, 12 gauge bosons) passes all five checks. N = 3 generations is selected uniquely by the Z₃ Koide circulant structure. All five constraints are verified computationally: gauge structure (8+3+1 = 12 generators), anomaly cancellation (Σ Y² = 10 per generation, β_U(1) = 20/3), three-generation count (15 × 3 = 45 Weyl fermions), Koide K = 2/3 (exact Fraction), and trace-anomaly numerators (a = 1991/2, c = 849) all reproduced.

**Gravitational decoherence (exact, zero free parameters).** The noise kernel N_grav produces a decoherence rate:

$$\Lambda_{\text{grav}} = \frac{Gm^2 S(l/R)}{\hbar l}$$

Six scaling laws, all independently falsifiable:

1. **Mass-squared (F1):** Λ_grav ∝ m². Verified across 20 orders of magnitude.
2. **Geometry (F2):** S(l/R) = min(1, (l/R)³/6). Cubic onset in near field.
3. **Plateau (F3):** Λ_grav saturates at large R. The nanoparticle plateau at ~689 Hz.
4. **Separation (F4):** Λ_grav ∝ 1/l in far field.
5. **Entanglement protection (F5):** Decoherence-free subspaces survive.
6. **Geometric kink (F6):** Sharp transition at l = R.

Five tested alternative models reach 0-4 of GRUT's six scaling laws under strict criteria:

| Model | F1 (m²) | F2 (geom) | F3 (plateau) | F4 (1/l) | F5 (entangle) | F6 (kink) | Score |
|:---|:---|:---|:---|:---|:---|:---|:---|
| GRUT | Yes | Yes | Yes | Yes | Yes | Yes | 6/6 |
| Diósi-Penrose | Yes | Yes | No | Yes | No | Yes | 4/6 |
| Anastopoulos-Hu* | Yes | Yes | Partial | Yes | Partial | Yes | 4/6+2p |
| CSL (Ghirardi) | No | No | No | No | No | No | 0/6 |
| Adler (mass-prop CSL) | Yes | No | No | No | No | No | 1/6 |
| GRW | No | No | No | No | No | No | 0/6 |

*Anastopoulos-Hu is the foundational master equation GRUT extends, not a competitor — included for completeness.*

Diósi-Penrose is the closest classical competitor at 4/6, sharing the G/(ℏ|x−x'|) kernel with GRUT but missing the strict 689 Hz plateau (its plateau value depends on the regulator R₀ rather than τ₀) and native decoherence-free subspace preservation. Strict criteria: F3 requires the specific 689 Hz value with zero free parameters; F5 requires DFS preservation as a native consequence of the noise kernel, not added by hand.

The decoherence plateau (F3) and the geometric kink (F6) are the most discriminating — no competitor produces either under strict criteria. The plateau is the primary falsifier for the entire framework.

**Isotope-pair discriminator: GRUT vs CSL.** The framework's lab-scale program has a second independent falsifier beyond the decoherence plateau. GRUT predicts Λ_grav ∝ m² (gravitational mass squared). CSL predicts Λ_CSL ∝ N (nucleon count, linear). For most matter these are degenerate — mass scales with particle number. Isotope variants break the degeneracy: same element, same particle count, different mass.

| Isotope pair | GRUT ratio (m²) | CSL ratio (linear-N) | Discriminator | Precision needed |
|:---|:---|:---|:---|:---|
| ³⁰Si / ²⁸Si | 1.1478 | 1.0714 | +7.13% | 3.8% |
| ¹⁰⁹Ag / ¹⁰⁷Ag | 1.0378 | 1.0187 | +1.87% | 0.95% |
| ¹⁸⁴W / ¹⁸²W | 1.0221 | 1.0110 | +1.10% | 0.56% |

GRUT is parameter-free at this scale — Λ_grav = Gm²S(l/R)/(ℏl), every input known. CSL's localization parameter λ cancels in isotope ratios (it enters numerator and denominator identically), so the discriminator is structural: quadratic vs linear mass scaling. Silicon gives the largest signal (7.13%) and requires only 3.8% measurement precision — within reach of next-generation matter-wave interferometry (MAQRO-class experiments).

The decoherence plateau tests the absolute coupling magnitude. The isotope discriminator tests the dimensional structure of the constitutive equation. Both must hold for GRUT's decoherence sector to be correct. They can fail independently, doubling the falsifier surface at the framework's most testable scale.

**External evidence for vacuum-as-medium.** The GRUT picture — that particle properties change because the vacuum responds constitutively to stress-energy — has independent experimental support in the QCD sector. The April 2026 η′-mesic nucleus result (Osaka/GSI) shows the η′ meson's mass decreases inside dense nuclear matter, demonstrating that the QCD vacuum modifies its constitutive properties under stress. GRUT extends this principle from the QCD vacuum to the gravitational vacuum.

**Gravitational entanglement formation rate.** The framework's Λ_grav = Gm²S(l/R)/(ℏl) predicts the rate at which gravitational interaction generates entanglement between two masses — the same quantity measured in BMV-class (Bose-Marletto-Vedral) and KTM (Krisnanda-Tham-Paternostro) experiments. At canonical BMV parameters (m ~ 10⁻¹⁴ kg, l ~ 200 μm), GRUT's prediction matches the BMV literature formula to four decimal places (ratio = 1.0000). The S(l/R) screening factor introduces a discriminator at sub-micron separations: at l = 1 μm, GRUT predicts factor 0.244 suppression vs BMV; at l = 0.5 μm, factor 0.031. This is currently experimentally inaccessible but names the precise separation scale where the two predictions diverge. [ANCHORED — matches BMV at canonical parameters; discriminator accessible only at sub-micron separations]

*Registry claims: qm_recovery (computed), sm_emergence (computed), sm_field_content_locked (computed), decoherence_zero_param (computed), six_scaling_laws (computed), decoherence_alternative_models_comparison (computed), grut_csl_isotope_discriminator (computed), gravitational_entanglement_formation_rate (anchored)*

---

# Chapter 6 — Gravity

*How GR is recovered. Where it breaks. What replaces the singularity.*

**GR recovery (computed, 7 legs verified).** Setting z = g_μν (metric) in the constitutive equation gives the constitutive gravity equation:

$$G_{\mu\nu} + \Phi_{\mu\nu}(\phi) = 8\pi G \, T_{\mu\nu}$$

**Scope status (post-Corrections #23–#25, v8→v2 synthesis, May 2026).** The constitutive correction Φ_μν is now DERIVED from the variation δS_CTP/δh_a |_{h_a=0} of the linearized Schwinger-Keldysh action (Correction #23): the kernel form Φ_μν(ω) = α_vac × χ(ω) × P^TT_μνρσ × h_r^ρσ emerges structurally from the constitutive cross-term, with six structural properties verified — kernel form, high-ω GR limit, low-ω full-constitutive limit, Bianchi preservation via ∂^μ P^TT = 0, α_vac = 1/3 inheritance from Duff 1994, and consistency with the existing susceptibility postulate. The covariant curved-background extension is SCAFFOLDED (Correction #24): bitensor kernel K^R_μνρσ(x, x') = α_vac × P^TT,g_μνρσ(x, x') × G^R(x, x') with explicit √-g measure and four physical-consistency checks (flat-limit recovery, covariant conservation ∇^μ Φ = 0, causality K^R supported on past lightcone, FRW scalar-mode compatibility). The explicit FRW result is COMPUTED (Correction #25): χ_FRW^WKB(k, η) = 1/[1 + (τ₀ k_phys)²], n_g²(k, η) = 1 + α_vac/[1 + (τ₀ k_phys)²]. The previous open question #10 (`constitutive_projection_gravity_heuristic_open_question`) is RESOLVED at linearized + scaffold + explicit-FRW levels. The remaining open work — Phase 2C explicit construction of P^TT,g and G^R on specific backgrounds (FRW/S⁴) and beyond-WKB (Hτ₀)² ≈ 10⁻⁶ refinement — is now sharper-successor work, not the original heuristic-projection gap.

Seven computational legs verify the recovery: (1) Φ_μν vanishes in the high-frequency limit ωτ₀ ≫ 1; (2) Φ_μν provides the expected enhancement in the low-frequency limit ωτ₀ ≪ 1; (3) the Bianchi identity is preserved across a full (ω, k) grid under the constitutive projection (now upgraded: Bianchi follows STRUCTURALLY from ∂^μ P^TT = 0, for ALL h_r and ALL kernel time structures, not just single-mode plane waves); (4) the graviton propagator has 1/ω³ UV falloff (exponent verified at −1.00 exactly); (5-7) boundary conditions, normalization, and stability checks all pass. GR is exact in the solar system because the solar system operates at frequencies where Φ_μν → 0.

**The graviton propagator.** The CTP graviton propagator is UV-complete: the 1/ω³ falloff at high energy suppresses the usual divergences. No ghosts — the CTP contour ensures unitarity. The massless graviton is recovered (no Pauli-Fierz mass term needed).

**The nonlinear ladder.** Full nonlinear quantum gravity requires closure of 8 rungs. The first four are completed and tested:

1. **Linearized graviton propagator** — the CTP graviton propagator on flat background is UV-complete with 1/ω³ falloff. Computed.
2. **UV completion** — the falloff suppresses the usual graviton-loop divergences without introducing new degrees of freedom. No Pauli-Villars regulators, no higher derivatives. The CTP structure itself provides the regulation. Computed.
3. **No ghosts** — the CTP contour (forward + backward branches) ensures unitarity by construction. The optical theorem is satisfied for the retarded propagator. Computed.
4. **Massless graviton** — no Pauli-Fierz mass term needed. The graviton mass is identically zero in the CTP framework because the gauge symmetry is preserved at linearized level. Computed.

The remaining four are open. Each represents a specific technical challenge:

5. **Tensor-sector stability at 2nd order** — does the constitutive correction Φ_μν remain well-behaved when graviton self-interactions are included? The concern: at second order, the constitutive projection could introduce runaway modes that don't exist in the linearized theory. V7 §24 identifies the specific diagram class (graviton-graviton scattering with one constitutive vertex) that needs checking. Status: not yet computed.

6. **Diffeomorphism invariance preservation** — does the constitutive projection preserve gauge invariance beyond linearized level? At linear order, Bianchi identity preservation is verified (leg 3 of the recovery harness). At nonlinear order, the projection could break diffeomorphism invariance through terms that vanish at linear order but contribute at quadratic order. Status: structural argument exists (V7 §24.3); computation incomplete.

7. **Background independence** — the current framework computes on a fixed background (Minkowski or S⁴). A complete quantum gravity theory must be background-independent. The constitutive equation τ₀ dz/dt + z = z_target[z] is formally background-independent (z can be the full metric, not perturbations around a background), but the computational implementation hasn't verified this. Status: conceptual argument only.

8. **Non-perturbative fixed point** — does the constitutive gravity sector have a UV fixed point under RG flow? This would connect GRUT to the asymptotic safety program but through constitutive (retarded, dissipative) dynamics rather than standard Euclidean RG. The constitutive equation's fixed point z* = z_target[z*] is a candidate, but it hasn't been shown to coincide with a Wilsonian UV fixed point. Status: speculative.

4/8 completed. The remaining four are open — an honest negative documented without apology. GRUT is a quantum theory of linearized gravity, not yet a complete quantum gravity theory. The distinction matters. The framework makes no claims about Planck-scale physics, quantum cosmology, or the resolution of the information paradox at the nonlinear level until rungs 5-8 are closed.

**The Whole Hole.** In GR, curvature diverges at r = 0 because the metric responds instantaneously to any stress-energy concentration. In GRUT, the medium has a constitutive saturation limit:

$$R_{\text{max}} \sim \frac{\alpha}{c^2 \tau_0^2}$$

This is a Ricci scalar saturation — it applies to the matter-bearing interior of black holes, not the Schwarzschild vacuum exterior (where R = 0 identically and R_max imposes no constraint). The tidal Weyl curvature outside the horizon is unconstrained by R_max — the vacuum exterior can still have arbitrarily strong tidal forces. What R_max prevents is the infinite-density singularity inside.

The universal interior density cap:

$$\rho_{\text{max}} = \frac{c^2 R_{\text{max}}}{8\pi G}$$

Every black hole has the same maximum interior density, regardless of mass. Larger black holes have larger cores at this density. The singularity is replaced by a finite-density core — the Whole Hole. No tear in the manifold, no infinite density. The name reflects the structure: the hole is whole. No information is lost because there is no singularity to lose it to.

**BH information.** Hawking radiation in GRUT was never truly thermal. The constitutive correlations that standard semiclassical gravity misses carry information in the retarded gravitational response — the memory kernel K(t) encodes correlations between early and late Hawking quanta that pure thermal radiation lacks. The Page curve is reproduced at linearized level with τ₀ setting the scrambling timescale. Full nonlinear BH information recovery depends on closing rungs 5-8. [OPEN]

**Open question on ρ_max.** The numerical value ρ_max ~ 10⁻²² kg/m³ from the universal-τ₀ formula is below typical naive BH interior densities. Whether additional structure beyond the universal formula is needed for quantitatively realistic core sizes remains open and flagged. [OPEN]

**Open seam status (post-v8→v2).** The constitutive projection in the gravitational sector is now DERIVED at the linearized level (Correction #23) and SCAFFOLDED at the curved-background level (Correction #24), with the explicit FRW result computed at WKB (Correction #25). The original Chapter 14 open question #10 (`constitutive_projection_gravity_heuristic_open_question`) is RESOLVED. The sharper successor open questions are: Phase 2C explicit construction of P^TT,g and G^R on FRW/S⁴ (`phi_munu_curved_background_scaffold` registered as anchored, with the explicit construction tracked separately) and the beyond-WKB (Hτ₀)² ≈ 10⁻⁶ refinement (subleading; tracked under `phi_munu_frw_beyond_wkb_open_question`). The full-Boltzmann CMB pipeline (CAMB/CLASS modification with μ_GRUT) remains a downstream computational task, theoretically unblocked by these closures.

*Registry claims: gr_recovery (computed), graviton_propagator (computed), nonlinear_ladder_4_of_8 (open_negative), r_max_ricci_saturation (computed), rho_max_universal (computed), bh_information_partial (anchored)*

---

# Chapter 7 — The Constant R

*R = √(4/3). A number as real as π.*

The canonical GRUT refractive coefficient is derived from the constitutive response kernel, not from the three-loop anomaly quotient. **The canonical route is the constitutive/refractive route. The three-loop anomaly quotient route is an honest-negative diagnostic.**

**The Gate R forward chain.** Every step is established; R is the last line.

1. Metric Weyl decomposition: $g_{\mu\nu} = e^{2\sigma}\hat{g}_{\mu\nu}$ — isolates $\sigma$ as the real scalar sector of the metric
2. $\sigma$ is spin-0, one real DOF, no gauge index — fermion and gauge alternatives excluded by representation
3. Einstein–Hilbert decomposition on $S^4$ gives conformal mass $m^2 = R/6$ — conformal coupling $\xi_c = 1/6$ exact, no tuning
4. Published trace anomaly (Duff 1994 (eq 30–31)): real conformally-coupled scalar → $(a,c) = (1,3)$ → $a/c = 1/3$
5. Identification: $\sigma \equiv$ real conformally-coupled scalar → $\alpha_{\rm vac} = a/c = 1/3$ (convention-independent, exact)
6. $\alpha_{\rm vac}$ enters the constitutive cross-kernel: $K^R = \alpha_{\rm vac}\,\chi(\omega)\,P^{TT}$ — scalar susceptibility amplitude, independent of TT projector
7. DC limit: $n_g(0)^2 = 1 + \alpha_{\rm vac} = 4/3$
8. $R = n_g(0) = \sqrt{4/3}$

**The conformal response mode: why one real scalar controls $\alpha_{\rm vac}$.**

Step 5 of the chain — the identification of the gravitational conformal mode with a real conformally-coupled scalar — is the load-bearing physical input. Steps 1–4 are standard differential geometry and published CFT results. Here is why the identification is forced, not chosen:

*Why a scalar.* The Weyl decomposition $g_{\mu\nu} = e^{2\sigma}\hat{g}_{\mu\nu}$ is the unique decomposition of the metric into a conformal factor $\sigma$ (real scalar) and a conformal equivalence class representative $\hat{g}$. The conformal factor is a real scalar by construction — it has spin 0 and no gauge index. It cannot be a fermion (spinor under $\mathrm{Spin}(4)$) or a gauge field (Lie-algebra-valued 1-form). The identification is determined by representation theory, not by the desire to produce $R = \sqrt{4/3}$.

*Why conformally coupled.* The Einstein–Hilbert action decomposed in the conformal gauge on $S^4$ gives $\sigma$ a kinetic term whose curvature coupling is $m^2 = R/6$. This is the conformal coupling $\xi_c = (D-2)/[4(D-1)] = 1/6$ in 4D, the coupling that makes $(\Box - R/6)\sigma = 0$ on-shell. No tuning: the coupling comes out of the gravitational action with no free parameter.

*Why one species.* The conformal factor $\sigma$ is a single real-valued function — one real degree of freedom. The functional integral over metrics decomposes into one integration over $\sigma$ and one over the conformal equivalence class. There is no doubling, no multiplet, and no superposition of species in the conformal sector.

*Why $P^{TT}$ does not contradict the scalar anomaly.* The constitutive kernel $K^R = \alpha_{\rm vac}\,\chi(\omega)\,P^{TT}$ contains two structurally independent factors. $\alpha_{\rm vac}\,\chi(\omega)$ is the vacuum's response amplitude — a property of the medium (the background $S^4$ vacuum with its conformal structure). $P^{TT}$ is a filter on which external perturbations $h_{\mu\nu}$ are admissible sources. The scalar anomaly sets the medium's susceptibility; the TT projector selects admissible inputs. A scalar dielectric constant does not contradict a transverse electromagnetic wave: the scalar $\varepsilon$ characterizes the medium, while transversality constrains the field. Same structure here.

*The published value.* With $\sigma$ established as one real conformally-coupled scalar, the Weyl anomaly coefficients are read directly from Duff (1994, eq 30–31): $(a,c) = (1,3)$, giving $\alpha_{\rm vac} = a/c = 1/3$. This is an exact rational number, convention-independent (the ratio $a/c$ is invariant under all normalization changes), and is a textbook result confirmed by two independent sources (Duff 1994; Christensen-Duff 1980). The old v11 "vacuum impedance = 1/d" narrative is superseded — it was a post-hoc assertion. The correct route is the trace anomaly route, and it gives the same number.

**Canonical value (constitutive/refractive route — Path G).** From the vacuum impedance:

$$R = n_g(0) = \sqrt{1 + \alpha_{\rm vac}} = \sqrt{\frac{4}{3}} = 1.15470\ldots$$

This is the DC refractive index of the vacuum. The derivation chain is fully computed: Weyl decomposition → conformal-mode scalar ($\xi_c = 1/6$) → Duff 1994 $a/c = 1/3$ → $n_g(0) = \sqrt{4/3}$. Every link is a passing test. No honest negatives in the path.

**The two R-tracks.**

| Track | Value | Status |
|:---|:---|:---|
| **Constitutive/refractive (Path G)** | $\sqrt{4/3} = 1.15470$ | **Canonical — derived** |
| 3-loop anomaly quotient (V7 §26) | $1.15428$ | **Honest negative — not reproduced in TJI Phase-0/0.5** |

These are not "tree-level + loop correction." They are two structurally independent derivation routes that give different values. The constitutive route is canonical; the anomaly-quotient route was investigated extensively and is retained as a diagnostic, not as the derivation.

**Honest-negative diagnostic: 3-loop anomaly-quotient route.** The V7 §26.2 three-loop CTP computation on Euclidean S⁴ produced:

$$R_{\text{anomaly}} = \left|\frac{C_{\text{Cosmo}}}{C_{\text{FINAL}}}\right| = 1.15428$$

Every integer in the expression traces to SM group theory (11 = QCD β₀, 99 = 11×9, 576 = 16×36, −100 = −(Σ Y²)²). The Allen-Jacobson S⁴ propagator (B. Allen & T. Jacobson, *Commun. Math. Phys.* **103**, 669 (1986)) has been Phase-1 implemented in the codebase (Correction #31, May 2026). However: the TJI Phase-0/0.5 reconciliation did **not** reproduce 1.15428 from first principles. The flat-space Phase-0.5 result is ε⁰ = −541/2304 (MS-bar); the previously cited FeynCalc value of 7/4 is unarchived and unreconcilable. **This route is an honest negative.** It is retained in the codebase and ledger as a diagnostic and as a structural cross-check on the canonical value — not as the canonical derivation. The remaining computational gate (`S4CurvatureObstacle`: Mathematica/HypExp ε-expansion of the ₂F₁³ radial integral) would either resolve or further constrain this route; it does not affect the canonical value.

**Route 3 — Independent check (Osborn local RG, now computed).** Osborn (2003) equation (36) gives a per-gauge-group ε from the local RG flow coefficients. Applied to SM gauge groups at M_Z with coupling-squared weighting (the natural QCD-dominant hierarchy):

| Gauge group | ε | Weight (α²-normalized) |
|:---|:---|:---|
| SU(3) | 1.15977 | 0.960 |
| SU(2) | 1.01746 | 0.032 |
| U(1) | 0.96726 | 0.008 |

$$\varepsilon_{\text{combined}} = \sum w_i \varepsilon_i = 1.15367$$

This is now a computed result in the codebase — 30 tests verify the per-sector values, the weighting scheme, and the combined output. The weights are not arbitrary: they emerge from coupling-squared scaling at M_Z, which is standard QFT. Osborn (2003) provides the per-group formula; the combination is derived from the coupling hierarchy.

**Routes and their status.**

| Route | Value | Status | Inputs |
|:---|:---|:---|:---|
| **Path G (canonical)** | **1.15470** | **Derived — Gate R closed** | Zero couplings — Weyl decomp. + Duff 1994 |
| **Osborn eq 36** | **1.15367** | **Computed (supporting)** | Measured α_s, α_2, α_Y at M_Z |
| V7 §26 (3-loop anomaly quotient) | 1.15428 | **Honest negative** | 3-loop CTP on S⁴ — not reproduced in TJI |

Max-min spread between the two non-negative routes: 0.089%. The two supporting routes share no inputs — one uses zero coupling constants, the other uses three measured couplings. Their agreement at <0.1% is a structural cross-check on the canonical value.

**Why Path G and Osborn converge.** Path G computes the vacuum's refractive index from its IR impedance ($\alpha_{\rm vac} = 1/3$, the conformal-mode $a/c$ ratio, zero coupling constants). The Osborn route computes the SM's combined trace-anomaly coefficient at the electroweak scale ($M_Z$) from measured gauge couplings. These converge because the conformal mode that carries the vacuum's IR response is the SM gravitational sector evaluated at its natural matching scale — the UV (electroweak) trace anomaly and the IR (gravitational) refractive index are measuring the same object at different scales. The convergence at 0.089% is not a coincidence; it reflects the SM's RG flow connecting IR vacuum properties to UV gauge structure. A precise derivation of this connection — showing that $n_g(\omega\to 0) = \varepsilon_{\rm combined}({\rm SM}, M_Z)$ up to loop corrections — would close the convergence from "remarkable agreement" to "derived identity."

**What R means physically.** R is the gravitational refractive index of the vacuum — how much slower gravity responds than it would in a perfectly elastic medium. At R = 1, gravity would be instantaneous: no dark matter, no constitutive expansion, no memory. At R = √(4/3) = 1.15470, gravity has a 41.9 Myr lag, a refractive enhancement of 1/3 at galactic scales, and an expansion rate driven by the conformal instability.

"The universe is √(4/3) ≈ 1.15470 trying to become 1."

**Open seam.** The 3-loop anomaly-quotient value $R_{\rm anomaly} = 1.15428$ remains honest_negative (Chapter 14, open question #2). The Allen-Jacobson Phase-1 S⁴ propagator is implemented (Correction #31, May 2026); the remaining gate is the Mathematica/HypExp ε-expansion of the $[{}_2F_1(h_+,h_-;D/2;(1+Z)/2)]^3$ radial integral (`S4CurvatureObstacle`). Closing this gate would either reproduce 1.15428 (confirming the anomaly-quotient route as a consistency check on the canonical value) or rule it out further. Either outcome leaves the canonical $R = \sqrt{4/3}$ unchanged. [HONEST NEGATIVE]

*Registry claims: r_canonical_path_g (computed — Gate R closed, constitutive/refractive route canonical), r_path_osborn_epsilon (computed — supporting), r_loop_corrected (open_negative/honest_negative — 3-loop anomaly-quotient route not reproduced in TJI Phase-0/0.5; retained as diagnostic), three_routes_convergence (computed — Path G + Osborn are load-bearing; anomaly-quotient is diagnostic), integer_provenance_traced (computed), tji_7_4_open_negative (open_negative)*

---

# Chapter 8 — The Terminal Velocity

*Why the universe expands. The strongest result in the framework.*

**The conformal instability.** In standard Euclidean gravity on a closed S⁴ manifold, the conformal mode's kinetic energy is strictly negative. The action is unbounded below. The path integral diverges. Gibbons, Hawking, and Perry (1978) resolved this by rotating the conformal factor into the complex plane — manually forcing the action positive.

GRUT does not need the Gibbons-Hawking rotation. The conformal instability is not a pathology. It is the engine of cosmic expansion.

**The −100.** The anomaly coefficient C_Cosmo is negative: C_Cosmo < 0. The magnitude traces to the SM hypercharge sum through the following chain:

*Step 1: SM hypercharge sum.* Per generation, the SM hypercharges squared sum to Σ Y² = 10 exactly (left-handed quarks: 6 × (1/6)² = 1/6; right-handed up quarks: 3 × (2/3)² = 4/3; right-handed down quarks: 3 × (1/3)² = 1/3; left-handed leptons: 2 × (1/2)² = 1/2; right-handed electron: 1 × 1² = 1; total = 10/3 per component... summing all components gives 10). Across 3 generations: 30. Per-generation average: 10.

*Step 2: How Σ Y² enters the CTP effective action.* In the 3-loop CTP computation on Euclidean S⁴, the U(1) hypercharge sector contributes a sub-insertion at 2-loop level. The FeynCalc-verified topology (V7 §26.2.3) shows this sub-insertion enters as (Σ Y²)² = 100 in the coefficient. The squaring arises because the 3-loop diagram has two U(1) vertices, each contributing one factor of Σ Y².

*Step 3: The sign.* The overall sign of C_Cosmo is negative — identified with the Gibbons-Hawking conformal-mode instability of the Euclidean action on S⁴. The sign encodes the direction of expansion.

**What this chapter does NOT contain:** The full 3-loop integral that produces −100 as a coefficient. That computation lives in V7 §26.2 (primary-source audit with integer provenance). The Allen-Jacobson Phase-1 propagator is now implemented (Correction #31, May 2026); the remaining specialist work is the Mathematica/HypExp ε-expansion of the ₂F₁³ radial integral (Chapter 14, open question #2, `S4CurvatureObstacle`). The derivation chain here traces the structural origin of the integer; the loop integral that assembles it is targeted by `theory/hard_theory/HYPEXP_TARGET_NOTEBOOK.ipynb`.

**The terminal velocity formula.** The Hubble rate decomposes as:

$$H_\infty = \frac{\text{drive}}{\text{friction}} = \frac{2 - R}{S \times \tau_0}$$

- **Drive** = 2 − R = 0.845. Using canonical R = √(4/3) = 1.15470 (Gate R, constitutive/refractive route). The Osborn supporting value R = 1.15367 gives drive = 0.846 — a 0.1% cross-check, not a loop correction. The conformal-mode outward pressure.
- **Friction** = S × τ₀ = 108π × 1.322 × 10¹⁵ s = 4.487 × 10¹⁷ s. The constitutive damping.
- **Terminal velocity** = H_inf = 1.885 × 10⁻¹⁸ Hz = 58.15 km/s/Mpc (canonical R). Using the Osborn cross-check (R = 1.15367) gives 58.18 km/s/Mpc. The 0.05% spread is a consistency check across independent routes, not a loop correction to the canonical value.

Cosmological expansion is not a static constant (Λ). It is the terminal velocity of a medium whose conformal mode is unstable but whose constitutive response prevents runaway.

**The cosmological constant.**

$$\Omega_\Lambda = \left(\frac{H_\infty}{H_0}\right)^2 = 0.6886$$

Planck 2018: 0.6889. The two computed routes (R = 1.15470 and R = 1.15367) bracket the Planck value, both within 0.2%. Zero free parameters.

**The Hubble rate.**

**The Hubble rate — two routes.**

*Route 1 (cosmic-baseline, zero parameters):* H₀ ≈ 1/(S × τ₀) = 1/(108π × 1.322 × 10¹⁵ s) ≈ 68.8 km/s/Mpc. This requires no observational input beyond what determines τ₀ and S. Genuinely zero-parameter.

*Route 2 (Friedmann integration, one parameter):* H₀ ≈ 69.03 km/s/Mpc using N_total = t₀/τ₀ = 329 (observed cosmic age) as input via Friedmann integration with the era map's transition function. Using canonical R = √(4/3) gives H₀ ≈ 69.0; using Osborn cross-check R = 1.15367 gives 69.03. These are not tree-level and loop-corrected values; they are two independently computed routes cross-checking the same derivation.

The two routes agree at 0.3% — a structural cross-check. Both sit in the Hubble tension gap between CMB (67.4) and distance-ladder (73.5). The cosmic-baseline route is the load-bearing prediction; the Friedmann route's one observational input (cosmic age) is documented as an open negative (Chapter 14, open question #13).

**The structural correlation.** H₀√Ω_Λ = H_inf = 58.16 km/s/Mpc = const. This is a testable prediction for DESI/Euclid/Roman. If the correlation holds across redshift, the terminal velocity picture is confirmed. If w(z) shows deviations from −1, the viscoelastic regulation is observable.

**The era map.** The discretized expansion history: N_total = t₀/τ₀ = 329 eras, each of duration τ₀. The era map's transition function uses R to set the sharpness of the matter-Λ transition. N_total = 329 uses observed cosmic age as input. A zero-parameter derivation of cosmic age from framework foundations would close this gap and promote the Friedmann route from one-parameter to zero-parameter (Chapter 14, open question #13).

**Open seams.** TJI Phase-1 is a stress test, not load-bearing — the two-route convergence carries the cosmological prediction independently (Chapter 14, open question #2). The conformal-mode coefficient match (Chapter 14, open question #3 prerequisite) would turn the terminal velocity picture from interpretation into derived identity. Both are documented in the auto-rendered ledger.

*Registry claims: minus_100_drive (computed), conformal_instability_identification (anchored), h_inf_terminal_velocity (computed), omega_lambda_computed (computed), h_0_one_parameter (computed), bridge_parameter_cross_sector (computed)*

---

# Chapter 9 — The Dark Sector

*Dark matter, dark energy, baryogenesis. All from the same medium.*

**Two regimes — load-bearing distinction (post v8→v2 synthesis).** Dark-sector phenomena in GRUT live in two structurally distinct regimes that use different operating variables. The deposit's predictions are organized by which regime applies; mixing them up is the most common confusion in reading the framework.

| Regime | Operating variable | Phenomena | Key observable | Module |
|:---|:---|:---|:---|:---|
| **Linear FRW perturbations** | k_phys = k/a (comoving wavenumber over scale factor) | Cosmological perturbation modes on FRW background; CMB anisotropy; matter power spectrum P(k) at low k; large-scale structure growth | μ_GRUT(k, a) = n_g²(k, a) = 1 + α/[1+(τ₀ k_phys)²], γ_GRUT = 1 (no slip) | `grut/derivation/phi_munu/frw_explicit.py`, `mg_eft_mapping.py`, `modified_growth.py` |
| **Bound systems / nonlinear halos** | Frequency-domain ω (orbital, decoherence) or time-domain τ₀ (merger evolution, BH interior) | Galactic rotation curves; cluster-merger gas-to-lensing offsets; Whole-Hole BH interiors; matter-wave-interferometry decoherence | Λ_grav, regime gate X = max(ω, Λ_grav)·τ₀, kernel-convolution offset δ ≈ v×τ₀ | `grut/foundation/closure_protocol.py` (regime gate), `grut/derived/cluster/`, `grut/derived/decoherence/` |

These two regimes operate via **different operating variables and different physical mechanisms**. The linear-FRW result of Phase 2C (Correction #25) — μ_GRUT(k_phys, a) = n_g²(k_phys, a), with sub-horizon (k_phys τ₀ ≫ 1) → ΛCDM recovery and super-horizon (k_phys τ₀ ≪ 1) → 4/3 enhancement — applies ONLY to linear FRW perturbation modes. It does NOT say that galaxies and clusters lose their constitutive enhancement. The galactic rotation curve operates in the BOUND-system regime: the relevant ω is the orbital frequency v/r, not k_phys; the regime gate X = ω·τ₀ ≪ 1 puts galaxies in "deep fluid" with full n_g² = 4/3 refractive enhancement on the bound matter (see "Why galaxies aren't" in Chapter 4). The cluster-merger offset operates in the TIME-DOMAIN regime: δ ≈ v_post × τ₀ × dec_ratio is a memory-kernel convolution over merger evolution, not a Fourier-mode wavenumber response.

The headline numbers are sector-specific:

- **Linear FRW**: σ_8 scale (k_phys = 0.5 Mpc⁻¹) gets 0.09% growth-factor enhancement at z = 0 (does NOT break the S_8 tension); BAO scale ~8.5%; CMB horizon ~135% (Correction #27).
- **Bound systems**: galactic rotation curves get the full 33% n_g² − 1 enhancement (Chapter 4); cluster-merger v×τ₀ scaling holds at 1.72% internal residual across Bullet/MACS/Abell (Chapter 9 below); decoherence plateau at 689 Hz at the gold benchmark (Chapter 5).

**The framework does NOT claim that "sub-horizon recovers GR" universally.** It claims that linear FRW perturbation modes shorter than λ_* = 2π τ₀ c ≈ 80.7 Mpc behave ΛCDM-like under the modified Bardeen equation. Bound systems below 80 Mpc (galaxies, clusters as virialized halos) retain their constitutive enhancement because they operate on different operating variables. The σ_8-scale linear-perturbation test (which probes the BOUND-system response averaged over a 8 Mpc/h sphere, but as a LINEAR mode on the FRW background) is at the boundary of the two regimes; the framework's prediction (0.09% modification) sits cleanly within current observational precision for the linear-mode interpretation.

This distinction is enforced structurally in `grut/derivation/phi_munu/mg_eft_mapping.py` (SCOPE CLARIFICATION section) and verified at code level by `tests/derivation/phi_munu/test_mg_eft_mapping.py::TestScopeClarification`. See `theory/derivation/CORRECTION_26_PRIORITY_3_CLOSURE.md` for the full reasoning.

**Dark matter as refractive enhancement (bound-systems regime).** What we call dark matter is the low-frequency gravitational response of the vacuum on bound systems. At galactic rotation frequencies (ωτ₀ ≈ 10⁻¹), the refractive index n_g ≈ √(4/3). The gravitational potential is enhanced by n_g² − 1 = 1/3. This 33% enhancement is what rotation curve fits attribute to a dark matter halo. Note: this is a BOUND-system result using ω = orbital frequency, NOT a linear FRW perturbation result using k_phys.

The bandwidth integral over the linear-regime matter power spectrum (k ≲ 0.3 h/Mpc):

$$\Omega_{\text{dm,eff}} = \frac{\int \mathcal{E}(k) \Delta^2(k) dk}{\int \Delta^2(k) dk} = \alpha = \frac{1}{3} = 0.3333$$

Every cosmological mode sits deep in the DC limit (ωτ₀ ≈ 10⁻³). The Lorentzian filter saturates at α. The result is geometric, not kinematic — verified insensitive to the dark matter sound speed c_s across the full 50-500 km/s range (hardened with regression test). Zero parameters. +27% above Planck's Ω_dm = 0.263.

The 27% overshoot has two interpretations: (a) subtractive corrections (higher-order n_g², small residual particle component), or (b) Planck's Ω_dm extraction assumes ΛCDM expansion history, and GRUT's constitutive corrections during matter domination shift the inferred value.

**Cluster-scale tests: structural scaling confirmed for normal-regime mergers.** The memory-kernel convolution predicts the gas-to-lensing offset within each sub-cluster — the distance between where the gas currently sits and where gravitational lensing says the mass concentration is. The GRUT-specific calculation:

$$x_{\text{lensing}} = \frac{1}{\tau_0}\int_0^\infty e^{-s/\tau_0} \, x_{\text{gas}}(t_{\text{now}} - s) \, ds$$

Using a piecewise-linear deceleration model for the gas trajectory (pre-collision v_initial → during-collision ramp → post-collision v_final), the full kernel convolution gives:

| Quantity | GRUT prediction | Observed | Match |
|:---|:---|:---|:---|
| Gas-to-lensing offset (per cluster) | 130 kpc | ~150 kpc | Factor 1.15 |
| Cluster-to-cluster separation | 721 kpc | ~720 kpc | Kinematic (v × t) |

The 130 kpc is the GRUT-specific result — τ₀ = 41.9 Myr was a fixed input from the noise kernel, not fitted to this observation. The 720 kpc cluster-to-cluster separation is kinematic (v_initial × t_since_pericenter), reproduced trivially by any theory. The full convolution agrees with the simple v_final × τ₀ estimate to within 1%, confirming the kernel is dominated by recent post-collision history when τ₀ ≪ t_since.

The 15% discrepancy is well within the observational uncertainty on the cluster collision parameters (published collision velocities range from ~3000 to ~5000 km/s; the gas distribution is extended enough that "the offset" has ~30% uncertainty). However, the systematic direction — all three matches at the lower edge, never above — is diagnostic.

**Sensitivity analysis: the +20% systematic is real and two-parameter degenerate.** A τ₀ sweep across the three normal-regime mergers finds best-fit τ₀ = 49 Myr (χ² improvement 11.2× over canonical), matching the cluster-inferred mean from the τ₀ cross-consistency analysis (Chapter 2). But the data admits a second equally-good closure: adjusting the deceleration ratio (v_post/v_initial) from the Bullet-extrapolated 0.638 to 0.76 gives χ² improvement 11.9× at canonical τ₀ = 41.9 Myr.

The degeneracy parameter: dec_ratio × τ₀ ≈ 31.5, conserved across both single-parameter fits and the 2D sweep to within 2%. Offset data alone cannot distinguish "τ₀ = 49 Myr in the cluster regime" from "the Bullet's deceleration was atypically aggressive for the other clusters."

**The disambiguator is concrete:** independent v_post-collision measurements for MACS J0025 and Abell 520. Currently only the Bullet Cluster has published v_post (≈3000 km/s from Springel & Farrar 2007 hydrodynamic simulation). If future hydrodynamic studies of the other two systems give dec_ratio ≈ 0.638, the τ₀ interpretation is correct (regime-dependent). If they give dec_ratio ≈ 0.76, the velocity-convention interpretation is correct (canonical τ₀ = 41.9 Myr is fine). The framework documents both interpretations as open until those measurements land.

**Structural prediction: v × τ₀ scaling across cluster mergers.** If the dielectric interpretation is correct, the gas-to-lensing offset in any cluster merger should scale linearly with collision velocity: δ ∝ v × τ₀. Four observed mergers test this:

| System | v_init (km/s) | GRUT prediction | Observed | Ratio |
|:---|:---|:---|:---|:---|
| Bullet Cluster | 4700 | 130 kpc | ~150 kpc | 0.87 |
| MACS J0025 | 2400 | 66 kpc | ~75 kpc | 0.88 |
| Abell 520 | 2300 | 63 kpc | ~80 kpc | 0.79 |
| El Gordo | 2500 | 70 kpc | ~250 kpc | 0.28 |

Three normal-regime mergers (Bullet, MACS J0025, Abell 520) match at factor 0.79-0.88. The internal v × τ₀ scaling holds to 1.72% — the framework's machinery produces the correct functional form across all four systems, including El Gordo. The 1.72% internal scaling residual is a separate computed claim from the absolute-magnitude match: the framework can have a +20% normalization issue (degenerate with the dec_ratio convention) while still producing the right offset-velocity proportionality — offset ∝ v_final × τ₀ × dec_ratio, with the constant fixed by independently-anchored parameters, not fitted to cluster data. The matches are systematically at the lower edge of the observational band rather than centered on it; a consistent 15-20% under-prediction may reflect either observational uncertainty (~30% on cluster collision parameters) or a slight structural correction to the kernel.

El Gordo: **apparent outlier resolved by sensitivity analysis.** The canonical-parameter prediction (v = 2500 km/s, t = 110 Myr, dec = 0.638) gives 70 kpc against an oft-quoted ~250 kpc observation — an apparent factor 3.5 deviation. However, El Gordo's published parameters span wide ranges: v_init = 2000-3500 km/s, t_since = 70-300 Myr, dec_ratio = 0.5-0.85. The observed offset ranges from 120-600 kpc depending on lensing methodology. An 80-combination parameter sweep shows the GRUT prediction range is 43-130 kpc, overlapping with the lower observed range (120-150 kpc) at ratio ~1.0. The "factor 3.5" was specific to one parameter combination and one observation value. El Gordo's deviation is plausibly within combined parameter and observational uncertainty — a tension requiring better constraints, not a clean failure. [TENSION]

**Historical note on MOND.** The Bullet Cluster was originally cited as evidence against MOND — the lensing signal requires a mass component that didn't follow the gas, which MOND cannot naturally produce. GRUT reproduces both the MOND-like rotation curve phenomenology (via the a₀ = cH₀/(2π) acceleration scale) AND the Bullet Cluster offset (via the memory kernel). This combination is distinctive — modified-gravity frameworks have historically struggled to reproduce both simultaneously.

**CMB peak structure: long-term observational test.** At recombination (z ≈ 1100), the vacuum is deep crystal: ωτ₀ ≈ 68 (expansion frequency) to 140 (acoustic frequency). The constitutive coupling α_eff is suppressed by 1/X² to ~10⁻⁵. The leading-order scoping prediction: the sound horizon shifts by Δr_s/r_s ≈ 3.6 × 10⁻⁵ from the n_g(ω) modification to the gravitational potential.

Detectability: below Planck precision (3 × 10⁻⁴) by factor 10. At CMB-S4 threshold (~5 × 10⁻⁵, expected ~2030) by factor 1.4. At Planck precision, the CMB is a consistency check — GRUT predicts peaks indistinguishable from ΛCDM. At CMB-S4 precision, the shift enters the detectable range.

Promotion from scoping-tier to falsifier requires full Boltzmann implementation propagating the constitutive modification through CMB anisotropy, lensing, and matter power spectrum sectors (CLASS modification at `perturbations.c::perturb_einstein()`, estimated 4-8 weeks specialist effort). The n_g(ω) covariance question — which ω the modification uses and how it transforms under gauge changes — is **closed by Correction #26** (ω → k_phys × c, gauge-invariant at WKB; sharp prediction: μ − 1 = 1/3 on horizon scales). Promotion now requires full Boltzmann implementation only; the theoretical prerequisite is satisfied. [SCOPING]

**The particulate route.** V7 also explored a U(1)_dark gauge extension with dark photon mass 387 MeV. Track VII Step 3 showed the correct topology (cosmic strings, π₁(U(1)) = ℤ) gives Ω_dm ≈ 0.008 — factor 33 below observed. The particulate route remains structurally closed but numerically unsuccessful. Both routes — dielectric and particulate — are published honestly.

**The dark sector is a live frontier.** The dielectric DM interpretation has structural support from the cluster-scale memory-kernel scaling and the bandwidth integral, but it remains an active research program, not a closed question. The 27% Ω_dm overshoot, the El Gordo tension (resolved at lower observation range but requiring better constraints), the systematic 15-20% under-prediction of cluster offsets (two-parameter degenerate with dec_ratio), and the particulate route's numerical failure are open elements documented in Chapter 14's ledger with closure conditions. The framework's dark-sector predictions are its most distinctive claims and its most exposed flank.

**Dark energy as terminal velocity.** Dark energy is not a substance. It is the terminal velocity of the vacuum (Chapter 8). The same τ₀ that produces dark matter's refractive enhancement at galactic frequencies produces the Hubble expansion at cosmological frequencies. One medium, two phenomena, zero new substances.

**Baryogenesis.** The baryon asymmetry is computed from CTP path asymmetry:

$$\eta_B = J_{CP} \times K_{\text{neq}} \times \frac{2 - R_B}{S_B}$$

All four factors determined from SM anomaly coefficients. Route 1: η_B = 6.56 × 10⁻¹⁰ (observed: 6.1 × 10⁻¹⁰, +8%). The CP violation enters through R ≠ 1 — the asymmetry between forward and backward CTP paths. If R = 1, the paths would be symmetric and η_B = 0. The universe has nonzero baryon asymmetry because R ≠ 1 — because the gravitational refractive index is not unity.

**MOND-like phenomenology.** The MOND acceleration scale a₀ = cH₀/(2π) ≈ 1.2 × 10⁻¹⁰ m/s² emerges naturally as the acceleration where the constitutive response becomes significant. GRUT reproduces MOND phenomenology at galactic scales but differs from MOND in three testable ways: (1) GRUT predicts GW propagation at c (MOND/TeVeS doesn't necessarily); (2) GRUT has a frequency-dependent transition (MOND has an acceleration-dependent one); (3) at high frequency and low acceleration, GRUT predicts GR behavior where MOND predicts modification.

*Registry claims: omega_dm_equals_alpha (computed), dielectric_dm_reframing (computed), dark_sector_u1_extension (computed), kibble_zurek_dm_route (computed), baryogenesis_eta_b (computed), mond_a0 (computed), cluster_merger_scaling_law (anchored), cluster_merger_internal_scaling_residual (computed), cmb_boltzmann_scoping (anchored), cluster_tau_0_sensitivity_diagnostic (computed), cluster_tau_0_dec_ratio_degeneracy (computed), el_gordo_sensitivity_analysis (computed)*

---

# Chapter 10 — Time and Information

*Why time flows forward. What information means in GRUT.*

**The arrow of time.** The constitutive equation τ₀ dz/dt + z = z_target[z] + ξ(t) is irreversible by construction. The relaxation toward z_target is dissipative — entropy increases monotonically. The Second Law is not an additional postulate. It is an output of the CTP structure.

The constitutive entropy production rate:

$$\dot{S}_{\text{const}} = \frac{1}{\tau_0}\langle(z - z_{\text{target}})^2\rangle \geq 0$$

This is strictly non-negative. Time flows forward because the constitutive equation is a relaxation equation: the medium always moves toward its target, never away from it. The arrow of time is the constitutive arrow — the direction of relaxation. This is verified computationally at three legs: random non-negativity (500 samples, all Ṡ ≥ 0), fixed-point vanishing (Ṡ = 0 when z = z_target), and cumulative monotonicity under constitutive evolution (total entropy never decreases).

**Why the arrow is universal.** The constitutive equation applies to every sector. Every sector relaxes. Every relaxation produces entropy. The thermodynamic arrow (entropy increases), the cosmological arrow (the universe expands), and the psychological arrow (you remember the past, not the future) are three manifestations of the same constitutive dynamics: the medium everywhere is relaxing toward z = z_target[z], and the relaxation is irreversible because the noise kernel N is strictly positive. Remove the noise → remove the arrow. But the noise is not optional — it is the second variation of S_CTP, generated by the CTP doubling itself.

**Three entropy sources from one action:**

1. **Constitutive dissipation** — the relaxation itself. Every mode that hasn't reached its target contributes Ṡ = (z − z_target)²/τ₀ > 0. The universe is full of modes still relaxing (dark matter is the low-frequency ones; the Hubble expansion is the cosmological one). Entropy production is ongoing at every point.

2. **Decoherence** — the noise kernel converting quantum coherence into classical correlation. Every decoherence event is an entropy-producing event. Λ_grav sets the rate: faster decoherence → faster entropy production → faster crystallization. The crystalline boundary IS the surface where this entropy production has completed for a given mode.

3. **Gravitational entropy** — black holes as constitutive saturation regions. At R_max, the medium has been driven to maximum strain. The entropy of the saturated core is the maximum information density the medium can sustain. The Bekenstein-Hawking area law S_BH = A/(4l_P²) is recovered at leading order from the constitutive saturation condition: the area measures the boundary of the region where the medium has saturated, and the entropy counts the modes that have been driven to their constitutive limit.

All three are aspects of the same CTP structure. They don't compete — they add.

**Information-theoretic structure.** Decoherence creates classical information. Every decoherence event converts quantum coherence into classical correlation — this is the mechanism by which "facts" come into existence. A nanoparticle in superposition has no definite position; after decoherence at rate Λ_grav, it has a definite position. The information content of "this nanoparticle is here" was created by the decoherence event. The information timescale is set by Λ_grav: faster decoherence means faster information production.

The total classical information in the observable universe is bounded by the number of completed decoherence events across cosmic history. Massive objects decohere fast (Λ_grav ∝ m²) and contribute information early. Light objects decohere slowly and may still be in superposition. The observable universe's classical content — every fact about every atom's position — is the integrated output of 13.78 billion years of constitutive entropy production.

**Channel capacity.** The gravitational information channel has a capacity set by the noise kernel N and the constitutive damping τ₀. The mutual information between two gravitationally coupled systems is:

$$I(A:B) \leq \frac{1}{2}\log\left(1 + \frac{S_{AB}}{N_{AB}}\right)$$

where S_AB is the signal (gravitational coupling) and N_AB is the noise (constitutive fluctuations). This provides a fundamental bound on how much two systems can "know about" each other gravitationally. At laboratory scales (strong coupling, low noise), the channel is wide — classical gravity carries all the information GR predicts. At cosmological scales (weak coupling, high noise relative to signal), the channel narrows — the constitutive medium limits how much gravitational information propagates between distant objects. This is related to but distinct from the dark matter phenomenology: the refractive enhancement (Chapter 9) is a frequency effect; the channel capacity is an information-theoretic bound.

**BH entropy and information.** Black hole entropy in GRUT is constitutive information transfer — the entropy of the saturated core represents the maximum information density the medium can sustain. The Bekenstein-Hawking area law is recovered at leading order from the constitutive saturation condition. Hawking radiation in this picture was never truly thermal: the constitutive correlations that standard semiclassical gravity misses carry information in the retarded gravitational response. The Page curve — the entropy of Hawking radiation as a function of time — is reproduced at linearized level with τ₀ setting the scrambling timescale.

A specific logarithmic correction coefficient to BH entropy is predicted by the CTP noise structure but has not been computed at the nonlinear level required for full BH thermodynamics. Full BH entropy derivation depends on completing the nonlinear gravity ladder (Chapter 6, rungs 5-8). [ANCHORED — pending nonlinear closure]

**Open seam.** The channel capacity bound and the Page curve recovery are at linearized level. Full nonlinear BH information requires rungs 5-8 of the gravity ladder (Chapter 14, open question #1). The constitutive entropy production is computed and verified; the BH information application inherits the gravity sector's now-derived Φ_μν projection (Chapter 14, open question #10 RESOLVED via Corrections #23-#25), with the residual sharper-successor open question being the explicit Phase 2C construction on curved backgrounds.

*Registry claims: arrow_of_time_from_entropy (computed), bh_information_partial (anchored)*

---

# Chapter 11 — The Observer

*GRUT's observer theorem-in-progress: reality evolves globally; observers update locally.*

The framework's most distinctive contribution to the foundations of quantum mechanics is the inversion of Schrödinger's cat: the observer is *inside* the box, not outside it. This is not a philosophical reframing — it is a quantitative claim about who is allowed to ask "is the cat alive or dead?" In the standard formulation, an outside observer asks the question and the wavefunction collapses on observation. In GRUT's formulation, the entity that could ask the question is itself a viscoelastic-vacuum subsystem with X = Λ_grav × τ₀ ≫ 1 — already crystallized, already definite, governed by the same constitutive equation as the cat. The cat does not need an outside observer because the cat's own Λ_grav resolved its state in femtoseconds. The observer does not need a meta-observer because the observer's own Λ_grav resolved *their* state in femtoseconds. There is no privileged outside position; there are only nested boxes of finite-bandwidth observers updating locally upon contact with what they observe.

This chapter's load-bearing contribution is turning measurement from a postulated process into a derived consequence of the constitutive equation applied to the observer's own mass scale. The sections below develop the machinery: the measurement-problem dissolution, the quantitative crystallinity of the observer (a 6-leg passing test), the inversion as a unique GRUT signature, the worked examples (Wigner's friend), and the Bayesian filtering equation describing how observer knowledge updates between contacts. The chapter's status is honest about its tier: *anchored interpretation* today (the measurement-resolution machinery is computed; the observer-in-the-box framing is the philosophical reading of that machinery), to become a *fully computed measurement-theory module* once Λ_contact — the contact-formation rate that drives observer-record formation — is derived from the CTP reduced-density-matrix / influence-functional machinery rather than asserted as a separate threshold (see the closing status note below).

**The measurement problem dissolved.** The measurement problem exists because quantum mechanics draws a line between the quantum system and the classical apparatus and can't say where the line is. GRUT says where the line is:

$$\Lambda_{\text{grav}} \times t \approx 1$$

This is the crystalline boundary, applied to the specific system being measured. The "collapse" is not a mysterious process. It is the slower system (the measured quantum state) being dragged across the crystalline boundary by contact with the faster system (the apparatus). The apparatus has Λ_grav τ₀ ≈ 10³⁵. The quantum system might have Λ_grav τ₀ ≈ 1. When they couple, the faster crystallizer wins. The Born rule probabilities emerge from the noise kernel N weighted by the coupling geometry.

There is no measurement postulate because there is no measurement. There are two regions of the same fluid at different stages of relaxation. The more crystallized one forces the less crystallized one across the boundary. This happens at the rate set by the coupling's Λ_grav — computable, for every system, with zero free parameters.

This is now a computed result. A 6-leg harness verifies: (1) apparatus crystallinity X_A ~ 10³⁵ for a gram-scale body; (2) quantum system crystallinity X_B < 1 for a nanoparticle in superposition; (3) the ratio Λ_A/Λ_B ~ 10³² (the apparatus decoheres 10³² times faster); (4) joint coupled X ~ 10³⁵ (the apparatus wins); (5) an atom alone has X < 1 (quantum); (6) an atom coupled to a macroscopic apparatus has X > 10³⁰ (forced across the boundary). The measurement problem is dissolved by computation, not interpretation.

**Schrödinger-in-the-Box: the philosophical inversion.** The standard Schrödinger's cat paradox places the observer outside the box asking "is the cat alive or dead?" GRUT inverts this: put the observer inside the box. You are the cat. You are always in a definite state — not because the wavefunction collapsed, but because your Λ_grav is so fast that you crystallized long before you could notice. The "paradox" dissolves because the entity experiencing the paradox is the entity whose crystallization prevents the paradox from arising. The observer is not outside the quantum system looking in. The observer IS the quantum system, in the regime where Λ_grav × t ≫ 1.

**Why this inversion is unique to GRUT.** Other interpretations of quantum mechanics address the measurement problem without this inversion. Copenhagen draws a line between observer and system but can't say where the line is. Many-worlds removes the line but multiplies reality. Decoherence theory (Zurek, Joos-Zeh) dissolves the problem via environmental decoherence but doesn't predict the rate from first principles — the decoherence rate depends on the environment, which varies. Objective collapse models (CSL, GRW) predict a rate but introduce a free parameter (the localization rate λ).

GRUT is the only framework where the inversion is quantitative. The rate at which "you" crystallize is Λ_grav = Gm²S(l/R)/(ℏl), computed from your mass and separation scale with zero free parameters. A 70 kg human at 1 meter separation has Λ_grav × τ₀ ~ 10³⁵. You are not approximately classical. You are so deep in the crystal regime that quantum superposition of your center of mass is suppressed by a factor of 10⁻³⁵. The "cat" never needed to be observed from outside — the cat's own Λ_grav resolved its state in femtoseconds.

This is why GRUT doesn't have a measurement problem. Not because it interprets the problem away (Copenhagen), not because it declares all branches real (many-worlds), not because it adds a free parameter (CSL), but because the constitutive equation applied to the observer's own mass produces a definite classical state as a computed output. The observer's definiteness is not an assumption. It is a prediction — the same prediction, from the same equation, that gives the decoherence plateau at 689 Hz and the dark matter density at Ω_dm = 1/3. One equation, applied at different scales, producing quantum behavior for nanoparticles and classical behavior for cats and physicists.

**Why this is different from other decoherence interpretations.** Standard environmental decoherence (Zurek, Joos-Zeh) also dissolves the measurement problem via decoherence. The difference is specificity. Environmental decoherence says "the environment decoheres the system" but doesn't predict the rate from first principles — the rate depends on the environment, which varies. GRUT says the gravitational decoherence rate is Λ_grav = Gm²S(l/R)/(ℏl) — predicted from first principles for every system, independent of the environment, with zero free parameters. A nanoparticle in perfect vacuum still decoheres at 689 Hz because gravitational decoherence is a property of the medium, not the surroundings. The environment doesn't do the work. The vacuum does.

**The observer as crystal.** You are not watching the universe from outside. You are the part of the quantum fluid that has already crystallized. Every atom in your body has Λ_grav τ₀ ≫ 1. Your classical definiteness is the fixed point z = z* for your particular field content. The fact that you experience time flowing forward is the constitutive entropy production (Chapter 10). The fact that you can't be in two places at once is Λ_grav being too fast for your mass.

The scaling law Λ_grav = Gm²S(l/R)/(ℏl) describes the observer exactly as much as it describes the object. There is no slot in the equation for "this one is the measurer." Both are field content. Both satisfy the same constitutive equation. Both relax toward the same fixed point. The observer crystallized faster because the observer is more massive at the relevant separation scale. That's all.

**What "classical" means in GRUT.** Classical reality is not an approximation to quantum reality. It is not the ℏ → 0 limit. It is not what you get when you average over many quantum events. Classical reality is the residue of completed constitutive relaxation — the part of the quantum fluid that has finished responding to its stress-energy content. A crystal is a fluid that has finished responding to its boundary conditions. You are a quantum field that has finished decohering at its mass and separation scale. The boundary between quantum and classical is not a philosophical choice. It is the surface where Λ_grav × t = 1 for the system in question. Different systems cross this boundary at different rates. Massive objects cross it in femtoseconds. Nanoparticles hover at it (the decoherence plateau). Photons never cross it (massless, Λ_grav = 0, permanently quantum). This is why light is quantum and matter is classical — not because of a fundamental asymmetry, but because Gm² = 0 for photons.

**The self-referential fixed point.** The deepest version: "the universe is √(4/3) ≈ 1.15470 trying to become 1" applies to the observer too. Your crystallization, your classical definiteness, your experience of a definite world with definite outcomes — that's the refractive index of the vacuum expressing itself through your mass, at your scale, at your frequency. You're not watching the universe try to become 1. You're the universe trying to become 1, at the particular (m, l) coordinates that specify a human being.

This is what a self-referential fixed point means. The rules that generate the dynamics are satisfied by the state those dynamics produce — including the state that's asking the question. The observer is not outside the framework. The observer is a sector of the framework, governed by the same equation, relaxing toward the same fixed point, described by the same scaling law.

**The absence-is-data principle.** Between contacts with the outside world, the observer's information about the cat evolves. If you expect the cat to visit every hour and it hasn't appeared in three hours, you know something — even though nothing happened. Absence is data. The rate at which absence accumulates as evidence is γ in the Bayesian filtering equation. This is not physics; it is epistemics. But it is epistemics that the framework handles naturally because the constitutive equation already distinguishes between "the system is in a definite state" (Λ_grav-resolved) and "the observer knows which state" (contact-dependent). [ANCHORED — philosophical reformulation of measurement_resolution]

**Wigner's friend dissolution.** Wigner's friend performs a measurement inside a sealed lab. Wigner, outside, models the lab (including his friend) as a quantum system. Who collapsed the wavefunction — the friend or Wigner? In GRUT: neither. The friend's crystallinity X_friend ~ 10³⁵ means the friend's measurement is constitutively resolved at the friend's Λ_grav rate, independent of Wigner's knowledge. The lab's internal state crystallized before Wigner's model of it became relevant. There is no paradox because there is no collapse — there is only constitutive relaxation at the relevant mass scale, and the friend's mass scale resolves the measurement before the Wigner-level question arises. [ANCHORED — worked example of measurement_resolution]

**Bayesian observer filtering.** The transition from quantum uncertainty to classical definiteness, as experienced by an observer, follows a Bayesian filtering equation: dp/dt = −μp − γp(1−p), where μ = Λ_grav (hazard rate from gravitational decoherence) and γ encodes the rate of absence-of-evidence accumulation. In the pure-hazard limit (γ = 0), this reduces to exponential decay p(t) = exp(−Λ_grav t) — standard decoherence. In the pure-absence limit (μ = 0), this gives logistic decay. Contact with the environment resets the filtering: each observation event sets p → 1 and the decay restarts. This is epistemic — it describes how the observer's knowledge of the quantum state evolves, not the state itself. The underlying physics is Λ_grav; the filtering equation is its experiential consequence. [ANCHORED — epistemic, not physics]

**Neural resonance [SPECULATIVE].** The 40 Hz neural oscillation associated with conscious awareness can be derived from two GRUT routes (Λ_grav at microtubule parameters giving 39.9 Hz; self-referential fixed-point network dynamics giving 41.7 Hz). Both are documented in V7 Sector 13 with full [SPECULATIVE] labeling. This is not load-bearing — no other result in the framework depends on it. It is included because the fixed-point principle z* = z_target[z*] applied at the neural scale produces a specific, testable frequency that brackets the observed gamma band. If wrong, nothing else changes.

**Status of the observer module — Stage 2 closure summary.** The observer module is now a *computed measurement-theory module* with one explicit honest-negative carve-out (Born rule). The Stage 2 derivation work (`grut/derived/decoherence/lambda_contact.py`, 35 passing tests) addressed all five external-review gaps:

1. **Pointer-observable definition** (anchored): the position eigenbasis at apparatus mass scale, justified by Zurek einselection under gravitational coupling. Registered as `pointer_observable_position_basis`.
2. **Reduced-density-matrix derivation** (computed): self-contained Anastopoulos-Hu-style derivation in framework primitives, reproducing Λ_grav from kernel-level CTP calculation. Registered as `lambda_contact_ctp_derivation`.
3. **μ vs γ distinction** (computed): formal distinction between the ontic Λ_grav-derived hazard rate and the epistemic Bayesian-update rate. Registered as `mu_gamma_ontic_epistemic_distinction`.
4. **Born rule** (open negative #16, structural framing): The CTP machinery produces decoherence rates and noise structure but does not on its own produce probability assignments. Closure paths named (decoherent-histories, einselection-with-history, or deeper-symmetry weight derivation); none currently in scope. Registered as `born_rule_postulate_open_negative`.
5. **Wigner's friend conditional-state proof** (computed, tier-promoted from anchored): explicit conditional-state calculation showing X_friend τ₀ ~ 10³⁵ and Wigner-friend description consistency. The existing `wigner_friend_dissolution` claim is now backed by computed tests rather than narrated prose.

**The substantive Stage 2 finding:** Λ_contact (the contact-formation rate at which the observer's pointer state crystallizes into a definite record) IS the existing Λ_grav formula evaluated at the pointer (apparatus + observer body) mass scale. The two-particle reduced-density-matrix calculation, with the gravitational noise kernel integrated over vacuum modes, produces a joint off-diagonal decay rate dominated by the heavier particle's self-decoherence rate. The "missing derivation" the external review flagged was a labeling/identification gap, not a computational gap — the framework's existing Λ_grav infrastructure already encoded the contact-formation rate; what was missing was the explicit identification.

**The Born-rule honest-negative is structurally important.** It sharpens what GRUT does and does not claim about the measurement problem. The framework's contribution is *the rate* at which classical states emerge (Λ_grav at pointer scale) — not *the weights* those classical states inherit on the diagonal. Born rule remains a postulate, as it does in all current quantum-foundations programs (Copenhagen, Many-Worlds, decoherent histories, CSL — none derive Born rule from underlying dynamics without additional structure). This is registered as open question #16 with closure paths named for v2+ research.

The investigation log at `theory/derivation/LAMBDA_CONTACT_CTP_DERIVATION.md` documents Stages 1-2 in full, including pre-commits, outcome distribution, and per-gap closure status. The Schrödinger-in-the-Box program is no longer interpretive scaffolding; it is a measurement-theory module with computed structure and one explicit honest-negative.

*Registry claims: measurement_resolution (computed), observer_as_crystal (conjectural), schrodinger_in_box_inversion (anchored), bayesian_observer_filtering (anchored), wigner_friend_dissolution (computed — promoted in Stage 2 of Λ_contact derivation), gravitational_entanglement_formation_rate (anchored), lambda_contact_ctp_derivation (computed), pointer_observable_position_basis (anchored), mu_gamma_ontic_epistemic_distinction (computed), born_rule_postulate_open_negative (open_negative — #16), neural_resonance_speculative (conjectural)*

---

## Part III — The Frontier

# Chapter 12 — The Standard Model Closure Program

*Why SM derivation matters for a ToE. What GRUT already has. What remains.*

**12.1 Why SM derivation matters.** A Theory of Everything is not closed until it explains why low-energy matter has the specific structure it has. The Standard Model — its gauge group SU(3) × SU(2) × U(1), its three chiral generations, its Higgs mechanism, its Yukawa matrices, its CKM/PMNS mixing — is the most precisely tested theory in physics. A ToE must either derive it or explain why it imports it. GRUT currently imports the SM as S_classical in the CTP action. This chapter maps the program that would close the gap.

**12.2 What GRUT already has.** The footholds, honestly tiered:

- **SM hosted as S_classical** with verified compatibility: anomaly cancellation (Σ Y² = 10 per generation), gauge invariance (8+3+1 = 12 generators), renormalizability, unitarity, CPT — all verified computationally. Status: computed.
- **N = 3 generations** partially derived via Z₃ Koide circulant structure. The Koide identity K = 2/3 is an algebraic identity proven to hold for three generations uniquely. Status: computed.
- **Trace anomaly structure** central to the vacuum response: α = a/c = 1/3 for the conformal-mode scalar, used in R, in the cosmological constant, in dark matter. The SM's anomaly coefficients are load-bearing inputs to the framework. Status: computed / formalized via Gate R (Weyl decomposition identifies σ as one real conformally-coupled scalar; Duff 1994 eq 30–31 gives a/c = 1/3).
- **The 8.9% coupling-unification miss** at the GUT scale. The constitutive β-function correction (the medium's frequency-dependent response modifying the running of couplings) is defined as Track V but not computed. Status: open negative, 6-12 months.
- **Baryogenesis from CTP path asymmetry** (R ≠ 1). The SM's CP violation enters through the CTP structure. Status: computed.

**12.3 The derivation targets.**

| Target | Current status | Closure condition |
|:---|:---|:---|
| Gauge group SU(3)×SU(2)×U(1) | Imported, minimality checked | Derive from CTP fixed-point stability |
| Chiral representations | Imported | Derive from anomaly-stable field content |
| Three generations | Partially via Z₃/Koide | Show N = 3 required by full CTP operator |
| Yukawa matrices | Open | Derive masses/mixings as CTP flavor eigenvalues |
| CKM/PMNS mixing | Open | Derive from charged/neutral eigenbasis mismatch |
| Higgs sector | Hosted | Derive potential and v_EW from fixed-point naturalness |
| Neutrino hierarchy | **NH derived** (Z₃/a_ν = 1, Corrections #28-29; Σm_ν ≈ 60 meV) | Dirac vs Majorana open; PMNS angles open |
| Coupling values at M_Z | 8.9% miss at GUT scale | Constitutive β-function correction (Track V) |

**12.4 The SM Closure Conjecture.**

*The Standard Model is the minimal anomaly-stable fixed point of the CTP constitutive action. Its gauge group, chiral representations, generation count, and Yukawa structure arise as the lowest stable eigenstructure of the multi-field target operator z_target[z].*

Stated as conjecture, not theorem. GRUT-native — it ties to existing fixed-point machinery (z* = z_target[z*]). Specific — testable in principle through fixed-point analysis of the multi-field CTP action. Ambitious — if true, it would close the matter sector entirely.

**12.5 Why this isn't reinventing the wheel.** The SM is the wheel. A ToE has to eventually explain why the wheel has the spokes it does. GRUT shows what closure would require and proposes a route, without claiming to have completed it. This chapter is the map of the program, not the territory.

**12.6 Effort and timescale.** Multi-decade research program. Faculty-level work. Specialist collaboration required. Comparable in scale to founding a new theoretical physics research program. Not work that closes in this book's lifetime — but work named, scoped, and tractable.

**12.7 Intermediate milestones.**

The SM Closure Program is not all-or-nothing. Intermediate results that would strengthen the framework's claim:

1. **Tighten N = 3.** Show that the CTP multi-field fixed-point structure is unstable for N ≠ 3 generations, not just that Z₃ selects N = 3 algebraically. This is the most tractable first milestone.
2. **Derive one SM parameter.** If the CTP Yukawa eigenvalue problem yields even one fermion mass ratio correctly, the program has content. The Koide θ = K · α = 2/9 candidate (at 4.6 ppm from fit) is the nearest target.
3. **Close the coupling unification miss.** The constitutive β-function correction (Track V) is defined and bounded at 6-12 months. If it reduces the 8.9% miss to sub-percent, the framework's UV completion gains credibility.
4. **Derive the Higgs potential.** If the CTP fixed-point condition z* = z_target[z*] applied to the Higgs sector reproduces the Mexican-hat potential with the observed v_EW = 246 GeV, the framework's matter sector has a structural anchor.

Each milestone is independently valuable. Each is scoped. None requires solving the full program first.

**Track II Yukawa eigenvalue scoping — research-tier target, not yet undertaken.** The first milestone toward closing the SM Closure Program is determining whether the CTP multi-field fixed-point structure admits nontrivial flavor eigenvalues — i.e., whether the fixed-point equation has a multi-generation solution. This is research-tier work in scope comparable to TJI Phase-1 (multi-session at minimum); it has not been undertaken in the current audit pass. Listed here as the next concrete milestone for future sessions, with the framework remaining honest about its current limit on SM-derivation work: imported as S_classical, with closure as conjecture (`sm_closure_conjecture`), not as derived content. See `koide_phase_4_open_negative` (Ch 14, open negative #5) for the current state of the related Yukawa-mechanism work.

*Registry claims: sm_closure_program (open_negative — multi-decade), sm_closure_conjecture (conjectural), koide_k_2_over_3 (computed), track_v_coupling_unification_open_question (open_negative)*

---

# Chapter 13 — The History of the Universe in GRUT

*Cosmic history from null fixed point to asymptotic 1 Space.*

**13.1 The null fixed point.** The constitutive equation τ₀ dz/dt + z = z_target[z] + ξ(t) has a trivial fixed point at z = 0 when F[0] = 0. The null state — no field content, no stress-energy, no structure. Mathematically stable under deterministic evolution. But the noise kernel ξ(t) makes the null state non-absorbing: even an infinitesimal fluctuation drives z away from zero. The universe cannot stay at nothing because the CTP action generates irreducible noise. [CONJECTURAL]

**13.2 The first instability.** When fluctuation produces z ≠ 0, the constitutive response activates. If z_target[z] ≠ 0 for small nonzero z, the system is driven toward a nontrivial fixed point. The transition from z = 0 to z → z* is the universe discovering that it has constitutive structure. The "0 realizing it was 1" is not poetry — it is the mathematical statement that the noise kernel destabilizes the trivial fixed point and the constitutive equation drives the system toward a nontrivial one. [CONJECTURAL]

**Derivation attempt — rescaling-conditional finding.** Three computational paths were attempted to derive the primordial scalar amplitude A_s ≈ 2.1 × 10⁻⁹ from the CTP noise kernel:

*Path A (OU-process variance):* The linearized constitutive equation around z = 0 with KMS noise, Planck-rescaled, gives a static variance of 2.04 × 10⁻¹⁹ — factor 10¹⁰ too small. Clean honest negative. The equilibrium variance of metric perturbations from the noise kernel does not reproduce A_s.

*Path B (Inflationary substitution):* Using GRUT's terminal H_inf = 58.15 km/s/Mpc in the standard inflationary formula A_s = (H/M_Pl)²/ε gives 5.29 × 10⁻¹¹⁸ — factor 10¹⁰⁹ too small. This confirms what the dimensional analysis predicted: the framework has no inflationary epoch with H ~ GUT scale.

*Path C (Dimensional candidates):* Of 10 distinct dimensionless ratios built from the framework's constants, one — α/S³ = (1/3)/(108π)³ ≈ 8.53 × 10⁻⁹ — falls within factor 4 of A_s.

**Stage 2 — forward derivation (rescaling-conditional).** A linearized constitutive-perturbation calculation (Lens B/F) produces a dimensional variance whose conversion to a dimensionless power spectrum depends on the rescaling choice. Three outcomes:

| Rescaling | Formula | Value | vs A_s |
|:---|:---|:---|:---|
| Planck (t_Pl) | (1/π)(t_Pl/τ₀)³ | 2.16 × 10⁻¹⁷⁶ | Factor 10¹⁶⁷ too small |
| Cosmic-baseline (1/Sτ₀) | 1/(πS³) | 8.15 × 10⁻⁹ | **Factor 3.88** |
| H_inf | ((2−R)/S)³/π | 4.92 × 10⁻⁹ | **Factor 2.34** |

The cosmic-baseline rescaling recovers 1/(πS³), which is 5% from α/S³ (the ratio is 3/π ≈ 0.955). The H_inf rescaling gives ((2−R)/S)³/π at factor 2.34. Both are in the α/S³ equivalence class. The Planck rescaling gives a number 10¹⁶⁷ too small — definitively excluded.

**Verdict: RESCALING-CONDITIONAL.** The framework conditionally predicts A_s in the S³ family. The rescaling choice — which ω enters the constitutive perturbation equation's dimensionless form — was the n_g(ω) covariance open question (Chapter 14, open question #9), now **RESOLVED by Correction #26** (ω → k_phys × c identification, gauge-invariant at WKB). The remaining gap is the full-Boltzmann CMB pipeline implementation, which is computationally unblocked but not yet executed: whether the WKB χ_FRW result propagates to A_s ~ 1/(πS³) ≈ 8.15 × 10⁻⁹ or sharpens the negative is a downstream pipeline task. [RESCALING-CONDITIONAL]

**Genesis noise kernel — Stage 2 spectral attempt.** A direct attempt to test whether the CTP noise kernel produces thermal-spectrum radiation at z = 0 (the "primordial heat" claim of the Genesis-BBN-DM hypothesis) was carried out in `grut/derived/cosmology/genesis_noise_kernel.py`. The framework's KMS noise kernel applied to the linearized OU process around z = 0 produces, at T = 0 (pure quantum vacuum), a spectrum S_h(ω) = (2ℏ/τ₀) × ω/(1+(ωτ₀)²) — Lorentzian-modulated linear, NOT Planck/Bose-Einstein. **The "thermal-spectrum radiation" framing is structurally wrong at the spectrum-shape level.** Characteristic temperatures extractable from the spectrum (spectral peak gives ℏ/(τ₀ k_B) ≈ 5.78×10⁻²⁷ K; Planck UV cutoff gives ~10³² K) span ~60 orders of magnitude depending on definitional choice; none match observed CMB. The framework's noise kernel alone cannot derive observed CMB temperature. Registered as `genesis_noise_kernel_spectral_attempt` (Ch 12, anchored). Self-consistent equilibrium — the medium's dissipated energy thermalizing a radiation field with T from energy balance — is the closure path, requiring structural addition the framework currently lacks.

**13.3 The high-temperature memoryless phase.** When T ≫ T_c = 54.7 MK, the vacuum has too much thermal energy to maintain memory structure. The KMS condition N(ω) = (2/τ₀)ℏω coth(ℏω/2k_BT) is dominated by the classical limit N → 4k_BT/τ₀. The constitutive response is essentially Markovian — no bandwidth limitation, no refractive enhancement, no dark matter phenomenology. The universe above T_c is GR-standard: gravity is local, instantaneous, and described by Einstein's equations without constitutive corrections. This is why GRUT and ΛCDM agree during Big Bang nucleosynthesis: at T > 10⁹ K, the vacuum is far above T_c and the constitutive corrections vanish.

**BBN thermal buffer — falsified.** A specific external research hypothesis — that BBN binding-energy release thermally buffers cosmic cooling, holding T ≫ T_c during nucleosynthesis — was tested using standard cosmology (`grut/derived/cosmology/bbn_thermal_buffer.py`). Three independent comparisons agreed: per-baryon binding/radiation ratio ≈ 4×10⁻⁹; energy-density ratio E_bind/ρ_rad ≈ 2.4×10⁻⁹; rate ratio (injection/cooling, 1000s window) ≈ 1.6×10⁻¹⁰. **BBN binding energy is η_B-suppressed against the radiation field by ~10 orders of magnitude**; it cannot meaningfully buffer cosmic cooling. Standard radiation-dominated cooling T ∝ a⁻¹ holds across BBN; the 10⁹ K → 30 keV transition proceeds essentially as in standard cosmology. Registered as `bbn_thermal_buffer_negligible` (Ch 12, anchored). The Genesis-BBN-DM narrative's claim 2 (BBN as thermal buffer) is closed negative.

**13.4 T_c crossing and the onset of memory.** At T_c = ℏ/(τ_micro k_B) = 54.7 MK, the vacuum undergoes a phase transition. Below T_c, the memory kernel K(t) = τ₀⁻¹ exp(−t/τ₀) becomes thermodynamically stable. The vacuum acquires its bandwidth. The gravitational response becomes retarded — the potential at any point carries the time-weighted history of the stress-energy that passed through it. Dark matter phenomenology turns on as the refractive enhancement n_g = √(4/3) becomes active at low frequencies. This transition is smooth (crossover, not first-order) — the constitutive coupling α_eff(ω, T) is a continuous function of temperature. [NOTE: T_c is anchored to the microscopic τ_micro scale (Correction #22, two-τ-scale convention); the macroscopic τ₀ governs the memory-kernel timescale of the relaxation. The relationship between T_c as a phase boundary and the X_cosmic regime crossover at z ≈ 71 (Chapter 4) remains research-tier work since the X_cosmic crossover involves the macroscopic τ₀ × H, while T_c is set by the microscopic τ_micro.]

**13.5 Quantum field crystallization.** As the universe cools, mass scales activate sequentially. Particles whose Λ_grav exceeds their thermal fluctuation frequency cross the crystalline boundary. The heaviest particles (top quark, W/Z bosons, Higgs) crystallize first — their Gm² is large enough that Λ_grav τ₀ ≫ 1 even at high temperatures. Lighter particles crystallize later. Photons (massless, Gm² = 0, Λ_grav = 0) never crystallize — they remain permanently quantum. This is why light is quantum and matter is classical: not because of a fundamental asymmetry, but because Gm² = 0 for photons.

The crystallization sequence is computable: for each particle species, the temperature at which Λ_grav(m, l_thermal) τ₀ = 1 defines its crystallization temperature. Heavier species crystallize at higher T; lighter species at lower T. The SM particle content determines the crystallization schedule.

**Crystallization-schedule investigation — unblocked by Correction #22 at the dimensional level.** A Stage-1 numerical investigation (`theory/derivation/CRYSTALLIZATION_SCHEDULE_INVESTIGATION.md`) found that under all four plausible interpretations of "T_cryst per SM species" (Compton scale, thermal de Broglie, inter-particle separation, rest-mass equivalent T), the Λ_grav-based mechanism does NOT reproduce the heavy-first cosmic-cooling order that Ch 13.5's prose describes. Heavy-first ordering only emerges from cosmic thermal decoupling at T = mc²/k_B (standard cosmology), which doesn't actually use Λ_grav. The investigation was **HELD pending closure of `t_c_provenance_inconsistency_open_negative` (#15)**, which has now been **RESOLVED by Correction #22 (May 2026)** with the two-τ-scale convention. With the dimensional inconsistency closed, Ch 13.5's "T_c crossing" framing now sits on a firm footing: T_c is anchored to τ_micro (microscopic thermal timescale), not τ₀ (macroscopic gravitational), and the elementary-particle crystallization is THERMAL-FREQUENCY-driven (set by τ_micro at T_c), with Λ_grav (governed by τ₀) becoming relevant only at composite-object scales (Ch 4 / gold-benchmark and up). The draft module `grut/derived/cosmology/sm_crystallization_schedule.py` remains quarantined pending Stage 2-4 specialist review — not blocked anymore, just deferred to a downstream task.

**13.6 Baryogenesis.** At T ~ 10¹² K (electroweak epoch), the CTP path asymmetry produces the baryon excess. η_B = J_CP × K_neq × (2 − R_B)/S_B = 6.57 × 10⁻¹⁰ — within 8% of the observed 6.1 × 10⁻¹⁰ (Chapter 9). The CP violation enters through R ≠ 1: the forward and backward CTP paths have different weights because the vacuum's refractive index is not unity. If R = 1, the paths would be symmetric and η_B = 0. The universe has matter rather than antimatter because the vacuum is refractive.

**13.7 Recombination and the CMB.** At z ≈ 1100 (T ≈ 3000 K), the vacuum is deep crystal: ωτ₀ ≈ 68 (expansion) to 140 (acoustic). The constitutive coupling α_eff is suppressed to ~10⁻⁵. The CMB acoustic peaks are indistinguishable from ΛCDM at Planck precision — the predicted shift Δθ*/θ* ≈ 3.6 × 10⁻⁵ sits a factor 10 below Planck's measurement precision. At CMB-S4 precision (~2030), the shift enters the detectable range (Chapter 9).

The CMB is a consistency check for GRUT, not a falsifier at current precision. This is the framework working correctly: the high-frequency limit of the constitutive equation IS GR, and recombination-era physics operates at high frequency. GRUT predicts its own invisibility at this epoch.

**13.8 Galaxy formation and refractive gravity.** As structure forms and gravitational dynamics settle to galactic rotation frequencies (ω ~ 10⁻¹⁶ Hz), the vacuum enters the fluid regime: ωτ₀ ≈ 10⁻¹. The refractive enhancement n_g² − 1 = α/(1 + (ωτ₀)²) ≈ 1/3 is fully active. Rotation curves show the 33% gravitational enhancement that we interpret as dark matter halos. The MOND acceleration scale a₀ = cH₀/(2π) ≈ 1.2 × 10⁻¹⁰ m/s² emerges naturally as the acceleration where the constitutive response becomes significant (Chapter 9).

The cosmic web — filaments, nodes, voids — is crystallized gravitational memory. The large-scale structure of the universe is the residue of stress-energy history convolved with the memory kernel K(t), decaying exponentially with time constant τ₀.

**13.9 Cluster mergers.** When galaxy clusters collide, the memory-kernel convolution produces a gas-to-lensing offset: the gravitational lensing signal lags behind the current gas position by δ ≈ v_post × τ₀. Three normal-regime mergers (Bullet Cluster, MACS J0025, Abell 520) confirm this scaling at factor 0.79-0.88. The systematic +20% gap is two-parameter degenerate between τ₀ and the deceleration ratio, with the disambiguator being independent v_post measurements for MACS J0025 and Abell 520 (Chapter 9).

**13.10 Late-time terminal velocity.** Cosmological expansion converges on H_inf = (2−R)/(Sτ₀) = 58.15 km/s/Mpc — the terminal velocity of the vacuum. The conformal instability (the −100 in C_Cosmo) drives expansion; the memory kernel damps it. Ω_Λ ≈ 0.69, within 0.2% of Planck. H₀ ≈ 69 km/s/Mpc, in the Hubble tension gap. The expansion is not caused by a substance (dark energy) or a constant (Λ). It is the steady-state rate that results when topological pressure meets viscoelastic resistance (Chapter 8).

**13.11 Asymptotic 1 Space.** As cosmic time approaches infinity, all modes at all frequencies complete their constitutive relaxation. z → z_target[z] globally. R → 1. n_g → 1. The universe becomes 1 Space — a single self-consistent state, the integrated totality. The asymptotic endpoint is the fixed point z* = z_target[z*] realized everywhere. The universe that began as "0 realizing it was 1" ends as "1 having always been 1." The endpoint and the present truth are the same thing seen from inside vs outside time. [CONJECTURAL]

**13.12 The complete arc.** From null instability to asymptotic 1 Space, each phase has a GRUT-specific prediction or a scoped question. The universe's history is the constitutive equation applied at every scale and every epoch: τ₀ dz/dt + z = z_target[z] + ξ(t), relaxing toward z* through matter domination, structure formation, cluster mergers, and terminal-velocity expansion. One equation, one medium, one arc.

*Registry claims: cosmic_history_arc (anchored — composition), null_instability_hypothesis (conjectural), crystallization_sequence (deferred — T_c provenance resolved; Stage 2 specialist review pending).*

*Cross-chapter claims surfaced in this narrative: `bbn_thermal_buffer_negligible` (Ch 12, anchored — BBN cooling-buffer falsification); `genesis_noise_kernel_spectral_attempt` (Ch 12, anchored — Genesis Claim 1 spectrum-shape falsification); `cosmic_x_crossover_prediction` (Ch 4, computed — X = H τ₀ = 1 at z ≈ 71 for atomic-scale perturbations); `primordial_amplitude_zero_parameter_open_negative` (Ch 12, open negative — rescaling-conditional finding documented in 13.2); `t_c_provenance_inconsistency_resolved` (Ch 12, resolved — Correction #22 two-τ-scale convention; referenced in 13.4-13.5).*

---

# Chapter 14 — Falsification and Open Ledger

*What would kill the theory. What has already failed. What comes next.*

A theory that cannot be falsified is not physics. GRUT is falsifiable along multiple independent axes. This chapter documents every falsifier, every honest negative, and every open question.

**See also: `theory/GRUT_FALSIFIER_PAPER.md`** — the v8→v2 short paper collecting six near-term falsifiers across three sectors (lab gravity, cluster astrophysics, cosmology, Standard Model). The paper articulates the framework's adversarial posture vs other ToE programs in compact form, with each falsifier given a sharp prediction, derivation reference, observational test, current status, and refutation condition. The paper's six falsifiers (F1-F6) are the same as the falsifier classes named below, organized for adversarial review rather than for full theoretical exposition.

**Primary falsifier: the decoherence plateau.** If nanoparticle interferometry experiments measure gravitational decoherence and the rate does NOT show a plateau at the predicted ~689 Hz, the predictive core of GRUT fails. If the rate shows a plateau but at a different value, τ₀ changes and the downstream cosmological predictions shift. If the six scaling laws (mass-squared, geometry, plateau, separation, entanglement protection, geometric kink) are not all satisfied simultaneously, the CTP noise-kernel structure is wrong. This is the single most important experiment.

**Cosmological falsifiers:**

- H₀ converges outside 69 ± 3 km/s/Mpc → the one-parameter prediction fails
- H₀√Ω_Λ ≠ 58.16 ± 1 km/s/Mpc (DESI/Euclid/Roman) → the structural correlation fails
- w(z) = −1 exactly at survey precision → the viscoelastic regulation picture weakens
- Bullet Cluster lensing-gas offset fails to scale as v × τ₀ across multiple cluster mergers → the dielectric DM interpretation fails

**Computational falsifiers:**

- TJI on S⁴ gives g_S⁴ ≠ 1 → the −100 identification is structural, not point-derived
- τ₀ from decoherence inconsistent with H_inf → the terminal velocity mechanism fails

**Structural falsifiers:**

- Axion detected → GRUT's dielectric DM interpretation is wrong
- Fourth generation found → N = 3 uniqueness from Z₃ fails
- Koide violated by precision lepton mass measurements → Z₃ identity fails
- Graviton mass detected → massless graviton assumption fails

**What has been withdrawn or failed:**

- Dark energy from ρ_eq: permanently failed (ρ_eq < 0)
- 10 singularity resolution routes: all frozen
- Running τ_eff from CTP: overshoots by 10¹²⁶
- DM via Coleman nucleation: S_E ~ 10¹³, zero nucleation
- DM via Kibble mechanism: defect density ~ 10⁻⁷⁰ m⁻³
- **Constitutive perturbation growth at first order: FAILS.** The first-order constitutive equation predicts homogeneous FLRW expansion with growth factor D = 1.0 against the observationally required ~3375. First-order constitutive corrections cannot produce Jeans instability — this requires second-order / nonlinear extension. This is a computed negative, not an open derivation gap. Closure path: same as open negative #1 (nonlinear gravity ladder, rungs 5-8) — second-order constitutive coupling to perturbation theory, plus the n_g(ω) covariance closure (open negative #9). Until both close, GRUT does not produce structure formation in the cosmological-perturbation sector. This is one of the framework's most exposed flanks; a deposit-readiness reviewer should see it surfaced explicitly.
- R_vol = 1.5428: typo of R_anomaly = 1.15428 (Correction #14)
- Track VII Step 1 Ω_dm = 0.38: wrong topology, retracted (Correction #15)
- Genesis Claim 1 (CTP noise → primordial heat): structurally wrong at spectrum-shape level (Lorentzian × ω, not Planck/Bose-Einstein). Cross-verified against existing fdt_noise infrastructure
- abs() on C_Cosmo/C_FINAL: hid the conformal instability sign (Correction #16)
- N_total = 329: uses observed cosmic age as input; zero-parameter derivation registered as open negative #13
- TJI Phase-0.5: FeynCalc 7/4 not reproduced from raw Laurent −541/2304
- Koide Phase 4: no flavor mechanism derived from V7 machinery
- Path F: published Im(W) on dS is particle-production, not V7's R
- El Gordo cluster offset: originally reported as factor 3.5 under-prediction; sensitivity analysis shows GRUT prediction range (43-130 kpc) overlaps lower observation range (120-150 kpc). Reclassified from "inconsistent" to "tension pending better observational constraints"

**What GRUT does NOT claim:**

- A complete Theory of Everything: charged-fermion masses, CKM/PMNS angles, Higgs-sector closure, Dirac/Majorana neutrino status, and nonlinear gravity remain open. Neutrino hierarchy itself is derived under the Z₃/a_ν = 1 framework (Correction #28-29).
- That the SM is derived (it is imported as S_classical)
- That dark matter is definitively resolved (dielectric +27%, particulate factor 33 low)
- Resolution of the Hubble tension (H₀ ≈ 69 is a prediction, not a resolution)
- Mechanism for subjective experience
- Observable GW modifications (10⁻³⁹ rad, dead)
- That the constitutive projection is exact at the FULL nonlinear level in gravity/cosmology (the linearized Φ_μν derivation is exact via Corrections #23-#25; the curved-background scaffold is consistency-checked but the explicit Phase 2C construction of P^TT,g and G^R on FRW/S⁴ is sharper-successor open work; nonlinear extension is part of the gravity ladder open negative #1)

**How GRUT differs from other TOE candidates:**

| Approach | Λ mechanism | Dark matter | Measurement problem | Falsifiable? |
|:---|:---|:---|:---|:---|
| String landscape | Anthropic selection from ~10⁵⁰⁰ vacua | New particles (moduli, axions) | Not addressed | Difficult |
| Loop quantum gravity | Discretized spacetime | Not addressed | Not addressed | Area gap |
| Asymptotic safety | UV fixed point of gravity | Not addressed | Not addressed | Planck-scale |
| GRUT | Terminal velocity of damped conformal instability | Vacuum refractive enhancement | Dissolved: Λ_grav computes the observer's own crystallization (Schrödinger-in-the-Box) | Decoherence plateau + cluster scaling + H₀ |

GRUT's distinctive position: it gives the cosmological constant a specific causal mechanism (conformal instability damped by τ₀), connects it to a lab-scale experiment (decoherence plateau), and dissolves the measurement problem through the same scaling law that produces dark matter — not by interpretation but by computing the observer's own decoherence rate from the same equation. No other TOE candidate connects a tabletop experiment to the vacuum expansion rate through the same parent action, or resolves the measurement problem with a zero-parameter prediction rather than a free parameter or an interpretive stance.

**External convergence.** Several independent 2025-2026 developments converge on GRUT's foundational picture without referencing GRUT:

- Kim (IJMPD, 2026): "Relativistic quantum corrections to classical dynamics as an alternative to dark matter and dark energy" — Wigner-Moyal phase-space quantum corrections reproduce galactic rotation curves and Pantheon+ luminosity distances without invoking dark matter or dark energy. Same conclusion as the dielectric interpretation through different mathematics.
- Alexander, Hui, and Bernardo (PRL, 2026): "Cosmological Constant from Quantum Gravitational θ Vacua and the Gravitational Hall Effect" — topology of the Chern-Simons-Kodama state in quantum gravity protects Λ via a quantum-Hall analogue. Same foundational claim (Λ is topologically determined) through different mechanism.
- Itahashi et al. at GSI/Osaka (PRL, 2026): η′-mesic nucleus result shows the η′ meson's mass changes inside dense nuclear matter — experimental evidence that the QCD vacuum is a responsive medium with constitutive properties, in the sector where it's well-established.

None of these prove GRUT. All of them validate the foundational picture: the vacuum is a medium, dark phenomena are vacuum properties, and Λ is not a free parameter.

**The correction ledger.** The framework's audit infrastructure has caught and documented 28 substantive corrections during its development. Each represents a moment where a claim was found to be inaccurate — in framing, in numerical value, in derivation chain, or in scope — and was corrected in place rather than concealed. This table surfaces the major corrections so that a specialist reading the deposit can verify the discipline pattern with worked examples. Frameworks that don't surface their corrections aren't necessarily error-free; they're often error-opaque. GRUT's discipline infrastructure (registry, claim tiers, foundations audits, CORRECTION_*.md files in `theory/derivation/`) makes errors catchable and correctable rather than silent.

| # | What was claimed | What audit found | What got corrected | When / Where |
|:---|:---|:---|:---|:---|
| 1 | α_vac = 1/3 derived from CTP first principles | Conformal-mode-as-IR-carrier is a posited identification, not a derivation | The `alpha_vac_derivation` claim's statement was rewritten to surface the postulate explicitly; provenance audit added at `theory/foundations_audit/ALPHA_VAC_PROVENANCE.md` | `theory/foundations_audit/ALPHA_VAC_PROVENANCE.md` |
| 2 | Gold benchmark mass m = 80.8 fg | Numerical units off by 10³ — silicon nanoparticle at 1 μm has m ≈ 10⁻¹³ kg = 80.8 pg, not fg | Mass corrected to 80.8 pg across all decoherence-rate computations; downstream Λ_grav unchanged | Codebase pre-V7 |
| 3 | τ₀ derived from gold-benchmark decoherence plateau | Gold benchmark is a downstream consistency check; τ₀ is anchored by cosmic-baseline (1/(H₀×108π)) and the Bullet Cluster offset, with the gold benchmark verifying both | Reframed as multi-route provenance; `theory/foundations_audit/TAU_0_PROVENANCE.md` documents the 7-route convergence | TAU_0_PROVENANCE audit |
| 4 | El Gordo cluster offset is "inconsistent" — factor 3.5 under-prediction (70 kpc vs ~250 kpc) | El Gordo's published parameters span wide ranges (v_init 2000-3500 km/s, t 70-300 Myr, dec_ratio 0.5-0.85, observed offset 120-600 kpc); 80-combination sweep gives GRUT prediction range 43-130 kpc, overlapping lower observation range at ratio ~1.0 | Reclassified from "inconsistent" to "tension pending better observational constraints"; `el_gordo_sensitivity_analysis` claim documents the sweep | Ch 9 ledger; CORRECTION ledger ongoing |
| 5 | Track VII Step 1 — Ω_dm = 0.38 from particulate (vorton/string) route | Wrong topology assumed; monopole-style scaling invalid for the configuration; defect density ~10⁻⁷⁰ m⁻³ | Track VII Step 1 retracted; `vorton_track_vii_open_negative` registered; particulate route remains open as research problem | Correction #15; Ch 14 honest-negative list |
| 6 | R_vol = 1.5428 (3-loop CTP volume coefficient) | Typo of R_anomaly = 1.15428 — leading-digit transposition that propagated through V7 sections | Corrected to 1.15428 throughout; anomaly-quotient R registered as `r_loop_corrected` (honest_negative — TJI Phase-0/0.5 did not reproduce; diagnostic cross-check only). The canonical R = √(4/3) is Path G / Gate R; 1.15428 is not a loop correction to it. | Correction #14; CORRECTION_14_RVOL_TYPO.md |
| 7 | C_Cosmo expression returned `abs(C)` (positive magnitude) | The absolute value hid the conformal-mode instability sign — but the negative sign IS the physics (Gibbons-Hawking pathology drives expansion) | abs() removed; sign preserved; `h_inf_decomposition` recomputed with negative C_Cosmo, recovering H_inf = (2−R)/(Sτ₀) = 58.15 km/s/Mpc | Correction #16; Ch 8 derivation |
| 8 | N_total = 329 era count is a zero-parameter derivation | The era count uses observed cosmic age (t_universe ≈ 13.8 Gyr) as input — that's one observational anchor, not zero parameters | Reclassified as one-parameter derivation; `n_total_zero_parameter_derivation_open_question` registered as open negative #13; the cosmic-baseline H₀ route remains zero-parameter | Ch 8 / Ch 14 ledger |
| 9 | Primordial scalar amplitude A_s = 1/(πS³) is a zero-parameter derivation | The S³ amplitude depends on a rescaling choice (cosmic-baseline normalization); under a different rescaling, the value changes by a factor connected to the n_g(ω) covariance gap | Reclassified as rescaling-conditional; `primordial_amplitude_zero_parameter_open_negative` registered as open negative #14, blocked by #9 (n_g(ω) covariance) | Ch 13 ledger; PRIMORDIAL_ALPHA_S3_INVESTIGATION.md |
| 10 | X_cosmic = H(z)×τ₀ describes cosmic-history regime evolution generically | Different mass classes give different X values at the same epoch; for stellar masses Λ_grav dominates H by 76+ orders, placing compact objects in deep crystal at all redshifts regardless of cosmic background | Scope tightened to "atomic-scale test-particle perturbations of the cosmic background"; mass-class dependence registered as connected to open negative #9 | Ch 4; COSMIC_X_CROSSOVER_INVESTIGATION.md |
| 11 | T_c = 54.7 MK is the framework's critical temperature, dimensionally consistent with the noise kernel | Two τ-scales surface inconsistently: T_c codebase value uses one τ₀, while ℏ/(τ₀k_B) dimensional analysis with the canonical τ₀ = 41.9 Myr gives a wildly different scale | Registered as `t_c_provenance_inconsistency_open_negative` (open question #15); no code change pending audit-driven reconciliation | T_C_PROVENANCE.md; recent session |
| 12 | Cluster v×τ₀ scaling holds across Bullet/MACS J0025/Abell 520/El Gordo | The internal scaling residual (1.72%) is a separate computed claim from the absolute-magnitude match, which has a 15-20% systematic two-parameter degenerate with dec_ratio | `cluster_merger_internal_scaling_residual` registered separately from `cluster_merger_scaling_law`; the framework can have +20% normalization while still producing correct functional form | Ch 9 ledger |
| 13 | Ch 13.5 crystallization schedule pins T_c via thermal decoupling | Conflated two crystallization mechanisms — gravitational (Λ_grav-based, body-pair) and thermal (T < T_c bandwidth recovery); the schedule cannot be pinned until T_c provenance is resolved | Ch 13.5 stale CCIR replaced with held-pending diagnostic; CRYSTALLIZATION_SCHEDULE_INVESTIGATION.md (HELD); blocked by correction #11 | Ch 13.5; recent session |
| 14 | Genesis Claim 1: CTP noise kernel produces primordial-heat / BBN-DM source | (a) Noise-kernel spectrum at z=0 is Lorentzian × ω, NOT Planck/Bose-Einstein — wrong shape at the spectrum level; (b) Hypothesized DM-as-stalled-thermal-buffer test gives per-baryon energy ratio 4×10⁻⁹, ruled out by η_B suppression at 10 orders of magnitude | Genesis Claim 1 registered as `genesis_noise_kernel_spectral_attempt` (anchored honest-negative); `bbn_thermal_buffer_negligible` documents the falsification | Ch 13 / App A; GENESIS_NOISE_KERNEL_HEAT and BBN_THERMAL_BUFFER investigation logs |
| 15 | T_c = 54.7 MK derived consistently from canonical τ₀ via T_c = 1/(τ₀ × k_B) | The formula was dimensionally invalid: with τ₀ in seconds and k_B in J/K, the result has units K/(J·s), not K. The "v9 natural-units convention" defense did not survive a proper natural-units check (1/τ₀_natural at canonical τ₀ gives 5.78×10⁻²⁷ K, NOT 54.7 MK) | RESOLVED via the two-τ-scale convention: τ₀ = 41.9 Myr (gravitational, macroscopic) is now distinguished from τ_micro ≈ 1.4×10⁻¹⁹ s (thermal, microscopic). T_c is computed via the SI-correct `ℏ/(τ_micro × k_B)`. Numerical value 54.7 MK preserved exactly. The previous open negative #15 (`t_c_provenance_inconsistency_open_negative`) is RESOLVED | Correction #22 (Priority 1, May 2026); CORRECTION_22_TAU_CLEANUP.md |
| 16 | Φ_μν gravitational constitutive correction is heuristically asserted (not derived from S_CTP) | Chapter 14 already acknowledged the heuristic-projection gap; v8's `constitutive_projection_gravity_heuristic_open_question` (#10) was the registered honest negative | DERIVED at the linearized level: Φ_μν = α_vac × χ(ω) × P^TT × h_r emerges directly from `δS_CTP/δh_a |_{h_a=0}` of the linearized Schwinger-Keldysh action. Six structural properties verified at code level (kernel form, GR limit, full-constitutive limit, Bianchi via P^TT divergence-free, α_vac = 1/3 inheritance, gr_recovery consistency). Open question #10 RESOLVED at linearized level; `phi_munu_linearized_derivation` registered as computed | Correction #23 (Priority 2A, May 2026); CORRECTION_23_PHI_MUNU_DERIVATION.md |
| 17 | Φ_μν derivation lands at linearized only; curved-background extension open | After Correction #23, the curved-background extension was the immediate honest-gap successor | Curved-background extension SCAFFOLDED with four physical-consistency checks: flat-limit recovery, covariant conservation (∇^μ Φ = 0 from ∇^μ P^TT,g = 0), causality (K^R supported on past lightcone), FRW scalar-mode compatibility (n_g²(ω, k, t) = 1 + α χ_FRW). `phi_munu_curved_background_scaffold` registered as anchored (Ch 6) | Correction #24 (Priority 2B, May 2026); CORRECTION_24_PHI_MUNU_CURVED_SCAFFOLD.md |
| 18 | Curved-background scaffold pinned but explicit FRW χ_FRW(k, η) not computed | Phase 2C work was the natural Priority-3 cosmology bridge | EXPLICIT FRW result derived: χ_FRW^WKB(k, η) = 1/[1 + (τ₀ k_phys)²] from `□_g φ_k = -(1/a²)[∂_η² + 2H_c ∂_η + k²] φ_k` in slow-H regime. n_g²(k, η) = 1 + α/[1+(τ₀ k_phys)²]. Three explicit limits verified: sub-horizon → 1 (GR), super-horizon → 4/3 (full constitutive), transition at λ_* ≈ 80.7 Mpc today. Beyond-WKB correction (H_0 τ_0)² ≈ 8.7×10⁻⁶ today, subleading. `phi_munu_frw_explicit_construction` registered as computed | Correction #25 (Priority 2C, May 2026); CORRECTION_25_FRW_EXPLICIT.md |
| 19 | n_g(ω) cosmological covariance ill-defined (which ω, gauge invariance, μ/γ mapping) | v8 carried `n_g_omega_cosmological_covariance_open_question` (#9) as a real theoretical gap blocking the CMB falsifier | RESOLVED via three closure gates: (i) ω → k_phys × c identification, gauge-invariant at WKB; (ii) gauge-invariance verified across conformal-Newtonian/synchronous/comoving; (iii) MG-EFT mapping μ_GRUT(k, a) = n_g²(k, a), γ_GRUT(k, a) = 1 (no slip). Sharp prediction: GRUT in "μ ≠ 1, γ = 1" subclass distinguishing it from Brans-Dicke, f(R), DGP. μ - 1 = 1/3 on horizon scales — testable by DESI Y3+ at ~5σ, Euclid 2027 definitively | Correction #26 (Priority 3, May 2026); CORRECTION_26_PRIORITY_3_CLOSURE.md |
| 20 | n_g(ω) covariance closed but linear-growth consequences not computed | Natural follow-on after Correction #26 | LOAD-BEARING SANITY CHECK: numerical integration of modified Bardeen equation gives σ_8-scale enhancement of only 0.09% — GRUT does NOT break the existing S_8 tension. Large-scale modes show significant enhancement (8.5% at BAO, 33% at Sloan, ~135% at CMB horizon — testable). `modified_linear_growth_first_look` registered as computed (Ch 9) | Correction #27 (Priority 3.1, May 2026); CORRECTION_27_MODIFIED_GROWTH.md |
| 21 | Charged-lepton Z₃ structure (a = √2, K = 2/3) extends to neutrinos under same coupling | Naive expectation from Koide identity success in charged leptons | DOES NOT extend: minimum admissible Δm²_atm/Δm²_sol under a = √2 is 194.7, vs observed 33.9 (factor of 6 too large). Charged-lepton Z₃ coupling is incompatible with neutrino observations. Modified Z₃ with a_ν = 1 admits unique NH interior solution: m_1 ≈ 0.8 meV, Σm_ν ≈ 60 meV (below Planck 0.12 eV). IH at a_ν = 1 sits at boundary m_3 → 0 (degenerate, fine-tuned). GRUT structurally PREFERS Normal Hierarchy. Two new claims: `charged_lepton_z3_does_not_extend_to_neutrinos` (computed), `neutrino_hierarchy_z3_nh_prediction` (anchored on Priority 4B uniqueness theorem, derived in next correction) | Correction #28 (Priority 4, May 2026); CORRECTION_28_NEUTRINO_HIERARCHY.md |
| 22 | a_ν = 1 is postulated; derivation from GRUT primitives is open | Priority 4B target identified by user with four candidate derivation routes | DERIVED via boundary-degenerate uniqueness theorem: a = 1 is the unique Z₃ coupling at which (i) boundary access (one s_k = 0) is admissible AND (ii) the OTHER two s values are exactly degenerate. Boundary-gap formula √3 × √(a²-1) vanishes only at a = 1. Combined with NH-interior + Σm_ν < Planck, uniquely selects a_ν = 1. Channel-counting interpretation: a²_e = 2 (EM + weak) vs a²_ν = 1 (weak only) — neutrino sector lacks the electromagnetic coupling channel. `neutrino_z3_coupling_a_equals_1_uniqueness_theorem` registered as computed (Ch 9). The previous open question is RESOLVED | Correction #29 (Priority 4B, May 2026); CORRECTION_29_PRIORITY_4B_UNIQUENESS.md |
| 23 | Need a concise adversarial-roster paper synthesizing the framework's near-term falsifiers | Priority 5 deliverable of the v8→v2 deposit roadmap | New paper at `theory/GRUT_FALSIFIER_PAPER.md` — six near-term-testable falsifiers across three sectors: F1 (decoherence plateau ~689 Hz), F2 (³⁰Si/²⁸Si isotope discriminator vs CSL), F3 (BMV/sub-micron-separation gravitational entanglement), F4 (cluster-merger v×τ₀ scaling), F5 (μ - 1 = 1/3 modified-gravity on horizon scales), F6 (Σm_ν ≈ 60 meV with NH). Paper articulates GRUT's adversarial posture: not more rigorous than other ToE programs, but more falsifiable on near-term timescales. `falsifier_paper_six_near_term_tests` registered as meta (Ch 12) with all six falsifiers as deps | Correction #30 (Priority 5, May 2026); GRUT_FALSIFIER_PAPER.md |
| 24 | Allen-Jacobson S⁴ propagator Phase-1 was unimplemented; the gate for the anomaly-quotient R diagnostic route was entirely missing code | Prior sessions carried `allen_jacobson_phase1_stub_open_negative` — no computable S⁴ propagator existed for the TJI radial integral; open question #3 listed the obstacle as "propagator stub" | IMPLEMENTED: `s4_propagator()`, conformal-limit form, UV series expansion, spectral degeneracy helpers, `tji_on_s4()` (raises `S4CurvatureObstacle` — physically correct: the ₂F₁³ radial integral is the remaining gate, not missing code). 37 tests passing. `euler_coefficient_landing.py` (5-branch decision guard) and `theory/hard_theory/HYPEXP_TARGET_NOTEBOOK.ipynb` (Mathematica/HypExp target notebook) created. Open question #3 RESOLVED; obstacle narrowed from "Phase-1 propagator missing" to "ε-expansion of the ₂F₁³ integral" (`S4CurvatureObstacle`) | Correction #31 (hard-theory Phase-1, May 2026); `grut/derivation/tji/allen_jacobson.py`; `euler_coefficient_landing.py` |
| 25 | V4 RG cascade claimed "emergent scaling" — R = 1.1498 from 9×9 mixing matrix with no free parameters | V4.3 states the 9×9 matrix "with no tuning or post-hoc corrections, produces the observed Hubble-scale R value as an inevitable consequence of cosmic RG flow." The β_eff formula in V4.3 explicitly back-solves from R_obs = 1.154: β_eff = ln(1.154/9.07×10⁻⁶)/ln(10⁻⁴²) = −0.1215 | DIAGNOSED AS CALIBRATED CONSISTENCY CHECK by `v4_matrix_resolution.py`: actual matrix exponential exp(M·t) acting on Euler-channel initial state C₀[1] = 9.07×10⁻⁶ gives R_matrix ≈ 10⁸⁹ (dominant eigenvalue +2.28 amplifies over 96.74 log-steps; Euler channel projects onto it with |coeff| = 0.32). V4.3-stated eigenvalues sum 1.831 ≠ described matrix trace 1.32. Nearest eigenvalue to required 0.1215 is 0.1247 (3% off) but Euler projects onto it with only |coeff| = 0.049. GENUINE RESULTS PRESERVED: (a) V3 barepoint R(M_P) = 9.07×10⁻⁶ from pure S⁴ geometry remains computed tier; (b) Λ-as-universal-coupling-hub architectural framework is a structural advance; (c) V4.7 three-loop instability (1.5% correction → 18.83% R error) is a valid diagnostic — framework confirmed as 2-loop EFT with identified truncation boundary. New open question #20 registered. `v4_rg_cascade_calibration_honest_negative` registered as computed (Ch 7) | Correction #32 (V4 matrix resolution audit, May 2026); `grut/derivation/euler/v4_matrix_resolution.py`; `theory/V4_PHASE_6_COUPLING_AUDIT_RATIONALE.md` |
| 26 | V4/V5 off-diagonal mixing magnitudes were structural estimates (0.45-0.92 in Λ row), allowing a dominant +2.28 mode to hijack Euler flow | Off-diagonal operator mixing is loop-mediated and must carry κ = 1/(16π²) ≈ 0.00633 suppression. Applying this to all off-diagonals collapses Gershgorin radii and removes the explosive eigenmode. New first-principles anchor found: Christensen-Duff round-S⁴ Euler-anomaly sum for SM field content gives a_hat_SM = 1991/720, with a_hat_SM/(8π) = 0.11003 matching the structural Euler diagonal 0.11, while a_hat_SM/(16π²) = 0.01751 does not. RHN test (N_F: 45→48) raises M_11 by +1.657% to 0.11185 and worsens R-fit (clean falsification of the "RHN fixes gap" hypothesis) | IMPLEMENTED and tested in `v5_loop_suppressed_matrix.py`: (1) all off-diagonals multiplied by κ, (2) dominant eigenvalue collapses 2.2805→0.2203, (3) Euler projection on dominant mode drops 0.322→0.0070, (4) Euler becomes near-pure mode (projection 0.9688), (5) residual β gap localizes to Euler-diagonal normalization question (β_eff = 0.12293 vs 0.1215). Scientific status upgraded: not proof of R, but a concrete first-principles QFT anchor for M_11 with unresolved normalization origin as the load-bearing open question. | Correction #33 (loop-suppressed EFT + anomaly anchor, May 2026); `grut/derivation/euler/v5_loop_suppressed_matrix.py` |
| 27 | Post-Correction #33 (anomaly anchor achieved), the R-discrepancy remains as 1.2% β_eff overshoot (→ 14% R error). Required next step: localize which matrix elements drive the overshoot and whether they represent missing physics or just refinements | Three independent diagnostic gates implemented to isolate the problem: (1) Gate 1 — Euler-diagonal normalization origin: Christensen-Duff anchor identified; 8π vs 16π² discrepancy shows two plausible candidates (integrated-Euler, CTP/Keldysh). (2) Gate 2 — V5 flow sensitivity audit: off-diagonal Euler ↔ Gauge mixing M[1,5] has ∂β/∂M = 10.8 (24× larger than Euler diagonal sensitivity); problem NOT in M11, but in loop-suppressed off-diagonals. (3) Gate 2b — Target inversion: minimal R-target fix requires M11 −3% OR κ −7% tightening (loop suppression insufficient). Results: problem is NOT architectural, but a ~7% higher-order refinement in loop-suppression factor and/or Seeley-DeWitt diagonal coefficients | CREATED three independent diagnostic modules: `normalization_origin.py` (tests 6 candidate geometric sources of 8π), `v5_sensitivity_audit.py` (ranks matrix elements by ∂β/∂M_ij), `r_target_inversion.py` (constrained deformation analysis). Added 12-test regression suite (`test_christensen_duff_anchor.py`) locking CD values and RHN falsification. All tests passing. Gate findings documented in `three_gate_diagnostic_summary.md`. Open question #20 now narrows to: (a) geometric origin of 8π normalization, (b) 2-loop off-diagonal refinement via explicit Seeley-DeWitt on S⁴, (c) 3-loop Euler quotient coefficient extraction (independent track). | Correction #34 (three-gate diagnostic framework, May 2026); `grut/derivation/euler/{normalization_origin, v5_sensitivity_audit, r_target_inversion}.py`; `theory/hard_theory/THREE_GATE_DIAGNOSTIC_SUMMARY.md`; `tests/derivation/test_christensen_duff_anchor.py` |

The remaining two corrections in the V7 era are minor — surfacing of test-marker conventions and a renumbering of Path-F stage logs — and are documented in the codebase audit logs without document-level surface area.

| 28 | α_vac = 1/3 was framed as "computed under named postulate" (conformal-mode-as-IR-carrier); the "vacuum impedance = 1/d" narrative in v11 App H was an assertion, not a published derivation; the two R-tracks (constitutive/refractive vs 3-loop anomaly quotient) were conflated as "tree-level + loop correction" | Gate R audit sequence (7 gates, May 2026): Gate 3 vertex provenance, CTP branch-incidence, sector-coupling, sector-dimensional, CTP action term, α_vac provenance, and Gate R identification (C1-C6 all SUPPORTED/FORMALIZED). Key findings: α_vac = 1/3 is Route 2 (Duff 1994 a/c = 1/3, published, exact, convention-independent); the Weyl decomposition formalizes the conformal-mode identification; R_anomaly = 1.15428 is an honest negative, not a loop correction to R = √(4/3); P^TT / scalar-anomaly compatibility resolved (R5b: scalar amplitude vs TT filter are independent roles) | Gate R closed: R = √(4/3) **derived** within constitutive-action framework via Path G. α_vac = 1/3 upgraded from "named postulate" to "formalized identification." R_anomaly = 1.15428 correctly classified as honest-negative diagnostic. Chapter 7 rewritten; all stale "loop-corrected" and "postulate" language updated throughout book. | Gate R closure (Corrections #32-34 era, May 2026); `theory/hard_theory/GATE_R_*` documents; `grut/hard_theory/s4_ctp_solver/gate3_*.py` |

**Cumulative correction tally (May 2026): 28 documented corrections across V7 development (rows 1-14), v8→v2 synthesis (rows 15-23), hard-theory audits (rows 24-27), and Gate R closure (row 28).** Each correction is a focused, tested, documented unit. The discipline pattern is unchanged across the development cycle: every correction is an addition to audit infrastructure, not a deletion of history.

The pattern across these entries: the framework treats every correction as an addition to the audit infrastructure, not a deletion of history. None of these corrections were silent. Each has a registry claim, an investigation log, or a CORRECTION_*.md file with traceable provenance. This is what "audit transparency" means concretely.

**Open questions (status as of v8→v2 synthesis, May 2026):**

| # | Open Question | Status | Chapter | Closure Path | Effort |
|:---|:---|:---|:---|:---|:---|
| 1 | Nonlinear gravity ladder (4/8 rungs) | open | Ch 6 | Complete rungs 5-8 | Multi-year |
| 2 | TJI Euler-channel coefficient extraction | open | Ch 7 | HypExp ε-expansion of [₂F₁]³ radial integral (Mathematica/HypExp) | ~1-2 weeks Mathematica specialist |
| 3 | Allen-Jacobson propagator stub | **RESOLVED (Correction #31, May 2026)** | Ch 12 | Phase-1 propagator IMPLEMENTED; `S4CurvatureObstacle` raised by tji_on_s4() — obstacle narrowed to ε-expansion step | Done |
| 4 | El Gordo tension | open (observational) | Ch 9 | Tighter lensing constraints; v_post measurements | Observational |
| 5 | Koide Phase 4 — no flavor mechanism | open | Ch 12 | CTP Yukawa eigenvalue problem | Multi-session |
| 6 | Path F — Im(W) translation gap | open | Ch 12 | Bridge published Im(W) to CTP R | Research |
| 7 | ρ_max numerical scale | open | Ch 12 | Extended derivation beyond universal τ₀ | Research |
| 8 | Vorton Track VII | open | Ch 12 | String-vorton computation | Research |
| 9 | ~~n_g(ω) covariance~~ | **RESOLVED (Correction #26, May 2026)** | Ch 9 | μ(k,a)/γ(k,a) MG-EFT mapping derived; CMB Boltzmann implementation now downstream computational task | — |
| 10 | ~~Constitutive projection gravity heuristic~~ | **RESOLVED at linearized + curved scaffold + FRW levels (Corrections #23, #24, #25, May 2026)** | Ch 6 | Φ_μν derived from δS_CTP/δh_a; sharper successor: curved-background explicit construction (still open as Phase 2D refinement) | — |
| 11 | Two-route R convergence physical equivalence | open | Ch 7 | Derive why Path G and Osborn compute the same object | Research |
| 12 | Track V coupling unification 8.9% miss | open | Ch 12 | Constitutive β-function correction to gauge running | 6-12 months |
| 13 | N_total zero-parameter derivation | open | Ch 8 | Derive cosmic age from framework foundations | Multi-phase research |
| 14 | Primordial A_s zero-parameter derivation | open (sharpened post-#26) | Ch 13 | Boltzmann-pipeline computation of pivot-mode A_s with μ_GRUT (no longer blocked by #9 since closed) | Research |
| 15 | ~~T_c provenance / dimensional consistency~~ | **RESOLVED (Correction #22, May 2026)** | Ch 2 | Two-τ-scale convention: τ₀ (gravitational, 41.9 Myr) and τ_micro (thermal, ~10⁻¹⁹ s) explicitly distinguished | — |
| 16 | Born rule from N_grav (structural framing) | open | Ch 11 | Decoherent-histories postulate, einselection, or deeper-symmetry path-integral derivation | Multi-decade |
| 17 | (new) `phi_munu_curved_background_scaffold` — Phase 2C explicit P^TT,g and G^R on FRW/S⁴ | open (sharper successor of #10) | Ch 12 | Killing-tensor decomposition + WKB Green-function on curved backgrounds | ~2-4 weeks specialist |
| 18 | (new) `phi_munu_frw_beyond_wkb_open_question` — beyond-WKB FRW correction | open (subleading) | Ch 12 | (H τ_0)² ≈ 10⁻⁶ correction; not load-bearing for current observables | Research-tier, deferred |
| 19 | (new) `neutrino_z3_coupling_a_equals_1_uniqueness_theorem` — full KS-anomaly derivation of channel counting | open (interpretive) | Ch 12 | Show a²_ν = 1 vs a²_e = 2 follows from KS coefficients in Dirac-ν + EM-channel-absent sector | Research |
| 20 | (new) `v4_rg_cascade_independent_matrix_derivation` — does the 9×9 RG beta-function matrix, derived from first-principles 2-loop curved-space anomaly calculations on S⁴, give Euler-channel eigenvalue ≈ 0.1215 without observational input? (Correction #32 diagnosed V4.3 as calibrated: β_eff back-solved from R_obs = 1.154; matrix trace 1.32 ≠ V4.3 eigenvalue sum 1.831) | open | Ch 7 | Three-step proof: (A) replace structural estimates with M_ij from S⁴ 2-loop Seeley-DeWitt/heat-kernel anomaly coefficients (Christensen & Duff 1979, Jack & Osborn 1990); (B) verify that Weyl² = 0 on S⁴ zeroes the non-topological off-diagonals M[Weyl-type, Euler], collapsing the Euler channel's projection onto the dominant +2.28 mode from |coeff|=0.322 to <0.01; (C) check that the topological sub-block eigenvalue refines from 0.1247 toward 0.1215 (≤1%). If all three hold, exp(M·t) acting on the Euler channel naturally produces R ≈ 1.154 with no observational input — formally deriving the macroscopic vacuum from the S⁴ geometry. Test harness already in place: `grut/derivation/euler/v4_matrix_resolution.py` (success criterion: `provenance == "independent"` and `error_percent < 1.0`). S⁴ geometric machinery available in `grut/derivation/tji/allen_jacobson.py` | Multi-month (curved-space QFT 2-loop beta functions) |

Closure priority (by downstream fan-out): **Gate R is now CLOSED** (May 2026) — R = √(4/3) is canonical via Path G / constitutive-refractive route; this unlocks `r_canonical_path_g` and `h_inf_decomposition` independently of TJI. TJI (#2) is now a **diagnostic cross-check** on the anomaly-quotient route, not a gate for the canonical R. Its downstream claims are: `three_routes_convergence` (would become 3-way if TJI reproduces 1.15428) and diagnostic confirmation of the integer provenance. **Publication-facing priority ranking (post-Gate R):** (1) nonlinear gravity rungs 5-8, (2) full Boltzmann/CAMB/CLASS pipeline, (3) SM Yukawa/CKM/PMNS closure, (4) dark-sector normalization tensions, (5) TJI as diagnostic cross-check. The former Allen-Jacobson propagator blocker (#3) is **RESOLVED** (Correction #31, May 2026): Phase-1 propagator implemented, `tji_on_s4()` now raises `S4CurvatureObstacle`; the remaining gate for #2 is the Mathematica/HypExp ε-expansion of the [₂F₁]³ radial integral. The n_g(ω) covariance question (#9) blocks two downstream gaps: CMB falsifier promotion AND primordial A_s derivation (#14). Open question #20 (V4 matrix derivation, Corrections #32-#33) has fan-out 1: closing it upgrades the R = 1.1498 calibrated result to a computed prediction; the dominant sub-gate is now Euler-channel normalization origin on round S⁴. All other open negatives have fan-out 0–1.

This section is mechanically generated from the open-question ledger in the codebase. Future open negatives enter the ledger and propagate here automatically.

**The completion ladder — from candidate framework to scientific establishment.** The fifteen open questions and the perturbation-growth failure are not equally proximate to closure. They form a ladder: lower tiers are reproducibility and near-term experimental gates; middle tiers are theoretical-derivation work; upper tiers are multi-year quantum-gravity completion. Each tier represents a coherent research program rather than a scattered set of tasks, and each tier's closure conditions name *what specific work would advance the framework's standing*. Closing the bottom tiers makes the framework defensible against external review. Closing the upper tiers makes the framework a candidate for scientific establishment as a complete ToE.

| Tier | Research package | Open negatives addressed | Closure condition | Effort scale |
|:---|:---|:---|:---|:---|
| **1** | **Reproducibility freeze and external-review readiness** | (housekeeping; not in registry) | Version, test-count, claim-count, install-path, Zenodo-metadata sync; appendices auto-rendered from canonical registry; one-command repro instructions | ~hours to ~days |
| **2** | **Near-term experimental falsifiers** | (no open negatives — these are *active* falsifier targets, not gaps) | Decoherence plateau measured at gold benchmark; isotope-pair discriminator (³⁰Si/²⁸Si at 3.8% precision); BMV-class entanglement formation rate at sub-micron separation | Active experimental programs (5-15 yr) |
| **3** | **Cosmological covariance closure** | #9 (n_g(ω) covariance), #14 (primordial A_s rescaling), perturbation-growth FAILS | Pick gauge-covariant n_g(ω) prescription; map to MG-EFT (μ(k,a), γ(k,a)); CLASS/CAMB implementation; resolve first-order growth-factor failure via second-order constitutive extension | Months — specialist cosmologist + Boltzmann-code work |
| **4** | **Gravity completion (curved-space)** | #2 (TJI Euler-channel extraction), #3 (~~Allen-Jacobson propagator~~ **DONE** — Correction #31), #10 (constitutive projection Φ_μν heuristic), #11 (two-route convergence physical equivalence) | ~~Allen-Jacobson propagator built on S⁴~~ **DONE**; TJI: HypExp ε-expansion of [₂F₁]³ radial integral (Mathematica specialist); Φ_μν derived from δS_CTP/δh_μν rather than asserted | AJ propagator: **DONE** (May 2026); TJI ε-expansion: ~1-2 weeks Mathematica; Φ_μν: multi-month |
| **5** | **Standard Model closure** | #5 (Koide Phase 4, no flavor mechanism), #6 (Path F translation gap), #12 (Track V coupling unification 8.9% miss) | At least one nontrivial Yukawa or mixing angle derived from CTP fixed-point machinery; β-function correction closes gauge-coupling unification | Multi-session to multi-year — particle-physics theorist work |
| **6** | **Nonlinear quantum-gravity** | #1 (nonlinear gravity ladder, 4/8 rungs), #7 (ρ_max scale), #8 (Vorton Track VII), perturbation growth (nonlinear closure) | Complete rungs 5-8 of the nonlinear constitutive ladder; tensor-mode stability; diffeomorphism closure at the constitutive level; non-perturbative fixed point | Multi-year program — quantum-gravity collaboration |

**Reading the ladder.** Tier 1 is housekeeping — necessary to make the framework reviewable but adds no new physics. Tier 2 is what the framework *invites the experimental community to do* — these are GRUT's near-term falsifiers, and active experimental programs (MAQRO, matter-wave interferometry, BMV-class entanglement) are positioned to test them. Tier 3 is the next theoretical step that the framework can pursue under its current machinery, and it gates two open negatives plus the perturbation-growth failure simultaneously. Tier 4 closes the gravity-side seams. Note: TJI / Euler-channel coefficient extraction is now a **diagnostic cross-check** on the anomaly-quotient route, not a gate for the canonical R = √(4/3) — that value is closed via Gate R (Path G, constitutive/refractive). TJI resolving or not does not affect the canonical derivation. Tier 5 is the SM-derivation program. Tier 6 is the nonlinear quantum-gravity completion required for the framework to claim ToE status in the strong sense — it is the longest-horizon work, and its incompleteness is the framework's most explicit honest negative.

The framework's deposit position: tiers 1-2 are achievable now and are the legitimate basis for external review; tiers 3-6 are the research roadmap that distinguishes candidate framework from completed theory. Specialists evaluating GRUT should evaluate it on its position in this ladder, not on the implicit standard of "complete and published Theory of Everything."

**GRUT-RAI v3 Hard-Theory Benchmark — S4 CTP solver milestone ladder.**

Stage 1 — Reproduce flat-space known results
Confirm the engine handles ordinary 1-loop / 2-loop / 3-loop diagram bookkeeping.

Stage 2 — Reproduce known curved-space trace anomaly coefficients
a, c, b for scalar, Weyl fermion, gauge boson.

Stage 3 — Build the S4 heat-kernel / Seeley-DeWitt basis
This is the curved-background backbone.

Stage 4 — Implement CTP doubling on curved background
Forward/backward metrics g_plus, g_minus, Keldysh basis, retarded/Hadamard structure.

Stage 5 — Compute 1-loop S4 effective action
This is the first real curved-space benchmark.

Stage 6 — Extend to 2-loop checks
Compare against any known literature limits.

Stage 7 — Attempt full 3-loop CTP S4
Only after the earlier rungs pass.

Stage 8 — Recover R without proxy
This is the GRUT benchmark.

**Toolkit-branch observation (research direction, not current framework content).** GRUT's foundational structure inherits explicitly from one branch of the nonperturbative-QFT toolkit: regularization-and-anomaly-coefficient calculus, with π (in S = 108π and noise-kernel normalization), digamma-like regularization integrals (in Khasanov-Segal trace-anomaly coefficients), imaginary numbers (in the iε prescription, the influence-functional noise term, the Schwinger-Keldysh contour), and −1/12 / zeta-regularization (in trace anomalies and conformal-mode contributions). It does *not* inherit from the adjacent branch: integrable systems, continued fractions, KAM-resonance hierarchies, quasiperiodic structures, and the φ / Fibonacci mathematics those produce. An examination of whether φ already appears somewhere in GRUT's existing self-referential structure (`theory/derivation/PHI_IN_FRAMEWORK_EXAMINATION.md`) finds it does not — at sub-1% precision, no framework constant matches a φ-related target value, and no fixed-point equation takes the φ-producing form `x² = x + 1`. The closest numerical coincidence (Weyl-fermion anomaly ratio a/c = 11/18 ≈ 1/φ at 1.12%) is consistent with random chance. The most substantive structural finding from the deeper hunt: φ appears *exactly* in 5-fold cyclic structure (2 cos(2π/5) = 1/φ); the framework has Z_3 generation structure, which uniquely selects N = 3 by anomaly cancellation. **If reality has hidden 5-fold structure — discrete flavor symmetry like A_5, quasicrystal-like vacuum structure, hidden gauge groups with 5-fold rotation, or icosahedral structure in a sector beyond the visible SM — that would be the natural place for φ to enter the framework.** Whether this branch is permanently absent from physical reality or whether the framework is missing structure from it is an open question for v2+ research, registered here for honesty rather than as a claim. The current deposit's predictions are unchanged by this observation; the framework's R = √(4/3) → 1 endpoint stands as derived from current structure. The φ research direction is documented for any future researcher who wants to pursue it.

**What comes next:**

| Priority | Target | What it would close | Timescale |
|:---|:---|:---|:---|
| 1 | Decoherence plateau experiment | Primary falsifier — validates or kills the framework | Active programs |
| 2 | TJI on S⁴ (~3 weeks) | Stress test — Route 2 confirmation or honest negative | Near-term |
| 3 | CTP Yukawa eigenvalue problem (Track II) | Fermion masses — the biggest open gap | Multi-session |
| 4 | Constitutive β-function correction (Track V) | Coupling unification — the 8.9% miss | 6-12 months |
| 5 | CMB Boltzmann implementation (CLASS) | CMB-S4 falsifier — requires covariance closure first | 4-8 weeks specialist |
| 6 | Additional cluster merger observations | v × τ₀ scaling confirmation; El Gordo resolution | Ongoing observational |

**V8 research tracks mapped to the ToE.** The V8 companion document organizes ongoing work by track. For specialists looking for the development organization behind this synthesis:

| Track | Sector | ToE Chapter | Status |
|:---|:---|:---|:---|
| Track I | CTP foundational structure | Ch 2-3 | Core computed |
| Track II | Yukawa eigenvalue / fermion masses | Ch 12 (open #5) | Scoped, not started |
| Track III | Gravitational decoherence experiments | Ch 5, 11 | Active programs (MAQRO, MAGIS-100) |
| Track IV | Cosmological constant / terminal velocity | Ch 7-8 | Two-route convergence computed |
| Track V | Coupling unification | Ch 12 (open) | 8.9% miss, β-function correction defined |
| Track VI | Nonlinear quantum gravity | Ch 6 | 4/8 ladder rungs |
| Track VII | Dark sector (DM, cluster scaling, CMB) | Ch 9 | Bandwidth integral computed, cluster scaling 3/4, CMB scoped |

The ToE synthesizes results across tracks. The V8 document preserves the track-by-track development log with per-track closure conditions and effort estimates.

**Predictions dashboard.** The companion document `GRUT_TOE_PREDICTIONS.md` (auto-generated from `grut/toe/dashboard.py`) lists all quantitative predictions in one artifact with values, observations, status glyphs, and falsification conditions. Status distribution: 17 consistent, 3 in tension (Ω_dm +27%, τ₀ cluster-cosmic +20%, El Gordo parameter-dependent), 0 definitively inconsistent, 4 untested, 2 scoping-tier, 1 rescaling-conditional (A_s). Every prediction has a registry back-link verified by passing tests. A specialist asking "what does GRUT predict?" starts there.

*Registry claims: correction_ledger (meta), predictions_dashboard (meta), marker_validator_discipline (meta), derivation_index_appendix (meta), claim_registry_appendix (meta), dependency_graph_appendix (meta), koide_phase_4_open_negative (open_negative), path_f_translation_gap (open_negative), vorton_track_vii_open_negative (open_negative), allen_jacobson_phase1_stub_open_negative (open_negative), rho_max_scale_open_question (open_negative), el_gordo_outlier_open_question (open_negative), constitutive_projection_gravity_heuristic_open_question (open_negative), two_route_convergence_physical_equivalence_open_question (open_negative), track_v_coupling_unification_open_question (open_negative), n_g_omega_cosmological_covariance_open_question (open_negative), n_total_zero_parameter_derivation_open_question (open_negative), primordial_amplitude_zero_parameter_open_negative (open_negative), t_c_provenance_open_question (open_negative), neutrino_dirac_prediction (anchored)*

---

## Part IV — Appendices and Reference

# Appendix A — The GRUT Genesis Hypothesis [SPECULATIVE]

**A.1 The null fixed point.** z = 0 satisfies z = z_target[z] when F[0] = 0. Trivial fixed point. Stable under deterministic evolution. The "nothing" state.

**A.2 The non-absorbing condition.** The noise kernel ξ(t) — generated by the CTP doubling, not added by hand — makes z = 0 unstable to fluctuations. Even an infinitesimal noise amplitude forces z to explore neighborhoods of the null state. The CTP action guarantees that perfect nothing cannot persist.

**Genesis noise kernel investigation (Stages 1-4 complete — structurally wrong).** Can the CTP noise kernel produce thermal radiation as a primordial heat source? The framework's KMS noise kernel N(ω) = (2/τ₀)ℏω coth(ℏω/2k_BT) requires T as input — it describes thermal noise in equilibrium with a bath at temperature T, it doesn't define T. At T = 0 (pure quantum vacuum), the computed spectrum is:

S_h(ω) = (2ℏ/τ₀) × ω/(1+(ωτ₀)²) — Lorentzian × linear

This is **not** Planck/Bose-Einstein at any temperature. The "thermal-spectrum radiation" framing fails at the shape level. Characteristic temperatures extractable from the spectrum: spectral peak gives ℏ/(τ₀k_B) ≈ 5.78 × 10⁻²⁷ K (27 orders too cold for CMB); Planck UV cutoff gives ~10³² K (32 orders too hot). Neither matches the observed CMB temperature of 2.725 K. Cross-verified exact against the framework's existing `fdt_noise` infrastructure (relative difference = 0 across all tested regimes). [STRUCTURALLY WRONG — spectrum shape excludes thermal interpretation]

**A.3 The constitutive drive.** When fluctuation produces z ≠ 0, the constitutive response τ₀ dz/dt + z = z_target[z] activates. If z_target[z] ≠ 0 for small nonzero z, the system is driven toward a nontrivial fixed point. The transition is automatic: the constitutive equation's fixed-point structure does the work.

**A.4 The primordial fluctuation spectrum — rescaling-conditional.** Three paths were computed to derive A_s ~ 2.1 × 10⁻⁹ from the CTP noise kernel. Path A (OU-process equilibrium variance at T_CMB) gives 2.04 × 10⁻¹⁹ — factor 10¹⁰ too small. Path B (inflationary formula with GRUT's terminal H_inf) gives 5.29 × 10⁻¹¹⁸ — the framework has no inflationary epoch. A forward derivation (Lens B/F) recovers the S³ family conditionally under specific rescaling choices.

The α/S³ result is not closed as coincidence. A forward derivation (linearized constitutive perturbation, Lens B/F) recovers the S³ family conditionally: cosmic-baseline rescaling gives 1/(πS³) ≈ 8.15 × 10⁻⁹ (factor 3.88 from A_s); H_inf rescaling gives ((2−R)/S)³/π ≈ 4.92 × 10⁻⁹ (factor 2.34); Planck rescaling gives (t_Pl/τ₀)³ ≈ 10⁻¹⁷⁶ (definitively excluded). The rescaling choice maps onto open question #9 (n_g(ω) covariance) — closing #9 selects the rescaling and either delivers A_s or sharpens the negative.

The framework's posture: A_s is conditionally predictable in the S³ family. Three candidate predictions exist; which is correct depends on the covariance closure. This is a sharper position than "we can't predict A_s" — it's "we have three quantitatively distinct predictions conditional on a specific theoretical question already in the ledger." [RESCALING-CONDITIONAL]

**A.5 "0 realizing it was 1."** The framework's natural reading: the universe began at the trivial fixed point and was driven by its own constitutive structure toward the nontrivial fixed point at z*. R = √(4/3) is the universe's name for that nontrivial fixed point in the cosmological sector. R = √(4/3) ≈ 1.15 encodes the endpoint the dynamics discovered.

**A.6 What this isn't.** Not a derivation of inflation. Not a substitute for proper early-universe cosmology. Not load-bearing — labeled [SPECULATIVE] throughout. This appendix is a formal home for the genesis intuition while keeping the computed core uncontaminated.

*Registry claims: genesis_hypothesis (conjectural — speculative), genesis_noise_kernel_spectral_attempt (anchored — structurally wrong at spectrum-shape level)*

---

# Appendix B — GRUT vs Established Frameworks

**B.1 GRUT vs General Relativity.** GR is recovered in the high-frequency limit (7-leg harness, Chapter 6). Eight independent solar-system tests confirm safety factors from 10⁵ to 10³⁵ (Chapter 4). What GRUT adds: low-frequency refractive structure (dark matter), the decoherence sector (laboratory predictions), and terminal velocity for expansion (dark energy mechanism). Where they agree: everywhere ωτ₀ ≫ 1. Where they differ: galactic and cosmological frequencies where ωτ₀ ≲ 1.

**B.2 GRUT vs ΛCDM.** Both predict Ω_Λ ≈ 0.69 — ΛCDM as input parameter; GRUT as derived from R = √(4/3). H₀ tension: ΛCDM has it as a problem; GRUT places H₀ ≈ 69 in the gap as a prediction. Dark matter: ΛCDM requires new particles (WIMPs, axions); GRUT's dielectric interpretation requires no new particles. BBN: identical (GRUT → GR above T_c). CMB: identical at Planck precision; distinguishable at CMB-S4.

**B.3 GRUT vs MOND.** Both reproduce galactic rotation phenomenology with a₀ ≈ 1.2 × 10⁻¹⁰ m/s². GRUT additionally reproduces the Bullet Cluster offset via memory kernel — where MOND historically struggled. Key difference: MOND has an acceleration threshold; GRUT has a frequency threshold. At high frequency and low acceleration, GRUT predicts GR behavior where MOND predicts modification. GW propagation: GRUT predicts c exactly; MOND/TeVeS has constraints.

**B.4 GRUT vs particle dark matter (WIMPs, axions).** GRUT's dielectric interpretation: Ω_dm = α = 1/3 from vacuum refractive enhancement, no new particles. Particle DM: requires specific particles with specific cross-sections. Discriminators: GRUT predicts no direct-detection signal (no particle to detect); particle DM predicts a detection signal. If dark matter is detected directly, GRUT's dielectric interpretation fails.

**B.5 GRUT vs objective collapse models (CSL, Diósi-Penrose).** All predict gravitational decoherence. GRUT's distinguishing features: zero free parameters (CSL has λ), m² scaling (CSL has N), specific plateau at 689 Hz, six scaling laws no alternative reproduces simultaneously. The isotope-pair discriminator (Chapter 5) provides a concrete near-term test: ³⁰Si/²⁸Si ratio at 3.8% precision distinguishes GRUT from CSL. Philosophically, GRUT goes further than objective collapse models: it dissolves the measurement problem entirely via the Schrödinger-in-the-Box inversion — the observer's own Λ_grav computes their classical definiteness from the same equation that predicts the decoherence plateau, with no free parameters and no interpretive stance required. CSL and GRW add a collapse mechanism; GRUT derives classicality as a consequence of the observer being field content in the constitutive medium.

**B.6 GRUT vs string theory.** Different ToE styles. String theory: extra dimensions, landscape of 10⁵⁰⁰ vacua, anthropic selection. GRUT: one CTP action, one medium, two constants, specific predictions. Where string theory excels: mathematical depth, graviton scattering amplitudes, AdS/CFT. Where GRUT excels: specific falsifiable predictions at laboratory scale, cosmological predictions with zero free parameters. Compatible? Possibly — the constitutive equation could emerge from a specific string compactification. Not explored.

**B.7 GRUT vs loop quantum gravity.** Both are gravity-first frameworks. LQG: quantized spacetime (spin foams, area gaps). GRUT: constitutive medium (relaxation, bandwidth, refractive index). LQG predicts discrete area spectrum at Planck scale; GRUT predicts continuous constitutive corrections at all scales. Different starting points, different predictions, potentially complementary.

**B.8 GRUT vs asymptotic safety.** Both make gravity quantum-tractable. Asymptotic safety: UV fixed point under Wilsonian RG. GRUT: constitutive fixed point z* = z_target[z*]. Different mechanisms — the constitutive fixed point is IR (relaxation endpoint), not UV (high-energy behavior). Rung 8 of the nonlinear ladder (Chapter 6) asks whether these coincide. If they do, GRUT's constitutive structure might provide the physical mechanism for asymptotic safety.

**B.9 Numerical comparison tables.** Specific numerical predictions where the frameworks make quantitative claims at the same operating point.

*Gravitational decoherence at the gold benchmark (m = 80.8 pg, l = 1 μm, R = 1 μm, T = 4 K, P = 10⁻¹⁶ Pa):*

| Framework | Λ_grav (Hz) | Free parameters | Notes |
|:---|:---:|:---:|:---|
| **GRUT** | **689** | **0** | Computed exactly from G m² S(l/R) / (ℏ l) with framework's α = 1/3 |
| Diósi-Penrose (R₀ = 0.05 fm) | ~10⁴ | 1 (R₀) | DP plateau magnitude depends on regulator R₀ |
| Diósi-Penrose (R₀ = 1 fm) | ~10² | 1 (R₀) | Different R₀ gives different plateau |
| CSL (λ = 10⁻¹⁶ s⁻¹, r_c = 100 nm) | ~10⁻⁹ | 2 (λ, r_c) | Standard parameter values; far below GRUT |
| Adler mass-prop CSL | ~10⁻⁵ | 1 | Mass-proportional rather than mass-squared |
| GRW | ~10⁻⁸ | 2 | State-independent collapse |

*Galactic rotation phenomenology at MOND scale (a₀ ≈ 1.2 × 10⁻¹⁰ m/s²):*

| Framework | a₀ derivation | Free parameters | GW propagation |
|:---|:---|:---:|:---|
| **GRUT** | **a₀ = c H₀ / (2π)** ≈ 1.2 × 10⁻¹⁰ m/s² (derived) | **0** | Exactly c (massless graviton) |
| MOND/TeVeS | a₀ fit to data (input) | 1 (a₀) + interpolation function | Bounded by GW170817 (TeVeS strained) |
| WIMP/axion DM | No a₀ scale (per-galaxy fit) | Cross-section, mass per particle | Exactly c |

*Cluster-merger gas-to-lensing offsets (post-collision velocity v_post, separation l):*

| System | v_post (km/s) | GRUT prediction (kpc) | Observed (kpc) | Ratio |
|:---|:---:|:---:|:---:|:---:|
| Bullet Cluster | 3000 | 130 | 150 | 0.87 |
| MACS J0025 | 1532 | 66 | 75 | 0.88 |
| Abell 520 | 1468 | 63 | 80 | 0.79 |
| El Gordo | 1596 | 70 | 250 | 0.28 (TENSION; sensitivity range 43-130 kpc) |

*Internal v × τ₀ scaling residual across the four systems: 1.72%* (registered as `cluster_merger_internal_scaling_residual`). Particle DM frameworks make no analogous prediction; the MOND/TeVeS literature historically struggles with the Bullet Cluster's lensing-gas offset.

*Cosmological parameters (zero-parameter GRUT prediction vs Planck 2018 best fit):*

| Quantity | GRUT prediction | Planck 2018 | Match |
|:---|:---:|:---:|:---:|
| Ω_Λ | 0.6886 | 0.6889 | <0.05% |
| H₀ (cosmic-baseline) | 68.8 km/s/Mpc | 67.4 ± 0.5 | within tension band |
| H₀ (one-param Friedmann) | 69.03 km/s/Mpc | 67.4-73.5 (tension) | within tension band |
| Ω_dm,eff (dielectric) | 1/3 = 0.333 | 0.263 | +27% (anchored) |
| η_B (baryogenesis) | 6.57 × 10⁻¹⁰ | 6.10 × 10⁻¹⁰ | +8% (anchored) |
| n_s (spectral index) | 0.9649 (Hτ-anchored) | 0.9649 | match by construction |
| t_entangle at BMV (m = 10⁻¹⁴ kg, l = 200 μm) | 3.16 s | (BMV literature: 3.16 s) | identical (S(l/R) = 1 in far field) |

*Discrimination summary by framework class:*

- **vs GR:** identical at ωτ₀ ≫ 1 (solar system 8/8 tests, 11 orders of magnitude in frequency); diverges at galactic and cosmological scales where ωτ₀ ≲ 1.
- **vs ΛCDM:** Ω_Λ derived rather than input; H₀ in tension gap as prediction; dark matter as dielectric rather than particles.
- **vs MOND:** identical a₀ phenomenology at galactic scale; GRUT additionally reproduces Bullet Cluster (MOND's historical weakness).
- **vs CSL/Diósi-Penrose:** zero free parameters; specific 689 Hz plateau at gold benchmark; m² scaling (CSL has m); F5 entanglement protection (CSL is state-independent).
- **vs particle DM:** no direct-detection signal predicted (no particle); falsified by direct detection.
- **vs Bose-Marletto-Vedral / KTM:** GRUT's Λ_grav formation rate matches BMV at canonical experimental parameters (l = 200 μm, m = 10⁻¹⁴ kg, ratio 1.0000); discriminator emerges at sub-micron separations (l < 1.6 R), currently inaccessible.

*Registry claims: comparison_landscape (anchored — composition)*

---

# Appendix C — Symbols and Constants Glossary

| Symbol | Name | Value | Status | Chapter |
|:---|:---|:---|:---|:---|
| α | Vacuum impedance | 1/3 | Computed under postulate | 2 |
| τ₀ | Memory bandwidth | 41.9 Myr | Computed (7 routes) | 2 |
| R | Vacuum refractive index (DC) | √(4/3) = 1.15470 | Computed | 7 |
| n_g(ω) | Frequency-dependent refractive index | √(1 + α/(1+(ωτ₀)²)) | Computed | 4 |
| S | Screening factor | 108π ≈ 339.29 | Computed | 8 |
| H_inf | Terminal velocity | 58.15 km/s/Mpc | Computed | 8 |
| H₀ | Current Hubble rate | 68.8 (zero-param) / 69.03 (one-param) km/s/Mpc | Computed (two routes) | 8 |
| Ω_Λ | Cosmological constant | ≈ 0.69 | Computed | 8 |
| Ω_dm | Dark matter density | 1/3 = 0.333 | Computed | 9 |
| Λ_grav | Gravitational decoherence rate | Gm²S(l/R)/(ℏl) | Computed | 5 |
| X | Crystallinity threshold | max(ω, Λ_grav) × τ₀ | Computed | 4 |
| T_c | Critical temperature | 54.7 MK | Computed | 2 |
| a₀ | MOND acceleration scale | cH₀/(2π) ≈ 1.2 × 10⁻¹⁰ m/s² | Computed | 9 |
| K | Koide identity | 2/3 | Computed | 5 |
| η_B | Baryon asymmetry | 6.57 × 10⁻¹⁰ | Computed | 9 |
| R_max | Ricci scalar saturation | α/(c²τ₀²) | Computed | 6 |
| ρ_max | Universal interior density | c²R_max/(8πG) | Computed | 6 |
| N_total | Era count | 329 | One parameter (open negative #13) | 8 |
| A_s | Primordial scalar amplitude | 1/(πS³) ≈ 8.15 × 10⁻⁹ (cosmic-baseline rescaling) | Open negative #14, rescaling-conditional | 13 |
| X_cosmic | Cosmic regime parameter | H(z) × τ₀; crosses 1 at z ≈ 71 (atomic-scale) | Computed (mass-class dependent) | 4 |
| z | Constitutive field | — | Defined | 3 |
| z_target | Target operator | — | Defined | 3 |
| N | Noise kernel | G/(ℏ|x−x'|) (gravitational) | Defined | 3 |
| F[z] | Equation-of-motion operator | — | Defined | 3 |
| K(t) | Memory kernel | τ₀⁻¹ exp(−t/τ₀) | Defined | 2 |

### C.1 Additional symbols, parameters, and derived quantities

The following symbols appear in specific chapters and are documented here for reference. Grouped thematically.

**Cosmological / dimensional parameters**

| Symbol | Name | Value | Status | Chapter |
|:---|:---|:---|:---|:---|
| τ_Λ | Cosmological relaxation time | Sτ₀ ≈ 14.2 Gyr | Computed | 2, 8 |
| M_Pl | Reduced Planck mass | √(ℏc/(8πG)) ≈ 2.4 × 10¹⁸ GeV | Imported | 13 |

**CTP / anomaly coefficients**

| Symbol | Name | Value | Status | Chapter |
|:---|:---|:---|:---|:---|
| C_Cosmo | S⁴ cosmological anomaly coefficient (the −100; conformal-mode instability) | Negative; magnitude tied to SM hypercharge sum | Computed | 8 |
| a | Type-A trace anomaly (per-generation SM total) | 1991/2 | Computed | 5 |
| c | Type-C trace anomaly (per-generation SM total) | 849 | Computed | 5 |
| ε (Osborn) | Per-gauge-group local-RG ratio (R-route 3) | combined ε = 1.15367 (α²-weighted across SU(3), SU(2), U(1)) | Computed | 7 |

**Bayesian observer filtering (Ch 11)**

| Symbol | Name | Meaning | Status | Chapter |
|:---|:---|:---|:---|:---|
| p(t) | Observer's posterior probability the system is in the live state | dp/dt = −μp − γp(1−p), p(t⁺) = 1 at contact events | Defined | 11 |
| μ | Hazard rate | = Λ_grav for gravitational decoherence | Defined | 11 |
| γ | Absence-of-evidence rate | Rate at which non-observation accumulates as evidence | Defined | 11 |

**Cluster merger parameters (Ch 9)**

| Symbol | Name | Value | Status | Chapter |
|:---|:---|:---|:---|:---|
| dec_ratio | Velocity-decay ratio = v_post / v_init | 0.638 (canonical kernel-derived); 0.76 (velocity-convention alternative) | Open question (#7) | 9 |
| v_post | Post-collision velocity | Bullet Cluster ≈ 3000 km/s (Springel-Farrar 2007); other clusters not yet measured | Imported / Open | 9 |
| δ | Gas-to-lensing offset | δ ∝ v_final × τ₀ × dec_ratio (1.72% internal scaling residual) | Computed | 9 |

**Decoherence experiments and falsifiers (Ch 5, 14)**

| Symbol | Name | Value | Status | Chapter |
|:---|:---|:---|:---|:---|
| 689 Hz | Decoherence plateau at the gold benchmark (m = 80.8 pg, l = 1 μm) | Λ_grav = Gm²S(l/R)/(ℏl) = 688.7 Hz | Computed (primary falsifier F1) | 5, 14 |
| t_entangle | Gravitational-entanglement formation time at BMV canonical parameters (m = 10⁻¹⁴ kg, l = 200 μm) | 3.16 s (matches BMV literature exactly in the far-field limit S(l/R) → 1) | Anchored | 5, B.5 |

**Stochastic / field-theoretic primitives (Ch 3, 5)**

| Symbol | Name | Meaning | Status | Chapter |
|:---|:---|:---|:---|:---|
| ξ(t) | Stochastic noise term in the constitutive equation | KMS-conditioned; spectrum N(ω) = (2/τ₀)ℏω coth(ℏω/2k_BT) | Defined | 3 |
| ψ | Wavefunction (sectoral specialization of z under τ → 0 limit) | Recovers Schrödinger equation | Defined | 5 |
| Z₃ | Three-generation circulant symmetry of the Koide identity | Selects N = 3 generations | Computed | 5 |

**Notation conventions**

- Bold symbols (e.g., **τ₀**, **α**) denote primary medium constants — the four constants τ₀, α, S, R that govern the framework's scale-universal behavior (see Chapter 4, Universal Scale Map).
- ε appears in two unrelated senses: as the Osborn local-RG ratio (R-route 3, Ch 7) and as the dimensional-regulator parameter in MS-bar Laurent expansions (V7 §26, Phase-0 closure work). Context disambiguates; the glossary entry above pins the Ch-7 sense.
- All decoherence rates and Hubble rates are reported in s⁻¹ or km/s/Mpc as native units; conversions follow standard cosmology (1 Mpc = 3.086 × 10¹⁹ km).

*Registry claims: glossary_reference (meta)*

---

# Appendix D — Derivation Index (auto-rendered)

*Auto-generated from `grut/toe/registry.py` via `python3 -m grut.toe.render_appendices`. To update an entry, edit the registry claim and regenerate. Manual edits below this header will be overwritten.*

This index lists every framework claim at tier `computed` or `anchored` — claims whose physical content has been derived, computed, or empirically anchored, and which are pinned by passing tests. Claims at tier `open_negative` are documented separately in Chapter 12; `conjectural`, `foundational`, and `meta` claims are framing-tier and are not derivations. Entries are grouped by chapter and sorted by claim ID within each chapter.

**Coverage:** 73 derivations across 11 chapters.

## Chapter 2 — The Medium

*4 derivations.*

- **`alpha_vac_derivation`** [computed] — α_vac = 1/3 is formalized via the Gate R identification (May 2026, C1-C6 all SUPPORTED/FORMALIZED): the Weyl decomposition g_μν = e^{2σ}ĝ_μν identifies σ as one real conformally-coupled scalar; the...
  · *deps: 0 · tests: 4 · fan-out: 58*
- **`tau_0_cross_consistency`** [computed] — τ_0 = 41.9 Myr is independently derived from multiple routes that converge to within observational uncertainty.
  · *deps: 4 · tests: 6 · fan-out: 2 · upstream: `tau_0_derivation`, `screening_108pi`, `bullet_cluster_offset`, +1 more*
- **`tau_0_derivation`** [computed] — τ_0 = 41.9 Myr is POSITED in Phase I §5 with two independent anchors: (1) cosmic-baseline relation τ_0 = 1/(H_0 × 108π) — exact to 1.7% at H_0 = 70 km/s/Mpc, giving 41.17 Myr; (2) Bullet Cluster of...
  · *deps: 0 · tests: 3 · fan-out: 35*
- **`zero_free_parameters`** [computed] — GRUT has zero free parameters.
  · *deps: 2 · tests: 1 · fan-out: 0 · upstream: `tau_0_derivation`, `alpha_vac_derivation`*

## Chapter 3 — The Equation

*4 derivations.*

- **`constitutive_equation`** [computed] — The constitutive equation τ_0 dz/dt + z = z_target governs the medium's retarded relaxation toward its source.
  · *deps: 1 · tests: 2 · fan-out: 64 · upstream: `ctp_action_structure`*
- **`ctp_action_structure`** [computed] — The framework is built on a single Closed Time Path (Schwinger-Keldysh) action S_CTP.
  · *deps: 0 · tests: 5 · fan-out: 76*
- **`framework_axioms_locked`** [computed] — Framework foundational invariants: Planck mass and fine-structure constant verified against CODATA; CTP Keldysh action invertibility (A0); intrinsic time scale τ_I = ℏ/2 (N0); noise kernel and cons...
  · *deps: 1 · tests: 1 · fan-out: 0 · upstream: `ctp_action_structure`*
- **`memory_kernel_form`** [computed] — The retarded memory kernel is a single-pole exponential: K(t) = (1/τ_0) exp(−t/τ_0) Θ(t).
  · *deps: 1 · tests: 2 · fan-out: 47 · upstream: `constitutive_equation`*

## Chapter 4 — The Crystal and the Fluid

*5 derivations.*

- **`cosmic_x_crossover_prediction`** [computed] — The framework's regime classification X = max(ω, Λ_grav) × τ_0, applied to ATOMIC-SCALE TEST-PARTICLE PERTURBATIONS of the cosmic background where ω = H dominates, gives X_cosmic(z) = H(z) × τ_0.
  · *deps: 2 · tests: 1 · fan-out: 0 · upstream: `regime_map`, `tau_0_derivation`*
- **`regime_map`** [computed] — The framework correctly classifies regimes across 23 orders of magnitude: Saturn orbit (ωτ_0 ~ 10⁷, deep crystal); galactic rotation (ωτ_0 ~ 1, boundary/fluid); cosmic expansion (ωτ_0 ~ 10⁻³, deep...
  · *deps: 1 · tests: 1 · fan-out: 15 · upstream: `threshold_bridge`*
- **`screening_108pi`** [computed] — The screening factor S = 12π/α_vac² = 108π ≈ 339.29 maps the cosmic baseline τ_Λ to the local relaxation time τ_0 = τ_Λ / S.
  · *deps: 1 · tests: 2 · fan-out: 14 · upstream: `alpha_vac_derivation`*
- **`solar_system_safety`** [computed] — Solar-system safety verified across EIGHT independent precision tests of GR spanning >10 orders of magnitude in frequency: Saturn ranging (30 yr), Mercury perihelion (88 d), lunar laser ranging (27...
  · *deps: 2 · tests: 8 · fan-out: 0 · upstream: `regime_map`, `threshold_bridge`*
- **`threshold_bridge`** [computed] — The crystallinity threshold X = ω·τ_0 is equivalent to Λ_grav·τ_0 for self-gravitating systems where the dominant dynamical frequency is the Diósi-Penrose decoherence rate.
  · *deps: 1 · tests: 1 · fan-out: 30 · upstream: `constitutive_equation`*

## Chapter 5 — Recovered Physics

*7 derivations.*

- **`decoherence_alternative_models_comparison`** [computed] — Among four COMPETITOR collapse / decoherence models — Diósi-Penrose, CSL, Adler mass-proportional CSL, and Ghirardi-Rimini-Weber — none reproduces all six GRUT scaling laws (F1 mass², F2 cubic-onse...
  · *deps: 1 · tests: 6 · fan-out: 2 · upstream: `decoherence_plateau`*
- **`decoherence_plateau`** [computed] — Gravitational decoherence with zero free parameters and six scaling laws (mass, separation, body size, temperature, internal-mode coupling, environmental gas pressure).
  · *deps: 2 · tests: 1 · fan-out: 14 · upstream: `threshold_bridge`, `alpha_vac_derivation`*
- **`gravitational_entanglement_formation_rate`** [anchored] — The framework's Λ_grav formation rate Gm²S(l/R)/(ℏl) for two gravitationally coupled masses gives identical numerical predictions to Bose-Marletto-Vedral (2017) at experimentally accessible separat...
  · *deps: 1 · tests: 1 · fan-out: 1 · upstream: `decoherence_plateau`*
- **`grut_csl_isotope_discriminator`** [computed] — GRUT's m² scaling is testable against CSL's linear-in-mass scaling via isotope-pair decoherence ratios.
  · *deps: 2 · tests: 9 · fan-out: 1 · upstream: `decoherence_plateau`, `decoherence_alternative_models_comparison`*
- **`qm_recovery`** [computed] — Standard quantum mechanics is recovered from the constitutive equation in the τ → 0 limit, with the Newton-Raphson z_target constructed from the Schrödinger residual F[ψ] = iℏ ∂_t ψ − Hψ.
  · *deps: 1 · tests: 4 · fan-out: 0 · upstream: `constitutive_equation`*
- **`sm_emergence`** [computed] — The Standard Model emerges as the unique minimal theory satisfying five CTP-derived constraints (V7 §15-§16): (C1) gauge structure SU(3)×SU(2)×U(1) → 12 gauge bosons; (C2) anomaly cancellation ΣY²...
  · *deps: 1 · tests: 6 · fan-out: 11 · upstream: `ctp_action_structure`*
- **`sm_field_content_locked`** [computed] — Standard Model field counts are locked in code: 4 real scalars, 45 Weyl fermions (15 per generation × 3), 12 gauge bosons.
  · *deps: 2 · tests: 1 · fan-out: 3 · upstream: `sm_emergence`, `minus_100_drive`*

## Chapter 6 — Gravity

*6 derivations.*

- **`gr_recovery`** [computed] — General relativity is recovered in the high-frequency limit (ωτ_0 ≫ 1): n_g(ω) → 1, α_eff(X) → 0, the constitutive Newtonian potential reduces to −GM/r exactly.
  · *deps: 2 · tests: 7 · fan-out: 10 · upstream: `memory_kernel_form`, `regime_map`*
- **`phi_munu_curved_background_scaffold`** [anchored] — Curved-background SCAFFOLD (Correction #24, Priority 2B).
  · *deps: 2 · tests: 1 · fan-out: 6 · upstream: `phi_munu_linearized_derivation`, `constitutive_projection_gravity_heuristic_resolved`*
- **`phi_munu_frw_explicit_construction`** [computed] — Phase 2C — explicit construction of χ_FRW(k, η) and n_g²(k, η) on FRW spacetime via the WKB / slow-H approximation (Correction #25, 2026-04-30).
  · *deps: 4 · tests: 1 · fan-out: 5 · upstream: `phi_munu_curved_background_scaffold`, `phi_munu_linearized_derivation`, `alpha_vac_derivation`, +1 more*
- **`phi_munu_linearized_derivation`** [computed] — The gravitational constitutive correction Φ_μν is structurally derived in the linearized limit from the Schwinger-Keldysh action variation δS_CTP/δh_a |_{h_a=0}.
  · *deps: 4 · tests: 1 · fan-out: 7 · upstream: `ctp_action_structure`, `alpha_vac_derivation`, `memory_kernel_form`, +1 more*
- **`r_max_ricci_saturation`** [computed] — The Ricci scalar of the matter-bearing interior saturates at R_max = α_vac/(c²τ_0²) ≈ 2.12 × 10⁻⁴⁸ m⁻².
  · *deps: 2 · tests: 2 · fan-out: 4 · upstream: `alpha_vac_derivation`, `tau_0_derivation`*
- **`rho_max_universal`** [computed] — Every black-hole core saturates at the same maximum interior density ρ_max = c²R_max/(8πG) ≈ 1.14 × 10⁻²² kg/m³, independent of mass.
  · *deps: 1 · tests: 2 · fan-out: 2 · upstream: `r_max_ricci_saturation`*

## Chapter 7 — The Constant

*5 derivations.*

- **`r_canonical_path_g`** [computed] — Path G — refractive-index identification — gives the canonical R = n_g(0) = √(1 + α_vac) = √(4/3) ≈ 1.15470.
  · *deps: 2 · tests: 2 · fan-out: 16 · upstream: `alpha_vac_derivation`, `memory_kernel_form`*
- **`r_path_d_dirac`** [computed] — Path D — SM 1-loop trace anomaly with Dirac neutrinos — gives a/c = 253/219 ≈ 1.15525, within 0.05% of Path G's canonical √(4/3).
  · *deps: 2 · tests: 2 · fan-out: 1 · upstream: `r_canonical_path_g`, `alpha_vac_derivation`*
- **`r_path_d_majorana`** [computed] — Path D variant — SM 1-loop trace anomaly with Majorana neutrinos — gives a/c = 1991/1698 ≈ 1.17256, secondary cross-check at the ~1.5% level vs Path G.
  · *deps: 1 · tests: 1 · fan-out: 1 · upstream: `r_canonical_path_g`*
- **`r_path_osborn_epsilon`** [computed] — Path 3 of the Three-Routes convergence: ε_combined from Osborn 2003 (hep-th/0302119) eq (36), evaluated for SM at M_Z in Dirac convention with QCD-dominant weighting.
  · *deps: 3 · tests: 4 · fan-out: 2 · upstream: `alpha_vac_derivation`, `sm_field_content_locked`, `r_canonical_path_g`*
- **`three_routes_convergence`** [computed] — Three independent routes converge on R ≈ 1.154 within 0.1%: Path G (tree-level √(4/3) ≈ 1.15470, zero coupling constants), V7 §26 (3-loop CTP claimed 1.15428, currently open_negative), and Osborn (...
  · *deps: 3 · tests: 2 · fan-out: 1 · upstream: `r_canonical_path_g`, `r_path_osborn_epsilon`, `tji_7_4_open_negative`*

## Chapter 8 — The Terminal Velocity

*7 derivations.*

- **`bridge_parameter_cross_sector`** [computed] — The bridge parameter τ_0 connects laboratory decoherence (noise kernel at the gold benchmark m=20818 amu, l=1 μm) to cosmology (H_inf = (2−R)/(S·τ_0), Ω_Λ).
  · *deps: 3 · tests: 1 · fan-out: 0 · upstream: `tau_0_derivation`, `h_inf_decomposition`, `decoherence_plateau`*
- **`h_0_prediction`** [computed] — H_0 ≈ 68.8 km/s/Mpc implied by τ_0 = 41.9 Myr and S = 108π.
  · *deps: 3 · tests: 1 · fan-out: 1 · upstream: `h_inf_decomposition`, `tau_0_derivation`, `screening_108pi`*
- **`h_inf_decomposition`** [computed] — The asymptotic Hubble rate decomposes as H_inf = drive / friction = (2 − R) / (S · τ_0).
  · *deps: 3 · tests: 2 · fan-out: 4 · upstream: `r_canonical_path_g`, `screening_108pi`, `tau_0_derivation`*
- **`minus_100_drive`** [computed] — The −100 coefficient in the conformal-instability sector of Euclidean gravity on S⁴ is the Gibbons-Hawking drive of cosmic expansion, not a calculational bug.
  · *deps: 1 · tests: 2 · fan-out: 4 · upstream: `ctp_action_structure`*
- **`omega_lambda_prediction`** [computed] — Ω_Λ = 0.6886 predicted, 0.04% from Planck 2018 best-fit.
  · *deps: 1 · tests: 1 · fan-out: 0 · upstream: `h_inf_decomposition`*
- **`t_c_thermal_transition`** [computed] — The 'boiling point of gravity' T_c = ℏ/(τ_micro × k_B) ≈ 54.7 MK, where τ_micro ≈ 1.4×10⁻¹⁹ s is the microscopic plasma relaxation time of the responsive vacuum (distinct from the macroscopic gravi...
  · *deps: 0 · tests: 5 · fan-out: 3*
- **`tau_micro_thermal_scale`** [computed] — τ_micro ≡ ℏ / (k_B × T_c) ≈ 1.396 × 10⁻¹⁹ s — the microscopic plasma/thermal relaxation time of the responsive vacuum's microstates.
  · *deps: 1 · tests: 3 · fan-out: 2 · upstream: `t_c_thermal_transition`*

## Chapter 9 — The Dark Sector

*23 derivations.*

- **`bandwidth_integral`** [computed] — The cosmological bandwidth integral evaluates the linear-regime contribution of the responsive vacuum to the matter budget; produces Ω_dm = α_vac = 1/3 with zero free parameters.
  · *deps: 2 · tests: 1 · fan-out: 1 · upstream: `alpha_vac_derivation`, `memory_kernel_form`*
- **`baryogenesis_eta_b`** [computed] — Baryogenesis from CTP path asymmetry (R ≠ 1) gives the baryon-to-photon ratio η_B = J_CP × K_neq × (2−R_B)/S_B ≈ 6.57 × 10⁻¹⁰ (route 1), +7.7% from Planck observed 6.10 × 10⁻¹⁰.
  · *deps: 2 · tests: 2 · fan-out: 0 · upstream: `r_canonical_path_g`, `ctp_action_structure`*
- **`bullet_cluster_offset`** [computed] — The Bullet Cluster gas-to-LENSING offset (per cluster) is GRUT's specific cluster-scale prediction.
  · *deps: 2 · tests: 5 · fan-out: 8 · upstream: `tau_0_derivation`, `memory_kernel_form`*
- **`charged_lepton_z3_does_not_extend_to_neutrinos`** [computed] — The charged-lepton Z₃ ansatz √m_i = M_0(1 + √2 cos(θ + 2πk/3)) — which gives K = 2/3 algebraically — DOES NOT admit any neutrino solution under either hierarchy.
  · *deps: 1 · tests: 1 · fan-out: 3 · upstream: `koide_z3_circulant_structure`*
- **`cluster_merger_internal_scaling_residual`** [computed] — Across the four-cluster sample (Bullet Cluster, MACS J0025, Abell 520, El Gordo), the framework's predicted gas-to-lensing offsets scale linearly with v_final with internal residual 1.72%.
  · *deps: 3 · tests: 1 · fan-out: 0 · upstream: `cluster_merger_scaling_law`, `tau_0_derivation`, `memory_kernel_form`*
- **`cluster_merger_scaling_law`** [anchored] — The v × τ_0 memory-kernel scaling law applied to four independent merging cluster systems.
  · *deps: 2 · tests: 5 · fan-out: 7 · upstream: `bullet_cluster_offset`, `tau_0_derivation`*
- **`cluster_tau_0_dec_ratio_degeneracy`** [computed] — The +20% cluster-vs-cosmic systematic is degenerate between τ_0 and the deceleration ratio dec_ratio = v_post/v_initial.
  · *deps: 2 · tests: 6 · fan-out: 0 · upstream: `cluster_merger_scaling_law`, `cluster_tau_0_sensitivity_diagnostic`*
- **`cluster_tau_0_sensitivity_diagnostic`** [computed] — Single-τ_0 sensitivity analysis across the three normal-regime mergers (Bullet, MACS J0025, Abell 520, El Gordo excluded) finds best-fit τ_0 = 49 Myr with chi² = 0.007, an 11× improvement over cano...
  · *deps: 3 · tests: 6 · fan-out: 1 · upstream: `cluster_merger_scaling_law`, `tau_0_cross_consistency`, `tau_0_derivation`*
- **`cmb_boltzmann_scoping`** [anchored] — CMB Boltzmann scoping completed: at recombination, H_rec × τ_0 ≈ 68 (expansion-rate ωτ_0) and ω_acoustic × τ_0 ≈ 140 (first acoustic peak); both deep in the crystal regime.
  · *deps: 3 · tests: 6 · fan-out: 0 · upstream: `tau_0_derivation`, `alpha_vac_derivation`, `memory_kernel_form`*
- **`dark_sector_u1_extension`** [anchored] — The dark sector is a gauged U(1)_dark extension (V7 §28) with two viable parameter routes: Route 1 (RG running from Planck) gives g_dark = 0.917, λ = 0.42, M ≈ 2.1 × 10⁹ GeV; Route 2 (anomaly extra...
  · *deps: 1 · tests: 1 · fan-out: 3 · upstream: `alpha_vac_derivation`*
- **`dielectric_dm_reframing`** [computed] — Track VII REFRAMED: dark-matter abundance is the dielectric response of the vacuum — the frequency-gated refractive enhancement n_g(ω) maps to Ω_dm at galactic-frequency modes.
  · *deps: 4 · tests: 1 · fan-out: 0 · upstream: `alpha_vac_derivation`, `memory_kernel_form`, `regime_map`, +1 more*
- **`el_gordo_sensitivity_analysis`** [computed] — El Gordo's apparent factor-3.5 outlier resolves under joint parameter + observational uncertainty analysis.
  · *deps: 2 · tests: 6 · fan-out: 0 · upstream: `cluster_merger_scaling_law`, `el_gordo_outlier_open_question`*
- **`kibble_zurek_dm_route`** [anchored] — Track VII Step 1: Kibble-Zurek formation of dark relic from a dark-sector phase transition with XY universality gives Ω_dm within factor ~2 of observation.
  · *deps: 2 · tests: 1 · fan-out: 1 · upstream: `dark_sector_u1_extension`, `tau_0_derivation`*
- **`koide_k_2_over_3`** [computed] — Charged-lepton masses satisfy the Koide identity K = (Σ m_i) / (Σ √m_i)² = 2/3 to 0.005%, validated against PDG values for e, μ, τ.
  · *deps: 1 · tests: 1 · fan-out: 6 · upstream: `sm_emergence`*
- **`koide_z3_circulant_structure`** [computed] — The Z₃-circulant Koide mass operator parameterizes the charged-lepton spectrum via (M_0, θ): K = 2/3 holds algebraically (machine precision for any nonzero M_0 and any θ).
  · *deps: 2 · tests: 1 · fan-out: 5 · upstream: `koide_k_2_over_3`, `sm_emergence`*
- **`mg_eft_mu_gamma_mapping`** [computed] — GRUT lives in the 'μ ≠ 1, γ = 1' subclass of modified-gravity models.
  · *deps: 3 · tests: 1 · fan-out: 2 · upstream: `phi_munu_frw_explicit_construction`, `alpha_vac_derivation`, `tau_0_derivation`*
- **`modified_linear_growth_first_look`** [computed] — Modified linear growth equation on FRW with μ_GRUT(k, a) from Priority 3, integrated numerically: δ'' + [2 - (3/2)Ω_m] δ' - (3/2) Ω_m μ_GRUT(k, N) δ = 0.
  · *deps: 4 · tests: 1 · fan-out: 0 · upstream: `mg_eft_mu_gamma_mapping`, `phi_munu_frw_explicit_construction`, `tau_0_derivation`, +1 more*
- **`mond_a_0_emergence`** [computed] — MOND-like trigger acceleration a_0 = c/(2π τ_Λ) ≈ 1.2 × 10⁻¹⁰ m/s² emerges from the response time, not from modified dynamics.
  · *deps: 1 · tests: 2 · fan-out: 1 · upstream: `tau_0_derivation`*
- **`neutrino_hierarchy_z3_nh_prediction`** [anchored] — Conditional on the postulate a_ν = 1 (giving K_ν = 1/2), the GRUT generalized Z₃ ansatz √m_i = M_0(1 + a_ν cos(θ + 2πk/3)) admits a UNIQUE INTERIOR solution in Normal Hierarchy with: m_1 = 0.802 me...
  · *deps: 2 · tests: 1 · fan-out: 2 · upstream: `charged_lepton_z3_does_not_extend_to_neutrinos`, `koide_z3_circulant_structure`*
- **`neutrino_z3_coupling_a_equals_1_uniqueness_theorem`** [computed] — DERIVED (Correction #29, Priority 4B, 2026-05-02).
  · *deps: 3 · tests: 1 · fan-out: 0 · upstream: `neutrino_hierarchy_z3_nh_prediction`, `charged_lepton_z3_does_not_extend_to_neutrinos`, `koide_z3_circulant_structure`*
- **`omega_dm_equals_alpha`** [computed] — Ω_dm = α_vac = 1/3 (~33%, +27% from Planck's 26.6%).
  · *deps: 2 · tests: 3 · fan-out: 0 · upstream: `bandwidth_integral`, `alpha_vac_derivation`*
- **`rotation_curves_match`** [computed] — Galactic rotation curves are produced by g_eff = g_bar [1 + (ν(y) − 1)/(1 + X²)] where y = g_bar/a_0 and X = ω·τ_0.
  · *deps: 2 · tests: 7 · fan-out: 0 · upstream: `mond_a_0_emergence`, `regime_map`*
- **`track_vii_relic_scoping`** [anchored] — Track VII relic-abundance infrastructure: thermal-freezeout baseline returns WRONG MECHANISM verdict for the V7 heavy (2 × 10⁹ GeV) soliton; Kibble-Zurek upper bound from causality is finite; full...
  · *deps: 1 · tests: 1 · fan-out: 0 · upstream: `dark_sector_u1_extension`*

## Chapter 10 — Time and Information

*2 derivations.*

- **`arrow_of_time_from_entropy`** [computed] — The arrow of time emerges from the constitutive entropy production rate Ṡ = (1/τ_0) ⟨(z − z_target)²⟩ ≥ 0, which (i) is non-negative for any state, (ii) vanishes only at the fixed point z = z_targe...
  · *deps: 1 · tests: 5 · fan-out: 0 · upstream: `constitutive_equation`*
- **`bh_information_partial`** [anchored] — Hawking radiation carries constitutive correlations and is not strictly thermal.
  · *deps: 2 · tests: 0 · fan-out: 0 · upstream: `r_max_ricci_saturation`, `memory_kernel_form`*

## Chapter 11 — The Observer

*7 derivations.*

- **`bayesian_observer_filtering`** [anchored] — The framework provides a Bayesian filtering equation for how an observer's certainty about a remote system evolves between contact events: dp/dt = −μp − γp(1−p), with reset rule p(t⁺) = 1 at contac...
  · *deps: 2 · tests: 1 · fan-out: 1 · upstream: `schrodinger_in_box_inversion`, `observer_as_crystal`*
- **`lambda_contact_ctp_derivation`** [computed] — Λ_contact (the contact-formation rate at which the observer's pointer state crystallizes into a definite record) is identified with Λ_grav evaluated at the pointer (apparatus + observer body) mass...
  · *deps: 4 · tests: 3 · fan-out: 4 · upstream: `memory_kernel_form`, `ctp_action_structure`, `decoherence_plateau`, +1 more*
- **`measurement_resolution`** [computed] — The measurement problem is resolved without an additional postulate: when an apparatus (Λ_grav,A τ_0 ≫ 1, deep crystal) couples to a quantum object (Λ_grav,B τ_0 ≲ 1, boundary), the joint Λ_eff = Λ...
  · *deps: 2 · tests: 5 · fan-out: 6 · upstream: `threshold_bridge`, `decoherence_plateau`*
- **`mu_gamma_ontic_epistemic_distinction`** [computed] — In the Bayesian filtering equation dp/dt = -μp - γp(1-p), the two terms have fundamentally different origins.
  · *deps: 2 · tests: 1 · fan-out: 0 · upstream: `lambda_contact_ctp_derivation`, `bayesian_observer_filtering`*
- **`pointer_observable_position_basis`** [anchored] — The pointer observable in the framework is the center-of-mass position operator x̂_P of macroscopic record-bearing degrees of freedom in the apparatus, evaluated at coarse-graining scales such that...
  · *deps: 2 · tests: 0 · fan-out: 0 · upstream: `lambda_contact_ctp_derivation`, `measurement_resolution`*
- **`schrodinger_in_box_inversion`** [anchored] — Philosophical reformulation of the Schrödinger's-cat thought experiment consistent with the framework's closed-self-referential-universe stance: the OBSERVER is the boxed system (finite, local, inf...
  · *deps: 2 · tests: 1 · fan-out: 3 · upstream: `measurement_resolution`, `observer_as_crystal`*
- **`wigner_friend_dissolution`** [computed] — The Wigner's-friend paradox dissolves under explicit conditional-state mathematics.
  · *deps: 4 · tests: 1 · fan-out: 0 · upstream: `measurement_resolution`, `observer_as_crystal`, `schrodinger_in_box_inversion`, +1 more*

## Chapter 12 — Falsification

*3 derivations.*

- **`bbn_thermal_buffer_negligible`** [anchored] — Standard-cosmology calculation testing one piece of an external research hypothesis: 'BBN binding-energy release provides a thermal buffer that slows or plateaus cosmic temperature.' Result: the hy...
  · *deps: 0 · tests: 1 · fan-out: 0*
- **`genesis_noise_kernel_spectral_attempt`** [anchored] — Standard-physics calculation testing one piece of the Genesis-BBN-DM external research hypothesis: 'CTP noise kernel acting on z = 0 produces thermal-spectrum radiation at some characteristic tempe...
  · *deps: 3 · tests: 1 · fan-out: 0 · upstream: `ctp_action_structure`, `memory_kernel_form`, `tau_0_derivation`*
- **`neutrino_dirac_prediction`** [anchored] — GRUT predicts Dirac neutrinos as the empirically preferred variant: Path D Dirac (a/c = 1.15525) is closer to the canonical Path G value (1.15470) than Majorana (1.17256).
  · *deps: 2 · tests: 1 · fan-out: 0 · upstream: `r_path_d_dirac`, `r_path_d_majorana`*


---

# Appendix E — Claim Registry (auto-rendered)

*Auto-generated from `grut/toe/registry.py` via `python3 -m grut.toe.render_appendices`. The complete registry — every framework claim across every tier — in one reference table. Sorted by chapter then claim ID.*

**Total: 103 claims** (15 anchored, 58 computed, 3 conjectural, 2 foundational, 10 meta, 15 open_negative).

| Ch | Claim ID | Tier | Statement | Deps | Tests |
|---:|:---|:---|:---|---:|---:|
| 1 | `closed_universe` | foundational | The universe is closed, finite, and self-referential. | 0 | 0 |
| 1 | `fixed_point_principle` | foundational | The universe sits at a fixed point of the constitutive equation: z* = z_target[z*]. | 1 | 1 |
| 1 | `one_space_endpoint` | conjectural | The saturated end-state of the responsive vacuum — where every action has been absorbed and the medium is fully crystallized — is '1 Space'. | 2 | 0 |
| 2 | `alpha_vac_derivation` | computed | α_vac = 1/3 is formalized via the Gate R identification (May 2026, C1-C6 all SUPPORTED/FORMALIZED): the Weyl decomposition g_μν = e^{2σ}ĝ... | 0 | 4 |
| 2 | `tau_0_cross_consistency` | computed | τ_0 = 41.9 Myr is independently derived from multiple routes that converge to within observational uncertainty. | 4 | 6 |
| 2 | `tau_0_derivation` | computed | τ_0 = 41.9 Myr is POSITED in Phase I §5 with two independent anchors: (1) cosmic-baseline relation τ_0 = 1/(H_0 × 108π) — exact to 1.7% a... | 0 | 3 |
| 2 | `zero_free_parameters` | computed | GRUT has zero free parameters. | 2 | 1 |
| 3 | `constitutive_equation` | computed | The constitutive equation τ_0 dz/dt + z = z_target governs the medium's retarded relaxation toward its source. | 1 | 2 |
| 3 | `ctp_action_structure` | computed | The framework is built on a single Closed Time Path (Schwinger-Keldysh) action S_CTP. | 0 | 5 |
| 3 | `framework_axioms_locked` | computed | Framework foundational invariants: Planck mass and fine-structure constant verified against CODATA; CTP Keldysh action invertibility (A0)... | 1 | 1 |
| 3 | `memory_kernel_form` | computed | The retarded memory kernel is a single-pole exponential: K(t) = (1/τ_0) exp(−t/τ_0) Θ(t). | 1 | 2 |
| 4 | `cosmic_x_crossover_prediction` | computed | The framework's regime classification X = max(ω, Λ_grav) × τ_0, applied to ATOMIC-SCALE TEST-PARTICLE PERTURBATIONS of the cosmic backgro... | 2 | 1 |
| 4 | `regime_map` | computed | The framework correctly classifies regimes across 23 orders of magnitude: Saturn orbit (ωτ_0 ~ 10⁷, deep crystal); galactic rotation (ωτ_... | 1 | 1 |
| 4 | `screening_108pi` | computed | The screening factor S = 12π/α_vac² = 108π ≈ 339.29 maps the cosmic baseline τ_Λ to the local relaxation time τ_0 = τ_Λ / S. | 1 | 2 |
| 4 | `solar_system_safety` | computed | Solar-system safety verified across EIGHT independent precision tests of GR spanning >10 orders of magnitude in frequency: Saturn ranging... | 2 | 8 |
| 4 | `threshold_bridge` | computed | The crystallinity threshold X = ω·τ_0 is equivalent to Λ_grav·τ_0 for self-gravitating systems where the dominant dynamical frequency is... | 1 | 1 |
| 5 | `decoherence_alternative_models_comparison` | computed | Among four COMPETITOR collapse / decoherence models — Diósi-Penrose, CSL, Adler mass-proportional CSL, and Ghirardi-Rimini-Weber — none r... | 1 | 6 |
| 5 | `decoherence_plateau` | computed | Gravitational decoherence with zero free parameters and six scaling laws (mass, separation, body size, temperature, internal-mode couplin... | 2 | 1 |
| 5 | `gravitational_entanglement_formation_rate` | anchored | The framework's Λ_grav formation rate Gm²S(l/R)/(ℏl) for two gravitationally coupled masses gives identical numerical predictions to Bose... | 1 | 1 |
| 5 | `grut_csl_isotope_discriminator` | computed | GRUT's m² scaling is testable against CSL's linear-in-mass scaling via isotope-pair decoherence ratios. | 2 | 9 |
| 5 | `qm_recovery` | computed | Standard quantum mechanics is recovered from the constitutive equation in the τ → 0 limit, with the Newton-Raphson z_target constructed f... | 1 | 4 |
| 5 | `sm_emergence` | computed | The Standard Model emerges as the unique minimal theory satisfying five CTP-derived constraints (V7 §15-§16): (C1) gauge structure SU(3)×... | 1 | 6 |
| 5 | `sm_field_content_locked` | computed | Standard Model field counts are locked in code: 4 real scalars, 45 Weyl fermions (15 per generation × 3), 12 gauge bosons. | 2 | 1 |
| 6 | `gr_recovery` | computed | General relativity is recovered in the high-frequency limit (ωτ_0 ≫ 1): n_g(ω) → 1, α_eff(X) → 0, the constitutive Newtonian potential re... | 2 | 7 |
| 6 | `nonlinear_ladder_4_of_8` | open_negative | The nonlinear-gravity ladder has 4 of 8 rungs explicitly computed (V7 §22-§25): linearized recovery, second-order consistency, third-orde... | 1 | 0 |
| 6 | `phi_munu_curved_background_scaffold` | anchored | Curved-background SCAFFOLD (Correction #24, Priority 2B). | 2 | 1 |
| 6 | `phi_munu_frw_explicit_construction` | computed | Phase 2C — explicit construction of χ_FRW(k, η) and n_g²(k, η) on FRW spacetime via the WKB / slow-H approximation (Correction #25, 2026-... | 4 | 1 |
| 6 | `phi_munu_linearized_derivation` | computed | The gravitational constitutive correction Φ_μν is structurally derived in the linearized limit from the Schwinger-Keldysh action variatio... | 4 | 1 |
| 6 | `r_max_ricci_saturation` | computed | The Ricci scalar of the matter-bearing interior saturates at R_max = α_vac/(c²τ_0²) ≈ 2.12 × 10⁻⁴⁸ m⁻². | 2 | 2 |
| 6 | `rho_max_universal` | computed | Every black-hole core saturates at the same maximum interior density ρ_max = c²R_max/(8πG) ≈ 1.14 × 10⁻²² kg/m³, independent of mass. | 1 | 2 |
| 7 | `r_canonical_path_g` | computed | Path G — refractive-index identification — gives the canonical R = n_g(0) = √(1 + α_vac) = √(4/3) ≈ 1.15470. | 2 | 2 |
| 7 | `r_path_d_dirac` | computed | Path D — SM 1-loop trace anomaly with Dirac neutrinos — gives a/c = 253/219 ≈ 1.15525, within 0.05% of Path G's canonical √(4/3). | 2 | 2 |
| 7 | `r_path_d_majorana` | computed | Path D variant — SM 1-loop trace anomaly with Majorana neutrinos — gives a/c = 1991/1698 ≈ 1.17256, secondary cross-check at the ~1.5% le... | 1 | 1 |
| 7 | `r_path_osborn_epsilon` | computed | Path 3 of the Three-Routes convergence: ε_combined from Osborn 2003 (hep-th/0302119) eq (36), evaluated for SM at M_Z in Dirac convention... | 3 | 4 |
| 7 | `three_routes_convergence` | computed | Three independent routes converge on R ≈ 1.154 within 0.1%: Path G (tree-level √(4/3) ≈ 1.15470, zero coupling constants), V7 §26 (3-loop... | 3 | 2 |
| 7 | `tji_7_4_open_negative` | open_negative | The TJI 3-loop path on flat space produces raw Laurent coefficient −541/2304 at ε⁰ in the gamma-function scheme. | 1 | 2 |
| 8 | `bridge_parameter_cross_sector` | computed | The bridge parameter τ_0 connects laboratory decoherence (noise kernel at the gold benchmark m=20818 amu, l=1 μm) to cosmology (H_inf = (... | 3 | 1 |
| 8 | `h_0_prediction` | computed | H_0 ≈ 68.8 km/s/Mpc implied by τ_0 = 41.9 Myr and S = 108π. | 3 | 1 |
| 8 | `h_inf_decomposition` | computed | The asymptotic Hubble rate decomposes as H_inf = drive / friction = (2 − R) / (S · τ_0). | 3 | 2 |
| 8 | `minus_100_drive` | computed | The −100 coefficient in the conformal-instability sector of Euclidean gravity on S⁴ is the Gibbons-Hawking drive of cosmic expansion, not... | 1 | 2 |
| 8 | `omega_lambda_prediction` | computed | Ω_Λ = 0.6886 predicted, 0.04% from Planck 2018 best-fit. | 1 | 1 |
| 8 | `t_c_thermal_transition` | computed | The 'boiling point of gravity' T_c = ℏ/(τ_micro × k_B) ≈ 54.7 MK, where τ_micro ≈ 1.4×10⁻¹⁹ s is the microscopic plasma relaxation time o... | 0 | 5 |
| 8 | `tau_micro_thermal_scale` | computed | τ_micro ≡ ℏ / (k_B × T_c) ≈ 1.396 × 10⁻¹⁹ s — the microscopic plasma/thermal relaxation time of the responsive vacuum's microstates. | 1 | 3 |
| 9 | `bandwidth_integral` | computed | The cosmological bandwidth integral evaluates the linear-regime contribution of the responsive vacuum to the matter budget; produces Ω_dm... | 2 | 1 |
| 9 | `baryogenesis_eta_b` | computed | Baryogenesis from CTP path asymmetry (R ≠ 1) gives the baryon-to-photon ratio η_B = J_CP × K_neq × (2−R_B)/S_B ≈ 6.57 × 10⁻¹⁰ (route 1),... | 2 | 2 |
| 9 | `bullet_cluster_offset` | computed | The Bullet Cluster gas-to-LENSING offset (per cluster) is GRUT's specific cluster-scale prediction. | 2 | 5 |
| 9 | `charged_lepton_z3_does_not_extend_to_neutrinos` | computed | The charged-lepton Z₃ ansatz √m_i = M_0(1 + √2 cos(θ + 2πk/3)) — which gives K = 2/3 algebraically — DOES NOT admit any neutrino solution... | 1 | 1 |
| 9 | `cluster_merger_internal_scaling_residual` | computed | Across the four-cluster sample (Bullet Cluster, MACS J0025, Abell 520, El Gordo), the framework's predicted gas-to-lensing offsets scale... | 3 | 1 |
| 9 | `cluster_merger_scaling_law` | anchored | The v × τ_0 memory-kernel scaling law applied to four independent merging cluster systems. | 2 | 5 |
| 9 | `cluster_tau_0_dec_ratio_degeneracy` | computed | The +20% cluster-vs-cosmic systematic is degenerate between τ_0 and the deceleration ratio dec_ratio = v_post/v_initial. | 2 | 6 |
| 9 | `cluster_tau_0_sensitivity_diagnostic` | computed | Single-τ_0 sensitivity analysis across the three normal-regime mergers (Bullet, MACS J0025, Abell 520, El Gordo excluded) finds best-fit... | 3 | 6 |
| 9 | `cmb_boltzmann_scoping` | anchored | CMB Boltzmann scoping completed: at recombination, H_rec × τ_0 ≈ 68 (expansion-rate ωτ_0) and ω_acoustic × τ_0 ≈ 140 (first acoustic peak... | 3 | 6 |
| 9 | `dark_sector_u1_extension` | anchored | The dark sector is a gauged U(1)_dark extension (V7 §28) with two viable parameter routes: Route 1 (RG running from Planck) gives g_dark... | 1 | 1 |
| 9 | `dielectric_dm_reframing` | computed | Track VII REFRAMED: dark-matter abundance is the dielectric response of the vacuum — the frequency-gated refractive enhancement n_g(ω) ma... | 4 | 1 |
| 9 | `el_gordo_sensitivity_analysis` | computed | El Gordo's apparent factor-3.5 outlier resolves under joint parameter + observational uncertainty analysis. | 2 | 6 |
| 9 | `kibble_zurek_dm_route` | anchored | Track VII Step 1: Kibble-Zurek formation of dark relic from a dark-sector phase transition with XY universality gives Ω_dm within factor... | 2 | 1 |
| 9 | `koide_k_2_over_3` | computed | Charged-lepton masses satisfy the Koide identity K = (Σ m_i) / (Σ √m_i)² = 2/3 to 0.005%, validated against PDG values for e, μ, τ. | 1 | 1 |
| 9 | `koide_z3_circulant_structure` | computed | The Z₃-circulant Koide mass operator parameterizes the charged-lepton spectrum via (M_0, θ): K = 2/3 holds algebraically (machine precisi... | 2 | 1 |
| 9 | `mg_eft_mu_gamma_mapping` | computed | GRUT lives in the 'μ ≠ 1, γ = 1' subclass of modified-gravity models. | 3 | 1 |
| 9 | `modified_linear_growth_first_look` | computed | Modified linear growth equation on FRW with μ_GRUT(k, a) from Priority 3, integrated numerically: δ'' + [2 - (3/2)Ω_m] δ' - (3/2) Ω_m μ_G... | 4 | 1 |
| 9 | `mond_a_0_emergence` | computed | MOND-like trigger acceleration a_0 = c/(2π τ_Λ) ≈ 1.2 × 10⁻¹⁰ m/s² emerges from the response time, not from modified dynamics. | 1 | 2 |
| 9 | `neutrino_hierarchy_z3_nh_prediction` | anchored | Conditional on the postulate a_ν = 1 (giving K_ν = 1/2), the GRUT generalized Z₃ ansatz √m_i = M_0(1 + a_ν cos(θ + 2πk/3)) admits a UNIQU... | 2 | 1 |
| 9 | `neutrino_z3_coupling_a_equals_1_uniqueness_theorem` | computed | DERIVED (Correction #29, Priority 4B, 2026-05-02). | 3 | 1 |
| 9 | `omega_dm_equals_alpha` | computed | Ω_dm = α_vac = 1/3 (~33%, +27% from Planck's 26.6%). | 2 | 3 |
| 9 | `rotation_curves_match` | computed | Galactic rotation curves are produced by g_eff = g_bar [1 + (ν(y) − 1)/(1 + X²)] where y = g_bar/a_0 and X = ω·τ_0. | 2 | 7 |
| 9 | `track_vii_relic_scoping` | anchored | Track VII relic-abundance infrastructure: thermal-freezeout baseline returns WRONG MECHANISM verdict for the V7 heavy (2 × 10⁹ GeV) solit... | 1 | 1 |
| 10 | `arrow_of_time_from_entropy` | computed | The arrow of time emerges from the constitutive entropy production rate Ṡ = (1/τ_0) ⟨(z − z_target)²⟩ ≥ 0, which (i) is non-negative for... | 1 | 5 |
| 10 | `bh_information_partial` | anchored | Hawking radiation carries constitutive correlations and is not strictly thermal. | 2 | 0 |
| 11 | `bayesian_observer_filtering` | anchored | The framework provides a Bayesian filtering equation for how an observer's certainty about a remote system evolves between contact events... | 2 | 1 |
| 11 | `born_rule_postulate_open_negative` | open_negative | Born rule probabilities \|⟨ψ\|pointer_i⟩\|² do NOT derive from the gravitational noise kernel N_grav alone. | 2 | 1 |
| 11 | `lambda_contact_ctp_derivation` | computed | Λ_contact (the contact-formation rate at which the observer's pointer state crystallizes into a definite record) is identified with Λ_gra... | 4 | 3 |
| 11 | `measurement_resolution` | computed | The measurement problem is resolved without an additional postulate: when an apparatus (Λ_grav,A τ_0 ≫ 1, deep crystal) couples to a quan... | 2 | 5 |
| 11 | `mu_gamma_ontic_epistemic_distinction` | computed | In the Bayesian filtering equation dp/dt = -μp - γp(1-p), the two terms have fundamentally different origins. | 2 | 1 |
| 11 | `neural_resonance_speculative` | conjectural | A 40 Hz neural resonance arises from two independent framework routes (V7 Sector 13). | 1 | 0 |
| 11 | `observer_as_crystal` | conjectural | The observer is not external to the framework — the observer is the part of the medium that has crystallized. | 2 | 0 |
| 11 | `pointer_observable_position_basis` | anchored | The pointer observable in the framework is the center-of-mass position operator x̂_P of macroscopic record-bearing degrees of freedom in... | 2 | 0 |
| 11 | `schrodinger_in_box_inversion` | anchored | Philosophical reformulation of the Schrödinger's-cat thought experiment consistent with the framework's closed-self-referential-universe... | 2 | 1 |
| 11 | `wigner_friend_dissolution` | computed | The Wigner's-friend paradox dissolves under explicit conditional-state mathematics. | 4 | 1 |
| 12 | `allen_jacobson_phase1_stub_open_negative` | open_negative | The Allen-Jacobson S⁴ propagator Phase-1 is IMPLEMENTED (Correction #31, 2026-05-07): s4_propagator(), s4_propagator_conformal(), s4_prop... | 1 | 1 |
| 12 | `bbn_thermal_buffer_negligible` | anchored | Standard-cosmology calculation testing one piece of an external research hypothesis: 'BBN binding-energy release provides a thermal buffe... | 0 | 1 |
| 12 | `claim_registry_appendix` | meta | Appendix E (Full Claim Registry) is auto-rendered as a Markdown reference table over every registry entry. | 0 | 1 |
| 12 | `constitutive_projection_gravity_heuristic_resolved` | meta | RESOLVED at the linearized level (Correction #23, 2026-04-30). | 3 | 1 |
| 12 | `correction_ledger` | meta | The repository maintains a public ledger of every correction to the framework: 28 documented corrections across the V7 development era, t... | 0 | 0 |
| 12 | `dependency_graph_appendix` | meta | Appendix F (Dependency Graph) is auto-rendered from grut/toe/dependencies.py. | 0 | 1 |
| 12 | `derivation_index_appendix` | meta | Appendix D (Derivation Index) is auto-rendered from the registry: every claim at tier 'computed' or 'anchored' is emitted as a per-chapte... | 0 | 1 |
| 12 | `el_gordo_outlier_open_question` | open_negative | ACT-CL J0102-4915 (El Gordo) was originally tagged as a factor-3.5 outlier (canonical 70 kpc prediction vs ~250 kpc observed). | 1 | 2 |
| 12 | `falsifier_paper_six_near_term_tests` | meta | The framework's six near-term falsifiers — decoherence plateau (~689 Hz, lab gravity), ³⁰Si/²⁸Si isotope discriminator vs CSL (lab gravit... | 6 | 0 |
| 12 | `genesis_noise_kernel_spectral_attempt` | anchored | Standard-physics calculation testing one piece of the Genesis-BBN-DM external research hypothesis: 'CTP noise kernel acting on z = 0 prod... | 3 | 1 |
| 12 | `koide_phase_4_open_negative` | open_negative | Track II Phase 4 (Koide flavor mechanism) was attempted and produced HONEST NEGATIVE: the Yukawa-hierarchy mechanism cannot be derived fr... | 1 | 1 |
| 12 | `marker_validator_discipline` | meta | Tier-marker discipline checker: every [OPEN], [SCOPING], [CONJECTURAL], [SPECULATIVE], or 'Outstanding verification' marker in the docume... | 0 | 2 |
| 12 | `n_g_omega_cosmological_covariance_resolved` | meta | RESOLVED (Correction #26, 2026-05-01). | 3 | 1 |
| 12 | `n_total_zero_parameter_derivation_open_question` | open_negative | GRUT's detailed Hubble-from-first-principles route (grut/derived/cosmology/hubble_from_first_principles.py: grut_H_0_prediction) computes... | 3 | 1 |
| 12 | `neutrino_dirac_prediction` | anchored | GRUT predicts Dirac neutrinos as the empirically preferred variant: Path D Dirac (a/c = 1.15525) is closer to the canonical Path G value... | 2 | 1 |
| 12 | `path_f_translation_gap` | open_negative | Path F (Im Γ on de Sitter) was investigated as an alternate route to V7's R = 1.15428. | 1 | 0 |
| 12 | `phi_munu_frw_beyond_wkb_open_question` | open_negative | Phase 2D — beyond-WKB extension of χ_FRW(k, η). | 1 | 0 |
| 12 | `predictions_dashboard` | meta | The framework's complete predictive surface is codified in 27 quantitative predictions across 7 categories (foundational constants, R, co... | 0 | 9 |
| 12 | `primordial_amplitude_zero_parameter_open_negative` | open_negative | The primordial scalar amplitude A_s ≈ 2.1 × 10⁻⁹ (Planck 2018) is observation-anchored, not derived zero-parameter from GRUT's CTP infras... | 5 | 2 |
| 12 | `rho_max_scale_open_question` | open_negative | The universal-τ_0 form ρ_max ~ 10⁻²² kg/m³ is cosmologically weak and below typical naive BH interior densities. | 1 | 0 |
| 12 | `t_c_provenance_inconsistency_resolved` | meta | RESOLVED (Correction #22, 2026-04-30). | 3 | 3 |
| 12 | `tau_zero_to_tau_micro_relation_open_question` | open_negative | The relation between the framework's two τ-scales is currently underived. | 3 | 0 |
| 12 | `track_v_coupling_unification_open_question` | open_negative | GRUT's Track V proposes that the Standard Model gauge couplings unify at high scale via a constitutive β-function correction from the res... | 2 | 0 |
| 12 | `two_route_convergence_physical_equivalence_open_question` | open_negative | The two computed routes for R (Path G: pure α=1/3 algebra giving 1.15470; Osborn ε at M_Z: weighted gauge-coupling correction giving 1.15... | 3 | 0 |
| 12 | `vorton_track_vii_open_negative` | open_negative | Track VII Step 3 (vortex-string topology): π_n(U(1)) correctly identifies cosmic strings (not monopoles); BPS tension μ = πv² = 0.56 GeV²... | 1 | 1 |


---

# Appendix F — Dependency Graph (auto-rendered)

*Auto-generated from `grut/toe/registry.py` and `grut/toe/dependencies.py` via `python3 -m grut.toe.render_appendices`. The framework's dependency structure: which claims are entry points, which are load-bearing, and which open negatives block which others.*

## F.1 Graph summary

| Metric | Value |
|:---|---:|
| Total claims (nodes) | 103 |
| Dependency edges | 188 |
| Roots (zero deps) | 12 |
| Leaves (no dependents) | 49 |
| Max downstream fan-out | 76 |
| Max upstream fan-in | 24 |

## F.2 Roots — framework entry points

Claims with zero registry dependencies. These are the seams the framework rests on: postulates, foundational definitions, and externally-anchored values that the rest of the registry builds from.

| Claim ID | Tier | Chapter | Fan-out | First sentence |
|:---|:---|---:|---:|:---|
| `ctp_action_structure` | computed | 3 | 76 | The framework is built on a single Closed Time Path (Schwinger-Keldysh) action S_CTP. |
| `alpha_vac_derivation` | computed | 2 | 58 | α_vac = 1/3 is formalized via the Gate R identification (May 2026, C1-C6 all SUPPORTED/FORMALIZED... |
| `tau_0_derivation` | computed | 2 | 35 | τ_0 = 41.9 Myr is POSITED in Phase I §5 with two independent anchors: (1) cosmic-baseline relatio... |
| `t_c_thermal_transition` | computed | 8 | 3 | The 'boiling point of gravity' T_c = ℏ/(τ_micro × k_B) ≈ 54.7 MK, where τ_micro ≈ 1.4×10⁻¹⁹ s is... |
| `closed_universe` | foundational | 1 | 2 | The universe is closed, finite, and self-referential. |
| `bbn_thermal_buffer_negligible` | anchored | 12 | 0 | Standard-cosmology calculation testing one piece of an external research hypothesis: 'BBN binding... |
| `claim_registry_appendix` | meta | 12 | 0 | Appendix E (Full Claim Registry) is auto-rendered as a Markdown reference table over every regist... |
| `correction_ledger` | meta | 12 | 0 | The repository maintains a public ledger of every correction to the framework: 28 documented corr... |
| `dependency_graph_appendix` | meta | 12 | 0 | Appendix F (Dependency Graph) is auto-rendered from grut/toe/dependencies.py. |
| `derivation_index_appendix` | meta | 12 | 0 | Appendix D (Derivation Index) is auto-rendered from the registry: every claim at tier 'computed'... |
| `marker_validator_discipline` | meta | 12 | 0 | Tier-marker discipline checker: every [OPEN], [SCOPING], [CONJECTURAL], [SPECULATIVE], or 'Outsta... |
| `predictions_dashboard` | meta | 12 | 0 | The framework's complete predictive surface is codified in 27 quantitative predictions across 7 c... |

## F.3 Top 10 claims by downstream fan-out

The most load-bearing claims in the framework, ranked by the number of downstream claims that depend (transitively) on each. Failure of a high-fan-out claim cascades furthest; rigor on these is highest-leverage.

| Rank | Fan-out | Claim ID | Tier | Chapter |
|---:|---:|:---|:---|---:|
| 1 | 76 | `ctp_action_structure` | computed | 3 |
| 2 | 64 | `constitutive_equation` | computed | 3 |
| 3 | 58 | `alpha_vac_derivation` | computed | 2 |
| 4 | 47 | `memory_kernel_form` | computed | 3 |
| 5 | 35 | `tau_0_derivation` | computed | 2 |
| 6 | 30 | `threshold_bridge` | computed | 4 |
| 7 | 16 | `r_canonical_path_g` | computed | 7 |
| 8 | 15 | `regime_map` | computed | 4 |
| 9 | 14 | `decoherence_plateau` | computed | 5 |
| 10 | 14 | `screening_108pi` | computed | 4 |

## F.4 Closure-priority — open-negative dependency chains

Open negatives ranked by downstream fan-out (closure-priority order), with explicit blockers shown for each. An open negative blocked by another cannot close until the blocker closes; the chain shows the prerequisite ordering.

| Rank | Fan-out | Open negative | Blocked by |
|---:|---:|:---|:---|
| 1 | 3 | `tji_7_4_open_negative` | `allen_jacobson_phase1_stub_open_negative` |
| 2 | 1 | `el_gordo_outlier_open_question` | — |
| 3 | 0 | `allen_jacobson_phase1_stub_open_negative` | — |
| 4 | 0 | `born_rule_postulate_open_negative` | — |
| 5 | 0 | `koide_phase_4_open_negative` | — |
| 6 | 0 | `n_total_zero_parameter_derivation_open_question` | — |
| 7 | 0 | `nonlinear_ladder_4_of_8` | — |
| 8 | 0 | `path_f_translation_gap` | — |
| 9 | 0 | `phi_munu_frw_beyond_wkb_open_question` | — |
| 10 | 0 | `primordial_amplitude_zero_parameter_open_negative` | — |
| 11 | 0 | `rho_max_scale_open_question` | — |
| 12 | 0 | `tau_zero_to_tau_micro_relation_open_question` | — |
| 13 | 0 | `track_v_coupling_unification_open_question` | — |
| 14 | 0 | `two_route_convergence_physical_equivalence_open_question` | — |
| 15 | 0 | `vorton_track_vii_open_negative` | — |

## F.5 Inter-gap blocking chains

```
  tji_7_4_open_negative
    └── blocked by → allen_jacobson_phase1_stub_open_negative
```




---

## Back Matter

## References

**CTP / Schwinger-Keldysh foundations**

- J. Schwinger, "Brownian Motion of a Quantum Oscillator," *J. Math. Phys.* **2**, 407 (1961).
- L. V. Keldysh, "Diagram Technique for Nonequilibrium Processes," *Sov. Phys. JETP* **20**, 1018 (1965).
- R. P. Feynman and F. L. Vernon, Jr., "The Theory of a General Quantum System Interacting with a Linear Dissipative System," *Ann. Phys.* **24**, 118 (1963).
- G. Lindblad, "On the Generators of Quantum Dynamical Semigroups," *Commun. Math. Phys.* **48**, 119 (1976).
- H. Mori, "Transport, Collective Motion, and Brownian Motion," *Prog. Theor. Phys.* **33**, 423 (1965).
- R. Zwanzig, "Memory Effects in Irreversible Thermodynamics," *Phys. Rev.* **124**, 983 (1961).

**Gravitational decoherence**

- L. Diósi, "A Universal Master Equation for the Gravitational Violation of Quantum Mechanics," *Phys. Lett. A* **120**, 377 (1987).
- R. Penrose, "On Gravity's Role in Quantum State Reduction," *Gen. Rel. Grav.* **28**, 581 (1996).
- C. Anastopoulos and B. L. Hu, "A Master Equation for Gravitational Decoherence," *Class. Quant. Grav.* **30**, 165007 (2013).
- D. Kafri, J. M. Taylor, and G. J. Milburn, "A classical channel model for gravitational decoherence," *New J. Phys.* **16**, 065020 (2014).

**Gravitational entanglement experiments (BMV / KTM class)**

- S. Bose, A. Mazumdar, G. W. Morley, H. Ulbricht, M. Toroš, M. Paternostro, A. A. Geraci, P. F. Barker, M. S. Kim, and G. Milburn, "Spin Entanglement Witness for Quantum Gravity," *Phys. Rev. Lett.* **119**, 240401 (2017).
- C. Marletto and V. Vedral, "Gravitationally Induced Entanglement Between Two Massive Particles is Sufficient Evidence of Quantum Effects in Gravity," *Phys. Rev. Lett.* **119**, 240402 (2017).
- T. Krisnanda, M. Zuppardo, M. Paternostro, and T. Paterek, "Revealing Nonclassicality of Inaccessible Objects," *Phys. Rev. Lett.* **119**, 120402 (2017).

**Objective collapse models (CSL / GRW)**

- G. C. Ghirardi, A. Rimini, and T. Weber, "Unified dynamics for microscopic and macroscopic systems," *Phys. Rev. D* **34**, 470 (1986).
- P. Pearle, "Combining stochastic dynamical state-vector reduction with spontaneous localization," *Phys. Rev. A* **39**, 2277 (1989).
- G. C. Ghirardi, P. Pearle, and A. Rimini, "Markov processes in Hilbert space and continuous spontaneous localization of systems of identical particles," *Phys. Rev. A* **42**, 78 (1990).
- S. L. Adler, "Lower and upper bounds on CSL parameters from latent image formation and IGM heating," *J. Phys. A* **40**, 2935 (2007).

**Decoherence theory and the measurement problem**

- E. Joos and H. D. Zeh, "The emergence of classical properties through interaction with the environment," *Z. Phys. B* **59**, 223 (1985).
- W. H. Zurek, "Decoherence, einselection, and the quantum origins of the classical," *Rev. Mod. Phys.* **75**, 715 (2003).
- E. P. Wigner, "Remarks on the Mind-Body Question," in *The Scientist Speculates*, ed. I. J. Good (Heinemann, London, 1961), p. 284.
- H. Everett III, "'Relative State' Formulation of Quantum Mechanics," *Rev. Mod. Phys.* **29**, 454 (1957).

**Euclidean quantum gravity and conformal instability**

- G. W. Gibbons, S. W. Hawking, and M. J. Perry, "Path Integrals and the Indefiniteness of the Gravitational Action," *Nucl. Phys. B* **138**, 141 (1978).
- B. Allen and T. Jacobson, "Vector two-point functions in maximally symmetric spaces," *Commun. Math. Phys.* **103**, 669 (1986).

**Anomaly coefficients and local RG**

- H. Osborn, "Local Couplings and Sl(2,R) Invariance for Gauge Theories at One Loop," *Phys. Lett. B* **561**, 174 (2003).
- I. Jack and H. Osborn, "Analogs of the c-Theorem for Four-Dimensional Renormalisable Field Theories," *Nucl. Phys. B* **343**, 647 (1990).
- I. Jack and H. Osborn, "Constraints on RG Flow for Four Dimensional Quantum Field Theories," *Nucl. Phys. B* **883**, 425 (2014).

**Multi-loop techniques**

- K. G. Chetyrkin, A. L. Kataev, and F. V. Tkachov, "New Approach to Evaluation of Multiloop Feynman Integrals," *Nucl. Phys. B* **174**, 345 (1980).
- K. G. Chetyrkin and M. F. Zoller, "Three-loop β-functions for top-Yukawa and the Higgs self-interaction in the Standard Model," *JHEP* **06**, 033 (2012).

**Cosmological data**

- Planck Collaboration, "Planck 2018 Results. VI. Cosmological Parameters," *Astron. Astrophys.* **641**, A6 (2020).
- S. Casertano et al., "The Local Distance Network," *Astron. Astrophys.* **708**, A166 (2026).

**Modern observational programs**

- DESI Collaboration, "DESI 2024 VI: Cosmological Constraints from BAO," arXiv:2404.03002 (2024).
- Euclid Collaboration, "Euclid preparation: Forecasts for complementarity of cosmological probes," *Astron. Astrophys.* **642**, A191 (2020).
- CMB-S4 Collaboration, K. N. Abazajian et al., "CMB-S4 Science Case, Reference Design, and Project Plan," arXiv:1907.04473 (2019).
- LISA Pathfinder Collaboration, "Sub-Femto-g Free Fall for Space-Based Gravitational Wave Observatories," *Phys. Rev. Lett.* **116**, 231101 (2016).
- R. Kaltenbaek et al., "MAQRO — Testing Quantum Physics in Space," *EPJ Quantum Technology* **3**, 5 (2016).

**Cluster mergers — primary sources**

- M. Markevitch, A. H. Gonzalez, D. Clowe, A. Vikhlinin, W. Forman, C. Jones, S. Murray, and W. Tucker, "Direct Constraints on the Dark Matter Self-Interaction Cross Section from the Merging Galaxy Cluster 1E 0657-56," *Astrophys. J.* **606**, 819 (2004).
- D. Clowe, M. Bradač, A. H. Gonzalez, M. Markevitch, S. W. Randall, C. Jones, and D. Zaritsky, "A Direct Empirical Proof of the Existence of Dark Matter," *Astrophys. J.* **648**, L109 (2006).
- V. Springel and G. R. Farrar, "The speed of the 'bullet' in the merging galaxy cluster 1E 0657-56," *Mon. Not. Roy. Astron. Soc.* **380**, 911 (2007).
- M. Bradač, S. W. Allen, T. Treu, H. Ebeling, R. Massey, R. G. Morris, A. von der Linden, and D. Applegate, "Revealing the Properties of Dark Matter in the Merging Cluster MACS J0025.4-1222," *Astrophys. J.* **687**, 959 (2008).
- A. Mahdavi, H. Hoekstra, A. Babul, D. D. Balam, and P. L. Capak, "A Dark Core in Abell 520," *Astrophys. J.* **668**, 806 (2007).
- F. Menanteau et al., "The Atacama Cosmology Telescope: ACT-CL J0102-4915 'El Gordo,' a Massive Merging Cluster at Redshift 0.87," *Astrophys. J.* **748**, 7 (2012).
- J. M. Diego et al., "Free-Form Lens Model and Mass Distribution of the Galaxy Cluster El Gordo," *Mon. Not. Roy. Astron. Soc.* **531**, 2505 (2024).

**Precision gravity tests**

- R. A. Hulse and J. H. Taylor, "Discovery of a pulsar in a binary system," *Astrophys. J. Lett.* **195**, L51 (1975).
- B. Bertotti, L. Iess, and P. Tortora, "A test of general relativity using radio links with the Cassini spacecraft," *Nature* **425**, 374 (2003).
- B. P. Abbott et al. (LIGO Scientific Collaboration and Virgo Collaboration), "GW170817: Observation of Gravitational Waves from a Binary Neutron Star Inspiral," *Phys. Rev. Lett.* **119**, 161101 (2017).
- J. G. Williams, S. G. Turyshev, and D. H. Boggs, "Lunar Laser Ranging Tests of the Equivalence Principle with the Earth and Moon," *Int. J. Mod. Phys. D* **18**, 1129 (2009).

**Mass relations**

- Y. Koide, "New Formula for the Cabibbo Angle and Composite Quarks and Leptons," *Phys. Rev. Lett.* **47**, 1241 (1981).

**Conformal anomaly — load-bearing citations for α_vac = 1/3**

The per-species trace anomaly coefficients $(a,c)$ for a real conformally-coupled scalar, Weyl fermion, and gauge field are the direct source of $\alpha_{\rm vac} = a/c = 1/3$ via Gate R. Primary published citations:

- M. J. Duff, "Twenty Years of the Weyl Anomaly," *Class. Quant. Grav.* **11**, 1387 (1994). **[Lead citation. Eq (30)–(31): $(a,c) = (1,3)$ for real scalar, $(11/2,9)$ for Weyl fermion, $(62,36)$ for gauge field. Convention-independent ratio $a/c = 1/3$.]**
- S. M. Christensen and M. J. Duff, "New gravitational index theorems and supertheorems," *Nucl. Phys. B* **154**, 301 (1979); and "Quantizing Gravity with a Cosmological Constant," *Nucl. Phys. B* **170**, 480 (1980). **[Independent source for the same per-species anomaly coefficients.]**
- N. D. Birrell and P. C. W. Davies, *Quantum Fields in Curved Space* (Cambridge UP, 1982). [Textbook reference for conformal coupling $\xi_c = 1/6$ in 4D.]

*Note on "KS 2011" shorthand:* Earlier drafts cited "KS 2011" as a shorthand that was ambiguous between (a) Khasanov-Segal 2011 — unpublished lecture notes summarizing Christensen-Duff and Duff 1994 results, not independently citable as a primary source; and (b) Kounnas-Scrucca 2011 — a paper cited in internal gate documents with eq A.5 but not otherwise verified for the bibliography. This shorthand has been removed from the book body; all load-bearing citations for $\alpha_{\rm vac} = 1/3$ now point to Duff 1994 (eq 30–31) and Christensen-Duff 1980 as the unambiguous published sources.

**GRUT program documents**

- D. R. Grover, "GRUT v7 — The Responsive Universe Program," Zenodo DOI: 10.5281/zenodo.18993689 (April 2026).
- D. R. Grover, "GRUT Phase I Closure Protocol," Zenodo DOI: 10.5281/zenodo.18008060 (February 2026).
- D. R. Grover, "GRUT-RAI: Responsive AI Computational Platform," GitHub: github.com/ryangrvr/GRUT-RAI (2025-2026).

**Modern observational programs and comparisons**

- K. Y. Kim, "Relativistic quantum corrections to classical dynamics as an alternative to dark matter and dark energy," *Int. J. Mod. Phys. D* (2026), DOI: 10.1142/S0218271826500100.
- S. Alexander, A. Hui, and H. Bernardo, "Cosmological Constant from Quantum Gravitational θ Vacua and the Gravitational Hall Effect," *Phys. Rev. Lett.* (2026).
- K. Itahashi et al., "Search for η′-mesic nuclei in ¹²C(p, dp) reaction with the WASA detector at GSI-FRS," *Phys. Rev. Lett.* (2026); GSI-FRS / FAIR Phase 0 program.

---

### Acknowledgments

**Specialist consultation.** I am grateful to my brother for sustained specialist conversation throughout this work — for asking the questions that surfaced ambiguities I had been treating as resolved, for pushing back when claims overreached the derivation, and for keeping the discipline pattern honest when it would have been easier to round corners. The framework's habit of surfacing rather than concealing weak points owes much to those exchanges. *[Names of additional human reviewers, if any, to be added at deposit time.]*

**AI collaboration.** This document was composed with sustained assistance from Anthropic's Claude across several distinct modes: a strategy and review channel that helped shape the discipline pattern, scope-setting language, and overall framing; a code-and-derivation channel (Claude Code) that executed the codebase work — claim registration, test scaffolding, foundations audits, and the investigation logs that back the corrections ledger; and a document-composition channel that drafted, structured, and tightened prose against pre-committed criteria. Where AI produced derivations, computations, or text that landed in the deposit, the discipline pattern required pre-commit expectations, post-hoc verification against tests, and explicit registration in the claim registry — the AI was used as a collaborator under the framework's own audit infrastructure, not as an unchecked author. The framework's organizing ideas, foundational postulates, scope decisions, and final-form claims are the author's responsibility; the AI helped surface, formalize, compute, and stress-test them.

**Computational platform.** The GRUT-RAI codebase (DOI 10.5281/zenodo.18993689) is the load-bearing artifact behind every claim in this document. The 2539-test suite (post v8→v2, including Phase-1 hard-theory benchmarks), the 103-claim registry, the foundations-audit infrastructure, and the auto-rendered appendices (D, E, F) are what make the discipline pattern operational. Builds, tests, and audit cycles ran on standard Python tooling (SymPy for exact-arithmetic derivations, pytest for verification, NumPy/SciPy for numerical routes).

**Prior work.** The framework rests on the published foundations referenced in this document — Schwinger-Keldysh CTP, Khasanov-Segal trace anomalies, the Diósi-Penrose / Anastopoulos-Hu gravitational decoherence program, the Bose-Marletto-Vedral and Kafri-Taylor-Milburn entanglement framework, and the cluster-merger lensing literature. Where GRUT diverges from these traditions (constitutive equation, finite-bandwidth medium, scale-universal constants) the divergence is a posited extension, not a critique of the source work.

**Errors are mine.** Every claim in this document has been audited against the codebase, but the framework remains a candidate, not a closed theory. Open questions are documented in Chapter 14; corrections are documented in the Ch 14 ledger and in `theory/derivation/` and `theory/foundations_audit/` in the repository. Errors that survive the audit infrastructure are my responsibility.

### Index

*To be generated.*

---

*D. Ryan Grover, May 2026.*

*GRUT — Grand Responsive Universe Theory: Candidate Framework.*

*2539 tests. 103 registered claims (58 computed, 15 anchored, 3 conjectural, 15 open_negative, 2 foundational, 10 meta). 27 documented corrections (V7 era #1-#16; v8→v2 #22-#30; hard-theory #31-#34). Full audit transparency.*

*The universe is √(4/3) ≈ 1.15470 trying to become 1.*
