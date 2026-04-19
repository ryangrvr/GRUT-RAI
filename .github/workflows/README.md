# GRUT-RAI CI Workflows

## test.yml

Runs on every push to `main` or `v2`, and on every pull request.

### What it does

1. Matrix: Ubuntu + macOS × Python 3.10/3.11/3.12/3.13 (8 configurations)
2. Install deps from `requirements.txt`
3. Run tests per sector (foundation, derived, bridge, utils) for clear
   failure attribution
4. Full test suite
5. Headline-value verification: directly asserts R_ANOMALY = 1.15428,
   τ_0 = 41.9 Myr, Koide K = 2/3, Ω_Λ within 1% of Planck

### Why the verification step is separate

Even if tests pass, the verification step serves as a second line of
defense against silent numerical drift. If a test assertion's tolerance
is ever loosened accidentally, this step catches the regression at a
more obvious level.

### Expected runtime

- Per job: ~30-60 seconds (installs are the slow part, tests are <1s)
- Total CI time for a push: ~1-2 minutes across all 8 matrix entries
  (run in parallel on GitHub Actions)

### When a run fails

1. Check the matrix entry that failed (OS × Python version)
2. Check which step failed (install, foundation, derived, bridge,
   utils, full, or verification)
3. If it's specific to one Python version or OS, flag as a compatibility
   issue and document the workaround
4. If it's the verification step, a V7 headline value has drifted;
   treat as a regression and investigate

### Regression policy

If `pytest` or verification fails on a PR, the PR does not merge.
Fix the code, not the test. The only valid test change is tightening
tolerance (never loosening).
