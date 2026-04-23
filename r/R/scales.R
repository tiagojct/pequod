#' Pequod discrete colour / fill scales for ggplot2
#'
#' Wraps [palette_pequod()] in a [ggplot2::discrete_scale()] so it can
#' be dropped into any ggplot that uses a discrete colour or fill
#' aesthetic.
#'
#' @param palette Palette name. See [palette_pequod()].
#' @param reverse Reverse the palette order.
#' @param direction `+1` (default) or `-1` to flip the palette.
#' @param ... Further arguments passed to [ggplot2::discrete_scale()].
#'
#' @return A ggplot2 scale.
#' @export
#'
#' @examples
#' \dontrun{
#' library(ggplot2)
#' ggplot(iris, aes(Sepal.Length, Sepal.Width, colour = Species)) +
#'   geom_point() +
#'   scale_color_pequod_d(palette = "crew")
#' }
scale_color_pequod_d <- function(palette = "crew",
                                 reverse = FALSE,
                                 direction = 1,
                                 ...) {
  ggplot2::discrete_scale(
    aesthetics = "colour",
    palette    = .pequod_pal_d(palette, reverse, direction),
    ...
  )
}

#' @rdname scale_color_pequod_d
#' @export
scale_colour_pequod_d <- scale_color_pequod_d

#' @rdname scale_color_pequod_d
#' @export
scale_fill_pequod_d <- function(palette = "crew",
                                reverse = FALSE,
                                direction = 1,
                                ...) {
  ggplot2::discrete_scale(
    aesthetics = "fill",
    palette    = .pequod_pal_d(palette, reverse, direction),
    ...
  )
}


#' Pequod continuous colour / fill scales for ggplot2
#'
#' Interpolates across a Pequod palette with
#' [ggplot2::scale_color_gradientn()]. Best used with the `"log"` or
#' `"log-cool"` palettes, which are ordered from light to dark; the
#' `"crew"` palettes are categorical and will not interpolate cleanly.
#'
#' @param palette Palette name. See [palette_pequod()].
#' @param reverse Reverse the palette order.
#' @param ... Further arguments passed to
#'   [ggplot2::scale_color_gradientn()] / [ggplot2::scale_fill_gradientn()].
#'
#' @return A ggplot2 scale.
#' @export
scale_color_pequod_c <- function(palette = "log", reverse = FALSE, ...) {
  cols <- palette_pequod(palette, type = "discrete")
  if (isTRUE(reverse)) cols <- rev(cols)
  ggplot2::scale_color_gradientn(colours = cols, ...)
}

#' @rdname scale_color_pequod_c
#' @export
scale_colour_pequod_c <- scale_color_pequod_c

#' @rdname scale_color_pequod_c
#' @export
scale_fill_pequod_c <- function(palette = "log", reverse = FALSE, ...) {
  cols <- palette_pequod(palette, type = "discrete")
  if (isTRUE(reverse)) cols <- rev(cols)
  ggplot2::scale_fill_gradientn(colours = cols, ...)
}


# Internal: build a palette() function that discrete_scale expects —
# it must take n and return n colours (interpolating if n exceeds the
# palette length).
.pequod_pal_d <- function(palette, reverse, direction) {
  cols <- palette_pequod(palette, type = "discrete")
  if (isTRUE(reverse) || direction == -1) cols <- rev(cols)
  function(n) {
    if (n > length(cols)) {
      grDevices::colorRampPalette(cols)(n)
    } else {
      cols[seq_len(n)]
    }
  }
}
