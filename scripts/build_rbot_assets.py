#!/usr/bin/env python3
"""
Complete brand asset builder for R-BOT WhatsApp (Established 2021):
- Refined Master SVGs (Symbol, App Icon, Horizontal Dark/Light, Stacked)
- SVG Variants (Monochromes, Favicon, Square Avatar)
- High-res PNG Exports (512px to 4K)
- Complete Web & PWA Icon Kit
- Brand Guidelines (brand-guide.md)
Target Output: result/logo/r-bot/
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT / "result" / "logo" / "r-bot"
SVG_DIR = OUTPUT_DIR / "svg"
PNG_DIR = OUTPUT_DIR / "png"
WEB_DIR = OUTPUT_DIR / "web"

for d in [SVG_DIR, PNG_DIR, WEB_DIR]:
    d.mkdir(parents=True, exist_ok=True)

SCRIPTS_LOGO = REPO_ROOT / "scripts" / "logo"

# Primary Colors
COLOR_WA_GREEN = "#25D366"  # WhatsApp Emerald
COLOR_CYAN = "#00F2FE"      # Cyber Mint
COLOR_DARK = "#0B141A"      # WhatsApp Dark
COLOR_SLATE = "#111B21"     # WhatsApp Card Background
COLOR_WHITE = "#FFFFFF"
COLOR_MUTED = "#94A3B8"

print("==================================================")
print(" R-BOT WHATSAPP BRAND ASSETS EXPORT GENERATOR")
print(" Output Target: result/logo/r-bot/")
print("==================================================")

# 1. Standalone Master Symbol (Transparent background, mathematically snapped angles)
SYMBOL_SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <title>R-BOT WhatsApp Symbol</title>
  <defs>
    <linearGradient id="rbot-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{COLOR_WA_GREEN}" />
      <stop offset="100%" stop-color="{COLOR_CYAN}" />
    </linearGradient>
  </defs>

  <!-- Outer Chat Speech Bubble Silhouette -->
  <path d="M 256,64 C 150,64 64,150 64,256 C 64,294 74,330 94,360 L 72,428 C 70,436 78,444 86,442 L 154,420 C 184,438 218,448 256,448 C 362,448 448,362 448,256 C 448,150 362,64 256,64 Z" 
        fill="none" stroke="url(#rbot-grad)" stroke-width="22" stroke-linecap="round" stroke-linejoin="round" />

  <!-- Robot 'R' Monogram -->
  <g transform="translate(16, -4)">
    <!-- Vertical Pillar -->
    <rect x="170" y="156" width="40" height="188" rx="14" fill="{COLOR_WHITE}" />

    <!-- Upper Loop with Robot Head Arc -->
    <path d="M 210,156 L 276,156 C 318,156 346,184 346,222 C 346,260 318,288 276,288 L 210,288 Z" 
          fill="none" stroke="url(#rbot-grad)" stroke-width="36" stroke-linecap="round" stroke-linejoin="round" />

    <!-- Robot Glowing Visor Eye Lens (Clear geometric element) -->
    <rect x="232" y="206" width="60" height="32" rx="16" fill="{COLOR_CYAN}" />
    <circle cx="250" cy="222" r="6" fill="{COLOR_DARK}" />
    <circle cx="274" cy="222" r="6" fill="{COLOR_DARK}" />

    <!-- Dynamic 45° Diagonal Leg -->
    <path d="M 240,264 L 326,350 C 332,356 344,356 350,350 L 358,342 C 364,336 364,324 358,318 L 274,234 Z" 
          fill="url(#rbot-grad)" />
  </g>
</svg>
"""

# 2. Master App Icon (Deep WhatsApp Dark Canvas with glow)
APP_ICON_SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <title>R-BOT WhatsApp App Icon</title>
  <defs>
    <linearGradient id="rbot-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{COLOR_WA_GREEN}" />
      <stop offset="100%" stop-color="{COLOR_CYAN}" />
    </linearGradient>
    <filter id="rbot-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="20" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- WhatsApp Obsidian Canvas -->
  <rect width="512" height="512" rx="112" fill="{COLOR_DARK}" />

  <!-- Ambient Glow -->
  <circle cx="256" cy="256" r="140" fill="{COLOR_WA_GREEN}" opacity="0.12" filter="url(#rbot-glow)" />

  <!-- Outer Chat Speech Bubble -->
  <path d="M 256,64 C 150,64 64,150 64,256 C 64,294 74,330 94,360 L 72,428 C 70,436 78,444 86,442 L 154,420 C 184,438 218,448 256,448 C 362,448 448,362 448,256 C 448,150 362,64 256,64 Z" 
        fill="none" stroke="url(#rbot-grad)" stroke-width="22" stroke-linecap="round" stroke-linejoin="round" />

  <!-- Central 'R' Monogram -->
  <g transform="translate(16, -4)">
    <rect x="170" y="156" width="40" height="188" rx="14" fill="{COLOR_WHITE}" />
    <path d="M 210,156 L 276,156 C 318,156 346,184 346,222 C 346,260 318,288 276,288 L 210,288 Z" 
          fill="none" stroke="url(#rbot-grad)" stroke-width="36" stroke-linecap="round" stroke-linejoin="round" />
    <rect x="232" y="206" width="60" height="32" rx="16" fill="{COLOR_CYAN}" />
    <circle cx="250" cy="222" r="6" fill="{COLOR_DARK}" />
    <circle cx="274" cy="222" r="6" fill="{COLOR_DARK}" />
    <path d="M 240,264 L 326,350 C 332,356 344,356 350,350 L 358,342 C 364,336 364,324 358,318 L 274,234 Z" 
          fill="url(#rbot-grad)" />
  </g>
</svg>
"""

# 3. Master Horizontal Lockup - Dark Mode (1200 x 360)
HORIZONTAL_DARK_SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 360" width="100%" height="100%">
  <title>R-BOT Horizontal Brand Lockup (Dark)</title>
  <defs>
    <linearGradient id="rbot-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{COLOR_WA_GREEN}" />
      <stop offset="100%" stop-color="{COLOR_CYAN}" />
    </linearGradient>
    <linearGradient id="text-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="85%" stop-color="#E2E8F0" />
      <stop offset="100%" stop-color="{COLOR_WA_GREEN}" />
    </linearGradient>
  </defs>

  <!-- Deep WhatsApp Canvas -->
  <rect width="1200" height="360" rx="36" fill="{COLOR_DARK}" />

  <!-- Symbol Left Scale (0.68x) -->
  <g transform="translate(60, 42) scale(0.68)">
    <path d="M 256,64 C 150,64 64,150 64,256 C 64,294 74,330 94,360 L 72,428 C 70,436 78,444 86,442 L 154,420 C 184,438 218,448 256,448 C 362,448 448,362 448,256 C 448,150 362,64 256,64 Z" 
          fill="none" stroke="url(#rbot-grad)" stroke-width="26" stroke-linecap="round" stroke-linejoin="round" />
    <g transform="translate(16, -4)">
      <rect x="170" y="156" width="40" height="188" rx="14" fill="{COLOR_WHITE}" />
      <path d="M 210,156 L 276,156 C 318,156 346,184 346,222 C 346,260 318,288 276,288 L 210,288 Z" 
            fill="none" stroke="url(#rbot-grad)" stroke-width="36" stroke-linecap="round" stroke-linejoin="round" />
      <rect x="232" y="206" width="60" height="32" rx="16" fill="{COLOR_CYAN}" />
      <circle cx="250" cy="222" r="6" fill="{COLOR_DARK}" />
      <circle cx="274" cy="222" r="6" fill="{COLOR_DARK}" />
      <path d="M 240,264 L 326,350 C 332,356 344,356 350,350 L 358,342 C 364,336 364,324 358,318 L 274,234 Z" 
            fill="url(#rbot-grad)" />
    </g>
  </g>

  <!-- Typography: R-BOT Wordmark -->
  <g transform="translate(380, 205)">
    <text font-family="'Space Grotesk', 'DejaVu Sans', sans-serif" font-size="124" font-weight="900" letter-spacing="8" fill="url(#text-grad)">R-BOT</text>
  </g>

  <!-- Tagline + Heritage 2021 -->
  <g transform="translate(385, 260)">
    <rect x="0" y="-18" width="8" height="22" rx="4" fill="{COLOR_WA_GREEN}" />
    <text x="20" y="0" font-family="'Space Grotesk', 'DejaVu Sans', sans-serif" font-size="20" font-weight="800" letter-spacing="6" fill="{COLOR_MUTED}">WHATSAPP AUTOMATION <tspan fill="{COLOR_WA_GREEN}">• EST. 2021</tspan></text>
  </g>
</svg>
"""

# 4. Master Horizontal Lockup - Light Mode (1200 x 360)
HORIZONTAL_LIGHT_SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 360" width="100%" height="100%">
  <title>R-BOT Horizontal Brand Lockup (Light)</title>
  <defs>
    <linearGradient id="rbot-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{COLOR_WA_GREEN}" />
      <stop offset="100%" stop-color="#0284C7" />
    </linearGradient>
  </defs>

  <!-- Symbol Left Scale (0.68x) -->
  <g transform="translate(60, 42) scale(0.68)">
    <path d="M 256,64 C 150,64 64,150 64,256 C 64,294 74,330 94,360 L 72,428 C 70,436 78,444 86,442 L 154,420 C 184,438 218,448 256,448 C 362,448 448,362 448,256 C 448,150 362,64 256,64 Z" 
          fill="none" stroke="url(#rbot-grad)" stroke-width="26" stroke-linecap="round" stroke-linejoin="round" />
    <g transform="translate(16, -4)">
      <rect x="170" y="156" width="40" height="188" rx="14" fill="{COLOR_DARK}" />
      <path d="M 210,156 L 276,156 C 318,156 346,184 346,222 C 346,260 318,288 276,288 L 210,288 Z" 
            fill="none" stroke="url(#rbot-grad)" stroke-width="36" stroke-linecap="round" stroke-linejoin="round" />
      <rect x="232" y="206" width="60" height="32" rx="16" fill="{COLOR_WA_GREEN}" />
      <circle cx="250" cy="222" r="6" fill="#FFFFFF" />
      <circle cx="274" cy="222" r="6" fill="#FFFFFF" />
      <path d="M 240,264 L 326,350 C 332,356 344,356 350,350 L 358,342 C 364,336 364,324 358,318 L 274,234 Z" 
            fill="url(#rbot-grad)" />
    </g>
  </g>

  <!-- Typography: R-BOT Wordmark in deep charcoal -->
  <g transform="translate(380, 205)">
    <text font-family="'Space Grotesk', 'DejaVu Sans', sans-serif" font-size="124" font-weight="900" letter-spacing="8" fill="{COLOR_DARK}">R-BOT</text>
  </g>

  <!-- Tagline + Heritage 2021 -->
  <g transform="translate(385, 260)">
    <rect x="0" y="-18" width="8" height="22" rx="4" fill="{COLOR_WA_GREEN}" />
    <text x="20" y="0" font-family="'Space Grotesk', 'DejaVu Sans', sans-serif" font-size="20" font-weight="800" letter-spacing="6" fill="#475569">WHATSAPP AUTOMATION <tspan fill="{COLOR_WA_GREEN}">• EST. 2021</tspan></text>
  </g>
</svg>
"""

# 5. Master Stacked Lockup - Dark Mode (600 x 720)
STACKED_DARK_SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 720" width="100%" height="100%">
  <title>R-BOT Stacked Brand Lockup (Dark)</title>
  <defs>
    <linearGradient id="rbot-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{COLOR_WA_GREEN}" />
      <stop offset="100%" stop-color="{COLOR_CYAN}" />
    </linearGradient>
  </defs>

  <!-- Deep Canvas -->
  <rect width="600" height="720" rx="48" fill="{COLOR_DARK}" />

  <!-- Symbol Centered Top (0.75x) -->
  <g transform="translate(108, 40) scale(0.75)">
    <path d="M 256,64 C 150,64 64,150 64,256 C 64,294 74,330 94,360 L 72,428 C 70,436 78,444 86,442 L 154,420 C 184,438 218,448 256,448 C 362,448 448,362 448,256 C 448,150 362,64 256,64 Z" 
          fill="none" stroke="url(#rbot-grad)" stroke-width="26" stroke-linecap="round" stroke-linejoin="round" />
    <g transform="translate(16, -4)">
      <rect x="170" y="156" width="40" height="188" rx="14" fill="{COLOR_WHITE}" />
      <path d="M 210,156 L 276,156 C 318,156 346,184 346,222 C 346,260 318,288 276,288 L 210,288 Z" 
            fill="none" stroke="url(#rbot-grad)" stroke-width="36" stroke-linecap="round" stroke-linejoin="round" />
      <rect x="232" y="206" width="60" height="32" rx="16" fill="{COLOR_CYAN}" />
      <circle cx="250" cy="222" r="6" fill="{COLOR_DARK}" />
      <circle cx="274" cy="222" r="6" fill="{COLOR_DARK}" />
      <path d="M 240,264 L 326,350 C 332,356 344,356 350,350 L 358,342 C 364,336 364,324 358,318 L 274,234 Z" 
            fill="url(#rbot-grad)" />
    </g>
  </g>

  <!-- Wordmark Centered -->
  <g transform="translate(300, 480)" text-anchor="middle">
    <text font-family="'Space Grotesk', 'DejaVu Sans', sans-serif" font-size="108" font-weight="900" letter-spacing="10" fill="{COLOR_WHITE}">R-BOT</text>
  </g>

  <!-- Tagline Centered -->
  <g transform="translate(300, 545)" text-anchor="middle">
    <text font-family="'Space Grotesk', 'DejaVu Sans', sans-serif" font-size="20" font-weight="800" letter-spacing="6" fill="{COLOR_MUTED}">WHATSAPP BOT <tspan fill="{COLOR_WA_GREEN}">• EST. 2021</tspan></text>
  </g>
</svg>
"""

# Write base SVGs to result/logo/r-bot/svg
(SVG_DIR / "rbot-symbol.svg").write_text(SYMBOL_SVG, encoding="utf-8")
(SVG_DIR / "rbot-app-icon.svg").write_text(APP_ICON_SVG, encoding="utf-8")
(SVG_DIR / "rbot-horizontal-dark.svg").write_text(HORIZONTAL_DARK_SVG, encoding="utf-8")
(SVG_DIR / "rbot-horizontal-light.svg").write_text(HORIZONTAL_LIGHT_SVG, encoding="utf-8")
(SVG_DIR / "rbot-stacked-dark.svg").write_text(STACKED_DARK_SVG, encoding="utf-8")

print("[SVG] Master files written to result/logo/r-bot/svg")

# 2. Run export_variants.py for Monochromes, Square & Web Icons
export_variants_script = SCRIPTS_LOGO / "export_variants.py"
print("\n--> Generating SVG Variants & Web Icons via export_variants.py...")
cmd_variants = [
    sys.executable,
    str(export_variants_script),
    str(SVG_DIR / "rbot-symbol.svg"),
    "--name", "rbot-symbol",
    "--title", "R-BOT WhatsApp Automation Logo",
    "--mono", COLOR_WA_GREEN,
    "--mono", COLOR_CYAN,
    "--icon-bg", COLOR_DARK,
    "--icon-fg", "keep",
    "--keep-white",
    "--web-icons",
    "--out-dir", str(SVG_DIR)
]
subprocess.run(cmd_variants, check=True)

# Move web-icons outputs (favicons, manifests, etc.) from SVG_DIR to WEB_DIR
for pattern in ["*.ico", "*favicon*.png", "apple-touch-icon.png", "icon-*.png", "maskable-*.png", "site.webmanifest", "head-snippet.html"]:
    for f in SVG_DIR.glob(pattern):
        dest = WEB_DIR / f.name
        shutil.move(str(f), str(dest))
        print(f"[WEB] Moved {f.name} -> {dest.relative_to(REPO_ROOT)}")

if (WEB_DIR / "favicon.ico").exists():
    shutil.copy2(WEB_DIR / "favicon.ico", OUTPUT_DIR / "favicon.ico")

# 3. High-Resolution PNG Exports via render_png.py
render_script = SCRIPTS_LOGO / "render_png.py"
print("\n--> Rendering High-Resolution PNGs...")

png_tasks = [
    # Symbol Transparent
    (SVG_DIR / "rbot-symbol.svg", PNG_DIR / "rbot-symbol-512.png", {"size": "512"}),
    (SVG_DIR / "rbot-symbol.svg", PNG_DIR / "rbot-symbol-1024.png", {"size": "1024"}),
    (SVG_DIR / "rbot-symbol.svg", PNG_DIR / "rbot-symbol-2048.png", {"size": "2048"}),
    (SVG_DIR / "rbot-symbol.svg", PNG_DIR / "rbot-symbol-4096.png", {"size": "4096"}),
    
    # App Icon with WhatsApp Dark Tile
    (SVG_DIR / "rbot-app-icon.svg", PNG_DIR / "rbot-app-icon-512.png", {"size": "512"}),
    (SVG_DIR / "rbot-app-icon.svg", PNG_DIR / "rbot-app-icon-1024.png", {"size": "1024"}),
    (SVG_DIR / "rbot-app-icon.svg", PNG_DIR / "rbot-app-icon-2048.png", {"size": "2048"}),

    # Horizontal Lockup (Dark & Light)
    (SVG_DIR / "rbot-horizontal-dark.svg", PNG_DIR / "rbot-horizontal-dark-1200x360.png", {"width": "1200", "height": "360"}),
    (SVG_DIR / "rbot-horizontal-dark.svg", PNG_DIR / "rbot-horizontal-dark-2400x720.png", {"width": "2400", "height": "720"}),
    (SVG_DIR / "rbot-horizontal-light.svg", PNG_DIR / "rbot-horizontal-light-1200x360.png", {"width": "1200", "height": "360"}),
    (SVG_DIR / "rbot-horizontal-light.svg", PNG_DIR / "rbot-horizontal-light-2400x720.png", {"width": "2400", "height": "720"}),

    # Stacked Lockup (Dark)
    (SVG_DIR / "rbot-stacked-dark.svg", PNG_DIR / "rbot-stacked-dark-600x720.png", {"width": "600", "height": "720"}),
    (SVG_DIR / "rbot-stacked-dark.svg", PNG_DIR / "rbot-stacked-dark-1200x1440.png", {"width": "1200", "height": "1440"}),
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

# 4. Brand Guidelines Document
BRAND_GUIDE_MD = f"""# R-BOT WhatsApp — Official Brand Identity & Design Guidelines

**R-BOT** is an intelligent WhatsApp automation bot and messaging assistant actively serving users since **2021**.

---

## 1. Brand Concept: "Chat Visor R" (Concept A)
- **Monogram Fusion**: The iconic letter **'R'** seamlessly structured within an aerodynamic WhatsApp **speech bubble**.
- **Robotic Visor**: Embedded inside the upper loop of the 'R' is a glowing **sensor visor**, communicating 24/7 automated intelligence and responsiveness.
- **Heritage (Est. 2021)**: Over 5 years of proven reliability and uptime in the WhatsApp automation ecosystem.

---

## 2. Color Palette

| Token | Hex Code | RGB | Usage |
|---|---|---|---|
| **WhatsApp Emerald** | `{COLOR_WA_GREEN}` | `rgb(37, 211, 102)` | Primary brand color, speech bubble perimeter, success state |
| **Cyber Mint / Cyan** | `{COLOR_CYAN}` | `rgb(0, 242, 254)` | Gradient end, glowing robot sensor visor, automation accents |
| **WhatsApp Dark** | `{COLOR_DARK}` | `rgb(11, 20, 26)` | Official canvas background, high-contrast dark theme |
| **WhatsApp Slate** | `{COLOR_SLATE}` | `rgb(17, 27, 33)` | Card containers, surface layers |
| **Pure White** | `{COLOR_WHITE}` | `rgb(255, 255, 255)` | Monogram backbone pillar, primary typography |
| **Muted Slate** | `{COLOR_MUTED}` | `rgb(148, 163, 184)` | Subtitles, heritage taglines |

---

## 3. Deliverables Directory (`result/logo/r-bot/`)

```
result/logo/r-bot/
├── favicon.ico                         # Root multi-resolution website favicon
├── brand-guide.md                      # Complete Brand Identity Guidelines
├── svg/                                # Infinite-resolution vector assets
│   ├── rbot-symbol.svg                 # Standalone mark (transparent)
│   ├── rbot-app-icon.svg               # WhatsApp dark squircle tile
│   ├── rbot-horizontal-dark.svg        # Header lockup (Dark mode)
│   ├── rbot-horizontal-light.svg       # Header lockup (Light mode)
│   ├── rbot-stacked-dark.svg           # Vertical poster lockup
│   ├── rbot-symbol-black.svg           # 1-color black print variant
│   ├── rbot-symbol-white.svg           # 1-color white variant
│   ├── rbot-symbol-mono-25d366.svg     # 1-color WhatsApp Emerald
│   ├── rbot-symbol-mono-00f2fe.svg     # 1-color Cyber Cyan
│   ├── rbot-symbol-square.svg          # 1:1 Social avatar (padded)
│   └── rbot-symbol-favicon.svg         # Tight browser favicon vector
├── png/                                # High-resolution raster deliverables
│   ├── rbot-symbol-512.png / 1024.png / 2048.png / 4096.png (Up to 4K UHD)
│   ├── rbot-app-icon-512.png / 1024.png / 2048.png
│   ├── rbot-horizontal-dark-1200x360.png / 2400x720.png
│   ├── rbot-horizontal-light-1200x360.png / 2400x720.png
│   └── rbot-stacked-dark-600x720.png / 1200x1440.png
└── web/                                # Complete Web & PWA Icon Kit
    ├── favicon.ico                     # 16x16, 32x32, 48x48 icon
    ├── favicon-16.png / favicon-32.png / favicon-48.png
    ├── apple-touch-icon.png            # 180x180 iOS home icon
    ├── icon-192.png / icon-512.png     # Android PWA launcher icons
    ├── maskable-512.png                # Adaptive Android icon
    ├── site.webmanifest                # Web App Manifest
    └── head-snippet.html               # Copy-paste HTML header tags
```

---

## 4. Typography
- **Primary Wordmark**: `Space Grotesk` (Weight: 900 Black, Letter-spacing: +8px)
- **Tagline**: `Space Grotesk` / `DM Sans` (Weight: 800 Bold, Letter-spacing: +6px)
"""

(OUTPUT_DIR / "brand-guide.md").write_text(BRAND_GUIDE_MD, encoding="utf-8")
print("\n[OK] Brand guide written to result/logo/r-bot/brand-guide.md")
print("\nAll assets successfully generated in result/logo/r-bot/!")
