# NON-STATIONARITY MEASUREMENT — CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Date:** 2026-09-25 · **Chartered by:** owner
(`KERNEL_TRANSPORT_OWNER_RULING_01.md` §3), question verbatim:

> **How large is K(t,t′) − K(t−t′) on the stored exact FRW solutions?**

**Binding constraints (owner):** pre-registered norm / fractional residual on
the transport instrument's grid class; **no new physical assumption**; the
instrument does NOT search for a transport law; it is **characterization of
an already-derived object, not a rescue of the old cosmological
discriminator, and not a prediction campaign.** Register untouched;
ledger 0; Λ_R, Matsubara, Π₀, U5 remain fenced.

---

## 1. THE OBJECT, AND AN HONESTY POINT SETTLED BEFORE ANY NUMBER EXISTS

The measured object is the one the transport instrument already computed and
validated: the **free TT commutator kernel at fixed comoving k**,
K(t, t′; k), from the C1-validated primitive on the declared Ω_m = 0.315
background (charter A4/A7), integrator controls at machine precision.

**Disclosed at pre-registration:** at fixed comoving k, even the de Sitter
mode kernel is not Δt-only — comoving k is not an invariant label (physical
wavenumber redshifts), so some same-lag drift exists even on the maximally
symmetric background. The object D3a proves stationary on dS is the
*position-space worldline* correlator, whose measurement would require a
smearing/window choice — **a new input, named here and NOT taken.** The
instrument therefore reports three curves on one grid:

- **FRW drift** (the measurement),
- **dS(H₀) comparator drift** (the declared maximally-symmetric baseline;
  H = H₀ and a(t₀) = 1 is a disclosed convention, not a physical claim),
- **flat-space drift** (exact zero control: at a ≡ 1 the kernel IS Δt-only).

The FRW-specific statement is the raw FRW drift together with its **excess
over the dS comparator**; both are reported, neither is suppressed.

## 2. THE GRID (frozen)

Anchors (observation) z_a ∈ {0, 0.25, 0.5}; cosmic-time lags
L·H₀ ∈ {0.1, 0.2, 0.4}; comoving k/(a₀H₀) ∈ {0.5, 1, 2}. A cell whose
emission time falls before the stored solution's start (z = 200) is dropped
with disclosure (none is expected to). Same integrator, same background,
same units as the transport instrument.

## 3. THE PRE-REGISTERED MEASURES

For each (k, L), over the anchor set {t_a}, with K_cell = K(t_a, t_a−L; k):

- **M1 — same-lag drift (primary):**
  spread(k, L) = max_a K_cell − min_a K_cell, reported two ways:
  (n1) normalized by max_grid |K| (global, robust near zeros);
  (n2) relative: spread / mean_a |K_cell|, reported for cells whose
  mean_a |K_cell| > 0.1 × max_grid |K| (declared floor against fake
  divergence). **Headline number: max over reportable cells of (n2) for
  FRW**, with the full table and the dS-comparator and flat values beside
  it.
- **M2 — best-stationary residual (secondary):** with
  K̄(L, k) = mean over anchors (the assumption-free Δt-only approximant on
  the sampled set), R(k) = sqrt[ Σ_{L,a}(K_cell − K̄)² / Σ_{L,a} K_cell² ],
  and the overall R pooled over k. This is the fraction of the kernel's
  sampled variation that no Δt-only function can carry.
- **M3 — excess over dS:** for each reportable cell,
  excess(k, L) = drift_FRW(n2) − drift_dS(n2); its grid maximum is reported
  beside the headline.

## 4. CONTROLS (halt on miss) AND FENCES

- Flat-space drift = 0 to 1e-10 (exact zero control).
- dS comparator evaluated from the closed BD form (already validated to
  1.4e-14 against the integrator); one spot-check against a numeric dS run.
- Integrator inherits the transport instrument's validated `Run` class
  unchanged (Wronskian, state-independence re-checked on one production
  run).
- **NO-CAMPAIGN fence (owner):** the instrument outputs measured numbers
  and nothing else — no transport rule is proposed, no discriminator is
  evaluated, no fenced route is touched, no register field changes. The
  verdict document is a measurement report; its only forward sentence is
  the D3b linkage (the measured size of the two-time structure).
- **NO-SELECTION:** all cells reported; the reporting floor (0.1) is frozen
  here, before any number exists.

## 5. DELIVERABLES AND STOP

1. `calc/kernel_nonstationarity.py` — reuses the validated integrator;
   emits `KERNEL_NONSTATIONARITY_RESULT.json` (sha-hashed).
2. `NONSTATIONARITY_RESULT_01.md` — the measurement report.
3. **HARD STOP at the report** (the waiting decision: the owner reads the
   measured magnitude and decides what, if anything, it changes about the
   fenced queue). No route is opened by this instrument.
