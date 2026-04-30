# Changelog

## [0.2.0] — 2026-04-30

A perceptual-correctness rewrite of every token in the theme. The
underlying [Pequod palette v0.2.0](https://github.com/tiagojct/pequod/blob/main/CHANGELOG.md)
fixes the Log scale's luminance reversal at step 8→9 and re-tunes
all eight crew accents in CIE-LCh so confusable hue pairs separate
by lightness even under colour-blindness simulation.

### Changed (breaking — every colour shifted)

- **Log scale** repigmented across all 12 stops; ΔL\* between
  successive stops is now even (5–11) and strictly monotonic, so
  contour fills and gradients no longer "stripe" at the warm-cool
  hinge. The cream paper end is `#F7F3EE` / `#EAE1D7`; the deep ink
  end is `#0C222F` / `#0B1720`.
- **Crew accents (light + dark variants)** retuned for
  CVD safety. Worst-pair ΔE under simulation went from
  1.0 (Pip ↔ Stubb under tritanopia) and 2.8 (Ahab ↔ Daggoo under
  protanopia) in v0.1.0 to a worst case of ≥ 6.8 across all three
  simulations in v0.2.0 — the only "close" pair that remains is
  Ishmael ↔ Tashtego under deuteranopia (green collapses to grey,
  mathematically unavoidable for any palette including both). The
  default theme already italicises comments to break that tie.
- **Light-mode contrast** improved: in v0.1.0, Pip / Stubb / Starbuck
  fell below WCAG-AA-large on Log 100; in v0.2.0 every accent clears
  AA-large (3 : 1) and four clear AA-body (4.5 : 1) on Log 100.

### Notes for upgraders

VS Code auto-updates installed extensions, so the theme will switch
to v0.2.0 colours on the next reload after install. If you have
custom `workbench.colorCustomizations` referencing v0.1.0 hex values
by literal, those will need to be re-pulled from the new tokens; the
[full hex map is in the upstream changelog](https://github.com/tiagojct/pequod/blob/main/CHANGELOG.md#020-alpha--2026-04-30).

## [0.1.0] — 2026-04-25

First public release on the Visual Studio Marketplace.

### Added

- **Pequod** (dark) — Log 950 ink surface, Log 100 cream text,
  crew-coloured syntax (Ahab keywords, Starbuck functions,
  Queequeg types, Pip numbers, Tashtego strings, Stubb constants,
  Ishmael comments, Daggoo variables/properties).
- **Pequod Light** — Log 50 paper surface, Log 800 deep-navy text,
  the same crew assignments at their light-variant hex values.

### Notes

- Tokens come from the canonical
  [`pequod.json`](https://github.com/tiagojct/pequod/blob/main/pequod.json)
  in the upstream repository.
- WCAG-AA contrast ratios documented in the README; CVD-safety
  guidance in the [main repository](https://github.com/tiagojct/pequod).
- Hex values may shift by a point or two before 1.0 — track
  [`CHANGELOG.md`](https://github.com/tiagojct/pequod/blob/main/CHANGELOG.md)
  in the main repository for breaking changes.
