# Book XV Terminal — Status Ledger and Threshold Tables

---

## Table 1 — Alpha-Through-Delta Stage Summary

| Stage | Function | Key result | Cost |
|-------|----------|-----------|------|
| Alpha | Specify Layer 3 computation | System defined; ~100–200 lines; three self-consistency layers | +0 |
| Beta | Implement + run Layer 3 | f ≫ 0 at ALL λ; m < 0; defect 0.04%; back-reaction negligible | +0 (code: layer3_backreaction.py) |
| Gamma | Forensic scalar audit | Positivity is proxy A_eff ≈ 2; defect is catalyst; interior repulsive | +0 |
| Delta | Independent scalar BVP solve | Regime mismatch: temporal ≠ spatial; A_eff neither validated nor invalidated | +0 |

---

## Table 2 — Final Claim-Status Table

| # | Claim | Status |
|---|-------|--------|
| 1 | Layer 3 code ready | **RETAINED** |
| 2 | f > 0 within proxy model | **RETAINED** (proxy-supported; not independently earned) |
| 3 | Restored strongest surplus | **REJECTED** |
| 4 | Defect-supported positivity | **REJECTED** (defect is 0.04% catalyst) |
| 5 | Scalar-dominated support | **NARROWED** (true in proxy; unvalidated independently) |
| 6 | A_eff ≈ 2 validated | **UNRESOLVED** (regime mismatch) |
| 7 | A_eff ≈ 2 falsified | **REJECTED** (regime mismatch ≠ falsification) |
| 8 | Static BVP comparison valid | **REJECTED** (temporal ≠ spatial) |
| 9 | Repulsive interior = compact support | **REJECTED** |
| 10 | Φ < 0 branch physical | **UNRESOLVED** |

---

## Table 3 — Regime-Mismatch Comparison

| Aspect | D7/D8 Proxy | Static BVP |
|--------|------------|-----------|
| Physical quantity | (1/2)(dΦ/dt)² | (1/2)(dΦ/dr)²f |
| Regime | DYNAMIC (temporal) | STATIC (spatial) |
| Energy at R_eq | ~23.6 | ~0.03 |
| Ratio | 1 | 0.001 |
| Mechanism | Relaxation at amplified rate | Spatial gradient of equilibrium |
| Comparable? | — | **NO** |

---

## Table 4 — Gravity-Frontier Status

| Category | Content | Authority |
|----------|---------|----------|
| COMPUTED | Layer 3 code; f > 0 within proxy at ALL λ | XV Beta (C2) |
| COMPUTED | Static BVP non-equilibrium branch (Φ < 0) | XV Delta (C3) |
| COMPUTED | Defect is catalyst (0.04% energy) | XV Gamma (C2) |
| PROXY-SUPPORTED | A_eff ≈ 2 from D7/D8 model | C3 (unvalidated) |
| UNRESOLVED | Temporal amplification physical status | C4 (regime mismatch) |
| CONDITIONAL | Early-universe regulator | XII Alpha (C3) |
| ABSENT | GW surplus | XII Beta (C5) |

---

## Table 5 — Surplus Portfolio

| Surplus | Post-XIV | Post-XV | Change |
|---------|---------|---------|--------|
| Interior positivity | Conditional (D9 + Layer 3 estimated) | **PROXY-SUPPORTED (f > 0 within model; A_eff unresolved)** | RE-CENTERED |
| Transient processing | Conditional | UNCHANGED | — |
| Cosmological regulator | Conditional | UNCHANGED | — |
| GW modification | Absent | UNCHANGED | — |
| **Portfolio** | 0 demonstrated + 2–3 conditional | **0 demonstrated + 2–3 conditional/proxy (A_eff UNRESOLVED)** | RE-CENTERED |

---

## Table 6 — Next-Stage Option Ranking

| Option | Question answered | Resolves mismatch? | Difficulty | Risk | Priority |
|--------|------------------|-------------------|-----------|------|----------|
| **B — Quasi-static rate** | **Is relaxation rate amplified on combined BG?** | **YES (linearized)** | **MODERATE** | May miss nonlinear | **FIRST** |
| A — Time-dependent PDE | Does full dynamics produce A_eff ~ 2? | YES (fully) | HIGH | Computational | SECOND (if B inconclusive) |
| C — Transient collapse | Does A > A_crit arise in collapse? | INDIRECTLY | HIGH | Different question | THIRD |
| D — Both A + B | Both | Both | Double scope | — | NOT SELECTED |

---

## Table 7 — Hard-Criteria Matrix

| Criterion | Assessment |
|-----------|-----------|
| Honesty | **PASS** (Gamma + Delta corrections preserved) |
| Regime clarity | **PASS** (temporal vs spatial explicitly stated) |
| Nontrivial content | **YES** (code, proxy result, BVP branch, regime finding) |
| Proxy dependence | **CRITICAL** (A_eff unvalidated) |
| Surplus restored | **NO** (0 demonstrated) |
| Next-stage quality | **HIGH** (quasi-static rate directly bridges regimes) |
| Worth continuing | **YES** (question is sharp and answerable) |

---

## Table 8 — Limitations

| Limitation | Severity |
|-----------|----------|
| A_eff ≈ 2 unvalidated | CRITICAL |
| Static BVP wrong tool for temporal question | FUNDAMENTAL |
| Interior repulsive (not compact) | SIGNIFICANT |
| Defect negligible as energy | INTERPRETIVE |
| Φ < 0 branch relevance unclear | MODERATE |
| No observational consequence | MODERATE |

---

## Table 9 — Final Handoff Decision

| Field | Value |
|-------|-------|
| Book XV closable? | **YES** |
| Verdict | **B** — re-centered unresolved frontier with clear handoff |
| Next stage | **Quasi-static rate analysis on combined background** |
| Designation | Program W5 or Book XVI Alpha |
| Key question | Is the scalar relaxation rate amplified above Schwarzschild rate? |
| If ~2×: | Proxy validated; surplus toward restored |
| If ~1×: | Proxy fails; surplus collapses |
| Cost change | **ZERO** (16/11/1/6 unchanged) |

---

*Book XV Terminal Ledger complete. Nine tables.*
