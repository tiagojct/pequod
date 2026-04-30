/**
 * pequod-tailwind — the Pequod colour palette for Tailwind CSS.
 *
 * Drop into your tailwind.config.js (Tailwind v3) like this:
 *
 *   const pequod = require("pequod-tailwind");
 *
 *   module.exports = {
 *     theme: {
 *       extend: {
 *         colors: pequod.colors,
 *       },
 *     },
 *   };
 *
 * Then write classes like `bg-log-50`, `text-log-800`, `border-ahab`,
 * `bg-ahab/10`, `text-pip-dark`, etc.
 *
 * Or apply only what you need:
 *
 *   colors: {
 *     paper: pequod.log[50],
 *     ink:   pequod.log[950],
 *     ahab:  pequod.crew.ahab,
 *   }
 *
 * Tailwind v4: import the plugin or merge the colours via the @theme
 * directive. See README.md for the v4 example.
 *
 * Generated from pequod.json (v0.2.0-alpha) — do not edit by hand.
 * Re-generate with: node data-raw/generate.mjs
 */

"use strict";

/** @type {Record<string, string>} The twelve-step Log base scale. */
const log = Object.freeze({
  50:  "#F7F3EE",
  100: "#EAE1D7",
  150: "#DBC9B6",
  200: "#CFAD8E",
  300: "#BD8C68",
  400: "#A16E50",
  500: "#835A49",
  600: "#335260",
  700: "#163F54",
  800: "#0D2F42",
  900: "#0C222F",
  950: "#0B1720",
});

/**
 * Crew accents. Each member exposes a `DEFAULT` (the light variant —
 * Tailwind's convention so `bg-ahab` resolves to the saturated value),
 * an explicit `light`, and a `dark` for dark-theme contexts.
 */
const crew = Object.freeze({
  ahab:     Object.freeze({ DEFAULT: "#A83732", light: "#A83732", dark: "#E3877C" }),
  starbuck: Object.freeze({ DEFAULT: "#0082B1", light: "#0082B1", dark: "#A6DFFF" }),
  queequeg: Object.freeze({ DEFAULT: "#253E82", light: "#253E82", dark: "#838CCF" }),
  pip:      Object.freeze({ DEFAULT: "#6A4A00", light: "#6A4A00", dark: "#DEC577" }),
  ishmael:  Object.freeze({ DEFAULT: "#76716B", light: "#76716B", dark: "#BFBBB6" }),
  stubb:    Object.freeze({ DEFAULT: "#CA6435", light: "#CA6435", dark: "#FFD9BB" }),
  tashtego: Object.freeze({ DEFAULT: "#177C55", light: "#177C55", dark: "#82C4A2" }),
  daggoo:   Object.freeze({ DEFAULT: "#552823", light: "#552823", dark: "#A17069" }),
});

/**
 * The merged colour palette ready to spread into Tailwind's
 * `theme.extend.colors`. Every key is a top-level Tailwind colour
 * name; nested objects expose shades (`log.50`) and crew variants
 * (`ahab.dark`).
 */
const colors = Object.freeze({
  log,
  ...crew,
});

module.exports = {
  log,
  crew,
  colors,
};
module.exports.default = module.exports;
