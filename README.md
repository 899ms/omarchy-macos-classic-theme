# macOS Classic for Omarchy

Two Omarchy themes based on Jason Lee's macOS Classic palettes:

- `macos-classic-light` — off-white surfaces, black text, and classic blue accents
- `macos-classic-dark` — near-black surfaces, cool gray text, and bright blue accents

The repository targets the current `colors.toml`-based Omarchy theme format. It includes matching Hyprland, btop, Chromium, icon, Neovim, VS Code, and Zed metadata plus simple palette-based backgrounds.

## Install

Clone the repository and run:

```bash
./install.sh
```

This installs both variants under `~/.config/omarchy/themes/` without changing the active theme. Existing installations are preserved. To intentionally replace both:

```bash
./install.sh --replace
```

For a custom location or a temporary test:

```bash
./install.sh --destination /path/to/themes
```

You can also manually copy `macos-classic-light` and `macos-classic-dark` into `~/.config/omarchy/themes/`.

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

The installer reports whether Fontconfig can find Monaco. Until it is installed, your existing Omarchy font remains unchanged.

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

Current Omarchy theme switching does not apply Zed metadata automatically; the included `zed.json` files record the correct upstream extension and variant names.

### Neovim

There is no maintained native macOS Classic Neovim theme in the upstream family. The light and dark variants therefore use Catppuccin Latte and Mocha as dependable LazyVim fallbacks.

## Palette and assets

The palette is mapped from [`gpui-component`'s macOS Classic theme](https://github.com/longbridge/gpui-component), which credits [`huacnlee/zed-theme-macos-classic`](https://github.com/huacnlee/zed-theme-macos-classic). The warning-derived orange and brown roles and the light selection fill are the only added role colors.

Backgrounds are intentionally restrained vertical tonal fields with a thin blue accent. Regenerate every PNG deterministically with:

```bash
python scripts/generate_assets.py
```

## Verify

```bash
bash -n install.sh
python -m unittest -v tests/test_theme.py
```

The theme structure follows current stock Omarchy themes. The older [Ayu Dark Omarchy theme](https://github.com/fdidron/omarchy-ayu-dark-theme) was used as an additional packaging reference.

## License

See [LICENSE](LICENSE). Upstream themes and editor extensions retain their respective licenses.
