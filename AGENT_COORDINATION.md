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

