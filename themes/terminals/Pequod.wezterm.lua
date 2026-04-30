-- Pequod — WezTerm colour scheme (dark)
-- https://tiagojct.eu/projects/pequod/
--
-- Background: Log 950 (#0B1720).  Foreground: Log 100 (#EAE1D7).
-- Save to ~/.config/wezterm/colors/Pequod.lua, then add to your
-- wezterm.lua:
--
--     config.color_scheme = "Pequod"

return {
  foreground       = "#EAE1D7",
  background       = "#0B1720",

  cursor_bg        = "#BD8C68",
  cursor_fg        = "#0B1720",
  cursor_border    = "#BD8C68",

  selection_fg     = "#EAE1D7",
  selection_bg     = "#0D2F42",

  scrollbar_thumb  = "#163f54",
  split            = "#0D2F42",

  ansi = {
    "#0C222F",   -- black
    "#E3877C",   -- red       (Ahab dark)
    "#82C4A2",   -- green     (Tashtego dark)
    "#DEC577",   -- yellow    (Pip dark)
    "#A6DFFF",   -- blue      (Starbuck dark)
    "#838CCF",   -- magenta   (Queequeg dark)
    "#9DC2C5",   -- cyan      (Softsage 3)
    "#EAE1D7",   -- white     (Log 100)
  },
  brights = {
    "#335260",   -- bright black
    "#E99C93",   -- bright red
    "#AFCCA6",   -- bright green
    "#E8CB8C",   -- bright yellow
    "#A0C2D4",   -- bright blue
    "#AAADDA",   -- bright magenta
    "#BCD9DB",   -- bright cyan
    "#F7F3EE",   -- bright white (Log 50)
  },

  tab_bar = {
    background = "#0C222F",
    active_tab = {
      bg_color = "#163f54",
      fg_color = "#EAE1D7",
    },
    inactive_tab = {
      bg_color = "#0C222F",
      fg_color = "#BFBBB6",
    },
    inactive_tab_hover = {
      bg_color = "#0D2F42",
      fg_color = "#EAE1D7",
    },
    new_tab = {
      bg_color = "#0C222F",
      fg_color = "#BFBBB6",
    },
    new_tab_hover = {
      bg_color = "#0D2F42",
      fg_color = "#EAE1D7",
    },
  },
}
