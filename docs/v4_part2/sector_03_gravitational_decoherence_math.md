# Sector 3 — Gravitational Decoherence: Mathematical Scaffold

## Symbol table

| Symbol | Meaning | Units |
|--------|---------|-------|
| Lambda | Gravitational decoherence rate | Hz |
| m | Mass of superposed object | kg |
| l | Superposition separation | m |
| R | Body radius | m |
| S(l/R) | Extended-body suppression factor | dimensionless |
| rho_1, rho_2 | Mass densities of two branches | kg m^-3 |
| P | Gas pressure | Pa |
| T | Temperature | K |
| P* | Gas-gravity crossover pressure | Pa |
| m* | Quantum-classical boundary mass | kg |
| C_Final | 3-loop anomaly coefficient | dimensionless, 1.14e-4 |

## 1. CTP influence-functional basis

The gravitational decoherence rate is derived from the tree-level gravitational self-energy in the Schwinger-Keldysh (CTP) influence functional. The CTP effective action for a massive particle in its own gravitational field includes a noise kernel whose imaginary part generates decoherence:

    Im[S_IF] = (G / hbar) integral integral [rho_1(x) - rho_2(x)] [rho_1(x') - rho_2(x')] / |x - x'| d^3x d^3x'

This is the Diosi functional.

## 2. Universal Scaling Law (USL)

For a point mass in a superposition of separation l:

    **Lambda = G m^2 / (hbar l)**

Zero free parameters. This is the tree-level result.

## 3. Extended-body geometry correction

For a uniform-density sphere of radius R:

    Lambda = G m^2 S(l/R) / (hbar l)

    S(l/R) = 1                  for l >= 2R   (far field)
    S(l/R) = (l/R)^3 / 6       for l < 2R    (near field)

Capped: S <= 1 always.

At l/R = 0.1: S = 1.67e-4 (point-mass overestimates by 6,000x).

## 4. Near-field / far-field behavior

- Near field (l < 2R): Lambda ~ l^2 (increases with separation)
- Far field (l > 2R): Lambda ~ 1/l (decreases with separation)
- Peak at l ~ 1.8R (the geometric kink)
- A single power-law fit fails: residual = 0.56 dex (265%)

## 5. Environmental channel decomposition

For any (m, R, l, T, P), the total decoherence rate is:

    Lambda_total = Lambda_grav + Lambda_gas + Lambda_BB + Lambda_trap + Lambda_charge + Lambda_vib + Lambda_readout + Lambda_anom

Each channel is independently computed. The binding constraint is the largest suppressible channel.

Key formulas:
- Gas: Lambda_gas = n sigma v_th (l / lambda_dB)^2
- Blackbody: Lambda_BB ~ (c/lambda_th)(R/lambda_th)^6(l/lambda_th)^2 * prefactor
- Anomaly: Lambda_anom = C_Final^2 * G m^2 / (hbar l)

## 6. Quantum-classical boundary

    **m* = sqrt(hbar l / (G t_obs))**

Objects heavier than m* at separation l decohere gravitationally within time t_obs.

## 7. Many-body Diosi functional

For N point masses:

    Lambda = (G/hbar) sum_{i,j} m_i m_j [1/d_LL + 1/d_RR - 1/d_LR - 1/d_RL]

Self-terms (i=j): standard USL per particle.
Cross-terms (i!=j): depend on quantum state (entangled vs product).

## 8. Bell-state protection and GHZ suppression

**Bell state** |LR> + |RL>: center of mass fixed, self-energy difference reduced.
- At d = 200 nm: Bell rate is 17% lower than product rate.
- At d = 150 nm: 53% lower.

**GHZ state** |LL...L> + |RR...R> at d = 200 nm:
- N=2: 33% suppression vs product
- N=5: 58%
- N=10: 67%
- N=20: 72%

## 9. Six-signature discriminant

| # | Signature | Structural origin | Discriminates against |
|---|-----------|-------------------|----------------------|
| 1 | Pressure plateau | Intrinsic Lambda != 0 | Standard QM |
| 2 | Geometry 193x span | Extended-body S(l/R) | DP point-mass |
| 3 | Entanglement -17% | Correlated mass distribution | CSL, nuisance floors |
| 4 | l-scaling slope -1 | USL form | CSL |
| 5 | Kink at l~1.8R | Near/far crossover | Single smooth power-law |
| 6 | Mass-squared ratio | Internal closure | Self-consistency |

No tested alternative reproduces all six simultaneously.

## 10. Experimental status

- All predictions consistent with existing bounds (OTIMA, KDTLI)
- GRUT signal is 10^-16 at current experimental masses (undetectable)
- Testable regime: m > 10 pg, P < 10^-9 Pa
- Timeline: 5-15 years
- Decisive test: pressure plateau measurement
