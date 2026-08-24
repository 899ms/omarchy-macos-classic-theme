local syntax = {
  ["@attribute"] = "#7FAEF9",
  ["@boolean"] = "#CC9E00",
  ["@comment"] = "#9D9D9D",
  ["@comment.documentation"] = "#9D9D9D",
  ["@constant"] = "#CC9E00",
  ["@constructor"] = "#CBA6F7",
  ["@error"] = "#E44A4F",
  ["@function"] = "#B3C5F3",
  ["@function.call"] = "#B3C5F3",
  ["@function.method"] = "#B3C5F3",
  ["@function.method.call"] = "#B3C5F3",
  ["@keyword"] = "#87B1F6",
  ["@keyword.conditional"] = "#87B1F6",
  ["@keyword.exception"] = "#87B1F6",
  ["@keyword.function"] = "#87B1F6",
  ["@keyword.import"] = "#87B1F6",
  ["@keyword.operator"] = "#87B1F6",
  ["@keyword.repeat"] = "#87B1F6",
  ["@number"] = "#CC9E00",
  ["@number.float"] = "#CC9E00",
  ["@operator"] = "#87B1F6",
  ["@property"] = "#BCC4E0",
  ["@string"] = "#A3E09F",
  ["@string.escape"] = "#68DC7C",
  ["@string.regexp"] = "#68DC7C",
  ["@string.special"] = "#A3E09F",
  ["@tag"] = "#419CFF",
  ["@type"] = "#CBA6F7",
  ["@type.builtin"] = "#CBA6F7",
  ["@variable.member"] = "#BCC4E0",
  ["@variable.parameter"] = "#BCC4E0",
  ["@variable.special"] = "#419CFF",
  Comment = "#9D9D9D",
  Constant = "#CC9E00",
  Error = "#E44A4F",
  Function = "#B3C5F3",
  Keyword = "#87B1F6",
  Number = "#CC9E00",
  Operator = "#87B1F6",
  Statement = "#87B1F6",
  String = "#A3E09F",
  Structure = "#CBA6F7",
  Type = "#CBA6F7",
  Typedef = "#CBA6F7",
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
        bg = "#131313",
        dark_bg = "#0D0D0D",
        darker_bg = "#080808",
        lighter_bg = "#1B1B1B",
        fg = "#DEDEDE",
        dark_fg = "#8F8F8F",
        light_fg = "#CACCCA",
        bright_fg = "#F2F9FF",
        muted = "#9D9D9D",
        red = "#FF5257",
        yellow = "#CC9E00",
        orange = "#E19773",
        green = "#30D158",
        cyan = "#0AC2A2",
        blue = "#419CFF",
        magenta = "#A550A7",
        brown = "#B0A878",
        bright_red = "#FF696D",
        bright_yellow = "#DBBB76",
        bright_green = "#68DC7C",
        bright_cyan = "#5CDBC6",
        bright_blue = "#7FAEF9",
        bright_magenta = "#B283F8",
        accent = "#077CFD",
        cursor = "#F2F9FF",
        foreground = "#DEDEDE",
        background = "#131313",
        selection = "#3F638B",
        selection_foreground = "#F2F9FF",
        selection_background = "#3F638B",
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
