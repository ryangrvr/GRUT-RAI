# GRUT v3 — The K⁽²⁾ Derivation (Constructive Phase, running record)

**Branch `main_v3` · constructive phase · audit frozen at tag `v3-audit-complete`**
**Flagship problem:** compute the explicit second-order CTP kernel
`K⁽²⁾_μνρσ = δ²S_IF / δh_a δh_r² |_{O(2)}` and the length scale it forces.
Decides whether GRUT possesses a *derived* dark-matter mechanism. See
`GRUT_V3_CONSTRUCTIVE_PHASE.md` for the problem statement and the moratorium.

This file accumulates the four stages (A → B → C → D) as each completes.

---

## Stage A — Minimal S_IF + the permitted O(2) operator basis  ✅ COMPLETE

**Method:** five independent reconstructions + skeptics (read-only workflow `wakeieuaw`),
grounded in `grut/derivation/phi_munu/linearized_ctp_action.py`,
`theory/PROJECTOR_CONSISTENCY_NOGO.md`, and the closure protocol. Convergent.

### A.1 The minimal surviving influence action (four terms)

```
S_IF[h_a, h_r] =
   S_EH       (linearized Einstein–Hilbert, per CTP branch)
 + S_matter   = ½ h_a^μν T_μν                    (minimal coupling; equivalence principle)
 + S_const    = −½ ∫∫ h_a^μν(x) K^R_μνρσ(x−x') h_r^ρσ(x')      (the sole responsive channel)
 + S_noise    = (i/2) h_a N h_a                  (Keldysh/FDT noise; vanishes at h_a=0)

  K^R_μνρσ(ω) = α_vac · χ(ω) · P^TT_μνρσ
     α_vac = 1/3              (conformal-mode-scalar identification; KS 2011)
     χ(ω)  = 1/(1 − iωτ₀)     (single-pole, causal — PURELY TEMPORAL memory)
     τ₀    = 41.9 Myr  →  L₀ = cτ₀ ≈ 12.85 Mpc   (the only dimensionful scale in K^R)
     P^TT  = transverse-tracefree projector (ALGEBRAIC in k̂ — direction only, dimensionless)
```

Structural properties: `S_IF[diagonal] = 0` (CTP on-shell); the responsive kernel is
**spatially scale-free** — temporal memory `χ(ω)` × the dimensionless directional projector
`P^TT`; it carries **no `|k|`-magnitude / `(L₀k)²` term**. No dark-sector mechanism imported
(moratorium honoured).

### A.2 The permitted O(2) operator basis — the Stage A result

The second-order operator is gated by the No-Go (separate-universe invariance ⊥ a conformal
scalar response ⇒ `μ_linear = 1`), minimal coupling, and kernel locality. Of the curvature-squared
basis {W², E₄, R², R_μν², □R}:

| Operator | Verdict | Reason |
|---|---|---|
| **W² = C_μνρσC^μνρσ** (Weyl²) | ✅ **PERMITTED — the unique dynamically-active channel** | Conformal/tracefree; W̄=0 on FRW (conformally flat) ⇒ `δW² = O(h²)`, genuinely second-order ⇒ escapes the linear-scalar No-Go; the c-anomaly channel; compatible with minimal coupling + tracefree P^TT |
| **E₄** (Gauss–Bonnet / Euler density) | ⊘ **PERMITTED but DORMANT (topological)** | The **a-anomaly** channel. In 4D `∫√g E₄` is the Euler characteristic — a topological invariant; its metric variation vanishes identically (Lovelock) on a fixed-topology background ⇒ **no local dynamical stress-energy**. Admissible in the basis, but contributes nothing to a local K⁽²⁾ unless a nonlocal Riegert structure activates it (Stage B checks). *Not* excluded "by the No-Go" — excluded by being topological. |
| **R², R_μν², □R** (Ricci-built) | ❌ **FORBIDDEN** | R, R_μν couple to the stress-energy trace via Einstein's eq; a response ∝ Ricci² reduces to a *first-order matter-density* response ⇒ violates `μ_linear=1` (the No-Go). Also: the kernel carries no `∇²` to build the required structure, and □R is 4th-order (incompatible with the single-pole χ). |

**Result:** **W² is the sole dynamically-active second-order operator.** If GRUT has a derived
dark-sector mechanism, it is uniquely W². E₄ is in the permitted basis but topologically dormant;
Ricci-built operators are excluded for good.

> **Correction to the workflow synthesis (banked deliberately):** the raw synthesis attributed
> E₄'s exclusion to "the No-Go forbidding the conformal channel" and rated it merely
> "phenomenologically secondary." That conflates two channels. E₄ is the **a-anomaly / Euler-density**
> term; its suppression is **topological** (Lovelock-null in 4D), not a No-Go consequence. Banking the
> sloppy attribution would risk Stage B mis-reading an E₄ survival as a No-Go violation. The precise
> statement: **W² (c-anomaly) is dynamical; E₄ (a-anomaly) is topological/dormant.**

### A.3 The scale candidates — and a sharpened read (revises the soft prior)

The coupling form is dimensionally `ρ_eff ~ σ · α_vac · L² · W²` (`[L²·W²] = 1/L² = [ρ]` in
G=c=1). `α_vac = 1/3` is locked; `σ ~ O(1)` is estimated, unverified; **`L` is the ~10²⁷× swing**
that decides C5a's fate.

| Scale | If selected | Requires |
|---|---|---|
| **L₀ = cτ₀ ≈ 12.85 Mpc** | `ρ_eff/ρ_baryon ≪ 1` → **C5a DIES**, DM hosted | nothing — it is the only scale `K^R` carries |
| **local `r`** (system size / `1/√W`) | galaxy-marginal (best GRUT signal) + ~100× cluster overshoot | a **spatial nonlocality** (`1/∇²`) to replace `L₀²` by `r²` |

**Sharpened structural lean (revises the Stage-A synthesis's ~60% local-`r` optimism):** the
*surviving* TT kernel `K^R = α χ(ω) P^TT` is **spatially scale-free** — `χ` is purely temporal,
`P^TT` is dimensionless/directional (confirmed in `linearized_ctp_action.py`; the `(L₀k)²`
spatial structure in `retarded_kernel_frw.py` belongs to the **ruled-out scalar μ-channel**, not
this one). A spatially-local kernel's second variation **cannot generate `1/∇²`**: integration by
parts on `W²~(∂²h)²` moves derivatives, it does not create an inverse Laplacian. So the only length
available is `L₀`, and the lean is **toward `L = L₀` → C5a dies**, not toward survival.

**The one genuine open question Stage B must settle:** does the *second-order* TT response use the
spatially-scale-free temporal kernel (`linearized_ctp_action` C4: `L₀`-only → death), or does it
inherit a `χ_eq(k)`-type spatial structure (`retarded_kernel_frw`, Phase 2D → possibly different)?
The first-order audit ruled the spatial structure into the *scalar* channel only; whether it
re-enters the *tensor* channel at second order is exactly the K⁽²⁾ computation. **No soft prior
overrides the explicit algebra — but the structural prior now points at death, not survival.**

### A.4 Stage A status

| Component | Status |
|---|---|
| Minimal S_IF (4 terms) | **established** |
| Permitted O(2) basis | **closed: W² unique dynamical; E₄ dormant/topological; Ricci forbidden** |
| Length scale `L` | **undetermined** — structural lean now toward `L₀` (death), pending Stage B |
| Prefactor `σ` | estimated `~O(1)`, unverified |
| `μ_linear = 1` | intact (W̄=0 on FRW ⇒ no linear signal) |
| Dark-sector fate | contingent on Stage B (the explicit second variation) |

---

## Stage B — The explicit second variation: the scale is L₀  ✅ COMPLETE

**Method:** workflow `whbpphrbb` (locality + compute + adversary) and closure `wgzzxunwo`
(explicit flat-space `K⁽²⁾(ω,k)` + k-pole test), both read-only; plus a direct re-derivation.

**Result — `L = L₀` is forced.** The explicit flat-space second variation gives

```
K⁽²⁾(ω,k) = σ · α_vac · χ(ω)          [k-INDEPENDENT — no 1/k² pole]
ρ_eff      = σ · α_vac · L₀² · W²       L = L₀ = c·τ₀ ≈ 12.85 Mpc
```

The surviving TT kernel `K^R = α·χ(ω)·P^TT` is spatially scale-free (χ purely temporal; `P^TT`
dimensionless/directional), so the only length the second variation can carry is `L₀`. The
local-`r` branch is **impossible**: a spatially-local causal memory kernel is a *polynomial in k²*
(entire function); `1/∇² ~ 1/k²` is a *pole at k=0*; no differentiation or integration-by-parts
turns a polynomial into a function with a pole (distribution theorem). All three closure routes
returned `no_pole_polynomial`; the `W²~(∂²h)²` source carries `k⁴` (polynomial), never `1/k²`.
3-0 locality + 2-0 compute + both closure skeptics confirmed. **Scale settled: `L=L₀`.**

Residual (honest): the exact `O(1)` prefactor `σ` and the full *covariant* tensor form of `K⁽²⁾`
need a dedicated CAS (xAct); `σ ∈ {1/3,1,3,9}` shifts only the magnitude, never the scale or shape.

## Stage C — The magnitude is VIABLE, not negligible  ✅ COMPLETE (a banked error corrected)

A workflow (`wq1lz8509`) first claimed `ρ_eff/ρ_baryon ~ 1e-27 ⇒ C5a dies`. **That was wrong** —
two independent arithmetic bugs, caught by a direct geometric-units recomputation:

1. **Unit mismatch** — comparing a *geometric* `ρ_eff` (`1/L²`) to an *SI* `ρ_baryon` (`kg/m³`)
   without the `c²/G ≈ 1.35×10²⁷` conversion. *That factor is the spurious `1e-27`.*
2. **Wrong Weyl formula** — `W²=48(r_s/r)⁶` (dimensionless) instead of `48(GM/c²)²/r⁶` (`1/L⁴`).

In consistent units the magnitude is `O(1–100)`:

| System | `ρ_eff/ρ_baryon` (σ=1) |
|---|---|
| Galaxy 10 kpc | ~53 |
| Galaxy 30 kpc | ~2 |
| MW 8 kpc | ~62 |
| Cluster core 0.3 Mpc | ~20 |
| Cluster 2 Mpc | ~0.07 |

The physical reason: `ρ_eff/ρ_baryon ~ α·(L₀/L_curv)²`, and the **curvature radius** of a *weak-field*
galaxy is `L_curv ~ r/√Φ ~ tens of Mpc` — *comparable to `L₀`*, not the ~10 kpc system size. A
genuine coincidence: `L₀` lands near the galactic curvature scale. **C5a does not die on magnitude.**

## Stage D — The shape is WRONG: the decisive phenomenology  ✅ COMPLETE

`ρ_eff ∝ W²`. For an extended spherical profile the weak-field Weyl is
`W² = (16/3)Λ²`, `Λ = Φ''−Φ'/r = 4π(ρ−⟨ρ⟩)`, so `ρ_eff ∝ (ρ−⟨ρ⟩)²`. For an isothermal halo
(`ρ∝1/r²`): `ρ_eff ∝ ρ² ∝ 1/r⁴` — **log-slope ≈ −3.9**, far steeper than the **−2** a *flat*
rotation curve requires (`ρ_DM∝1/r²`). The implied enclosed `M_eff(r)` saturates and `v_eff(r)`
*falls* with radius. The `W²` source is centrally concentrated and tracks **baryons-squared** — it
is **not** the extended, flat-curve dark halo, and `σ` (which scales magnitude only) cannot fix the
shape. Module: `grut/derivation/phi_munu/second_order_kernel.py` (`verify()` locks all six legs).

---

## VERDICT — the constructive-phase flagship is RESOLVED

> **C5a (the `W²` second-order channel) produces a real effective source of the right ORDER OF
> MAGNITUDE at galactic scales (`ρ_eff/ρ_baryon ~ O(1–100)`, not `1e-27`) but with the WRONG RADIAL
> PROFILE (`ρ_eff ∝ W² ∝ ρ_baryon² ∝ 1/r⁴`, too steep) to be the dark-matter halo. GRUT has NO
> derived dark-matter mechanism that reproduces halo phenomenology; dark matter remains a HOSTED
> input — with the derived `a₀` scale and `μ_linear=1` (linear cosmology = ΛCDM).**

The recurring v3 signature, once more: **the math survives, the ontology changes.** The audit had
compressed the dark sector to this one computation; the computation is now done, and it closes the
constructive-phase flagship. The moratorium's premise holds — C5a not being the DM mechanism is the
honest endpoint, **not** a cue to invent a fifth mechanism.

**Stages A–D complete.** Scale `L₀` (rigorous) · magnitude viable (error corrected) · shape refuted
(decisive). Residual: exact `σ` + full covariant `K⁽²⁾` (CAS) — cannot change the shape verdict.

---

## Test 06 — the shape failure is a THEOREM, not a heuristic artifact  ✅ COMPLETE

The Stage-D verdict rested on one assumption: `ρ_eff ∝ W²` (the scalar). Test 06 (workflow `wo7mvnscu`;
full record `GRUT_V3_TEST_06_PROFILE_THEOREM.md`) derives the effective `00`-source from the actual
tensor structure of `Φ⁽²⁾_μν` and shows **all permitted routes converge to `ρ_eff ∝ 1/r⁴` (or steeper)**:

- **Route A** scalar `W²` → `1/r⁴`.
- **Route B** Bach tensor `B_μν ~ ∇∇C ⇒ ∇²ρ_baryon` → `1/r⁴` (same; `bach_route_isothermal_slope()=−4`).
- **Route C** `P^TT` loophole → `1/r⁴` (closed): the `k_ik_j/k²` is **degree-0 in `|k|`** (angular,
  not a `1/∇²` pole), and `K⁽²⁾(ω,k)` is k-independent (Stage B), so no inverse Laplacian survives.

**Why it's a theorem:** shallowing `1/r⁴ → 1/r²` requires *integrating* the source (`1/∇²`) — the very
operation the locality result that fixes `L=L₀` forbids. 3/3 skeptics (incl. one tasked only with
*reviving* C5a) classified the failure `theorem_from_locality`; none found a shallowing mechanism. The
dark-sector frontier — "can the `W²` response be dressed to change its radial scaling?" — is therefore
not just open-and-disfavored but **provably closed within the local, causal, No-Go-respecting kernel.**
