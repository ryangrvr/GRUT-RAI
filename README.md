# GRUT RAI v2

**Grand Responsive Universe Theory — Interactive Research Platform**

GRUT RAI is the computational engine and interactive research environment for the Grand Responsive Universe Theory (GRUT) — a unified physics framework built on the Schwinger-Keldysh closed-time-path (CTP) effective action.

One CTP action. One constitutive equation. 13 sectors of physics. Zero free parameters in the predictive core.

---

## What is GRUT?

GRUT (Grand Responsive Universe Theory) proposes that the universe is a closed responsive system — every physical subsystem relaxes toward a self-consistent target state determined by the CTP effective action. The framework is built on:

- **Axiom A0**: CTP doubling (Schwinger-Keldysh closed time path)
- **Axiom A1**: Retarded variation (causal, forward-in-time dynamics)
- **Normalization N0**: τ_I = ℏ/2 (connects CTP to quantum mechanics)

These produce the **constitutive equation**:

```
τ dz/dt + z = z_target[z]
```

derived from three independent routes (CTP variation, Mori-Zwanzig memory kernel, gradient flow), establishing it as the universal first-order dynamics of open systems.

### Key Results

| Result | Value | Status |
|:---|:---|:---|
| Gravitational decoherence | Λ_grav = G m² S(l/R) / (ℏ l) | DERIVED (zero parameters) |
| Cosmological constant | Ω_Λ = 0.6886 (Planck: 0.6889) | COMPUTED (+0.04%, V7 §26.2) |
| Baryon asymmetry | η_B = 6.57 × 10⁻¹⁰ (obs: 6.1 × 10⁻¹⁰) | COMPUTED (+8%) |
| Dark matter | g_dark = 0.917, m_A = 387 MeV | CLOSED (Route 1, 5/5) |
| Koide identity | K = 2/3 exactly | PROVEN (Z₃ algebraic) |
| Three generations | N = 3 uniquely θ-independent | PROVEN |
| SM emergence | Unique minimal EFT from 5 CTP constraints | COMPUTED |
| Quantum gravity | 5/5 linearized closures (τ₀ branch) | STRUCTURAL |

**R_anomaly = 1.15428** is *computed* from 3-loop CTP on S⁴ (V7 §26.2),
with primary-source audit confirming pure transcendental structure (no
coupling inputs; every integer traced to SM group theory). Independent
confirmation via Osborn 2003 eq (36): ε_combined(SM, M_Z) = 1.1537
matches at 0.05% — two independent mathematical constructions agreeing.

### The Bridge Parameter

One parameter — τ₀ — connects the decoherence sector to cosmology through a derived structural relation. A single laboratory measurement of gravitational decoherence would fix τ₀ and convert the cosmological constant from a one-parameter match to a zero-parameter prediction.

---

## Setup

### Requirements

- **Python 3.10, 3.11, 3.12, or 3.13**
  (Python 3.14+ not yet supported — numpy wheels unavailable)
- numpy ≥ 1.24, scipy ≥ 1.10, flask ≥ 2.3, python-dotenv ≥ 1.0
- Anthropic API key (optional, for AI chat)

### Quick start

```bash
git clone https://github.com/ryangrvr/GRUT-RAI.git
cd GRUT-RAI

# Install runtime dependencies (pinned versions)
pip install -r requirements.txt

# (Optional) Install the AI chat support
pip install anthropic
echo "ANTHROPIC_API_KEY=sk-ant-..." > .env

# Run the test suite — 1655 tests, completes in ~3 minutes
pytest tests/

# Start the dashboard — auto-detects compatible Python 3.10-3.13
./run_server.sh
```

Then open http://localhost:5000.

### Manual server start (if you prefer)

```bash
python -m flask --app ui.app run --port 5000
```

The `run_server.sh` wrapper is preferred because it auto-detects a
compatible Python version on systems that have multiple installed, and
gives clear error messages if dependencies are missing.

### Without API Key

The dashboard, computations, GRUTipedia, and experiments tabs all work without an API key. The RAI Chat tab falls back to keyword-based responses instead of Claude-powered AI.

### Running tests

```bash
pytest tests/                    # all 1655 tests
pytest tests/derived/ -v         # sector tests with verbose output
pytest tests/foundation/ -v      # foundation tests only (268)
```

Tests cover every V7 numerical claim as a regression check. If any core
value (R_anomaly, Ω_Λ, H_inf, Koide K, dark photon mass, η_B, τ_0)
silently changes, the test suite flags it.

---

## Using GRUT RAI

### The Dashboard (4 tabs)

**RAI Chat** — Ask GRUT RAI anything. Claude-powered with 22 computation tools. It computes real physics, not just answers from memory:
- *"Calculate the decoherence rate for a 50pg silica sphere at 500nm"*
- *"How does GRUT compare to string theory for the cosmological constant?"*
- *"What if R_anomaly were 1.3 instead of 1.15428?"*
- *"Design an experiment to detect gravitational decoherence at 100 Hz"*

**Dashboard** — Interactive calculators:
- Decoherence rate calculator (any mass, material, separation)
- Scaling laws plot (shows the geometric kink at l = 6^(1/3)R ≈ 1.817R)
- Mass dependence plot (m² scaling on log-log)
- Bridge calculator (τ₀ → Ω_Λ prediction)
- Constitutive dynamics visualizer

**GRUTipedia** — 23 articles covering the complete framework:
- Foundation: CTP action, constitutive equation, noise kernel, fixed-point principle
- Derived results: decoherence, cosmology, baryogenesis, dark matter, Koide, SM emergence
- Architecture: bridge parameter, projection audit, conjectures, limitations
- Experiments: decoherence competition, kink scan, material swap, entanglement, Hubble tension, dark photon, spectral running, baryogenesis cross-check, isotope test

**Experiments** — 9 predictive tests with falsification conditions:
- Decoherence plateau (PRIMARY — 5-10 years)
- Dark photon at 387 MeV (TESTABLE NOW — LHCb, Belle II)
- Koide precision, no 4th generation, no axion (ONGOING)
- Non-thermal Hawking radiation, spectral index running (FUTURE)

### Interactive Visualizations

Click "Visualize" buttons (appear in chat responses and at the bottom of the page):
- **Decoherence Frontier** — explore the quantum-classical boundary with mass/material sliders
- **Scaling Laws** — see the six signatures, the kink, material comparison overlays
- **Era Map** — play through 329 eras of cosmic evolution
- **The Bridge** — adjust H₀ and watch Ω_Λ respond

### API (115 endpoints)

All computations are available as REST endpoints:

```
GET /api/decoherence?m=80.8e-15&l=1e-6&R=1e-6
GET /api/bridge?H_0=70
GET /api/baryogenesis?route=1
GET /api/dark_matter
GET /api/cosmology/vacuum?H_0=70
GET /api/koide
GET /api/compare/all
GET /api/whatif?parameter=R_anomaly&value=1.3
GET /api/experiment/design?target_Lambda=100
GET /api/decoherence/isotope?iso_a=Si-28&iso_b=Si-30
GET /api/decoherence/competition?m_amu=1e9&T=4
GET /api/noise/budget?m=80.8e-15&T=4&P=1e-14
GET /api/robustness
GET /api/multiscale
GET /api/data/planck
```

115 endpoints across foundation, derived physics, bridge, decoherence experiments (competition, kink, material swap, isotope, entanglement), cosmology (vacuum, Hubble tension, spectral running), dark matter (exclusion, roadmap), baryogenesis (cross-check, models), noise models, covariance, robustness, multiscale, comparison, what-if, experiment design, pedagogy, discovery, and AI chat.

---

## Architecture

```
GRUT-RAI-v2/
├── grut/                          # Physics engine
│   ├── foundation/                # Axioms, constitutive eq, noise kernel, anomaly
│   │   ├── constants.py           # CODATA 2018 physical constants
│   │   ├── axioms.py              # A0, A1, N0
│   │   ├── constitutive.py        # τ dz/dt + z = z_target[z]
│   │   ├── noise_kernel.py        # Λ_grav, FDT, KMS τ
│   │   └── anomaly.py             # C_FINAL, R_ANOMALY, S_CTP
│   ├── derived/                   # 9 physics domains, 24 modules
│   │   ├── quantum_mechanics/     # Schrödinger recovery
│   │   ├── decoherence/           # 7 modules: sector, competition, kink, material swap, isotope, entanglement
│   │   ├── baryogenesis/          # η_B from CTP anomaly formula
│   │   ├── dark_matter/           # Route 1/2, branch discriminator
│   │   ├── cosmology/             # H_inf, era map, constitutive H(t)
│   │   ├── koide/                 # K=2/3, N-generation uniqueness
│   │   ├── sm_emergence/          # 5 CTP constraints
│   │   └── quantum_gravity/       # Closure conditions, nonlinear ladder
│   ├── bridge/                    # τ₀ ↔ Ω_Λ connection
│   └── utils/                     # 13 modules: compare, covariance, data, dimensions, discovery,
│                                  #   experiment, multiscale, noise_models, pedagogy, robustness, sweep, whatif
├── ui/                            # Web dashboard
│   ├── app.py                     # Flask server
│   ├── api/routes.py              # 115 API endpoints
│   ├── ai/chat.py                 # Claude-powered chat with 22 tools
│   └── static/                    # HTML, CSS, JS, visualizations
├── theory/                        # V8 theory document
├── papers/                        # Decoherence prediction paper
└── tests/                         # Test suite
```

### Design Principles

- **Foundation layer imports nothing from derived** — dependency arrow points one direction
- **Every constant traces to CODATA or a computed formula** — no magic numbers
- **Every result carries a status tier** — DERIVED, COMPUTED, STRUCTURAL, HYPOTHESIS, or HONEST NEGATIVE
- **Every honest negative is documented** — hierarchy problem unsolved, perturbation growth fails, fermion masses open

---

## Theory Documents

- `theory/GRUT_V8.md` — Complete top-down theory (Foundation → Derived → Conjectures → Bridge → Audit)
- `papers/DECOHERENCE_PREDICTION.md` — Standalone decoherence prediction paper (zero parameters, six scaling laws, experimental proposal)

For the full research history, v6 formalism paper, and v7 program document, see the [Zenodo community](https://zenodo.org/communities/grut).

---

## Testing

```bash
# Foundation tests (268 automated checks)
python -m pytest tests/foundation/ -v

# All automated tests
python -m pytest tests/ -v
```

The **1655 automated tests** verify every load-bearing numerical claim in the framework: foundation-level consistency (constants, axioms, constitutive equation, noise kernel, anomaly structure), every sector from decoherence through cosmology through the v8→v2 synthesis additions (Phase I canonical constants, bandwidth integral, thermal transition, rotation-curve engine, Track VII dielectric reframing, TJI Phase-0 closure, Schrödinger-in-the-Box observer module with Λ_contact CTP derivation, foundations audits, and the v8→v2 corrections #22-#30: τ-cleanup, Φ_μν derivation/scaffold/FRW, n_g(ω) MG-EFT closure, modified linear growth, neutrino hierarchy via Z₃, a_ν = 1 uniqueness theorem, falsifier paper). Each test corresponds to a specific claim in the GRUT-RAI registry (`grut/toe/registry.py`, 103 claims); if any value silently changes, the suite flags it.

---

## What Would Falsify GRUT

| Observation | What it kills |
|:---|:---|
| No decoherence plateau | The predictive core |
| Λ_grav measured, wrong Ω_Λ | The bridge |
| Axion detected | Strong CP conjecture |
| 4th generation found | N = 3 uniqueness |
| Koide violated | Z₃ identity |

---

## Author

D. Ryan Grover — dryangrover@gmail.com

## License

MIT

## Citation

```
@software{grover2026grut,
  author = {Grover, D. Ryan},
  title = {GRUT RAI v2: Grand Responsive Universe Theory — Interactive Research Platform},
  year = {2026},
  url = {https://github.com/ryangrvr/GRUT-RAI}
}
```
