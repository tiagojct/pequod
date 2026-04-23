#' Pequod palette
#'
#' Returns a character vector of hex colours from a named Pequod
#' palette. Supports both discrete selection (first `n` colours) and
#' continuous interpolation between the palette's stops.
#'
#' Available palettes:
#' \describe{
#'   \item{`"log"`}{The full 12-step Log base scale.}
#'   \item{`"log-warm"`}{Log 50–400 (six warm steps).}
#'   \item{`"log-cool"`}{Log 500–950 (six cool steps).}
#'   \item{`"crew"`}{The eight crew accents, light variants.}
#'   \item{`"crew-dark"`}{The eight crew accents, dark variants.}
#'   \item{`"syntax"`}{Crew accents in syntax-role order — keyword,
#'     string, number, comment, function, type, constant, variable.}
#' }
#'
#' @param name Palette name; see Details.
#' @param n Number of colours to return. Defaults to the full palette
#'   length. For `type = "continuous"`, any positive integer.
#' @param type `"discrete"` takes the first `n` colours (errors if `n`
#'   exceeds the palette length). `"continuous"` interpolates `n`
#'   colours across the full palette with [grDevices::colorRampPalette()].
#' @param reverse If `TRUE`, reverse the returned palette.
#' @param direction `+1` (default) or `-1` to flip the palette.
#'
#' @return An unnamed character vector of hex codes of length `n`.
#' @export
#'
#' @examples
#' palette_pequod("log")
#' palette_pequod("crew", n = 5)
#' palette_pequod("log-cool", n = 100, type = "continuous")
palette_pequod <- function(name = "log",
                           n = NULL,
                           type = c("discrete", "continuous"),
                           reverse = FALSE,
                           direction = 1) {
  type <- match.arg(type)
  palettes <- .pequod_palette_map()

  if (!name %in% names(palettes)) {
    stop(
      "Unknown palette '", name, "'. Available palettes: ",
      paste(names(palettes), collapse = ", "),
      call. = FALSE
    )
  }

  cols <- palettes[[name]]
  if (is.null(n)) n <- length(cols)
  if (n < 1L) stop("`n` must be a positive integer.", call. = FALSE)

  if (type == "discrete") {
    if (n > length(cols)) {
      stop(
        "Requested ", n, " colours from palette '", name,
        "' which has only ", length(cols), ". ",
        "Use type = 'continuous' to interpolate.",
        call. = FALSE
      )
    }
    out <- cols[seq_len(n)]
  } else {
    out <- grDevices::colorRampPalette(cols)(n)
  }

  if (isTRUE(reverse) || direction == -1) out <- rev(out)
  unname(out)
}

# Internal: master palette lookup table.
.pequod_palette_map <- function() {
  list(
    "log"       = pequod_log,
    "log-warm"  = pequod_log[1:6],
    "log-cool"  = pequod_log[7:12],
    "crew"      = pequod_crew_light,
    "crew-dark" = pequod_crew_dark,
    "syntax"    = pequod_crew_light[c(
      "Ahab", "Tashtego", "Pip", "Ishmael",
      "Starbuck", "Queequeg", "Stubb", "Daggoo"
    )]
  )
}
