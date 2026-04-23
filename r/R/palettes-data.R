# Generated from ../pequod.json (v0.1.0-alpha).
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
  "Log 50"  = "#FBFAF5",
  "Log 100" = "#F8F4EB",
  "Log 150" = "#ECE5D3",
  "Log 200" = "#DFD3B8",
  "Log 300" = "#C4A57B",
  "Log 400" = "#A8865E",
  "Log 500" = "#8B7B6B",
  "Log 600" = "#6E5F52",
  "Log 700" = "#527275",
  "Log 800" = "#2C3E50",
  "Log 900" = "#1C2936",
  "Log 950" = "#13181F"
)

#' Pequod crew accents — light variants
#'
#' Eight accent hues, each named after a character in *Moby-Dick*,
#' tuned to sit against a Log 100 paper surface. These are the
#' saturated, darker values you should use on light-mode UIs.
#'
#' @format A named character vector of length 8.
#' @export
pequod_crew_light <- c(
  Ahab     = "#B5534A",
  Starbuck = "#527C98",
  Queequeg = "#4A4E8C",
  Pip      = "#A8812B",
  Ishmael  = "#6E6E6B",
  Stubb    = "#B5683A",
  Tashtego = "#507352",
  Daggoo   = "#7A5440"
)

#' Pequod crew accents — dark variants
#'
#' Eight accent hues tuned to sit against the Log 950 ink surface.
#' These are the brighter, de-saturated values for dark-mode UIs.
#'
#' @format A named character vector of length 8.
#' @export
pequod_crew_dark <- c(
  Ahab     = "#E07A72",
  Starbuck = "#7FA8C3",
  Queequeg = "#8A8ECE",
  Pip      = "#D9B461",
  Ishmael  = "#A5A5A0",
  Stubb    = "#E29B6E",
  Tashtego = "#8AB08C",
  Daggoo   = "#AF8870"
)

#' Pequod crew metadata
#'
#' A list bundling the light and dark crew accents together with
#' their suggested syntax roles.
#'
#' @format A list with three elements:
#' \describe{
#'   \item{light}{Named character vector of 8 hex codes (light variants).}
#'   \item{dark}{Named character vector of 8 hex codes (dark variants).}
#'   \item{roles}{Named character vector of 8 role labels (red, blue, etc.).}
#' }
#' @export
pequod_crew <- list(
  light = pequod_crew_light,
  dark  = pequod_crew_dark,
  roles = c(
    Ahab     = "red",
    Starbuck = "blue",
    Queequeg = "indigo",
    Pip      = "yellow",
    Ishmael  = "grey",
    Stubb    = "orange",
    Tashtego = "green",
    Daggoo   = "brown"
  )
)
