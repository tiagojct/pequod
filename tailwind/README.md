# pequod-tailwind

The Pequod palette for Tailwind CSS — the full Log base scale, eight
crew accents (light + dark variants), all named after the crew of the
whaler in *Moby-Dick*. Designed for long-form reading, not glance-
ability.

The narrative, design rationale, and full accessibility analysis live
in the [main repository](https://github.com/tiagojct/pequod) and on
the [project website](https://tiagojct.eu/projects/pequod/).

## Install

```bash
npm install pequod-tailwind
# or: pnpm add pequod-tailwind
# or: yarn add pequod-tailwind
```

## Use — Tailwind v3

`tailwind.config.js`:

```js
const pequod = require("pequod-tailwind");

module.exports = {
  content: ["./src/**/*.{html,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: pequod.colors,   // log + all eight crew accents
    },
  },
};
```

Now you can write classes like:

```html
<body class="bg-log-50 text-log-800 dark:bg-log-950 dark:text-log-100">
  <h1 class="text-queequeg dark:text-queequeg-dark">Pequod</h1>
  <p class="text-log-700 dark:text-log-300">
    A pigment-inspired colour palette for reading and code.
  </p>
  <code class="bg-log-150 text-daggoo dark:bg-log-900 dark:text-daggoo-dark">
    palette("crew")
  </code>
  <button class="bg-starbuck text-log-50 hover:bg-starbuck-dark">
    Read on
  </button>
</body>
```

## Use — Tailwind v4

`app.css` (or wherever your `@theme` lives):

```css
@import "tailwindcss";
@import "pequod-tailwind/index.js" layer(theme);

/* or, more precisely, declare the tokens yourself: */
@theme {
  --color-log-50:  #FBFAF5;
  --color-log-100: #F8F4EB;
  /* ... etc; see `node_modules/pequod-tailwind/index.js` for all values */
  --color-ahab:    #B5534A;
  --color-ahab-dark: #E07A72;
}
```

(A first-class v4 plugin is on the roadmap once Tailwind v4's plugin
API stabilises further.)

## Apply only what you need

If you don't want every Pequod colour to leak into your tab-completion
in editors, pull just the shades you use:

```js
const pequod = require("pequod-tailwind");

module.exports = {
  theme: {
    colors: {
      paper:  pequod.log[50],
      ink:    pequod.log[950],
      muted:  pequod.log[600],
      accent: pequod.crew.starbuck.DEFAULT,
      danger: pequod.crew.ahab.DEFAULT,
    },
  },
};
```

## API

```js
const pequod = require("pequod-tailwind");

pequod.log        // { 50: "#FBFAF5", 100: "#F8F4EB", ..., 950: "#13181F" }
pequod.crew       // { ahab: { DEFAULT, light, dark }, starbuck: {...}, ... }
pequod.colors     // { log, ahab, starbuck, queequeg, pip, ishmael,
                  //   stubb, tashtego, daggoo }
```

Every crew member has a `DEFAULT` (so `bg-ahab` works) plus an
explicit `light` and `dark`. The defaults are the saturated
"light-mode" variants — designed against Log 100 paper. Dark-mode
variants are tuned for Log 950 ink and clear WCAG-AA on that surface.

## Accessibility

- Body-text contrast on the light theme: **10.5 : 1** (Log 800 on
  Log 50). On dark: **16.2 : 1** (Log 100 on Log 950).
- All eight dark-mode crew accents clear WCAG-AA (4.5 : 1) on Log 950.
- Five of eight light-mode crew accents clear AA-body on Log 100; the
  other three (Pip, Stubb, Starbuck) sit between 3.3 and 4.1 — fine
  for bold, large text, or UI elements where AA-large (3 : 1) applies.

The full colour-vision-deficiency analysis (including which crew pairs
collapse under each dichromacy) lives in the
[main repository](https://github.com/tiagojct/pequod#colour-vision-deficiency).

## Beyond Tailwind

Pequod also ships as:

- **VS Code** themes (Marketplace + Open VSX) — `tiagojct.pequod-color-theme`
- **Zed** theme family (dark + light, single file)
- **iTerm2 / Ghostty / Alacritty / kitty / WezTerm / tmux / Windows Terminal** — terminal presets
- **Python** package — `pip install pequod`
- **R** package — install from GitHub or CRAN (review pending)
- **Printable A4 specimen** PDF generated from the canonical tokens

All of these live at [github.com/tiagojct/pequod](https://github.com/tiagojct/pequod).

## Licence

MIT. The underlying palette tokens are also published under
CC-BY-4.0 in the upstream repository.
