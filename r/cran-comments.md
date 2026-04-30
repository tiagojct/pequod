# CRAN submission — pequod 0.2.0

## Update — 2026-04-30

This is a minor-version update to the previously-published `pequod`
0.1.1 (CRAN, 2026-04-24). The colour values shipped in
`pequod_log`, `pequod_crew_light`, `pequod_crew_dark`, and the
internal `.pequod_palette_map()` lookup have all changed —
deliberately, to fix two issues that the upstream colour-vision
deficiency check was already flagging in 0.1.x:

1. The 12-step `pequod_log` sequential scale was non-monotonic in
   CIE L\* between stops 8 and 9 (Log 600 was darker than Log 700).
   This produced "stripey" contour rings on continuous fills. The
   new ramp is strictly monotonic with even ΔL\* spacing.
2. The eight crew accents had two pair-collapses under
   colour-vision-deficiency simulation: ΔE = 1.0 (Pip ↔ Stubb under
   tritanopia) and ΔE = 2.8 (Ahab ↔ Daggoo under protanopia-dark).
   The new accents — re-tuned in CIE-LCh — clear ΔE ≥ 6.8 across
   all three dichromatic simulations; the only remaining "close"
   pair is Ishmael ↔ Tashtego under deuteranopia (green collapses
   to neutral grey, mathematically unavoidable for any palette
   including both).

No API changes. All exported functions (`palette_pequod`,
`scale_color_pequod_d`/`_c`, `scale_fill_pequod_d`/`_c`,
`pequod_preview`, `scale_colour_pequod_*` UK aliases) keep their
v0.1.1 signatures. Existing user code that called these functions
continues to work; only the returned hex values have changed.

The full hex map (v0.1.1 → v0.2.0) is documented in the upstream
`CHANGELOG.md`
(<https://github.com/tiagojct/pequod/blob/main/CHANGELOG.md>).

There are no reverse dependencies on CRAN.

## R CMD check results — pequod 0.2.0

Local check:

* `R CMD check --as-cran pequod_0.2.0.tar.gz`
* 0 errors, 0 warnings, 3 NOTEs.

### NOTEs and explanations

1. **CRAN incoming feasibility** — maintainer note, standard for
   updates.
2. **Future file timestamps** — local clock NTP issue on the build
   machine; unrelated to the package contents.
3. **HTML Tidy validation skipped** — same environmental note that
   accompanied 0.1.0 / 0.1.1; my local `tidy` binary predates the
   version CRAN expects.

## Test environments

* Local: macOS Tahoe 26.4, R 4.5.2 (aarch64-apple-darwin20).
* GitHub Actions CI (R-release / R-devel × macOS / Ubuntu / Windows)
  green at the v0.2.0 tag.

## Reverse dependencies

None on CRAN.

---

Earlier submission notes (preserved for context) follow.

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
