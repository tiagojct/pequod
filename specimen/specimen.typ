// Pequod — printable palette specimen.
// Regenerate with: typst compile specimen/specimen.typ specimen/specimen.pdf
//
// Fonts: Atkinson Hyperlegible Next + JetBrains Mono (Google Fonts, OFL).
// Must be installed on the system or available via --font-path. The website
// uses the same fonts.

#set document(
  title: "Pequod — palette specimen",
  author: "Tiago Jacinto",
)

#set page(
  paper: "a4",
  margin: (top: 1.7cm, bottom: 1.6cm, left: 1.8cm, right: 1.8cm),
  fill: rgb("#F7F3EE"),   // Log 50 — paper
)

#set text(
  font: "Atkinson Hyperlegible Next",
  size: 10pt,
  fill: rgb("#0D2F42"),   // Log 800 — ink
)

#set par(leading: 0.55em, justify: false)


// ── palette ────────────────────────────────────────────────────────────

#let log-scale = (
  (name: "Log 50",  hex: "#F7F3EE", dark-bg: false),
  (name: "Log 100", hex: "#EAE1D7", dark-bg: false),
  (name: "Log 150", hex: "#DBC9B6", dark-bg: false),
  (name: "Log 200", hex: "#CFAD8E", dark-bg: false),
  (name: "Log 300", hex: "#BD8C68", dark-bg: false),
  (name: "Log 400", hex: "#A16E50", dark-bg: false),
  (name: "Log 500", hex: "#835A49", dark-bg: true),
  (name: "Log 600", hex: "#335260", dark-bg: true),
  (name: "Log 700", hex: "#163F54", dark-bg: true),
  (name: "Log 800", hex: "#0D2F42", dark-bg: true),
  (name: "Log 900", hex: "#0C222F", dark-bg: true),
  (name: "Log 950", hex: "#0B1720", dark-bg: true),
)

#let crew = (
  (name: "Ahab",     role: "red",    light: "#A83732", dark: "#E3877C", note: "errors, alarms, destructive actions"),
  (name: "Starbuck", role: "blue",   light: "#0082B1", dark: "#A6DFFF", note: "functions, primary actions, hyperlinks"),
  (name: "Queequeg", role: "indigo", light: "#253E82", dark: "#838CCF", note: "types, classes, interfaces"),
  (name: "Pip",      role: "yellow", light: "#6A4A00", dark: "#DEC577", note: "numbers, literals, highlights"),
  (name: "Ishmael",  role: "grey",   light: "#76716B", dark: "#BFBBB6", note: "comments, punctuation, muted text"),
  (name: "Stubb",    role: "orange", light: "#CA6435", dark: "#FFD9BB", note: "constants, warnings, changes"),
  (name: "Tashtego", role: "green",  light: "#177C55", dark: "#82C4A2", note: "strings, success, additions"),
  (name: "Daggoo",   role: "brown",  light: "#552823", dark: "#A17069", note: "variables, references, identifiers"),
)


// ── helpers ────────────────────────────────────────────────────────────

#let section-label(body) = text(
  fill: rgb("#335260"),
  size: 8pt,
  weight: "semibold",
  tracking: 0.12em,
)[#upper(body)]

#let log-swatch(entry) = {
  let fg = if entry.dark-bg { rgb("#EAE1D7") } else { rgb("#0D2F42") }
  block(
    fill: rgb(entry.hex),
    width: 100%,
    height: 3em,
    inset: (x: 0.55em, y: 0.45em),
    radius: 2pt,
    stroke: 0.4pt + rgb("#CFAD8E"),
    stack(
      spacing: 0.2em,
      text(fill: fg, size: 8pt, weight: "semibold")[#entry.name],
      text(fill: fg, size: 7pt, font: "JetBrains Mono")[#entry.hex],
    ),
  )
}

// Accent chips: the "light-variant" hex is the saturated, darker colour
// (designed against Log 100 paper), so it needs cream text on top. The
// "dark-variant" hex is the brighter, de-saturated colour (designed
// against Log 950 ink), so it reads best with navy text.
#let accent-chip(hex, variant: "light") = {
  let fg = if variant == "light" { rgb("#EAE1D7") } else { rgb("#0D2F42") }
  block(
    fill: rgb(hex),
    width: 100%,
    height: 1.8em,
    inset: (x: 0.55em, y: 0.3em),
    radius: 2pt,
    stroke: 0.3pt + rgb("#CFAD8E"),
    align(center + horizon,
      text(fill: fg, size: 7pt, font: "JetBrains Mono", weight: "medium")[#hex]
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
    text(weight: "bold", size: 26pt, fill: rgb("#0D2F42"))[Pequod],
    text(size: 10pt, fill: rgb("#335260"))[
      A pigment-inspired colour palette for reading and code.
    ],
  ),
  stack(
    spacing: 0.25em,
    text(size: 8pt, fill: rgb("#163F54"), font: "JetBrains Mono")[v0.2.0-alpha],
    text(size: 8pt, fill: rgb("#335260"))[tiagojct.eu/projects/pequod/],
  ),
)

#v(1.2em)
#line(length: 100%, stroke: 0.4pt + rgb("#CFAD8E"))
#v(0.8em)


// ── the log scale ──────────────────────────────────────────────────────

#section-label("The Log scale") #h(0.5em)
#text(size: 8pt, fill: rgb("#835A49"))[warm paper  →  deep ink  ·  twelve steps]
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
#text(size: 8pt, fill: rgb("#835A49"))[eight accents, each a character; light · dark variants]
#v(0.4em)

#table(
  columns: (auto, auto, 5.2em, 5.2em, 1fr),
  stroke: none,
  align: (left + horizon, left + horizon, center + horizon, center + horizon, left + horizon),
  inset: (x: 0.5em, y: 0.35em),
  ..crew.map(e => (
    text(weight: "semibold", size: 10pt)[#e.name],
    text(size: 8pt, fill: rgb("#335260"), font: "JetBrains Mono")[#e.role],
    accent-chip(e.light, variant: "light"),
    accent-chip(e.dark,  variant: "dark"),
    text(size: 9pt, fill: rgb("#335260"))[#e.note],
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

#let kw(t)   = text(fill: rgb("#E3877C"))[#t]              // keyword — Ahab
#let fn(t)   = text(fill: rgb("#A6DFFF"))[#t]              // function — Starbuck
#let ty(t)   = text(fill: rgb("#838CCF"))[#t]              // type — Queequeg
#let num(t)  = text(fill: rgb("#DEC577"))[#t]              // number — Pip
#let str(t)  = text(fill: rgb("#82C4A2"))[#t]              // string — Tashtego
#let prop(t) = text(fill: rgb("#A17069"))[#t]              // parameter/property — Daggoo
#let cmt(t)  = text(fill: rgb("#BFBBB6"), style: "italic")[#t]  // comment — Ishmael
#let pun(t)  = text(fill: rgb("#BFBBB6"))[#t]              // operator/punctuation
#let var(t)  = text(fill: rgb("#EAE1D7"))[#t]              // plain variable
#let nl      = linebreak()

#block(
  fill: rgb("#0B1720"),
  inset: (x: 1em, y: 0.85em),
  radius: 3pt,
  width: 100%,
  [
    #set text(font: "JetBrains Mono", size: 9pt, fill: rgb("#EAE1D7"))
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
  #text(size: 7pt, fill: rgb("#835A49"), font: "JetBrains Mono")[
    PEQUOD  ·  v0.2.0-alpha  ·  CC-BY-4.0 (palette) + MIT (code)  ·  github.com/tiagojct/pequod
  ]
]
