# macOS Classic Omarchy Theme Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and document independently selectable macOS Classic Light and Dark themes for current Omarchy.

**Architecture:** Store each variant as a complete Omarchy theme directory with `colors.toml` as its canonical palette. A root installer copies both directories into the user's Omarchy theme directory without activating either one; a repository-level test validates structure, syntax, images, contrast, and safe installer behavior.

**Tech Stack:** TOML, Lua, JSON, Bash, PNG assets, Python 3 standard library test harness.

## Global Constraints

- Preserve the visual roles from `/home/jason/work/gpui-component/themes/macos-classic.json` for both light and dark variants.
- Target the current Omarchy theme format visible in `/usr/share/omarchy/themes/`.
- Do not modify `/usr/share/omarchy`, `~/.config`, or the active desktop theme during implementation or validation.
- Keep backgrounds simple and palette-based, without logos, scenery, or generated artwork.
- The installer must not overwrite existing themes unless passed an explicit replacement option.

---

### Task 1: Validation Harness and Canonical Theme Palettes

**Files:**
- Create: `tests/test_theme.py`
- Create: `macos-classic-light/colors.toml`
- Create: `macos-classic-dark/colors.toml`

**Interfaces:**
- Consumes: Source GPUI palette and current Omarchy `colors.toml` field names.
- Produces: Two TOML palettes and a `unittest` harness reused by later tasks.

- [ ] **Step 1: Write failing structural and palette tests**

Create tests that load both TOML files with `tomllib`, require the complete stock Omarchy color-key set, assert `mode` is correct, assert source background/foreground/accent values are retained, and calculate WCAG contrast for primary foreground/background pairs.

- [ ] **Step 2: Run the tests and verify failure**

Run: `python -m unittest -v tests/test_theme.py`

Expected: FAIL because the theme directories and palettes do not exist.

- [ ] **Step 3: Add both canonical palettes**

Map background levels, foreground levels, semantic ANSI colors, selection, and accent to the exact Omarchy keys used by stock `colors.toml` files. Use `#0060de` as the light accent and `#077CFD` as the dark accent.

- [ ] **Step 4: Run the tests and verify success**

Run: `python -m unittest -v tests/test_theme.py`

Expected: all palette and contrast tests PASS.

- [ ] **Step 5: Commit**

```bash
git add tests/test_theme.py macos-classic-light/colors.toml macos-classic-dark/colors.toml
git commit -m "feat: add macOS Classic Omarchy palettes"
```

### Task 2: Omarchy Integration Files

**Files:**
- Create: `macos-classic-light/hyprland.lua`
- Create: `macos-classic-light/btop.theme`
- Create: `macos-classic-light/chromium.theme`
- Create: `macos-classic-light/icons.theme`
- Create: `macos-classic-light/neovim.lua`
- Create: `macos-classic-light/vscode.json`
- Create: `macos-classic-light/zed.json`
- Create: `macos-classic-dark/hyprland.lua`
- Create: `macos-classic-dark/btop.theme`
- Create: `macos-classic-dark/chromium.theme`
- Create: `macos-classic-dark/icons.theme`
- Create: `macos-classic-dark/neovim.lua`
- Create: `macos-classic-dark/vscode.json`
- Create: `macos-classic-dark/zed.json`
- Modify: `tests/test_theme.py`

**Interfaces:**
- Consumes: Exact palette values from each variant's `colors.toml`.
- Produces: Current Omarchy integration files for Hyprland, btop, Chromium, icons, Neovim, VS Code, and Zed metadata.

- [ ] **Step 1: Extend tests for required files and syntax**

Require every integration file, parse JSON, validate Chromium RGB triples, check Hyprland active-border mapping, inspect btop required keys, and run `luac -p` conditionally when `luac` exists.

- [ ] **Step 2: Run the tests and verify failure**

Run: `python -m unittest -v tests/test_theme.py`

Expected: FAIL listing missing integration files.

- [ ] **Step 3: Add integration files**

Use palette-consistent application colors. Configure active Hyprland borders from each accent, select `Adwaita` for light icons and `Adwaita-dark` for dark icons, use the official macOS Classic VS Code and Zed extension metadata, and retain a documented Neovim fallback.

- [ ] **Step 4: Run the tests and verify success**

Run: `python -m unittest -v tests/test_theme.py`

Expected: all integration tests PASS.

- [ ] **Step 5: Commit**

```bash
git add tests macos-classic-light macos-classic-dark
git commit -m "feat: add Omarchy application integrations"
```

### Task 3: Background and Preview Assets

**Files:**
- Create: `scripts/generate_assets.py`
- Create: `macos-classic-light/backgrounds/macos-classic-light.png`
- Create: `macos-classic-light/preview.png`
- Create: `macos-classic-light/preview-unlock.png`
- Create: `macos-classic-light/unlock.png`
- Create: `macos-classic-dark/backgrounds/macos-classic-dark.png`
- Create: `macos-classic-dark/preview.png`
- Create: `macos-classic-dark/preview-unlock.png`
- Create: `macos-classic-dark/unlock.png`
- Modify: `tests/test_theme.py`

**Interfaces:**
- Consumes: Background, surface, border, accent, and foreground colors from both palettes.
- Produces: Deterministic dependency-free PNG assets and a reproducible generator.

- [ ] **Step 1: Extend tests for PNG assets**

Validate the PNG signature and IHDR dimensions for every expected image, requiring desktop backgrounds and unlock images to be 1920×1080 and preview images to be 640×360.

- [ ] **Step 2: Run the tests and verify failure**

Run: `python -m unittest -v tests/test_theme.py`

Expected: FAIL listing missing PNG files.

- [ ] **Step 3: Implement deterministic asset generation**

Write a Python standard-library PNG encoder using `zlib` and `struct`. Render restrained vertical tonal backgrounds with a thin accent treatment, and derive matching preview/unlock images from the same palette.

- [ ] **Step 4: Generate and validate assets**

Run: `python scripts/generate_assets.py && python -m unittest -v tests/test_theme.py`

Expected: generation succeeds and all image tests PASS.

- [ ] **Step 5: Commit**

```bash
git add scripts tests macos-classic-light macos-classic-dark
git commit -m "feat: add macOS Classic theme artwork"
```

### Task 4: Safe Installer and Documentation

**Files:**
- Create: `install.sh`
- Create: `README.md`
- Modify: `tests/test_theme.py`

**Interfaces:**
- Consumes: The two complete theme directories.
- Produces: `./install.sh [--replace] [--destination DIR]` and user-facing installation/switching documentation.

- [ ] **Step 1: Extend tests for installer behavior**

Use a temporary destination to verify both variants copy successfully, a second run refuses overwrite, `--replace` replaces both variants, unknown arguments fail, and no active-theme command is invoked.

- [ ] **Step 2: Run the tests and verify failure**

Run: `python -m unittest -v tests/test_theme.py`

Expected: FAIL because `install.sh` is absent.

- [ ] **Step 3: Implement installer and README**

Implement strict Bash argument parsing, preflight both destinations before copying, report Monaco availability without modifying the global font, and document `./install.sh`, `omarchy theme set macos-classic-light`, `omarchy theme set macos-classic-dark`, `omarchy font set Monaco`, manual installation, palette attribution, compatibility, and editor integration.

- [ ] **Step 4: Validate installer and documentation**

Run: `bash -n install.sh && python -m unittest -v tests/test_theme.py`

Expected: shell syntax succeeds and all tests PASS.

- [ ] **Step 5: Commit**

```bash
git add install.sh README.md tests/test_theme.py
git commit -m "feat: package and document both theme variants"
```

### Task 5: Final Verification

**Files:**
- Modify only if verification exposes a defect.

**Interfaces:**
- Consumes: Entire finished repository.
- Produces: Evidence that all spec success criteria are met.

- [ ] **Step 1: Run automated verification**

Run: `python scripts/generate_assets.py && bash -n install.sh && python -m unittest -v tests/test_theme.py && git diff --check`

Expected: every command exits 0.

- [ ] **Step 2: Inspect repository completeness**

Run: `find macos-classic-light macos-classic-dark -maxdepth 2 -type f | sort`

Expected: both variants contain the same required file set and exactly one background each.

- [ ] **Step 3: Review changes and status**

Run: `git status --short && git diff --stat HEAD`

Expected: only intentional theme, test, script, and documentation files appear.

- [ ] **Step 4: Commit verification fixes if needed**

```bash
git add README.md install.sh scripts tests macos-classic-light macos-classic-dark
git commit -m "fix: resolve final theme validation issues"
```
