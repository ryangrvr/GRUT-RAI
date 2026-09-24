# K_ROUND_INSPECTION_01 — direct inspection of the blinded outputs

**Date:** 2026-09-24. **Mandate:** owner ruling — inspect the six blinded kernel files and
the adjudicated 48-row table, especially the flavor result and the leak-protected matches;
determine whether the surviving correspondence is genuinely mathematical or whether the
synthesis was compressing several phenomena under the word "kernel." **Method:** main-session
read of the actual files (`rrp/rrp01/kernels/*.json`, `COMPARATOR_02.json`), no new agents.

## 1. The leak-protected core, isolated

Of the 25 YES rows, **17 have corpus_refs in the stripped fields** (empirical_inputs,
constants) — the rows blinding actually protected. The 8 non-protected YES rows all sit in
`primitives`/`observables` and inherit the §0 contamination discount at whatever level the
comparator assigned. Everything below concerns the protected 17 unless stated.

## 2. The flavor result, verified by direct read: GENUINE

The G_F computation in `qft-gauge-flavor.json` is correct, complete group theory, not
pattern-matching: G_F = U(3)_Q×U(3)_u×U(3)_d×U(3)_L×U(3)_e acting by
(Y_u,Y_d,Y_e) → (V_Q†Y_uV_u, V_Q†Y_dV_d, V_L†Y_eV_e); quark sector 36 real parameters,
acting dimension 27, **generic stabilizer U(1)_B of dimension 1**, orbit 26, invariants
10 = 6 masses + 3 angles + 1 phase; lepton sector 18 − 15 = 3 with stabilizer U(1)³.
**Honesty note: the number 13 was visible** to the computer (it sits in
`domain_of_validity`, not only in the stripped field) **— but the derivation was not**:
the stabilizer dimensions, the 26-dimensional fibre, the Weinberg-operator extension
(c₅ collapses the stabilizer to nothing → 12 lepton invariants), the Jarlskog determinant
identity det[H_u,H_d] = 2iJ·(six mass-difference products), rank protection by the
one-sided RGE structure *plus* 't Hooft naturalness, and the **θ̄–rank interlock** (a
massless up quark would delete the θ̄ kernel element — two kernels not independent) appear
nowhere in the corpus. The last two are structure the audit itself had never recorded.

## 3. Spot-checks of the strongest protected matches: same object, real argument

- **Branch weights ↔ Schur-multiplier fixed points** (open-quantum, THEOREM): with
  H_int = A⊗B and [A,H_S]=0, every Kraus operator is diagonal in A's eigenbasis; the
  channel is a Schur multiplier with unit diagonal, whose diagonal entries are fixed points
  *by inspection* — exact, non-perturbative, environment-state-independent. And it explains
  the corpus data rather than restating it: the measured decoherence rates (Brune,
  Hornberger, Hackermüller) probe the off-diagonals "precisely because the diagonal is
  inert."
- **R_K ↔ Chern/TKNN** (condensed-matter, THEOREM): integer-valued, continuous on the
  gapped set, hence locally constant; Hastings–Michalakis without averaging assumptions;
  the load-bearing hypotheses (gap, finite range) stated, with the physical scope taken
  from `domain_of_validity`.
- **A_s, n_s ↔ super-horizon ζ-conservation** (cosmology, THEOREM) — and the same file
  independently identifies **the basin boundary where the contraction fails** (ultra-slow-
  roll: φ̇ ~ a⁻³, the erased data becomes observable in the squeezed bispectrum — the PBH
  regime). An agent that knows where its own contraction stops acting is doing physics,
  not echoing.

## 4. The answer to the owner's question: yes — "kernel" was compressing two phenomena, and the blinded agent said so first

From the flavor computer's method note, verbatim:

> "The contractions split into two kinds that are usually conflated. The **redundancy
> quotients** (gauge orbit, flavor basis, chiral/theta, scheme) are EXACTLY non-invertible
> at every scale — *the information was never there*. The **scale flows** (Wilsonian
> coarse-graining, EFT truncation, Yukawa running) are, at a finite scale ratio, formally
> invertible ODE flows whose inverse is merely exponentially ill-conditioned; they become
> exactly many-to-one only in the limits μ→0 and E/Λ→0."

So the surviving correspondence decomposes into **two mathematically different phenomena**
(plus the labels and the expanding directions):

| Sense of "kernel" | Nature | Protected instances | What it explains |
|---|---|---|---|
| **Invariant ring of an exact redundancy quotient** | kinematic identification — a fact about the theory's *description space* | 13 flavor parameters (+θ̄) inside the SM-19+ row | the *identity and dimension* of what can possibly be an input — near-analytic but contentful: the count is a theorem |
| **Residue of a dynamical contraction** (limit of a flow: μ→0, t→∞, horizon exit, weak coupling) | dynamic — a fact about *what survives evolution/reduction* | bath (J(ω),β); Davies γ(ω); transport coefficients + EoS; material response; A_s,n_s; acoustic quantities; T via KMS ratio; gauge couplings as relevant/marginal set | *which* data of the upstream description remain expressible downstream — the genuinely empirical part of the correspondence |
| **Protected labels** (integrality/conservation) | either — protection, not retention | R_K (Chern); T_CMB (attractor label); branch weights (Schur fixed points) | why these cannot drift |
| **Expanding directions** | dynamic, anti-contractive | G, Λ, Planck-length combination | why these must be supplied, with anti-smallness |

The two columns have different epistemic characters and should never again share the bare
word "kernel" in this program's documents. Proposed vocabulary (recorded, not banked):
**quotient-kernel** vs **flow-residue**.

## 5. What this does to the carried question

*"Why does a physical theory determine some elements of a retained kernel while leaving
others as supplied content?"* now splits cleanly:

- **For quotient-kernels** the question dissolves locally and re-poses upstream: a theory
  cannot determine coordinates on its own physical quotient — they are its arguments. The
  real question becomes *why this quotient* — i.e., why U(3)⁵, i.e., why this field
  content: the content-selection question, untouched.
- **For flow-residues** the law-determined/law-undetermined split within the residue has a
  visible geometric shape in the inspected files: the law-determined elements (exponents,
  anomaly coefficients, scaling relations, monotones) are properties *of the flow and its
  fixed points*; the law-undetermined ones (coupling values, boundary amplitudes, which
  phase) are *positions within the flow's structure* — which basin, where on the unstable
  manifold, which point of the fixed-point manifold. **Observation only — UNCHALLENGED,
  not a candidate, not banked**: "the theory fixes the geometry; the supplied data are
  coordinates in it." This is recorded for a future round to attack, with the obvious trap
  named at birth: "position vs geometry" may itself be presentation-relative.

## 6. Grade and limits

Main-session single-reader inspection; no adversarial pass on §4's decomposition or §5's
observation; the flavor derivation checked by me at mathematics level, not re-derived by an
independent instrument; the 8 non-protected YES rows remain at their discounted grades; the
category-leak defect of the round stands unrepaired (the clean re-run specified in the
synthesis remains the decisive test for the seven discounted showcase rows). The verdict
ledger of AMENDMENT 01 is unchanged by this inspection — it is sharpened, not upgraded.
