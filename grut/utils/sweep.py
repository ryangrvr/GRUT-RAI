"""Parameter Sweep & Sensitivity Analysis Engine."""
import numpy as np
from grut.foundation.noise_kernel import lambda_grav, extended_body_suppression
from grut.foundation.anomaly import R_ANOMALY, S_CTP

TAU_0 = 41.9e6 * 3.156e7

def sweep_1d(func, param_name, values, fixed_params=None):
    """Sweep a single parameter and collect results."""
    fixed = fixed_params or {}
    results = []
    for v in values:
        params = {**fixed, param_name: v}
        results.append({"param": float(v), "result": func(**params)})
    return results

def sensitivity_omega_lambda(delta_pct=10):
    """How much does Omega_Lambda shift when each input changes by delta_pct%."""
    H_0 = 70e3 / 3.0857e22
    base_OL = ((2-R_ANOMALY)/(S_CTP*TAU_0*H_0))**2
    results = {}
    for name, base_val, getter in [
        ("R_anomaly", R_ANOMALY, lambda v: ((2-v)/(S_CTP*TAU_0*H_0))**2),
        ("S_CTP", S_CTP, lambda v: ((2-R_ANOMALY)/(v*TAU_0*H_0))**2),
        ("tau_0", TAU_0, lambda v: ((2-R_ANOMALY)/(S_CTP*v*H_0))**2),
        ("H_0", H_0, lambda v: ((2-R_ANOMALY)/(S_CTP*TAU_0*v))**2),
    ]:
        shifted = base_val * (1 + delta_pct/100)
        OL_shifted = getter(shifted)
        results[name] = {"base": base_OL, "shifted": OL_shifted,
                         "delta_OL_pct": (OL_shifted/base_OL - 1)*100}
    return results

def uncertainty_propagation(m, l, R, dm_frac=0.01, dl_frac=0.01, dR_frac=0.01):
    """Propagate measurement uncertainties to Lambda_grav."""
    L0 = lambda_grav(m, l, R)
    dL_dm = (lambda_grav(m*(1+dm_frac), l, R) - lambda_grav(m*(1-dm_frac), l, R)) / (2*m*dm_frac)
    dL_dl = (lambda_grav(m, l*(1+dl_frac), R) - lambda_grav(m, l*(1-dl_frac), R)) / (2*l*dl_frac)
    dL_dR = (lambda_grav(m, l, R*(1+dR_frac)) - lambda_grav(m, l, R*(1-dR_frac))) / (2*R*dR_frac)
    sigma_L = np.sqrt((dL_dm*m*dm_frac)**2 + (dL_dl*l*dl_frac)**2 + (dL_dR*R*dR_frac)**2)
    return {"Lambda": L0, "sigma_Lambda": sigma_L, "relative_pct": sigma_L/L0*100,
            "partials": {"dL/dm": dL_dm, "dL/dl": dL_dl, "dL/dR": dL_dR}}
