# Pequod

A pigment-inspired colour palette for reading and code, rooted in
Herman Melville's *Moby-Dick*. Warm paper on one end, deep ink on
the other, and eight accent hues named after the crew of the whaler.
Designed for long reading and long-form code, not glance-ability.

![Pequod swatches](https://raw.githubusercontent.com/tiagojct/pequod/main/cover.jpg)

## Themes included

- **Pequod** — dark (deep-ink Log 950 surface, cream Log 100 text)
- **Pequod Light** — light (warm-paper Log 50 surface, deep-navy Log 800 text)

Activate with **Preferences: Color Theme** and pick *Pequod* or
*Pequod Light*.

## The crew

Each accent is a character with a syntax role:

| Crew | Role | Light | Dark |
|---|---|---|---|
| **Ahab** — the wound, the fire | keywords, errors | `#B5534A` | `#E07A72` |
| **Starbuck** — moderate reason | functions, links | `#527C98` | `#7FA8C3` |
| **Queequeg** — tattoos, loyalty | types, classes | `#4A4E8C` | `#8A8ECE` |
| **Pip** — sun-addled | numbers, literals | `#A8812B` | `#D9B461` |
| **Ishmael** — the narrator | comments, punctuation | `#6E6E6B` | `#A5A5A0` |
| **Stubb** — pipe smoke | constants, warnings | `#B5683A` | `#E29B6E` |
| **Tashtego** — moss, low pine | strings, success | `#507352` | `#8AB08C` |
| **Daggoo** — mahogany | variables, properties | `#7A5440` | `#AF8870` |

## Accessibility

- Body-text contrast on the light theme: **10.5 : 1** (Log 800 on
  Log 50). On dark: **16.2 : 1** (Log 100 on Log 950).
- All eight dark-mode accents clear WCAG-AA (4.5 : 1) on Log 950.
- Five of eight light-mode accents clear AA-body on Log 100; the
  other three (Pip, Stubb, Starbuck) are tuned for bold, large
  text, or UI elements where AA-large (3 : 1) applies.
- Worst-case colour-vision-deficiency collapses are documented in
  the [main repository](https://github.com/tiagojct/pequod):
  Pip↔Stubb collapse under tritanopia, Ahab↔Daggoo under
  protanopia. Pair these with shape, weight, or position where
  colour-blind-safe distinction matters.

## Beyond VS Code

Pequod also ships as:

- **Zed** theme family (dark + light) — single JSON file,
  drop into `~/.config/zed/themes/`.
- **iTerm2** preset (dark).
- **R package** (`pequod`) with palette helpers and ggplot2
  scales — install via `install.packages("pequod")` or from
  GitHub.
- **Printable A4 specimen** PDF, generated from the canonical
  tokens with [Typst](https://typst.app/).
- **`pequod.json`** — the canonical machine-readable token file
  (CC-BY-4.0). Use it to generate themes for any other tool.

All of these live at [github.com/tiagojct/pequod](https://github.com/tiagojct/pequod).
The narrative, the design rationale, and the full accessibility
analysis are at [tiagojct.eu/projects/pequod](https://tiagojct.eu/projects/pequod/).

## Licence

MIT. The underlying palette tokens are also published under
CC-BY-4.0; see the upstream repository.
