/**
 * Type declarations for pequod-tailwind.
 *
 * The Pequod colour palette as plain JS objects, ready to spread into
 * a Tailwind CSS `theme.extend.colors` block.
 */

/** The twelve-step Log base scale, keyed by their numbered steps. */
export interface LogScale {
  50: "#FBFAF5";
  100: "#F8F4EB";
  150: "#ECE5D3";
  200: "#DFD3B8";
  300: "#C4A57B";
  400: "#A8865E";
  500: "#8B7B6B";
  600: "#6E5F52";
  700: "#527275";
  800: "#2C3E50";
  900: "#1C2936";
  950: "#13181F";
}

/**
 * A crew accent with three accessors:
 *   - DEFAULT (Tailwind convention — used by `bg-ahab`)
 *   - light   (the saturated variant tuned for Log 100 paper)
 *   - dark    (the brighter variant tuned for Log 950 ink)
 */
export interface CrewVariant {
  DEFAULT: string;
  light: string;
  dark: string;
}

export type CrewName =
  | "ahab"
  | "starbuck"
  | "queequeg"
  | "pip"
  | "ishmael"
  | "stubb"
  | "tashtego"
  | "daggoo";

export type Crew = Record<CrewName, CrewVariant>;

/** The Log base scale. */
export const log: LogScale;

/** The eight crew accents, each with light + dark variants. */
export const crew: Crew;

/**
 * Merged palette ready to spread into Tailwind's `theme.extend.colors`.
 * Equivalent to `{ log, ...crew }`.
 */
export const colors: { log: LogScale } & Crew;

declare const _default: {
  log: LogScale;
  crew: Crew;
  colors: { log: LogScale } & Crew;
};
export default _default;
