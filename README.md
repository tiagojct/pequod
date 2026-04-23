# Pequod

A pigment-inspired colour palette for reading and code, rooted in *Moby-Dick*.
Warm paper on one end, deep ink on the other, with eight accent hues named
after the crew of the Pequod.

![Pequod swatches](./cover.jpg)

- **Base scale:** twelve steps from Log 50 (warm paper) to Log 950 (night sky).
- **Accents:** eight crew members — Ahab, Starbuck, Queequeg, Pip, Ishmael,
  Stubb, Tashtego, Daggoo — each with a light and a dark variant and a
  recommended syntax role.
- **Read-first:** designed for long-form reading and code at length, not
  for glance-ability. Saturation stays low, backgrounds stay warm, accents
  stay in the same pigment register.
- **Accessibility:** every body-text pair clears WCAG-AA (4.5:1) on the
  reference surface; dark-mode accents clear 4.5:1 comfortably. Colour-
  vision-deficiency collapses are documented, not hidden — see below.
- **Semantics, not decoration:** each accent has a role. Using the palette
  should feel earned; the colour choice should tell you something.

The full narrative and design rationale live at
<https://tiagojct.eu/projects/pequod/>. This repository is the canonical
source of truth for the tokens and the built themes.

## Status

**Alpha (0.1.0).** Tokens are stable enough to run a website on them, but
hex values may still shift by a point or two as the palette is tested
against more code and long-form prose. Breaking changes before 1.0 will
be called out in `CHANGELOG.md`.

## Contents

```
pequod/
├── pequod.json                  # the canonical palette tokens
├── themes/
│   ├── Pequod.itermcolors                 # iTerm2 (dark)
│   ├── Pequod-color-theme.json            # VS Code (dark)
│   ├── Pequod-light-color-theme.json      # VS Code (light)
│   └── Pequod.zed.json                    # Zed (dark + light in one file)
├── specimen/
│   ├── specimen.typ             # single-page specimen source (Typst)
│   └── specimen.pdf             # rendered output — swatches + samples
├── scripts/
│   └── cvd_check.py             # Viénot–Brettel–Mollon CVD simulation + ΔE
├── Makefile                     # `make specimen`, `make cvd`, `make clean`
├── README.md
├── CHANGELOG.md
├── LICENSE-CC-BY-4.0            # palette tokens and docs
└── LICENSE-MIT                  # theme files and scripts
```

## Install

### VS Code

VS Code does not load bare colour-theme files; it expects an extension.
The quickest path:

1. Clone or download this repo.
2. Create a folder `~/.vscode/extensions/pequod-theme/` and copy the `themes/`
   folder into it.
3. Drop this `package.json` next to `themes/`:

   ```json
   {
     "name": "pequod-theme",
     "displayName": "Pequod",
     "version": "0.1.0",
     "publisher": "local",
     "engines": { "vscode": "^1.70.0" },
     "contributes": {
       "themes": [
         { "label": "Pequod",       "uiTheme": "vs-dark", "path": "./themes/Pequod-color-theme.json" },
         { "label": "Pequod Light", "uiTheme": "vs",      "path": "./themes/Pequod-light-color-theme.json" }
       ]
     }
   }
   ```
4. Restart VS Code → *Preferences: Color Theme* → pick **Pequod** or **Pequod Light**.

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

## The tokens

`pequod.json` is the single source of truth. The file contains:

- `log` — the twelve-step base scale (Log 50 → Log 950).
- `accents` — the eight crew accents, each with `light`, `dark`, `role`,
  and a short `note` explaining the character and the syntax role.
- `roles` — semantic role → token mappings for light and dark modes
  (`bg`, `text`, `text-muted`, `link`, `accent-primary`, etc.).
- `syntax` — default mappings from syntax role to accent (keyword,
  string, comment, function, type, constant, variable, operator).

All theme files in this repo are produced by hand for now. A future
version will generate them from `pequod.json` so the JSON stays
authoritative. See `What comes next` below.

## Accessibility

Body-text contrast on the reference surfaces:

| Pair | Use | Ratio |
|---|---|---|
| Log 800 on Log 50 | light body | 10.5 : 1 |
| Log 700 on Log 50 | light link | 5.0 : 1 |
| Log 400 on Log 50 | muted / large text | 3.2 : 1 |
| Log 100 on Log 950 | dark body | 16.2 : 1 |
| Accent-light on Log 100 | UI accents | 3.3 – 6.9 : 1 |
| Accent-dark on Log 950 | dark-mode accents | 5.6 – 9.0 : 1 |

Five of eight light-mode accents clear 4.5:1 on Log 100 for body text
(Queequeg, Daggoo, Tashtego, Ishmael, Ahab). Pip, Stubb, and Starbuck
fall short; use them for bold, large text (≥ 18.7 px), or UI-only uses
where AA-large (3:1) is the relevant target.

### Colour vision deficiency

`scripts/cvd_check.py` simulates each accent at 100 % severity for
protanopia, deuteranopia, and tritanopia using the Viénot–Brettel–Mollon
(1999) model, and reports pairwise ΔE*~ab~ (CIE76, Lab D65) between
simulated accents. Worst-case collapses (ΔE < 10) documented:

- **Pip ↔ Stubb** — collapse under tritanopia (ΔE 1.0 light / 2.3 dark).
- **Ahab ↔ Daggoo** — collapse under protanopia (ΔE 4.6 / 2.8).
- **Ahab ↔ Stubb, Ahab ↔ Pip** — collapse under tritanopia.
- **Queequeg ↔ Tashtego** — close under tritanopia-dark (ΔE 7.2).

Queequeg and Starbuck stay separable across all three simulations
(minimum ΔE 15.8 in deuteranopia-dark).

**Usage guidance:** do not rely on colour alone to distinguish *Ahab/Daggoo*,
*Pip/Stubb*, *Ahab/Pip*, *Ahab/Stubb*, or *Queequeg/Tashtego*. Pair with
icon, shape, weight, or position where colour-blind-safe distinction
matters (error states, diff gutters, warning badges).

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

Typst uses the system-installed Geist and Geist Mono. Install them
from [Google Fonts](https://fonts.google.com/specimen/Geist) if they
are not already present.

## What comes next

- **Generators** that take `pequod.json` and emit each theme target,
  so the JSON stays authoritative and themes cannot drift from tokens.
- **iTerm2 light preset** to round out the terminal theme.
- **Terminal themes:** Ghostty, Kitty, Alacritty. Trivial once the
  tokens are fixed.
- **Vim / Neovim colourscheme** using Lush.
- **Helix, Sublime** — lower priority.

Contributions to any of these are welcome.

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
- **Theme files (`themes/*`) and scripts (`scripts/*`)** —
  [MIT](https://opensource.org/licenses/MIT). See `LICENSE-MIT`.

## Contact

If you use Pequod in a project or have a suggestion, I would love to
hear about it: [tiagojacinto@med.up.pt](mailto:tiagojacinto@med.up.pt),
or open an issue here.
