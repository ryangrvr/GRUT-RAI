"""
Osborn Assembly Module — Final R Computation from Brother's Three Inputs

This module assembles the three pieces the brother will compute into the
final R and Omega_Lambda prediction. It takes honest inputs and produces
whatever answer falls out — no target-guided adjustments.

THE THREE INPUTS THE BROTHER WILL PROVIDE:

1. c_w: The w_i coefficients for SM fields from the BoxR anomaly coefficient
   at 1-loop. Extractable from Jack & Osborn (NPB 343, 1990) and the
   individual field contributions to b' in Birrell-Davies / Vassilevich.

2. delta_beta_b_integrated: The integrated shift in beta_b from M_Planck
   to M_Z using c_w in the Osborn equation.

3. absorptive_contribution (optional): Additional imaginary-part contribution
   from CTP absorptive structure at 2-loop, if it turns out to be nonzero.

The module takes these three values, applies the Osborn consistency
relations, and computes the resulting R = |beta_b / beta_a| and
Omega_Lambda = (H_inf / H_0)^2.

PRINCIPLE: Whatever comes out, comes out. If Omega_Lambda matches Planck,
the framework survives. If it doesn't, the framework's prediction adjusts
to whatever the honest calculation gives.
"""

import math


def compute_omega_lambda_from_inputs(
    c_w_scalar=None,
    c_w_dirac=None,
    c_w_vector=None,
    delta_beta_b_integrated=None,
    absorptive_contribution=0.0,
    H_0=70.0,
    neutrino_type="weyl",
):
    """Assemble the brother's three inputs into the final Omega_Lambda.

    Parameters
    ----------
    c_w_scalar : float or None
        The w_i coefficient for a real scalar field (from BoxR anomaly).
        If None, prints a note asking for it.
    c_w_dirac : float or None
        The w_i coefficient for a Dirac fermion.
    c_w_vector : float or None
        The w_i coefficient for a vector (gauge) boson.
    delta_beta_b_integrated : float or None
        The integrated shift Delta_beta_b from M_Planck to M_Z with the
        actual c_w values plugged in. If None, uses the order-of-magnitude
        estimate from integrated_rg_flow_estimate().
    absorptive_contribution : float
        Additional contribution to Delta_beta_b from CTP absorptive parts
        at 2-loop. Default 0 (ignore).
    H_0 : float
        Hubble constant in km/s/Mpc. Default 70.
    neutrino_type : str
        "weyl" or "dirac" for the 1-loop SM content.

    Returns
    -------
    dict with the full chain: inputs -> R -> H_inf -> Omega_Lambda
    """
    from grut.foundation.anomaly_derived import (
        compute_R_one_loop, sm_field_content
    )

    # Get the 1-loop baseline
    one_loop = compute_R_one_loop(neutrino_type)
    a_SM = one_loop['coefficients']['a_SM_float']
    b_SM = one_loop['coefficients']['b_SM_float']
    R_1loop = one_loop['R_1loop']['float']

    # Assemble c_w for the full SM field content
    sm = sm_field_content(neutrino_type)

    c_w_sum = None
    if all(v is not None for v in [c_w_scalar, c_w_dirac, c_w_vector]):
        c_w_sum = (
            sm['N_s'] * c_w_scalar +
            float(sm['N_f']) * c_w_dirac +
            sm['N_v'] * c_w_vector
        )

    # If brother has provided the integrated shift, use it directly
    # Otherwise, use the order-of-magnitude estimate
    if delta_beta_b_integrated is None:
        from grut.foundation.osborn_rg import integrated_rg_flow_estimate
        est = integrated_rg_flow_estimate()
        # Use midrange estimate (20% asymmetry)
        delta_beta_b_est = 0.5 * (
            est['R_shift_estimate_low_asymmetry_10pct'] +
            est['R_shift_estimate_high_asymmetry_30pct']
        ) * b_SM
        delta_beta_b_used = delta_beta_b_est
        delta_source = "order-of-magnitude estimate (midrange)"
    else:
        delta_beta_b_used = delta_beta_b_integrated
        delta_source = "brother's actual calculation"

    # Total shift in beta_b (real + absorptive)
    total_delta_beta_b = delta_beta_b_used + absorptive_contribution

    # Final beta_b and R
    # At leading order, beta_a shifts in lockstep with beta_b via chi^g
    # but the asymmetry (from c_w in b, not in a) is what changes the ratio.
    # The "delta_beta_b_integrated" input from the brother should represent
    # the ASYMMETRIC part — the piece that would NOT be present in a's equation.
    # So we apply this shift only to b.
    beta_b_final = b_SM + total_delta_beta_b
    beta_a_final = a_SM  # no corresponding shift in a equation

    R_final = abs(beta_b_final / beta_a_final)

    # Framework formula: H_inf = (2 - R) / (S * tau_0)
    # With the asserted S = 108pi and tau_0 = 41.9 Myr
    S = 108 * math.pi
    tau_0 = 1.322e15  # seconds (41.9 Myr)

    f_R_1loop = 2 - R_1loop
    f_R_final = 2 - R_final

    H_inf_1loop = f_R_1loop / (S * tau_0)
    H_inf_final = f_R_final / (S * tau_0)

    # Convert H_0 to Hz: H_0 [Hz] = H_0 [km/s/Mpc] / (1 Mpc in km) * (1/s)
    H_0_Hz = H_0 * 1e3 / (3.086e22)  # km/s per Mpc -> Hz

    Omega_Lambda_1loop = (H_inf_1loop / H_0_Hz) ** 2
    Omega_Lambda_final = (H_inf_final / H_0_Hz) ** 2

    Omega_Lambda_observed = 0.6889  # Planck 2018

    return {
        'status': ('FINAL R AND OMEGA_LAMBDA from brother\'s inputs' if
                   delta_beta_b_integrated is not None else
                   'PROVISIONAL (using order-of-magnitude estimate)'),
        'delta_source': delta_source,
        'inputs': {
            'c_w_scalar': c_w_scalar,
            'c_w_dirac': c_w_dirac,
            'c_w_vector': c_w_vector,
            'c_w_sum_over_SM': c_w_sum,
            'delta_beta_b_integrated': delta_beta_b_integrated,
            'absorptive_contribution': absorptive_contribution,
        },
        'baseline': {
            'a_SM_1loop': a_SM,
            'b_SM_1loop': b_SM,
            'R_1loop': R_1loop,
            'neutrino_type': neutrino_type,
        },
        'computed': {
            'total_delta_beta_b': total_delta_beta_b,
            'beta_b_final': beta_b_final,
            'beta_a_final': beta_a_final,
            'R_final': R_final,
            'f_R_final': f_R_final,
            'H_inf_final_Hz': H_inf_final,
        },
        'omega_lambda': {
            'Omega_Lambda_1loop_only': Omega_Lambda_1loop,
            'Omega_Lambda_with_shifts': Omega_Lambda_final,
            'Omega_Lambda_observed_Planck': Omega_Lambda_observed,
            'deviation_pct': (
                (Omega_Lambda_final - Omega_Lambda_observed) /
                Omega_Lambda_observed * 100
            ),
        },
        'verdict': _make_verdict(Omega_Lambda_final, Omega_Lambda_observed,
                                  delta_beta_b_integrated),
        'formula_used': 'H_inf = (2 - R) / (S * tau_0), S = 108pi, tau_0 = 41.9 Myr',
        'honest_note': (
            'S = 108pi and tau_0 = 41.9 Myr are themselves NOT derived '
            'from first principles. If R comes out correctly but Omega_Lambda '
            'is wrong, the next question is: are S and tau_0 correctly '
            'identified from CTP structure, or do they also need derivation? '
            'The observed Omega_Lambda + honest R together constrain '
            'S * tau_0 = (2 - R) / (H_0 * sqrt(Omega_Lambda)).'
        ),
    }


def _make_verdict(omega_final, omega_obs, had_real_input):
    """Produce a verdict string based on the computed Omega_Lambda."""
    deviation = abs(omega_final - omega_obs) / omega_obs * 100

    if not had_real_input:
        return f'PROVISIONAL: with order-of-magnitude estimate, Omega_Lambda = {omega_final:.4f}. Awaiting brother\'s actual calculation.'

    if deviation < 1.0:
        return f'MATCH: Omega_Lambda = {omega_final:.4f} within 1% of Planck {omega_obs}. Framework survives.'
    elif deviation < 5.0:
        return f'CLOSE: Omega_Lambda = {omega_final:.4f} within 5% of Planck {omega_obs}. Framework has support but not perfect match.'
    elif deviation < 15.0:
        return f'NOTABLE GAP: Omega_Lambda = {omega_final:.4f}, {deviation:.1f}% from Planck. Framework partially works; other mechanisms needed.'
    else:
        return f'SIGNIFICANT GAP: Omega_Lambda = {omega_final:.4f}, {deviation:.1f}% from Planck. Either S/tau_0 also need correction, or framework structure needs revision.'


def show_current_state():
    """Display the current state of inputs needed vs what's available."""
    return {
        'needed_from_brother': {
            '1_c_w_coefficients': 'c_w_scalar, c_w_dirac, c_w_vector from 1-loop BoxR anomaly',
            '2_delta_beta_b_integrated': 'Integrated Delta beta_b from M_Planck to M_Z with c_w',
            '3_absorptive_contribution': 'Optional: CTP absorptive contribution at 2-loop',
        },
        'what_we_have': {
            'R_1loop': 1.02680,
            'a_SM': 283/120,
            'b_SM': -3487/1440,
            'order_of_magnitude_estimate': '5.4% to 16.2% R shift from integrated RG',
        },
        'next_step': (
            'When c_w values arrive, call compute_omega_lambda_from_inputs() '
            'with c_w_scalar, c_w_dirac, c_w_vector. If brother also computes '
            'the actual integrated delta_beta_b, pass that too. The module '
            'returns whatever Omega_Lambda falls out.'
        ),
    }
