# Specialist Brief 3 — Deriving the spatial adiabatic dilatation from a finite-memory influence action on de Sitter (decides: derived or presupposed?)

> ## STATUS: SUPERSEDED (marked 2026-08-09) — do not dispatch
> The L0-redundancy question was resolved in-house (`calc/L0_redundancy.py`, the L0 screen);
> the residue lives in the register, not in an external ask. Retained for the record.

_Drafted by the GRUT oversight loop; adversarially pre-screened (4 lenses: leads-the-witness, decisive-object, self-contained, discriminating-outcomes) with the FIX-THEN-RELEASE fixes applied; **pending overseer screen before release.** Forwardable as-is; assumes zero context about the requesting framework._


## Addressed to

A specialist in **cosmological perturbation theory and adiabatic modes** (Weinberg's adiabatic mode; the Maldacena / single-field consistency relation; the dilatation Ward identities of Hinterbichler–Hui–Khoury), **de Sitter / Euclidean-S⁴ quantum field theory**, and **closed-time-path (Schwinger–Keldysh) influence-functional / open-system methods in curved spacetime**. No prior knowledge of the requesting framework is assumed or required; all terms are defined inline against standard literature.


## Background (self-contained)

Consider an effective open-system description of a slow gravitational variable — the long-wavelength metric perturbation `h` of a spatially flat FRW / de Sitter background — obtained by integrating out fast degrees of freedom in the closed-time-path (in-in) formalism. The result is a **Feynman–Vernon influence action** S_IF[h₊, h₋] on the doubled (CTP) contour, whose real part contains a **retarded response (memory) kernel** K_R and whose imaginary part contains a noise kernel. The retarded kernel is **non-local in time with a single characteristic memory time L₀** (a correlation time); in frequency space a single-pole / relaxation form is K_R(ω) = −iω · χ(ω), χ(ω) = 1/(1 − iωL₀). The **memoryless (Markovian) limit is L₀→0**, where K_R becomes local in time (instantaneous).

Separately, recall the standard **adiabatic mode**: a constant long-wavelength spatial dilatation **x → e^λ x** is, in the k→0 limit, a residual large gauge transformation of **any FRW** cosmological action — locally pure gauge — and generates the physical adiabatic curvature perturbation (Weinberg 2003; the soft-ζ consistency relation). Separately, on de Sitter the **dilatation isometry** acts *jointly* on conformal time and space, (η, x) → (s η, s x). These are two distinct objects, and **whether the spatial adiabatic mode x → e^λ x coincides with the spatial part of the de Sitter isometry, as read off the influence action S_IF, is precisely the open question of this brief — not an assumed identity.**


## The object

Compute the variation of the influence action S_IF on a de Sitter background under the adiabatic dilatation, and decide its origin:

1. **The variation.** Compute δS_IF under the de Sitter dilatation isometry (the joint time/space rescaling whose long-wavelength spatial part is x → e^λ x), keeping the finite-memory kernel K_R(L₀). Determine (i) whether **δS_IF → 0 as L₀ → 0** (i.e. the memoryless influence action is exactly invariant under the adiabatic dilatation), and (ii) whether **L₀ is the unique *classical* (tree-level) parameter whose nonvanishing breaks that invariance** — δS_IF = O(L₀), with no other classical scale in the local sector breaking it.

2. **The decisive object — the identification map.** The kernel K_R(ω) is a function of **frequency** ω only; its local (L₀→0) part −iω is homogeneous of degree 1, which singles out the **frequency dilatation ω → s ω** as the unique constant-weight redundancy of the kernel. The physical adiabatic mode, however, is a **spatial dilatation x → e^λ x**. **The decisive question is whether the map between them — frequency-dilatation ↔ spatial-adiabatic-dilatation (call it the "ω↔x map") — is *derived from* the de Sitter S_IF (via the de Sitter isometry that links time- and spatial-rescaling), or whether it must be *assumed* by importing the background's diffeomorphism / adiabatic-mode structure as external input.**


## The question

> **On de Sitter, is the spatial adiabatic dilatation (x → e^λ x) and its invariance of the memoryless influence action *derived from* S_IF and the de Sitter isometry — i.e. does the de Sitter covariance of S_IF itself supply the ω↔x identification — or is that identification an *input* (the separate-universe / Weinberg adiabatic-mode construction, presupposing the background diffeomorphism structure)?**
>
> Equivalently: can you exhibit, from the de Sitter influence action alone, a Ward identity that *forces* the kernel's frequency-dilatation to be the spatial adiabatic dilatation — with the adiabatic mode and its field weight read off the action — without separately assuming the adiabatic-mode ansatz?


## Why it matters (stated neutrally)

The requesting framework currently *posits* a long-wavelength consistency relation (a separate-universe / adiabatic-dilatation statement) and would like to know whether that relation is **derivable from the influence action**, or whether it is an **irreducible assumed input**. **Both outcomes are equally useful and equally publishable to us.** A positive result (the adiabatic mode is derived from the de Sitter S_IF) upgrades a posited consistency relation to a *theorem*; a negative result (the ω↔x map is an imported assumption) cleanly *names the irreducible input*, which is itself the result we are after. We have **no stake in which way it resolves**, and we are actively trying to avoid fooling ourselves into the positive answer (see the independence note).


## What we have ALREADY established (please do not redo; build on or refute it)

A frequency-space, single-mode in-house calculation has already settled the parts that frequency space *can* settle — please take these as given inputs, and either build on them or refute them:

- **(i) is settled in frequency space and is general.** Define the dilatation-breaking density B(ω) = (ω ∂_ω − 1) K_R(ω). For **any** analytic causal kernel K_R(ω) = −iω · f(iωL₀) with f(0) = 1, one finds **B(ω) = ω² L₀ f′(iωL₀) = O(L₀)**, vanishing linearly as L₀→0 (verified across single-pole, exponential, and higher-pole memories). So the memoryless influence action is **exactly invariant under the frequency dilatation** — this part holds and is not in question.
- **(ii) fails beyond the classical sector and is rescuable only classically.** With L₀ = 0 exactly, a quantum **trace/conformal anomaly** (⟨T^μ_μ⟩ ≠ 0) enters as a **log-running coupling**, K_R^anom(ω) ≈ −iω · b · log(ω/μ), whose dilatation-breaking density is B^anom = (ω ∂_ω − 1) K_R^anom = **−i b ω ≠ 0** (the *logarithm* is what makes B nonzero — a bare −ibω term would be degree-1 and give B = 0). So the anomaly breaks dilatation invariance **independently of memory**: L₀ is **not** the unique breaker; it is the unique breaker only in the **classical / anomaly-free** sector (there B ≡ 0 for all ω ⟺ f′ ≡ 0 ⟺ no memory term). **Please do not chase "memory is the only source of structure" — it is already excluded by the anomaly.**
- **What frequency space CANNOT settle (your object).** The in-house input above is a **frequency-only kernel** K_R(ω) with the homogeneity operator (ω ∂_ω − 1) — i.e. a **flat-space / time-translation-invariant** calculation. On de Sitter the scale factor a(η) breaks global time-translation invariance, so K_R is generically **bi-local in conformal time** and that operator need not act diagonally; promoting the frequency-space result to de Sitter is itself part of your task (and a genuine possible negative — see the decision table). Moreover the calculation has no spatial structure, so it cannot decide whether the kernel's frequency-dilatation **is** the spatial adiabatic dilatation. Deciding that ω↔x identification — the decisive question above — requires the de Sitter spatial geometry; **we ask you to decide it *either way*, and we do not assume the spatial geometry supplies the link.**


## Decision table — every outcome maps to a disposition

| Your finding | Disposition |
|---|---|
| **ω↔x map DERIVED** from the de Sitter S_IF / isometry (a Ward identity forces it; the adiabatic mode + weight come from the action) | The long-wavelength redundancy is **derived**; the posited consistency relation **graduates to a theorem**. (Subject to the ceiling below — still only the *classical* uniqueness.) |
| **ω↔x map ASSUMED** (you must import the adiabatic-mode ansatz / background diffeomorphism structure to make the identification) | The assumption is **relocated, not discharged**; we bank "the foundation rests on a named irreducible input (the ω↔x / adiabatic map)." Report this plainly. |
| **δS_IF ≠ O(L₀)** on de Sitter (memoryless limit is *not* exactly invariant) | Refutes (i) on the real background; the frequency-space result was a flat-space artifact — a decision-relevant negative. |
| **A second classical scale** (besides L₀ and the anomaly) breaks the dilatation on de Sitter | Refutes the *classical* uniqueness too; report the scale. |
| **ω↔x map derived only under one order of limits** (k→0 vs ω→0 non-commuting) | Conditional/partial graduation; report which order yields the derivation and treat the other as the irreducible input. |

*Findings compose across two independent axes — (a) the origin of the ω↔x map (derived vs assumed) and (b) the classical uniqueness of L₀.* A derived map (row 1) together with a second classical scale (row 4) yields a *derived redundancy whose classical uniqueness is nonetheless refuted*; report each axis separately rather than forcing the result into a single row.


## The ceiling (stated up front, so you don't chase a dead claim)

The strong claim "**memory L₀ is the unique breaker / the only source of physical structure**" is **already dead** — the conformal/trace anomaly breaks dilatation invariance independently of memory (established above; standard physics). **Do not attempt to revive it.** The most that a positive result can reach is the **weaker, real** statement: *"the spatial adiabatic mode is derived from the de Sitter influence action, and L₀ is the unique **classical** breaker."* That is the ceiling; please target exactly that, and report honestly if even it is not reached.


## Pitfalls & wrong objects

- **Do not assume the adiabatic mode to prove it.** The entire question is whether the spatial mode is *derived* or *assumed*. A computation that starts by writing down the Weinberg adiabatic transformation (or the separate-universe rescaling) and checks its invariance has **presupposed** the answer — that is the failure mode we most need you to avoid. The derivation, if it exists, must produce the spatial mode *from* the de Sitter covariance of S_IF.
- **Frequency-dilatation ≠ spatial-dilatation, a priori.** The kernel's homogeneity in ω singles out ω→sω; that is *not* the same as x→e^λ x until the de Sitter isometry is shown to link them from the action. Conflating them is the relocation trap.
- **Classical vs quantum.** Keep the (already-excluded) anomalous quantum breaking separate from the classical/tree question; the uniqueness claim lives only in the classical sector.
- **Order of limits.** Take the long-wavelength limit (k→0) and the soft/zero-frequency limit explicitly; report any non-commutativity.
- **No new physics is expected.** Even a fully positive result is a **foundational theorem** — it predicts no observable and fixes no constant. Do not over-claim a prediction; numerology relating dimensionless coefficients is explicitly out of scope.


## Independence note (please resist us)

We **want** the positive answer — a derived adiabatic mode would upgrade our posited consistency relation to a theorem. That is exactly why we are asking an outside specialist and why we ask you to **default to "the ω↔x map is assumed / relocated" unless the derivation is genuinely from the action.** If at any point the derivation quietly inserts the adiabatic-mode ansatz, the de Sitter diffeomorphism structure, or the spatial rescaling by hand, that is a *relocation*, and the honest verdict is "presupposed." Tell us we relocated the assumption; that is the result we expect and will bank.


## Scope & deliverable

A short technical note stating: (1) whether δS_IF → 0 exactly as L₀→0 on de Sitter, and whether L₀ is the unique *classical* breaker there; (2) **the decisive verdict** — is the ω↔x map (spatial adiabatic dilatation ↔ the kernel's frequency-dilatation) **derived** from the de Sitter S_IF / isometry, or **assumed**? — with the explicit chain that makes it one or the other; (3) if derived, the Ward identity that forces it; if assumed, the precise external input that had to be imported. Either verdict is a complete, useful deliverable. This is the **last open foundational question** in the program; a clean negative is as valuable to us as a clean positive.


## References to cite

- S. Weinberg, *Adiabatic modes in cosmology*, Phys. Rev. D 67, 123504 (2003), arXiv:astro-ph/0302326.
- J. Maldacena, *Non-Gaussian features…*, JHEP 05 (2003) 013, arXiv:astro-ph/0210603 (the consistency relation).
- L. Hinterbichler, L. Hui, J. Khoury, *An Infinite Set of Ward Identities for Adiabatic Modes in Cosmology*, JCAP 01 (2014) 039, arXiv:1304.5527.
- E. Calzetta & B. L. Hu, *Nonequilibrium Quantum Field Theory* (CUP, 2008) — the CTP influence action and its memory/noise kernels.
- (For the anomaly, if needed) M. J. Duff, *Twenty years of the Weyl anomaly*, Class. Quantum Grav. 11, 1387 (1994).


## Fixes the pre-screen applied to the draft

- **Leads-the-witness (blocking) — removed a framing leak.** The Background originally asserted "this spatial dilatation is part of the de Sitter dilatation isometry," pre-loading the very ω↔x identification that is the open question. Reworded to keep the spatial adiabatic mode (x→e^λx, a residual large-gauge transformation of any FRW action) and the de Sitter isometry (joint (η,x)→(sη,sx)) as **distinct objects**, with whether they coincide *as read off S_IF* stated explicitly as the open question.
- **Correctness — the anomaly's breaking density.** "B = −ibω" was ambiguous (a bare −ibω is degree-1 and would give B=0). Restated via the log-running kernel K_R^anom ≈ −iω·b·log(ω/μ), so B^anom = (ω∂_ω−1)K_R^anom = −ibω ≠ 0 — the logarithm is the genuine breaker.
- **Correctness — flat-space vs de Sitter.** Flagged that the frequency-only kernel K_R(ω) and the (ω∂_ω−1) operator are the **flat-space / time-translation-invariant** input; on de Sitter a(η) breaks time-translation invariance, so K_R is generically bi-local in conformal time and the promotion to dS is part of the specialist's task (a genuine possible negative).
- **Leads-the-witness parity.** Replaced the "your expertise" competence-flattery at the hand-off with "decide it *either way*; we do not assume the spatial geometry supplies the link."
- **Discriminating outcomes.** Added a decision-table row for an **order-of-limits-dependent** derivation (k→0 vs ω→0 non-commuting → conditional/partial graduation), and a note that the map-origin and classical-uniqueness axes **compose** (report each separately).
