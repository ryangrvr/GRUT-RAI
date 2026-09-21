# T3-05I — RESPONSE-TO-OBSERVABLE TRACE

**Status:** diagnostic only · append-only · W-0 not banked · R′, H⁶, Tier-3 loop untouched

## Question

Does the existing repository define a path

```
Sigma_R (or A2(u_b))
  -> equation of motion / effective inverse propagator
  -> response function / propagator
  -> declared observable functional
  -> stated measurement / bound / falsifier
```

using only already-declared links? No observable was defined; no clock, gauge
choice, detector, or equivalence relation was introduced.

## Final status: `PARTIAL_RESPONSE_PATH_FOUND`

### What was found

| Link | Type | Source |
|---|---|---|
| `Sigma_R` → FDT/KMS noise-lock gate | **explicit mathematical dependency** (internal → internal) | `wall_kr_gate_e_fdt_kms.py:173-226` |
| `Sigma_R^finite` → adjudication / renormalization (`Pi_local^MS` + `Pi_nonlocal^invariant`) | **explicit mathematical dependency** (older frozen kernel; still internal) | `wall_a3_4_adjudication.py:151`, `wall_a_assembly2.py:96-141`, `wall_a4_response_dressed.py:122` |
| `G_R = 1/(G0^-1 - Sigma)` | **proposed/aspirational prescription** (frontier-reserved; never evaluated) | `BUILD_BANKING_PROMPT.md:50` |
| `Sigma(x;x')` → assembled `G_R^TT` | **absent — explicitly audited absent** | `RUNG3_BRIDGE_SCOPE.md:52` |
| `rho_TT(ω→0)`, Kubo `η = lim Im G_R^TT/ω` | **declared observable endpoint, uncomputed** | `CLASS_C_WALL_CONTRACTS.md:18`, `SPECIALIST_BRIEF_1_bath_spectral_function.md:31` |

### The decisive fact

The repository's own rung-3 bridge audit (`RUNG3_BRIDGE_SCOPE.md`, owner-commissioned 2026-08-21, status "NOTHING BANKED") states at line 52:

> *"No calc in this repository constructs K_R or N from Σ(x;x′); J(ω) is staked directly"*

and at line 70 classifies the assembled `G_R^TT` from `Σ(x;x′)` as **object class C — "never computed; never reduced; THE keystone"**.

So the observable endpoint **exists in the theory** (the wall contracts name `rho_TT(ω→0)` as the only thing that counts, and the Kubo η as the scalar the question reduces to), but the **path from the computed Tier-3 coefficients to that endpoint is precisely the missing bridge** the repository has already formally identified.

### Missing bridge (recorded, not repaired)

1. **Assembly:** Σ(x;x′) → G_R^TT (resummed + continued) — the declared keystone, never computed.
2. **Reduction:** class-C self-energy → worldline (A) or homogeneous-susceptibility (B) object — the unexhibited map (RUNG3_BRIDGE_SCOPE §3).
3. **For A₂ specifically:** whether the `u_b^2`/`u_b^4` pieces survive assembly into G_R^TT is **undetermined and not claimable in either direction** from current artifacts.

### Consequence for the u_b question

The H⁴ coefficient

```
A2(u_b) = -127/(1280π) + 11 ω² u_b²/(64π) − 9 ω⁴ u_b⁴/(640π)
```

is currently an **internal response coefficient with a partial forward path**:
it feeds internal consistency machinery, and it would feed the named physical
observable *through the assembly that has not been built*. Its frame status is
therefore not merely "untested" — the instrument that would test it (the
assembled observable) is itself the declared missing keystone of the program.

## Mandatory final statement

**No conclusion about physical covariance, frame dependence, gauge
removability, or observability was made.** No observable was invented,
defined, or proposed; R′ was not invoked; W-0 was not banked; H⁶ and the
Tier-3 loop were untouched; all frozen artifacts remain read-only.
