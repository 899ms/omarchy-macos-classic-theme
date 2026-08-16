import colorsys
import json
import shutil
import struct
import subprocess
import tempfile
import tomllib
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VARIANTS = {
    "macos-classic-light": {
        "mode": "light",
        "background": "#F9F9F9",
        "foreground": "#000000",
        "accent": "#0060de",
        "chromium": "249,249,249",
        "vscode": "macOS Classic",
        "zed": "macOS Classic Light",
    },
    "macos-classic-dark": {
        "mode": "dark",
        "background": "#131313",
        "foreground": "#DEDEDE",
        "accent": "#077CFD",
        "chromium": "19,19,19",
        "vscode": "macOS Classic Dark v2",
        "zed": "macOS Classic Dark",
    },
}

COLOR_KEYS = {
    "mode",
    "accent",
    "selection",
    "muted",
    "background",
    "dark_background",
    "darker_background",
    "lighter_background",
    "foreground",
    "dark_foreground",
    "light_foreground",
    "bright_foreground",
    "red",
    "yellow",
    "orange",
    "green",
    "cyan",
    "blue",
    "magenta",
    "brown",
    "bright_red",
    "bright_yellow",
    "bright_green",
    "bright_cyan",
    "bright_blue",
    "bright_magenta",
}


def load_palette(name):
    with (ROOT / name / "colors.toml").open("rb") as handle:
        return tomllib.load(handle)


def relative_luminance(hex_color):
    channels = [int(hex_color[index : index + 2], 16) / 255 for index in (1, 3, 5)]
    linear = [value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4 for value in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast_ratio(first, second):
    high, low = sorted((relative_luminance(first), relative_luminance(second)), reverse=True)
    return (high + 0.05) / (low + 0.05)


class PaletteTests(unittest.TestCase):
    def test_palettes_have_all_current_omarchy_keys(self):
        for name in VARIANTS:
            with self.subTest(name=name):
                self.assertEqual(COLOR_KEYS, set(load_palette(name)))

    def test_palettes_preserve_source_identity_colors(self):
        for name, expected in VARIANTS.items():
            with self.subTest(name=name):
                palette = load_palette(name)
                self.assertEqual(expected["mode"], palette["mode"])
                self.assertEqual(expected["background"].lower(), palette["background"].lower())
                self.assertEqual(expected["foreground"].lower(), palette["foreground"].lower())
                self.assertEqual(expected["accent"].lower(), palette["accent"].lower())

    def test_primary_text_contrast_meets_wcag_aa(self):
        for name in VARIANTS:
            with self.subTest(name=name):
                palette = load_palette(name)
                self.assertGreaterEqual(contrast_ratio(palette["foreground"], palette["background"]), 4.5)


class IntegrationTests(unittest.TestCase):
    REQUIRED_FILES = {
        "hyprland.lua",
        "btop.theme",
        "chromium.theme",
        "icons.theme",
        "neovim.lua",
        "vscode.json",
        "zed.json",
    }

    def test_all_integration_files_exist(self):
        for name in VARIANTS:
            for filename in self.REQUIRED_FILES:
                with self.subTest(name=name, filename=filename):
                    self.assertTrue((ROOT / name / filename).is_file())

    def test_chromium_uses_source_background(self):
        for name, expected in VARIANTS.items():
            with self.subTest(name=name):
                value = (ROOT / name / "chromium.theme").read_text().strip()
                self.assertEqual(expected["chromium"], value)
                self.assertTrue(all(0 <= int(channel) <= 255 for channel in value.split(",")))

    def test_hyprland_uses_accent_for_active_borders(self):
        for name, expected in VARIANTS.items():
            with self.subTest(name=name):
                content = (ROOT / name / "hyprland.lua").read_text()
                accent = expected["accent"].removeprefix("#").lower()
                self.assertIn(f'local active_border_color = "rgb({accent})"', content.lower())
                self.assertIn("border_active = active_border_color", content)

    def test_btop_defines_all_required_theme_fields(self):
        required = {
            "main_bg", "main_fg", "title", "hi_fg", "selected_bg", "selected_fg",
            "inactive_fg", "proc_misc", "cpu_box", "mem_box", "net_box", "proc_box",
            "div_line", "temp_start", "temp_mid", "temp_end", "cpu_start", "cpu_mid",
            "cpu_end", "free_start", "free_mid", "free_end", "cached_start", "cached_mid",
            "cached_end", "available_start", "available_mid", "available_end", "used_start",
            "used_mid", "used_end", "download_start", "download_mid", "download_end",
            "upload_start", "upload_mid", "upload_end",
        }
        for name in VARIANTS:
            with self.subTest(name=name):
                content = (ROOT / name / "btop.theme").read_text()
                present = {
                    line.split("]", 1)[0].removeprefix("theme[")
                    for line in content.splitlines()
                    if line.startswith("theme[")
                }
                self.assertEqual(required, present)

    def test_editor_metadata_is_valid(self):
        for name, expected in VARIANTS.items():
            with self.subTest(name=name):
                metadata = json.loads((ROOT / name / "vscode.json").read_text())
                self.assertEqual({"name", "extension"}, set(metadata))
                self.assertEqual(expected["vscode"], metadata["name"])
                self.assertEqual("huacnlee.theme-macos-classic", metadata["extension"])

                zed = json.loads((ROOT / name / "zed.json").read_text())
                self.assertEqual(
                    {
                        "extension": "macos-classic",
                        "name": expected["zed"],
                    },
                    zed,
                )

    @unittest.skipUnless(shutil.which("luac"), "luac is not installed")
    def test_lua_files_parse(self):
        for name in VARIANTS:
            for filename in ("hyprland.lua", "neovim.lua"):
                with self.subTest(name=name, filename=filename):
                    result = subprocess.run(
                        ["luac", "-p", ROOT / name / filename],
                        capture_output=True,
                        text=True,
                    )
                    self.assertEqual(0, result.returncode, result.stderr)


class AssetTests(unittest.TestCase):
    def png_dimensions(self, path):
        data = path.read_bytes()
        self.assertEqual(b"\x89PNG\r\n\x1a\n", data[:8])
        self.assertEqual(b"IHDR", data[12:16])
        return struct.unpack(">II", data[16:24])

    def test_assets_have_expected_png_dimensions(self):
        for name in VARIANTS:
            expected = {
                ROOT / name / "backgrounds" / f"{name}.png": (1920, 1080),
                ROOT / name / "unlock.png": (1920, 1080),
                ROOT / name / "preview.png": (640, 360),
                ROOT / name / "preview-unlock.png": (640, 360),
            }
            for path, dimensions in expected.items():
                with self.subTest(path=path):
                    self.assertEqual(dimensions, self.png_dimensions(path))


if __name__ == "__main__":
    unittest.main()
