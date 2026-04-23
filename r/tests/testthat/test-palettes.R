test_that("log scale has twelve steps, named Log 50 to Log 950", {
  expect_length(pequod_log, 12)
  expect_identical(names(pequod_log)[1], "Log 50")
  expect_identical(names(pequod_log)[12], "Log 950")
})

test_that("crew palettes have eight named entries each", {
  expect_length(pequod_crew_light, 8)
  expect_length(pequod_crew_dark, 8)
  expect_identical(names(pequod_crew_light), names(pequod_crew_dark))
  expect_setequal(
    names(pequod_crew_light),
    c("Ahab", "Starbuck", "Queequeg", "Pip",
      "Ishmael", "Stubb", "Tashtego", "Daggoo")
  )
})

test_that("every palette entry is a valid six-digit hex code", {
  all_hex <- c(pequod_log, pequod_crew_light, pequod_crew_dark)
  expect_true(all(grepl("^#[0-9A-Fa-f]{6}$", all_hex)))
})

test_that("pequod_crew bundles light, dark, and roles", {
  expect_named(pequod_crew, c("light", "dark", "roles"))
  expect_length(pequod_crew$roles, 8)
})

test_that("palette_pequod returns an unnamed character vector", {
  x <- palette_pequod("log")
  expect_type(x, "character")
  expect_length(x, 12)
  expect_null(names(x))
})

test_that("palette_pequod supports continuous interpolation", {
  x <- palette_pequod("log", n = 100, type = "continuous")
  expect_length(x, 100)
  expect_true(all(grepl("^#[0-9A-Fa-f]{6}$", x)))
})

test_that("palette_pequod reverse flag flips the palette", {
  fwd <- palette_pequod("log")
  rev <- palette_pequod("log", reverse = TRUE)
  expect_identical(fwd, rev(rev))
})

test_that("palette_pequod errors on unknown palette name", {
  expect_error(palette_pequod("nonexistent"), "Unknown palette")
})

test_that("palette_pequod errors when requesting too many discrete colours", {
  expect_error(palette_pequod("crew", n = 100), "has only")
})

test_that("ggplot2 scale builders return Scale objects", {
  skip_if_not_installed("ggplot2")
  expect_s3_class(scale_color_pequod_d(), "Scale")
  expect_s3_class(scale_fill_pequod_d(), "Scale")
  expect_s3_class(scale_color_pequod_c(), "Scale")
  expect_s3_class(scale_fill_pequod_c(), "Scale")
})
