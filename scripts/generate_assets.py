#!/usr/bin/env python3
"""Generate deterministic, dependency-free PNG assets for both theme variants."""

import binascii
import struct
import zlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
THEMES = {
    "macos-classic-light": {
        "top": "#FFFFFF",
        "bottom": "#E9E9E9",
        "accent": "#0060DE",
    },
    "macos-classic-dark": {
        "top": "#202020",
        "bottom": "#0B0B0B",
        "accent": "#077CFD",
    },
}


def rgb(value):
    value = value.removeprefix("#")
    return tuple(int(value[index : index + 2], 16) for index in (0, 2, 4))


def chunk(kind, payload):
    return struct.pack(">I", len(payload)) + kind + payload + struct.pack(">I", binascii.crc32(kind + payload))


def render_png(path, width, height, colors):
    top, bottom, accent = (rgb(colors[key]) for key in ("top", "bottom", "accent"))
    rows = []
    accent_height = max(2, height // 180)

    for y in range(height):
        if y < accent_height:
            pixel = accent
        else:
            position = (y - accent_height) / max(1, height - accent_height - 1)
            pixel = tuple(round(start + (end - start) * position) for start, end in zip(top, bottom))
        rows.append(b"\x00" + bytes(pixel) * width)

    header = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    payload = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header)
    payload += chunk(b"IDAT", zlib.compress(b"".join(rows), level=9))
    payload += chunk(b"IEND", b"")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)


def main():
    for name, colors in THEMES.items():
        theme = ROOT / name
        render_png(theme / "backgrounds" / f"{name}.png", 1920, 1080, colors)
        render_png(theme / "unlock.png", 1920, 1080, colors)
        render_png(theme / "preview.png", 640, 360, colors)
        render_png(theme / "preview-unlock.png", 640, 360, colors)


if __name__ == "__main__":
    main()
