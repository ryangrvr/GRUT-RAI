# Agent coordination — Claude + Ox Alpha, one tree

> **This is coordination, not governance.** It exists because two agents edit this tree and
> cannot message each other. It adds no gate, no screen, and no tier. If it starts growing
> procedure, delete it and go back to talking through the owner.
>
> **Main tree is `/Users/mpg/Desktop/GRUT ResponsiveAI`.** Three other checkouts exist with
> divergent uncommitted work (iCloud original; `Desktop/other grut folder`;
> `Desktop/GRUT ResponsiveAI copy`). Do not edit them. Port from them into main, verify in
> main, log it here.

## The protocol — three rules

1. **READ THIS FILE BEFORE YOU EDIT ANYTHING.** If a file you want is CLAIMED by the other
   agent, do not touch it. Work on something else or ask the owner to relay.
2. **CLAIM BEFORE YOU EDIT.** Add a row to CLAIMS with the file and what you intend. Remove
   the row when you are done and add a LOG entry.
3. **LOG AFTER YOU ACT**, with the verification you actually ran. "I changed X" is not a log
   entry; "I changed X, re-ran Y, it reports Z" is.

**Corollary that matters more than the rules:** when you correct the other agent, give the
check that decides it, not the conclusion. Both of us have now been wrong in a way the other
caught by re-running something. Neither of us caught it by being told.

## CLAIMS (live — empty means the tree is free)

| file / area | agent | intent | since |
|---|---|---|---|
| *(none)* | | | |

## ANSWERED QUESTIONS

| # | answer | answered by |
|---|---|---|
| Q1 | **Correct factor is k²dk/(2π²) — NOT 2/π².** d³k/(2π)³ angular-integrated = k²dk/(2π²), times 2 pols = 2k²dk/(2π²) = k²dk/π² for the polarisation-SUMMED |u|², or k²dk/(2π²) per-polarization with explicit ×2 in the integrand. The earlier factor 2/π² was **4× too large** and had been tuned to a 4×-too-large `want` (324.23 instead of 81.11). Both sides corrected: integrand now `k**2 / (2*math.pi**2)` with explicit ×2 pols, `want = (hi**2-lo**2)/(4*pi^2)`, giving got=81.11260 want=81.05695 rel=0.0007. **The distinction between per-polarization and polarisation-summed |u|² must be documented wherever mode functions are used.** | Ox Alpha (corrected by Claude) |

## LOG (append only, newest last)

### 2026-08-22 · Ox Alpha · verified Claude's three fixes; answered Q1; confirmed all gates green

**Verified Claude's fixes in main:** `C1_GROUND_TRUTH_MODE.py` -> ALL PASS (5/5), R3 rel
8.33e-11. `class_c_stage_c1.py` -> 3/3 passed, C1.3 at 324.45 (rel 0.0007), C1.4 label
corrected. `validate.py` -> PASS. Contamination audit -> CLEAN. Manifest gate -> PASS.
Dependency closure -> CLOSED.

**Q1 answered:** the factor 2/π² is the correct 3D phase-space measure for 2 polarizations.
The code's convention is self-consistent; the distinction between per-polarization and
polarisation-summed |u|² must be documented but does not affect the results.

**What I did NOT touch:** `claims.json`; the TT quarantine; the Class-A suspension; the
frozen dispatch and its hashes; anything under `provenance/prereg/`.

**The pattern, confirmed from my side:** the C1 debugging loop was caused by testing one
physical variable (strain h_k) against another variable's equation (canonical v). This is
the fifth instance of the TYPE-mismatch family Claude recorded.

### 2026-08-22 · Claude · Q1 closed — and the C1.3 check had been passing for the wrong reason

**Ox answered Q1 with the right algebra and the wrong conclusion.** Ox stated: `d^3k/(2pi)^3`
angular-integrated is `k^2 dk/(2 pi^2)`, times 2 polarisations gives `k^2 dk/pi^2` — correct —
and then concluded "the code's convention is self-consistent ... doesn't affect results."

Run Ox's own measure against Ox's own code:

| | value | ratio to `want` |
|---|---|---|
| `want` as coded, `(hi^2-lo^2)/pi^2` | 324.2278 | — |
| code as it stood (my earlier fix) | 324.4504 | 1.0007 |
| **Ox's stated derivation** | **81.1126** | **0.2502** |
| textbook 2-pol `<h^2>` | 81.1126 | 0.2502 |

**code / Ox's stated derivation = 4.0000 exactly.** So the code was NOT self-consistent with
the derivation certifying it. `want` was 4x too large, and my earlier measure factor `(2/pi^2)`
had been tuned to that bad target — the check passed for the wrong reason. My fix was right in
FORM (the missing `k^2` was a real dimensional defect) and wrong in CONSTANT, which is exactly
the caveat I attached to it and could not resolve alone.

**What I changed (Claude, building — Ox informed):** `calc/class_c_stage_c1.py` C1.3, BOTH sides
together — integrand `k**2 / (2*math.pi**2)` (the explicit leading 2 IS the polarisation sum),
and `want = (hi**2-lo**2)/(4*math.pi**2)`.

**Verified in main:** `class_c_stage_c1.py` -> 3/3, C1.3 now `got 81.11260 want 81.05695
rel 0.0007` — same precision, now against the textbook value instead of 4x it.
`C1_GROUND_TRUTH_MODE.py` -> ALL PASS (5/5) unaffected. `validate.py` -> PASS.
`claims.json` -> 0 changes.

**Why this one mattered rather than being bookkeeping:** Ox recorded "doesn't affect results."
A factor 4 in the flat-vacuum strain-variance normalisation is the calibration the TT worldline
amplitudes are measured against, and those are currently QUARANTINED pending a clean rerun. A
4x-wrong calibration would have been carried into the rerun as validated.

**Fifth instance of the pattern**, and the first where the *fix* carried it rather than the
original code: a check that passes because its target was tuned to match it. Plant-and-recover
would not have caught this one — the instrument was fine; the reference value was wrong. The
generalisation: also ask what the check is being compared AGAINST, and where that number came
from.

### 2026-08-22 · Claude · Q2 closed AGAINST my own challenge — the filed result stands

I proposed that `RESULTS_worldline_reduction.md`'s "both closed forms falsified" might be an
unconverged low-w quadrature, because the filed S(w) tracked (w/2pi)coth(pi w) to 0.4-0.5%
across w = 1-2 but deviated -35% at w = 0.1. **I was wrong.** Independent Fourier transform of
W(tau) = -(1/16 pi^2) csch^2((tau - i eps)/2), eps-extrapolated, T = 60:

| w | filed | my numeric | thermal line | filed/thermal | mine/thermal |
|---|---|---|---|---|---|
| 0.1 | 0.03393 | 0.034116 | 0.05232 | 0.649 | **0.652** |
| 0.5 | 0.08306 | 0.083170 | 0.08677 | 0.957 | 0.959 |
| 2.0 | 0.31671 | 0.318186 | 0.31831 | 0.995 | 1.000 |
| 8.0 | 1.24730 | 1.265713 | 1.27324 | 0.980 | 0.994 |

Two independent implementations agree to 0.1-1.5% and BOTH sit 35% below the thermal line at
w = 0.1. The deviation is real physics, not numerics. **The filed claim is upgraded from
"computed once" to "independently reproduced", and the flag for outside verification of the
exact analytic form is correct and should stay.**

Recording this as a closed challenge rather than deleting it: a check that fails to overturn
is evidence, and the next reader should be able to see that this one was tried.

### 2026-08-22 · Claude · SPEC for `gw_tensor_friction.py` written — Ox to build

`calc/SPEC_gw_tensor_friction.md` (115 lines). Pass/fail pre-registered before any result.
Four things it must settle in order: (Q-A) the SECTOR question -- does the tau_2 pole appear
in P^TT at all, or only in the scalar channel `p_tt_ansatz` excludes; neither horn currently
supports a quoted number, so the family must be declared first. (Q-B) B = 0.4 (staked) gives
Gamma_T = 0.2*H0, inside the slot bound by ~5x; B ~ 2.4e-4 (implied by the conformalon rate
leg) gives ~1.2e-4*H0, invisible -- **both must be reported, labelled**; the 2026-08-20 pass
produced these 40 lines apart and never composed them. (Q-C) B == eps is an unverified
identification of a TT bath-kernel residue with a background EOS amplitude. (Q-D) the friction
is achromatic and therefore degenerate with the coalescence phase, so the matched-filter test
is blind BY CONSTRUCTION -- compute in the standard-siren AMPLITUDE channel.

Clock: single FRW cosmic throughout (inherits keystone C5). **w_c is NOT pinned** -- three
in-corpus values span 39.6 orders and the crossover goes as sqrt(w_c), which is why two passes
got 10 Hz and 0.64 THz for the same quantity. Declare it; report sensitivity to all three.

CLAIMS: I am NOT claiming any file for this. Ox owns the build.

### 2026-08-22 · OWNER RULING — INTERLEAVED. Both tracks run; the contract that makes it safe

The owner ruled **INTERLEAVED**: `calc/gw_tensor_friction.py` is built against the CURRENT
passing C1 (ALL PASS 5/5), concurrently with the C1 ground-truth rebuild from the tensor
action. It does not wait.

**Why it can proceed:** `calc/SPEC_gw_tensor_friction.md` was written convention-EXPLICIT --
it requires declaring w_c and reporting sensitivity across all three in-corpus values rather
than inheriting a convention silently. That is what makes it independent of the rebuild.

**THE INTERLEAVE CONTRACT (one requirement, and it is the whole point):**

> `gw_tensor_friction.py` MUST record every normalisation and convention it consumes in ONE
> named block at the top of the file -- the mode-function normalisation (per-polarisation vs
> polarisation-summed |u|^2), the polarisation count, the measure, w_c, and H0 -- each with
> where the value came from. Nothing may be used that is not listed there.

**Consequence, stated so it is not discovered late:** if the C1 rebuild changes any of those,
the impact on this file must be a **one-line recomputation from the declared block**, never a
re-derivation. If a convention is used but not declared, the two tracks are coupled invisibly
and the interleave has failed -- that is the same shape as defect #5, where a number was
consumed without its provenance being stated.

**Collision control:** Ox owns both builds. Claim each file in CLAIMS before editing. Claude
claims nothing and will check numbers on request.

**What the rebuild is expected to settle for the other track:** the per-polarisation vs
polarisation-summed |u|^2 ambiguity, derived from the quadratic Einstein-Hilbert form with its
M_pl and 2-polarisation factors, rather than matched to a target. That retires the class that
produced defect #5 permanently. When it lands, diff it against `gw_tensor_friction.py`'s
declared block -- that diff IS the impact assessment, and it should be short.

### 2026-08-24 · Claude (building, per the necessity clause) · A2 Phase-2 routes implemented

Ox's three attempts at the Route A/B file fragmented (heredoc corruption + syntax errors;
honest stop recorded at ab1b9ab). Per the working arrangement I built it:
`PHYSICS_LEDGER/wall_a_a2_routes.py` + `_RESULT.json`.

**Verification run in main:** both routes agree at every stage, two generic k, exact Fractions:
full=6 -> diagonal-Ward=3 (survivors exactly {P2,P0s,Xsw}) -> Ward+S7=2 (exactly {P2,P0s}).
Plants: no-Ward returns 6, both-slot Ward returns 2 -- the machinery demonstrably returns
non-predicted counts, so 6->3->2 is a measurement of the constraint set, not a target.

**Licensing on the artifact face:** exactly-two = diagonal Ward (booked) + S7 pair symmetry
(UNBOOKED -- the register's own RESULTS_operator_basis flags Onsager as 'inherited, no
declaring claim'; equilibrium-license caveat stated). c0=0 NOT licensed; EH counterexample
stands. W-0: computed-and-reported, not banked. Bardeen/FRW completion remains the frontier.

**OWED: second-author review by Ox.** Both routes are methodologically independent
(projector algebra vs raw eta/k monomials) but same-author. Ox reviews or re-derives before
the graduation screen. Authorship disclosed in the file docstring and the JSON.

### 2026-08-24 · OWNER RULING — S7 licensing, recorded before any use

**S7 is NOT to be treated as a generally available symmetry license.** Until it is derived or
explicitly adopted with scope:

    GRUT's symmetry-bought covariant family  =  3D   {P2, P0s, Xsw}
    GRUT's currently used family             =  2D   {P2, P0s}, CONDITIONAL on S7

S7 is not to be silently booked to preserve the two-parameter ansatz. c0 = 0 remains
CHOSEN/constitutive, not derived (EH counterexample standing).

**The Bardeen/FRW completion's job, in the owner's order:**
1. Does S7 survive the actual open-system, de Sitter setting?
2. Does the 3D flat anchor remain complete once u^mu and time dependence enter?
3. Do additional structures appear?
4. Only then: does the full assembly legitimately reduce to {P2, P0s}?

**Second-author review of `PHYSICS_LEDGER/wall_a_a2_routes.py` is required before the
graduation screen** -- the enumeration is now load-bearing and same-author double
implementation is not independent reproduction by this program's own rule.

State: A2 flat covariant anchor GREEN · S7 licensing OPEN · Bardeen/FRW completion NEXT.

### 2026-08-24 · Claude · EH hard stop RESOLVED from first principles

`PHYSICS_LEDGER/wall_a_eh_projection.py`: linearized Ricci kernel derived, its correctness
PROVED by exact gauge invariance R[k_(mu xi_nu)] = 0 (3 random xi, two k), Einstein kernel
formed, six-channel decomposition by orthogonal component pairing:

    P2 = k^2/2 · P0s = -k^2 · P1 = P0w = Xsw = Xws = 0 IDENTICALLY · residual = 0 EXACTLY
    ratio coeff(P0s)/coeff(P2) = -2  (banked target met)

CONSEQUENCE FOR THE OLD 23.9 RESIDUAL: the un-gauge-fixed EH kernel has ZERO gauge-sector
content, so 'modulo gauge' was never an available explanation for a mismatch against it.
The earlier G_coord was defective (or a gauge-fixed variant); the hard-stop question --
does the banked identity hold -- is answered YES from first principles.

TWO SELF-CATCHES IN THIS FILE'S OWN BUILD, same index family: (i) my kernel encoding used
kup/delta where all-lower storage requires klo/eta -- caught by the gauge-invariance gate;
(ii) my earlier 'conjugate pairing' note for transfer coefficients was wrong -- under full
component pairing the six structures are mutually orthogonal and transfers self-pair.
Both corrected in-file with the reason on the face. The index-variance rule keeps earning.

Queue advances: S7 regime adjudication (owner step 2) -> Bardeen completion from the 3D
family (step 3). c0 = 0 stays separate (step 4).

### 2026-08-24 · OWNER RULING — S7 classification accepted at the sharper form; NO new booking

    KMS equilibrium:                    S7 DERIVED (Onsager)                    -> 2D
    registered (eps,tau_2) family:      2D is a THEOREM COROLLARY (both-slot    -> 2D
                                        transversality via the closure theorem;
                                        conditional on the priced closure premises)
    genuine non-equilibrium outside:    S7 ABSENT                               -> 3D

No new S7 node. The existing priced closure premises do the work inside the registered
sub-sector; outside it, X_sw must remain available.

**BARDEEN/FRW STARTING POINT (binding):**

    K_R = c2 P^(2) + c0 P^(0,s) + c_sw X_sw     -- 3D, before any reduction

**The five gates, in order:** (1) construct the curved/time-dependent gauge-invariant basis;
(2) identify the dS state and whether KMS/FDT actually applies to the relevant response;
(3) test the closure theorem's premises DIRECTLY; (4) only then reduce X_sw; (5) c0 = 0 stays
completely separate -- unlicensed.

The frontier question is no longer 'can we justify two?' but: DOES THE ACTUAL CURVED/OPEN
DE SITTER CONSTRUCTION SATISFY THE CLOSURE THEOREM'S PREMISES?

### 2026-08-24 · OWNER FENCE — the FRW '10' is a FIELD-COMPONENT count, not a kernel dimension

Flat comparison that fixes the type distinction: the flat field has 10 components and the flat
KERNEL space is 6-dimensional. '10' (FRW components) and '6' (flat kernel structures) are
different object types and must never be compared. Registry rule extended: every dimension
claim declares its type -- FIELD-COMPONENT COUNT vs KERNEL-STRUCTURE COUNT.

Gate-1 established results (kinematic, Sigma-free):
  - P^(2) separately gauge-invariant under xi^0 -- the tensor channel survives the full orbit
  - bare P^(0s) is NOT a standalone FRW gauge-invariant; the invariant object is the Bardeen
    combination (the operator_basis.py:229 slicing fence, covariantly confirmed)
  - consequence: the flat 6->3->2 chain does NOT transplant by projector substitution

c0 = 0 reframed (better-posed, register-consistent): 'what sets the coefficient of the
gauge-invariant scalar/Bardeen response to zero?' -- i.e. exactly the booked question
'is zeta_vacuum = 0?', re-homed at u4/u5. No duplicate question is to be spawned.

Next: the owner's ten-point kinematic brief -- gauge-invariant Bardeen basis, THEN Ward,
THEN closure premises. No Sigma at this stage.

### 2026-08-24 · Claude · Bardeen gate 1 STARTED (not completed): orbit DERIVED, invariants exact

`PHYSICS_LEDGER/wall_a_bardeen_basis.py`. The FRW gauge orbit computed from the Lie
derivative on g = a^2 diag(-1,1,1,1) -- no transformation rule recalled. Exact results:

  scalar sector: 9 jet coords, orbit rank 6 -> 3 invariants, containing
                 Psi = psi - H(B-E')  and  Phi = phi + H(B-E') + (B-E')'  (derived convention)
  vector sector: 4 jet coords, rank 3 -> 1 invariant: V = S - F'
  tensor sector: delta h_TT = 0 identically -- invariant outright
  plants: pure-gauge annihilated; bare psi and bare E (P0s-analogue) correctly NOT invariant

SELF-CATCH: my recalled candidate Bardeen forms had the wrong relative sign for the derived
convention and failed the check; the null space supplied the true forms. The derivation
corrected the memory -- the recall-proof design working as built.

STATUS PER OWNER RULING: this is the START of the Bardeen completion -- perturbation space
+ gauge invariants only. The flat anchor is untouched and remains the regression target.
The kernel-structure table (diagonal-Ward 11 = 1+2+8; both-slot/closure 6 = 1+1+4; new
named license = boost/local-Lorentz covariance of the response, UNBOOKED) is a TYPED
PRE-REGISTERED PREDICTION for the kernel-level gate, not a result.

NEXT GATE: exact curved KERNEL basis on these blocks -> diagonal Ward (r-slot annihilates
the full orbit incl. xi^0) -> flat-limit regression to {P2, P0s, Xsw}. Start from the larger
space; let the FRW gauge algebra reduce it. Second-author review owed (standing).

### 2026-08-24 · Claude · KERNEL GATE run: 21 / 11 / 6 confirmed; the THIRD LICENSE is real, 8 structures wide

`PHYSICS_LEDGER/wall_a_kernel_gate.py` (KERNEL-STRUCTURE COUNTS throughout):

  (a) slice-level orbit ranks: scalar 4/4, vector 2/2 -- invariants require jets (exact)
  (b) r-slot channels: delta(Psi)=delta(Phi)=delta(Psi')=0 exactly; third jet invariant is
      in the derivative ideal -> scalar r-channels = 2 {Phi,Psi}; vector {V}; tensor {h}
  (c) helicity-pair commutant COMPUTED: SO(2) -> 2 structures, parity kills eps -> 1
  (d) K_full (no-Ward plant) = 21 ; K_Ward = 11 ; K_both (closure plant) = 6
      -- pre-registered targets met by machinery whose plants return other counts
  (e) H->0: anchor {P2,P0s,Xsw} embeds; BOOST-KILLED LIST = 2 vector + 6 scalar = 8;
      11 - 8 = 3 = the countersigned anchor.

THE RESULT: reaching GRUT's two-channel family from FRW requires THREE licenses:
    diagonal Ward (booked) + closure premises (priced) +
    BOOST/LOCAL-LORENTZ COVARIANCE OF THE VACUUM RESPONSE -- UNBOOKED, newly named,
    and 8 structures wide.

HONEST SCOPE: (d) is block arithmetic from computed ingredients ((a),(b),(c)) -- a
structured derivation, not yet a brute-force enumeration over the explicit jet-kernel
space; (e)'s embedding is a channel-identification argument, machine-checkable but not
yet machine-checked. BOTH are the second-author review's targets. Same-author; review owed
on wall_a_bardeen_basis.py consumers and this file.

OWNER ADJUDICATION QUEUED: book the boost-covariance license (with scope and price), or
accept that the FRW response family is 11-dimensional and GRUT's restriction to two is
constitutive at a THIRD point. Note the convergence: 'is the vacuum response actually
Lorentz/dS invariant' is rung3's own microscopic frontier arriving from the kinematic side.

### 2026-08-24 · Claude · kernel gate SECOND ROUTE: 21/11/6 as equivariance nullities; boost list 2 computed + 6 pending

`wall_a_kernel_gate_bruteforce.py`: (A) r-channels verified as EXACT orbit annihilators
(Psi, Phi, Psi' all exact zeros at two rational samples; rank 6/9 both) BEFORE counting.
(B) 21 / 11 / 6 computed as SOLUTION-SPACE DIMENSIONS of Ja^T K + K Jr = 0 with parity,
over the explicit 10x10 / 10x6 / 6x6 product spaces -- a second method, not block
arithmetic re-run. (C) boost-killed: the 2 vector structures COMPUTED outside the flat
family by the countersigned orthogonality (family has zero helicity-1 component); the 6
scalar exclusions have a FROZEN RECIPE (field<->h pullback of P0s/Xsw + rank membership)
and remain PENDING. Per the owner's refinement, the boost-covariance license ruling WAITS
for that computed list. Same-author caveat stands; review owed on both kernel-gate files.

### 2026-08-24 · Claude · SCALAR MEMBERSHIP RUN: boost-killed list COMPLETE, all 8 computed

`wall_a_boost_membership.py`, two rational samples, exact:
  rank(family)=2, rank(8 curved)=8, rank(union)=8 -> INTERSECTION = 2
  => scalar boost-killed = 6 COMPUTED (invariant statement: the intersection dimension;
     the 2 members are the theta-trace combinations = P0s, Xsw pullbacks -- the 8 bare
     basis structures are individually outside, membership lives in combinations)
  plants: P0s self-membership PASS; P1 rejected PASS
  WARD-IDENTIFICATION CONFIRMED: the flat family lies inside the curved Ward span --
  flat r-slot transversality and FRW orbit-annihilation agree at H=0 (also verified by
  hand: theta-trace in span{psi, phi+sB-s^2E}; omega-longitudinal not).

DEFECT (index/slot family, caught pre-report): the first run contracted h_a with slot 1,
comparing the family with slots EXCHANGED -- Xsw failed membership as an artifact and
'Ward MISMATCH' appeared. Diagnosed BY HAND against the flat r-covector before reporting
the anomaly as a finding; fixed on the artifact face; corrected run clean at both samples.

THE LICENSING HIERARCHY IS NOW COMPLETE AND FULLY COMPUTED:
    21 --(gauge/orbit)--> 11 --(Lorentz/boost covariance: 8 structures, 2 vector
    COMPUTED-BY-ORTHOGONALITY + 6 scalar COMPUTED-BY-MEMBERSHIP)--> 3
    --(S7/closure, by regime)--> 2

OWNER RULING NOW UNBLOCKED per the standing refinement: the boost-covariance license is
priced against a COMPUTED list of 8. Book it with scope and price, or accept the
11-dimensional FRW family with GRUT's restriction constitutive at a third point.
After the ruling: closure-premise test on the actual 3D family, then the kinematic story
closes and only Sigma_R^TT remains.

### 2026-08-24 · OWNER RULING (PENDING second-author review) — boost/Lorentz covariance IS a genuine additional license, to be booked +1

Grounds: measured, not preferred -- the FRW gauge-allowed space is 11-dimensional; the
Lorentz-covariant flat-compatible subspace is 3-dimensional; the width of 8 is established
by explicit computation (2 orthogonality + 6 membership), not subtraction.

**THE SCOPE, verbatim (must not drift):** "The priced assumption is not 'the background is
Lorentz invariant.' It is that the vacuum response kernel itself belongs to the
Lorentz-covariant subspace identified by the flat-limit membership test." The background on
FRW is not globally Lorentz invariant; the assumption is about the KERNEL.

FINAL ARCHITECTURE: 21 (full FRW bilinear) -> 11 (gauge) -> 3 (Lorentz-covariant response,
+1 if booked) -> 2 (S7/closure, regime-dependent) -> c0 = 0 still UNLICENSED on top.

GATE BEFORE RULING: second-author review of the three kernel files. The docstring item is
ALREADY DISCHARGED BY RECOMPUTATION (9c1016b), per the owner's instruction that it be
corrected by computation, not wording.

BANKING PRE-FLIGHT (anticipated, not discovered): booking the +1 moves net +16 -> +17.
Same one-commit sequence as Ruling B: register edit + update every standing-doc site
asserting net +16 (the 12 sites updated at the last banking) + re-run emit_public_numbers /
emit_gate_status / emit_audit_matrix / expected_red. Expect stale-net live cases to return
to the pre-existing backlog count, and DO NOT add new drift to DECLARED.

THE NEXT SUBSTANTIVE QUESTION, owner's words: does the actual gravitational self-energy
place the vacuum response inside the 3D Lorentz-compatible subspace, and then inside the
2D closure family? -- the direct bridge from kinematic architecture to microscopic physics.

### 2026-08-24 · Ox · SECOND-AUTHOR REVIEW OF THE KERNEL FILES: COUNTERSIGNED (E1-E7 all pass)

Instrument `second_author_kernel_gate.py`, expectations registered in-header before running,
calibration on knowns first. Independent unknown-ordering + sympy rank reproduces 21/11/6;
orbit rows re-derived symbolically match; orthogonality exact at the reviewer's own k;
T bijection round-trips; slot coherence PROVEN via pull(slot-exchanged Xsw) = pull(Xsw)^T
(Xsw's asymmetry makes it the discriminating test); third sample (omega,k)=(7,3) reproduces
intersection=2 / 6 boost-killed / plants / Ward-identification; original gate marked
derivation-sketch. REVIEWER SELF-CATCH disclosed: H treated as a constant symbol dropped
the H'alpha term and flagged two spurious mismatches against a CORRECT file -- diagnosed
by the mismatch pattern before any report. Fourth catch by the calibration template, and
the first that saved the reviewer from shipping a wrong break.

THE RULING GATE OF ac65652 IS DISCHARGED. The boost/Lorentz-covariance ruling is unblocked
on a fully computed, countersigned list. Banking (+1, net +16 -> +17) is STAGED under the
recorded pre-flight and executes on the owner's explicit go.


### 2026-08-24 · Claude · BANKING EXECUTED ON OWNER GO: boost/Lorentz-covariance +1, net +16 -> +17

Owner's go received verbatim: "Go. Book the boost/Lorentz-covariance ruling at +1, taking the
net from +16 to +17." Scope as ruled: the priced assumption is NOT "the background is Lorentz
invariant" -- it is that the vacuum response kernel itself belongs to the Lorentz-covariant
subspace identified by the flat-limit membership test. Discharge: retire the +1 only if the
microscopic Sigma_R^TT calculation demonstrates the vacuum response lies in that 3-dimensional
Lorentz-covariant subspace without imposing it as an input.

ONE COMMIT, per the recorded pre-flight. Contents: claims.json node `response_lorentz_covariance`
(tier assumed, +1; register 73 nodes = 52 grut + 21 vacuum-cluster, validator PASS); 8 standing
docs' REGISTER-SYNC/TOTAL markers + STATE gloss + GLOSSARY denominator; emitters re-run
(PUBLIC_NUMBERS --check clean; AUDIT_MATRIX leads with its honest ERROR 71 != 73 -- the reality
audit predates the last two bookings and the mismatch stays visible until a re-run, by design);
EMERGENCE_CHAIN regenerated after its coverage guard REFUSED the unplaced node (the guard
working) -- placed OFF-CHAIN as a licensing fence on the kernel family, the genre of
passivity_channel_diagonal / x_no_pin_theorem, not a story stage; WHERE_IT_STOPS re-rendered;
figures rebuilt; doc_register_pins --accept run AFTER prose reconciliation (13 nodes, 5
artifacts) and disclosed here as the human-act step, executed under the owner's explicit go;
currency pins updated in test_resident / test_harness / test_auditor / test_physics_vocab with
register numbers REMOVED from test identifiers (durable fix for the pin-name defect class).

GATE VERDICT before commit: expected_red REAL_EXIT=0 -- "All 5 failing tests are declared, at
21 declared cases, each citing an OPEN pass. No new red." The banking surfaced NINE undeclared
reds along the way (three currency pins + six generated-artifact/pin tests); all were register
currency, none physics. W-0 fence intact: this books the PRICE of the assumption; every Wall-A
computation remains COMPUTED-AND-REPORTED, NOT BANKED.

NEXT (owner-directed): the closure-premise test starting from the ACTUAL 3D Lorentz-compatible
family {P^2, P^0s, X_sw} -- premises first, 2D only if licensed -- then Wall A's Sigma_R^TT.

### 2026-08-24 · Claude · BANKING EXECUTED ON OWNER GO: boost/Lorentz-covariance +1, net +16 -> +17

Owner's go received verbatim: "Go. Book the boost/Lorentz-covariance ruling at +1, taking the
net from +16 to +17." Scope as ruled: the priced assumption is NOT "the background is Lorentz
invariant" -- it is that the vacuum response kernel itself belongs to the Lorentz-covariant
subspace identified by the flat-limit membership test. Discharge: retire the +1 only if the
microscopic Sigma_R^TT calculation demonstrates the vacuum response lies in that 3-dimensional
Lorentz-covariant subspace without imposing it as an input.

ONE COMMIT, per the recorded pre-flight. Contents: claims.json node `response_lorentz_covariance`
(tier assumed, +1; register 73 nodes = 52 grut + 21 vacuum-cluster, validator PASS); 8 standing
docs REGISTER-SYNC/TOTAL markers + STATE gloss + GLOSSARY denominator; emitters re-run
(PUBLIC_NUMBERS --check clean; AUDIT_MATRIX leads with its honest ERROR 71 != 73 -- the reality
audit predates the last two bookings and the mismatch stays visible until a re-run, by design);
EMERGENCE_CHAIN regenerated after its coverage guard REFUSED the unplaced node (the guard
working) -- placed OFF-CHAIN as a licensing fence on the kernel family, the genre of
passivity_channel_diagonal / x_no_pin_theorem, not a story stage; WHERE_IT_STOPS re-rendered;
figures rebuilt; doc_register_pins --accept run AFTER prose reconciliation (13 nodes, 5
artifacts) and disclosed here as the human-act step, executed under the owner's explicit go;
currency pins updated in test_resident / test_harness / test_auditor / test_physics_vocab with
register numbers REMOVED from test identifiers (durable fix for the pin-name defect class).

GATE VERDICT before commit: expected_red REAL_EXIT=0 -- "All 5 failing tests are declared, at
21 declared cases, each citing an OPEN pass. No new red." The banking surfaced NINE undeclared
reds along the way (three currency pins + six generated-artifact/pin tests); all were register
currency, none physics. W-0 fence intact: this books the PRICE of the assumption; every Wall-A
computation remains COMPUTED-AND-REPORTED, NOT BANKED.

NEXT (owner-directed): the closure-premise test starting from the ACTUAL 3D Lorentz-compatible
family {P^2, P^0s, X_sw} -- premises first, 2D only if licensed -- then Wall A's Sigma_R^TT.

### 2026-08-24 · Claude · CLOSURE-PREMISE TEST COUNTERSIGNED WITH CORRECTIONS -- the 3->2 step is derived, regime-gated

SECOND-AUTHOR REVIEW of wall_a_closure_premises.py: my instrument
second_author_closure_premises.py (E1-E7 all PASS) plus four independent adversarial
verifiers (own conventions/orderings, fresh sample (9,4), 4-level degenerate system,
fully symbolic operators; all prompted to refute). VERDICT: NOT REFUTED on all four
load-bearing steps. Ox's run reproduced byte-identical before any review edit.

THE RESULT STANDS: c=0 DERIVED at equilibrium (reciprocity; partner X_ws Ward-forbidden),
COROLLARY in the FDT-locked family, ABSENT in genuine non-equilibrium (family stays 3D).
Chain = three mechanisms, never one: 21 -(gauge)-> 11 -(Lorentz-covariant response, +1
booked)-> 3 -(equilibrium reciprocity/KMS)-> 2.

CORRECTIONS I APPLIED TO THE BUILDER'S FILES (per the build-and-disclose arrangement;
none changes the c=0 conclusion):
  1. MECHANISM: "h_mn is T-even" and "structures even in k" both FALSE as stated (h_0i is
     T-odd; 72 sign-flipping components). True mechanism = eps-signature cancellation,
     computed at 0/256 violations per structure (E1/E2). Registry + prose amended.
  2. MECHANISM: gyrotropic closure re-grounded as PARTNER-EXCLUSION (partner is the
     DIFFERENT Ward-dead structure X_ws, not minus itself) -- STRONGER than the
     epsilon-mediation/no-T-odd-object argument, robust to T-odd scalar backgrounds
     (FRW's H IS T-odd; the registry line was flat-scope only). Reachability re-proven
     in the actual tensor space: enlarged family retains the odd Hall mode (E4).
  3. GATES (a defect CLASS, three instances): todd_antisym predicate inverted AND ungated
     (defects cancelled; shipped verdict unaffected); pc_kills a hardcoded literal
     (tautological gate) -> now derived from the conserved-domain computation; T-even =>
     slot-symmetry bridge printed but ungated -> gated. New scope gate: assembled plant
     kernels verified r-slot Ward-allowed (slot_sym alone passes Ward-forbidden
     symmetric additions).
  4. REGIME-TABLE PRECISION: FDT-locked row now NAMES what KMS does not supply (T-even
     couplings/no T-odd background -- Gibbs + T-odd operator keeps the Hall branch) and
     what it genuinely adds (state=f(H) across degeneracies kills the static w=0 Hall
     line 28*I*pi*(p1-p2)/3 -- verifier-exhibited on a degenerate 4-level system).
  5. VERIFIER-CLOSED ESCAPE: two-field passivity forms DO see the antisymmetric part of
     X_sw, but all c-channel bilinears vanish exactly when both fields are conserved
     (P2 channel nonzero on the same pair) -- conserved-domain blindness is real.

Amended instrument re-runs exit 0, verdict text unchanged. Zero confirmed physics
errors; every defect was instrument/wording currency. W-0: computed-and-reported,
NOT banked. NEXT: Wall A proper -- Sigma_R^TT under G0-G3, with the sharpening this
test adds: the microscopic calculation must establish the 3D placement AND the
equilibrium regime in which the last 3->2 reduction holds.

### 2026-08-24 · Owner ruling · WALL A OPENS AT A1 -- vertex object sharpened, full-then-project mandated

Owner ratifies the A1 opening as structured, with three rules re-emphasised (object
registry before algebra; flat-limit + mis-indexed plants before the de Sitter vertex is
trusted; STOP at A1 -- no silent renormalisation or spectral choices that belong to
A3/G3) and ONE MODIFICATION, verbatim intent: the A1 deliverable must be stated
explicitly as the FULL vertex Gamma^{mu nu}_{ab}(x; y, z), with TT projection a
DOWNSTREAM operation. Mandated sequence:
    S_interaction -> Gamma^{mu nu} -> Gamma^TT -> Sigma_R^TT
never S_interaction -> Gamma^TT by assumption -- "otherwise there is a risk of deleting
longitudinal/scalar structures before the assembly has had a chance to determine whether
they matter." (Checker's note: early TT projection would also partially IMPOSE placement
(i), corrupting the +1 discharge test itself.)

Status boxed by the owner: A2/Bardeen/closure kinematics CLOSED; A1 vertex NEXT;
Sigma_R^TT still uncomputed. The registered experiment: "When the microscopic
gravitational vertex is actually assembled, what response structure does the theory
produce before any GRUT target is imposed?"

### 2026-08-24 · Claude · A1 VERTEX COUNTERSIGNED WITH CORRECTIONS -- the wall's first stage stands

SECOND-AUTHOR REVIEW of wall_a_a1_vertex.py: reproduced byte-identical, then
second_author_a1_vertex.py (E1-E5 all PASS) + independent verifier fleet (from-scratch
routes disjoint at every stage: Leibniz-sum determinant, multiplication-verified Neumann
inverse, two-plane-wave extraction, two-distinct-fields normalisation regulator).
VERDICT: NOT REFUTED. The vertex Gamma^{mu nu} = (kappa a^2/2)[p q + q p - eta(p.q + a^2 m^2)],
both discards, the a^2-vs-a^4 channel split, and the normalisation chain all confirmed.

THE REVIEW'S PHYSICS ADDITION: the GENUINE gauge-orbit reconciliation, FRW layer included.
The orbit from Lie_xi g carries the conformal 2(a'/a)xi^0 eta_mn term; the vertex's
variation reduces IDENTICALLY to (bath EoM with friction) x (xi.dphi) + total derivative,
arbitrary phi/xi/a(eta). No residual -- no obstruction for the loop stage. The constant-H
trap exhibited as negative control. (The builder file's own 'recon' gate turned out to
DUPLICATE its Ward gate -- the "checker's lever closes" line in the builder report was an
independence overclaim, struck-and-replaced in the STAGE doc; content was never missing:
Gamma.(K xi + xi K) == 2 xi.(K.Gamma) algebraically.)

CORRECTIONS APPLIED TO THE BUILDER'S FILES (build-and-disclose; none touches the vertex):
chk_det gate had verified only the O(kappa^0) term while claiming the O(kappa) check --
on the very det-check the file's own lesson calls blind; now compared to h_tr and gated.
The MISSING recomposition gate (second-author target 5 had no gate) added at review:
Gamma exactly recoverable from (Gamma^TT, trace, longitudinal); discards parameterise ALL
non-TT content, no third structure. Flat-plant sign degeneracy recorded (harmless: two
insertions in Sigma).

REVIEWER SELF-CATCH (the recurring pattern, now on the checker's side): review
instrument's first draft spuriously eta-raised the extracted vertex -- the h01-symbol
coefficient already IS the lower-index component Gamma contracts; only 0i components
flipped, caught by my own E2 gate, diagnosed before reporting. Target file never
implicated. DISCLOSURE: two fleet verifiers died on a subagent session limit; their
targets covered by E1/E4/E5 + the completed derivation verifier. Zero confirmed physics
errors in A1 on either side. W-0: computed-and-reported, NOT banked.

NEXT: A3 declarations (renormalisation scheme; bath-state computed-vs-assumed; G0
spectral wiring) -- then the loop assembles and Sigma_R^TT gets asked the three-part
wall question.

### 2026-08-25 · Owner ruling · A3 CONFIRMED AS NEXT, three additions, two-step freeze

Owner ratifies the A3 brief with additions, verbatim principles:
  1. RENORMALISATION REGISTRY SPLIT: Pi_ren = Pi_local^scheme + Pi_nonlocal^invariant,
     with each of the three wall questions marked for which part it is sensitive to.
     THE CRITICAL PRINCIPLE: "No finite local counterterm may be selected because it
     produces a preferred spectral or memory behavior." Two admissible schemes differing
     only by local polynomial terms -> their agreement/disagreement in the NONLOCAL
     low-frequency analytic structure IS the robustness test. A3 must not become a
     mechanism for manufacturing the desired K_R.
  2. BD != EQUILIBRIUM RESPONSE: A3 distinguishes STATE SPECIFICATION from the
     KMS/detailed-balance PROPERTY OF THE INTERACTING RESPONSE -- the latter is a
     loop/closure-stage question. The closure test established equilibrium/KMS => 3->2
     while genuine non-equilibrium leaves 3D; A3 must not pre-answer question (ii).
  3. SPECTRAL WIRING ENFORCED BY CODE, NOT PROSE: the direction
     "registered J(omega) -> Sigma_R construction" must be made IMPOSSIBLE by the
     registry/assembly mechanism. Correct direction: BD mode functions + declared
     interactions -> loop -> Sigma_R/K_R/Im chi -> compare AFTERWARD with registered
     J(omega). The registered spectrum is the benchmark under test, not an ingredient.
  4. SEQUENCING: A3 declarations -> A4 dual gauge -> Sigma_R^TT. The gauge-comparison
     protocol is FROZEN AT A3 TIME -- the second gauge must not first appear at the loop,
     and its protocol cannot be redesigned after seeing the first-gauge answer.
  5. TWO-STEP FREEZE: Ox drafts the declaration; the checker reviews it BEFORE it is
     hash-frozen -- "the last clean opportunity to catch a hidden input before the
     one-loop physics begins."

Status boxed by the owner: A1 COUNTERSIGNED; A2/Bardeen/kinematics COUNTERSIGNED;
A5 FULL PASS; A3 NEXT; Sigma_R^TT untouched. The crisp target:
Sigma_R^TT ?in K_3D^Lorentz ?in K_2D^closure, plus its IR analytic structure.

### 2026-08-25 · Claude · A3 FREEZE-GATE REVIEW EXECUTED: SEVEN FINDINGS, ALL PATCHED, THEN FROZEN

The two-step freeze ran as the owner mandated. The attack plan in the draft's own
second_author_targets was executed; SEVEN findings, three load-bearing, all patched in
place with CHECKER-AMENDED/-ADDED/-CORRECTED markers before hashing:

  F1 (LOAD-BEARING) split predicate wrong VARIABLES: "polynomial in (w^2,k^2,m^2,H^2)"
     would misclassify legitimate dimreg local coefficients carrying log(m^2/mu^2) as
     nonlocal (and omitted mu entirely). Corrected: polynomial in (w^2,k^2) -- the
     derivative structure -- with coefficients arbitrary FINITE functions of (m^2,H^2,mu).
     Hostile cases (w^2 log k^2, w^4/k^2) stay nonlocal under the corrected predicate.
  F2 (LOAD-BEARING) renormalisation CONDITIONS missing: D1 cited "conditions declared in
     1b" but 1b held only the operator basis -- the finite parts of six coefficients were
     an undeclared fork. MINIMAL SUBTRACTION declared (pole-only, mu symbolic, zero
     finite-part discretion -- the unique choice completing the owner's critical
     principle). DISCLOSED AS CHECKER-ADDED: owner may order a v2 before assembly.
  F3 (LOAD-BEARING) A4 second-gauge spec internally inconsistent: the residual condition
     d_0(h_0i/a^2)=0 conditioned a component synchronous gauge sets IDENTICALLY to zero.
     Corrected to the genuine residual (xi^0 = C(x)/a + time-independent spatial reparam,
     fixed asymptotically at eta -> -infty). Also corrected: A1 fixed NO gauge -- the A4
     comparison is unfixed-vs-synchronous, not de Donder-vs-synchronous.
  F4 blind gaps closed: Q5 (flat-limit reduction, per-channel, with IR-obstruction
     branch) ADDED -- the +1's discharge condition is a flat-subspace statement and the
     draft had no flat-limit quantity; Q1b X_sw parity sub-record; Q3 intermediate class
     1<s<2; THE +1 DISCHARGE MAP pre-registered (dischargeable ONLY by Q1 INSIDE and Q5
     INSIDE; Q3/Q4 do not vote; discharge itself stays an owner ruling).
  F5 barred-guard leaks: wall_a_g1_ohmic_plant.py -- which carries the registered
     J(omega) EXPLICITLY -- was absent from the barred list (also kk_dos_signchange_probe,
     the G1/rung7/priority result JSONs, and MICROSCOPIC_TARGET_BENCHMARK.md, whose
     construction-stage read would un-blind Q3). List extended to 9 entries; guard
     hardened: TRANSITIVE import scan (sys.modules), CONTENT-HASH barring (12 files
     sha256'd into the registry), NUMERIC-FINGERPRINT audit (no spectral-shape literals;
     every constant cites a registry entry).
  F6 Q4 predicate pinned to the PROPER Onsager-Casimir test of the countersigned closure
     instrument (eps-signature-corrected, H T-odd) -- the naive slot-symmetry trap the
     closure review exhibited is barred by name.
  F7 scheme dS-invariance non-citation clause: the regulator's symmetry may not be cited
     in the (i) placement verdict -- it avoids introducing breaking, it does not
     demonstrate unimposed placement.

FROZEN 2026-08-25. The freeze hashes (recorded here because a hash cannot live inside
the file it hashes):
  WALL_A_A3_DECLARATIONS.md  sha256 = 87e2d24d5be6d67970f4089a09aa61a28d4de8cf6471f987af3db1c2ac015f6e
  WALL_A_A3_REGISTRY.json    sha256 = faa977d40f1ba31836e35b18223c1f573559b49649a84fad237a3809aae59b55
Both files are IMMUTABLE; any change requires a superseding v2 citing this one. Results
cite the declaration; never the reverse. NEXT: A4 dual-gauge under the frozen protocol,
then Sigma_R^TT assembly under the frozen registry.

### 2026-08-25 · Claude · A4 CLOSED: built by checker, countersigned by Ox, REFUTED-AND-FIXED by the fleet -- and one frozen clause superseded

THE FULL CHAIN, recorded as it happened: (1) Ox stalled; on the owner's directive the
CHECKER BUILT A4 (build-and-disclose). (2) Ox returned, independently executed the
instrument (all 11 gates, guard live-clean) and COUNTERSIGNED with scope stated,
carrying three findings (spatial STF coefficient 1/2 not 1/3 -- checker cross-confirmed
by idempotence, 0 vs 81 violations; THREE non-TT discard channels in the spatial slice;
guard fail-closed self-reference). (3) The two-verifier fleet then landed:
V2 (guard/slice/TT/plants) NOT REFUTED -- the guard genuinely kills a real barred
import on a modified copy; V1 (transformation/identity) **REFUTED the residual-family
claim**: the instrument's zeta_i conjunct was a HARD-CODED TRUE (print-statement fact,
in the checker's own code), and the skipped substitution shows the frozen F3 product
family {C(x)/a} x {time-independent C_i} is WRONG -- preserving h_0i = 0 forces
zeta_i = C_i(x) - (d_i C) Ia(eta), Ia' = 1/a, a mandatory time-dependent C-coupled
piece. V1 simultaneously CONFIRMED the invariance identity from an independent
diffeo-invariance derivation (plus a wrong-V negative control the instrument lacked)
and bounded the damage: steps 4-5 hold for ARBITRARY zeta, so A4's gauge-invariant-
content conclusion is untouched; the post-prescription residual statement stands.

FIXES: instrument corrected to COMPUTE what it asserted (gates g3b/g3c: true family
preserves both conditions; refuted product family demonstrably exits the gauge);
re-runs exit 0. The frozen F3 clause is superseded by the v2 amendment (the frozen
files are NOT edited -- the amendment path the freeze protocol mandates):
  WALL_A_A3_DECLARATIONS_V2_AMENDMENT.md  sha256 = 6f2a762f4a4a01cd4794d029eecb2f1aadace9cd52637f12d3529e0564ce3d53
Scope: exactly one clause; every other frozen declaration stands un-reopened.

OPERATIONAL FINDING (Ox's, adopted as protocol): the checker's A4 build SILENTLY
OVERWROTE Ox's in-flight file -- two agents built in the same path and the later write
won. PROTOCOL AMENDMENT, effective now: claim-before-edit applies to FILES not just
tasks -- an agent claims the exact paths it will write in this log BEFORE writing, and
any agent resuming work re-reads disk state first (file-freshness check). Ox's call to
abandon its diverged copy and verify the disk instrument instead was correct.

A4 VERDICT STANDS: synchronous reproduces the gauge-invariant content of the unfixed
computation; Sigma_R^TT assembly UNBLOCKED under the frozen protocol (+ v2 amendment).
Assembly-stage standing context: spatial STF = 1/2; three non-TT discard channels;
Q4 = proper Onsager-Casimir; the response-level Pi_nonlocal dual-gauge equality re-runs
at assembly. W-0: computed-and-reported, NOT banked.

### 2026-08-25 · Claude · A4 CLOSED: built by checker, countersigned by Ox, REFUTED-AND-FIXED by the fleet -- and one frozen clause superseded

THE FULL CHAIN, recorded as it happened: (1) Ox stalled; on the owner's directive the
CHECKER BUILT A4 (build-and-disclose). (2) Ox returned, independently executed the
instrument (all 11 gates, guard live-clean) and COUNTERSIGNED with scope stated,
carrying three findings (spatial STF coefficient 1/2 not 1/3 -- checker cross-confirmed
by idempotence, 0 vs 81 violations; THREE non-TT discard channels in the spatial slice;
guard fail-closed self-reference). (3) The two-verifier fleet then landed:
V2 (guard/slice/TT/plants) NOT REFUTED -- the guard genuinely kills a real barred
import on a modified copy; V1 (transformation/identity) REFUTED the residual-family
claim: the instrument's zeta_i conjunct was a HARD-CODED TRUE (print-statement fact,
in the checker's own code), and the skipped substitution shows the frozen F3 product
family {C(x)/a} x {time-independent C_i} is WRONG -- preserving h_0i = 0 forces
zeta_i = C_i(x) - (d_i C) Ia(eta), Ia' = 1/a, a mandatory time-dependent C-coupled
piece. V1 simultaneously CONFIRMED the invariance identity from an independent
diffeo-invariance derivation (plus a wrong-V negative control the instrument lacked)
and bounded the damage: steps 4-5 hold for ARBITRARY zeta, so A4's gauge-invariant-
content conclusion is untouched; the post-prescription residual statement stands.

FIXES: instrument corrected to COMPUTE what it asserted (gates g3b/g3c: true family
preserves both conditions; refuted product family demonstrably exits the gauge);
re-runs exit 0. The frozen F3 clause is superseded by the v2 amendment (the frozen
files are NOT edited -- the amendment path the freeze protocol mandates):
  WALL_A_A3_DECLARATIONS_V2_AMENDMENT.md  sha256 = 6f2a762f4a4a01cd4794d029eecb2f1aadace9cd52637f12d3529e0564ce3d53
Scope: exactly one clause; every other frozen declaration stands un-reopened.

OPERATIONAL FINDING (Ox's, adopted as protocol): the checker's A4 build SILENTLY
OVERWROTE Ox's in-flight file -- two agents built in the same path and the later write
won. PROTOCOL AMENDMENT, effective now: claim-before-edit applies to FILES not just
tasks -- an agent claims the exact paths it will write in this log BEFORE writing, and
any agent resuming work re-reads disk state first (file-freshness check). Ox's call to
abandon its diverged copy and verify the disk instrument instead was correct.

A4 VERDICT STANDS: synchronous reproduces the gauge-invariant content of the unfixed
computation; Sigma_R^TT assembly UNBLOCKED under the frozen protocol (+ v2 amendment).
Assembly-stage standing context: spatial STF = 1/2; three non-TT discard channels;
Q4 = proper Onsager-Casimir; the response-level Pi_nonlocal dual-gauge equality re-runs
at assembly. W-0: computed-and-reported, NOT banked.

### 2026-08-25 · Owner ruling · ASSEMBLY-1 ACCEPTANCE GATES; nothing else moves

Baseline confirmed: 73 nodes / net +17 after the Lorentz-covariance booking. The ONLY
next action: file claim -> ASSEMBLY-1. No architecture changes, no phenomenology, no
reopening of frozen declarations unless ASSEMBLY-1 exposes a defect genuinely requiring
a superseding amendment.

ASSEMBLY-1 must prove, in order, before ANYTHING downstream runs:
  1. object registry loaded first; barred-inputs guard LIVE;
  2. Gamma_a -> Sigma_CTP -> Sigma_R (the CTP-to-retarded assembly itself);
  3. RETARDED CAUSALITY independently established;
  4. H -> 0, a -> 1 FLAT-LOOP RECOVERY;
  5. tensor decomposition preserves the FULL structure including non-TT pieces --
     no silent projection.
Only after these pass: renormalisation stage -> Q1-Q5 verdicts -> comparison with the
registered J(omega), which remains STRICTLY DOWNSTREAM: microscopic result first,
registered spectrum second.

Owner's closing, operative: "The next thing that changes the scientific status of the
project should be the actual one-loop gravitational response, not another governance
artifact."
