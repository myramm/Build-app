#!/usr/bin/env python3
"""
Build all branding & logo assets for Kunime Anime Streaming Web:
- SVGs (Symbol, App Icon, Horizontal Lockup, Stacked Lockup, Monochromes)
- High-res PNGs (512, 1024, 2048, 4096)
- Web & PWA Icon Kit (favicon.ico, apple-touch-icon, webmanifest, head snippet)
- Documentation & Brand Guidelines (brand-guide.md)
All outputs saved to result/logo/
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT / "result" / "logo"
SVG_DIR = OUTPUT_DIR / "svg"
PNG_DIR = OUTPUT_DIR / "png"
WEB_DIR = OUTPUT_DIR / "web"

for d in [SVG_DIR, PNG_DIR, WEB_DIR]:
    d.mkdir(parents=True, exist_ok=True)

SCRIPTS_LOGO = REPO_ROOT / "scripts" / "logo"

# 1. Colors & Definitions
COLOR_CRIMSON = "#FF2A5F"
COLOR_VERMILION = "#FF6B35"
COLOR_OBSIDIAN = "#090A10"
COLOR_WHITE = "#FFFFFF"
COLOR_MUTED = "#94A3B8"

print("==================================================")
print(" KUNIME BRAND ASSETS EXPORT GENERATOR")
print(" Output Target: result/logo/")
print("==================================================")

# Generate Base SVGs
BRANDING_DIR = REPO_ROOT / "branding"

# Run generate_branding.py first
subprocess.run([sys.executable, str(REPO_ROOT / "scripts" / "generate_branding.py")], check=True)

# Copy base masters to result/logo/svg
masters = {
    "kunime-symbol.svg": BRANDING_DIR / "kunime-symbol.svg",
    "kunime-app-icon.svg": BRANDING_DIR / "kunime-app-icon.svg",
    "kunime-horizontal.svg": BRANDING_DIR / "kunime-horizontal.svg",
    "kunime-horizontal-dark.svg": BRANDING_DIR / "kunime-horizontal-dark.svg",
    "kunime-horizontal-light.svg": BRANDING_DIR / "kunime-horizontal-light.svg",
    "kunime-stacked.svg": BRANDING_DIR / "kunime-stacked.svg",
    "kunime-stacked-dark.svg": BRANDING_DIR / "kunime-stacked-dark.svg",
}

for name, src in masters.items():
    dest = SVG_DIR / name
    shutil.copy2(src, dest)
    print(f"[SVG] Master saved: {dest.relative_to(REPO_ROOT)}")

# 2. Run export_variants.py for Monochromes, Square & Favicon
export_variants_script = SCRIPTS_LOGO / "export_variants.py"
print("\n--> Generating SVG Variants & Web Icons via export_variants.py...")
cmd_variants = [
    sys.executable,
    str(export_variants_script),
    str(SVG_DIR / "kunime-symbol.svg"),
    "--name", "kunime-symbol",
    "--title", "Kunime Anime Streaming Logo",
    "--mono", COLOR_CRIMSON,
    "--mono", COLOR_VERMILION,
    "--icon-bg", COLOR_OBSIDIAN,
    "--icon-fg", "keep",
    "--keep-white",
    "--web-icons",
    "--out-dir", str(SVG_DIR)
]
subprocess.run(cmd_variants, check=True)

# Move web-icons outputs (favicons, manifests, etc.) from SVG_DIR to WEB_DIR if generated there
for pattern in ["*.ico", "*favicon*.png", "apple-touch-icon.png", "icon-*.png", "maskable-*.png", "site.webmanifest", "head-snippet.html"]:
    for f in SVG_DIR.glob(pattern):
        dest = WEB_DIR / f.name
        shutil.move(str(f), str(dest))
        print(f"[WEB] Moved {f.name} -> {dest.relative_to(REPO_ROOT)}")

# Also copy web favicon to root if helpful
if (WEB_DIR / "favicon.ico").exists():
    shutil.copy2(WEB_DIR / "favicon.ico", OUTPUT_DIR / "favicon.ico")

# 3. High-Resolution PNG Exports via render_png.py
render_script = SCRIPTS_LOGO / "render_png.py"
print("\n--> Rendering High-Resolution PNGs...")

png_tasks = [
    # Symbol Transparent
    (SVG_DIR / "kunime-symbol.svg", PNG_DIR / "kunime-symbol-512.png", {"size": "512"}),
    (SVG_DIR / "kunime-symbol.svg", PNG_DIR / "kunime-symbol-1024.png", {"size": "1024"}),
    (SVG_DIR / "kunime-symbol.svg", PNG_DIR / "kunime-symbol-2048.png", {"size": "2048"}),
    (SVG_DIR / "kunime-symbol.svg", PNG_DIR / "kunime-symbol-4096.png", {"size": "4096"}),
    
    # App Icon with Tile
    (SVG_DIR / "kunime-app-icon.svg", PNG_DIR / "kunime-app-icon-512.png", {"size": "512"}),
    (SVG_DIR / "kunime-app-icon.svg", PNG_DIR / "kunime-app-icon-1024.png", {"size": "1024"}),
    (SVG_DIR / "kunime-app-icon.svg", PNG_DIR / "kunime-app-icon-2048.png", {"size": "2048"}),

    # Horizontal Lockup (Dark & Light)
    (SVG_DIR / "kunime-horizontal-dark.svg", PNG_DIR / "kunime-horizontal-dark-1200x360.png", {"width": "1200", "height": "360"}),
    (SVG_DIR / "kunime-horizontal-dark.svg", PNG_DIR / "kunime-horizontal-dark-2400x720.png", {"width": "2400", "height": "720"}),
    (SVG_DIR / "kunime-horizontal-light.svg", PNG_DIR / "kunime-horizontal-light-1200x360.png", {"width": "1200", "height": "360"}),
    (SVG_DIR / "kunime-horizontal-light.svg", PNG_DIR / "kunime-horizontal-light-2400x720.png", {"width": "2400", "height": "720"}),

    # Stacked Lockup (Dark)
    (SVG_DIR / "kunime-stacked-dark.svg", PNG_DIR / "kunime-stacked-dark-600x720.png", {"width": "600", "height": "720"}),
    (SVG_DIR / "kunime-stacked-dark.svg", PNG_DIR / "kunime-stacked-dark-1200x1440.png", {"width": "1200", "height": "1440"}),
]

for src_svg, dest_png, opts in png_tasks:
    args = [sys.executable, str(render_script), str(src_svg), "-o", str(dest_png)]
    if "size" in opts:
        args.extend(["--size", opts["size"]])
    if "width" in opts:
        args.extend(["--width", opts["width"]])
    if "height" in opts:
        args.extend(["--height", opts["height"]])
    
    print(f"Rendering: {dest_png.name}...")
    subprocess.run(args, check=True)

# 4. Generate Brand Guidelines Markdown
BRAND_GUIDE_MD = f"""# Kunime — Official Brand Identity & Design Guidelines

**Kunime** (クニメ) is a next-generation anime streaming platform featuring an ultra-fast, modern UI, curated Japanese animation streams, and immersive cinema viewing.

---

## 1. Concept: "Katana Play" (Symbol Concept A)
- **Geometry**: The iconic letter **'K'** constructed from an anchored Torii/Katana backbone (left pillar) crossed with dynamic **Katana strikes** at precise 45°/135° angles.
- **Embedded Media Iconography**: At the core of the diagonal blades lies a crisp, high-energy **Play Button** triangle, symbolizing direct instant-play streaming.
- **Visual Personality**: High-octane, Japanese animation aesthetic, sharp, aerodynamic, cyber-entertainment.

---

## 2. Color Palette

| Token | Hex Code | RGB | Role / Usage |
|---|---|---|---|
| **Cyber Crimson** | `{COLOR_CRIMSON}` | `rgb(255, 42, 95)` | Primary gradient start, key actions, live tags |
| **Neon Vermilion** | `{COLOR_VERMILION}` | `rgb(255, 107, 53)` | Primary gradient end, play accents, hover glows |
| **Cinema Obsidian** | `{COLOR_OBSIDIAN}` | `rgb(9, 10, 16)` | App icon canvas, dark mode web background |
| **Pure White** | `{COLOR_WHITE}` | `rgb(255, 255, 255)` | Katana backbone, primary wordmark, play core |
| **Muted Slate** | `{COLOR_MUTED}` | `rgb(148, 163, 184)` | Secondary taglines, subtitles, UI metadata |

---

## 3. Directory Structure of Deliverables (`result/logo/`)

```
result/logo/
├── favicon.ico                         # Root multi-resolution website favicon
├── brand-guide.md                      # This comprehensive guide
├── svg/                                # Scalable vector masters & variants
│   ├── kunime-symbol.svg               # Standalone mark (transparent)
│   ├── kunime-horizontal.svg           # Header lockup (Symbol + Wordmark + Tagline)
│   ├── kunime-stacked.svg              # Poster / splash lockup
│   ├── kunime-app-icon.svg             # Rounded squircle app icon
│   ├── kunime-symbol-black.svg         # 1-color black print variant
│   ├── kunime-symbol-white.svg         # 1-color white dark variant
│   ├── kunime-symbol-mono-ff2a5f.svg   # 1-color Cyber Crimson
│   ├── kunime-symbol-mono-ff6b35.svg   # 1-color Neon Vermilion
│   ├── kunime-symbol-square.svg        # 1:1 Social avatar (padded)
│   └── kunime-symbol-favicon.svg       # Tight browser favicon vector
├── png/                                # High-resolution raster graphics
│   ├── kunime-symbol-512.png / 1024.png / 2048.png / 4096.png
│   ├── kunime-app-icon-512.png / 1024.png / 2048.png
│   ├── kunime-horizontal-1200x360.png / 2400x720.png
│   └── kunime-stacked-600x720.png / 1200x1440.png
└── web/                                # Complete Web & PWA Icon Kit
    ├── favicon.ico                     # 16x16, 32x32, 48x48 icon
    ├── favicon-16x16.png
    ├── favicon-32x32.png
    ├── apple-touch-icon.png            # 180x180 iOS home icon
    ├── icon-192.png / icon-512.png     # Android PWA launcher icons
    ├── maskable-512.png                # Adaptive Android icon
    ├── site.webmanifest                # Web App Manifest
    └── head-snippet.html               # Copy-paste HTML header tags
```

---

## 4. Typography
- **Wordmark**: `Space Grotesk` (Weight: 900 Black, Letter-spacing: +8px)
- **Tagline**: `Space Grotesk` / `Inter` (Weight: 700 Bold, Letter-spacing: +6px to +8px)
- **Japanese Kanji/Katakana**: `Noto Sans JP` / `Hiragino Sans` (`クニメ`)

---

## 5. Web Implementation Quickstart

Insert into your HTML `<head>`:
```html
<link rel="icon" href="/logo/web/favicon.ico" sizes="any">
<link rel="icon" href="/logo/web/favicon-32x32.png" type="image/png">
<link rel="apple-touch-icon" href="/logo/web/apple-touch-icon.png">
<link rel="manifest" href="/logo/web/site.webmanifest">
```
"""

(OUTPUT_DIR / "brand-guide.md").write_text(BRAND_GUIDE_MD, encoding="utf-8")
print("\n[OK] Brand guide written to result/logo/brand-guide.md")
print("\nAll assets successfully generated in result/logo/!")
