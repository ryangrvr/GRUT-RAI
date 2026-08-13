PRE-REGISTRATION DIRECTORY -- the rule, and why it is a directory rather than a convention.

  A PRE-REGISTRATION IS IMMUTABLE ONCE HASHED. Results cite it; they never join it.

Layout:
  PREREG_<topic>_<date>.txt   expectations ONLY. Never edited after MANIFEST records its hash.
  RESULT_<topic>_<date>.txt   results, citing the prereg's hash.
  MANIFEST.txt                sha256 of every PREREG file, appended when written.

THE FAILURE THAT PRODUCED THIS (2026-08-04): the first pre-registration had its results APPENDED to
it after scoring, so the file on disk was no longer the file that was hashed. The substance was
sound -- expectations preceded results, and the honest limit was written into the expectations block
before any result existed -- but "verify by hash" became unverifiable, which is the entire point of
hashing it. This is the THIRD instance of one shape in this program: a record that describes itself
(FROZEN_MERGE v1's hash inside the file it described), a guard that bounds itself (OWED_CEILING
computed from OWED), and now an artifact that grows after being sealed. Enforced by
test_prereg_immutable.py.

================================ THE GENERALIZATION (added 2026-08-04) ================================
This rule -- prereg immutable after hashing, results in a separate citing file -- is the third fix of
ONE failure, and the pattern is worth more than the three fixes:

    A RECORD THAT DESCRIBES ITSELF.      (a selftest whose answer lived in its own print statement;
                                          a "two derivations agree" check that was a tautology)
    A GUARD THAT BOUNDS ITSELF.          (OWED_CEILING = frozenset(OWED) -- a ratchet computed from
                                          the very list it existed to bound)
    AN ARTIFACT THAT GROWS AFTER BEING   (results appended to the pre-registration they were
    SEALED.                               supposed to be tested against)

Three different failures, one structure: *** THE THING THAT CERTIFIES SITTING INSIDE THE THING BEING
CERTIFIED. *** Each was caught only by an outsider constructing a case the author's own controls had
already certified as clean.

WHAT TO DO WITH IT. When you build any check, ask where its authority comes from, and then ask
whether that source is downstream of what it is checking. If it is, the check is decorative no matter
how green it runs. The remedy is never a fourth hardening pass on the same object -- it is to move
the certifying thing OUTSIDE: an external hash, a frozen literal, a separate file, an adversary who
did not write the answer.

AND THE COROLLARY THIS PROGRAM PAID FOR FOUR TIMES: IF A TOOL CANNOT BE CERTIFIED, DO NOT LET THAT
TOOL CERTIFY ANYTHING. That is why the merge criterion was reframed as a declaration schema rather
than hardened a fourth time into a decision procedure.

================================ THE BLIND-SAFE RULE (added 2026-08-09) ================================
A pre-registration for any OBSERVATION-ADJACENT wave (one where an agent must be blinded to a
measurement) must carry the line "BLIND-SAFE: yes" and must then contain NO result-adjacent
numerics -- no sigma values, no tension ranges, no arXiv ids. Motive quantities go in a SEPARATE
file that CITES the prereg's hash. Enforced by test_prereg_immutable.py::TestBlindSafe.
WHY: the kappa wave's blinding failed through its own seal -- PREREG_KAPPA's motive paragraph
carried the tension sigmas, and the blinding protocol pointed every blinded agent at it. The
certifier inside the certified, sixth appearance, roles inverted: THE SEAL WAS THE LEAK. The sealed
file stays as recorded history (immutable); the rule binds every future prereg.

================================ FOURTEENTH INSTANCE (added 2026-08-10) ================================
The certifier-inside-the-certified shape, this time INSIDE A REMEDY FOR ITS OWN CLASS: the
draft disclosure entry for the v4 R1/R5 seam carried "where consumption was feasible" -- a
feasibility standard appearing in neither rule, which would have functioned as an unauthorized
gloss on what R1 means, in an entry whose entire purpose was to disclose without interpreting.
Caught by the external reviewer before logging; struck; recorded here with the others because
the remedy-authoring position turns out to be no safer than the artifact-authoring one.
