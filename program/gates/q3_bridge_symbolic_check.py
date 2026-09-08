"""
Q3 PHYSICAL SCALE BRIDGE GATE -- symbolic verification only. Draft 4.
No numerical experiment, no parameter fitting, no new coupling/scale/renormalization condition.

Record inputs only:
  Tier-4 H^0:  Sigma = A*w^4*(2*log(mu/w) + I*pi) + c4*w^4,  A = -3/(1280*pi^2)
  Lambda_R := mu*exp(c4/(2A))                  [WALL_KR_LAMBDA_R_OWNER_RULING.md]
  D_0 = w^2/(2*kappa^2), k -> 0 FIRST  PINNED  [wall_kr_tier4_retarded.py:296, :297, :513]
  Im G_R = Im Sigma/|D|^2                      [WALL_KR_CONTRACT_RETARDED_VERDICT.md:122]
"""
import sympy as sp

w, k, LR, mu, kap = sp.symbols('omega k Lambda_R mu kappa', positive=True)
dlt, a = sp.symbols('delta a', real=True)          # field redefinition: REAL parameter
A  = sp.Rational(-3, 1280)/sp.pi**2
D0 = w**2/(2*kap**2)

def D(lr, aa):                                      # aa = real local quartic counterterm
    return (D0 - 2*A*w**4*sp.log(lr/w)) - sp.I*sp.pi*A*w**4 + aa*w**4

print("=== Sec. 4 -- THE DECIDING RESULT: the Lambda_R direction is removable ===")
shift = sp.simplify(D(LR*sp.exp(dlt), 0) - D(LR, 0))
print("N1  shift from Lambda_R -> Lambda_R*e^delta :", shift)
print("    purely REAL?", sp.simplify(sp.im(sp.expand_complex(shift))) == 0)
astar = sp.solve(sp.Eq(sp.simplify(D(LR*sp.exp(dlt), a) - D(LR, 0)), 0), a)[0]
print("N2  removed EXACTLY by real counterterm a* :", astar,
      "| omega-independent?", sp.simplify(sp.diff(astar, w)) == 0)
print("N3  Im Sigma                               :", sp.simplify(sp.pi*A*w**4),
      "  IMAGINARY -> no real a can produce or remove it.")
print("    => the reality condition PRESERVES Im Sigma, the cut, rho_TT, Gamma_T.")
print("       Draft 3's 'it proves too much' omitted this and is withdrawn.")

print()
print("=== supporting ===")
print("R1  d(ReSigma)/dlogLambda_R                :", sp.simplify(sp.diff(2*A*w**4*sp.log(LR/w), LR)*LR))
print("R2  w^4/D_0^2                              :", sp.simplify(w**4/D0**2), " (omega-independent)")
print("K4  (w^2-k^2)^2/D_0(k)^2                   :", sp.simplify((w**2-k**2)**2/((w**2-k**2)/(2*kap**2))**2),
      " (same proportionality at ALL k)")
print("R6  ReD=0 lever: log(Lambda_R/w)           :", sp.simplify(D0/(2*A*w**4)), " (~1/(kappa*w)^2: out of band)")

print()
print("=== Sec. 4.1 -- true, but NOT refutations (off-shell G is not redefinition-invariant) ===")
ReS, ImS = 2*A*w**4*sp.log(LR/w), sp.pi*A*w**4
absD2 = (D0-ReS)**2 + ImS**2
print("    d(Im G_R)/dlogLambda_R (small w)       :",
      sp.simplify(sp.series(sp.diff(ImS/absD2, LR)*LR, w, 0, 4).removeO()), " nonzero -- as redundancy PREDICTS")
sens, diss = sp.simplify(4*A*w**4/D0), sp.simplify(ImS/D0)
print("    ratio sens/diss                        :", sp.simplify(sens/diss),
      " <- ANALYTIC IDENTITY (A and omega cancel); carries no magnitude information")

print()
print("=== Sec. 2.4 -- which quantity is mu-free? ===")
c4mu = A*(sp.Rational(-6841,2835) - sp.EulerGamma + sp.log(4*sp.pi)) - 2*A*sp.log(mu)
print("    Lambda_R = mu*exp(c4(mu)/2A)           :", float(sp.simplify(mu*sp.exp(c4mu/(2*A)))),
      " <- mu-FREE CONSTANT")
print("    Lambda_R/mu                            :", sp.simplify(sp.exp(c4mu/(2*A))), " <- mu-DEPENDENT")

print()
print("=== Sec. 3.1 -- certification apparatus is Lambda_R-blind (uncontested) ===")
print("    d^5/dw^5[2A w^4 log(Lambda_R/w)]       :", sp.simplify(sp.diff(2*A*w**4*sp.log(LR/w), w, 5)), " (no Lambda_R)")
print()
print("NOT EVALUATED: the w->0 limit -- outside the declared band (w >> H), where the H^2 term")
print("-(13/480 pi^2) H^2 w^2 L is the SAME order in w as D_0.")
