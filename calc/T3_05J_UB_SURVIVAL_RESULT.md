# T3-05J -- H^4 u_b survival under the existing response assembly

## Question
Do already-declared assembly operations fix the fate of the H^4 terms A_{2,2} = +11 w^2 u_b^2/(64 pi) and A_{2,4} = -9 w^4 u_b^4/(640 pi) WITHOUT constructing the missing Sigma -> G_R^TT keystone?

## Answer

**SURVIVES_EXISTING_ASSEMBLY_OPERATORS**

| Test | Result |
|---|---|
| A: operator inventory | every declared operator acts before/at Sigma; NO post-Sigma operator exists |
| A: P^TT placement | input-side tensor rule (bath contraction, ~line 177); consumed before Sigma_R exists |
| B: tensor structure | A_{2,2}, A_{2,4} are scalars -- no free indices for any declared contraction |
| C: ledger search | G_R/Dyson language present but ASPIRATIONAL only (RUNG3 class-C keystone, never computed) |
| D: survival regression | u_b present in both cone branches and in the assembled A2 (trusted T3-05A records) |
| E: keystone | unavoidable for the observable-level fate; missing operation = Sigma(x;x') -> G_R^TT resummation |

## Required caveat
This class means ONLY: no currently DEFINED assembly operation removes the H^4 u_b^2/u_b^4 terms. It does NOT establish physical frame dependence: the declared-but-uncomputed keystone (Sigma -> G_R^TT resummation) is the legitimate place where the fate could still change. Class 3 with an identified missing operation is therefore also the authorization basis for the keystone calculation if pursued.

## Not adjudicated
Physical status of u_b; R'; W-0; deep IR; H^6.
