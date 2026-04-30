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
| **Ahab** — the wound, the fire | keywords, errors | `#A83732` | `#E3877C` |
| **Starbuck** — moderate reason | functions, links | `#0082B1` | `#A6DFFF` |
| **Queequeg** — tattoos, loyalty | types, classes | `#253E82` | `#838CCF` |
| **Pip** — sun-addled | numbers, literals | `#6A4A00` | `#DEC577` |
| **Ishmael** — the narrator | comments, punctuation | `#76716B` | `#BFBBB6` |
| **Stubb** — pipe smoke | constants, warnings | `#CA6435` | `#FFD9BB` |
| **Tashtego** — moss, low pine | strings, success | `#177c55` | `#82C4A2` |
| **Daggoo** — mahogany | variables, properties | `#552823` | `#a17069` |

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
