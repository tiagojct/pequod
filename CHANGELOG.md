# Changelog

All notable changes to Pequod will be documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html),
with the understanding that versions below 1.0 are alpha and breaking
changes may still occur between 0.x releases.

## [0.2.0-alpha] — 2026-04-30

A perceptual-correctness rewrite of the palette tokens. The Log
sequential scale now has monotonic, evenly-spaced luminance, and every
crew accent has been re-tuned in CIE-LCh to (a) clear AA-large contrast
on its target surface and (b) survive protanopia and tritanopia
simulation with worst-case ΔE ≥ 10 — fixing the catastrophic CVD
collapses documented under v0.1's "Known limitations".

### Changed (breaking — palette tokens)

- **Log scale**, all twelve stops repigmented. Step sizes are now
  evenly-spaced in CIE L\*: ΔL\* between successive stops ranges 5.0 to
  11.1 (was 1.2 to 25.7), and the scale is strictly monotonic — v0.1
  had a luminance reversal at step 8→9 (Log 600 was darker than Log
  700) that produced "stripey" contour rings on continuous fills. New
  hex codes:

  | Stop | v0.1 | v0.2 |
  |---|---|---|
  | Log 50  | `#FBFAF5` | `#F7F3EE` |
  | Log 100 | `#F8F4EB` | `#EAE1D7` |
  | Log 150 | `#ECE5D3` | `#DBC9B6` |
  | Log 200 | `#DFD3B8` | `#CFAD8E` |
  | Log 300 | `#C4A57B` | `#BD8C68` |
  | Log 400 | `#A8865E` | `#A16E50` |
  | Log 500 | `#8B7B6B` | `#835A49` |
  | Log 600 | `#6E5F52` | `#335260` |
  | Log 700 | `#527275` | `#163F54` |
  | Log 800 | `#2C3E50` | `#0D2F42` |
  | Log 900 | `#1C2936` | `#0C222F` |
  | Log 950 | `#13181F` | `#0B1720` |

- **Crew accents (light variants)** retuned. Each character keeps its
  hue role (red = Ahab, blue = Starbuck, …), but L\* is now laddered
  across the readable range [22, 54] so confusable hue pairs separate
  by lightness even under CVD. Ahab leans vermillion (h ≈ 32°) and
  Tashtego leans cyan-green (h ≈ 160°) for better deutan separation.
  Pip moves from a saturated mustard at L\* 24 to a deeper ochre at
  L\* 34 — keeps "warm yellow" character while gaining tritan distance
  from Stubb.

  | Crew | v0.1 light | v0.2 light |
  |---|---|---|
  | Ahab     | `#B5534A` | `#A83732` |
  | Starbuck | `#527C98` | `#0082B1` |
  | Queequeg | `#4A4E8C` | `#253E82` |
  | Pip      | `#A8812B` | `#6A4A00` |
  | Ishmael  | `#6E6E6B` | `#76716B` |
  | Stubb    | `#B5683A` | `#CA6435` |
  | Tashtego | `#507352` | `#177C55` |
  | Daggoo   | `#7A5440` | `#552823` |

- **Crew accents (dark variants)** repaired. v0.1's dark variants sat
  at clustered L\* ≈ 50 with several pairs collapsing to the same
  shade under deutan; v0.2 spreads them across L\* [58, 90] for
  deutan/protan separation and pulls the saturation down so they read
  as comfortable on Log 950 ink rather than glaring.

  | Crew | v0.1 dark | v0.2 dark |
  |---|---|---|
  | Ahab     | `#E07A72` | `#E3877C` |
  | Starbuck | `#7FA8C3` | `#A6DFFF` |
  | Queequeg | `#8A8ECE` | `#838CCF` |
  | Pip      | `#D9B461` | `#DEC577` |
  | Ishmael  | `#A5A5A0` | `#BFBBB6` |
  | Stubb    | `#E29B6E` | `#FFD9BB` |
  | Tashtego | `#8AB08C` | `#82C4A2` |
  | Daggoo   | `#AF8870` | `#A17069` |

- All theme files (VS Code light + dark, Zed, iTerm2, Alacritty,
  Ghostty, kitty, WezTerm, tmux, Windows Terminal), the Tailwind
  plugin, the Typst specimen, the project page, and all auto-
  generated R/Python data have been re-emitted from the new tokens.
  No hand-edited file should still reference a v0.1 hex.

### Improved

- **Light-mode contrast.** v0.1 had Pip (3.3 : 1), Stubb (3.8), and
  Starbuck (4.1) all *failing* AA-large on Log 100. In v0.2, every
  light-mode accent clears AA-large (3 : 1) and four of eight clear
  AA-body (4.5 : 1): Daggoo 9.5 : 1, Queequeg 7.8, Pip 6.3, Ahab 5.0.
- **CVD safety**, measured by `make cvd`:

  | Simulation | v0.1 worst pair | v0.2 worst pair |
  |---|---|---|
  | protanopia (light)   | Ahab ↔ Daggoo, ΔE 4.6     | Ishmael ↔ Tashtego, ΔE 15.1 |
  | protanopia (dark)    | Ahab ↔ Daggoo, ΔE 2.8     | Stubb ↔ Tashtego, ΔE 11.8   |
  | deuteranopia (light) | (close pairs documented)  | Ishmael ↔ Tashtego, ΔE 8.0  |
  | deuteranopia (dark)  | (close pairs documented)  | Ishmael ↔ Tashtego, ΔE 6.8  |
  | tritanopia (light)   | Pip ↔ Stubb, ΔE 1.0       | Pip ↔ Daggoo, ΔE 13.3       |
  | tritanopia (dark)    | Pip ↔ Stubb, ΔE 2.3       | Ahab ↔ Pip, ΔE 10.2         |

  The single residual "close" pair under deuteranopia is **Ishmael ↔
  Tashtego** (green-collapses-to-grey is mathematically unavoidable for
  any palette that includes both a saturated green and a low-chroma
  grey at similar L\*); the comment / string distinction it codifies is
  rarely encoded by colour alone in practice, and the default theme
  italicises comments anyway.

### Added

- `scripts/design_palette.py` — the LCh palette designer used to lay
  out v0.2 stops. Reports per-stop L\*/C/h, ΔL\* between successive
  log stops, and pairwise ΔE under all three CVD simulations so the
  next palette revision can iterate with the same constraints.

### Notes for upgraders

This is a token-level breaking change. Anything that referenced a v0.1
hex code by literal value (custom themes, screenshots, design mocks,
brand-style guides) needs to be re-pulled from `pequod.json`.
Downstream consumers that import the canonical token file (R, Python,
Tailwind, the editor themes) pick up the new values automatically on
upgrade.

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

### Added (2026-04-26, batch 2)

- `themes/terminals/` — six dark terminal presets that share the same
  ANSI palette mapping (Log 950 background, Log 100 foreground, crew
  dark variants on ANSI 1–6, brighter shades on 9–14):
  Ghostty (`Pequod.ghostty`), Alacritty (`Pequod.alacritty.toml`),
  kitty (`Pequod.kitty.conf`), WezTerm (`Pequod.wezterm.lua`),
  tmux (`Pequod.tmux.conf`), and Windows Terminal
  (`Pequod.windowsterminal.json`). Per-terminal install paths in
  `themes/terminals/README.md`.
- `tailwind/` — Tailwind CSS plugin published as `pequod-tailwind`
  on npm. Exposes `log`, `crew`, and a merged `colors` ready to
  spread into `theme.extend.colors`. Each crew accent has `DEFAULT`,
  `light`, and `dark` so `bg-ahab` resolves to the saturated value
  while `bg-ahab-dark` is available for dark-theme contexts.
  TypeScript types via `index.d.ts`. Six Node-runner tests for
  shape, hex format, freezing, and anchor values. Tarball is
  4.5 KB packed; tested against Tailwind v3 config.
- Makefile: new `tw-test`, `tw-pack`, `tw-publish` targets.

### Added (2026-04-26)

- `python/` — an installable Python package. Pure-Python data and
  helpers (`LOG`, `CREW_LIGHT`, `CREW_DARK`, `CREW`, `palette()`)
  with no required dependencies, plus optional matplotlib glue
  (`to_cmap()`, `register_cmaps()`) under the `[plot]` extra.
  Six named palettes (`log`, `log-warm`, `log-cool`, `crew`,
  `crew-dark`, `syntax`), discrete and continuous interpolation,
  reverse flag. Built with hatchling; published as `pequod` on PyPI.
  Data regenerated from `pequod.json` by
  `python/data-raw/generate_data.py`. 22 pytest tests covering the
  pure-Python API and the matplotlib integration; tests skip
  cleanly when matplotlib isn't installed.

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
