# Gate 3 Massive_Regulated Integral Reduction Strategy

Date: May 9, 2026  
Goal: Discover which mathematical route can produce resolved Laurent coefficients for massive_regulated branch.

## Motivation

The full cube integral evaluated with massive_regulated regulator times out in Mathematica:

$$\int_{-1}^{1} \left[{}_2F_1(h_+, h_-; D/2; (1+Z)/2)\right]^3 (1-Z^2)^{(D-3)/2} dZ$$

where $h_\pm = \frac{D-1}{2} \pm \sqrt{\frac{(D-1)^2}{4} - \frac{m^2}{H^2}}$ and $D = 4-2\epsilon$.

This integrand is too complicated for direct numerical/symbolic evaluation even with HypExp. We need to reduce it before asking Mathematica to compute.

## Discovery Routes

### Route A: Epsilon-Expansion First, Then Integrate Term-by-Term

**Strategy:** Expand the entire integrand (kernel³ × measure) in powers of ε before integrating.

**Procedure:**
1. Expand $h_\pm$ to order ε in terms of m²/H² (analytic continuation)
2. Expand ${}_2F_1(h_+, h_-; D/2; (1+Z)/2)$ to order ε using HypExp
3. Cube the expansion
4. Expand $(1-Z^2)^{(D-3)/2} = (1-Z^2)^{1/2 - 3\epsilon + ...}$ in ε
5. Multiply expansions to get integrand(Z, ε)
6. Extract coefficient of ε⁰ (finite part) and ε⁻¹ (pole)
7. For each coefficient, integrate term-by-term

**Pros:**
- Mathematica can handle series expansions easily
- Each integrated term is simpler than the full integral
- Clear tracking of which ε order contributes

**Cons:**
- May require many terms before a pattern emerges
- Cubic dependence on kernel may cause factorial growth

**Expected output:**
- Laurent coefficient data from integrated terms
- Or blocked if terms do not converge/resolve

---

### Route B: Change Variable u = (1+Z)/2 (Beta-Weighted Form)

**Strategy:** Transform to u-space and recognize beta-function structure.

**Change of variables:**
$$u = \frac{1+Z}{2}, \quad Z = 2u-1, \quad dZ = 2du$$
$$1-Z = 2(1-u), \quad 1-Z^2 = 4u(1-u)$$

**Transformed integral:**
$$\int_0^1 \left[{}_2F_1(h_+, h_-; D/2; u)\right]^3 [4u(1-u)]^{(D-3)/2} \cdot 2 \, du$$

$$= 2 \cdot 4^{(D-3)/2} \int_0^1 {}_2F_1(h_+, h_-)^3 \cdot u^{(D-3)/2} (1-u)^{(D-3)/2} \, du$$

**Form:**
$$\text{Beta}((D-1)/2, (D-1)/2) \times \text{(hypergeometric-cubed correction)}$$

**Pros:**
- Standard Beta-function form may factor out easily
- HypExp designed to handle Beta reductions
- Cleaner boundary behavior (u ∈ [0,1])
- u-variable more natural for hypergeometric expansion

**Cons:**
- Still requires ${}_2F_1^3$ evaluation
- Prefactor $4^{(D-3)/2}$ introduces additional ε dependence

**Expected output:**
- Laurent data from Beta-reduced form
- Or blocked if reduction stalls

---

### Route C: Numerical Mellin/Beta Sanity Check

**Strategy:** For concrete m²/H² > 0, evaluate the integrand numerically at small ε values and fit Laurent coefficients.

**Procedure:**
1. Fix m²/H² to a test value (e.g., 0.5)
2. Fix D = 4 - 2ε for ε = 10⁻³, 10⁻⁴, 10⁻⁵
3. Numerically integrate using NIntegrate with high precision
4. Collect (ε_value, integral_result) pairs
5. Fit polynomial: $I(ε) ≈ c_{-1}/ε + c_0 + c_1 ε + ...$
6. Extract pole and finite coefficients

**Pros:**
- Completely bypasses symbolic bottlenecks
- Can verify analyticity/smoothness of coefficient as function of m²/H²
- Quick discovery of which terms dominate
- Can test stability across ε range

**Cons:**
- Cannot promote R (numerical only)
- Precision losses accumulate at small ε
- Does not provide symbolic form
- May not reveal underlying structure

**Expected output:**
- Numerical Laurent data (informational only)
- Signals whether finite part is stable or singular
- Reveals typical scales of pole/finite parts

---

### Route D: Endpoint Asymptotic Subtraction (u -> 0)

**Strategy:** Isolate the endpoint-singular contribution near $u=0$, integrate it analytically, and integrate only the subtracted remainder numerically.

With the reduced kernel
$$K(u,\epsilon) = 2\cdot 4^{(D-3)/2}\,{}_2F_1(h_+,h_-;D/2;u)^3\,u^{(D-3)/2}(1-u)^{(D-3)/2},$$
write
$$I(\epsilon)=\int_0^1 du\,K(u,\epsilon)=\int_0^1 du\,K_{\text{sing}}(u,\epsilon)+\int_0^1 du\,[K(u,\epsilon)-K_{\text{sing}}(u,\epsilon)].$$

Choose $K_{\text{sing}}$ as the endpoint asymptotic expansion at $u\to0$:
$$K_{\text{sing}}(u,\epsilon)=2\cdot 4^{(D-3)/2}u^{(D-3)/2}(a_0(\epsilon)+a_1(\epsilon)u+\cdots).$$

**Procedure:**
1. Compute endpoint coefficients $a_0(\epsilon), a_1(\epsilon)$ from the smooth factor at $u=0$.
2. Integrate $K_{\text{sing}}$ analytically to capture pole structure.
3. Numerically integrate $K-K_{\text{sing}}$ on $[0,1]$ (improved stability).
4. Sample multiple small-$\epsilon$ values and fit $I(\epsilon)\approx c_{-1}/\epsilon + c_0 + c_1\epsilon$.
5. Export $(c_{-1},c_0)$ with full route/provenance metadata.

**Pros:**
- Separates analytic pole terms from finite remainder.
- Directly targets diagnosed endpoint singularity.
- More stable than raw NIntegrate on full kernel.

**Cons:**
- Still numerical-fit based (informational unless independently replicated).
- Requires careful selection of subtraction order and fit window.

**Expected output:**
- Better-conditioned samples for Laurent fitting.
- Explicit blocker if subtraction still fails.

---

## Integration into Gate3 Workflow

**New file:** `GATE3_AJ_MASSIVE_REDUCED_HYPEXP.wl`
- Unified Wolfram script implementing all three routes
- Parameterized by GATE3_MASSIVE_ROUTE ∈ {A, B, C, D}
- Per-route logging to output JSON files

**Wrapper logic** (scripts/run_gate3_mathematica_handoff.sh):
- Checks for GATE3_MASSIVE_ROUTE environment variable
- If massive_regulated + route set → dispatches to reduced script
- Otherwise → proceeds with full integral (original behavior)

**Invocation:**
```bash
export GATE3_BRANCH_ID=massive_regulated
export GATE3_M2_OVER_H2=0.5
export GATE3_MASSIVE_ROUTE=D  # or A/B/C
bash scripts/run_gate3_mathematica_handoff.sh
```

**Output metadata:**
- route: "A", "B", "C", or "D"
- regulator_approach: "reduced_integral"
- elapsed_seconds: actual runtime (helps diagnose timeouts)
- status: "computed", "blocked", or "timeout"
- if blocked: reason_code (e.g., "expansion_did_not_resolve")
- if computed: full Laurent data with resolved_scalar guarantees

**Test sequence:**
1. Route A (expand ε, integrate terms)
2. Route B (u-variable change, Beta form)
3. Route C (raw numerical sanity check)
4. Route D (endpoint asymptotic subtraction)

If any route produces resolved_scalar coefficients → use that for production
If all routes block → indicates fundamental mathematical issue (singularity, non-convergence)

## Branch Priority After Discovery

| Priority | Branch / method | Why |
|---|---|---|
| 1 | hminus_derivative_regularized | Most likely serious target branch |
| 2 | massive_regulated Route D (endpoint-subtracted) | Diagnosed singularity now has structured mitigation |
| 3 | hminus_direct_limit | Comparison-only path; higher risk |
| 4 | conformal_closed_form | Benchmark only |
| 5 | mmc_massless | Zero-mode blocked |

## Recommendation

Do not pursue further brute-force reductions. Continue with endpoint asymptotics (Route D) as fallback while prioritizing derivative regularization as the main next implementation branch.
