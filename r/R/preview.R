#' Preview a Pequod palette
#'
#' Draws a strip of coloured rectangles with labels using base R
#' graphics. Useful for seeing a palette before committing to it in
#' an analysis.
#'
#' @param palette Palette name. See [palette_pequod()].
#' @param labels If `TRUE` (default) writes each colour's label above
#'   the rectangle.
#'
#' @return The palette, invisibly.
#' @export
#'
#' @examples
#' pequod_preview("log")
#' pequod_preview("crew")
pequod_preview <- function(palette = "log", labels = TRUE) {
  cols <- palette_pequod(palette, type = "discrete")
  # Names are dropped inside palette_pequod() — reach back to the map
  # for labels so the preview stays meaningful.
  map <- .pequod_palette_map()
  nm <- names(map[[palette]])
  if (is.null(nm)) nm <- seq_along(cols)

  n <- length(cols)
  op <- graphics::par(mar = c(2, 1, 3, 1))
  on.exit(graphics::par(op), add = TRUE)

  graphics::plot.new()
  graphics::plot.window(xlim = c(0, n), ylim = c(0, 1), asp = NA)

  for (i in seq_len(n)) {
    graphics::rect(i - 1, 0, i, 1, col = cols[i], border = NA)
    if (labels) {
      graphics::text(i - 0.5, 1.05, labels = nm[i],
                     cex = 0.75, xpd = NA, srt = 0)
    }
  }

  graphics::title(main = paste0("Pequod: ", palette), cex.main = 0.95)

  invisible(stats::setNames(cols, nm))
}
