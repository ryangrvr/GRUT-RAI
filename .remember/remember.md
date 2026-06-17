# Handoff

## State
**On branch `main_v3` (the GitHub default; v3.0.0.dev0). v2 retired at tag `v2-final`.**
v3 = GR-limit dilatation redundancy broken by one scale L₀=cτ₀≈12.85 Mpc; pillars Q (CTP, proven) +
F (finite memory, postulated); **F breaks D**; **μ_linear=1 → linear cosmology = ΛCDM**.

**The v3 dark-sector AUDIT PHASE (Tests 01–05) is COMPLETE and FROZEN** (tag `v3-audit-complete`,
local; intermediate tag `v3-audit-checkpoint` = Tests 01–04). It compressed the dark sector from
4 mechanisms to **one surviving channel (C5a, W²) + one scale (a₀) + one decisive computation (K⁽²⁾)**.
- T01: dielectric Ω_dm=1/3 + linear enhancement → RULED OUT (omega_dm_equals_alpha → open_negative).
- T02: C5b gate frequency → ASSUMED. T03: C5b gate magnitude → REFUTED (~1/√N).
- T04: C5a (W²) → UNDETERMINED (sign ✓, scaling ✓, magnitude open).
- T05: reduced C5a to the single symbolic K⁽²⁾ computation (`undetermined_needs_symbolic`; soft lean
  toward local-scale → galaxy-marginal, but a cluster ~100× overshoot). Registry:
  `c5a_weyl_squared_dark_sector` (conjectural). Docs: `theory/GRUT_V3_TEST_0[1-5]_*.md`.

## Next — the CONSTRUCTIVE phase (one flagship problem)
1. **Compute K⁽²⁾ = δ²S_IF/δh_a δh_r²|_{O(2)}** (symbolic, sympy/xAct on FRW+halo): its coupling
   length scale (L₀ → C5a dies; local r → galaxy-marginal) + prefactor σ → new module
   `grut/derivation/phi_munu/second_order_kernel.py`. Spec: `theory/GRUT_V3_CONSTRUCTIVE_PHASE.md`.
   This single calculation decides whether GRUT has a derived dark-matter mechanism.
2. **MORATORIUM (active):** propose NO new dark-sector mechanism until K⁽²⁾ is computed (re-spreading
   would reproduce the v2 mechanism-accumulation failure the audit cured). If C5a dies → dark matter
   is a hosted input (with a derived a₀); not a cue to invent a fifth mechanism.
3. Other open frontiers (after / parallel, not dark-sector): α-selection (4th-order Riegert), the
   L₀→0 redundancy proof.

## Context
- **Holding the PUSH** (user: build more before pushing). main_v3 is on GitHub at the v3-build commit;
  ALL of Tests 01–05 are committed locally on main_v3, NOT pushed.
- **Verification workflows must be read-only** (`agentType:'Explore'`). (A non-Explore skeptic edited
  rotation_curves.py in T02 — reviewed/kept; lesson applied for T03–T05.)
- Discipline: adversarial verification; survivors are constraints + honest no-gos; recurring signature
  "math survives, ontology changes." Hold any clean positive to the same check.
- python3.12 for code/tests; uploads/pdf_venv/bin/python3.12 for PDF builds. v2 book/PDF frozen.
