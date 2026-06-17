# GRUT v3 — Test 02: The C5b Orbital-Gate Derivation

**Date:** June 2026 (2026-06-17) · branch `main_v3`
**Status:** COMPLETE — **verdict B (ASSUMED, partial credit)**; adversarially verified (workflow
`w0lb09as8`; 5 agents converge).
**Question (the discharge gate banked by Test 01):** is the bound-system orbital gate
`1/(1+X²)`, `X=ω_dyn·τ₀` with `ω_dyn=v/r`, **derived** from GRUT's CTP constitutive physics — or a
phenomenological interpolation inherited from an earlier branch?

---

## Verdict: the form is derived; the controlling frequency is assumed

- **DERIVED — the gate FORM.** Varying the gravitational CTP action gives the constitutive kernel
  `K^R(ω)=α·χ(ω)·P^TT` with the single-pole susceptibility `χ(ω)=1/(1−iωτ₀)`. The gate
  `|χ(ω)|²=1/(1+(ωτ₀)²)` is genuine constitutive physics (α at DC, χ→0 at high ω = GR recovery).
  The MOND scale `a₀=cH₀/(2π)` it sets is independently derived from `τ_Λ=1/H₀`.
- **ASSUMED — the controlling frequency `ω_dyn=v/r`.** The string `ω_dyn` does not appear in the CTP
  action; `z_target`'s bound-system time-dependence is never written down. `rotation_curves.py`
  sets `omega_dyn = v/r` by hand and feeds it into the cosmological χ. There is no calculation that
  takes a virialized configuration, removes the separate-universe-absorbable mean field, computes
  the time-spectrum of the realized metric source, and shows it peaks at `ω ≈ v/r`.

## The crux (steady-state DC vs orbital) — resolved in direction, not magnitude

A virialized galaxy's **mean** field is quasi-static; if the medium relaxed to it, `χ(0)=1` → full
`α` (~33%), not the gated ~19%. **The No-Go defeats this objection** (`PROJECTOR_CONSISTENCY_NOGO.md`):
separate-universe invariance forbids response to any locally-absorbable/conformal mode, and the
halo's static homogeneous mean field IS such a mode — so the medium *principledly* ignores the mean
and responds only to realized/Weyl/tidal structure. **But the No-Go is a no-go, not a constructive
theorem.** It removes the mean from contention; it does **not** prove the surviving realized tidal
structure varies at precisely `v/r` rather than `σ/r`, a pattern speed, or a broad spectrum. `v/r`
is selected by dimensional plausibility, not by a CTP computation. → **half-resolved: direction
principled, magnitude assumed.**

## Flag — a latent regime-rule contradiction

The regime label is `X = max(ω_dyn, Λ_grav)·τ₀` (`closure_protocol.py`), but the galactic case uses
only `ω_dyn`, never computing `Λ_grav`. Applied literally, `Λ_grav` (Diósi-Penrose decoherence rate)
is enormous for a galaxy → `X→∞` → crystal → **zero** enhancement, contradicting the dark-matter use.
Resolution: `Λ_grav` is a *decoherence/classicalization* rate (relevant only for coherent-superposition
systems), **not** the gravitational-response frequency; for a classical virialized halo `ω_dyn`
governs. The `max(ω_dyn, Λ_grav)` rule must be scoped accordingly (the two are different physical
quantities, not comparable in a single `max`). Logged for repair.

## Banked

- `mond_a_0_emergence`: **HELD at `computed`** (the `a₀` scale is genuinely derived), statement
  **corrected** to split provenance: gate FORM derived / controlling frequency `ω_dyn` **assumed**,
  with the open discharge pointer. *Not* promoted to "derived."
- `rotation_curves.py` docstring already carries the split-provenance language (added by a
  verification agent this turn — reviewed: docstring-only, correct, kept). *Process note:* the
  verification workflow's skeptics ran with write access by oversight; future verification workflows
  are read-only (`Explore`-only).
- C5b **survives as conjectural-with-open-discharge — NOT collapsed to C5a.** It is genuinely
  distinct from the ruled-out linear branch (responds to realized tidal structure, escapes the
  No-Go that killed `Ω_dm=1/3`), carries a derived `a₀`, and yields a falsifiable high-ω MOND
  deviation. What it lacks is a derived controlling frequency.

## The recurring v3 signature (third instance)

The mathematics survives; the ontology changes. The gate *form* is real constitutive physics; its
*status as a derived bound-system law* is not. (Cf. Koide: identity survives, prediction lost;
linear enhancement: possibility survives, selection lost; `Ω_dm=1/3`: integral survives,
interpretation lost.)

## Open discharge (Test 02's exit gate — NOT cleared)

Take a virialized bound configuration, remove the separate-universe-absorbable mean field per the
No-Go, compute the **time-spectrum of the realized/Weyl metric source `h_r(t)`** the medium sees, and
show it is dominated by `ω ≈ v/r` — **or** show it is dominated by a different scale (`σ/r`, pattern
speed, broadband) and re-derive the gate accordingly.
- If `v/r` **confirmed** → promote the gate frequency and `mond_a_0_emergence` to derived; C5b becomes structural.
- If **refuted** → the bound-system gate frequency is replaced, and the dark sector routes further toward **C5a (W² second-order, uncomputed)**.

This is the next concrete C5b computation. Until it clears, full `Ω_dm` and the flat-curve shape
remain routed to **C5a**.
