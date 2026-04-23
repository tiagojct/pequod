// Pequod — printable palette specimen.
// Regenerate with: typst compile specimen/specimen.typ specimen/specimen.pdf
//
// Fonts: Geist + Geist Mono (Google Fonts, OFL). Must be installed on the
// system or available via --font-path. The website uses the same fonts.

#set document(
  title: "Pequod — palette specimen",
  author: "Tiago Jacinto",
)

#set page(
  paper: "a4",
  margin: (top: 1.7cm, bottom: 1.6cm, left: 1.8cm, right: 1.8cm),
  fill: rgb("#FBFAF5"),   // Log 50 — paper
)

#set text(
  font: "Geist",
  size: 10pt,
  fill: rgb("#2C3E50"),   // Log 800 — ink
)

#set par(leading: 0.55em, justify: false)


// ── palette ────────────────────────────────────────────────────────────

#let log-scale = (
  (name: "Log 50",  hex: "#FBFAF5", dark-bg: false),
  (name: "Log 100", hex: "#F8F4EB", dark-bg: false),
  (name: "Log 150", hex: "#ECE5D3", dark-bg: false),
  (name: "Log 200", hex: "#DFD3B8", dark-bg: false),
  (name: "Log 300", hex: "#C4A57B", dark-bg: false),
  (name: "Log 400", hex: "#A8865E", dark-bg: false),
  (name: "Log 500", hex: "#8B7B6B", dark-bg: true),
  (name: "Log 600", hex: "#6E5F52", dark-bg: true),
  (name: "Log 700", hex: "#527275", dark-bg: true),
  (name: "Log 800", hex: "#2C3E50", dark-bg: true),
  (name: "Log 900", hex: "#1C2936", dark-bg: true),
  (name: "Log 950", hex: "#13181F", dark-bg: true),
)

#let crew = (
  (name: "Ahab",     role: "red",    light: "#B5534A", dark: "#E07A72", note: "errors, alarms, destructive actions"),
  (name: "Starbuck", role: "blue",   light: "#527C98", dark: "#7FA8C3", note: "functions, primary actions, hyperlinks"),
  (name: "Queequeg", role: "indigo", light: "#4A4E8C", dark: "#8A8ECE", note: "types, classes, interfaces"),
  (name: "Pip",      role: "yellow", light: "#A8812B", dark: "#D9B461", note: "numbers, literals, highlights"),
  (name: "Ishmael",  role: "grey",   light: "#6E6E6B", dark: "#A5A5A0", note: "comments, punctuation, muted text"),
  (name: "Stubb",    role: "orange", light: "#B5683A", dark: "#E29B6E", note: "constants, warnings, changes"),
  (name: "Tashtego", role: "green",  light: "#507352", dark: "#8AB08C", note: "strings, success, additions"),
  (name: "Daggoo",   role: "brown",  light: "#7A5440", dark: "#AF8870", note: "variables, references, identifiers"),
)


// ── helpers ────────────────────────────────────────────────────────────

#let section-label(body) = text(
  fill: rgb("#6E5F52"),
  size: 8pt,
  weight: "semibold",
  tracking: 0.12em,
)[#upper(body)]

#let log-swatch(entry) = {
  let fg = if entry.dark-bg { rgb("#F8F4EB") } else { rgb("#2C3E50") }
  block(
    fill: rgb(entry.hex),
    width: 100%,
    height: 3em,
    inset: (x: 0.55em, y: 0.45em),
    radius: 2pt,
    stroke: 0.4pt + rgb("#DFD3B8"),
    stack(
      spacing: 0.2em,
      text(fill: fg, size: 8pt, weight: "semibold")[#entry.name],
      text(fill: fg, size: 7pt, font: "Geist Mono")[#entry.hex],
    ),
  )
}

// Accent chips: the "light-variant" hex is the saturated, darker colour
// (designed against Log 100 paper), so it needs cream text on top. The
// "dark-variant" hex is the brighter, de-saturated colour (designed
// against Log 950 ink), so it reads best with navy text.
#let accent-chip(hex, variant: "light") = {
  let fg = if variant == "light" { rgb("#F8F4EB") } else { rgb("#2C3E50") }
  block(
    fill: rgb(hex),
    width: 100%,
    height: 1.8em,
    inset: (x: 0.55em, y: 0.3em),
    radius: 2pt,
    stroke: 0.3pt + rgb("#DFD3B8"),
    align(center + horizon,
      text(fill: fg, size: 7pt, font: "Geist Mono", weight: "medium")[#hex]
    ),
  )
}


// ── header ─────────────────────────────────────────────────────────────

#grid(
  columns: (1fr, auto),
  align: (left + bottom, right + bottom),
  column-gutter: 1em,
  stack(
    spacing: 0.3em,
    text(weight: "bold", size: 26pt, fill: rgb("#2C3E50"))[Pequod],
    text(size: 10pt, fill: rgb("#6E5F52"))[
      A pigment-inspired colour palette for reading and code.
    ],
  ),
  stack(
    spacing: 0.25em,
    text(size: 8pt, fill: rgb("#527275"), font: "Geist Mono")[v0.1.0-alpha],
    text(size: 8pt, fill: rgb("#6E5F52"))[tiagojct.eu/projects/pequod/],
  ),
)

#v(1.2em)
#line(length: 100%, stroke: 0.4pt + rgb("#DFD3B8"))
#v(0.8em)


// ── the log scale ──────────────────────────────────────────────────────

#section-label("The Log scale") #h(0.5em)
#text(size: 8pt, fill: rgb("#8B7B6B"))[warm paper  →  deep ink  ·  twelve steps]
#v(0.4em)

#grid(
  columns: (1fr,) * 6,
  column-gutter: 0.4em,
  row-gutter: 0.4em,
  ..log-scale.map(e => log-swatch(e))
)

#v(1.2em)


// ── the crew ───────────────────────────────────────────────────────────

#section-label("The Crew") #h(0.5em)
#text(size: 8pt, fill: rgb("#8B7B6B"))[eight accents, each a character; light · dark variants]
#v(0.4em)

#table(
  columns: (auto, auto, 5.2em, 5.2em, 1fr),
  stroke: none,
  align: (left + horizon, left + horizon, center + horizon, center + horizon, left + horizon),
  inset: (x: 0.5em, y: 0.35em),
  ..crew.map(e => (
    text(weight: "semibold", size: 10pt)[#e.name],
    text(size: 8pt, fill: rgb("#6E5F52"), font: "Geist Mono")[#e.role],
    accent-chip(e.light, variant: "light"),
    accent-chip(e.dark,  variant: "dark"),
    text(size: 9pt, fill: rgb("#6E5F52"))[#e.note],
  )).flatten()
)

#v(1.2em)


// ── prose sample ───────────────────────────────────────────────────────

#section-label("Prose sample · Log 800 on Log 50")
#v(0.4em)

#block(inset: (x: 0.1em))[
  Pequod is a palette designed for long reading. Paper to ink, with eight accent hues drawn in the same pigment register — earthy, muted, the colours of things that have been in the world long enough to weather. The whole thing is named after the whaler in #emph[Moby-Dick], and its accents are named after the people who sailed her.

  Most terminal and editor palettes are optimised for glance, not reading. Saturated primaries tire the eye after ten minutes. Pequod aims for comfort at hour four.
]

#v(1em)


// ── code sample (dark) ─────────────────────────────────────────────────

#section-label("Code sample · dark (Log 950 + crew accents)")
#v(0.4em)

#let kw(t)   = text(fill: rgb("#E07A72"))[#t]              // keyword — Ahab
#let fn(t)   = text(fill: rgb("#7FA8C3"))[#t]              // function — Starbuck
#let ty(t)   = text(fill: rgb("#8A8ECE"))[#t]              // type — Queequeg
#let num(t)  = text(fill: rgb("#D9B461"))[#t]              // number — Pip
#let str(t)  = text(fill: rgb("#8AB08C"))[#t]              // string — Tashtego
#let prop(t) = text(fill: rgb("#AF8870"))[#t]              // parameter/property — Daggoo
#let cmt(t)  = text(fill: rgb("#A5A5A0"), style: "italic")[#t]  // comment — Ishmael
#let pun(t)  = text(fill: rgb("#A5A5A0"))[#t]              // operator/punctuation
#let var(t)  = text(fill: rgb("#F8F4EB"))[#t]              // plain variable
#let nl      = linebreak()

#block(
  fill: rgb("#13181F"),
  inset: (x: 1em, y: 0.85em),
  radius: 3pt,
  width: 100%,
  [
    #set text(font: "Geist Mono", size: 9pt, fill: rgb("#F8F4EB"))
    #set par(leading: 0.5em)

    #cmt("# Apply the ICD-10 cohort definition for acute MI")#nl
    #kw("def") #fn("build_cohort")#pun("(")#prop("df")#pun(":") #ty("DataFrame")#pun(")") #pun("->") #ty("DataFrame")#pun(":")#nl
    #h(2em)#str(`"""Select first admissions with a primary ICD-10 I21.* code."""`)#nl
    #h(2em)#prop("mask") #pun("=") #prop("df")#pun("[")#str(`"primary_icd10"`)#pun("].")#fn("str")#pun(".")#fn("startswith")#pun("(")#str(`"I21"`)#pun(")")#nl
    #h(2em)#kw("return") #pun("(")#nl
    #h(4em)#prop("df")#pun("[")#prop("mask")#pun("]")#nl
    #h(6em)#pun(".")#fn("sort_values")#pun("(")#str(`"admission_date"`)#pun(")")#nl
    #h(6em)#pun(".")#fn("drop_duplicates")#pun("(")#str(`"patient_id"`)#pun(")")#nl
    #h(6em)#pun(".")#fn("head")#pun("(")#num("1")#pun(")")#nl
    #h(2em)#pun(")")
  ]
)

#v(0.8em)


// ── licence tag (footer) ───────────────────────────────────────────────

#align(center)[
  #text(size: 7pt, fill: rgb("#8B7B6B"), font: "Geist Mono")[
    PEQUOD  ·  v0.1.0-alpha  ·  CC-BY-4.0 (palette) + MIT (code)  ·  github.com/tiagojct/pequod
  ]
]
