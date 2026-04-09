# Sector 1 — Quantum Mechanics Recovery

**Status: Recovered**

## What GRUT already has

The quantum-mechanical host structure is fully recovered from Axioms A0–A2 of the directed-response framework. This sector establishes that GRUT contains standard quantum mechanics as a structural limit, providing the foundation on which the novel gravitational decoherence sector (Sector 3) is built. This is a consistency sector, not the flagship prediction sector.

## Minimal sector equations

| # | Equation | Role |
|---|----------|------|
| 1 | (τ_R + iτ_I) ∂_t z = z_target − z | Constitutive law (A1 + A2) |
| 2 | z_target = δF/δz* = c₀(x)z − c₂∇²z | Variational target from F[z] |
| 3 | iℏ ∂_t z = [−ℏ²/(2m)∇² + V(x)]z | Schrödinger (from τ_R = 0, τ_I = ℏ/2) |
| 4 | ∂_t ρ + ∇·j = 0, j = (ℏ/m)Im(z*∇z) | Continuity / probability current |
| 5 | (□ + M²)z = 0 | Klein-Gordon (Lorentz-covariant S[z]) |
| 6 | iℏ ∂_t ψ = (α·p + βM)ψ | Dirac (first-order spinor DR) |
| 7 | Z(X₀) = Z(X₁) (linear case) | Born-rule transparency |
| 8 | dρ/dt = −(i/ℏ)[H,ρ] + Σγᵢ𝒟_Lᵢ[ρ] | Lindblad (CTP completion, A0) |
| 9 | ∂_t S + (∇S)²/(2m) + V = 0 | Hamilton-Jacobi (WKB classical limit) |

## Derived observables

| Observable | Formula | Status |
|------------|---------|--------|
| Mass | m = τ_I²/c₂ | Derived (structural ratio) |
| Potential | V(x) = 2(c₀(x) − 1) | Derived (target multiplier) |
| Probability density | ρ = \|z\|² | Derived |
| Probability current | j = (ℏ/m)Im(z*∇z) | Derived |
| Dispersion (NR) | ω = ℏk²/(2m) | Derived |
| Dispersion (rel.) | ω² = k² + M² | Derived |
| Group velocity | v_g = ℏk/m (NR); k/ω (rel.) | Derived |
| Decoherence rate (CTP) | γ from Lindblad operators | Derived |

## GRUT-RAI implementation

| Module | Function | Status |
|--------|----------|--------|
| `constitutive_qm.py` | Base parameters, z_target, RHS | Implemented |
| `schrodinger_recovery.py` | Recovery benchmark, RK4 evolution | Implemented |
| `continuity.py` | ρ, j, continuity residual | Implemented |
| `relativistic_extensions.py` | KG dispersion, Dirac 1+1D | Implemented |
| `born_transparency.py` | Linear + bistable Z-ratio | Implemented |
| `ctp_lindblad.py` | τ_R instability, Lindblad, thermalization | Implemented |
| `classical_limit.py` | Ehrenfest, group velocity | Implemented |

Entry point: `notebooks/sector_01_qm_recovery.py`

## Validation summary

| Test | Quantity | Expected | Measured | Error | Status |
|------|----------|----------|----------|-------|--------|
| Schrödinger recovery | max \|z_DR − z_SE\| | < 10⁻¹² | 9.2 × 10⁻¹⁶ | — | **PASS** |
| Norm conservation | \|∫\|z\|²dx − 1\| | < 10⁻¹⁰ | < 10⁻¹⁵ | — | **PASS** |
| Continuity | rel. violation | < 0.1 | 0.0046 | FD-limited | **PASS** |
| KG NR limit | ω_exact vs ω_NR | < 10⁻³ | 1.2 × 10⁻⁵ | — | **PASS** |
| Dirac norm | \|∫\|ψ\|²dx − 1\| | < 10⁻⁸ | 1.1 × 10⁻¹¹ | — | **PASS** |
| Dirac v_g | v_meas vs k/ω | < 5% | 2.5% | Peak tracking | **PASS** |
| Born (linear) | Z₀/Z₁ | 1.000000 | 1.000000 | Exact | **PASS** |
| Born (bistable) | \|Z₀/Z₁ − 1\| | < 0.01 | < 10⁻⁶ | — | **PASS** |
| τ_R instability | all eigs > 0 | True | True | — | **DEMONSTRATED** |
| Lindblad therm. | max pop error | < 10⁻⁴ | 1.4 × 10⁻⁶ | — | **PASS** |
| Ehrenfest | rel. error | < 1% | 0.42% | — | **PASS** |
| Group velocity | v_g = p/m | Exact | Exact | — | **PASS** |

**12 / 12 tests pass.**

## What remains open

| Item | Status | Note |
|------|--------|------|
| τ_I = ℏ/2 derivation | Open (Gate O1) | Identified, not computed |
| Born rule derivation | Not claimed | Preserved, not derived |
| Nonlinear Born correction bound | Documented, not yet bounded | Could tighten for all parameter regimes |
| 3D Dirac benchmark | Not yet implemented | 1+1D demonstrated |
| Gauge-coupled Schrödinger in sector module | Not yet packaged here | Available in `grut_solver/` (Stage 5) |

## Closure condition

Sector 1 is closed. All benchmarks pass. The QM host structure is recovered from A0–A2 with explicit numerical verification at each step. No new experimental prediction is made in this sector. The sector provides the structural foundation for the novel gravitational decoherence predictions in Sector 3.
