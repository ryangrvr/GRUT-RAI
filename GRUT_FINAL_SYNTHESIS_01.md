# GRUT_FINAL_SYNTHESIS_01 — what the program actually discovered

**Status: the final physics synthesis, produced on the owner's charter** (*"the
goal is not to prove GRUT; the goal is to determine what the program actually
discovered"*) **after the keystone ruling of 2026-09-21** (T3-08A accepted as
endpoint; keystone BANKED; PV/Re Σ named future work). **Governing rule:**
*GRUT is the name given to whatever coherent physical account survives the
investigation.*

**Provenance.** This document synthesizes two frozen bodies of evidence and
adds nothing to either: (1) the Stage A baseline `GRUT_REALITY_BASELINE_01`
(GRUT-RAI branch v4, commit `5bdda88`, registry sha256
`dc693eb6fa664c6fa89ed2f94577d9a99431c8ea462127f38d8c32ea906436a9` — re-fetched
from the remote and re-verified byte-identical at this document's writing),
covering the program through 2026-09-16 with categories A(13)/B(23)/C(36)/
D(22)/E(22)/F(19)/G(11)/H(0), a 13-item A.1 core, and 17 recorded absences;
and (2) the banked T3 chain in this repository (`calc/`, commits `fbaeec9`,
`12eded2`, `4e85822`, `e229908` + the owner-ruling file), covering 2026-09-19
through 2026-09-21. Owner rulings are tagged as such. Every number below is
mechanically verified against its source artifact before commit.

---

## 0. The answer in one paragraph

The program set out to determine whether GRUT — the responsive-vacuum,
finite-memory picture of gravitation — could be established from its own
calculations. Under hostile internal auditing it could not: the frozen baseline
concludes, verbatim, *"What GRUT has actually established is a set of
in-house-verified standard calculations on declared inputs, a partly-verified
set of negatives about its own framework, and an audit discipline — not a
physics result that distinguishes it from standard QFT/GR plus open-system
EFT."* What the final campaign then discovered, by pushing the deepest of
those standard calculations to its endpoint, is a genuinely sharp piece of
physics: **the one-loop graviton self-energy on de Sitter space carries a fully
certified absorptive response through H⁶ that is not representable by the
tested class of stationary amplitude/frequency dressings — and its structure
separates two things the original hypothesis had fused: cosmic-time dependence
and memory are not the same thing.** The u_b-dependent (nonstationary)
structure is confined, through H⁶, to *local* terms — the response remembers
the expanding background through a time-dependent local dressing of the wave
operator — while the first genuine *nonlocal* memory contribution (the ω⁻²
term at H⁶) is u_b-independent: stationary. This characterizes graviton-loop
dissipation on an expanding background concretely, and it does not by itself
distinguish GRUT from standard QFT on de Sitter.

---

## 1. ESTABLISHED (demonstrated computationally or analytically, gate-certified)

**1a. The certified absorptive response through H⁶** (the deepest computed
object of the program; T3 chain, custody: K2 partition closure → T3-05L
extraction completeness → T3-05G provenance → T3-07 sector extractions with an
exact A2-reproduction gate). With x = H·u_b, y = H/ω, valid ω ≳ 3.4H:

Im Σ_R(ω>0) = (ω⁴/1280π) · P(x, y), where

| order | contribution to P | status |
|---|---|---|
| H⁰ | −3 | complete; three routes agree |
| H¹ | 0 | complete — vanishes exactly |
| H² | −(104/3)y² | complete; u_b-free |
| H³ | +24x³ − (472/3)xy² | complete — first u_b-odd (time-asymmetric) term |
| H⁴ | −18x⁴ + 220x²y² − 127y⁴ | complete |
| H⁵ | (416/3)x³y² − 496xy⁴ | **δ-class only — PV leak; QUARANTINED, never binding** |
| H⁶ | −48x⁶ + (3448/3)x⁴y² − 3312x²y⁴ − (1280/3)y⁶ | complete — first negative ω power |

Sources: `calc/T3_07_H6_EXTRACTION_RESULT.json`, `calc/T3_05_H4_SECTOR_RESULT.json`,
baseline category C (the H⁰/H² record). H⁷/H⁸ exist in the theory (object
degree 8) and remain outside the certificate (builder-truncated; owner: run
only with a physics question attached).

**1b. The stationary dressed representation is refuted at H⁶** (`calc/
T3_07B_SLOT_CERTIFICATE_RESULT.json`). For any Im Σ = F(x)·(ω̃⁴/1280π)·T(H/ω̃)
with ω̃ = ω·g(x) — containing amplitude-only, redshift-only, and combined
dressings — the slot chain fixes every parameter from data (t = −3, −104/3,
−127, −1280/3; f₁ = 118/13, g₁ = −59/26 pinned by the *measured* H¹/H³
content; f₂ = 1336/169), and the then-parameter-free x²y⁴ slot requires
−169672/169 ≈ −1004 against the complete H⁶ datum −3312. Parameter-free,
single-witness, on complete data only.

**1c. The two-time response is assembled and characterized** (keystone T3-08A
under the ratified frozen protocol, sha `caaf7a70…`; outcome
`TWO_TIME_RESPONSE_CHARACTERIZED`, accepted by owner ruling). The exact
structural finding: **every u_b-dependent monomial of the certified response
sits at ω-powers {4, 2, 0} — local (contact/higher-derivative) terms — while
the sole genuine nonlocal memory term (ω⁻², H⁶) is u_b-free**, IR-cut at the
record's own refusal boundary ω\* = √(104/9)·H = 3.399H.

**1d. The Wigner-local approximation is quantitatively bounded** (same
instrument). Error field E = (H/ω)|∂ₓP|/|P|: maximum ≈ 0.33 on the tested
inner domain (ω ≥ 5H, |Hu_b| ≤ 0.3), ≈ 1.68 at the 3H edge, dominated by the
certified u_b-odd H³ term. Owner's formulation, binding: *"On the tested inner
domain, the Wigner-local reduction carries an error reaching approximately
33%, and therefore is not certified as a controlled reduction under the
preregistered 20% criterion."*

**1e. Supporting exact results.** Dissipative sign throughout the
self-consistent window (exact maximum of the ≤H⁴ object −599127/270400 < 0;
grid-negative with H³/H⁶ included; `calc/T3_06B_KEYSTONE_STATUS_RESULT.json`);
the secular self-termination x\* = 6^(−1/4) at y = 0; the derived validity
boundary ε_H = (104/9)H²/ω² with its refusal at ω = 3.4H; and the baseline's
category A (13 entries): in-house-verified standard calculations on declared
inputs, including the standard-physics controls carrying zero GRUT content.

**Scope stamp on all of 1a–1e:** these are results of standard QFT on de
Sitter under the declared Tier-3 contract, computed and certified in-house.
None is a GRUT discriminator.

## 2. DERIVED, CONDITIONAL ON STATED ASSUMPTIONS

Everything in §1a–1d is conditional on the declared contract: TT bath
(uniqueness explicitly not claimed — D3(iii)), Option-B adiabatic modes, the
k_ext → 0 controlled limit, dimensional continuation with no explicit IR
scale, the patch-local quotient declared with R′ UNRESOLVED, and the single
assumed time-translation flow the baseline identifies under its entire ledger.
The baseline's conditional theorems stand at their recorded scope: the
ξ-covariant two-time form theorem on exact dS with its ω_T = ω_cosmic bridge;
the D4/KTERM identities at consequence scope (not general-gauge uniqueness);
the relaxational-class no-crossing of w = −1 (a genuine class constraint: a
data-demanded crossing would exclude the whole relaxational kernel class,
GRUT's included).

## 3. EFFECTIVE / RECONSTRUCTED

The responsive-vacuum *form* is standard open-system EFT — the baseline's
recorded verdict: *"the universal FORM = standard open-system EFT, NOT
GRUT-specific."* Dissipation, noise, and memory-kernel structure are EFFECTIVE
via Mori–Zwanzig (derivable from closed system + coarse-graining; fundamental
status unsupported). Standard open-system facts were reproduced with zero GRUT
input: reduced-state decoherence with global purity preserved, branch-weight
inheritance, recoherence. The free static-patch TT results are null-not-
adverse; the a/c sector-split identities are exact flat-space facts.

## 4. FAILED / RULED OUT (results of the program, not unfinished business)

From the T3 chain: every stationary amplitude/frequency dressing of the dS
graviton response (§1b). From the baseline's 22 category-E closures, the
principal ones: the symmetry route to forced pure-TT (closed); α = a/c as an
anchor (settled-negative — a ratio of coefficients in different channels);
Γ_T as a discriminator (computed 62.7 orders below the shared-slot bound); GW
dissipation as a differentiator (invisible-by-suppression, 21–62 orders below
LIGO); the 689 Hz parameter-free falsifier and its BMV backup (retired/
withdrawn); any GRUT-internal kernel-selection principle (every alternative
excluded by an input, never by a principle); the registered s = 3 spectral
family at flat contract scope (s = 5 found); Λ_R via its zero (withdrawn — a
reparameterization is not emergence); τ₂ ~ 1/H₀ as derived (it is inserted);
the conformalon; memory as the mechanism of single-particle interference;
every sharp IR completion tested (covariance, KMS strip-analyticity,
positivity, exact flat limit); and — decisive for the foundations arm —
**decoherence is not outcome selection** within the branch-preserving unitary
class, the tested closed-unitary/coarse-graining route did **not** derive the
Born weights, and **ħ remained an irreducible input**. The baseline flags
three negatives MUST-BE-REOPENED (the ROOT-1 battery's hard-coded gate, the
composite no-pole negative, the tt_worldline decay) — ruled-out status there
is only as strong as its flag.

## 5. UNRESOLVED (the calculation genuinely not completed)

Re Σ_R / the PV machinery (owner: explicitly named future work — it answers
*whether the u_b-dependent local coefficients survive renormalization/field
redefinition*, a different question from what §1 establishes); the H⁵ PV
completion; the deep-IR / ω ≲ H completion (K_R is unevaluated at its own
claim point — not nulled there); the transport class at ω → 0
(frontier-reserved by the record; decided by bath internal dynamics absent
from any one-loop object); H⁷/H⁸; the R′ missing declaration (the boundary/
growth/observable class at spatial infinity — candidates priced, owner's
desk); the smooth-window S5/S7 test (specified, licensed, unexecuted); the
single-pole hypothesis (UNRESOLVED — neither derived nor refuted, with the
recorded W-0 tension unreconciled); the Wall-C in-in/retarded equivalence at
O(H); the gauge-invariant Tier-3 target (spec drafted, unratified). The
baseline's A.1 core stands: of its 13 items, **nothing is ESTABLISHED or
DERIVED** — the responsive medium and microscopic bath are HYPOTHESIS, the
formal apparatus IMPORTED, dissipation/noise EFFECTIVE, the deep questions
UNRESOLVED.

## 6. OPEN PHYSICS (the short list worth pursuing)

1. **The local/memory split** (§1c) — is the time-dependent local dressing
   physical after renormalization? (= the Re Σ/PV program.)
2. **The stationary memory tail's fate at ω → 0** — the deep-IR completion,
   where the u_b-free ω⁻² term and the series' own convergence boundary
   (≈ 1.8H by three-term ratio, suggestive only) point.
3. **The stationarity↔homogeneity trade at H ≠ 0** — the program's central
   structural finding, now carrying exact coefficients through H⁶.
4. Whether *any* consistent IR completion exists (the smooth-window class,
   every sharp one being dead).
5. The gravity–quantum interface as the baseline leaves it: emergent-vs-
   fundamental UNRESOLVED; outcome selection and ħ untouched by everything
   tried.

## 7. PREDICTIONS

**EMPTY.** The Γ_T prediction gate is unmet; the register's PREDICTED class is
empty; no quantitative, non-post-fit, GRUT-vs-standard discriminating effect
survived any gate. The one surviving quantitative wedge (the shape wedge) is
recorded as *a prediction of standard theory*. An honest empty ledger is the
result.

---

## 8. The GRUT interpretation, priced and placed

The responsive-vacuum picture is *consistent with* §1: an expanding background
carries time-dependent response structure that no tested stationary dressing
absorbs. But the calculation is standard QFT on dS; the interpretation adds an
ontology the record does not establish, and the baseline prices the full
stance at +16 net underived inputs with the 'derived' tier empty. What GRUT
now *names*, under the governing rule, is: the certified response
characterization (§1), the constraint set (§2, §4), the audit discipline that
produced them, and the short open-physics list (§6). The original fusion of
cosmic-time dependence with memory is refined by its own investigation into
the sharper statement of §0 — which is what a reality-directed program is for.

## 9. Record

Process disclosures carried with the chain: two refuted instrument premises
(conjugate-mirror; H-exactness), two defective error measures, one namespace
artifact, one i-convention port bug — each caught by predeclared gates or
adversarial reruns, each disclosed in its instrument and preserved in run
logs. The Stage A record additionally carries 30 quotation-audit corrections,
8 category contradictions resolved, 12 referee-undeterminable items, and the
standing note that no outside human has reviewed any of it. H⁵'s quarantine,
the ε_H refusal, and the frontier reservation on the transport class are
stamped wherever they bind. Nothing in this synthesis modifies Stage A
(immutable) or any banked artifact.

*Written 2026-09-21. Mechanically number-verified against the frozen baseline
(re-fetched from GRUT-RAI v4, sha re-verified) and the banked T3 artifacts
before commit; verification log committed alongside.*
