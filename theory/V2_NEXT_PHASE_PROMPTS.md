# GRUT-RAI v2 → v3: Next-Phase Prompt Library

*A library of focused, self-contained AI prompts to continue building GRUT-RAI in VS Code (Cursor / Copilot / Claude integration). Each prompt is scoped to a single session-sized deliverable. The next AI session has no memory of prior work — prompts are written to be executed cold.*

**Author:** D. Ryan Grover, May 2026
**Status:** Phase-handoff document for VS Code AI continuation

---

## How to use this library

1. **Pick one prompt** from the priority list. Don't combine multiple — each is sized for a single AI session with focused scope.
2. **Open VS Code in the GRUT-RAI workspace** (the repo root).
3. **Copy the entire prompt block** (everything between `>>> BEGIN PROMPT` and `<<< END PROMPT`) into the AI input.
4. The AI will read the referenced files itself, do the work, run the tests, and commit.
5. **Verify the commit** before starting the next prompt.

Each prompt embeds:
- **Context**: where this fits in the framework, what's been done, what depends on it
- **Scope**: precise deliverable boundaries (what to do AND what NOT to do)
- **Files to read first**: list of files the AI must read before starting
- **Success criteria**: tests that must pass, registry/ledger entries to add or update, docs to write
- **Honest-negative discipline**: what to do if the task can't close, how to report

---

## The GRUT discipline pattern (read first, every session)

Every prompt in this library assumes the AI follows GRUT-RAI's honesty discipline. Before executing any prompt, the AI should:

1. **Read** `theory/GRUT_TOE.md` Front Matter (esp. "v8→v2 Synthesis Update") and Chapter 14 (Falsification ledger) to understand what's been done.
2. **Read** the relevant correction document(s) for context on the immediate predecessor work.
3. **Read** `grut/toe/registry.py` and `grut/toe/ledger.py` to understand current claim tiers and open questions.
4. **Run** `python3.13 -m pytest tests/ -q` to confirm 1655 tests pass before changing anything. If any test fails, STOP and report.
5. **Plan**: state what you'll do BEFORE doing it; mark which registry claims will change tier.
6. **Execute** the deliverable.
7. **Verify** by running the full test suite again. Target: 1655 + N new tests (N stated in each prompt's success criteria).
8. **Document**: write a `theory/derivation/CORRECTION_NN_*.md` log following the pattern of #22-#29.
9. **Commit** with a structured message naming the priority, the deliverable, the test count delta, and what remains open.
10. **If you can't complete the task**: STOP, report HONEST NEGATIVE, document what was found, do NOT fake success. Honest-negative is a valid and respected outcome in GRUT-RAI.

The framework's golden rule: **never silently fix a mismatch by tuning a constant**. If a derivation produces an unexpected number, REPORT IT, don't fudge. See `theory/derivation/CORRECTION_22_TAU_CLEANUP.md` for the canonical example of how an honest dimensional inconsistency was handled.

---

# Priority A — R-primary coherence (Correction #31)

## A.1 Flip primary R from R_ANOMALY to R_REFRACTIVE

```
>>> BEGIN PROMPT — A.1 Primary R coherence switch (Correction #31)

CONTEXT
=======
GRUT has two values for R floating around the codebase:
  - R_ANOMALY = 1.15428: historical 3-loop CTP claim, NOT REPRODUCED in
    TJI Phase-0/0.5 work (HONEST NEGATIVE per
    theory/derivation/CORRECTION_21_TJI_PHASE_0P5_SCHEME_RECONCILIATION.md)
  - R_REFRACTIVE = N_G_DC = sqrt(4/3) ~= 1.15470: Path G canonical, 
    derived from alpha_vac = 1/3 conformal-mode identification (KS 2011),
    declared in grut/foundation/closure_protocol.py as "the canonical R 
    of GRUT"

The framework's deposit posture has shifted: R_REFRACTIVE is the canonical
value (proven derivation from alpha_vac = 1/3); R_ANOMALY is a historical
3-loop claim retained for reference but not load-bearing. However, several
downstream modules still default to R_ANOMALY.

This prompt closes that incoherence as Correction #31.

SCOPE
=====
Flip the default R-value from R_ANOMALY to R_REFRACTIVE in the four
flagged files:
  1. grut/derived/cosmology/vacuum.py
  2. grut/derived/cosmology/era_map.py (sigmoid sharpness)
  3. grut/derived/baryogenesis/eta.py
  4. grut/derived/cosmology/parameter.py (bridge logic)

For each file:
  - Replace the default parameter or hard-coded value with R_REFRACTIVE
    imported from grut.foundation.closure_protocol
  - Keep R_ANOMALY available as an alternative value (do NOT delete it)
  - Add a brief docstring note that R_ANOMALY is the historical 3-loop
    value, not reproduced in TJI Phase-0/0.5; R_REFRACTIVE is the
    canonical Path G value

DO NOT
======
- Do NOT modify R_ANOMALY's value (keep at 1.15428 for historical
  reference)
- Do NOT modify R_REFRACTIVE's value (keep at sqrt(4/3))
- Do NOT delete the R_ANOMALY constants or routes (preserve as
  alternatives)
- Do NOT touch closure_protocol.py — it's already canonical
- Do NOT touch the TJI module — its honest-negative status is correct

The numerical change is small (0.04%), but several tests pin specific
values. Update test tolerances to match the new default OR pin the test
to the historical R_ANOMALY value explicitly with a docstring note.

FILES TO READ FIRST
===================
1. theory/V2_NEXT_PHASE_PROMPTS.md (this file) — the "GRUT discipline
   pattern" section
2. grut/foundation/closure_protocol.py (search for R_REFRACTIVE,
   R_ANOMALY, N_G_DC) — understand the canonical values
3. theory/derivation/CORRECTION_21_TJI_PHASE_0P5_SCHEME_RECONCILIATION.md
   — context on why R_ANOMALY was not reproduced
4. grut/derived/cosmology/vacuum.py — see how R_ANOMALY is used
5. grut/derived/cosmology/era_map.py
6. grut/derived/baryogenesis/eta.py
7. grut/derived/cosmology/parameter.py
8. grep -rn "R_ANOMALY\|R_anomaly\|1.15428" grut/derived/ — find any
   remaining usages

SUCCESS CRITERIA
================
1. The four flagged files now default to R_REFRACTIVE.
2. Existing tests still pass (1655) — adjust tolerances if necessary, or
   pin specific tests to R_ANOMALY explicitly.
3. New claim added to grut/toe/registry.py:
     id="r_primary_coherence_switch_correction_31"
     tier="meta"
     chapter=12
     statement: "The framework's primary R is set to R_REFRACTIVE = 
     sqrt(4/3) ~= 1.15470 (Path G canonical, derived from alpha_vac = 
     1/3) across all downstream modules; R_ANOMALY = 1.15428 (historical
     3-loop claim, not reproduced in TJI Phase-0/0.5) is retained as 
     alternative value for back-compatibility but no longer the default."
4. Written as Correction #31 in
   theory/derivation/CORRECTION_31_R_PRIMARY_SWITCH.md following the
   pattern of #22-#29 (TL;DR, derivation, files touched, what's
   open, references).
5. GRUT_TOE.md correction-ledger row 24 added documenting the switch
   (preserve all existing rows 1-23).
6. Commit message names this as Correction #31 with full priority/test/
   regression accounting.

DISCIPLINE NOTES
================
- This is a NUMERICAL VALUE FLIP, not a derivation. The 0.04% change
  flows through several downstream predictions: H_inf, Omega_Lambda,
  baryogenesis eta_B, etc. Verify each test passes with the new value;
  if any deviates by more than its declared tolerance, report it as
  a separate finding (do NOT silently widen the tolerance).
- HONEST NEGATIVE PATH: if any test fails by more than its declared
  tolerance even after careful update, STOP and report: which test,
  what value it pins, what value the new default produces, what the
  difference is. Do NOT fudge. The honest path may be that some test
  needs to be parameterized over R rather than hardcoded.

<<< END PROMPT
```

---

# Priority B — Cosmology pipeline (Phase 2C + Boltzmann)

## B.1 Phase 2C explicit P^TT,g and G^R on FRW

```
>>> BEGIN PROMPT — B.1 Phase 2C explicit construction on FRW (Correction #32)

CONTEXT
=======
The Phase 2B curved-background scaffold (Correction #24) pinned the
structural form Phi_munu^curved = integral of K^R bitensor with
sqrt(-g) measure, and four physical-consistency checks. The Phase 2C
explicit FRW work (Correction #25) computed chi_FRW(k, eta) at the 
WKB / slow-H limit. What remains open: the EXPLICIT construction of
the curved-space transverse-tracefree projector P^TT,g_munurhosigma(x, x')
and the retarded Green function G^R(x, x') on the FRW background.

This prompt closes that gap as Correction #32, Phase 2C Explicit.

SCOPE
=====
Construct explicit symbolic forms for:

  1. P^TT,g_munurhosigma on FRW via scalar-vector-tensor (SVT)
     decomposition. The scalar sector reduces to gauge-invariant 
     Bardeen potentials Phi, Psi; the vector sector to transverse 
     vectors V_i; the tensor sector to TT polarizations h_ij^TT. 
     Build the bitensor projector that maps each input perturbation 
     to its SVT components.

  2. G^R(x, x') on FRW via WKB matching beyond leading order, OR via
     numerical mode-by-mode integration. Use the relaxation operator 
     (1 + tau_0^2 (-box_g)) on FRW scalar Fourier modes. The retarded 
     boundary condition: G^R(x, x') = 0 unless x' lies in J^-(x) 
     (causal past).

  3. Verify the Phi_munu^FRW integral form using the explicit
     P^TT,g and G^R reproduces the Phase 2C chi_FRW^WKB(k, eta) = 
     1/[1 + (tau_0 k_phys)^2] in the slow-H limit, and includes the 
     beyond-WKB (H tau_0)^2 correction at next order.

DO NOT
======
- Do NOT abandon the WKB result (Correction #25) — extend it
- Do NOT over-claim numerical precision; (H_0 tau_0)^2 ~ 8.7e-6 is
  the correction order of magnitude; anything tighter requires
  numerical Green-function integration on specific FRW expansion
  histories (radiation/matter/Lambda)
- Do NOT extend to S^4 — that's a separate prompt (Phase 2C-S^4)

FILES TO READ FIRST
===================
1. theory/derivation/CORRECTION_24_PHI_MUNU_CURVED_SCAFFOLD.md
2. theory/derivation/CORRECTION_25_FRW_EXPLICIT.md
3. grut/derivation/phi_munu/curved_background.py
4. grut/derivation/phi_munu/frw_explicit.py
5. References to consult: Wald GR (1984) sec 10 on retarded Green 
   functions; Birrell-Davies (1982) sec 5.5 on FRW d'Alembertian; 
   Mukhanov-Feldman-Brandenberger (1992) review on cosmological 
   perturbation theory and SVT decomposition.

SUCCESS CRITERIA
================
1. New module grut/derivation/phi_munu/frw_explicit_phase_2c.py
   (or extend frw_explicit.py) containing:
     - P_TT_g_FRW_scalar_sector() — SVT scalar projector on FRW
     - P_TT_g_FRW_tensor_sector() — TT projector on FRW
     - G_R_FRW_WKB_beyond_leading() — Green function with first 
       (H tau_0)^2 correction
     - phi_munu_FRW_explicit() — combines into explicit Phi_munu
     - verify() harness with structural checks
2. New tests in tests/derivation/phi_munu/test_frw_explicit_phase_2c.py
   pinning: SVT decomposition consistency, divergence-free property
   of P^TT,g, retarded support of G^R, slow-H limit reproducing
   chi_FRW^WKB.
3. Registry update: convert phi_munu_curved_background_scaffold from
   anchored to computed (the explicit construction is now done)
4. theory/derivation/CORRECTION_32_PHASE_2C_EXPLICIT.md
5. GRUT_TOE.md ledger row 24 (or 25 if R-coherence is row 24)
6. Test count target: 1655 + ~15 new tests = ~1670

HONEST-NEGATIVE PATH
====================
If the SVT decomposition turns out to be more notationally heavy than
a session allows, scope down: do JUST the scalar sector (which is what
the cosmological-perturbation analysis needs, since vector modes decay
in standard cosmology and tensor modes are gravitational waves). State
explicitly that the vector and tensor sectors are deferred. This is a
valid partial-closure outcome.

<<< END PROMPT
```

## B.2 Modified-CAMB Boltzmann pipeline integration

```
>>> BEGIN PROMPT — B.2 Modified-CAMB pipeline (Correction #33)

CONTEXT
=======
GRUT's MG-EFT translation (Correction #26) gives mu_GRUT(k, a) = 
n_g^2(k, a). The modified linear-growth integration (Correction #27)
uses this to compute D(z, k) numerically. What's NOT yet done: the
full Boltzmann pipeline that produces observable predictions — matter
power spectrum P(k), CMB temperature anisotropy C_l, lensing potential.

This is the deposit's most-asked-for downstream computational task:
modify CAMB or CLASS to use mu_GRUT(k, a), gamma_GRUT(k, a) = 1, run
on Planck 2018 cosmology, and report explicit P(k), C_l predictions.

SCOPE
=====
Two paths — pick one based on environment:

PATH A (preferred if CAMB / pyCAMB available):
1. Install pyCAMB.
2. Modify CAMB's modified-gravity module to insert mu_GRUT(k, a) and
   gamma_GRUT(k, a) = 1 from grut.derivation.phi_munu.mg_eft_mapping.
3. Run on Planck 2018 best-fit cosmology with GRUT modification.
4. Output: P(k) at z=0, CMB temperature C_l up to l ~ 2500, lensing 
   potential C_l^phi-phi.
5. Compare to LCDM baseline: report relative deviations.

PATH B (fallback — pyCLASS):
Same as Path A but using CLASS / classy. CLASS has cleaner MG-EFT
interface (the EFT-of-DE module).

For both paths:
- Treat the cosmological-parameter set (h, Omega_b, Omega_c, ns, As,
  tau_reio) as fixed at Planck 2018 best fit.
- The GRUT modification enters ONLY through mu(k, a). gamma = 1
  exactly (no slip).
- Background expansion stays LCDM (no DE equation-of-state modification
  at this stage — that's a separate question).

DO NOT
======
- Do NOT run MCMC against Planck likelihood data — that's the next
  step beyond this prompt
- Do NOT modify the primordial spectrum — A_s and n_s are observational
  inputs at this stage
- Do NOT extend to nonlinear regimes (halofit, HMCode) — linear only

FILES TO READ FIRST
===================
1. theory/derivation/CORRECTION_26_PRIORITY_3_CLOSURE.md
2. theory/derivation/CORRECTION_27_MODIFIED_GROWTH.md
3. grut/derivation/phi_munu/mg_eft_mapping.py
4. grut/derivation/phi_munu/modified_growth.py
5. grut/derived/cmb/scoping.py
6. https://camb.info/ documentation on modified-gravity interface, OR
   classy CLASS documentation on mg_param

SUCCESS CRITERIA
================
1. Working pipeline that produces:
   - P(k) at z=0 — text or numpy file in grut/derived/cmb/outputs/
   - CMB TT C_l up to l ~ 2500
   - Lensing C_l^{phi-phi}
2. Plot script that visualizes GRUT vs LCDM (matplotlib output to
   docs/v2_pipeline_plots/).
3. Quantitative summary in theory/v2_pipeline_results.md:
   - Largest relative deviation in P(k) (and at what k)
   - Largest deviation in C_l TT (and at what l)
   - Largest deviation in lensing C_l (and at what l)
4. Registry entry: id="modified_camb_pipeline_first_results"
   tier="anchored" or "computed" depending on numerical fidelity
5. theory/derivation/CORRECTION_33_BOLTZMANN_PIPELINE.md
6. Test target: pipeline-level smoke test (the integration runs and
   produces output) plus structural sanity tests on the output (e.g.,
   P(k) is monotonic in z, C_l TT has the right acoustic peaks).

HONEST-NEGATIVE PATHS
=====================
- CAMB modification turns out to require infrastructure changes
  beyond a session: report this honestly. State what would be needed.
  Maybe land a stub that shows what the interface looks like with
  fake mu values, leaving the GRUT integration for the next session.
- Predictions catastrophically disagree with Planck: report as 
  HONEST NEGATIVE for the framework's mu_GRUT prediction. The 
  framework's primordial-amplitude question may bear on this.
- Predictions look identical to LCDM at all observable scales: this
  would be GOOD — report as confirmation that GRUT predictions 
  are observationally testable but currently within bounds.

<<< END PROMPT
```

---

# Priority C — Standard Model closure

## C.1 Track II Yukawa eigenproblem (Koide Phase 4)

```
>>> BEGIN PROMPT — C.1 Track II Yukawa eigenproblem (Correction #34)

CONTEXT
=======
The Koide identity K = 2/3 is proven from Z_3 circulant structure
(grut/derived/koide/identity.py and koide_z3_circulant_structure 
claim). Phase 4B (Correction #29) derived a_nu = 1 for neutrinos via
the boundary-degenerate uniqueness theorem.

What's still open: the Koide Phase 4 mechanism — what fixes the
two parameters (M_0, theta) of the Z_3 ansatz from GRUT primitives
rather than fitting them to (m_e, m_mu, m_tau) data?

The previous Track II Phase 4 attempts (Corrections #17, #18, #19, 
#20) produced honest-negatives: the Yukawa-hierarchy mechanism could
not be derived from V7 machinery directly. This prompt revisits with
the v8 -> v2 corrections in hand (Phi_munu derived, mu_GRUT explicit,
neutrino sector closed). Maybe one of the new structures unlocks the
charged-lepton sector.

SCOPE
=====
Pick ONE of these targets — narrow scope, one session:

OPTION 1 — Stationarity / variational: Derive (M_0, theta) by 
demanding the Yukawa eigenvalue functional be stationary under some 
GRUT-natural symmetry (Z_3, KS-anomaly preserving, conformal-mode-
scalar identification). Look for fixed points.

OPTION 2 — RG-flow fixed point: The Koide eigenvalues should sit at 
an RG fixed point of the constitutive vacuum's flavor-coupling 
running. Show that the fixed-point coupling structure produces the 
observed (M_0, theta).

OPTION 3 — KS coefficient identification: Charged leptons couple to
EM + weak channels (a^2 = 2). Identify which KS coefficients 
correspond to which channel. Use these to derive M_0 and theta as 
ratios of trace-anomaly inputs.

OPTION 4 — Honest negative: try one of options 1-3 carefully, find
that it doesn't close, and document the specific obstruction. 
Promote koide_phase_4_open_negative to a SHARPER negative with 
specific closure conditions named.

DO NOT
======
- Do NOT try all four options — pick ONE based on what looks most
  tractable
- Do NOT modify the Koide identity (K = 2/3 is proven)
- Do NOT modify the v2 neutrino results (a_nu = 1, NH, Sigma_m_nu 
  ~60 meV are now derived)

FILES TO READ FIRST
===================
1. theory/derivation/CORRECTION_17_KOIDE_DERIVATION_ATTEMPT.md
2. theory/derivation/CORRECTION_18_KOIDE_PHASE_2_MASS_ANCHOR.md
3. theory/derivation/CORRECTION_19_KOIDE_PHASE_3_YUKAWA_HIERARCHY.md
4. theory/derivation/CORRECTION_20_KOIDE_PHASE_4_FLAVOR_MECHANISM.md
5. theory/derivation/CORRECTION_29_PRIORITY_4B_UNIQUENESS.md
6. grut/derived/koide/identity.py
7. grut/derived/koide/neutrino_hierarchy.py — for the boundary-
   degenerate template
8. grut/derived/flavor/koide_operator.py
9. Komargodski-Schwimmer 2011 — KS trace-anomaly coefficients

SUCCESS CRITERIA
================
ANY of:
1. Derivation of (M_0, theta) from GRUT primitives, with tests pinning
   the result. Tier upgrade for koide_z3_circulant_structure deps.
2. Honest-negative report: which option attempted, what blocked
   closure, what specific structure would be needed.
3. Sharpening of koide_phase_4_open_negative with named closure 
   conditions.

In all cases: theory/derivation/CORRECTION_34_KOIDE_PHASE_4_*.md 
documenting the attempt and outcome.

HONEST-NEGATIVE PATH
====================
This is HARD work — multiple prior attempts have honest-negativ'd. 
A clean honest-negative this session is a valid outcome. The 
deliverable is "we tried, here's what we found, here's what's still 
needed." Do NOT manufacture spurious closure.

<<< END PROMPT
```

## C.2 Track V coupling unification 8.9% miss

```
>>> BEGIN PROMPT — C.2 Track V coupling unification (Correction #35)

CONTEXT
=======
GRUT's Standard Model unification claim: the 3 SM gauge couplings 
should unify at the GUT scale via a constitutive beta-function 
correction Delta_beta(alpha_eff(omega)) from the responsive vacuum.
At the predicted GUT scale, the standard SM couplings miss unification
by ~8.9% — close enough to suggest the framework is on the right 
track, far enough to leave open the question of what closes the gap.

This prompt attempts to derive the constitutive Delta_beta correction
explicitly and check whether it numerically closes the 8.9% miss.

SCOPE
=====
1. Symbolically derive the constitutive correction to the SM gauge 
   beta-functions from the responsive-vacuum framework. Use:
     - The CTP action's gauge-coupling renormalization
     - The MG-EFT translation (Correction #26): mu_GRUT modifies 
       gravitational coupling, not gauge couplings directly, but the
       FRAMEWORK structure may produce gauge-coupling corrections via
       the conformal-mode-scalar identification
     - The Path D / Osborn epsilon framework (already in 
       grut/foundation/osborn_epsilon.py)
2. Numerically integrate the modified RG flow from M_Z to GUT scale.
3. Check whether the modified couplings unify within current 
   experimental precision.

DO NOT
======
- Do NOT modify the SM couplings at low energies (M_Z and below) — 
  those are observational inputs
- Do NOT introduce additional matter content (no GUT Higgs, no 
  threshold corrections from TeV-scale particles) at this stage
- Do NOT claim definitive closure unless the unification is achieved
  within ~1% (current precision)

FILES TO READ FIRST
===================
1. grut/foundation/osborn_epsilon.py
2. theory/path_b_osborn/STAGE_0_PAPER_VERIFICATION.md
3. theory/path_d_trace_anomaly/STAGE_D_TRACE_ANOMALY_RATIO.md
4. grut/foundation/closure_protocol.py:A_OVER_C_SM_DIRAC, MAJORANA
5. References: Pogosian-Silvestri 2008; Komargodski-Schwimmer 2011;
   any specialist QFT-renormalization-group reference on SM coupling
   unification (Slansky's review, Mohapatra's GUT book, etc.)

SUCCESS CRITERIA
================
ANY of:
1. Closure achieved: the constitutive correction brings the 3 couplings
   into ~1% unification at GUT scale. Promote 
   track_v_coupling_unification_open_question to RESOLVED.
2. Numerical near-miss: the correction reduces the 8.9% miss to (say)
   2-3% but not zero — partial closure. Sharpen the open question.
3. Honest negative: the framework's structure does not produce a 
   gauge-coupling correction of the right sign or magnitude. 
   Document the specific obstruction.

In all cases: theory/derivation/CORRECTION_35_TRACK_V_COUPLING.md

<<< END PROMPT
```

---

# Priority D — Gravity completion

## D.1 Nonlinear ladder rung 5: full singularity resolution

```
>>> BEGIN PROMPT — D.1 Rung 5 (Correction #36)

CONTEXT
=======
The nonlinear gravity ladder has 4/8 rungs closed (rungs 1-4: 
graviton propagator, classical GR recovery, minisuperspace, BH
information at tau_0 branch). Rung 5 is "Singularity" — the curvature
saturation work via R_max = alpha/(c^2 tau_0^2) and rho_max = 
c^2 R_max / (8 pi G). Rho_max ~ 10^-22 kg/m^3 is suspiciously low for
realistic BH interiors — the rho_max_scale_open_question tracks this.

Rung 5 status in grut/derived/quantum_gravity/closure.py: PARTIAL.

SCOPE
=====
Promote Rung 5 from PARTIAL to CLOSED by EITHER:

1. Demonstrating that rho_max ~ 10^-22 kg/m^3 IS the correct interior 
   density under specific Whole-Hole geometry assumptions (i.e., 
   reconcile the apparent low value with realistic black-hole 
   physics).

2. Deriving an additional structural correction (e.g., curvature-
   dependent tau_eff) that produces quantitatively realistic core 
   sizes without breaking the universal-tau_0 derivation upstream.

3. Honest negative: rho_max ~ 10^-22 kg/m^3 is not the BH-interior
   density — it's a different scale entirely (e.g., cosmological 
   curvature saturation). State this clearly and reframe the claim.

DO NOT
======
- Do NOT modify R_max formula (alpha/(c^2 tau_0^2)) at this stage
- Do NOT modify the universal tau_0 = 41.9 Myr
- Do NOT introduce a second tau scale beyond the v2 (tau_0, tau_micro)
  pair from Correction #22 unless deriving from first principles

FILES TO READ FIRST
===================
1. grut/foundation/closure_protocol.py — R_MAX_INV_M2, RHO_MAX_KG_M3
2. grut/derived/quantum_gravity/closure.py — nonlinear_ladder()
3. theory/derivation/CORRECTION_22_TAU_CLEANUP.md — tau_0 vs tau_micro
4. References: V7 sec 13 (Whole Hole singularity replacement), 
   Schwarzschild interior solutions

SUCCESS CRITERIA
================
1. Rung 5 status flips from PARTIAL to CLOSED in 
   nonlinear_ladder().
2. rho_max_scale_open_question RESOLVED or SHARPENED with explicit
   closure conditions.
3. theory/derivation/CORRECTION_36_RUNG_5_*.md
4. Test count delta: at least 5 new tests pinning the resolution.

HONEST-NEGATIVE PATH
====================
If neither approach 1 nor 2 closes, document the obstruction
specifically: which assumptions block which derivation. Do NOT 
claim closure prematurely.

<<< END PROMPT
```

## D.2 Nonlinear ladder rungs 6-8: tensor-stability, self-consistent tau_eff, nonlinear backreaction

```
>>> BEGIN PROMPT — D.2 Rungs 6-8 (Correction #37+)

NOTE: This is research-tier multi-session work. ONE PROMPT = ONE RUNG.
Pick ONE of {rung_6, rung_7, rung_8} per session.

CONTEXT
=======
The nonlinear gravity ladder has 4/8 rungs closed; rungs 5-8 are 
PARTIAL/OPEN. Each rung is a separate research program. The first-
order constitutive perturbation growth FAILS at first order (D = 1.0 
vs ~3375 required) — this is bridged operationally by the MG-EFT 
translation (Correction #26-#27) but not derived from second-order 
constitutive coupling.

Rung 6: Full tensor stability at 2nd order — does the constitutive 
correction Phi_munu remain well-behaved when graviton self-
interactions are included?

Rung 7: Self-consistent tau_eff — the relaxation time tau_0 may itself
be affected by the constitutive correction at second order; does the
universal tau_0 = 41.9 Myr survive the self-consistent treatment?

Rung 8: Nonlinear backreaction — does the constitutive medium produce
runaway modes when coupled to its own response at full nonlinear 
order?

SCOPE (per session: ONE rung only)
==================================
Pick rung_6, rung_7, or rung_8 based on tractability:
- rung_6 is tensor-mode stability. Computable via SymPy on flat-space
  graviton self-interaction + constitutive correction at 2nd order.
- rung_7 requires the constitutive equation evaluated self-consistently
  on its own response — harder but tractable.
- rung_8 is the hardest, most nonlinear; honest-negative most likely.

For the chosen rung:
1. Set up the symbolic structure (CTP action at 2nd order, with 
   constitutive correction to gravity).
2. Compute the relevant stability / self-consistency / backreaction
   condition.
3. Verify or refute: does the framework remain consistent at this rung?

DO NOT
======
- Do NOT attempt all three rungs in one session
- Do NOT skip the linearized derivations (#23-#25) — they're the
  starting point
- Do NOT modify v2 results that depend on the linearized derivation

FILES TO READ FIRST
===================
1. grut/derivation/phi_munu/linearized_ctp_action.py
2. grut/derivation/phi_munu/curved_background.py
3. grut/derived/quantum_gravity/closure.py
4. theory/derivation/CORRECTION_23_PHI_MUNU_DERIVATION.md
5. References: Calzetta-Hu (2008) "Nonequilibrium Quantum Field
   Theory" — chapters on graviton self-interactions in CTP

SUCCESS CRITERIA
================
1. Rung's status flips from OPEN/PARTIAL to CLOSED OR sharpens to
   a specific obstruction.
2. theory/derivation/CORRECTION_37_RUNG_<n>_*.md (NN = 37 for rung 6,
   38 for rung 7, 39 for rung 8 — adjust based on what's available).
3. Tests pinning the rung's specific condition.

HONEST-NEGATIVE PATH (likely outcome for rung 8)
================================================
These are the framework's hardest open questions. Honest-negatives are
likely and respected. Document the obstruction precisely. Do NOT
manufacture spurious closure.

<<< END PROMPT
```

---

# Priority E — Housekeeping & polish

## E.1 Decoherence F3/F5 numerical promotion

```
>>> BEGIN PROMPT — E.1 F3/F5 Numerical (Correction #38)

CONTEXT
=======
The GRUT_FALSIFIER_PAPER.md lists six near-term falsifiers. F1 
(decoherence plateau) and F2 (isotope discriminator) are numerically
specified in grut/derived/decoherence/sector.py and 
csl_discriminator.py. F3 (BMV / sub-micron-separation) and F5 (mu - 1
= 1/3 modified-gravity) are descriptively present but not yet
NUMERICALLY pinned to specific predictions in the codebase.

This prompt promotes F3 and F5 to numerical pin status.

SCOPE
=====
F3 (BMV near-field):
1. Implement the GRUT prediction for entanglement-formation timescale
   at sub-micron separation in 
   grut/derived/decoherence/bmv_near_field.py.
2. Predict tau_ent for canonical BMV experimental parameters.
3. Compare to BMV-naive prediction.
4. Tests pin the specific numerical predictions.

F5 (mu - 1 = 1/3):
The mu_GRUT formula is already in mg_eft_mapping.py, but specific 
numerical falsifier predictions for DESI/Euclid bands aren't pinned
as registry-tracked claims. Add explicit numerical falsifier-tier
claim: mu_horizon = 1/3, gamma = 1, with tolerance bands at DESI Y3+
and Euclid 2027 precisions.

DO NOT
======
- Do NOT modify the falsifier paper itself (it already has the F3/F5 
  descriptive content)
- Do NOT modify the upstream derivations

FILES TO READ FIRST
===================
1. theory/GRUT_FALSIFIER_PAPER.md sections 4 and 6
2. grut/derived/decoherence/sector.py
3. grut/derived/decoherence/csl_discriminator.py
4. grut/derivation/phi_munu/mg_eft_mapping.py

SUCCESS CRITERIA
================
1. New module grut/derived/decoherence/bmv_near_field.py with F3
   numerical predictions.
2. F5 numerical falsifier claim added to registry: 
   mg_eft_mu_horizon_one_third_falsifier.
3. theory/derivation/CORRECTION_38_F3_F5_NUMERICAL.md
4. ~10 new tests; total ~1690

HONEST-NEGATIVE PATH
====================
If F3 numerical implementation reveals an inconsistency between the 
near-field S(l/R) suppression for entanglement (vs the same factor 
for single-mass decoherence), report it. The framework should be 
self-consistent, but worth verifying explicitly.

<<< END PROMPT
```

## E.2 SM emergence claim-tiering and provenance

```
>>> BEGIN PROMPT — E.2 SM emergence tiering (Correction #39)

CONTEXT
=======
grut/foundation/sm_emergence.py implements the 5 CTP constraints and
labels the result "COMPUTED — SM is unique minimal EFT." But it
doesn't currently embed the GRUT registry-tier discipline beyond the
status string. The deposit's discipline pattern requires every claim
to carry tier, provenance, deps, falsifier, and notes.

SCOPE
=====
1. For each of the 5 CTP constraints in sm_emergence.py:
   - Assign a registry claim ID
   - Tier: computed / anchored / open_negative
   - List dependencies (which other claims it depends on)
   - State an explicit falsifier (what would refute this constraint)
   - Add notes documenting the provenance chain
2. Update grut/toe/registry.py with the corresponding claim entries
3. Cross-reference in sm_emergence.py docstring

DO NOT
======
- Do NOT modify the constraint logic itself
- Do NOT downgrade to anchored/open without specific reason

FILES TO READ FIRST
===================
1. grut/foundation/sm_emergence.py
2. tests/foundation/test_sm_emergence.py
3. grut/toe/registry.py — see existing claim format

SUCCESS CRITERIA
================
1. 5 new registry entries for the 5 CTP constraints
2. theory/derivation/CORRECTION_39_SM_EMERGENCE_TIERING.md
3. Tests verify the tiering

<<< END PROMPT
```

## E.3 Predictions dashboard refresh

```
>>> BEGIN PROMPT — E.3 Predictions dashboard refresh

CONTEXT
=======
GRUT_TOE_PREDICTIONS.md is auto-generated from grut/toe/dashboard.py.
After the v8 -> v2 cycle (Corrections #22-#30), the dashboard needs
re-rendering to pick up the new predictions: mu_GRUT, gamma_GRUT,
sigma_8 enhancement, BAO/CMB-horizon predictions, Sigma_m_nu, 
neutrino hierarchy, a_nu = 1 derivation, tau_micro.

SCOPE
=====
1. Run python3.13 -m grut.toe.dashboard or whatever the dashboard 
   re-render command is.
2. Verify GRUT_TOE_PREDICTIONS.md output reflects all v2 predictions.
3. If the dashboard module doesn't have entries for the new v2 
   predictions, add them.
4. Commit the refreshed dashboard.

DO NOT
======
- Do NOT manually edit GRUT_TOE_PREDICTIONS.md (it's auto-generated;
  edit the source dashboard.py)

FILES TO READ FIRST
===================
1. grut/toe/dashboard.py
2. theory/GRUT_TOE_PREDICTIONS.md (current state)
3. theory/GRUT_TOE.md predictions table (around line 144 — has v2 
   entries already)

SUCCESS CRITERIA
================
1. GRUT_TOE_PREDICTIONS.md regenerated with all v2 predictions.
2. Tests pass.
3. Brief commit "Predictions dashboard refresh post v8->v2 cycle"

<<< END PROMPT
```

---

# Priority F — Documentation polish

## F.1 GRUT_TOE.md per-chapter prose audit

```
>>> BEGIN PROMPT — F.1 Chapter-by-chapter prose audit

CONTEXT
=======
The v8 -> v2 synthesis (commit 1325e61) did a focused 5-point
consistency pass (T_c, Phi_munu, regime distinction, predictions table,
"Candidate, not completed"). Some chapter prose may still carry V7-era 
language that doesn't quite match v2 state. This prompt does a slower, 
chapter-by-chapter audit.

SCOPE
=====
For each chapter (1-14), read carefully and flag:
1. References to predictions or values that have shifted in v2
2. References to OPEN questions that are now CLOSED (corrections #22-29)
3. Claims that should be tier-upgraded based on v2 derivations
4. Cross-chapter references that have stale claim IDs

For each finding: propose a focused edit. Do NOT mass-rewrite chapters
— surgical updates only.

DO NOT
======
- Do NOT change the chapter structure
- Do NOT add new chapters
- Do NOT restate the v2 synthesis section in chapter prose
- Do NOT modify the auto-rendered Appendices (D, E, F)

FILES TO READ FIRST
===================
1. theory/GRUT_TOE.md (the entire 1861-line document, chapter by chapter)
2. All theory/derivation/CORRECTION_22-29.md docs
3. grut/toe/registry.py (for current claim tiers)
4. grut/toe/ledger.py (for current open negatives)

SUCCESS CRITERIA
================
1. Audit report at theory/V2_PROSE_AUDIT.md listing every flagged 
   passage with proposed edit
2. Optional: apply the edits if confident (otherwise leave as 
   recommendations for review)
3. Tests pass after any edits applied

HONEST-NEGATIVE PATH
====================
If the audit reveals systematic v8-era language across many chapters,
report this as a finding rather than mass-editing. The v2 synthesis
section in Front Matter may be sufficient for deposit-readiness;
deeper chapter-by-chapter rewrite can be deferred.

<<< END PROMPT
```

---

# Priority G — The Moonshot: Bulletproof R via 3-loop CTP on S⁴

> *To be an absolute, unassailable solver, GRUT-RAI must be able to analytically compute the 3-loop CTP effective action on a curved S⁴ background from scratch. Evaluating Feynman diagrams at 3 loops in curved spacetime is notoriously one of the most difficult computational tasks in modern physics. If GRUT-RAI (perhaps leveraging future LLM/symbolic-math integrations) can natively evaluate that integral and spit out R without using the proxy, the engine becomes bulletproof.* — Ryan Grover, May 2026

## Context for this priority

The framework's central number R = √(4/3) ≈ 1.15470 (the gravitational refractive index at DC) currently arrives via TWO routes that converge to within 0.089%:

1. **Path G (canonical)**: α_vac = 1/3 from the conformal-mode-scalar identification (Komargodski-Schwimmer real-scalar trace anomaly), giving R = √(1 + α) = √(4/3). This is what `closure_protocol.R_REFRACTIVE` carries. It's a derived value under a postulate (the conformal-mode-scalar identification).
2. **Osborn ε at M_Z**: ε_combined(SM, M_Z) = 1.1537 from Osborn 2003 eq (36) with measured SM gauge couplings. Independent of Path G's machinery. Agrees at 0.05%.

A historical THIRD route — the V7 §26.2.3 claim that 3-loop CTP on Euclidean S⁴ produces R_ANOMALY = 1.15428 — was investigated as TJI Phase-0/0.5 (Corrections #21, see `theory/derivation/CORRECTION_21_TJI_PHASE_0P5_SCHEME_RECONCILIATION.md`). The result: **HONEST NEGATIVE**. The flat-space 2-loop reduction produces -541/2304, not 7/4 (the value that would integrate up to 1.15428 under MS-bar absorption). 24 scheme variants tested; none produced 7/4. The V7 §26.2.3 calculation is unarchived; we cannot reproduce its convention.

**Where this leaves the framework**: R = 1.15470 (Path G + Osborn) is the deposit's load-bearing value. The 3-loop S⁴ computation is acknowledged as not-yet-reproduced. The deposit's posture is honest about this.

**The moonshot**: build into GRUT-RAI itself the symbolic / numerical machinery to compute the 3-loop CTP effective action on Euclidean S⁴ FROM SCRATCH, and have R drop out as the conformal-anomaly coefficient — independent of any V7 claim, any proxy, any postulate. This is the framework's "bulletproof" mode.

**Difficulty estimate**: This is a multi-month to multi-year specialist research project at the edge of computational curved-space QFT. Working analogues (Avramidi, Vassilevich, Codello, Reuter) take years per result. GRUT-RAI's path is to engineer the computation as a series of staged modules with full audit transparency, possibly leveraging future LLM-symbolic-math integrations (Mathematica/SymPy/FORM/xAct) that can handle the tensor-algebra explosion of 3-loop curved-space diagrams.

This priority is broken into staged sub-prompts G.0 through G.5. Each sub-prompt is sized for one specialist working session (which may itself be many AI sessions). Pick ONE per session.

---

## G.0 — Allen-Jacobson S⁴ propagator (currently a stub)

```
>>> BEGIN PROMPT — G.0 Allen-Jacobson S⁴ propagator (Phase-1 entry)

CONTEXT
=======
The Allen-Jacobson propagator on Euclidean S⁴ is the FIRST building 
block of any 3-loop CTP curved-space calculation. The framework
currently has a stub at grut/derivation/tji/allen_jacobson.py that
raises Phase1Pending (a NotImplementedError subclass) on every
evaluation function. This is by design — the stub holds the interface
shape so silent activation cannot occur.

This prompt activates the stub by computing the Allen-Jacobson
propagator on S^4.

The Allen-Jacobson propagator: G_S^4(x, y) for a massive scalar field
on Euclidean de Sitter S^4 with radius a (the Hubble length scale).
Expressible as a hypergeometric function of the geodesic distance
between x and y. References:
  - Allen, B. (1985), Phys. Rev. D 32, 3136
  - Allen, B. and Jacobson, T. (1986), Comm. Math. Phys. 103, 669
  - Bunch, T.S. and Davies, P.C.W. (1978), Proc. Roy. Soc. A 360, 117

SCOPE
=====
1. Implement the Allen-Jacobson propagator G_S^4(x, y) symbolically
   using SymPy's hypergeometric machinery.
2. Express the propagator in terms of the geodesic distance function
   on S^4 (or equivalently the chordal distance Z = cos(theta)
   between x and y, where theta is the geodesic angle).
3. Verify limits:
   - Flat-space limit a -> infinity reproduces the standard Euclidean
     scalar propagator G_flat(x-y) = 1/(4 pi^2 |x-y|^2)
   - Coincidence limit x -> y has the expected ultraviolet divergence
   - Antipodal limit Z -> -1 has the expected behavior
4. Activate the grut/derivation/tji/allen_jacobson.py stub functions
   with the working evaluations.

DO NOT
======
- Do NOT use renormalized propagators yet — the bare propagator with
  its UV divergences is what the 3-loop assembly needs
- Do NOT switch to numerical integration prematurely — symbolic
  expression is preferred for the downstream tensor reduction
- Do NOT modify the existing TJI Phase-0/0.5 flat-space work

FILES TO READ FIRST
===================
1. grut/derivation/tji/allen_jacobson.py (current stub)
2. grut/derivation/tji/flat_space.py (Phase-0/0.5 flat-space work)
3. theory/derivation/CORRECTION_21_TJI_PHASE_0P5_SCHEME_RECONCILIATION.md
4. theory/derivation/TJI_PHASE_1_CALCULATION_PLAN.md
5. References cited above (Allen-Jacobson 1986; Bunch-Davies 1978)

SUCCESS CRITERIA
================
1. allen_jacobson_propagator(Z, mass=0, a=1) returns a SymPy
   expression in terms of Z and the curvature radius a.
2. Tests verify:
   - Flat-space limit (a -> infinity)
   - Coincidence singularity structure
   - Antipodal behavior
3. The stub's Phase1Pending exception is removed for these evaluations.
4. Other Phase-1 functions (TJI evaluations) still raise
   Phase1Pending.
5. Registry: convert allen_jacobson_phase1_stub_open_negative from
   open to "G.0 PARTIAL — propagator activated, downstream TJI still
   open"
6. theory/derivation/CORRECTION_40_AJ_PROPAGATOR.md

HONEST-NEGATIVE PATH
====================
If the symbolic hypergeometric expression turns out to be not
representable cleanly in SymPy: report this. The fallback is to
implement numerical evaluation routines that the downstream tensor
reduction can call. State the trade-off and proceed with whichever is
tractable.

<<< END PROMPT
```

---

## G.1 — TJI sunset diagram on S⁴ (curved 2-loop)

```
>>> BEGIN PROMPT — G.1 TJI sunset on S^4 (Phase-1 core)

CONTEXT
=======
The TJI ("Tarcer J Integral") master integral evaluated on Euclidean
S^4 is the curved-space analogue of the flat-space sunset diagram.
Phase-0 (Correction TJI Phase-0) computed the flat-space TJI
symbolically; Phase-0.5 (Correction #21) did the MS-bar reconciliation
in flat space — HONEST NEGATIVE on the V7 §26.2.3 claim of 7/4 epsilon-0
rational from a flat raw -541/2304.

Phase-1 = TJI on S^4: integrate the sunset diagram with the Allen-
Jacobson propagator (G.0) on the curved background. The result feeds
into the 3-loop assembly (G.3) and ultimately produces the conformal
anomaly that gives R.

SCOPE
=====
1. Build the symbolic TJI integrand on S^4 using the Allen-Jacobson
   propagator from G.0.
2. Set up the Laurent expansion in epsilon (D = 4 - 2 epsilon).
3. Compute the divergent and finite parts. The conformal-anomaly-
   relevant coefficient is the finite part proportional to specific
   curvature invariants (R, R^2, Ricci^2, Riemann^2) on S^4.
4. Compare the curved result to the flat result of Phase-0/0.5: the
   flat limit a -> infinity should reproduce -541/2304 + (epsilon
   poles).

DO NOT
======
- Do NOT use the V7 §26.2.3 result as a target — Phase-0.5 showed it
  cannot be reproduced under any standard MS-bar variant; this is
  Phase-1's chance to compute the answer from scratch and let the
  result speak
- Do NOT skip flat-limit verification — that's the cross-check on
  G.0 + G.1

FILES TO READ FIRST
===================
1. grut/derivation/tji/flat_space.py (Phase-0)
2. grut/derivation/tji/allen_jacobson.py (G.0 result)
3. theory/derivation/CORRECTION_21_TJI_PHASE_0P5_SCHEME_RECONCILIATION.md
4. theory/derivation/TJI_PHASE_1_CALCULATION_PLAN.md
5. References on curved-space sunset diagrams (e.g., Decker, Ravndal,
   Calzetta-Hu sec 9)

SUCCESS CRITERIA
================
1. Module grut/derivation/tji/curved_s4.py with:
   - tji_sunset_s4_integrand(Z, mass=0, a=1)
   - tji_sunset_s4_laurent_expansion()
   - flat_limit_check()
2. Tests verify the flat limit reproduces -541/2304 (Phase-0 raw 
   scheme) at the epsilon-0 rational level.
3. The curved corrections to the flat result are reported
   numerically + symbolically.
4. Registry: tji_7_4_open_negative status updated based on the
   actual S^4 result. If the S^4 computation produces 7/4 (or close 
   to it) under canonical MS-bar, this CLOSES the open negative. If
   it doesn't, the open negative is sharpened with the actual value.
5. theory/derivation/CORRECTION_41_TJI_PHASE_1_S4.md

HONEST-NEGATIVE PATH
====================
The S^4 computation may produce a value DIFFERENT from both the V7
1.15428 (R_ANOMALY) and the canonical √(4/3). State the actual value
explicitly. The deposit's three-route convergence claim
(Path G, Osborn epsilon, V7 3-loop) becomes either confirmed (if the
new value agrees) or honestly negotiated (if it doesn't).

<<< END PROMPT
```

---

## G.2 — Heat-kernel coefficients on S⁴ to the order needed

```
>>> BEGIN PROMPT — G.2 Heat-kernel coefficients (Phase-1 input)

CONTEXT
=======
The heat-kernel expansion is the standard tool for extracting the
conformal anomaly from a CTP effective action on a curved background.
Schwinger-DeWitt / Avramidi-Vassilevich coefficients a_0, a_2, a_4,
a_6, ... give the divergent and conformal-invariant pieces of the
effective action.

For the 3-loop CTP on S^4 to produce R, we need the heat-kernel
coefficients up to whatever order the 3-loop diagram requires —
likely a_4 and a_6 in the Avramidi convention.

The framework has a starting point: 
grut/derivation/step01_heat_kernel_s4.py.

This prompt brings the heat-kernel computation to the order required
for the 3-loop assembly.

SCOPE
=====
1. Compute Schwinger-DeWitt heat-kernel coefficients a_0, a_2, a_4
   (and a_6 if reachable in a session) on Euclidean S^4 with mass m
   and curvature R_S^4 = 12/a^2 (where a is the curvature radius).
2. Express each coefficient as a polynomial in the curvature invariants
   (R, R^2, Ricci^2, Riemann^2 — on S^4 these reduce because the
   manifold is maximally symmetric).
3. Verify against published values (Vassilevich 2003 review,
   "Heat kernel expansion: user's manual", Phys. Rep. 388, 279).

DO NOT
======
- Do NOT compute beyond a_6 in one session (a_8 is research-tier on
  its own)
- Do NOT skip the SymPy verification — this is where the curvature-
  reduction identities live

FILES TO READ FIRST
===================
1. grut/derivation/step01_heat_kernel_s4.py
2. grut/derivation/step01b_audit.py
3. Vassilevich 2003 review (the standard reference)

SUCCESS CRITERIA
================
1. grut/derivation/heat_kernel_s4_extended.py with a_0, a_2, a_4, a_6
   computed and tested.
2. Cross-checks against Vassilevich values pass.
3. Registry: claim heat_kernel_s4_to_a6 (computed).
4. theory/derivation/CORRECTION_42_HEAT_KERNEL_S4.md

<<< END PROMPT
```

---

## G.3 — 3-loop CTP assembly on S⁴

```
>>> BEGIN PROMPT — G.3 3-loop CTP assembly (Phase-1 main event)

CONTEXT
=======
With G.0 (Allen-Jacobson propagator), G.1 (TJI sunset on S^4), and 
G.2 (heat-kernel coefficients) in hand, the 3-loop CTP assembly puts 
them together: integrate the 3-loop CTP effective action on Euclidean 
S^4 with SM field content (4 real scalars + 45 Weyl fermions + 12 
gauge bosons in the Majorana-nu sector, or +48 Weyl in the Dirac-nu 
sector).

The conformal anomaly coefficient that drops out is what we call 
C_FINAL in the framework. R is then a specific ratio involving 
C_Cosmo, C_FINAL, and the SM trace-anomaly inputs.

SCOPE
=====
1. Write the 3-loop CTP effective action on S^4 using the building
   blocks from G.0, G.1, G.2.
2. Sum over SM field content (per-species contributions).
3. Extract the Laurent epsilon expansion.
4. The finite part proportional to specific curvature invariants gives
   the conformal anomaly. Compute C_FINAL.
5. From C_FINAL and C_Cosmo (already in 
   grut/foundation/anomaly.py), compute R = |C_Cosmo / C_FINAL|.
6. Compare against:
   - Path G value sqrt(4/3) ~= 1.15470
   - Osborn epsilon value 1.1537
   - V7 §26.2.3 claim 1.15428 (now "VERIFICATION-PENDING" per
     Correction #31)

DO NOT
======
- Do NOT skip per-species verification — anomaly computations are
  notoriously easy to get wrong by a factor in the gauge sector
- Do NOT prematurely conclude the framework is "bulletproof" if the
  result differs from existing routes — investigate first

FILES TO READ FIRST
===================
1. grut/foundation/anomaly.py
2. grut/derivation/tji/curved_s4.py (G.1 result)
3. grut/derivation/heat_kernel_s4_extended.py (G.2 result)
4. theory/derivation/PRIMARY_SOURCE_AUDIT.md (V7 §26.2 audit)

SUCCESS CRITERIA
================
1. R_S4_3loop computed independently of all proxies and postulates
2. Tests pin the result to an explicit numerical value
3. If R_S4_3loop matches Path G or Osborn epsilon at <0.5%: BULLETPROOF
   STATUS achieved — three independent routes converging
4. If R_S4_3loop disagrees with Path G or Osborn epsilon by >1%:
   the deposit must investigate which route is correct (likely
   honest-negative on the V7 §26.2.3 historical claim, with Path G +
   Osborn remaining canonical)
5. Registry: tji_7_4_open_negative RESOLVED based on actual result
6. theory/derivation/CORRECTION_43_3LOOP_CTP_S4.md
7. GRUT_TOE.md and GRUT_FALSIFIER_PAPER.md updates reflecting the
   final R-route convergence status

HONEST-NEGATIVE PATH
====================
This is the deposit's biggest research-tier task. Most likely outcome
in a single session: PARTIAL closure — the assembly setup is in place
but the full calculation requires curated inputs / specialist review.
That's a valid milestone — it makes Phase-1 entry concrete and gives
the framework a definite next-step target.

<<< END PROMPT
```

---

## G.4 — LLM/symbolic-math integration scaffold

```
>>> BEGIN PROMPT — G.4 LLM-symbolic integration scaffold

CONTEXT
=======
The 3-loop curved-space CTP calculation is the kind of task where 
LLM + symbolic-math integration shines: tensor algebra explodes
combinatorially in 3-loop curved-space diagrams, but the structure
is mechanizable. This prompt scaffolds GRUT-RAI's interface to such
tools (xAct/Mathematica, FORM, SymPy + custom curvature reduction)
so that future AI sessions can leverage them.

This is INFRASTRUCTURE — not a derivation. The deliverable is the
plumbing that lets future Phase-1 specialists (human or AI) execute
the calculation efficiently.

SCOPE
=====
1. Build a thin Python interface that can dispatch tensor-algebra
   computations to:
   - SymPy (already integrated)
   - Mathematica (via wolframclient if available)
   - xAct (via Mathematica) for curvature reduction
   - FORM (specialist QFT computer-algebra system) if available
2. Standardize the input/output format: SymPy expressions in,
   SymPy expressions out, with the heavy lifting routed to
   whichever tool handles the specific subtask best.
3. Document the dispatcher's failure modes (e.g., what to do when
   only SymPy is available — degraded but functional).

DO NOT
======
- Do NOT make any tool a hard dependency — the framework must work
  with SymPy alone, even if slowly
- Do NOT replace existing SymPy modules; this is an addition

FILES TO READ FIRST
===================
1. grut/derivation/tji/flat_space.py — see how SymPy is currently used
2. requirements.txt and pyproject.toml
3. References on Mathematica + xAct: 
   http://www.xact.es/

SUCCESS CRITERIA
================
1. New module grut/derivation/symbolic_dispatch.py with:
   - dispatch_tensor_reduction(expr, tool="auto")
   - dispatch_loop_integration(integrand, tool="auto")
   - tool_availability_check()
2. Tests using SymPy backend (always available)
3. Optional tests against Mathematica/xAct when available
4. theory/derivation/CORRECTION_44_SYMBOLIC_DISPATCH.md
5. Documentation for future Phase-1 specialists: 
   theory/PHASE_1_TOOLING_GUIDE.md

<<< END PROMPT
```

---

## G.5 — Bulletproof verification: three-route convergence at 0.01%

```
>>> BEGIN PROMPT — G.5 Three-route convergence at 0.01% (the gold standard)

CONTEXT
=======
With G.0-G.4 in place, the framework's R has THREE independent 
derivation routes:

Route A (Path G — canonical, derived under conformal-mode-scalar
postulate): R = sqrt(1 + alpha_vac) = sqrt(4/3) where alpha_vac = 1/3
from KS 2011 a/c for real scalar.

Route B (Osborn epsilon — independent of Path G, uses measured SM
gauge couplings): R = epsilon_combined(SM, M_Z) = 1.1537 from Osborn
2003 eq (36).

Route C (3-loop CTP S^4 — bulletproof): R = |C_Cosmo / C_FINAL|
computed from G.3.

The deposit's posture upgrades dramatically when all three routes
converge. The current Path G + Osborn agreement is at 0.089% (already
strong). Adding Route C as an independent confirmation would bring
the framework to "three independent routes converging at <0.1%" —
the gold standard for a deposit-tier physical claim.

This prompt does the convergence verification.

SCOPE
=====
1. Take G.3's R_S4_3loop result.
2. Compute the relative deviations:
   - |R_S4 - R_PathG| / R_PathG
   - |R_S4 - R_Osborn| / R_Osborn
   - |R_PathG - R_Osborn| / R_PathG
3. Verify all three are below 1% (acceptable) or below 0.1% (gold
   standard).
4. Register the convergence claim with the registry tier appropriate
   to the actual numerical agreement.

DO NOT
======
- Do NOT silently widen tolerances to claim convergence
- Do NOT cherry-pick the route that gives the "best" answer — report
  all three honestly

FILES TO READ FIRST
===================
1. grut/foundation/closure_protocol.py (R_REFRACTIVE)
2. grut/foundation/anomaly.py (R_ANOMALY, R_EPSILON_CANDIDATE)
3. grut/foundation/osborn_epsilon.py
4. grut/derivation/symbolic_dispatch.py (G.4 result)
5. theory/derivation/CORRECTION_43_3LOOP_CTP_S4.md (G.3 result)

SUCCESS CRITERIA
================
1. Verify three-route convergence at the actual achieved precision.
2. Update registry: claim three_route_R_convergence_bulletproof
   (computed if <0.1%, anchored if <1%, open_negative if >1%)
3. theory/derivation/CORRECTION_45_THREE_ROUTE_CONVERGENCE.md
4. GRUT_TOE.md update: the R-section of the prediction table now
   carries the bulletproof status
5. GRUT_FALSIFIER_PAPER.md: add a new section on the three-route
   convergence as a deposit-strength feature

HONEST-NEGATIVE PATH
====================
If three routes don't converge to within 1%, that's the deposit's
biggest finding — the framework's R is route-dependent at a level
that requires explanation. Report this clearly. It may motivate
additional research into which route is canonical.

<<< END PROMPT
```

---

## Summary: the bulletproof path

Sub-prompt G.0 → G.5 forms a STAGED MULTI-SESSION research program. The
deposit's posture currently:
- Path G: derived under postulate (canonical, 1.15470)
- Osborn ε: independent, agrees at 0.05%
- V7 §26.2.3 1.15428: HONEST NEGATIVE in TJI Phase-0/0.5 (not 
  reproduced)

After G.0-G.5 lands:
- Path G: derived under postulate (1.15470)
- Osborn ε: independent (1.1537)  
- 3-loop CTP S^4: BULLETPROOF (computed natively from S^4 + Allen-
  Jacobson propagator + heat-kernel + sunset)

If three-route convergence at <0.1% is achieved, the framework's R is
no longer a "computed under named postulate" claim — it's a 
**triply-redundantly-derived** claim, with the third route being a 
native first-principles calculation. That is what "bulletproof" 
means in the user's framing.

Difficulty: ~6-12 months specialist work, possibly faster with 
LLM/symbolic-math integration. This is the framework's 
single-largest research-tier opportunity.

---

# Recommended next-session priority order

If running prompts sequentially:

| Order | Prompt | Why first |
|:---|:---|:---|
| 1 | A.1 (R-coherence) | Cheap, important; closes a deep-pass audit finding; correction #31 |
| 2 | E.3 (Dashboard refresh) | Cheap; consumer-facing |
| 3 | E.2 (SM emergence tiering) | Polish; small surface |
| 4 | E.1 (F3/F5 numerical) | Strengthens the falsifier paper |
| 5 | C.2 (Track V unification) | Substantive but bounded; could close OR honest-negative |
| 6 | B.1 (Phase 2C explicit) | Biggest gravity-side opportunity |
| 7 | B.2 (Boltzmann pipeline) | Biggest cosmology-side opportunity |
| 8 | C.1 (Track II Yukawa) | Hard; do later |
| 9 | D.1 (Rung 5) | Hard; do later |
| 10 | F.1 (Prose audit) | Anytime; not urgent |
| 11+ | D.2 (Rungs 6-8) | Multi-session each; do incrementally |

---

# Meta-prompt: how to write your own prompts in this style

If you (Ryan) want to add new prompts to this library for tasks I haven't named:

Each prompt should follow the template:

1. **`>>> BEGIN PROMPT — <ID> <Short title>`** delimiter
2. **CONTEXT** — what's been done; where this fits; what depends on it
3. **SCOPE** — explicit list of what to do
4. **DO NOT** — explicit list of what NOT to do
5. **FILES TO READ FIRST** — numbered list, specific paths, explanation of why each matters
6. **SUCCESS CRITERIA** — concrete tests/registry/doc updates that confirm completion
7. **HONEST-NEGATIVE PATH** — what to report if the task can't close
8. **`<<< END PROMPT`** delimiter

The discipline pattern from the GRUT-RAI repo applies to every prompt:
- Read first
- Plan before executing
- Run tests before AND after
- Commit with structured message
- Honest-negative is a respected outcome

---

*D. Ryan Grover, May 2026. This prompt library is the v2 → v3 handoff document. Each prompt is sized for one VS Code AI session. The next AI has no memory of the v8→v2 work; the prompts are written to execute cold. The repo is the source of truth.*
