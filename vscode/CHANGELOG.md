# Changelog

## [0.3.0] — 2026-10-07

The last release of this extension. Pequod is now part of
[Ensigns](https://ensigns.tiagojacinto.eu), a set of ten colour families. The
source is at <https://github.com/tiagojct/ensigns>.

### Changed

- Six crew colours corrected so that every crew colour reaches 4.5 : 1 as
  text on its page. The light theme changes where it draws Ahab, Starbuck,
  Ishmael, Stubb and Tashtego, which includes keywords, functions, comments,
  constants, strings, errors and the terminal red, green and blue. The dark
  theme changes where it draws Daggoo, which is parameters and properties, and
  the status bar while debugging, which is the light Ahab colour. The full
  account, with contrast figures, is in the
  [palette changelog](https://github.com/tiagojct/pequod/blob/main/CHANGELOG.md#030--2026-10-07).

| Crew | Mode | 0.2.0 | 0.3.0 |
|---|---|---|---|
| Ahab | light | `#A83732` | `#931432` |
| Starbuck | light | `#0082B1` | `#006A98` |
| Ishmael | light | `#76716B` | `#6A6164` |
| Stubb | light | `#CA6435` | `#AA430B` |
| Tashtego | light | `#177C55` | `#06724B` |
| Daggoo | dark | `#A17069` | `#A7766F` |

- The homepage link points to <https://ensigns.tiagojacinto.eu/pequod/>. The
  old link returned 404.
- The README contrast figures are corrected: body text is 12.7 : 1 on the
  light theme and 14.0 : 1 on the dark theme. The 0.2.0 README quoted 10.5 : 1
  and 16.2 : 1, which were 0.1.0 figures.

### Notes for upgraders

VS Code installs the update on its own. If you copied a 0.2.0 crew hex value
into `workbench.colorCustomizations`, use the values in the table above.

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
