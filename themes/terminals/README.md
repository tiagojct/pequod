# Pequod terminal themes

Pequod for the terminal you actually use. All six files map the same
ANSI palette — Log 950 background, Log 100 foreground, eight crew
accents on ANSI 1–6 plus brighter shades for the bright variants —
so different terminals look like the same colour scheme.

| Terminal | File | Install |
|---|---|---|
| **Ghostty** | `Pequod.ghostty` | Drop in `~/.config/ghostty/themes/Pequod`, then add `theme = Pequod` to your config. |
| **Alacritty** | `Pequod.alacritty.toml` | Drop in `~/.config/alacritty/themes/pequod.toml`, then `import = ["~/.config/alacritty/themes/pequod.toml"]` in `[general]`. |
| **kitty** | `Pequod.kitty.conf` | Drop in `~/.config/kitty/themes/Pequod.conf`, then `kitty +kitten themes Pequod` (or `include themes/Pequod.conf`). |
| **WezTerm** | `Pequod.wezterm.lua` | Drop in `~/.config/wezterm/colors/Pequod.lua`, then `config.color_scheme = "Pequod"` in `wezterm.lua`. |
| **tmux** | `Pequod.tmux.conf` | `source-file ~/.config/tmux/Pequod.tmux.conf` from your `tmux.conf`. |
| **Windows Terminal** | `Pequod.windowsterminal.json` | Open Settings → JSON, paste the object into the `schemes` array, set `defaults.colorScheme` to `"Pequod"`. |

The iTerm2 preset (`../Pequod.itermcolors`) shares the same ANSI
mapping and lives one directory up to keep it close to the canonical
`pequod.json` and the rest of the themes.

A light terminal preset for each of these is on the roadmap.
