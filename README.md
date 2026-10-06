This repository is archived. Pequod is now a family in Ensigns: https://github.com/tiagojct/ensigns/tree/main/families/pequod. Ensigns has ten families and builds every file from one token file per family. Version 0.3.0 is the last release of the packages pequod (CRAN and PyPI), pequod-tailwind (npm) and the Pequod Palette extension. New work is at https://ensigns.tiagojacinto.eu/pequod/.

# Pequod

A pigment-inspired colour palette for reading and code, rooted in *Moby-Dick*.
Warm paper on one end, deep ink on the other, with eight accent hues named
after the crew of the Pequod.

[![PyPI](https://img.shields.io/pypi/v/pequod?label=PyPI&color=2C3E50)](https://pypi.org/project/pequod/)
[![npm](https://img.shields.io/npm/v/pequod-tailwind?label=npm&color=2C3E50)](https://www.npmjs.com/package/pequod-tailwind)
[![VS Code](https://vsmarketplacebadges.dev/version-short/tiagojct.pequod-color-theme.svg)](https://marketplace.visualstudio.com/items?itemName=tiagojct.pequod-color-theme)
[![Open VSX](https://img.shields.io/open-vsx/v/tiagojct/pequod-color-theme?label=Open%20VSX&color=2C3E50)](https://open-vsx.org/extension/tiagojct/pequod-color-theme)
[![CRAN](https://www.r-pkg.org/badges/version/pequod)](https://CRAN.R-project.org/package=pequod)
[![Licence](https://img.shields.io/badge/licence-MIT%20%2B%20CC--BY--4.0-C4A57B)](#licence)

![Pequod swatches](./cover.jpg)

- **Base scale:** twelve steps from Log 50 (warm paper) to Log 950 (night sky).
- **Accents:** eight crew members — Ahab, Starbuck, Queequeg, Pip, Ishmael,
  Stubb, Tashtego, Daggoo — each with a light and a dark variant and a
  recommended syntax role.
- **Read-first:** designed for long-form reading and code at length, not
  for glance-ability. Saturation stays low, backgrounds stay warm, accents
  stay in the same pigment register.
- **Accessibility:** every body-text pair clears WCAG-AA (4.5:1) on the
  reference surface, and every crew accent clears 4.5:1 on its page in both
  modes. Colour-vision-deficiency collapses are documented, not hidden — see
  below.
- **Semantics, not decoration:** each accent has a role. Using the palette
  should feel earned; the colour choice should tell you something.

The full narrative and design rationale live at
<https://ensigns.tiagojacinto.eu/pequod/>. From 0.3.0 the source of truth for
the tokens is the Ensigns repository, <https://github.com/tiagojct/ensigns>.

## Status

Version 0.3.0 is the last release of the Pequod packages. Pequod now lives
in [Ensigns](https://github.com/tiagojct/ensigns), a set of ten colour
families built from one token file each: <https://ensigns.tiagojacinto.eu>.
This repository publishes nothing more under the old package names, except
fixes. The surfaces below are at 0.3.0:

| Surface | Where | Status |
|---|---|---|
| VS Code extension | [Marketplace](https://marketplace.visualstudio.com/items?itemName=tiagojct.pequod-color-theme), [Open VSX](https://open-vsx.org/extension/tiagojct/pequod-color-theme) | live |
| Zed theme | `themes/Pequod.zed.json` | drop-in |
| Terminal presets | `themes/terminals/` | Ghostty, Alacritty, kitty, WezTerm, tmux, Windows Terminal, iTerm2 |
| Python package | [PyPI](https://pypi.org/project/pequod/) | `pip install pequod` |
| Tailwind plugin | [npm](https://www.npmjs.com/package/pequod-tailwind) | `npm install pequod-tailwind` |
| R package | [CRAN](https://CRAN.R-project.org/package=pequod) | `install.packages("pequod")` |
| Specimen PDF | `specimen/specimen.pdf` | regenerated from tokens |

0.3.0 changes six crew colours so that every crew colour reaches 4.5:1 as
text on its page. `CHANGELOG.md` lists each value.

## Showcase

Eight hero plots in matplotlib — sequential heatmaps, grouped and
horizontal bars, scatter, box plots, distributions, time series,
and a specimen-style swatch grid. Four on dark, four on light:

![Log heatmap on dark](examples/02_log_heatmap.png)
![Horizontal bars on light](examples/07_hbars_light.png)

Titles in Atkinson Hyperlegible Next SemiBold, ticks in JetBrains Mono, surfaces and series
colours pulled directly from `pequod.LOG`, `pequod.CREW_LIGHT`, and
`pequod.CREW_DARK`. Full gallery, code patterns, and reproduction
instructions live in [`examples/`](examples/). Generate them
yourself with:

```bash
pip install "pequod[plot]" numpy
python examples/plots.py
```

## Contents

```
pequod/
├── pequod.json                  # the canonical palette tokens
├── themes/
│   ├── Pequod.itermcolors                 # iTerm2 (dark)
│   ├── Pequod-color-theme.json            # VS Code (dark) — canonical
│   ├── Pequod-light-color-theme.json      # VS Code (light) — canonical
│   ├── Pequod.zed.json                    # Zed (dark + light in one file)
│   └── terminals/                         # Ghostty, Alacritty, kitty,
│                                          # WezTerm, tmux, Windows Terminal
├── tailwind/                    # npm package — `npm install pequod-tailwind`
├── vscode/                      # VS Code extension — `make vsix` builds
│   │                            # the .vsix; published to the Marketplace
│   │                            # as "tiagojct.pequod-color-theme"
│   ├── package.json
│   ├── icon.png
│   └── themes/                  # copies of the canonical themes
├── python/                      # Python package — install with
│   │                            #   pip install pequod
│   ├── pyproject.toml           # see python/README.md for full Python docs
│   ├── src/pequod/              # palette + matplotlib helpers
│   ├── tests/
│   └── data-raw/                # generator: re-reads ../pequod.json
├── r/                           # R package — install with
│   │                            #   remotes::install_github(
│   │                            #     "tiagojct/pequod", subdir = "r")
│   ├── DESCRIPTION              # see r/README.md for full R docs
│   ├── R/                       # palette constants, ggplot2 scales
│   ├── tests/
│   └── data-raw/                # generator: re-reads ../pequod.json
├── specimen/
│   ├── specimen.typ             # single-page specimen source (Typst)
│   └── specimen.pdf             # rendered output — swatches + samples
├── scripts/
│   └── cvd_check.py             # Viénot–Brettel–Mollon CVD simulation + ΔE
├── Makefile                     # ~13 targets — see `make help`
├── README.md
├── CHANGELOG.md
├── LICENSE-CC-BY-4.0            # palette tokens and docs
└── LICENSE-MIT                  # theme files, scripts, R package
```

## Install

### VS Code

The themes ship as a marketplace extension under [`vscode/`](vscode/),
published as `tiagojct.pequod-color-theme` on both surfaces. Install
in any of three ways:

1. **Marketplace** — open *Extensions* (⌘⇧X), search **Pequod
   Palette**, install. Or use [the listing page](https://marketplace.visualstudio.com/items?itemName=tiagojct.pequod-color-theme).
   For VSCodium / Cursor / Gitpod, use the [Open VSX listing](https://open-vsx.org/extension/tiagojct/pequod-color-theme) instead.
2. **`.vsix` file** — build with `make vsix`, then
   `code --install-extension vscode/pequod-color-theme-0.3.0.vsix`.
3. **From source (no marketplace)** — copy the [`vscode/`](vscode/)
   folder to `~/.vscode/extensions/pequod-color-theme/`. VS Code will
   pick it up on next launch.

Then *Preferences: Color Theme* → pick **Pequod** or **Pequod Light**.

### Zed

Zed reads user themes directly from disk:

1. Copy `themes/Pequod.zed.json` to `~/.config/zed/themes/Pequod.zed.json`
   (create the folder if it does not exist).
2. Restart Zed → *theme selector: toggle* → pick **Pequod Dark** or **Pequod Light**.

### iTerm2

1. Open *Settings → Profiles → Colors → Color Presets → Import…*
2. Select `themes/Pequod.itermcolors`.
3. Apply the *Pequod* preset.

An iTerm2 light preset is on the roadmap.

### Other terminals

Drop-in dark presets for the most common terminals live in
[`themes/terminals/`](themes/terminals/):

| Terminal | File |
|---|---|
| Ghostty | `Pequod.ghostty` |
| Alacritty | `Pequod.alacritty.toml` |
| kitty | `Pequod.kitty.conf` |
| WezTerm | `Pequod.wezterm.lua` |
| tmux | `Pequod.tmux.conf` |
| Windows Terminal | `Pequod.windowsterminal.json` |

See [`themes/terminals/README.md`](themes/terminals/README.md) for the
install path each terminal expects.

### Tailwind CSS

```bash
npm install pequod-tailwind
```

```js
// tailwind.config.js
const pequod = require("pequod-tailwind");

module.exports = {
  theme: {
    extend: {
      colors: pequod.colors,    // log + all eight crew accents
    },
  },
};
```

```html
<body class="bg-log-50 text-log-800 dark:bg-log-950 dark:text-log-100">
  <h1 class="text-queequeg dark:text-queequeg-dark">Pequod</h1>
</body>
```

Full usage in [`tailwind/README.md`](tailwind/README.md).

### Python

```bash
pip install pequod              # palette + helpers
pip install "pequod[plot]"      # adds matplotlib glue
```

```python
from pequod import LOG, CREW_LIGHT, palette

palette("log")                  # 12-step Log scale, list of hex
palette("crew", n=5)            # first five crew accents

# matplotlib (with the [plot] extra)
import matplotlib.pyplot as plt
import pequod
pequod.register_cmaps()
plt.imshow(data, cmap="pequod_log")
```

Full usage in [`python/README.md`](python/README.md).

### R

The R package is on [CRAN](https://CRAN.R-project.org/package=pequod):

```r
install.packages("pequod")

library(pequod)
palette_pequod("log")              # 12-step Log scale
palette_pequod("crew", n = 5)      # first five crew accents
pequod_preview("crew")             # quick base-R preview
```

Source lives in [`r/`](r/); to follow the development version,
`remotes::install_github("tiagojct/pequod", subdir = "r")`.

ggplot2 scales are provided too:

```r
library(ggplot2)
ggplot(iris, aes(Sepal.Length, Sepal.Width, colour = Species)) +
  geom_point(size = 3) +
  scale_color_pequod_d(palette = "crew")
```

Full usage in [`r/README.md`](r/README.md).

## The tokens

`pequod.json` is the single source of truth. The file contains:

- `log` — the twelve-step base scale (Log 50 → Log 950).
- `accents` — the eight crew accents, each with `light`, `dark`, `role`,
  and a short `note` explaining the character and the syntax role.
- `roles` — semantic role → token mappings for light and dark modes
  (`bg`, `text`, `text-muted`, `link`, `accent-primary`, etc.).
- `syntax` — default mappings from syntax role to accent (keyword,
  string, comment, function, type, constant, variable, operator).

The R package, the Python package, the Typst specimen, and the CVD
test script all regenerate from `pequod.json` (see each one's
`data-raw/` or generator). The terminal presets and the editor themes
are still produced by hand; bringing them under the same generator
contract is the next priority — see `What comes next` below.

## Accessibility

Body-text contrast on the reference surfaces:

| Pair | Use | Ratio |
|---|---|---|
| Log 800 on Log 100 | light body | 10.8 : 1 |
| Log 700 on Log 50 | light link | 10.1 : 1 |
| Log 400 on Log 50 | muted / large text | 3.9 : 1 |
| Log 100 on Log 950 | dark body | 14.0 : 1 |
| Accent-light on Log 100 | UI accents | 4.6 – 9.5 : 1 |
| Accent-dark on Log 950 | dark-mode accents | 4.7 – 13.7 : 1 |

In 0.3.0 every crew accent clears 4.5 : 1 (WCAG AA for body text) on its
target surface: the eight light variants on Log 100 and the eight dark
variants on Log 950. In 0.2.0 five did not: Starbuck, Stubb, Tashtego and
Ishmael (light) and Daggoo (dark). The editor themes draw the crew on the
editor background (Log 50 in the light theme, Log 950 in the dark theme). The
lowest crew ratios in the dark theme are 4.72 : 1 on that background, 4.47 : 1
on the current-line highlight and 3.64 : 1 on the selection, all Daggoo. In
the light theme they are 5.41, 4.51 and 3.99 : 1.

### Colour vision deficiency

`scripts/cvd_check.py` simulates each accent at 100 % severity for
protanopia, deuteranopia, and tritanopia using the Viénot–Brettel–Mollon
(1999) model, and reports pairwise ΔE*~ab~ (CIE76, Lab D65) between
simulated accents.

In 0.3.0 the worst-case pair under each simulation:

| | light variants | dark variants |
|---|---|---|
| protanopia    | Pip ↔ Stubb, ΔE 4.0         | Ahab ↔ Daggoo, ΔE 10.5    |
| deuteranopia  | Ishmael ↔ Tashtego, ΔE 12.2 | Ishmael ↔ Tashtego, ΔE 6.8 |
| tritanopia    | Ahab ↔ Pip, ΔE 8.4          | Ahab ↔ Pip, ΔE 10.2       |

The 0.3.0 corrections darkened five light accents to reach 4.5 : 1 on paper.
That brought some pairs closer in lightness. Four pairs now fall below ΔE 10
under one simulation: Pip and Stubb (light, protanopia, 4.0), Ahab and Daggoo
(light, protanopia, 6.7), Ahab and Pip (light, tritanopia, 8.4) and Ishmael
and Tashtego (dark, deuteranopia, 6.8). In 0.2.0 two pairs fell below 10:
Ishmael and Tashtego under deuteranopia (8.0 light, 6.8 dark).

The deuteranopia floor is set by **Ishmael ↔ Tashtego** because green
collapses to neutral grey under deutan and the two accents sit at similar
L\*. This is unavoidable for an 8-hue palette that includes both a green
and a low-chroma grey, so it is documented rather than designed away —
in practice, comments (Ishmael) and strings (Tashtego) are rarely
adjacent and rarely encode meaning by colour alone.

**Usage guidance:** do not rely on colour alone to tell apart the four pairs
above under the simulation named. Pair colour with icon, weight, italics or
position (the default theme already italicises comments). Every other pair
clears ΔE ≥ 10 across all three simulations. Ensigns uses a different
simulation (Machado, Oliveira and Fernandes, 2009) and measures distance in
OKLab, so its figures differ from these.

Run the check yourself:

```bash
python3 scripts/cvd_check.py
```

The script has no dependencies beyond NumPy.

## Specimen

A one-page A4 specimen — the full Log scale, the eight crew accents
with light and dark variants, a body-text sample, and a dark code
sample with every token coloured by its crew role — lives at
[`specimen/specimen.pdf`](specimen/specimen.pdf). Use it as a quick
reference when choosing which accent a new UI element should take,
or print it and pin it somewhere.

The PDF is generated from [`specimen/specimen.typ`](specimen/specimen.typ)
with [Typst](https://typst.app/). To regenerate after a token change:

```bash
make specimen
# equivalent to: typst compile specimen/specimen.typ specimen/specimen.pdf
```

Typst uses the system-installed Atkinson Hyperlegible Next and
JetBrains Mono. Install them from
[Google Fonts](https://fonts.google.com/specimen/Atkinson+Hyperlegible+Next)
if they are not already present.

## What comes next

Nothing in this repository. Ensigns has generators for the editor and
terminal themes, light terminal presets, a Neovim colourscheme and a Tailwind
CSS 4 stylesheet for Pequod: <https://github.com/tiagojct/ensigns>. Sublime
Text, Helix and Emacs themes were not started.

## Inspirations and credits

- [Flexoki](https://stephango.com/flexoki) by Steph Ango is the most
  direct inspiration. Pequod owes its philosophy — warm paper, cool
  ink, muted accents, published tokens — to Flexoki. Where Flexoki
  draws on earth pigments broadly, Pequod narrows the story to a
  ship, a century, and a text.
- [Solarized](https://ethanschoonover.com/solarized/) by Ethan
  Schoonover established the modern practice of designing palettes
  for reading first.
- [Tokyo Night](https://github.com/enkia/tokyo-night-vscode-theme)
  and [Nord](https://www.nordtheme.com/) are two other palettes with
  a disciplined colour story worth studying.
- Herman Melville, *Moby-Dick; or, The Whale* (1851), for the names.

## Licence

- **Palette tokens (`pequod.json`) and documentation** — [Creative Commons
  Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).
  Use, adapt, ship; credit required. See `LICENSE-CC-BY-4.0`.
- **Theme files, scripts, and packages** (`themes/*`, `scripts/*`,
  `tailwind/*`, `vscode/*`, `python/*`, `r/*`, `specimen/*`) —
  [MIT](https://opensource.org/licenses/MIT). See `LICENSE-MIT`.

## Contact

If you use Pequod in a project or have a suggestion, I would love to
hear about it: [tiagojacinto@med.up.pt](mailto:tiagojacinto@med.up.pt),
or open an issue here.
