# Appendix T-C: Dissipation Functional, Lyapunov Structure, and Balance-Law

GRUT Thermodynamic Program -- Phase T-C

---

## Core Result

**Global Lyapunov function**: V = (1/2)(Phi - X_ss)^2

    dV/dt = -(2/tau) V < 0    for V > 0

    V(t) = V(0) exp(-2t/tau)

**Dissipation rate**: D = delta^2/tau >= 0

**Balance**: dV/dt + D = 0 (autonomous); dV/dt + D = forcing power (driven)

---

## Evidence Table

| Regime | Functional | Monotone? | Exact? | Balance? |
|--------|-----------|----------|--------|---------|
| Free X=0 | V=(1/2)Phi^2 | Yes | Exact | dV/dt+D=0 |
| Const X=X0 | V=(1/2)(Phi-X0)^2 | Yes | Exact | dV/dt+D=0 |
| Time-dep | V=(1/2)(Phi-X)^2 | Conditional | Conditional | +forcing |
| Distance | \|delta\| | Yes | Exact | N/A |
| Norm | V=(1/2)delta^2 | Yes | Exact | dV/dt+D=0 |
| General | V=(1/2)(Phi-X)^2 | Conditional | Conditional | +forcing |

---

## Entropy Firewall (Track E)

V is Lyapunov, **NOT entropy**. D is dissipation rate, **NOT entropy production**.
Balance is bookkeeping, **NOT first law**. 2/tau is contraction rate, **NOT
inverse temperature**. Monotone theorem is Lyapunov stability, **NOT second law**.

---

## Verdicts

| Verdict | Value |
|---------|-------|
| Lyapunov | global_lyapunov_function_supported |
| Dissipation | exact_decay_functional_identified |
| Balance | exact_dissipative_balance_supported |
| Firewall | monotone_not_entropy_explicitly_secured |
| Authorization | authorized_to_proceed_to_TD |

**Overall: native_dissipation_functional_supported_with_entropy_firewall**

## Licensed
Lyapunov functional, decay rate, dissipation rate, balance law, distance
monotone, conditional monotone, restricted H-theorem analog.

## NOT Licensed
Entropy, entropy production, temperature, equilibrium, free energy,
first/second law, statistical mechanics, partition function, bath.

**T-D authorized.**
