local active_border_color = "rgb(7a7a7a)"
-- Full opacity on purpose: the shared default is rgba(595959aa), and that alpha
-- blends the inactive frame down into the near-black surface until it vanishes.
local inactive_border_color = "rgb(595959)"

hl.config({
  general = {
    col = {
      active_border = active_border_color,
      inactive_border = inactive_border_color,
    },
  },

  group = {
    col = {
      border_active = active_border_color,
      border_inactive = inactive_border_color,
    },
  },
})
