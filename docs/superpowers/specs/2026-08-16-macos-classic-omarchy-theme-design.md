# macOS Classic Omarchy Theme Design

## Goal

Create an installable Omarchy theme repository derived from the `macOS Classic` light and dark palettes in `/home/jason/work/gpui-component/themes/macos-classic.json`.

The repository will provide two independently selectable themes:

- macOS Classic Light
- macOS Classic Dark

The implementation will target the current Omarchy theme format installed on this system. The older Ayu Dark theme repository is a packaging and presentation reference, but obsolete per-application files will not be copied when current Omarchy derives them from `colors.toml`.

## Repository Structure

Each variant will live in its own installable theme directory:

```text
macos-classic-light/
  backgrounds/
  colors.toml
  hyprland.lua
  btop.theme
  chromium.theme
  icons.theme
  neovim.lua
  vscode.json
  zed.json
  preview.png
  preview-unlock.png
  unlock.png

macos-classic-dark/
  backgrounds/
  colors.toml
  hyprland.lua
  btop.theme
  chromium.theme
  icons.theme
  neovim.lua
  vscode.json
  zed.json
  preview.png
  preview-unlock.png
  unlock.png

install.sh
```

Omarchy's `theme install` command clones one repository into one theme directory, so it cannot directly install two sibling variants from a single repository. A small `install.sh` script will copy both variant directories into `~/.config/omarchy/themes/` without changing the active theme. The script will stop rather than overwrite an existing variant unless the user explicitly passes its documented replacement option.

The root README will explain installation, manual copying, and switching between the installed variants. It will also credit the source palette and the Ayu Dark Omarchy repository used as a structural reference.

## Palette Mapping

`colors.toml` is the canonical color definition for each variant. Source UI roles will map to Omarchy roles by meaning rather than by blindly copying values:

- `background` becomes the main background.
- Popover or title-bar surfaces become darker/lighter background levels.
- `foreground` becomes the main foreground.
- Muted and tab text become dark/light foreground levels.
- `primary.background` or `ring` becomes the accent and active border.
- `selection.background` or a readable blend of the primary blue becomes selection.
- Source base colors populate terminal red, yellow, green, cyan, blue, and magenta.
- Orange and brown are derived from the closest syntax or warning colors when they are not explicitly defined.

The light theme will retain off-white surfaces, black text, neutral grays, and classic blue selection. The dark theme will retain near-black surfaces, cool gray text, and bright blue selection, with its source semantic colors preserved.

Where a source color lacks enough contrast in its new role, it may be adjusted minimally while keeping the same hue and visual character. Such adjustments will be documented in the README.

## Integrations

- Hyprland will use the primary blue for active and grouped active borders.
- btop will use the canonical semantic colors and surface hierarchy.
- Chromium will use the primary background color.
- Icon files will select a broadly available light/dark-compatible icon theme rather than introducing an icon dependency.
- VS Code and Zed metadata will select their official macOS Classic extensions and the correct light/dark variant names. Neovim will use a broadly available fallback because the upstream macOS Classic family does not provide a maintained Neovim theme.

Monaco is the intended monospace font. Because Omarchy manages fonts separately from themes and Monaco is proprietary, the repository will not bundle or automatically apply it. The installer will report whether Monaco is available, and the README will document `omarchy font set Monaco` plus Zed's `buffer_font_family` setting.

No configuration under `/usr/share/omarchy` or the user's `~/.config` directory will be modified. This repository will remain a distributable theme source.

## Visual Assets

Each theme will include a simple background based directly on its palette. The image will be either solid or use a very subtle tonal treatment, without logos, scenery, or generated artwork.

Preview, unlock, and preview-unlock images will be derived from the same background so the repository is self-contained and visually consistent. Assets will be generated at practical desktop dimensions and checked for correct format and dimensions.

## Validation

Validation will include:

- Parsing both `colors.toml` files.
- Parsing both `vscode.json` files and checking the Lua files for syntax when a Lua interpreter is available.
- Syntax-checking the installer and testing its copy behavior against a temporary home directory.
- Verifying that all required files exist in both variants.
- Confirming image formats and dimensions.
- Checking representative foreground/background and accent/background contrast ratios.
- Comparing the structure against current stock Omarchy themes.
- If supported without altering the active desktop, using the Omarchy CLI's read-only/help commands to confirm installation expectations.

The active user theme will not be changed as part of validation.

## Success Criteria

- One repository installation places both independently selectable variants in Omarchy's user theme directory.
- Both variants visibly reflect their corresponding source palette.
- Current Omarchy can consume the repository structure without relying on legacy-only files.
- The repository contains simple, coherent backgrounds and previews.
- Installation, switching, attribution, and compatibility limitations are documented.
