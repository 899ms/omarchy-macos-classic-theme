# macOS Classic for Omarchy

Two Omarchy themes based on Jason Lee's macOS Classic palettes:

- `macos-classic-light` — off-white surfaces, black text, and classic blue accents
- `macos-classic-dark` — near-black surfaces, cool gray text, and bright blue accents

Includes matching light and dark palettes, application colors, and simple backgrounds.

## Install

### Quick install

Copy and run this block to install or update both variants:

```bash
(
  install_tmp=$(mktemp -d)
  trap 'rm -rf "$install_tmp"' EXIT
  git clone --depth 1 https://github.com/huacnlee/omarchy-macos-classic-theme.git "$install_tmp/theme"
  "$install_tmp/theme/install.sh"
)
```

Then select a variant:

```bash
omarchy theme set macos-classic-light
# or
omarchy theme set macos-classic-dark
```

### Manual install

Clone the repository and run its installer:

```bash
git clone https://github.com/huacnlee/omarchy-macos-classic-theme.git
cd omarchy-macos-classic-theme
./install.sh
```

This installs both variants under `~/.config/omarchy/themes/` without changing the active theme. Existing installations are updated automatically.

## Use

```bash
omarchy theme set macos-classic-light
omarchy theme set macos-classic-dark
```

## Monaco font

Monaco is the intended monospace companion for this theme. Omarchy manages fonts separately from themes, so switching themes cannot automatically switch the font.

Monaco is proprietary and is not bundled here. After installing a licensed copy on your system, apply it with:

```bash
omarchy font set Monaco
```

The installer reports whether Monaco is available. Until it is installed, your existing Omarchy font remains unchanged.

## Editors

### VS Code

Omarchy uses the official [`huacnlee.theme-macos-classic`](https://marketplace.visualstudio.com/items?itemName=huacnlee.theme-macos-classic) extension metadata:

- Light: `macOS Classic`
- Dark: `macOS Classic Dark v2`

The upstream extension recommends `Menlo, Monaco, Consolas, 'Courier New', monospace` as the editor font stack.

### Zed

Install the official [macOS Classic Zed extension](https://zed.dev/extensions/macos-classic), then configure automatic switching in `~/.config/zed/settings.json`:

```json
{
  "theme": {
    "mode": "system",
    "light": "macOS Classic Light",
    "dark": "macOS Classic Dark"
  },
  "buffer_font_family": "Monaco"
}
```

Current Omarchy does not automatically switch Zed themes, so configure Zed once using the settings above.

## Credits

Based on [`huacnlee/zed-theme-macos-classic`](https://github.com/huacnlee/zed-theme-macos-classic) and the matching [VS Code theme](https://marketplace.visualstudio.com/items?itemName=huacnlee.theme-macos-classic).

## License

See [LICENSE](LICENSE).
