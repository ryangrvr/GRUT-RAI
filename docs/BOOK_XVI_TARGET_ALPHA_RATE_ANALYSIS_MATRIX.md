# Book XVI — Target Alpha: Rate Analysis Matrix

---

## Table 1 — Self-Consistent A_eff vs D7/D8 Proxy

| lambda | A_proxy | A_SC | Ratio | f_proxy | f_SC | m_proxy | m_SC | Source+ |
|--------|---------|------|-------|---------|------|---------|------|---------|
| 5 | 1.424 | 0.276 | 0.194 | ~13 | +0.22 | 0.670 | ~0.13 | YES |
| 10 | 1.596 | 0.231 | 0.145 | ~24 | +0.35 | 0.751 | ~0.11 | YES |
| 25 | 1.944 | 0.111 | 0.057 | +53.8 | +0.69 | 0.915 | 0.052 | YES |
| 50 | 2.220 | 0.010 | 0.005 | +90 | +1.27 | 1.046 | ~0.005 | MARGINAL |
| 100 | 2.443 | 0.010 | 0.004 | +136 | +1.90 | 1.150 | ~0.005 | MARGINAL |

**At ALL lambda: A_SC < 1 (no amplification). Proxy overpredicts by factors of 5-250x.**

---

## Table 2 — The Sign Error

| Quantity | D7/D8 formula | Correct physics | Sign |
|----------|--------------|-----------------|------|
| Sigma_defect(R_eq) | integral R_eq to R_ext of defect energy | Same | Same |
| m_eff(r) | M + beta * Sigma | M - Sigma (Birkhoff) | **REVERSED** |
| Effect on source X | X amplified (m_eff > M) | X reduced (m < M) | **REVERSED** |
| Effect on A_eff | A_eff ~ 2 (amplification) | A_eff ~ 0.1 (attenuation) | **REVERSED** |
| Basis | "Defect gravitates, deepens well" | Defect mass is ABOVE R_eq, not enclosed | **ERROR** |

---

## Table 3 — Relaxation Rate Extraction

| Rate type | Formula | Value | Amplified? |
|-----------|---------|-------|-----------|
| Proper-time | 1/tau | 0.817 | **NO** (always 1/tau; constitutive property) |
| Coordinate (flat) | sqrt(1)/tau | 0.817 | N/A (reference) |
| Coordinate (Schw at R_ext) | sqrt(0.5)/tau | 0.577 | Slower (inside potential well) |
| Coordinate (SC at R_eq) | sqrt(0.686)/tau | 0.676 | **SLOWER** than flat (f < 1) |
| Coordinate (proxy at R_eq) | sqrt(53.8)/tau | 5.99 | Artifact of sign error |

**No rate amplification exists. The first-order constitutive equation relaxes at rate 1/tau in proper time, always.**

---

## Table 4 — Mass Function at R_eq

| Regime | m(R_eq) D7/D8 | m(R_eq) SC | f(R_eq) D7/D8 | f(R_eq) SC |
|--------|---------------|-----------|---------------|-----------|
| **Peak processing** (Phi=0) | -9.97 (from A=2) | 0.052 (from A=0.11) | +60.8 | +0.69 |
| **Equilibrium** (Phi=X) | (not computed) | 85.8 (SINGULAR) | (not computed) | -513.8 |

**Peak processing:** D7/D8 mass goes deeply negative (artifact); SC mass is small and positive.
**Equilibrium:** Mass diverges at r ~ 0.75; singularity confirmed (XIII Gamma, tov_interior.py).

---

## Table 5 — Surplus Portfolio Update

| Surplus type | Before XVI Alpha | After XVI Alpha | Reason |
|-------------|-----------------|-----------------|--------|
| Demonstrated | 0 | **0** | Unchanged (none existed) |
| Conditional (equilibrium) | 1 | **0** | A_eff sign error; equilibrium path collapsed |
| Conditional (transient) | 1-2 | **0** | Processing negligible at A_SC ~ 0.1 |
| GW surplus | 0 | **0** | Unchanged (XII Beta: tensor = GR) |
| **Total** | **0 + 2-3 conditional** | **0 + 0** | **COLLAPSED** |

---

## Table 6 — D7/D8 Model Validity Assessment

| Component | Valid? | Detail |
|-----------|--------|--------|
| D7 source amplification formula | **NO** | Sign error: m_eff = M + Sigma should be M - Sigma |
| D8 portal coupling derivation | **YES** | Action-derived; sign correct (stabilizing) |
| D8 portal feedback on defect | **PARTIALLY** | Portal term is correct but couples to wrong A_eff |
| D9 Picard iteration convergence | **YES** | Convergence is genuine; profile self-consistency is real |
| D9 metric injection | **YES** | f = 1 - 2(M-Sigma)/r is correct metric formula |
| Layer 3 back-reaction | **INHERITED ERROR** | Uses D7 A_eff; back-reaction is on wrong energy |
| XV Beta positivity | **ARTIFACT** | f >> 0 driven by wrong A_eff |

---

## Table 7 — What Changes vs What Survives

| Component | Status | Detail |
|-----------|--------|--------|
| Constitutive equation | **INTACT** | tau*dPhi/dt + Phi = X unchanged |
| Five committed bridges | **INTACT** | 16/11/1/6 cost unchanged |
| Phase 4 T^Phi | **INTACT** | Energy-momentum tensor correctly derived |
| D1-D10 mathematics | **INTACT** | ODEs, BVPs, profiles all valid as math |
| D7 source amplification | **INVALIDATED** | Sign error in m_eff formula |
| D7-D10 metric support claims | **INVALIDATED** | Depend on wrong A_eff |
| XV Beta f >> 0 | **INVALIDATED** | Artifact of sign error |
| Matter-within-GR identity | **STRENGTHENED** | No competing frontier remains |
| GGB uncommitted architecture | **INTACT** | Still valid design; even further from commitment |

---

## Table 8 — Final Classification

| Aspect | Status |
|--------|--------|
| **Verdict** | **A — proxy INVALIDATED; sign error in D7/D8; surplus collapses** |
| Rate analysis | Complete; self-consistent |
| A_eff proxy | INVALIDATED (sign error; overpredicts 17x) |
| Self-consistent A_eff | ~0.1 (no amplification) |
| Rate amplification | NONE (proper rate = 1/tau always) |
| Surplus demonstrated | 0 |
| Surplus conditional | 0 (collapsed from 2-3) |
| Frontier | COLLAPSED to matter-within-GR baseline |
| Cost change | ZERO |
| Next step | D7/D8 sign correction; frontier restructuring or freeze |

---

*Rate Analysis Matrix complete. Eight tables. D7/D8 sign error confirmed. A_eff ~ 0.1, not 2. Surplus collapses. Frontier collapsed.*
