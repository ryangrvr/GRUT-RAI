# CLASS-C wall contracts — D4 (gauge/assembly) and D5 (renormalization)

> **STATUS: CONTRACTS, NOT RESOLUTIONS.** The manifest fields `gauge` and
> `renormalization` remain `UNDECIDED-DISPATCH`. What is frozen here is the
> PROCEDURE each field will be resolved under: the five questions answered from
> the banked literature record, the acceptance criteria, and the checks that
> must pass before any result is interpreted. Nothing here uses the desired
> rung-3 outcome as a criterion. Written 2026-08-22 per owner direction;
> supersedes nothing; banks nothing.

## D4 — the gauge/assembly contract

### Q1. What object is being assembled?

The gauge-invariantly assembled retarded TT response of the PURE-graviton de
Sitter self-energy:

    rho_TT(w->0) = 2 Im G_R^TT(w),  eta = lim Im G_R^TT / w,

obtained from the coefficient function T²(x;x′) of Tan–Tsamis–Woodard
(arXiv:2103.08547) after (i) Schwinger–Keldysh conversion to the retarded
object T²_SK (arXiv:2107.13905 §2.2.3, eqs 52–55), (ii) gauge-invariant
assembly of source vertex + observer vertex + external-mode-function
corrections in the manner of arXiv:2602.07908 — built for a SCALAR probe; the
graviton-probe version does not exist and must be constructed (wall A), and
(iii) IR resummation — the RG half of the arXiv:2409.12003 deferral remains
open (wall B); arXiv:2507.04308 discharged only the h_mu0 untangling half.

### Q2. What gauge freedom remains at the declared order?

At O(G²) in a dS background with BD state: the individual self-energy pieces
(spin-2 and spin-0 sectors, and their gauge-parameter dependence) are
GAUGE-DEPENDENT — established for the dS graviton self-energy by
arXiv:1205.4468 and stated as unknown-in-detail by TTW §4.3. The de Donder /
trace-reverse gauge fixes the graviton two-point function but NOT the physical
content of any single diagram or sector: gauge transformations move terms
between the T-structure functions and the mode functions.

### Q3. What quantity is expected to be gauge-invariant?

Only the FULLY ASSEMBLED observable: rho_TT(w→0) (or its two-time analogue if
D1's reduction proof fails). Secondary gauge-covariant checkpoints: the Ward
identity on the assembled kernel (transversality on the retarded slot — the
diagonal-subtraction scope of the register's SCDP-scoped correction), and the
Einstein–Hilbert lock ratio P^(0,s)/P^(2) = −2 evaluated on the linearized EH
counterexample as a calibration of the projector algebra (NOT of the interacting
object).

### Q4. What additional diagrams/terms are required for gauge independence?

Per wall (A): source-vertex correction diagrams, observer-vertex correction
diagrams, and external graviton-mode-function correction diagrams — none of
which exist in the published corpus for a graviton probe. Per renormalization
(D5): the local counterterm insertions R², C²(Riemann²) and Lambda-terms of
Park–Wardard (arXiv:1101.5804), which are REQUIRED members of the assembled set,
not optional corrections. Per the frozen-TT scoping correction: graviton-loop
Table-8 structures carry ln(H²Δx²) factors that MUST survive into the assembled
object or be explicitly cancelled by counterterms — either way tracked.

### Q5. How will gauge-equivalent formulations be checked?

Mandatory dual-gauge computation at dispatch: assemble rho_TT in (i) de Donder
traceless and (ii) one independent gauge (conformal/other), same state, same
clock declaration, same regulator set. ACCEPTANCE: the classification outcome
(pole/cut/ladder/secular/none) must AGREE between gauges; amplitudes may differ
only by gauge-characterized factors which must be reported. A classification
disagreement is a structural finding about the assembly, not a numerical
discrepancy to average.

### Resolution status

`gauge` STAYS `UNDECIDED-DISPATCH` until the dispatched computation exists.
What is frozen here: the object (Q1), the assembly requirements (Q4), and the
acceptance test (Q5). The solver remains refused.

## D5 — the renormalization contract

### Q1. What divergences occur at the declared order?

UV divergences of the one-loop pure-graviton self-energy in dS: absorbed by the
counterterm set {Lambda, R², C² = Riemann²} (Park–Woodard arXiv:1101.5804),
plus the standard field/Newton-constant renormalizations. IR: no divergence
regulator is chosen here (see Phase-4 ordering rule); the secular ln(H²Δx²)
structure is NOT a divergence to be subtracted but candidate physics — its
status is exactly what the calculation decides.

### Q2. Which counterterms are permitted by the frozen framework?

Exactly the local diffeomorphism-invariant operators of the booked EFT operator
basis (calc/operator_basis.py, S1–S7 frame; eta,k family fences): R², C², and
the cosmological-constant term, with coefficients renormalized — NO operator
outside the basis may be introduced, and the trace-anomaly-fixed coefficients
(b, b′) are imported with their booked provenance (rung9a).

### Q3. Which finite pieces are scheme-dependent?

The finite local parts of the allowed counterterms (notably the finite R²-type
coefficient, i.e., a possible mass-like secular term) and any scheme-dependent
local contact contributions to the noise kernel's short-distance piece.

### Q4. Which quantity, if any, is scheme-independent?

The EXISTENCE and CLASSIFICATION of the low-frequency structure (pole vs cut vs
ladder vs floor vs none) is required to be scheme-independent for the result to
be physical — because these are nonanalytic-in-ω structures, and analytic
(local/contact) redefinitions cannot move them without changing the theory's
observable content. Amplitudes and local pieces MAY be scheme-dependent; those
differences must be reported, never averaged away.

### Q5. Does changing scheme alter the existence/classification of the memory structure?

THIS IS A MANDATORY DISPATCH TEST: compute the classification under two
prescriptions (e.g., cutoff vs dimensional-like regularization of the same
one-loop set, or the two available SK conversions where applicable). Acceptance:
classification agreement. If classification changes with scheme, the registered
question has answer "scheme-dependent existence" — itself a decisive negative/
structural result recorded as such (outcome class 6-adjacent), NOT smoothed over.

### Resolution status

`renormalization` STAYS `UNDECIDED-DISPATCH` until the dispatched computation
adopts a prescription satisfying this contract. What is frozen: the divergence
set (Q1), the permitted counterterm boundary (Q2), the scheme-dependence map
(Q3), the scheme-independence requirement on classification (Q4/Q5).

## RUNG1 CONSEQUENCE ASSESSMENT (draft — owner adjudication required)

If the assembled class-C response yields any of C1.d (secular/nonstationary),
C1.e (no long-memory structure), or C1.f (ill-posed), those outcomes contradict
`rung1_inin_action`'s clause *"a responsive medium with finite memory"* at tier
`shown`, Δ4. Three of seven branches noticed this contradiction and listed rung1
as untouched anyway — declining to carry the consequence into the register.

The contradiction is real and must be assessed, not routed around:

- If the response shows **secular growth** or **nonstationary memory**, then
  "finite memory" is not an exact property of the medium — it may hold only in
  a regime (e.g., subhorizon, early-time) that the class-C calculation probes
  beyond. Rung1 would need re-tiering from `shown` to `derived-pending` on
  the finite-memory clause specifically, with the scope of validity stated.
- If the response shows **no long-memory structure at all**, then "finite
  memory" fails as a description of the medium's response to gravitational
  perturbations — which would require re-examining whether rung1's influence-
  action formalism describes gravity at all, or only matter on a fixed
  gravitational background.
- Either way, the consequence propagates: `rung3_single_pole` inherits the
  revised rung1 status, and every downstream export that assumed finite memory
  inherits the revision.

This assessment requires owner adjudication because it touches a shown-tier,
Δ4 node — the highest-consequence register change available in this program.



