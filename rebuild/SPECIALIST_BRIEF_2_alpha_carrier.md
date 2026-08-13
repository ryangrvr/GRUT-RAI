# Specialist Brief 2 — S^4 conformal-anomaly a/c value + the alpha carrier

> ## STATUS: PARTIALLY SUPERSEDED (re-marked 2026-08-09) — scope before any dispatch
> The normalization half targets a banked settled-negative; the carrier half remains live but is
> now carried as **Rider A of `SPECIALIST_BRIEF_rung3_spine.md`** — dispatch that, not this.
> Original partial-staleness note of 2026-08-02 below.

> **⚠️ PART 2 IS PARTIALLY STALE (2026-08-02) — scope carefully before dispatch.** The **normalization question only** (can a trace/anomaly coefficient normalize the tracefree TT kernel — Q2/outcomes O3–O4) targets the α→TT bridge the register has since banked **settled-negative and frozen** (`rung9b_bridge`, 2026-06-27; three named obstructions, projector orthogonality primary — see `NO_GO_LEDGER.md`). If dispatched, that question can serve only as *external confirmation of a banked negative* (or as a hunt for the named rescues — a new metric-built scalar→TT intertwiner, or a legitimate CFT route in which the c/C_T Weyl-sector coefficient normalizes the TT two-point; see `NO_GO_LEDGER.md`'s spec-for-completion). **The carrier question (which sector carries the DC spectral weight — Q3/outcomes O5–O6) remains LIVE and register-open**: rung9b explicitly fences "the settled-negative does NOT prejudice the S⁴ front," and `rung9a_value` keeps the carrier identification open. Part 1 (the a/c value) is unaffected.

_Drafted by the GRUT oversight loop, then adversarially screened (4 lenses: decisive-object, leads-the-witness, self-contained, discriminating-outcomes) before release. Forwardable as-is; assumes zero GRUT context._


## Addressed to

A specialist in conformal anomalies and heat-kernel / Seeley-DeWitt methods in curved space (Part 1), and separately a specialist in linear-response / retarded two-point functions of the gravitational field on de Sitter / Euclidean S^4 (Part 2). The brief is split because the two parts require different expertise and target different objects; a single specialist competent in both may answer both. NO prior knowledge of the requesting framework is assumed or required.


## The object

TWO DISTINCT OBJECTS, deliberately separated (they were conflated in the draft).

OBJECT 1 — the per-species conformal-anomaly ratio a/c (a CFT-coefficient computation; decides only a coefficient VALUE).
Compute the two universal type-A and type-B 4D trace-anomaly coefficients for a single real conformally-coupled scalar (xi = 1/6, operator -Box + R/6) in the convention
    <T^mu_mu> = c * W^2 - a * E_4   (+ scheme-dependent local term beta * Box R, to be discarded),
where W^2 = C_{munurhosigma} C^{munurhosigma} is the Weyl-squared invariant and E_4 = R_{munurhosigma}R^{munurhosigma} - 4 R_{munu}R^{munu} + R^2 is the Gauss-Bonnet/Euler density, both in the standard 1/(4pi)^2 normalization with the per-species table of Duff 1994 (CQG 11, 1387), eqs. (30)-(31), equivalently Birrell-Davies (1982) §6.3, equivalently Komargodski-Schwimmer (2011) App. A. Report (i) raw a, (ii) raw c, (iii) the convention-independent dimensionless ratio a/c, and (iv) the explicit scheme used. The Box R term is scheme-dependent (removable by a local counterterm) and is NOT part of either a or c; state how it was discarded.
   CRITICAL EXTRACTION NOTE (this is where the draft was ill-posed): a and c are background-INDEPENDENT local Seeley-DeWitt a_2(x) coefficients. They must NOT be read off from the value of the effective action evaluated on a fixed conformally-flat S^4, because the Weyl tensor vanishes identically on S^4 (W = 0 there), so the c-term is identically zero ON that background and is invisible in the S^4 bulk a_2. Extract a from the Euler/type-A structure (nonzero on S^4) and extract c from the response to a Weyl-curving (transverse-traceless metric) deformation OFF conformal flatness — i.e. the coefficient of W^2 in the general-background a_2(x), not the on-S^4 value. State both extractions explicitly.

OBJECT 2 — the DC normalization of the retarded spin-2 (transverse-traceless) response (a linear-response computation; decides which sector CARRIES the susceptibility and whether a trace-sector coefficient can normalize a tracefree-sector kernel).
Setting/state: Euclidean S^4 of unit radius (equivalently its Lorentzian continuation to de Sitter in the Euclidean / Bunch-Davies vacuum), maximally symmetric round metric, signature and continuation to be stated by you. Consider the retarded metric-response (graviton self-energy / metric two-point) kernel decomposed into irreducible sectors: a spin-2 transverse-traceless (TT) sector and a spin-0 trace/conformal sector. Define the rank-4 4D TT projector P^TT_{munurhosigma} (transverse, symmetric, traceless: eta^{munu} P^TT_{munurhosigma} = 0, projecting onto the 5 spin-2 polarizations). The requesting framework writes its constitutive kernel as
    K^R_{munurhosigma}(omega) = c_0 * chi(omega) * P^TT_{munurhosigma},   chi(omega) = 1/(1 - i*omega*tau_0),   chi(0) = 1,
so the DC amplitude of the kernel in the TT sector is the single number c_0 = K^R(omega -> 0) on the TT channel. The order of limits is FIXED as omega -> 0 taken at strictly k = 0 (the long-wavelength, then zero-frequency, limit; both limits must be reported and any non-commutativity flagged). The retarded operator ordering is to be used (the spectral content is Im of the retarded correlator if a spectral statement is made).
The question for Object 2 is a structural/operator one, stated below — it asks whether a coefficient defined in the trace sector can legitimately set c_0 in the tracefree sector, GIVEN the stated fact that the double trace eta^{munu} eta^{rhosigma} P^TT = 0 identically.


## The question

See decision_table and the_question fields; this duplicate placeholder is intentionally identical in intent.


## Why it matters

A constitutive amplitude in a model of the gravitational vacuum is currently fixed by adopting a single dimensionless number, and we are trying to determine which, if any, first-principles object actually determines it — or to establish cleanly that nothing does, so the number must be reported as a free adopted parameter. Both a positive result (a concrete object fixes the amplitude) and a negative result (no such object exists; the amplitude is free) are equally useful and equally publishable to us; we have no stake in which way it comes out, and a result that frees the parameter is as valuable to us as one that fixes it. The two parts are separated because an anomaly-coefficient value (Part 1) and the question of which sector carries a retarded response and whether a trace coefficient can normalize a tracefree kernel (Part 2) are logically distinct objects, and we want each answered on its own terms rather than have one stand in for the other.


## Decision table — every outcome maps to an action

Every outcome maps to a defined, terminal decision; there is no ambiguous "null" branch.

PART 1 (value):
- O1: a/c = 1/3 (in the stated convention). DECISION: the per-species value for a single real conformally-coupled scalar is confirmed; this fixes a coefficient VALUE only and is explicitly NOT taken to decide Part 2. Booked as: value-confirmed, carrier/normalization still governed by Part 2.
- O2: a/c != 1/3. DECISION: the identification of the relevant degree of freedom with a single real conformally-coupled scalar is falsified; the adopted value is not the conformal-scalar ratio, and the amplitude is treated as free / sourced by a different coefficient. (This is a genuinely live outcome ONLY if Part 1 is later re-posed for a different operator — for a single real conformally-coupled scalar the published value is 1/3, so O2 here would indicate a convention/computation error to be reconciled, not a physics falsifier. The live falsifier on VALUE lives in the IDENTIFICATION, handled in O5 below.)

PART 2 (carrier / normalization):
- O3: a valid channel EXISTS by which a conformal-anomaly coefficient sets c_0 on the TT kernel (explicit identity/Ward relation supplied). DECISION: the amplitude is anchored to that coefficient; record the identity, state, and limit. (Positive result.)
- O4: NO valid channel exists (eta-eta-P^TT = 0 is an obstruction with no rescue; trace-coefficient -> tracefree-amplitude is a category mismatch). DECISION: terminal and actionable — the amplitude c_0 is a FREE adopted normalization with no anomaly carrier; downstream quantities that depend on it must be reported as resting on a free parameter. This is a COMPLETE answer, not a stuck state. (Negative result — fully acceptable and expected-possible.)
- O5 (carrier, Q3): the DC spectral weight is carried by the SPIN-0/TRACE sector. DECISION: consistent with a trace/conformal carrier; pursue whether its coefficient can normalize the TT kernel (feeds O3/O4).
- O6 (carrier, Q3): the DC spectral weight is carried by the SPIN-2/TT sector (or is source-multipole-dependent with no unique answer). DECISION: the trace/conformal-mode carrier identification is falsified or undetermined; the amplitude is sourced by the TT sector itself or remains unidentified. (Live falsifier on the IDENTIFICATION.)
- O7 (well-posedness): if Q2 or Q3 is found ILL-POSED as stated (e.g. the limits do not commute, the sector decomposition is ambiguous on this background, or "carrier" is not a well-defined property of the response). DECISION: report the ill-posedness with the minimal reformulation that WOULD be well-posed; this redirects the program rather than leaving it stuck.


## Pitfalls & wrong objects

- WRONG OBJECT (the draft's central error): asking the a/c ratio to decide which sector carries the response, or to set an absolute DC amplitude. a/c is dimensionless and normalization-independent; it is provably silent on the carrier and cannot fix an absolute normalization. Do not let Object 1 stand in for Object 2.
- WRONG EXTRACTION: do NOT read c from the effective action evaluated on the fixed S^4. W = 0 on S^4, so the W^2 (type-B) term is identically zero there and c is invisible. c must come from the off-conformally-flat (TT/Weyl-curving) variation; a from the Euler/type-A structure. Reporting "c = 0 on S^4" or an ill-defined ratio is the symptom of this error.
- TWO PHYSICALLY DISTINCT OPERATORS must not be conflated: (i) a healthy 2nd-order real conformally-coupled scalar (-Box + R/6), whose a/c = 1/3 (Object 1 as specified); versus (ii) a 4th-order Paneitz/Riegert conformal-mode (sigma) effective action, a pure type-A / Q-curvature object whose a/c is NOT generically 1/3. Object 1 is specified as (i). If you believe the physically relevant carrier is (ii), do not silently substitute it — flag it and report its a/c separately (a != 1/3 result for (ii) would be a meaningful identification finding, not an error).
- KINEMATIC vs DYNAMICAL: Object 1 is the trace-anomaly structure constant in the renormalized one-loop background effective action Gamma[g] (coefficients of E_4 and W^2), NOT the inverse-Paneitz Green's function / propagating mode. If the only well-defined a/c for the operator you choose requires its propagator (a dynamical object), report THAT explicitly — it is itself a decisive return (it means no purely kinematic ratio exists for that operator).
- STATE / ORDERING / LIMITS for Object 2: a Euclidean S^4 anomaly is a zeta-function object with no operator ordering or i-epsilon; the kernel amplitude c_0 is a Lorentzian retarded (in-in) DC limit. Do not bridge these implicitly. State your analytic continuation (Euclidean S^4 -> de Sitter / Bunch-Davies -> retarded), the operator ordering, and the order of limits (omega -> 0 at k = 0; report if limits fail to commute).
- CONVENTION TRAP: a/c is convention-independent only if a and c are in the same anomaly basis; raw coefficients differ between references by factors (e.g. 360 between Birrell-Davies and Komargodski-Schwimmer normalizations). Report raw a, raw c, the basis, AND the ratio so the result is auditable and you do not return the inverse (3 instead of 1/3).
- GIBBONS-HAWKING-PERRY conformal-factor instability / S^4 zero modes: state whether you include or exclude these for the kinematic ratio; if out of scope, declare it.


## Independence note (please resist us)

Neutral statement of what is sought, de-biased: we are determining (a) the per-species conformal-anomaly ratio a/c for one real conformally-coupled scalar, and (b) whether any conformal-anomaly coefficient can consistently set the DC amplitude of a transverse-traceless response kernel whose double trace vanishes identically, and which sector carries the DC spectral weight of the retarded response. We are NOT seeking any particular value and NOT seeking any particular sector to be the carrier. Request to resist any pull toward a preferred answer: prior internal work on this exact question has, by the requesters' own audit, repeatedly erred in the single direction that would make the construction succeed, so please treat a positive finding (a coefficient fixes the amplitude / a specific sector carries it) and a negative finding (no coefficient can fix it / the amplitude is free / the carrier is the other sector or undetermined) as equally expected and equally reportable. Do NOT infer from anything in this brief which outcome would be convenient — there is no convenient outcome. A clean "no consistent channel exists; the amplitude is free" is a complete, welcome deliverable, not a failure. If any framing in this brief reads as steering you toward a result, disregard the steer and report what the mathematics gives.


## Scope & deliverable

DELIVERABLE, PART 1 (anomaly specialist): (i) raw a and raw c for a single real conformally-coupled scalar (xi = 1/6, 4D) in the stated convention; (ii) the dimensionless ratio a/c; (iii) the regularization/scheme used (zeta-function / dimensional / proper-time heat-kernel) and confirmation that the scheme-dependent Box R term was discarded; (iv) explicit statement of how a was extracted (Euler/type-A on the background) and how c was extracted (W^2 coefficient from the off-conformally-flat variation, since W = 0 on S^4); (v) which reference table you reproduced against. Expected effort: a standard heat-kernel computation / table reproduction.
DELIVERABLE, PART 2 (response-function specialist): (i) a yes/no on Q2 with, if yes, the explicit operator identity / Ward relation and the state+ordering+limit under which a conformal-anomaly coefficient sets c_0 on the TT kernel, or, if no, a statement that the trace-coefficient -> tracefree-amplitude assignment is a category mismatch and c_0 is a free normalization; (ii) an answer to Q3 naming which sector (spin-2 TT or spin-0 trace) carries the DC spectral weight of the retarded response, whether this is source-multipole-dependent, and the order of limits used; (iii) flag of any ill-posedness with the minimal well-posed reformulation. A single specialist may deliver both parts. Each part stands alone; do not let Part 1's value substitute for Part 2's structural answer.
SELF-CONTAINMENT: all framework-internal terms are defined inline above (chi(omega), chi(0), c_0, P^TT and its trace properties, the kernel K^R, the convention for a and c, the state and limits). No external/internal documents are needed; the named public references suffice.


## References to cite

- Duff, M.J., 'Twenty Years of the Weyl Anomaly,' Class. Quantum Grav. 11 (1994) 1387, eqs. (30)-(31) — per-species (a, c) anomaly coefficients and convention
- Birrell, N.D. & Davies, P.C.W., 'Quantum Fields in Curved Space' (CUP 1982), §6.3 and Table 6.1 — conformally-coupled scalar a_2 / trace anomaly coefficients
- Komargodski, Z. & Schwimmer, A., 'On Renormalization Group Flows in Four Dimensions,' JHEP 12 (2011) 099, Appendix A — (a, c) normalization and the a-theorem framing
- Christensen, S.M. & Duff, M.J., Nucl. Phys. B154 (1979) 301 / Phys. Lett. B76 (1978) 571 — heat-kernel trace anomaly on curved backgrounds
- Vassilevich, D.V., 'Heat kernel expansion: user's manual,' Phys. Rept. 388 (2003) 279 — Seeley-DeWitt a_2 conventions and extraction
- Gilkey, P.B., 'Invariance Theory, the Heat Equation, and the Atiyah-Singer Index Theorem' — a_2(x) coefficient definitions
- Riegert, R.J., Phys. Lett. B134 (1984) 56; Antoniadis, I. & Mottola, E., Phys. Rev. D45 (1992) 2013 — the 4th-order conformal-mode (Paneitz/Riegert) effective action, for the operator-distinction note
- Dowker, J.S. & Critchley, R., Phys. Rev. D13 (1976) 3224; Bunch, T.S. & Davies, P.C.W., Proc. R. Soc. A360 (1978) 117 — de Sitter / S^4 stress-tensor and two-point structure, for Part 2's retarded-response/continuation object


## Fixes the screen applied to the draft

- DECISIVE-OBJECT SPLIT: separated the bundled, non-decisive a/c question from the actual open question. The draft asked a normalization-independent ratio (a/c) to decide which sector carries chi and to set an absolute DC amplitude; the team's own TEST B proves a/c is silent on the carrier. Now Object 1 (value, via heat-kernel a_2) and Object 2 (carrier + whether a coefficient can normalize the TT kernel, via the retarded response function) are distinct deliverables, with an explicit statement that Object 1 cannot decide Object 2.
- FIXED THE ILL-POSED EXTRACTION: the draft asked for c (Weyl^2 coefficient) 'on S^4 via a_2,' but W = 0 on S^4 (confirmed in grut/derivation/step01_heat_kernel_s4.py:123-129), making c invisible there and the ratio ill-posed. The brief now specifies a from the Euler/type-A structure and c from the off-conformally-flat (TT/Weyl-curving) variation, as background-independent a_2 coefficients.
- REMOVED LEADS-THE-WITNESS FRAMING: deleted the verbatim 'we want a/c=1/3 AND want it to be the TT-kernel carrier,' the 'keystone' and 'ONLY surviving route' stakes language, and the pre-stated target value 1/3 inside the question. The value is no longer named in the ask (only in the post-hoc comparison/decision table and as a convention reference); stakes are stated symmetrically with an explicit 'no convenient outcome' instruction.
- RELOCATED THE FALSIFIER TO WHERE THE UNCERTAINTY ACTUALLY LIVES: for a single real conformally-coupled scalar a/c = 1/3 is a textbook lookup (not a live falsifier), so the live falsifier was moved to the IDENTIFICATION (Q3 / O5-O6: which sector carries the response; is the carrier a single real conformally-coupled scalar) and to Object 2 (O4: no consistent normalization channel exists).
- PINNED STATE / ORDERING / LIMITS / SCHEME / CONVENTION so two independent specialists compute the same quantities: Euclidean S^4 unit radius / Bunch-Davies, explicit Euclidean->de Sitter->retarded continuation, retarded ordering, order of limits omega->0 at k=0 (with non-commutativity flagged), zeta/heat-kernel scheme with Box R discarded, and the anomaly basis <T^mu_mu> = c W^2 - a E_4 with raw a, raw c, and ratio all reported (guarding the 360-factor / inverse-ratio convention trap noted in the repo's clashing labelings).
- ELIMINATED THE AMBIGUOUS-NULL OUTCOME: the most-likely honest result (value = 1/3 but carrier/normalization undecided) is now a DEFINED, non-stuck branch (O1 + O4), explicitly booked as 'value confirmed; amplitude is a free adopted parameter; downstream results rest on a free parameter' rather than 'bridge stays open / stuck.' Added the previously-missing outcomes O7 (ill-posed -> minimal reformulation) and the 4th-order-Riegert-operator branch.
- MADE IT SELF-CONTAINED FOR ZERO-CONTEXT SPECIALISTS: defined chi(omega), chi(0), c_0, K^R, P^TT (with eta P^TT = 0 and the double-trace = 0 stated as a starting datum), the anomaly convention as an equation, the state, and the limits inline; stripped framework-internal jargon (alpha carrier, sector-orthogonal, IR carrier, E4/E8 labels) and named the canonical public references (Duff 1994, Birrell-Davies, KS 2011, Vassilevich, etc.).
- STATED THE KNOWN OBSTRUCTION (eta^{munu} eta^{rhosigma} P^TT = 0) UP FRONT as the specialist's starting datum so they are not asked to rediscover it or to 'find a way' to make the trace coefficient enter the tracefree kernel — Q2 is posed neutrally as 'exhibit a consistent channel or report that none exists,' with the negative result pre-blessed as complete.

---

## AMENDMENT v1.1 — three strengthenings (from a referee-mode review of this brief)

These three additions raise the rigor bar; none of them steers toward an outcome.

**A. Object 2 (Q2) must EXHIBIT the identity, not answer yes/no.** Do not return a verdict in words. Either (i) write the explicit operator identity / Ward relation in equation form that relates the transverse-traceless retarded two-point function `Im G_R^{TT}(omega,k->0)` (equivalently its DC normalization c_0) to a conformal-anomaly coefficient, stating the state, ordering, and limit under which it holds; or (ii) prove no such identity exists (e.g. by the orthogonality of the trace and TT irreducible representations: the anomaly lives in `g^{munu}T_{munu}` while `g^{munu} P^TT_{munurhosigma} = 0`, and no diffeomorphism/Weyl Ward identity maps one irrep into the other). Produce mathematics, not intuition. A clean proof that no identity exists is a complete, welcome deliverable — but if you claim impossibility, NAME THE PRECISE OBSTRUCTION (e.g. representation-theoretic / no scalar→TT intertwining operator, a Ward identity, a BRST/gauge argument, analyticity, a conservation law, or projector orthogonality). "No, because they seem unrelated" is not acceptable; identify *why* no map can exist.

**B. UV normalization vs IR susceptibility — supply the RG bridge or concede the gap.** A conformal-anomaly coefficient is UV data (a coefficient in the renormalized one-loop effective action); the DC susceptibility c_0 = chi(0) is an IR observable. These are generically not equal. IF you claim the anomaly coefficient fixes c_0, you must additionally exhibit the renormalization-group / non-renormalization argument by which the UV coefficient survives UNCHANGED into the IR DC response. "They are both one-loop" is NOT sufficient. If no such RG argument exists, say so — that itself implies c_0 is not fixed by the anomaly even if a formal index-level channel were found.

**C. O6 expanded to include a 'source-dependent / non-invariant carrier' answer.** "Which sector (spin-2 TT vs spin-0 trace) carries the DC spectral weight?" may not have an invariant answer: in linear response the spin decomposition depends on the source, the observable, and the order of limits. A fully legitimate (non-evasive) return is: "the notion of a unique 'carrier' is not invariant — different external sources project onto different irreducible components; here is the carrier for source X and for source Y." This is a real feature of tensor decompositions in response theory, not a dodge; book it as a defined outcome alongside O5/O6.

_Net effect: A converts the structural question into a proof obligation (the thing that would bank or kill the alpha-bridge); B adds a third independent hurdle for the bridge (beyond trace-vs-TT orthogonality and the carrier question); C prevents a forced false-dichotomy on the carrier._
