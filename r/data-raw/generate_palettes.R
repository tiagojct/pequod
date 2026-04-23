# Regenerate R/palettes-data.R from ../../pequod.json.
#
# Run from the R package root:
#   Rscript data-raw/generate_palettes.R
#
# This keeps the R palette in sync with the canonical tokens and is
# the only place the colour values should be edited.

if (!requireNamespace("jsonlite", quietly = TRUE)) {
  stop("jsonlite is required to run the generator. ",
       "Install it with install.packages('jsonlite').")
}

repo_root    <- normalizePath("..", mustWork = TRUE)
palette_path <- file.path(repo_root, "pequod.json")
out_path     <- file.path("R", "palettes-data.R")

if (!file.exists(palette_path)) {
  stop("pequod.json not found at ", palette_path,
       " — is the R package still nested inside the pequod repo?")
}

tokens  <- jsonlite::read_json(palette_path)
version <- tokens$version

log_scale <- vapply(tokens$log, identity, character(1))
names(log_scale) <- paste0("Log ", names(log_scale))

capitalise <- function(s) {
  paste0(toupper(substring(s, 1, 1)), substring(s, 2))
}

accent_names  <- names(tokens$accents)
crew_light    <- setNames(
  vapply(tokens$accents, `[[`, character(1), "light"),
  capitalise(accent_names)
)
crew_dark     <- setNames(
  vapply(tokens$accents, `[[`, character(1), "dark"),
  capitalise(accent_names)
)
crew_roles    <- setNames(
  vapply(tokens$accents, `[[`, character(1), "role"),
  capitalise(accent_names)
)

fmt_vec <- function(vec, indent = "  ") {
  name_width <- max(nchar(names(vec))) + 2L   # room for surrounding quotes
  lines <- sprintf(
    '%s%-*s = "%s"',
    indent,
    name_width,
    paste0('"', names(vec), '"'),
    unname(vec)
  )
  paste(lines, collapse = ",\n")
}

body <- sprintf(
'# Generated from ../pequod.json (v%s).
# Re-generate with: Rscript data-raw/generate_palettes.R

#\' Pequod Log base scale
#\'
#\' The twelve-step base scale, from warm paper (`Log 50`) to the
#\' night-before-the-storm ink of `Log 950`. Warm on the paper side,
#\' cool on the ink side; the hinge sits between Log 500 (warm
#\' taupe) and Log 700 (cool sage).
#\'
#\' @format A named character vector of length 12 (hex codes).
#\' @export
pequod_log <- c(
%s
)

#\' Pequod crew accents — light variants
#\'
#\' Eight accent hues, each named after a character in *Moby-Dick*,
#\' tuned to sit against a Log 100 paper surface.
#\'
#\' @format A named character vector of length 8.
#\' @export
pequod_crew_light <- c(
%s
)

#\' Pequod crew accents — dark variants
#\'
#\' Eight accent hues tuned to sit against the Log 950 ink surface.
#\'
#\' @format A named character vector of length 8.
#\' @export
pequod_crew_dark <- c(
%s
)

#\' Pequod crew metadata
#\'
#\' A list bundling the light and dark crew accents together with
#\' their suggested syntax roles.
#\'
#\' @format A list with three elements: `light`, `dark`, `roles`.
#\' @export
pequod_crew <- list(
  light = pequod_crew_light,
  dark  = pequod_crew_dark,
  roles = c(
%s
  )
)
',
  version,
  fmt_vec(log_scale),
  fmt_vec(crew_light),
  fmt_vec(crew_dark),
  fmt_vec(crew_roles, indent = "    ")
)

writeLines(body, out_path)
message(sprintf(
  "Wrote %s from pequod.json v%s (%d log steps, %d crew accents).",
  out_path, version, length(log_scale), length(accent_names)
))
