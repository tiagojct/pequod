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
