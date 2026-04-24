# CRAN submission — pequod 0.1.0

This is a new submission.

## Resubmission — 2026-04-24

Previous submission flagged a relative file URI in `README.md` linking
to `../README.md` (Uwe Ligges, 2026-04-24). That worked inside the
repository — where the R package lives in `r/` and the link walks up
to the repository-root README — but failed on CRAN, which extracts
the package as a standalone tarball.

Fixed in this resubmission: the link now points at the absolute
GitHub URL for the repository README
(<https://github.com/tiagojct/pequod/blob/main/README.md>), which
resolves correctly both on CRAN and on GitHub. No other changes.

## R CMD check results

Local check:

* `R CMD check --as-cran pequod_0.1.0.tar.gz`
* 0 errors, 0 warnings, 2 NOTEs.

### NOTEs and explanations

1. **New submission / Package was archived on CRAN.**

   A package named `pequod` existed on CRAN between 2010 and 2016 (a
   moderated-regression tool by Mirko Di Rosa) and was archived on
   2024-04-20.

   This submission is **unrelated in scope and authorship**: it
   provides a colour palette and `ggplot2` scales, has a different
   maintainer, and shares only the project name (chosen
   independently after Melville's *Moby-Dick*, which is also the
   theme of the accent hues). The archived package's source lives in
   `Archive/pequod/` and is not referenced or reused here. I am
   happy to rename the package if CRAN prefers the previous name
   remain out of circulation.

2. **HTML Tidy validation skipped.**

   My local `tidy` binary is older than the version CRAN expects.
   This is an environmental note and does not indicate a problem
   with the package.

## Downstream dependencies

There are none — this is a new submission.

## Test environments

* Local: macOS Tahoe 26.4, R 4.5.2 (aarch64-apple-darwin20).
* GitHub Actions CI (if available post-submission): intended to run
  R-release and R-devel on macOS, Ubuntu, and Windows.

## Reverse dependencies

None (new submission).
