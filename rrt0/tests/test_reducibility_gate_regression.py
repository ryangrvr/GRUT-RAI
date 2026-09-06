"""Regression test: eigh must NEVER be applied to the non-Hermitian unitary U.

Root cause of the superseded failed audit
(reports/REDUCIBILITY_GATE.FAILED-eigh_on_unitary-*.json):
the "independent" propagator was built as V diag(w^t) V^dagger with
w, v = np.linalg.eigh(U). U is unitary, NOT Hermitian, so eigh silently
returns garbage and produced max residuals ~597. This test fails if that
route ever reappears in the gate script or if any code path applies eigh
to U without a Hermiticity guard.
"""
import ast
import re
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT.parent))

from rrt0.model.core import (  # noqa: E402
    D, DT, SEED_PRIMARY, gue_hamiltonian, step_unitary,
)

GATE = ROOT / "scripts" / "run_reducibility_gate.py"


# ---------------------------------------------------------------------------
# 1. Static check: no unguarded eigh on non-Hermitian arguments anywhere in
#    the model or scripts tree (the gate script, sectors, etc.).
#    AST-based: catches any argument expression, not just the literal "U".
# ---------------------------------------------------------------------------
_SCAN_ROOTS = [ROOT / "model", ROOT / "scripts"]


def _is_hermitian_guarded(func_node, arg_name):
    """True if the enclosing function asserts Hermiticity of arg_name before
    calling eigh on it (e.g. support_projector asserts
    norm(op - op.conj().T) < tol immediately before eigh(op)).
    Such calls are valid; eigh is only a Hermitian solver."""
    for stmt in ast.walk(func_node):
        if isinstance(stmt, ast.Assert) and stmt.lineno is not None:
            seg = (ast.get_source_segment(
                getattr(func_node, "_src", ""), stmt) or "")
            if (arg_name in seg
                    and ("conj()" in seg or "ermitian" in seg)):
                return True
    return False


def test_no_eigh_on_non_hermitian_args_anywhere():
    offenders = []
    for root in _SCAN_ROOTS:
        for path in sorted(root.rglob("*.py")):
            src = path.read_text()
            tree = ast.parse(src)
            # map line numbers to enclosing top-level function nodes
            funcs = [n for n in ast.walk(tree)
                     if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
            for node in ast.walk(tree):
                if (isinstance(node, ast.Call)
                        and isinstance(node.func, ast.Attribute)
                        and node.func.attr == "eigh"):
                    if not node.args:
                        continue
                    arg_src = ast.get_source_segment(src, node.args[0]) or ""
                    if re.search(r"\b[Hh]\b", arg_src):
                        continue  # argument named H — the Hermitian generator
                    enclosing = next((f for f in funcs
                                      if f.lineno <= node.lineno <= f.end_lineno),
                                     None)
                    if enclosing is not None:
                        enclosing._src = src
                        if _is_hermitian_guarded(enclosing, arg_src.strip()):
                            continue
                    rel = path.relative_to(ROOT)
                    offenders.append(
                        f"{rel}:{node.lineno} eigh({arg_src})"
                    )
    assert not offenders, (
        "np.linalg.eigh applied to a non-H(ermitian) argument — this is the "
        "invalid route that produced the superseded failed audit:\n"
        + "\n".join(offenders)
    )


# ---------------------------------------------------------------------------
# 2. Numeric check: eigh on a generic unitary is demonstrably invalid,
#    while both valid routes reproduce U^tau correctly.
# ---------------------------------------------------------------------------
def _make_U():
    rng = np.random.default_rng(SEED_PRIMARY)
    H = gue_hamiltonian(rng)
    return H, step_unitary(H)


def test_eigh_on_unitary_is_invalid_and_valid_routes_agree():
    H, U = _make_U()

    # U really is NOT Hermitian (the invalid assumption of the failed route)
    assert np.linalg.norm(U - U.conj().T) > 1e-3

    # The failed route: eigh on U. It does NOT reproduce U^1 faithfully
    # (this is exactly the bug that produced the 597-residual report).
    w_bad, v_bad = np.linalg.eigh(U)
    U_bad = (v_bad * w_bad) @ v_bad.conj().T
    assert np.linalg.norm(U_bad - U, ord="fro") > 1e-6, (
        "eigh(U) unexpectedly reproduced U — the invalid route would go undetected"
    )

    # Route A: repeated multiplication of the validated unitary
    Ut_A = np.linalg.matrix_power(U, 17)
    Ut_A_inv = np.linalg.matrix_power(U.conj().T, 17)
    assert np.linalg.norm(Ut_A @ Ut_A_inv - np.eye(D), ord="fro") < 1e-12

    # Route B: spectral decomposition of the Hermitian generator H
    assert np.linalg.norm(H - H.conj().T, ord="fro") < 1e-12
    wH, vH = np.linalg.eigh(H)
    Ut_B = (vH * np.exp(-1j * wH * 17 * DT)) @ vH.conj().T

    # The two VALID routes must agree to numerical precision
    assert np.linalg.norm(Ut_A - Ut_B, ord="fro") < 1e-10
