# Handoff

## State
**V2→V3 transition COMPLETE (June 2026). Now on branch `v3`, version 3.0.0.dev0.**
- v2 RETIRED + FROZEN at tag **`v2-final`** (branch `v2`, commit 393efe5, version 2.8.0): the
  v2.8 Final book (`uploads/GRUT_TOE.pdf`, with V2→V3 Synthesis foreword) + the v3-readiness-audited
  backend. NOT pushed (local only).
- v3 OPERATIVE (commit f156adf): inherits the verified backend; `STATUS.md` declares the corrected
  physics. Suite green: **3209 passed, 2 xfailed** (documented camb-fork ΛCDM baseline).
- v3 physics: GRUT = GR-limit dilatation redundancy broken by one scale L₀=cτ₀≈12.85 Mpc; pillars
  Q (CTP unitarity, proven) + F (finite memory, postulated); **F breaks D**; **μ_linear=1 →
  linear cosmology = ΛCDM**. Foundation: `theory/GRUT_V3_ORGANIZING_STRUCTURE.md`,
  `theory/V2_TO_V3_SYNTHESIS.md`, `grut/foundation/organizing_structure.py`.

## Next
1. Begin building v3 forward on the spine in `V2_TO_V3_SYNTHESIS.md §9` (foundation-first).
2. Live frontiers (the real physics): **nonlinear/tensor dark sector** (C5a W², C5b orbital-ω,
   C5c TT) — the only surviving home for GRUT deviations; first-principles α (4th-order Riegert);
   the L₀→0 underlying-redundancy proof.
3. **v3 must baseline ΛCDM against stock CAMB** — the default fork (~/camb_grut) has μ always-on
   (= the ruled-out enhancement); this is why the 2 σ₈ tests are xfail'd.

## Context
- Discipline that earned this: adversarial verification caught multiple clean over-claims; survivors
  are constraints + honest no-gos, never rescues. Hold any new "clean positive" to the same check.
- Do NOT push to GitHub except on an explicit release. python3.12 for code/tests;
  uploads/pdf_venv/bin/python3.12 for PDF builds.
- Flavor/Koide is OUTSIDE the vacuum-response scheme (hosted Yukawa input), not a gap.
- The retired v2 book/PDF (uploads/) is frozen — out of scope; v3 work is forward-only.
