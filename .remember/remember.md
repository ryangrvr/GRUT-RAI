# Handoff

## State
**On branch `main_v3` (the GitHub default; v3.0.0.dev0). v2 retired at tag `v2-final`.**
v3 = GR-limit dilatation redundancy broken by one scale L₀=cτ₀≈12.85 Mpc; pillars Q (CTP, proven) +
F (finite memory, postulated); **F breaks D**; **μ_linear=1 → linear cosmology = ΛCDM**.

**The v3 dark-sector AUDIT (Tests 01–04) is COMPLETE and CHECKPOINTED** (tag `v3-audit-checkpoint`,
local). It compressed the dark sector from 4 mechanisms to: **C5a (W²) sole surviving channel
(undetermined)**, `a₀` scale survives, everything else refuted.
- Test 01: dielectric Ω_dm=1/3 + linear enhancement → RULED OUT (omega_dm_equals_alpha → open_negative).
- Test 02: C5b gate frequency → ASSUMED (mond_a_0_emergence statement corrected).
- Test 03: C5b gate magnitude → REFUTED (~1/√N negligible).
- Test 04: C5a (W²) → UNDETERMINED — sign ✓, scaling ✓, magnitude swings ~10²⁷× on the L₀-vs-local
  scale; hinges on the uncomputed 2nd-order CTP kernel K⁽²⁾ (registry: `c5a_weyl_squared_dark_sector`,
  conjectural). Docs: `theory/GRUT_V3_TEST_0[1-4]_*.md`, `theory/GRUT_V3_AUDIT_CHECKPOINT.md`.

## Next
1. **Test 05 = the constructive phase** — the decisive computation: derive `K⁽²⁾ = δ²S_CTP/δh_a δh_r|_{O(2)}`,
   its coupling length scale (L₀ → C5a dies; local r → galaxy-marginal + cluster overshoot) and
   prefactor σ. This single computation closes GRUT's dark sector (viable or dead).
2. Other open frontiers: α-selection (4th-order Riegert), the L₀→0 redundancy proof.

## Context
- **Holding the PUSH** (user: build more before pushing). main_v3 IS already on GitHub as default
  (pushed at the v3-build commit); the Test 01–04 batch is committed locally on main_v3, NOT pushed.
- **Workflow agents must be read-only for verification** (`agentType:'Explore'`). A non-Explore
  skeptic edited rotation_curves.py docstring in Test 02 (reviewed, correct, kept) — lesson applied.
- Discipline: adversarial verification; survivors are constraints + honest no-gos. The recurring v3
  signature: "the math survives, the ontology changes." Hold any clean positive to the same check.
- python3.12 for code/tests; uploads/pdf_venv/bin/python3.12 for PDF builds. v2 book/PDF frozen.
