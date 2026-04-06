# Phase I Closure Protocol — Internal Reference

## Source: GRUTPhase I Closure Protocol (Zenodo DOI: 10.5281/zenodo.18008060)

### Core Content

Phase I establishes GRUT as an operational, falsifiable protocol for dark sector phenomenology via universal responsiveness.

### Locked Constants
- tau_0 ≈ 41.9 Myr = 1.3225 × 10^15 s (vacuum relaxation timescale)
- alpha_vac = 1/3 (vacuum impedance fraction)
- alpha_mem ≈ 0.1 (cosmological memory weighting)

### Key Equations
- Modified Friedmann: H^2 = (1 - alpha_mem) H^2_base + alpha_mem M_X
- Memory ODE: tau_eff dM_X/dt + M_X = H^2_base
- tau_eff(H) = tau_0 / (1 + (H tau_0)^2)
- Screening via causal memory kernel: K(Delta_t) = (1/tau_0) exp(-Delta_t/tau_0) Theta(Delta_t)

### Status
- LOCKED as operational foundation (Phase II and III build on this without modification)
- All constants enter as canonical definitions, not derived from first principles
- NIS (Numerical Integrity Standard) discipline established

### RAI Internal Implementation
- `grut/engine.py`: cosmological memory sector
- `grut/operators.py`: operator stack (OP_GENESIS through OP_GROWTH_LINEAR)
- Phase I constants inherited through all subsequent phases without modification
