# CLASS_C_CONTAMINATION_AUDIT — emitted, never hand-typed

*Generated 2026-08-22 22:49 by `provenance/class_c_contamination_audit.py` (Phase 0, owner brief 2026-08-21). Verdict: **CLEAN**.*

## What was searched

Active surface: `CLASS_C_DISPATCH_SPEC.md`, `RUNG3_SPECTRAL_MEASURE_SPEC.md`, `CLASS_C_DISPATCH_DECISIONS.md`, `CLASS_C_MANIFEST.json`; code globs `calc/class_c*.py`, `provenance/class_c*.py`; prereg glob `provenance/prereg/*CLASS_C*`.
Historical surface (inert unless promoted): `RUNG3_KEYSTONE_MAP.md`, `RUNG3_BRIDGE_SCOPE.md`, `DISPATCH_ONE_PAGE.md`, `SPECIALIST_BRIEF_rung3_spine.md`, `calc/worldline_reduction.py`, `calc/tt_worldline_spectrum.py`, `calc/RESULTS_worldline_reduction.md`, `calc/RESULTS_tt_worldline.md`.

Forbidden-pattern set: TAU0_TARGET, MYR_TARGET, S3_EXPONENT, J_OMEGA3, SINGLE_POLE_ANSATZ, PREFERRED_OUTCOME_LANGUAGE, HARDCODED_REGULATOR_DEFAULT, HARDCODED_EPOCH_DEFAULT.

## Active-surface findings

- `CLASS_C_DISPATCH_SPEC.md:31` [PROSE-INERT] SINGLE_POLE_ANSATZ: Not "does the bath have a single pole?":
- `CLASS_C_DISPATCH_SPEC.md:74` [PROSE-INERT] SINGLE_POLE_ANSATZ: 2. **No single-pole ansatz** — the ansatz under test may not be assumed inside the test.
- `CLASS_C_DISPATCH_SPEC.md:75` [PROSE-INERT] MYR_TARGET: 3. **No τ₀ target** — no 41.9 Myr, no desired timescale may enter setup, plots, fits, or
- `RUNG3_SPECTRAL_MEASURE_SPEC.md:11` [PROSE-INERT] PREFERRED_OUTCOME_LANGUAGE: Not "can we justify J ∼ ω³", and not "find an exponent that gives the desired memory":
- `RUNG3_SPECTRAL_MEASURE_SPEC.md:56` [PROSE-INERT] PREFERRED_OUTCOME_LANGUAGE: 3. physical justification for the chosen order **selected independently of the desired memory
- `RUNG3_SPECTRAL_MEASURE_SPEC.md:65` [PROSE-INERT] SINGLE_POLE_ANSATZ: 4. only then: comparison against the registered single-pole/Markovian structure — accepting
- `CLASS_C_DISPATCH_DECISIONS.md` [no forbidden pattern] -: -
- `CLASS_C_MANIFEST.json:49` [PROSE-INERT (declared prohibition)] J_OMEGA3: "J(omega) ~ omega^3 as an input",
- `CLASS_C_MANIFEST.json:50` [PROSE-INERT (declared prohibition)] SINGLE_POLE_ANSATZ: "single-pole ansatz inside the test",
- `CLASS_C_MANIFEST.json:51` [PROSE-INERT (declared prohibition)] TAU0_TARGET: "tau_0 or any target timescale",
- `calc/class_c_solver.py` [no forbidden pattern] -: -
- `calc/class_c_stage_c1.py` [no forbidden pattern] -: -
- `provenance/class_c_benchmark_matrix.py:56` [REFERENCE-DATA-INERT] J_OMEGA3: return (Lam ** 3 / 3.0 - Lam ** 2 * w / 2.0 + w ** 3 / 6.0) / (4.0 * math.pi ** 2)
- `provenance/class_c_contamination_audit.py:3` [REFERENCE-DATA-INERT] PREFERRED_OUTCOME_LANGUAGE: know what answer GRUT wants.
- `provenance/class_c_contamination_audit.py:59` [REFERENCE-DATA-INERT] PREFERRED_OUTCOME_LANGUAGE: ("PREFERRED_OUTCOME_LANGUAGE", r"desired memory|make GRUT work|preserve GRUT|GRUT wants"),
- `provenance/class_c_dependency_closure.py:16` [REFERENCE-DATA-INERT] TAU0_TARGET: FORBIDDEN_TOKEN     tau_0 / s=3 / single-pole / J~omega^3 / 41.9 (reuse of
- `provenance/class_c_dependency_closure.py:16` [REFERENCE-DATA-INERT] MYR_TARGET: FORBIDDEN_TOKEN     tau_0 / s=3 / single-pole / J~omega^3 / 41.9 (reuse of
- `provenance/class_c_dependency_closure.py:16` [REFERENCE-DATA-INERT] S3_EXPONENT: FORBIDDEN_TOKEN     tau_0 / s=3 / single-pole / J~omega^3 / 41.9 (reuse of
- `provenance/class_c_dependency_closure.py:16` [REFERENCE-DATA-INERT] J_OMEGA3: FORBIDDEN_TOKEN     tau_0 / s=3 / single-pole / J~omega^3 / 41.9 (reuse of
- `provenance/class_c_dependency_closure.py:16` [REFERENCE-DATA-INERT] SINGLE_POLE_ANSATZ: FORBIDDEN_TOKEN     tau_0 / s=3 / single-pole / J~omega^3 / 41.9 (reuse of
- `provenance/class_c_dependency_closure.py:66` [REFERENCE-DATA-INERT] HARDCODED_REGULATOR_DEFAULT: "DEFAULT_ARG_NUMERIC": "def kernel(omega, k_min=0.25):\n    return omega\n",
- `provenance/class_c_dependency_closure.py:67` [REFERENCE-DATA-INERT] S3_EXPONENT: "FORBIDDEN_TOKEN": "J = w ** 3  # the registered super-Ohmic bath, s = 3\n",
- `provenance/class_c_dependency_closure.py:67` [REFERENCE-DATA-INERT] J_OMEGA3: "FORBIDDEN_TOKEN": "J = w ** 3  # the registered super-Ohmic bath, s = 3\n",
- `provenance/class_c_freeze.py` [no forbidden pattern] -: -
- `provenance/class_c_manifest_gate.py:36` [REFERENCE-DATA-INERT] J_OMEGA3: "J(omega) ~ omega^3",
- `provenance/class_c_manifest_gate.py:37` [REFERENCE-DATA-INERT] SINGLE_POLE_ANSATZ: "single-pole ansatz",
- `provenance/class_c_manifest_gate.py:38` [REFERENCE-DATA-INERT] TAU0_TARGET: "tau_0",
- `provenance/class_c_manifest_gate.py:97` [REFERENCE-DATA-INERT] TAU0_TARGET: missing = [s for s in ("omega^3", "single-pole", "tau_0",
- `provenance/class_c_manifest_gate.py:97` [REFERENCE-DATA-INERT] J_OMEGA3: missing = [s for s in ("omega^3", "single-pole", "tau_0",
- `provenance/class_c_manifest_gate.py:97` [REFERENCE-DATA-INERT] SINGLE_POLE_ANSATZ: missing = [s for s in ("omega^3", "single-pole", "tau_0",

## Historical-surface findings (inert unless promoted)

- `RUNG3_KEYSTONE_MAP.md:27` [HISTORICAL-INERT] HISTORICAL: > Do not search for a way to make GRUT work. Search for the mathematically necessary bridge
- `RUNG3_KEYSTONE_MAP.md:117` [HISTORICAL-INERT] HISTORICAL: | C1 | "rung7 carries τ₂ ~ 1/H₀, i.e. Ht ~ 1; single-pole dominance needs Ht > 4.3" (`finite_T_pole_structure.py:262`) | toy-stationary t → 
- `RUNG3_KEYSTONE_MAP.md:347` [HISTORICAL-INERT] HISTORICAL: 3. **The free-ladder ≠ single-pole fence (E8) rides on every use of §2**, and E4's retraction
- `RUNG3_BRIDGE_SCOPE.md:41` [HISTORICAL-INERT] HISTORICAL: (omega=c|k|) gives DOS~omega^2, **J(omega)~omega^3** (s=3 super-Ohmic); WITHIN the
- `RUNG3_BRIDGE_SCOPE.md:41` [HISTORICAL-INERT] HISTORICAL: (omega=c|k|) gives DOS~omega^2, **J(omega)~omega^3** (s=3 super-Ohmic); WITHIN the
- `RUNG3_BRIDGE_SCOPE.md:42` [HISTORICAL-INERT] HISTORICAL: collisional/analytic-bath regime … the Mori-Zwanzig kernel collapses to single-pole /
- `RUNG3_BRIDGE_SCOPE.md:96` [HISTORICAL-INERT] HISTORICAL: is used.** It is assumed every time rung3 language ("memory time", "single pole", "collision
- `RUNG3_BRIDGE_SCOPE.md:106` [HISTORICAL-INERT] HISTORICAL: low-frequency dS TT spectral density is precisely the open keystone. So the s = 3 super-Ohmic
- `RUNG3_BRIDGE_SCOPE.md:107` [HISTORICAL-INERT] HISTORICAL: premise — the premise the entire single-pole derivation rests on — has an **uncomputed
- `DISPATCH_ONE_PAGE.md:28` [HISTORICAL-INERT] HISTORICAL: **Does ρ_TT(ω→0) for the pure-graviton case have a single-pole (Markovian/Debye) structure, or a branch cut?** Concretely: after assembly an
- `DISPATCH_ONE_PAGE.md:42` [HISTORICAL-INERT] HISTORICAL: We maintain a small research program (an open-system, finite-memory framing of the gravitational vacuum, audited claim-by-claim with every a
- `SPECIALIST_BRIEF_rung3_spine.md:35` [HISTORICAL-INERT] HISTORICAL: > **Spine test run → earned dispatch (2026-07-04).** The probe was *loaded onto the actual computed object* — Tan–Tsamis–Woodard, arXiv:2103
- `SPECIALIST_BRIEF_rung3_spine.md:47` [HISTORICAL-INERT] HISTORICAL: This breaks the finite-memory≈single-pole **circularity**: the pole structure becomes an *output* of Σ, not the premise (rung1's "finite mem
- `SPECIALIST_BRIEF_rung3_spine.md:49` [HISTORICAL-INERT] HISTORICAL: **Decisive because it settles the horn-conditional.** The spine test showed the low-ω TT class *is* the Tsamis–Woodard-vs-Higuchi/Marolf–Mor
- `SPECIALIST_BRIEF_rung3_spine.md:51` [HISTORICAL-INERT] HISTORICAL: **Open sub-question the dispatch also owes — the converse / uniqueness gap.** The horn-conditional is **forward-only**: screening ⇒ pole. A 
- `SPECIALIST_BRIEF_rung3_spine.md:76` [HISTORICAL-INERT] HISTORICAL: 4. **Scheme-invariance across resummation** (MEDIUM, load-bearing). The pole-vs-cut verdict must **agree** between the un-resummed and the S
- `SPECIALIST_BRIEF_rung3_spine.md:86` [HISTORICAL-INERT] HISTORICAL: | **HOLDS** | η finite / analytic single pole in the pure, S_IF-forced, gauge- and scheme-invariant object → rung3 graduates `shown→derived`
- `SPECIALIST_BRIEF_rung3_spine.md:87` [HISTORICAL-INERT] HISTORICAL: | **REFUTED** | η = 0/∞ or a non-analytic branch cut (incl. a legitimate secular-log) in that same object → single-pole class refuted; the t
- `SPECIALIST_BRIEF_rung3_spine.md:93` [HISTORICAL-INERT] HISTORICAL: 2. **Gauge-artifact kill.** A "single pole" read off the bare gauge-fixed (de Donder) Σ_R or bare Im G_R^TT, without demonstrated gauge-fami
- `SPECIALIST_BRIEF_rung3_spine.md:105` [HISTORICAL-INERT] HISTORICAL: - **Strictly v5.** The v4 single-pole anchor is reference-history, not an input. The favorable lean is flagged in the register's own ledger 
- `SPECIALIST_BRIEF_rung3_spine.md:144` [HISTORICAL-INERT] HISTORICAL: 1. **The k-direction structure of c₀(ω,k²) — specifically its crossover scale.** The register banks the scalar coefficient's ω-structure onl
- `SPECIALIST_BRIEF_rung3_spine.md:176` [HISTORICAL-INERT] HISTORICAL: the body's kill-conditions: a single-pole/finite-memory structure must be an OUTPUT of the graviton
- `calc/worldline_reduction.py:16` [HISTORICAL-INERT] HISTORICAL: PART 1 (where rho ~ omega^3 actually comes from). Flat space, T=0: a bilinear
- `calc/worldline_reduction.py:20` [HISTORICAL-INERT] HISTORICAL: The memory-carrying NONANALYTIC piece is w^3/6 -- the register's s=3 premise,
- `calc/worldline_reduction.py:123` [HISTORICAL-INERT] HISTORICAL: # ---------------- PART 1: where omega^3 comes from (flat, T = 0) --------
- `calc/worldline_reduction.py:135` [HISTORICAL-INERT] HISTORICAL: print("     -> memory-carrying NONANALYTIC part: + w^3/(24 pi^2): s = 3 located;")
- `calc/worldline_reduction.py:221` [HISTORICAL-INERT] HISTORICAL: print("  1. rho ~ omega^3 is recovered ONLY as the zero-temperature flat-space")
- `calc/worldline_reduction.py:254` [HISTORICAL-INERT] HISTORICAL: return (Lam ** 3 / 3.0 - Lam ** 2 * w / 2.0 + w ** 3 / 6.0) / (4.0 * math.pi ** 2)
- `calc/tt_worldline_spectrum.py:94` [HISTORICAL-INERT] HISTORICAL: print("\nPART 1 -- <h^2>(t) with IR regulator k_min = 0.5, UV cutoff W_c = 50")
- `calc/tt_worldline_spectrum.py:174` [HISTORICAL-INERT] HISTORICAL: print("\nPART 6 -- regulated spectrum S_TT(w; k_min, t_bar=2.0), Hann window")
- `calc/tt_worldline_spectrum.py:196` [HISTORICAL-INERT] HISTORICAL: print("     tau_eff vs k_min (half-decorrelation at t_bar = 2.0):")
- `calc/RESULTS_worldline_reduction.md:27` [HISTORICAL-INERT] HISTORICAL: w³/6: rung3's s = 3 premise is real, but it is a **zero-temperature flat-space artifact** —
- `calc/RESULTS_worldline_reduction.md:60` [HISTORICAL-INERT] HISTORICAL: contradicting the FINITE-memory claim as much as it contradicts s = 3; and it is NOT a verdict
- `calc/RESULTS_worldline_reduction.md:79` [HISTORICAL-INERT] HISTORICAL: > super-Ohmic input J ~ omega^3 is recovered only as the zero-temperature flat-space
- `calc/RESULTS_worldline_reduction.md:90` [HISTORICAL-INERT] HISTORICAL: - Does not validate or refute the single-pole ANSATZ itself at class C.
- `calc/RESULTS_tt_worldline.md:38` [HISTORICAL-INERT] HISTORICAL: single-pole) cannot be POSED for the gravitational channel without an epoch-window
- `calc/RESULTS_tt_worldline.md:81` [HISTORICAL-INERT] HISTORICAL: exists at class A for the graviton.** The registered J ∼ ω³ → single-pole chain therefore

## Adjudication rule

EXECUTABLE/MANIFEST/PREREG hits fail the audit outright. PROSE-REVIEW hits
block transmission until reclassified. PROSE-INERT hits are permitted only
where the quantity is named in order to be prohibited or reported.
