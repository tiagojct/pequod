# Changelog

All notable changes to Pequod will be documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html),
with the understanding that versions below 1.0 are alpha and breaking
changes may still occur between 0.x releases.

## [0.1.0-alpha] — 2026-04-23

First public release.

### Added

- `pequod.json` — canonical palette tokens: twelve-step Log base scale,
  eight crew accents (each with light/dark variants and syntax role),
  light- and dark-mode role mappings, and default syntax assignments.
- `themes/Pequod.itermcolors` — iTerm2 dark colour scheme.
- `themes/Pequod-color-theme.json` — VS Code dark theme.
- `themes/Pequod-light-color-theme.json` — VS Code light theme.
- `themes/Pequod.zed.json` — Zed theme family with dark and light
  variants in a single file.
- `scripts/cvd_check.py` — Viénot–Brettel–Mollon CVD simulation with
  pairwise ΔE reporting for all eight accents across protanopia,
  deuteranopia, and tritanopia, for both light and dark variants.
- Licence files: CC-BY-4.0 for the palette tokens and documentation,
  MIT for the theme files and scripts.

### Added (follow-up)

- `specimen/specimen.typ` + rendered `specimen/specimen.pdf` — a
  one-page A4 reference showing the Log scale, the eight crew
  accents (light and dark variants), a body-text sample, and a dark
  code sample with every token coloured by its crew role. Rendered
  with Typst against system-installed Geist / Geist Mono.
- `r/` — an installable R package. Exposes `pequod_log`,
  `pequod_crew_light`, `pequod_crew_dark`, `pequod_crew`, a general
  `palette_pequod()` helper (discrete + continuous, six named
  palettes), ggplot2 scales `scale_color_pequod_d/c` and
  `scale_fill_pequod_d/c` (both UK and US spellings), and a
  `pequod_preview()` base-R visualiser. Install with
  `remotes::install_github("tiagojct/pequod", subdir = "r")`.
  Palette data is generated from `pequod.json` by
  `r/data-raw/generate_palettes.R`, so the R package cannot drift
  from the canonical tokens.
- `Makefile` — `specimen`, `cvd`, `r-data` (regenerate the R
  palette from the JSON), `r-check` (R CMD check), and `clean`
  targets.
- `cover.jpg` bundled in the repo root (README no longer depends on
  an external URL).

### Fixed (follow-up)

- `specimen/specimen.typ`: accent-chip text colour was inverted
  (cream on already-light chips, navy on already-dark chips) and
  hex labels were clipped by the column width. Flipped the colour
  logic and widened the chips to 5.2em.

### Added (2026-04-25)

- `vscode/` — the dark and light themes packaged as a Visual Studio
  Marketplace extension. Includes `package.json`, README,
  CHANGELOG, MIT LICENSE, a 128×128 icon (eight crew accents on a
  Log 950 background), and `.vscodeignore`. Build the .vsix with
  `make vsix`; publish with `make vsce-publish` (requires a
  publisher account and PAT). Theme files inside `vscode/themes/`
  are copies of the canonical files under `/themes/`. Marketplace
  extension ID: `tiagojct.pequod-color-theme` (the `pequod-theme`
  slug was already reserved on the VS Marketplace global
  namespace, so this one falls back to the more explicit
  VS-Code-convention name).

### Known limitations

- Theme files are hand-maintained; they do not yet regenerate
  automatically from `pequod.json`. Generators are the next
  priority — until they exist, tokens in `pequod.json` and colours
  in the theme files must be kept in sync by hand.
- No iTerm2 light preset yet.
- Light-mode contrast on Log 100 for Pip (3.3), Stubb (3.8), and
  Starbuck (4.1) falls below AA-body; these accents are tuned for
  bold, large text, or UI use. The dark-mode counterparts all clear
  AA-body on Log 950.
- Under tritanopia, Pip and Stubb collapse to near-identical values
  (ΔE 1.0 / 2.3). Under protanopia, Ahab and Daggoo collapse
  (ΔE 4.6 / 2.8). Do not rely on colour alone for these pairs —
  pair with icon, weight, or position.
