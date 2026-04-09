"""
GRUT Solver — Command-Line Interface

Usage:
    grut compute --mass 1e-14 --radius 50e-9 --separation 100e-9
    grut compute --mass 1e-14 --radius 50e-9 --separation 100e-9 --T 0.01 --P 1e-10
    grut boundary --separation 1e-7 --time 1.0
    grut kill
    grut figures [output_dir]
    grut test
    grut self-test
    grut info
"""

import sys
import argparse


def cmd_compute(args):
    from grut_solver import GRUTSolver
    solver = GRUTSolver()
    r = solver.decoherence(
        m=args.mass, R=args.radius, l=args.separation,
        T_env=args.T, P=args.P,
    )
    print(f"GRUT Decoherence Budget")
    print(f"{'='*50}")
    print(f"  Mass:           {args.mass:.2e} kg")
    print(f"  Radius:         {args.radius*1e9:.0f} nm")
    print(f"  Separation:     {args.separation*1e9:.0f} nm")
    print(f"  Temperature:    {args.T*1e3:.0f} mK")
    print(f"  Pressure:       {args.P:.0e} Pa")
    print(f"{'='*50}")
    print(f"  Lambda_grav:    {r.lambda_grav:.2e} Hz  (zero free parameters)")
    print(f"  Lambda_total:   {r.lambda_total:.2e} Hz")
    print(f"  S(l/R):         {r.S_extended:.4f}")
    print(f"  SNR (grav/env): {r.signal_to_noise:.1f}")
    print(f"  Binding:        {r.binding_channel}")
    print(f"  Testable:       {r.is_testable}")
    print(f"  t_coherence:    {r.t_coherence:.2e} s")
    print()
    print(f"  Competing models:")
    print(f"    DP point-mass: {r.lambda_dp_point:.2e} Hz")
    print(f"    CSL (GRW):     {r.lambda_csl_grw:.2e} Hz")
    print(f"    Standard QM:   0 Hz")


def cmd_boundary(args):
    from grut_solver.usl.gravitational import boundary_mass
    m = boundary_mass(args.separation, args.time)
    print(f"Quantum-classical boundary mass:")
    print(f"  l = {args.separation:.2e} m, t = {args.time:.2e} s")
    print(f"  m* = {m:.2e} kg = {m*1e15:.2f} fg")


def cmd_kill(args):
    from grut_solver.kill.model_comparison import run_all_kill_tests, kill_summary
    results = run_all_kill_tests()
    print(kill_summary(results))


def cmd_figures(args):
    from grut_solver.figures import generate_all
    out = args.output if args.output else "paper_figures"
    generate_all(out_dir=out)


def cmd_test(args):
    import subprocess
    subprocess.run([sys.executable, "tests/test_grut_solver.py"], check=False)


def cmd_selftest(args):
    import subprocess
    subprocess.run([sys.executable, "grut_solver/self_test.py"], check=False)


def cmd_info(args):
    from grut_solver import __version__
    from grut_solver.constants import C_FINAL, TAU_I, HBAR
    print(f"GRUT Solver v{__version__}")
    print(f"  tau_I = hbar/2 = {TAU_I:.6e} J s")
    print(f"  C_Final = {C_FINAL:.6e}")
    print(f"  12 sectors, 122 tests, 9 applications")
    print(f"  Zero free parameters in the gravitational decoherence sector")


def main():
    parser = argparse.ArgumentParser(
        prog="grut",
        description="GRUT Solver — zero-parameter gravitational decoherence framework",
    )
    sub = parser.add_subparsers(dest="command")

    # compute
    p_comp = sub.add_parser("compute", help="Compute decoherence budget")
    p_comp.add_argument("--mass", "-m", type=float, required=True, help="Mass [kg]")
    p_comp.add_argument("--radius", "-r", type=float, required=True, help="Radius [m]")
    p_comp.add_argument("--separation", "-l", type=float, required=True, help="Separation [m]")
    p_comp.add_argument("--T", type=float, default=10e-3, help="Temperature [K]")
    p_comp.add_argument("--P", type=float, default=1e-10, help="Pressure [Pa]")

    # boundary
    p_bnd = sub.add_parser("boundary", help="Quantum-classical boundary mass")
    p_bnd.add_argument("--separation", "-l", type=float, required=True)
    p_bnd.add_argument("--time", "-t", type=float, required=True)

    # kill
    sub.add_parser("kill", help="Run adversarial kill tests")

    # figures
    p_fig = sub.add_parser("figures", help="Generate paper figures")
    p_fig.add_argument("output", nargs="?", default=None)

    # test
    sub.add_parser("test", help="Run solver test suite")
    sub.add_parser("self-test", help="Run full self-test protocol")

    # info
    sub.add_parser("info", help="Package information")

    args = parser.parse_args()

    if args.command == "compute":
        cmd_compute(args)
    elif args.command == "boundary":
        cmd_boundary(args)
    elif args.command == "kill":
        cmd_kill(args)
    elif args.command == "figures":
        cmd_figures(args)
    elif args.command == "test":
        cmd_test(args)
    elif args.command == "self-test":
        cmd_selftest(args)
    elif args.command == "info":
        cmd_info(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
