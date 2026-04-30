/**
 * Type declarations for pequod-tailwind.
 *
 * The Pequod colour palette as plain JS objects, ready to spread into
 * a Tailwind CSS `theme.extend.colors` block.
 */

/** The twelve-step Log base scale, keyed by their numbered steps. */
export interface LogScale {
  50: "#F7F3EE";
  100: "#EAE1D7";
  150: "#DBC9B6";
  200: "#CFAD8E";
  300: "#BD8C68";
  400: "#A16E50";
  500: "#835A49";
  600: "#335260";
  700: "#163F54";
  800: "#0D2F42";
  900: "#0C222F";
  950: "#0B1720";
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
