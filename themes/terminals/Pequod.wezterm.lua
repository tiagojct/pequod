-- Pequod — WezTerm colour scheme (dark)
-- https://tiagojct.eu/projects/pequod/
--
-- Background: Log 950 (#13181F).  Foreground: Log 100 (#F8F4EB).
-- Save to ~/.config/wezterm/colors/Pequod.lua, then add to your
-- wezterm.lua:
--
--     config.color_scheme = "Pequod"

return {
  foreground       = "#F8F4EB",
  background       = "#13181F",

  cursor_bg        = "#C4A57B",
  cursor_fg        = "#13181F",
  cursor_border    = "#C4A57B",

  selection_fg     = "#F8F4EB",
  selection_bg     = "#2C3E50",

  scrollbar_thumb  = "#527275",
  split            = "#2C3E50",

  ansi = {
    "#1C2936",   -- black
    "#E07A72",   -- red       (Ahab dark)
    "#8AB08C",   -- green     (Tashtego dark)
    "#D9B461",   -- yellow    (Pip dark)
    "#7FA8C3",   -- blue      (Starbuck dark)
    "#8A8ECE",   -- magenta   (Queequeg dark)
    "#9DC2C5",   -- cyan      (Softsage 3)
    "#F8F4EB",   -- white     (Log 100)
  },
  brights = {
    "#6E5F52",   -- bright black
    "#E99C93",   -- bright red
    "#AFCCA6",   -- bright green
    "#E8CB8C",   -- bright yellow
    "#A0C2D4",   -- bright blue
    "#AAADDA",   -- bright magenta
    "#BCD9DB",   -- bright cyan
    "#FBFAF5",   -- bright white (Log 50)
  },

  tab_bar = {
    background = "#1C2936",
    active_tab = {
      bg_color = "#527275",
      fg_color = "#F8F4EB",
    },
    inactive_tab = {
      bg_color = "#1C2936",
      fg_color = "#A5A5A0",
    },
    inactive_tab_hover = {
      bg_color = "#2C3E50",
      fg_color = "#F8F4EB",
    },
    new_tab = {
      bg_color = "#1C2936",
      fg_color = "#A5A5A0",
    },
    new_tab_hover = {
      bg_color = "#2C3E50",
      fg_color = "#F8F4EB",
    },
  },
}
