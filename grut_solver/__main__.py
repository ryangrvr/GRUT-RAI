"""CLI entrypoint: python -m grut_solver [figures|test]"""

import sys

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "figures":
        out = sys.argv[2] if len(sys.argv) > 2 else "paper_figures"
        from grut_solver.figures import generate_all
        generate_all(out_dir=out)
    else:
        print("Usage:")
        print("  python -m grut_solver figures [output_dir]")

if __name__ == "__main__":
    main()
