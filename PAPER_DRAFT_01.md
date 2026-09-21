# Wigner-time structure of one-loop graviton dissipation in de Sitter space: certified absorptive coefficients through sixth order in H and a no-go for stationary dressings

**D. Ryan Grover**

*Draft 01 — 2026-09-21. Built from the frozen evidence base (see §9); all
in-house verification, no external review yet (§7, item 9).*

---

## Abstract

We compute the Wigner-time-resolved absorptive part of the one-loop
pure-graviton self-energy on a de Sitter background, within a fully declared
contract (transverse-traceless internal legs, adiabatically dressed mode
functions, zero external spatial momentum, dimensional continuation), through
sixth order in the expansion rate H. With x = H·u_b (u_b the Wigner time) and
y = H/ω, the certified result is

> Im Σ_R(ω>0) = (ω⁴/1280π)·P(x, y),
> P = −3 − (104/3)y² + 24x³ − (472/3)xy² − 18x⁴ + 220x²y² − 127y⁴
>     − 48x⁶ + (3448/3)x⁴y² − 3312x²y⁴ − (1280/3)y⁶,

valid for ω ≳ 3.4H, with the H⁵ sector quarantined (extracted in its
delta-class only; see §7). The H¹ sector vanishes exactly; H³ supplies the
first u_b-odd (time-asymmetric) dissipative term. We establish, by a
parameter-free coefficient certificate, that no representation of the form
F(Hu_b)·(ω̃⁴/1280π)·T(H/ω̃) with ω̃ = ω·g(Hu_b) — encompassing all
time-dependent amplitude dressings, frequency rescalings, and their
combinations, equivalently the leading-adiabatic action of local field
rescalings and time reparametrizations — reproduces the certified
coefficients. Under the frozen retarded convention, and assuming the retarded
kernel is real at fixed u_b, the certified non-analytic absorptive terms
reconstruct for Δ > 0 as power-law memory tails; the u_b-dependent
contributions occur in the faster-decaying tails (Δ⁻⁵, Δ⁻³, Δ⁻¹), while the
deepest certified infrared contribution (ω⁻²) is u_b-independent at this
order. Local counterterms cannot alter the Δ > 0 content of this certified
non-analytic absorptive sector. No observable is claimed; the calculation is
a result of standard quantum field theory on de Sitter space.

---

## 1. Introduction

How does the dissipative response of the gravitational vacuum depend on
cosmic time? On a de Sitter background the question is sharp: the background
has no global timelike Killing vector adapted to the spatially flat slicing,
so a two-point response kernel Σ_R(t, t′) need not be a function of t − t′
alone. Whether — and in precisely what structural way — the one-loop graviton
self-energy departs from stationarity is a well-posed, computable question,
and this paper answers it at the level of the absorptive (imaginary,
dissipative) part, through sixth order in H, within a fully declared
calculational contract.

The result is presented in the order of its logical construction:
the calculation (§2); the certified absorptive structure (§3); the exact
Fourier/distributional mapping to relative-time memory structure, with its
single physical premise stated explicitly (§4); the representation test — a
no-go certificate for stationary dressings (§5); physical interpretation
(§6); limitations (§7); and what remains unresolved (§8). Section 9 records
provenance. This ordering is deliberate: every interpretive statement in §6
is downstream of a certificate or an exact mapping in §3–§5, and the
qualifications of §7 are part of the result, not caveats appended to it.

This work originated in a research program (GRUT) investigating a
"responsive-vacuum" interpretation of gravitation; the program's own audit
concluded that no result herein distinguishes that interpretation from
standard quantum field theory on de Sitter space (§6.4, §9). The calculation
and its certificates stand independently of any interpretation.

## 2. The calculation

The object is the retarded self-energy of the transverse-traceless (TT)
graviton on a de Sitter background of expansion rate H, at one loop in the
pure-gravity sector, under the following declared contract (all elements
frozen before computation; see §9 for the audit trail):

- **Internal legs:** the declared TT bath, ⟨hh⟩ = P^TT × W, with the
  Wightman kernels W± = (κ²/q)e^{∓iq(u−u′)}[(1−Hu)(1−Hu′) ± iH²(u−u′)/q +
  H²/q²] — the exact product of linearly dressed adiabatic modes,
  terminating at O(H²) per kernel. TT uniqueness is not claimed.
- **Vertex:** the cubic de Sitter vertex reduced to H-graded bilinear
  C-matrices on the spatial pair basis (maximum H-degree 2).
- **External kinematics:** frequency ω at zero external spatial momentum,
  reached as a controlled k → 0 limit (never the literal point), with an
  executed two-axis isotropy gate.
- **Radial sector:** dimensional continuation only, no explicit IR scale;
  angular averages at symbolic dimension d, with d → 3 taken term-by-term
  (smoothness verified at each order).
- **Retarded convention (frozen, quoted):** Σ_R = −iθ(Δ)·RET with
  Σ̃_R(ω) = ∫₀^∞ dΔ e^{+iωΔ} Σ_R(Δ) — the upper-half-plane-analytic
  transform. The absorptive part is extracted from the ω = +2q cone of the
  loop integrand by the Sokhotski delta class, with a reality gate (iⁿcₙ
  real) enforced per Δ-degree; for the present ω > 0 absorptive
  delta-class extraction the opposite cone has no support (its delta class
  lies at q = −ω/2, outside the measure domain; both cones carry independent
  content for the dispersive part — §8) — verified per degree, term by term.
- **Units:** κ = 1; all coefficients below are exact rationals over π.

The two-time structure is carried in Wigner variables: u_b = (u+u′)/2 (the
Wigner time) and Δ = u − u′, with the transform taken in Δ at fixed u_b. The
expansion is H-graded; the source object carries H-degree 8, of which orders
0–6 are extracted here (orders 7–8 were removed by a builder-level truncation
prior to caching and are outside the certificate; §7).

## 3. The certified absorptive structure

The certified result, with x = H·u_b and y = H/ω:

**Im Σ_R(ω>0) = (ω⁴/1280π) · P(x, y)**

| order | contribution to P | status |
|---|---|---|
| H⁰ | −3 | complete; three independent routes agree |
| H¹ | 0 | complete — vanishes exactly |
| H² | −(104/3)·y² | complete; u_b-free |
| H³ | +24x³ − (472/3)·x·y² | complete — first u_b-odd term |
| H⁴ | −18x⁴ + 220x²y² − 127y⁴ | complete |
| H⁵ | (416/3)x³y² − 496xy⁴ | delta-class only — **quarantined**, never binding |
| H⁶ | −48x⁶ + (3448/3)x⁴y² − 3312x²y⁴ − (1280/3)y⁶ | complete — first negative ω power |

"Complete" means: extracted through gated machinery whose per-degree reality
preconditions all hold, whose d → 3 reduction is smooth piece-by-piece, and
which reproduces the independently established H⁴ coefficient exactly as a
prerequisite gate on every run. At H⁵ the reality precondition fails at one
Δ-degree — the condition under which the extraction's own derivation states
that principal-value content leaks into the absorptive part — so only the
delta-class content is reported there and no binding statement uses it.

Structural features of the certified table:

1. **Validity domain.** The record's own derived boundary is
   ε_H = (104/9)H²/ω², with refusal at ω = √(104/9)·H ≈ 3.399H — the ratio
   of the H² to H⁰ coefficients. The u_b-free tower (−3, −104/3, −127,
   −1280/3) has successive ratios ≈ 11.6, 3.7, 3.4, suggesting (three terms
   only) a convergence boundary near ω ≈ 1.8H, safely inside the refusal.
2. **Sign.** P < 0 — the response is dissipative — throughout the
   self-consistent window: exactly for the ≤H⁴ truncation (maximum
   −599127/270400 on the window), and at every tested grid point with the
   H³ and H⁶ terms included, for both signs of u_b.
3. **Time asymmetry.** The first u_b-odd dissipative content enters at H³
   (odd in u_b, even under the joint flip (H, u_b) → (−H, −u_b), as the
   construction's parity mechanism requires): dissipation into the expanding
   background distinguishes earlier from later Wigner time.
4. **Secular self-termination.** The u_b-dependence equals the flat response
   at Hu_b = 6^(−1/4) ≈ 0.64 (at y = 0): the truncated two-time expansion is
   trustworthy only for Wigner drifts below this surface.

## 4. Fourier/distributional mapping to relative-time structure

Three layers, kept separate.

**4.1 Mathematical mapping (prescription-independent; conditional on the
§4.2 premise).** Assuming the retarded kernel is real at fixed u_b (the
premise stated in §4.2), the frozen convention permits reconstruction of its
Δ > 0 component from the corresponding full odd absorptive spectrum:
K(Δ) = (2/π)∫₀^∞ Im Σ̃(ω) sin(ωΔ) dω. A local
(contact) operator K = c·δ^(n)(Δ−0⁺) has Σ̃ = c(−iω)ⁿ exactly: only odd n
contributes to the absorptive part, and then as an *analytic odd polynomial*.
The certified terms are even powers of |ω| — no certified term is a
local-operator form. Their Δ > 0 kernels, computed identically under two
independent prescriptions (Abel regularization; analytic continuation
Γ(p+1)·sin(π(p+1)/2)/Δ^(p+1)) and confirmed by direct quadrature:

> ω⁴ → +48/(πΔ⁵)  ω² → −4/(πΔ³)  ω⁰ → +2/(πΔ)

— power-law memory tails, not contact terms. Contact/counterterm ambiguities
are supported at Δ = 0 only and cannot affect any Δ > 0 statement.

**4.2 Physical premise (stated, not derived).** Extending the computed
positive-frequency absorptive coefficients to the full odd spectral function
sgn(ω)|ω|^p — the step on which §4.1's reconstruction rests — requires the
retarded kernel to be *real at fixed u_b*. This is a physical reality
condition on the retarded response (standard for retarded responses of
hermitian sources, and consistent with every gate of the extraction,
including the per-degree reality preconditions), **not** something the cached
loop integrand itself proves: the cached object's pointwise form is dressed
by the assembly's derivative-operator routing and is not pointwise
anti-hermitian. The move from computed coefficient to odd extension is
therefore a stated premise of the tail statements, not an identity.

**4.3 Regime limitation (the infrared window).** The ω⁻² term (H⁶,
u_b-free) has, with infrared cutoff ω\* at the domain boundary, the exact
Δ > 0 kernel −Δ·Ci(ω\*Δ) + sin(ω\*Δ)/ω\*: it grows as
Δ[1 − γ_E − ln(ω\*Δ)] **within the window Δ ≲ 1/ω\*** (ω\* = 3.399H, i.e.
Δ ≲ 0.29/H) and is bounded oscillation beyond, in the cut model. The
calculation does not determine the asymptotic behavior beyond the window;
"indefinitely growing secular tail" is *not* a licensed description.

## 5. The representation test: a no-go for stationary dressings

**5.1 The tested class.** Consider representations

> Im Σ = F(x) · (ω̃⁴/1280π) · T(H/ω̃),  ω̃ = ω·g(x),

with F, g analytic (F(0) = g(0) = 1) and T arbitrary through the matched
order. This class contains all time-dependent amplitude dressings (g ≡ 1),
all frequency rescalings (F ≡ 1), and their combinations; equivalently, it is
the leading-adiabatic (Wigner-local) action of local field rescalings
h → Z(u_b)h and time reparametrizations u → f(u) on a stationary law.

**5.2 The certificate.** Matching the class to the certified table on every
complete slot through total order 6 proceeds as a chain of single linear
equations: the pure-y slots fix t = (−3, −104/3, −127, −1280/3); the measured
H¹ = 0 and H³ data pin the odd parameters f₁ = 118/13, g₁ = −59/26; the
(2,0)/(2,2) slots fix f₂ = 1336/169, g₂ = 14733/1352; and the x²y⁴ slot is
then **parameter-free**: the class requires −169672/169 ≈ −1004.0, while the
complete H⁶ datum is −3312. The residual 390056/169 ≠ 0 refutes the entire
class on complete data, independent of the quarantined H⁵ sector (which
enters no matched slot). Narrower certificates refute the amplitude-only and
rescaling-only subclasses already at H⁴.

**5.3 Robustness.** Because the certified content is non-analytic (§4.1),
local counterterms cannot generate or remove any certified coefficient: the
no-go concerns content that is not a renormalization convention. Beyond
leading adiabatic order, the redefinition orbit acquires gradient
corrections, bounded by the computed field E = (H/ω)|∂ₓP|/|P|; on a computed
subdomain (larger H/ω, the u_b-odd side) the certificate's obstruction
exceeds this bound and the no-go extends to the full orbit there; elsewhere
only the leading-order statement is claimed.

**5.4 The Wigner-local approximation, quantified.** The same field E measures
the error of replacing the two-time response by a local-frequency form: it
reaches ≈ 0.33 on the tested inner domain (ω ≥ 5H, |Hu_b| ≤ 0.3) and ≈ 1.68
at the ω ≈ 3H edge, dominated by the u_b-odd H³ term. On the tested inner
domain the Wigner-local reduction carries an error reaching approximately
33%, and therefore is **not certified as a controlled reduction** under the
preregistered 20% criterion. Any use of G_R(ω, k) in place of G_R(t, t′; k)
on this domain inherits that error.

## 6. Physical interpretation

**6.1 The central statement.** Within the frozen retarded convention, and
assuming the retarded kernel is real at fixed u_b, the certified non-analytic
absorptive terms reconstruct for Δ > 0 as power-law memory tails. The
u_b-dependent contributions occur in the faster-decaying tails, while the
deepest certified infrared contribution is u_b-independent at this order.
This statement concerns the certified non-analytic absorptive sector; local
counterterms cannot alter its Δ > 0 content. The time-domain behavior of the
ω⁻² contribution remains bounded by the stated infrared window, beyond which
the calculation does not determine the asymptotic behavior.

**6.2 Cosmic-time dependence and memory are not the same thing.** The
original intuition motivating this program fused them; the calculation
separates them. Within the certified response, cosmic-time dependence and
memory *depth* are anti-correlated: the explicitly time-dependent
pieces ride the short-memory tails (Δ⁻⁵, Δ⁻³, Δ⁻¹), and the longest-memory
certified contribution is stationary. Equivalently, in frequency space: no
time-dependent amplitude, no time-dependent clock, and no combination of the
two turns the certified response into a stationary law (§5.2) — yet the
component that most resembles genuine long-time memory carries no explicit
cosmic-time dependence at this order.

**6.3 What kind of result this is.** Every statement above is a result *of*
standard quantum field theory on de Sitter space, obtained within the
declared contract. The calculation provides the Wigner-time-resolved
absorptive coefficients at H³, H⁴, H⁶, including the exact H¹ vanishing and
the first u_b-odd term, together with the stationarity no-go certificate,
the tail/nonstationarity anti-correlation, and the quantified
Wigner-reduction error; a supported novelty statement awaits a documented
literature search. No claim of
physics beyond standard QFT is made.

**6.4 Interpretation programs.** A "responsive-medium" reading of the
gravitational vacuum is *consistent with* this structure — an expanding
background carrying time-dependent response that no stationary dressing
absorbs — but nothing here distinguishes such a reading from standard QFT on
de Sitter; the originating program's own audit records that its prediction
ledger is empty and no discriminating observable survived its gates. The
computed absorptive response is Planck-suppressed on every channel examined (tens of
orders of magnitude below existing bounds); no observable is claimed.

## 7. Limitations

The following are part of the result.

1. Validity domain ω ≳ 3.4H (derived; coefficient chart-dependent); nothing
   at ω ≲ H is evaluated at its claim point.
2. Wigner-time window: secular self-termination at Hu_b ≈ 0.64 (y = 0);
   statements tested at |Hu_b| ≤ 0.5.
3. H⁵ quarantined (delta-class only; a principal-value completion is
   absent); H⁷/H⁸ not extracted (source object degree 8).
4. Re Σ_R not computed: no pole structure, no μ-anchored dispersive
   statement, no full G_R resummation.
5. The Wigner-local reduction is not certified as controlled (§5.4): ~33%
   error on the tested inner domain against a preregistered 20% criterion.
6. The full-orbit form of the stationarity no-go holds on its computed
   subdomain only; elsewhere the statement is leading-adiabatic-order exact.
7. Long-Δ statements beyond Δ ≈ 0.29/H are not licensed; the ω⁻² kernel's
   form beyond the infrared window is undetermined (§4.3).
8. One loop only; internal bath dynamics absent; the ω → 0 transport class
   is undetermined and is excluded here by prior programmatic reservation.
9. All verification is in-house; no external review has yet occurred.
10. Three auxiliary negatives in the wider program record carry a
    must-be-reopened flag and are not used here.
11. The contract's boundary declarations are temporal only; the status of
    the constant-TT mode under the equivalence relation is unresolved, and
    it is not quotiented by assumption.
12. An earlier internal labeling of the u_b-dependent terms as "local" was
    incorrect and is superseded by §4 (the correction is part of the
    program record).
13. The odd spectral extension rests on the stated reality premise (§4.2);
    the counterterm-invariance claim is scoped to the certified
    non-analytic absorptive sector, not the complete self-energy.

## 8. What remains unresolved

The dispersive side (Re Σ_R via principal-value integrals of both cones —
the two cones carry independent content and neither is reconstructible from
the other by conjugation); the H⁵ completion; the deep-infrared completion
ω ≲ H and with it the transport class of the response (a question that
additionally requires the bath's internal dynamics, beyond one loop); the
H⁷/H⁸ sectors; the boundary/equivalence declaration for the constant-TT
mode at spatial infinity; whether any consistent infrared completion exists
in the smooth-window class after the exclusion of sharp completions; and
the foundational questions the wider program leaves standing (outcome
selection; the origin of ħ; the emergent-versus-fundamental status of the
framework), untouched by everything computed here.

## 9. Provenance and methods

The evidence base is frozen and versioned: (i) the program baseline
`GRUT_REALITY_BASELINE_01` (repository GRUT-RAI, branch v4, commit 5bdda88;
registry sha256 dc693eb6…436a9), itself the output of an audited
reconstruction with a quotation-verified record; (ii) the banked calculation
chain T3-01 through T3-09B in the working repository (instruments, result
files, and complete run logs, including disclosed instrument defects and
their corrections), with provenance-pinned caches for every extracted
object. Every number in this paper is mechanically verified against those
artifacts before commit. Computations were performed symbolically (exact
rational arithmetic throughout; numerical checks by independent quadrature
where stated) with AI-assisted execution under a pre-registration
discipline: outcome classes declared before each computation, adversarial
gates required to pass before any number is read, and refuted premises
disclosed rather than removed. Numerical-method failures encountered en
route (two quadrature/extrapolation mis-setups) are recorded in the run
logs as provenance; they are method episodes, not properties of the
transforms, and the corrected calculations appear in §4.

---

*Draft note: owner edits 1–6 of 2026-09-21 applied; FROZEN as the
scientific manuscript pending the external literature/venue pass. Nothing in it may be strengthened
without a corresponding certificate; the thirteen limitations travel with
any excerpt.*
