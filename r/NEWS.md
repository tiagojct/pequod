# pequod 0.3.0

This is the last release of the package. Pequod is now part of Ensigns, a set of
ten colour families: <https://ensigns.tiagojacinto.eu>, with the source at
<https://github.com/tiagojct/ensigns>.

* Six crew colours changed so that every crew colour reaches 4.5:1 (WCAG AA) as
  text on its page. The Log scale and the other ten crew colours are unchanged.
  The functions and their signatures are unchanged.
  * Ahab, light variant: #A83732 to #931432.
  * Starbuck, light variant: #0082B1 to #006A98.
  * Ishmael, light variant: #76716B to #6A6164.
  * Stubb, light variant: #CA6435 to #AA430B.
  * Tashtego, light variant: #177C55 to #06724B.
  * Daggoo, dark variant: #A17069 to #A7766F.

* `pequod_crew_light`, `pequod_crew_dark`, the `crew`, `crew-dark` and `syntax`
  palettes of `palette_pequod()` and the discrete scales return the new values.

* The project link in `DESCRIPTION` and in the help pages points to
  <https://ensigns.tiagojacinto.eu/pequod/>. The old link returned 404.
