# GRUT — Grand Responsive Universe Theory

**A universal response framework with zero-parameter gravitational decoherence predictions.**

---

## What GRUT Is

GRUT is a candidate Theory of Everything framework in which physical laws emerge as structural limits of a universal directed-response system. The framework recovers quantum mechanics and the Standard Model from three axioms, and predicts a specific, testable gravitational decoherence law with zero free parameters.

**The core prediction:** At sufficiently low pressure, a levitated nanoparticle's decoherence rate will plateau — not go to zero. The plateau height is computed exactly. Standard quantum mechanics predicts no plateau. One experiment decides.

## Quick Start

```bash
pip install -e .

python -c "
from grut_solver import GRUTSolver
solver = GRUTSolver()
r = solver.decoherence(m=1e-14, R=50e-9, l=100e-9, T_env=10e-3, P=1e-10)
print(f'Lambda_grav = {r.lambda_grav:.1f} Hz (zero free parameters)')
print(f'Binding constraint: {r.binding_channel}')
"
```

## Run Tests

```bash
python tests/test_grut_solver.py                          # 27 core tests
python tests/sectors/qm/test_sector_01.py                 # Sector 1
python tests/sectors/gravity_decoherence/test_sector_03.py # Sector 3
python -m grut_solver figures                              # Publication figures
python grut_solver/self_test.py                            # Adversarial self-test
python -m grut_solver.applications.consciousness           # Closing calculation
```

## The Solver API

```python
from grut_solver import GRUTSolver
solver = GRUTSolver()

# Full decoherence budget
result = solver.decoherence(m=1e-14, R=50e-9, l=100e-9, T_env=10e-3, P=1e-10)

# Falsification scans
solver.pressure_scan(m, R, l, T_env, P_min=1e-14, P_max=1e-6)
solver.mass_scan(l, rho=2200, T_env=10e-3, P=1e-10)
solver.radius_scan(m, l, T_env, P, densities={"gold": 19300, "aerogel": 100})

# Many-body entanglement
solver.bell_vs_product(m=1e-14, l=100e-9, d_AB=200e-9, R=50e-9)
solver.ghz_scaling(m=1e-14, l=100e-9, d=200e-9, N_max=20)

# Adversarial kill tests
solver.try_kill("all")

# Quantum-classical boundary
solver.boundary_mass(l=1e-7, t_obs=1.0)
```

## Package Structure

```
grut_solver/
├── solver.py                # Main API: GRUTSolver
├── constants.py             # All physical constants (single source)
├── figures.py               # Publication figures
├── self_test.py             # Adversarial self-test protocol
├── usl/                     # Universal Scaling Law (novel sector)
├── budget/                  # Environmental + nuisance channels
├── kill/                    # Adversarial self-attack framework
├── experiments/             # Platforms and competing models
├── sectors/                 # 12-sector ToE map
├── applications/            # 9 applications: Planck to consciousness
├── core/                    # Foundational equations
└── reference/               # Publication documents
```

## 122 Tests Across 12 Sectors

| Sector | Status | Tests |
|--------|--------|-------|
| 1. QM Recovery | Recovered | 12/12 |
| 2. Electroweak / SM | Recovered host | 13/13 |
| 3. Gravitational Decoherence | **Predictive** | 14/14 |
| 4. Gravity | Partial | 8/8 |
| 5. Cosmology | Partial | 8/8 |
| 6. QCD / Strong Force | Open (entry point) | 13/13 |
| 7. Flavor / Masses | Open | 6/6 |
| 8. Neutrinos | Open | 8/8 |
| 9. Dark Matter | Open | 3/3 |
| 10. Baryogenesis | Open | 3/3 |
| 11. Coupling Unification | Open | 4/4 |
| 12. Quantum Gravity | Open | 3/3 |
| Main Solver | Operational | 27/27 |
| **Total** | | **122/122** |

## 9 Applications: Planck to Consciousness

| # | Application | Key Result |
|---|------------|------------|
| 1-2 | Matter-wave interferometry | 7 published experiments consistent; mass frontier at ~0.1 fg |
| 3 | Bullet Cluster | Null result (classical by 10^54) |
| 4 | Observer dynamics | Measurement hierarchy: smooth QC boundary |
| 5 | Structure formation | Boundary mass ~35 ng at recombination |
| 6 | Early universe | Gravity wins below T ~ 1400 K |
| 7 | Solar system | Dust-to-pebble crossover at R ~ 2 mm |
| 8 | Biology | Water beats gravity by 10^15 to 10^33 |
| 9 | Consciousness | 38,000 neurons for 40 Hz; 28-order thermal wall |

## What GRUT Does NOT Claim

- All constants are derived (tau_I = hbar/2 is identified, not computed)
- Gravity is fully unified (semiclassical only)
- The theory is complete (four open gates remain)
- Standard Model parameters are predicted (same free-parameter count)
- Dark energy, dark matter, or quantum gravity are solved

## Publications

- [Part 1: Foundational Framework and Gravitational Decoherence](https://zenodo.org/communities/grut)
- Part 2: Universal Structural Synthesis — 12-Sector Map
- Part 3: Open Gates, Failed Routes, and Closure Paths
- Applications: The USL Across All Scales — From Planck to Consciousness

## Author

D. Ryan Grover — dryangrover@gmail.com

Software DOI: 10.5281/zenodo.18993690

## License

MIT License. See [LICENSE](LICENSE).
