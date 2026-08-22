local syntax = {
  ["@attribute"] = "#0433FF",
  ["@boolean"] = "#C5060B",
  ["@comment"] = "#007FFF",
  ["@comment.documentation"] = "#007FFF",
  ["@constant"] = "#C5060B",
  ["@constructor"] = "#0433FF",
  ["@error"] = "#D21F07",
  ["@function"] = "#0000A2",
  ["@function.call"] = "#0000A2",
  ["@function.method"] = "#0000A2",
  ["@function.method.call"] = "#0000A2",
  ["@keyword"] = "#0433FF",
  ["@keyword.conditional"] = "#0433FF",
  ["@keyword.exception"] = "#0433FF",
  ["@keyword.function"] = "#0433FF",
  ["@keyword.import"] = "#0433FF",
  ["@keyword.operator"] = "#0433FF",
  ["@keyword.repeat"] = "#0433FF",
  ["@number"] = "#0433FF",
  ["@number.float"] = "#0433FF",
  ["@operator"] = "#0433FF",
  ["@property"] = "#333333",
  ["@string"] = "#036A07",
  ["@string.escape"] = "#036A07",
  ["@string.regexp"] = "#036A07",
  ["@string.special"] = "#036A07",
  ["@tag"] = "#0060DE",
  ["@type"] = "#6F42C1",
  ["@type.builtin"] = "#6F42C1",
  ["@variable.member"] = "#333333",
  ["@variable.parameter"] = "#333333",
  ["@variable.special"] = "#C76500",
  Comment = "#007FFF",
  Constant = "#C5060B",
  Error = "#D21F07",
  Function = "#0000A2",
  Keyword = "#0433FF",
  Number = "#0433FF",
  Operator = "#0433FF",
  Statement = "#0433FF",
  String = "#036A07",
  Structure = "#6F42C1",
  Type = "#6F42C1",
  Typedef = "#6F42C1",
}

local function apply_syntax()
  for group, color in pairs(syntax) do
    local highlight = vim.api.nvim_get_hl(0, { name = group, link = false })
    highlight.fg = tonumber(color:sub(2), 16)
    vim.api.nvim_set_hl(0, group, highlight)
  end
end

return {
  {
    "bjarneo/aether.nvim",
    branch = "v3",
    name = "aether",
    priority = 1000,
    opts = {
      colors = {
        bg = "#F9F9F9",
        dark_bg = "#E9E9E9",
        darker_bg = "#E0E0E0",
        lighter_bg = "#F5F5F5",
        fg = "#000000",
        dark_fg = "#555555",
        light_fg = "#333333",
        bright_fg = "#000000",
        muted = "#555555",
        red = "#D21F07",
        yellow = "#B59A00",
        orange = "#C76500",
        green = "#319A00",
        cyan = "#007E8A",
        blue = "#0060DE",
        magenta = "#9A0068",
        brown = "#957931",
        bright_red = "#C5060B",
        bright_yellow = "#957931",
        bright_green = "#036A07",
        bright_cyan = "#007FFF",
        bright_blue = "#0433FF",
        bright_magenta = "#6F42C1",
        accent = "#0060DE",
        cursor = "#000000",
        foreground = "#000000",
        background = "#F9F9F9",
        selection = "#B8D8FF",
        selection_foreground = "#000000",
        selection_background = "#B8D8FF",
      },
    },
    init = function()
      vim.api.nvim_create_autocmd("ColorScheme", {
        pattern = "aether",
        callback = apply_syntax,
      })
      if vim.g.colors_name == "aether" then
        apply_syntax()
      end
    end,
  },
  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = "aether",
    },
  },
}
