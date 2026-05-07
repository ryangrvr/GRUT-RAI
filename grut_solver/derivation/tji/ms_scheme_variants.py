"""MS-family scheme absorption factor variants for dimensional regularization."""

import sympy as sp
from sympy import symbols, gamma, log, pi, series, exp
from typing import Dict

EPS = symbols('epsilon', real=True)


class MSSchemeVariant:
    """Base class for MS-family absorption conventions."""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def absorption_factor(self, n_loops: int = 2, order: int = 3) -> sp.Expr:
        raise NotImplementedError

    def per_loop_factor(self, order: int = 3) -> sp.Expr:
        raise NotImplementedError


class CollinsMSBar(MSSchemeVariant):
    """Standard MS-bar (Collins 1984): Γ(1+ε)^(-1) · (4π)^ε"""
    def __init__(self):
        super().__init__("Collins MS-bar", "Standard: Γ(1+ε)^(-1) · (4π)^ε")

    def per_loop_factor(self, order: int = 3) -> sp.Expr:
        return (1 / gamma(1 + EPS)) * (4 * pi) ** EPS

    def absorption_factor(self, n_loops: int = 2, order: int = 3) -> sp.Expr:
        per_loop = self.per_loop_factor(order)
        factor = per_loop ** n_loops
        expanded = series(factor, EPS, 0, n=order)
        return expanded


class FeynCalcVariant(MSSchemeVariant):
    """FeynCalc-like variant with exp(γ_E)."""
    def __init__(self):
        super().__init__("FeynCalc variant", "With exp(γ_E) factor")

    def per_loop_factor(self, order: int = 3) -> sp.Expr:
        return exp(sp.EulerGamma) * (1 / gamma(1 + EPS)) * (4 * pi) ** EPS

    def absorption_factor(self, n_loops: int = 2, order: int = 3) -> sp.Expr:
        per_loop = self.per_loop_factor(order)
        factor = per_loop ** n_loops
        try:
            expanded = series(factor, EPS, 0, n=order)
            return expanded
        except:
            return per_loop


class MSPrime(MSSchemeVariant):
    """MS-prime: Γ(1+ε)^(-1) · (4π)^(-ε)"""
    def __init__(self):
        super().__init__("MS-prime", "With inverse scale: (4π)^(-ε)")

    def per_loop_factor(self, order: int = 3) -> sp.Expr:
        return (1 / gamma(1 + EPS)) * ((4 * pi) ** (-EPS))

    def absorption_factor(self, n_loops: int = 2, order: int = 3) -> sp.Expr:
        per_loop = self.per_loop_factor(order)
        factor = per_loop ** n_loops
        try:
            expanded = series(factor, EPS, 0, n=order)
            return expanded
        except:
            return per_loop


class GammaOnly(MSSchemeVariant):
    """Simplified: just Γ(1+ε)^(-1)"""
    def __init__(self):
        super().__init__("Gamma-only", "Just Γ(1+ε)^(-1) expansion")

    def per_loop_factor(self, order: int = 3) -> sp.Expr:
        return 1 / gamma(1 + EPS)

    def absorption_factor(self, n_loops: int = 2, order: int = 3) -> sp.Expr:
        per_loop = self.per_loop_factor(order)
        factor = per_loop ** n_loops
        try:
            expanded = series(factor, EPS, 0, n=order)
            return expanded
        except:
            return per_loop


class SimpleScale(MSSchemeVariant):
    """Simple log(2) scale: Γ(1+ε)^(-1) · exp(ε·ln(2))"""
    def __init__(self):
        super().__init__("Simple scale", "With exp(ε·ln(2)) factor")

    def per_loop_factor(self, order: int = 3) -> sp.Expr:
        return (1 / gamma(1 + EPS)) * exp(EPS * log(2))

    def absorption_factor(self, n_loops: int = 2, order: int = 3) -> sp.Expr:
        per_loop = self.per_loop_factor(order)
        factor = per_loop ** n_loops
        try:
            expanded = series(factor, EPS, 0, n=order)
            return expanded
        except:
            return per_loop


SCHEME_REGISTRY: Dict[str, MSSchemeVariant] = {
    'collins_ms_bar': CollinsMSBar(),
    'feyncalc_variant': FeynCalcVariant(),
    'ms_prime': MSPrime(),
    'gamma_only': GammaOnly(),
    'simple_scale': SimpleScale(),
}


def get_scheme(name: str) -> MSSchemeVariant:
    if name not in SCHEME_REGISTRY:
        raise ValueError(f"Unknown scheme: {name}")
    return SCHEME_REGISTRY[name]


def list_schemes() -> Dict[str, str]:
    return {name: scheme.description for name, scheme in SCHEME_REGISTRY.items()}
