# macOS Classic for Omarchy

An Omarchy theme based on Jason Lee's macOS Classic palette — near-black surfaces, cool gray text, and bright blue accents. Includes application colors and a matching background.

<img width="3840" height="2160" alt="screenshot-2026-08-16_16-53-45" src="https://github.com/user-attachments/assets/828e801b-2a15-4220-ad6d-b46f565a65d6" />

## Install

```bash
omarchy theme install https://github.com/huacnlee/omarchy-macos-classic-theme
```

This installs the theme as `macos-classic` and applies it right away. Pick it up again later with `omarchy theme set macos-classic`, and pull in updates with `omarchy theme update`.

The palette is designed for Monaco. Once a licensed copy is installed, apply it with `omarchy font set Monaco`.

### Light variant

A light variant lives in [`macos-classic-light/`](macos-classic-light). It is less polished than the dark theme, and `omarchy theme install` cannot reach it — omarchy builds exactly one theme per repository, from the files at the top level. Install it by hand:

```bash
git clone https://github.com/huacnlee/omarchy-macos-classic-theme
cd omarchy-macos-classic-theme
./install.sh
omarchy theme set macos-classic-light
```

`install.sh` installs both variants and activates neither.

## Credits

Based on [`huacnlee/zed-theme-macos-classic`](https://github.com/huacnlee/zed-theme-macos-classic) and the matching [VS Code theme](https://marketplace.visualstudio.com/items?itemName=huacnlee.theme-macos-classic).

## License

See [LICENSE](LICENSE).
