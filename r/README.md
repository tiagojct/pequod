# pequod · R package

The Pequod palette packaged for R. Provides the full Log base scale,
the eight crew accents (light and dark variants), and ggplot2 scales
for both discrete and continuous mapping.

The narrative, design rationale, and full accessibility analysis live
in the [repository README](https://github.com/tiagojct/pequod/blob/main/README.md)
and on the [project website](https://tiagojct.eu/projects/pequod/).

## Install

From GitHub (the R package lives in the `r/` subdirectory):

```r
# install.packages("remotes")
remotes::install_github("tiagojct/pequod", subdir = "r")
```

Or `devtools::install_github("tiagojct/pequod", subdir = "r")`.

## Quick start

```r
library(pequod)

# The raw palettes as named character vectors
pequod_log           # 12-step Log base scale
pequod_crew_light    # 8 accents, light variants
pequod_crew_dark     # 8 accents, dark variants

# A general-purpose palette helper
palette_pequod("log")                         # full Log scale, 12 colours
palette_pequod("crew", n = 5)                 # first five crew accents
palette_pequod("log-cool", 100, "continuous") # 100-colour interpolation

# Base-R preview
pequod_preview("log")
pequod_preview("crew")
```

## ggplot2

```r
library(ggplot2)

ggplot(iris, aes(Sepal.Length, Sepal.Width, colour = Species)) +
  geom_point(size = 3) +
  scale_color_pequod_d(palette = "crew") +
  theme_minimal()

ggplot(faithfuld, aes(waiting, eruptions, fill = density)) +
  geom_tile() +
  scale_fill_pequod_c(palette = "log-cool")
```

Both `scale_color_*` and `scale_colour_*` spellings are exported.

## Palettes

| Name        | Length | Type        | Suggested use                              |
|-------------|:-----:|-------------|--------------------------------------------|
| `log`       | 12    | sequential  | continuous gradients, heatmaps             |
| `log-warm`  | 6     | sequential  | warm side only (Log 50–400)                |
| `log-cool`  | 6     | sequential  | cool side only (Log 500–950)               |
| `crew`      | 8     | qualitative | categories, groups (light variants)        |
| `crew-dark` | 8     | qualitative | categories on a dark theme                 |
| `syntax`    | 8     | qualitative | crew in syntax-role order                  |

## Keeping tokens in sync

The canonical palette lives at `../pequod.json`. The data shipped with
this package is generated from it:

```bash
cd r
Rscript data-raw/generate_palettes.R
```

That rewrites `R/palettes-data.R` so the R values always match the
JSON tokens.

## Licence

MIT. The underlying palette tokens are also available under CC-BY-4.0
via `../pequod.json`; see `../LICENSE-CC-BY-4.0`.
