# GRUT v7 — Appendix K: GRUT RAI — The Computational Platform

## A Reproducible, AI-Augmented Physics Research Tool

*D. Ryan Grover, April 2026*

---

## K.0 — Purpose

This appendix documents GRUT RAI (Responsive AI), a computational platform
that makes every numerical result in the GRUT program reproducible,
explorable, and interactively verifiable. GRUT RAI is not a paper supplement —
it is a research instrument that computes predictions on demand, compares
them against observations, propagates uncertainties, and explains results
through an AI chat interface that is grounded in real computation, not
language-model recall.

**Repository:** https://github.com/ryangrvr/GRUT-RAI

---

## K.1 — What Is GRUT RAI

GRUT RAI v2 is a web-based physics computation platform with four layers:

1. **Foundation modules** — The axioms, constants, and CTP structure (Python)
2. **Derived modules** — All computed predictions across 9 physics domains
3. **REST API** — 93 endpoints exposing every computation
4. **AI Chat Interface** — Claude-powered conversation with 22 tool-use functions

The platform answers questions like "What is the decoherence rate for a 10^9 amu
gold nanoparticle?" by calling the actual computation module — not by retrieving
a cached answer or generating one from training data.

---

## K.2 — Architecture

    grut/
    ├── foundation/          # 5 modules: axioms, constants, constitutive, noise_kernel, anomaly
    ├── derived/             # 24 modules across 9 physics domains
    │   ├── baryogenesis/    # eta_B computation, cross-check vs observations
    │   ├── cosmology/       # vacuum prediction, Hubble tension, spectral running
    │   ├── dark_matter/     # U(1)_dark sector, dark photon exclusion
    │   ├── decoherence/     # 7 modules: competition, kink, material swap, isotope, entanglement
    │   ├── koide/           # K=2/3 identity, N-generation uniqueness
    │   ├── quantum_gravity/ # linearized closure conditions
    │   ├── quantum_mechanics/ # Schrodinger recovery
    │   └── sm_emergence/    # 5 CTP constraints
    ├── bridge/              # tau_0 <-> Omega_Lambda connection
    └── utils/               # 13 modules: compare, covariance, data, dimensions, discovery,
                             #   experiment, multiscale, noise_models, pedagogy, robustness, sweep, whatif

    ui/
    ├── app.py               # Flask web server
    ├── api/routes.py        # 93 REST API endpoints
    ├── ai/chat.py           # Claude AI with 22 tool-use functions
    └── static/
        ├── index.html        # 4-tab dashboard (Chat, Dashboard, GRUTipedia, Experiments)
        ├── app.js            # 23 GRUTipedia articles, chat logic
        └── viz/viz.js        # 4 interactive Prezi-style visualizations

    tests/
    └── foundation/test_foundation.py  # 22 consistency checks

---

## K.3 — Installation and Setup

    git clone https://github.com/ryangrvr/GRUT-RAI.git
    cd GRUT-RAI
    pip install -e .
    
    # Set Anthropic API key for AI chat (optional)
    echo "ANTHROPIC_API_KEY=sk-ant-..." > .env
    
    # Run the server
    python ui/app.py
    
    # Open http://127.0.0.1:5000

Requirements: Python 3.9+, numpy, flask. The Anthropic API key enables the
AI chat; without it, the keyword fallback responds to basic queries.

---

## K.4 — Foundation Modules (5 modules)

Every computation in GRUT RAI traces back to these five modules:

| Module | What it computes | Key outputs |
|:---|:---|:---|
| constants.py | CODATA 2018 physical constants | G, hbar, c, k_B, M_Planck, alpha_EM |
| axioms.py | CTP doubling (A0), retarded variation (A1) | Keldysh transform, tau_I = hbar/2 |
| constitutive.py | tau dz/dt + z = z_target[z] | Exact stepper, fixed-point analysis, stability |
| noise_kernel.py | Gravitational noise, FDT, decoherence | Lambda_grav, S(l/R), tau_KMS |
| anomaly.py | 3-loop anomaly structure | C_FINAL, R_ANOMALY, S_CTP, c_cosmo |

Self-test: python -m pytest tests/ runs 22 checks verifying all foundation values.

---

## K.5 — Derived Modules (24 modules, 9 domains)

### Decoherence (7 modules)
- sector.py: 6 scaling laws, adversarial comparison vs 5 models
- competition.py: GRUT vs gas/blackbody/EM/vibrational, scaling exponents
- kink_scan.py: Geometry kink at l = 6^(1/3)R ≈ 1.817R
- material_swap.py: Same mass, different material (Os vs Al: 737%)
- isotope_test.py: Same element, different isotope (Ca: 30.6%, Si: 12.9%)
- entanglement.py: Bell vs separable (59% protection)

### Cosmology (4 modules)
- vacuum.py: Omega_Lambda = 0.6904, 329-era map, constitutive H(t)
- hubble_tension.py: GRUT curve vs 7 measurements
- spectral_running.py: n_s running +0.00068 vs slow-roll -0.00160

### Baryogenesis (2 modules)
- eta.py: eta_B = 6.57 x 10^-10 (Route 1, Route 2)
- crosscheck.py: vs 6 competing models, CMB-S4 forecast

### Dark Matter (2 modules)
- sector.py: Route 1 (5/5), g_dark = 0.917, m_A = 387.4 MeV
- exclusion.py: 7 experiments, kinetic mixing, detection roadmap

### Other domains
- koide/identity.py: K = 2/3, N = 3 uniqueness
- quantum_gravity/closure.py: 5/5 linearized gates, nonlinear ladder
- sm_emergence/constraints.py: 5 CTP constraints -> SM
- quantum_mechanics/recovery.py: Schrodinger from CTP

---

## K.6 — API Reference (93 endpoints)

All endpoints accept GET with query parameters and return JSON.

### Foundation (7 endpoints)
    /api/health — Module verification
    /api/constants — All physical constants
    /api/anomaly — C_FINAL, R_ANOMALY, S_CTP
    /api/decoherence?m=80.8e-15&l=1e-6&R=1e-6 — Lambda_grav(m, l, R)
    /api/suppression?R=1e-6 — S(l/R) scan
    /api/tau_kms?T=300 — KMS relaxation time

### Bridge (2 endpoints)
    /api/bridge?H_0=70 — tau_0 -> Omega_Lambda
    /api/bridge/experimental?lambda_grav=689 — measured Lambda -> prediction

### Decoherence experiments (20 endpoints)
    /api/decoherence/competition — multi-channel analysis
    /api/decoherence/full_analysis — complete competition
    /api/decoherence/scaling_exponents — alpha, beta, gamma, delta table
    /api/decoherence/protocols — 3 experimental protocols
    /api/decoherence/kink_scan — geometry kink
    /api/decoherence/material_swap — gold vs silica
    /api/decoherence/isotope — Si-28 vs Si-30
    /api/decoherence/isotope/full — all isotope pairs
    /api/decoherence/entanglement — Bell vs separable
    ... (and mass/separation scans for each)

### Cosmology (10 endpoints)
    /api/cosmology/vacuum — Omega_Lambda prediction
    /api/cosmology/era_map — 329-era evolution
    /api/cosmology/hubble_tension — 7 measurements
    /api/cosmology/spectral — n_s, running, r

### All other domains
    /api/baryogenesis — eta_B Route 1/2
    /api/dark_matter — branch discrimination
    /api/dark_matter/exclusion — dark photon exclusion
    /api/koide — K = 2/3 check
    /api/sm_emergence — 5 constraints
    /api/quantum_gravity — closure conditions
    /api/compare/all — GRUT vs String vs LQG vs CSL
    /api/whatif?parameter=R_anomaly&value=1.2 — modify and recompute
    /api/noise/budget — 7-channel noise budget
    /api/robustness — N-gen + R_anomaly + MC
    /api/multiscale — 24 objects across 130 orders of magnitude

---

## K.7 — AI Chat System (22 tools)

The chat uses the Anthropic Claude API with tool-use. When asked a quantitative
question, Claude calls a computation tool rather than generating an answer
from training data.

### Anti-hallucination architecture

1. **System prompt:** "NEVER invent, estimate, or recall numbers from memory.
   ALL quantitative answers MUST come from a tool call."
2. **22 typed tools:** Each tool maps to a specific Python module
3. **Honest negatives list:** The system prompt explicitly states that
   hierarchy, perturbation growth, and singularity are unsolved
4. **Known traps:** tau_0 = 41.9 Myr (NOT 401.5), hierarchy != CC problem
5. **Force-answer loop:** If tool-use exceeds 6 rounds, a clean conversation
   is created to force a text response without further tool calls
6. **Result truncation:** Tool outputs > 8KB are trimmed to prevent context overflow

### Tool list

    compute_decoherence — Lambda_grav(m, l, R)
    compute_for_material — auto-compute R from density
    compute_bridge — tau_0 -> Omega_Lambda
    compute_baryogenesis — eta_B Route 1/2
    get_dark_matter — dark sector properties
    get_cosmology — Omega_Lambda prediction
    get_koide — K = 2/3, N-gen uniqueness
    get_anomaly — C_FINAL, R_ANOMALY, S_CTP
    compute_sensitivity — d(OL)/d(input) at +/- delta%
    compute_uncertainty — error propagation
    get_experimental_data — Planck, PDG, materials
    compare_theories — GRUT vs competitors
    whatif_analysis — modify parameters, see what breaks
    design_experiment — specify target Lambda -> required setup
    compute_snr — signal-to-noise ratio
    get_walkthrough — step-by-step derivations
    run_discovery — numerical coincidences
    decoherence_competition — multi-channel analysis
    get_scaling_exponents — alpha, beta, gamma, delta table
    get_experimental_protocols — 3 protocols
    isotope_test — Si-28 vs Si-30 comparison
    isotope_element_scan — best isotope pair ranking

---

## K.8 — GRUTipedia (23 articles)

An in-app encyclopedia covering every computed result:

### Foundation (5 articles)
CTP Effective Action, Constitutive Equation, Noise Kernel & FDT,
Fixed-Point Principle, Gravitational Decoherence

### Predictions (5 articles)
Cosmological Constant, Baryon Asymmetry, Dark Matter, Koide & 3 Generations,
SM Emergence

### Framework (4 articles)
Bridge Parameter, Projection Audit, Conjectures, Limitations

### Computed Experiments (9 articles)
Decoherence Competition, Geometry Kink, Material Swap, Entanglement Protection,
Hubble Tension, Dark Photon Exclusion, Spectral Running, Baryogenesis Cross-Check,
Isotope Test

---

## K.9 — Interactive Visualizations (4 modules)

Each visualization is a Prezi-style interactive panel with real-time sliders:

1. **Decoherence Frontier** — Lambda_grav vs mass with material selection,
   separation slider, regime boundaries. Shows C60 and PFNS8 experiments.

2. **Scaling Laws** — All 6 signatures (F1-F6) with pass/fail validation.
   Mass-squared, geometry, plateau, l-scaling, entanglement, kink.

3. **Era Map** — 329-era constitutive evolution from radiation through
   matter to acceleration. Slider scrubs through cosmic history.

4. **Bridge: Lab -> Universe** — The full chain: Lambda_grav -> tau_0 -> H_inf -> Omega_Lambda.
   H_0 slider shows sensitivity. Planck comparison displayed.

---

## K.10 — How to Reproduce Every Result in This Paper

Every computed number in the v7 document can be verified:

    # Decoherence benchmark (689 Hz)
    python -c "from grut.foundation.noise_kernel import lambda_grav; print(lambda_grav(80.8e-15, 1e-6, 1e-6))"
    
    # Omega_Lambda (0.6904)
    python -c "from grut.bridge.parameter import bridge_prediction; print(bridge_prediction(70.0)['Omega_Lambda'])"
    
    # eta_B (6.57e-10)
    python -c "from grut.derived.baryogenesis.eta import compute_eta_b; print(compute_eta_b(1)['eta_B'])"
    
    # C_FINAL (1.14021e-4)
    python -c "from grut.foundation.anomaly import C_FINAL; print(C_FINAL)"
    
    # Isotope test (Ca: 30.6%)
    python -c "from grut.derived.decoherence.isotope_test import isotope_experiment; r=isotope_experiment(1e9,1e-7,'Ca-40','Ca-48'); print(r['ratio']['deviation_from_unity_pct'])"

Every API endpoint can be called directly:

    curl http://localhost:5000/api/decoherence?m=80.8e-15&l=1e-6&R=1e-6
    curl http://localhost:5000/api/bridge?H_0=70
    curl http://localhost:5000/api/baryogenesis?route=1

No result in this paper requires trusting a number that cannot be independently
recomputed from the source modules.

---

*D. Ryan Grover, April 2026.*
*GRUT v7 Appendix K: GRUT RAI — The Computational Platform.*
