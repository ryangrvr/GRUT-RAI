# TIER 2 — THE MASSLESS GRAVITON BATH: VERDICT

**Date:** 2026-08-31 · **Authorization:** owner, 2026-08-31 (bath ONLY) ·
**Declarations:** D1=1a, D2=2a, D3=3a (countersign d5dc33b) ·
**Instrument:** `wall_kr_tier2_massless_bath.py`
(sha `546df0d90ac5c62f…`; a one-character transcription error in the first
committed version of this line — `…c62b` — was caught by the Tier-3 T3-0
pin gate and corrected 2026-08-31; the file itself never changed) ·
**Artifact:**
`WALL_KR_TIER2_MASSLESS_BATH.json` (sha `c5d399f525407839…`) ·
**Battery:** 39/39, zero failures, every control detecting ·
**Mutation battery:** 4/4 killed. **W-0: computed-and-reported, NOT banked.**

## PRIMARY QUESTION — ANSWERED

*"Is the massless graviton bath, including its IR prescription, a validated
input for the contract-level K_R calculation?"*

**YES — with two recorded fences.** Every object the fixed-ω contract path
requires is constructed, gated, and IR-finite per order under dimensional
continuation with **no IR scale introduced**. The two fences: (i) the
equal-time/secular class carries a scaleless 1/(d−3) pole at O(H²) — fork
(ii) is **ARMED, not fired**, with its trigger condition recorded; (ii) the
graded ω-domain reporting is valid for ω ≫ H — the ω → 0 class question is
outside the truncation's validity and is NOT adjudicated here.

## THE BATH (frozen)

- **Mode (exact, closed form):** h_k(u) = N e^{−iku}[(1−Hu) + iH/k] solves
  the derived TT mode equation (a²h′)′ + k²a²h = 0 **exactly**. The BD mode
  of this chart is **polynomial in H** — the per-mode kernels TERMINATE at
  O(H²), so the graded state IS the exact state per mode and **Option A ran
  as a live cross-check**, not a deferred gesture (V3 condition 4
  satisfied concretely).
- **Quadratic action (derived + tied):** L₂ = (1/2κ²)·P(u)(ψ′ψ*′ − k²ψψ*),
  **P = −a² exactly** — the pipeline's Ricci orientation (the same one
  giving R_dS = −12H², Λ = −3H², G3 = +1·p₁·p₂) carries into the kinetic
  weight. The independent quadratic build matches the **frozen Tier-1
  cached {1,2} sector pointwise** through O(H²), including the off-shell
  EOM-class structure — consistent dressing with the Tier-1 vertex is a
  gate, not a claim.
- **Normalization chain (no textbook import):** pipeline density → reduced
  action → classical retarded response (variation of parameters; source
  defined by S_int = (1/2)h_ij T^ij) → |N|² = κ²/k by magnitude + state
  positivity. The Kubo factor then comes out **derived**:
  G_R = −iθ⟨[ψ,ψ*]⟩ — the standard retarded definition, as a **result**.
- **Flat anchor:** G_R(H=0) = −2κ²θ(Δ)sin(kΔ)/k — shape and magnitude are
  the anchor content; the overall sign is the derived pipeline orientation
  (in the standard Ricci orientation P and G_R flip together).
  ω·Im G_R < 0, so Im χ = −Im G_R > 0: the passive orientation of the
  frozen χ = −G dictionary.
- **KMS/FDT:** W₊ = e^{−ikΔ} × (degree-2 polynomial in Δ) at every base
  time — all frequency content at ω = +k, so the T = 0 adiabatic FDT
  N(ω) = ½sgn(ω)ρ(ω) holds **identically** per order. The dS temperature
  H/2π is a static-patch, non-perturbative statement (invisible at every
  finite H order) — recorded as the Option-A thermality cross-check target.

## THE IR VERDICT (the load-bearing part)

| object | small-k / d-continuation | status |
|---|---|---|
| retarded/spectral kernel (fixed Δ) | **finite as k → 0**: the 1/k and 1/k³ enhancements CANCEL; limit = −2κ²(Δ + H²Δ³/12) | IR-SOFT, exact |
| noise/Hadamard kernel (fixed Δ) | → κ²H²/k³ (dS superhorizon enhancement, **exact in BD** — not a truncation artifact) | IR-ENHANCED at O(H²) |
| fixed-ω mode sums | δ-support at k = ω > 0: k → 0 never sampled; analytic at d = 3 | FINITE per order, no scale |
| equal-time O(H²) mode sum | scaleless H²k₀^{d−3}/(d−3) pole; residue split-point independent | CLASSIFIED, not regulated |

**The structural finding:** dissipation is IR-soft; the superhorizon
enhancement lives entirely in the noise/state half. **Fork-(ii) trigger
(armed):** if any downstream tier's loop integrals sample the
equal-time/secular class (the k^{−3} noise region with non-oscillatory
weight), the 1/(d−3) pole enters and fork (ii) fires *there* — "named and
priced — a new register input." No IR scale was necessary here; none was
introduced.

## THE SPECTRAL DENSITY (T2-4)

Support exactly on the light cone ω = ±k at every order (graded
corrections are δ′/δ″ **on** the cone: c₀ = (κ²/k)[(1−Hu_b)² + H²/k²],
c₁ = iκ²H²/k², c₂ = −κ²H²/4k); gapless; c₀ a sum of squares (positivity,
with full distributional positivity inherited from the exact BD state).
TT-traced fixed-ω mode sum at d = 3, u_b = 0:

    rho_bar(omega) = (2 kappa^2 / pi) * (omega + H^2/omega)

i.e. flat part ∝ ω^{d−2} with **relative O(H²) correction = H²/ω²
exactly** (the δ′/δ″ cone terms carry (d−3) factors and vanish at d = 3).
Reported factually with the ω ≫ H validity fence; **not fitted to, and not
compared with, any registered family** (guard live; the Q3-class outcome
table applies only at the K_R level, k → 0 first, ω → 0 LAST).

## THE EIGHT DECLARED CHECKS

1. flat anchor ✓ 2. normalization (jump + Wronskian + pipeline tie) ✓
3. retarded sign (upper-half FT = closed form, rel < 1e−12) ✓
4. spectral positivity ✓ 5. IR convergence ✓ 6. dimensional scaling
(analytic at d=3 fixed-ω vs 1/(d−3) equal-time — the pole detector fires
exactly where it must) ✓ 7. wrong-state control: Bogoliubov β ≠ 0
DETECTED by the FDT/support gate while G_R stays blind (both directions
gated) ✓ 8. wrong-retarded-sign control: Im-sign flip DETECTED ✓

## DEFECT HISTORY (all disclosed; every defect instrument-side)

- **Run 1:** exp(ikz)-explicit representation stalled past the 20-minute
  rule → killed, re-represented with phases absorbed into the nilpotent
  markers (the Tier-1 lesson). 78 s → 61 s total afterward.
- **Run 2 (6 failures, the valuable ones):** the P-gate caught
  **P = −a²** — and thereby exposed that the run-2 "flat anchor pass" was
  **two compensating hand-set signs** (+2κ² asserted, +2κ² hand-built).
  The whole response chain was rebuilt orientation-derived. Remaining
  four: unmapped plain-`u` symbol vs real-`u` (two symbols printing
  identically defeated the tie's cancellation), sqrt(a²) → Abs breaking
  the v-form check, plain quadrature on a slowly-damped oscillatory tail
  (rel 8e+02 — replaced by quadosc + finite-η exact comparison), and
  sympy Piecewise on the symbolic-d integral (replaced by a gated exact
  antiderivative).
- **Mutation battery (mandatory, calc-layer floor):** M1 wrong-Λ, M2
  corrupted mode, M3 wrong |N|², M4 wrong response sign — **all four
  killed** by the intended gates. Harness defect disclosed: the mutants
  ran in the ledger and overwrote the artifact; the clean instrument was
  re-run (run 4) and reproduced the artifact **byte-identical**
  (sha c5d399f5… deterministic).

## SCOPE LIMITATIONS

Per-mode and mode-sum objects only — no loop, no vertex application. The
δ′/δ″ cone-weight FT phase conventions enter no d = 3 deliverable (they
carry (d−3) factors); recorded. Tensor assembly declared:
kernel^{ij,kl} = P^TT_{ij,kl}(k̂) × scalar kernel (trace (d+1)(d−2)/2 = 2
polarizations at d = 3, projector gated idempotent + transverse).
Wigner-domain objects use the declared base-time convention (u_b = 0 for
quoted numbers; general u_b in the artifact).

## HARD STOP

No contract-level loop, no TT-TT-TT vertex application, no D5, no D4
response comparison, no K_R, no matter-pole revisit, no Ward modification,
no comparator comparison. **The bath is frozen pending owner inspection.**
