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
 * Generated from pequod.json (v0.1.0-alpha) — do not edit by hand.
 * Re-generate with: node data-raw/generate.mjs
 */

"use strict";

/** @type {Record<string, string>} The twelve-step Log base scale. */
const log = Object.freeze({
  50:  "#FBFAF5",
  100: "#F8F4EB",
  150: "#ECE5D3",
  200: "#DFD3B8",
  300: "#C4A57B",
  400: "#A8865E",
  500: "#8B7B6B",
  600: "#6E5F52",
  700: "#527275",
  800: "#2C3E50",
  900: "#1C2936",
  950: "#13181F",
});

/**
 * Crew accents. Each member exposes a `DEFAULT` (the light variant —
 * Tailwind's convention so `bg-ahab` resolves to the saturated value),
 * an explicit `light`, and a `dark` for dark-theme contexts.
 */
const crew = Object.freeze({
  ahab:     Object.freeze({ DEFAULT: "#B5534A", light: "#B5534A", dark: "#E07A72" }),
  starbuck: Object.freeze({ DEFAULT: "#527C98", light: "#527C98", dark: "#7FA8C3" }),
  queequeg: Object.freeze({ DEFAULT: "#4A4E8C", light: "#4A4E8C", dark: "#8A8ECE" }),
  pip:      Object.freeze({ DEFAULT: "#A8812B", light: "#A8812B", dark: "#D9B461" }),
  ishmael:  Object.freeze({ DEFAULT: "#6E6E6B", light: "#6E6E6B", dark: "#A5A5A0" }),
  stubb:    Object.freeze({ DEFAULT: "#B5683A", light: "#B5683A", dark: "#E29B6E" }),
  tashtego: Object.freeze({ DEFAULT: "#507352", light: "#507352", dark: "#8AB08C" }),
  daggoo:   Object.freeze({ DEFAULT: "#7A5440", light: "#7A5440", dark: "#AF8870" }),
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
