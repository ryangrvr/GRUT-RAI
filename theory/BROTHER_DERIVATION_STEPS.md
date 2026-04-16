# Steps to Derive w_g for the Standard Model

## For: Ryan's brother (physicist)
## Task: Extract w_g_i from Osborn 2003 ε coefficients via consistency relations
## Estimated time: 1-2 focused hours

---

## What's already done

From Osborn 2003 eq (36), evaluated for SM field content:

| Group | ε coefficient A (at 1-loop, in units g²/(16π²)) |
|-------|-------------------------------------------------|
| SU(3)_c | **+5** |
| SU(2)_L | **−61/12** |
| U(1)_Y | **−485/12** |

where ε_i = 1 + A_i · g_i²/(16π²).

The group theory data used:
- C_SU3 = 3, C_SU2 = 2, C_U1 = 0
- R_ψ: SU(3)=6, SU(2)=6, U(1)=10
- R_φ: SU(3)=0, SU(2)=1/2, U(1)=1/2

See `OSBORN_2003_EPSILON_SM.md` for the full derivation of these.

---

## What you need to do

**Goal:** Convert the ε_i coefficients into w_g_i coefficients via the
Weyl consistency relation [Dσ, Dσ'] = 0.

---

## Step 1: Start from Osborn 2003 equation (35)

The local 1-loop effective action for a gauge theory with local coupling g(x):

```
L = n_V × {
     (1/g²) [ α (∇²g)² - 2δ G_μν ∂^μg ∂^νg - (1/3) ε R ∂_μg ∂^μg ]
   - 2κ (1/g³) ∂_μg ∂^μg ∇²g
   + 2λ (1/g⁴) (∂g)²(∂g)²
}
```

with α, δ, ε, κ, λ given by eq (36) (1-loop, scheme dependent).

---

## Step 2: Identify the terms that contribute to the Osborn equation

In Osborn 1991 eq (29), the anomaly is:

```
∫ dv σ B + ∫ dv ∂_μσ Z^μ − ∫ dv ∇²σ A
```

with:
- B = β_a F + β_b G + (1/9) β_c R² + (1/3) χ^e_i ∂_μg^i ∂^μR
      + (1/6) χ^f_ij ∂_μg^i ∂^μg^j R + (1/2) χ^g_ij ∂_μg^i ∂^νg^j G^μν + ...
- Z^μ = G^μν w_i ∂_ν g^i + (1/3) R Y_i ∂^μg^i + S_ij ∂^μg^i ∇²g^j + ...
- A = (1/3) d R + U_i ∇²g^i + (1/2) V_ij ∂_μg^i ∂^μg^j

**w_i lives in Z^μ**, specifically multiplying G^μν ∂_ν g^i.

---

## Step 3: Perform the integration-by-parts

The Osborn 2003 Lagrangian eq (35) has:
```
-(1/3) ε R ∂_μg ∂^μg    (in L)
```

This term can be IBP-rewritten using ∇_μ(g ∂^μg) to produce pieces
living in different Osborn 1991 structures. Specifically:

```
R ∂_μg ∂^μg = ∇_μ(R g ∂^μg) - g ∇_μ(R ∂^μg)
            = ∇_μ(...) - g R ∇²g - g (∂_μR)(∂^μg)
```

The total-derivative piece drops under integration. The (∂_μR)(∂^μg) term
contributes to χ^e_i. The g R ∇²g term contributes elsewhere (or to the
U_i ∇²g term in A via another IBP).

**Key identity to use:**
Under σ-integration, ∂_μσ Z^μ can be rewritten as -σ ∇_μ Z^μ + total deriv.
So Z^μ terms appear in the anomaly structure as their divergence.

---

## Step 4: Apply [Dσ, Dσ'] = 0

The commutator condition from Osborn 1991 eq (30) generates several
consistency relations. The relevant ones for w_i are the derivatives
of the b-equation (eq 31):

```
8 ∂_i β_b = χ^g_ij β^j - L_β w_i
```

and related relations involving χ^e, χ^f, w, Y, S, etc. (multiple
relations from eq (31) and neighboring equations in Osborn 1991).

The ε coefficient from 2003 lives in χ^f (the R (∂g)² coupling), not in
w directly. But χ^f and w are RELATED through the consistency conditions:

```
∂_i (something involving χ^f) = χ^g_ij β^j + (contribution to w_i)
```

The exact form of this relation is in Osborn 1991 section 3, equations
following (30).

---

## Step 5: Extract w_g for each SM gauge coupling

For a single gauge coupling g_i, the structure at 1-loop (from eq 35 form):

```
w_g_i ~ n_V_i × f(α_i, δ_i, ε_i, κ_i, λ_i) / g_i
```

where f is the combination that survives the consistency conditions
(this is the combination you need to extract).

**Minimum deliverable for us:**
Three numbers: w_g_SU3, w_g_SU2, w_g_U1 at one-loop evaluated at M_Z,
in units of (16π²)^(-1).

---

## Step 6: Report the three numbers

Format we need:

```
w_g_SU3 = [value] × (1/16π²)    [sign: + or −]
w_g_SU2 = [value] × (1/16π²)
w_g_U1  = [value] × (1/16π²)
```

Plus any notes on scheme dependence, integrability constraints, or
caveats (e.g., "valid in MS-bar", "subject to subleading correction from...").

---

## What Ryan does with your answer

1. Plugs w_g_i into `grut/foundation/osborn_integrated.py`:
   ```python
   # Currently: run_rg_flow(c_w_gauge=<unknown>)
   # After: run_rg_flow(c_w_gauge_SU3=YOUR_VALUE_1,
   #                    c_w_gauge_SU2=YOUR_VALUE_2,
   #                    c_w_gauge_U1=YOUR_VALUE_3)
   ```

2. The module integrates (1/8) ∫ χ^g_ij β^j dg^i − (1/8) ∫ L_β w_i dg^i
   along the SM RG trajectory from M_Planck to M_Z.

3. Reports:
   - Δβ_b (shift in Euler coefficient)
   - R_final = |β_b_final / β_a_final|
   - Ω_Λ = ((2 − R_final) / (S · τ_0 · H_0))²
   - Comparison to Planck 0.6889

4. **No adjustments, no target-matching.** Whatever Ω_Λ falls out is the
   answer.

---

## Possible outcomes and their meaning

| Outcome | What it means |
|---------|---------------|
| Ω_Λ matches Planck (~0.69) | Framework derived from established physics |
| Ω_Λ close but off (~0.60-0.80) | Framework partially works; other corrections needed |
| Ω_Λ way off (>0.85 or <0.50) | Mechanism fails; R_1loop is closer to right answer than R=1.15 |
| w_g_i have signs that prevent R increase | Unitarity/structure constrains GRUT's target |

All outcomes are publishable. A clean "mechanism fails in this specific way"
is a real result.

---

## Critical constraint: no sign-flipping or scheme-picking to hit the target

If your derived w_g_i give Ω_Λ = 0.95 (i.e., R goes down not up), that's
the answer. Don't choose a different scheme to make it work. The PZ
framework (Prochazka-Zwicky 2017) established that Δb̄ > 0 by unitarity,
which already constrains the sign — any scheme choice must respect that.

---

## Key references on your desk

1. **Osborn 1991** (NPB 363, 486) — `https://www.damtp.cam.ac.uk/user/ho10/loc.pdf`
   - Eq (28): definition of β_a, β_b, β_c in terms of F, G, R²
   - Eq (29): anomaly structure with B, Z^μ, A, and χ^g_ij, w_i
   - Eq (30): Weyl consistency condition [Dσ, Dσ'] = 0
   - Eq (31): 8 ∂_i β_b = χ^g_ij β^j − L_β w_i ← **our target**

2. **Osborn 2003** (hep-th/0302119) — Already extracted:
   - Eq (35): L with α, δ, ε, κ, λ
   - Eq (36): explicit 1-loop coefficients in terms of C, R_ψ, R_φ

3. **Jack & Osborn 1990** (NPB 343, 647) — Section 4
   - The original derivation of the w_i structure for gauge+fermion theories

4. **Prochazka & Zwicky 2017** (arXiv:1703.01239)
   - Eq (38): integrated form of Osborn consistency
   - Eq (60): NNLO explicit at CBZ-FP (for sanity check)
   - Sec 2.5: Δb̄ > 0 by unitarity

---

## If you get stuck

The single ambiguity we hit is: **which combination of (α, δ, ε, κ, λ)
from Osborn 2003 eq (35) maps to w_i in Osborn 1991 eq (29)?**

Jack & Osborn 1990 section 4 has the explicit derivation for pure gauge
theory with fermions. That's where the unambiguous identification is.
If you can read section 4 and pull out the expression, we have c_w.

---

## The clean deliverable we need from you

Either:
(a) Three numbers w_g_SU3, w_g_SU2, w_g_U1 in explicit form, OR
(b) A statement "the expression in Jack-Osborn 1990 eq (X.Y) gives
    w_g_i = [formula]; for SM that evaluates to ..."

Either gets us unstuck. Everything else — integrating, reporting Ω_Λ,
comparing to Planck — is automated in Ryan's Python pipeline.

---

*Estimated time with papers in hand: 1-2 focused hours. The calculation
is bounded; the answer exists; you're the one person in this chain
qualified to do this specific step.*
