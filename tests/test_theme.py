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
    },
    "macos-classic-dark": {
        "mode": "dark",
        "background": "#131313",
        "foreground": "#DEDEDE",
        "accent": "#077CFD",
        "chromium": "19,19,19",
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


if __name__ == "__main__":
    unittest.main()
