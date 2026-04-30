# Generated from ../pequod.json (v0.2.0-alpha).
# Re-generate with: Rscript data-raw/generate_palettes.R

#' Pequod Log base scale
#'
#' The twelve-step base scale, from warm paper (`Log 50`) to the
#' night-before-the-storm ink of `Log 950`. Warm on the paper side,
#' cool on the ink side; the hinge sits between Log 500 (warm
#' taupe) and Log 700 (cool sage).
#'
#' @format A named character vector of length 12 (hex codes).
#' @export
pequod_log <- c(
  "Log 50"  = "#F7F3EE",
  "Log 100" = "#EAE1D7",
  "Log 150" = "#DBC9B6",
  "Log 200" = "#CFAD8E",
  "Log 300" = "#BD8C68",
  "Log 400" = "#A16E50",
  "Log 500" = "#835A49",
  "Log 600" = "#335260",
  "Log 700" = "#163F54",
  "Log 800" = "#0D2F42",
  "Log 900" = "#0C222F",
  "Log 950" = "#0B1720"
)

#' Pequod crew accents — light variants
#'
#' Eight accent hues, each named after a character in *Moby-Dick*,
#' tuned to sit against a Log 100 paper surface.
#'
#' @format A named character vector of length 8.
#' @export
pequod_crew_light <- c(
  "Ahab"     = "#A83732",
  "Starbuck" = "#0082B1",
  "Queequeg" = "#253E82",
  "Pip"      = "#6A4A00",
  "Ishmael"  = "#76716B",
  "Stubb"    = "#CA6435",
  "Tashtego" = "#177C55",
  "Daggoo"   = "#552823"
)

#' Pequod crew accents — dark variants
#'
#' Eight accent hues tuned to sit against the Log 950 ink surface.
#'
#' @format A named character vector of length 8.
#' @export
pequod_crew_dark <- c(
  "Ahab"     = "#E3877C",
  "Starbuck" = "#A6DFFF",
  "Queequeg" = "#838CCF",
  "Pip"      = "#DEC577",
  "Ishmael"  = "#BFBBB6",
  "Stubb"    = "#FFD9BB",
  "Tashtego" = "#82C4A2",
  "Daggoo"   = "#A17069"
)

#' Pequod crew metadata
#'
#' A list bundling the light and dark crew accents together with
#' their suggested syntax roles.
#'
#' @format A list with three elements: `light`, `dark`, `roles`.
#' @export
pequod_crew <- list(
  light = pequod_crew_light,
  dark  = pequod_crew_dark,
  roles = c(
    "Ahab"     = "red",
    "Starbuck" = "blue",
    "Queequeg" = "indigo",
    "Pip"      = "yellow",
    "Ishmael"  = "grey",
    "Stubb"    = "orange",
    "Tashtego" = "green",
    "Daggoo"   = "brown"
  )
)

