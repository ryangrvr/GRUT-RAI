# GR2-d2 — QUANTUM CONE SEPARATION: CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Fork:** GR2-d2, a **narrow re-charter of GR2-d gate Q-2 only**, under
the GR-2 campaign.
**Authority:** owner ruling of 2026-09-27 (`GR2D_OWNER_RULING_01.md`),
which accepts GR2-d at D-PARTIAL and authorizes exactly this isolated
quantum-leg experiment, with three required pre-run gates and one hard
rule.
**Not reopened:** the classical, exchange, relabeling, and memory legs
of GR2-d — adjudicated at the accepted D-PARTIAL. GR2-d's V-2/V-3
failures **stand at recorded strength** and are not retroactively
flipped by any outcome here.
**Source commits:** `master-w25bu9`; the quantum-front machinery of
`calc/gr2d_cone.py` (`ad66176`) replicated verbatim; the GR2-d recorded
sector-A front table as procedure anchor.

## 0. The question (the owner's, frozen verbatim)

> **Can an earned GRUT constraint distinguish genuinely different
> quantum propagation cones?**

What success can and cannot establish (frozen from the ruling): a clean
result establishes *quantum causal-cone distinction is demonstrable
within the tested class*, strengthening the irreducibility
demonstration — locality + influence + geometry + memory + quantum
dynamics ⇏ c_universal — and making the supplied status of causal
structure considerably harder to dispute. It does **not** establish
*the universal cone is derived*; that would need an earned
discriminator eliminating the different-cone alternatives, which no leg
here provides.

**The hard rule (the owner's, frozen):** if the separation gates fail
again, the failure is recorded. **No parameter re-selection.**

## 1. Gate one — parameter separation (established before any front measurement)

The target sectors are frozen here, chosen as **pure transverse-field
members** (h_z = 0) of the record's chain family, where the
quasiparticle velocity is exact — $v_{\max} = 2\min(J, h)$, from the
dispersion $\varepsilon(k) = 2\sqrt{J^2 + h^2 - 2Jh\cos k}$:

| target | (J, h_x, h_z) | analytic v_max |
|---|---|---|
| **C** | (1.0, 0.9045, 0.0) | **1.8090** |
| **D** | (0.5, 0.9, 0.0) | **1.0000** |

Analytic separation ratio **1.8090 ≥ 1.5** (the frozen requirement). D
is **not** a rescale of C (J/h = 1.105 vs 0.556), so the distinction is
not a units artifact. In-instrument gate P-1 (halt-grade): the two
$v_{\max}$ recomputed from the exact dispersion on a k-grid replicate
1.8090 and 1.0000 within $10^{-3}$ and their ratio is ≥ 1.5 — computed
**before** the front legs run.

## 2. Gate two — procedure calibration (disclosed; non-target sectors only)

The quantum-front estimator — $F(r, t) = \|[X_0(t), X_r]\,\psi_0\|$ on
7-site open chains, t step 0.05, relative arrival threshold 0.1,
least-squares fit over r = 1..5, machinery byte-for-byte that of
GR2-d — was calibrated **pre-freeze** on two sectors that are **not**
the targets:

| calibration sector | (J, h_x, h_z) | analytic v | measured t\*(1..5) | fitted v_est | systematic |
|---|---|---|---|---|---|
| E2 | (0.7, 0.6, 0.0) | 1.2 | 0.10, 0.65, 1.30, 2.00, 2.70 | 1.5267 | ×1.2723 |
| E3 | (0.8, 0.75, 0.0) | 1.5 | 0.10, 0.55, 1.10, 1.70, 2.25 | 1.8349 | ×1.2232 |

The estimator runs ~22–27% fast (the relative-threshold precursor
effect, the quantum analogue of the classical leg's +2.6%), drifting
~4% over Δv = 0.3 — so the ratio gate below leaves ≥ ±15% for
differential systematic. In-run, halt-grade:
- RQ-1 the GR2-d recorded sector-A table replicates exactly:
  t\* = (0.05, 0.45, 0.90, 1.40, 1.90) on its original [0, 6] window —
  the estimator is anchored to the accepted GR2-d run.
- RQ-2/RQ-3 the E2 and E3 calibration tables replicate exactly (window
  [0, 8]).
- QI-1 $F(r, 0) < 10^{-10}$ for all sectors and r; QI-2 unitarity
  $< 10^{-8}$ at t = 2.

## 3. Gate three — the blind separation gates (frozen here, before any target measurement)

The targets C and D are measured **only in the recorded run** (window
[0, 8], t step 0.05):

- **S-1** fitted-slope ratio $\mathrm{slope}_D / \mathrm{slope}_C \in
  [1.5, 2.1]$ (analytic ratio 1.809; the additive-lag component cancels
  in slopes, the multiplicative systematic largely cancels in the
  ratio).
- **S-2** $|t^*_C(5) - t^*_D(5)| > 0.25 \cdot \max(t^*_C(5),
  t^*_D(5))$ — the GR2-d Q-2 form, at a *stricter* threshold than the
  one that failed (0.25 vs 0.10), because this time the separation is
  analytically guaranteed at the microscopic level and the burden is on
  the measurement to exhibit it.
- **S-3** both targets earned-admissible: $t^*(r)$ strictly increasing
  over r = 1..5 for both; identical interaction graphs; ground-state
  two-time Gram of $\sum_i X_i$ PSD ($\ge -10^{-12}$) for both. The
  elimination row: sector D (the different-cone system) against the
  earned battery — the earned tests must pass it, or the outcome moves
  toward SELECTED territory per GR2-d's converse discipline.

No threshold in this section may be revisited after the target
measurement, and no alternative parameter set may be substituted under
any outcome (§0, the hard rule).

## 4. Outcome rule (frozen, mechanical)

- **D2-QCONE-DISTINCT** iff every gate holds: two earned-admissible
  quantum sectors with analytically separated and measurably distinct
  causal cones. Consequence (frozen from the ruling): quantum
  causal-cone distinction is demonstrable within the tested class;
  the irreducibility demonstration for the cone coordinate is
  strengthened — locality + influence + geometry + memory + quantum
  dynamics ⇏ c_universal; GR2-d's D-PARTIAL and its V-2/V-3 failures
  **still stand as recorded**; no status upgrade beyond this
  consequence; the universal cone is **not** thereby derived.
- **D2-QCONE-INDISTINCT** iff S-1 or S-2 fails while every control,
  identity, and admissibility gate passes: the failure is recorded at
  full strength; **no parameter re-selection**; what follows is the
  owner's to decide.
- **D2-PARTIAL** for any other gate failure; **HALT** (instrument bug,
  never physics; no verdict) on any P-1/RQ/QI breach.

Under every outcome: no red gate is touched; no public-record status
moves; the public paper is **not** updated. **HARD STOP** after the
verdict, pending owner ruling.

## 5. Instrument contract

`calc/gr2d2_qcone.py`: pure Python 3 standard library; helpers imported
unchanged from the committed `s41_sel4` and `partition_selection_p1`
modules; the front machinery replicated verbatim from
`calc/gr2d_cone.py` (X-probe path; the Z-probe diagnostic is not
re-run — representation independence was adjudicated in GR2-d);
deterministic (no RNG); single run; no post-hoc tuning; writes
`GR2D2_QCONE_RESULT.json` (sha-hashed) at the repository root with a
`defect_history` field; runtime minutes (five 128-dim
eigendecompositions plus two Gram evaluations). Scope: exactly the
GR2-d quantum-leg construction — 7-site open chains, D = 1, the
X-commutator front estimator. Nothing else is in scope.
