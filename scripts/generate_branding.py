#!/usr/bin/env python3
"""
Generate master branding assets for Kunime (Anime Streaming Web Platform):
1. branding/kunime-symbol.svg (transparent background, standalone master)
2. branding/kunime-app-icon.svg (on-tile with deep cinema canvas)
3. branding/kunime-horizontal-dark.svg (Dark cinema background lockup)
4. branding/kunime-horizontal-light.svg (Light transparent background lockup)
5. branding/kunime-stacked-dark.svg (Dark cinema stacked poster lockup)
6. branding/kunime-stacked-light.svg (Light transparent stacked lockup)
"""

from pathlib import Path

OUT_DIR = Path("/root/Build-app/branding")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Master Colors
COLOR_GRAD_START = "#FF2A5F"  # Cyber Crimson
COLOR_GRAD_END = "#FF6B35"    # Neon Vermilion
COLOR_DARK_CANVAS = "#090A10" # Cinema Obsidian
COLOR_CHARCOAL = "#0F172A"    # High-contrast charcoal for light mode
COLOR_WHITE = "#FFFFFF"

# 1. Master Symbol (Transparent, perfect 45°/135° geometric cuts)
SYMBOL_SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <title>Kunime Katana Play Symbol</title>
  <defs>
    <linearGradient id="kunime-primary" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{COLOR_GRAD_START}" />
      <stop offset="100%" stop-color="{COLOR_GRAD_END}" />
    </linearGradient>
  </defs>

  <g id="kunime-symbol" transform="translate(121, 116)">
    <!-- Vertical Katana Backbone / Pillar -->
    <rect x="0" y="0" width="56" height="280" rx="16" fill="{COLOR_WHITE}" />

    <!-- Upper Katana Diagonal Slash -->
    <path d="M 88,160 L 216,32 C 224,24 236,24 244,32 L 256,44 C 264,52 264,64 256,72 L 144,184 Z" fill="url(#kunime-primary)" />

    <!-- Lower Streaming Diagonal Slash -->
    <path d="M 88,120 L 256,232 C 264,240 264,252 256,260 L 236,276 C 228,284 216,284 208,276 L 72,168 Z" fill="url(#kunime-primary)" />

    <!-- Embedded High-Energy Play Triangle Core -->
    <polygon points="112,96 224,170 112,244" fill="{COLOR_WHITE}" />
  </g>
</svg>
"""

# 2. Master App Icon (Deep Obsidian Rounded Tile with glow)
APP_ICON_SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <title>Kunime App Icon</title>
  <defs>
    <linearGradient id="kunime-primary" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{COLOR_GRAD_START}" />
      <stop offset="100%" stop-color="{COLOR_GRAD_END}" />
    </linearGradient>
    <filter id="kunime-subtle-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="16" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Cinema Dark Background Tile -->
  <rect width="512" height="512" rx="112" fill="{COLOR_DARK_CANVAS}" />

  <!-- Background Ambient Glow behind Katana Blade -->
  <circle cx="280" cy="240" r="140" fill="{COLOR_GRAD_START}" opacity="0.18" filter="url(#kunime-subtle-glow)" />

  <g transform="translate(121, 116)">
    <!-- Vertical Katana Backbone -->
    <rect x="0" y="0" width="56" height="280" rx="16" fill="{COLOR_WHITE}" />

    <!-- Upper Katana Diagonal Slash -->
    <path d="M 88,160 L 216,32 C 224,24 236,24 244,32 L 256,44 C 264,52 264,64 256,72 L 144,184 Z" fill="url(#kunime-primary)" />

    <!-- Lower Streaming Diagonal Slash -->
    <path d="M 88,120 L 256,232 C 264,240 264,252 256,260 L 236,276 C 228,284 216,284 208,276 L 72,168 Z" fill="url(#kunime-primary)" />

    <!-- Embedded High-Energy Play Triangle Core -->
    <polygon points="112,96 224,170 112,244" fill="{COLOR_WHITE}" />
  </g>
</svg>
"""

# 3. Master Horizontal Lockup - Dark Cinema Mode (Standard for streaming UI headers)
# ViewBox: 1200 x 360
HORIZONTAL_DARK_SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 360" width="100%" height="100%">
  <title>Kunime Horizontal Brand Lockup (Dark)</title>
  <defs>
    <linearGradient id="kunime-primary" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{COLOR_GRAD_START}" />
      <stop offset="100%" stop-color="{COLOR_GRAD_END}" />
    </linearGradient>
    <linearGradient id="text-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="85%" stop-color="#F1F5F9" />
      <stop offset="100%" stop-color="{COLOR_GRAD_START}" />
    </linearGradient>
  </defs>

  <!-- Cinema Dark Canvas -->
  <rect width="1200" height="360" rx="36" fill="{COLOR_DARK_CANVAS}" />

  <!-- Symbol Left Scale (0.75x) -->
  <g transform="translate(80, 75) scale(0.75)">
    <!-- Vertical Pillar -->
    <rect x="0" y="0" width="56" height="280" rx="16" fill="{COLOR_WHITE}" />

    <!-- Upper Slash -->
    <path d="M 88,160 L 216,32 C 224,24 236,24 244,32 L 256,44 C 264,52 264,64 256,72 L 144,184 Z" fill="url(#kunime-primary)" />

    <!-- Lower Slash -->
    <path d="M 88,120 L 256,232 C 264,240 264,252 256,260 L 236,276 C 228,284 216,284 208,276 L 72,168 Z" fill="url(#kunime-primary)" />

    <!-- Play Arrow -->
    <polygon points="112,96 224,170 112,244" fill="{COLOR_WHITE}" />
  </g>

  <!-- Typography: KUNIME Wordmark -->
  <g transform="translate(340, 205)">
    <text font-family="'Space Grotesk', 'DejaVu Sans', sans-serif" font-size="124" font-weight="900" letter-spacing="8" fill="url(#text-grad)">KUNIME</text>
  </g>

  <!-- Subtitle Accent + Tagline -->
  <g transform="translate(344, 258)">
    <rect x="0" y="-18" width="8" height="22" rx="4" fill="url(#kunime-primary)" />
    <text x="20" y="0" font-family="'Space Grotesk', 'DejaVu Sans', sans-serif" font-size="20" font-weight="700" letter-spacing="8" fill="#94A3B8">ANIME STREAMING PLATFORM</text>
  </g>
</svg>
"""

# 4. Master Horizontal Lockup - Light Transparent Mode
HORIZONTAL_LIGHT_SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 360" width="100%" height="100%">
  <title>Kunime Horizontal Brand Lockup (Light)</title>
  <defs>
    <linearGradient id="kunime-primary" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{COLOR_GRAD_START}" />
      <stop offset="100%" stop-color="{COLOR_GRAD_END}" />
    </linearGradient>
  </defs>

  <!-- Symbol Left Scale (0.75x) -->
  <g transform="translate(80, 75) scale(0.75)">
    <!-- Vertical Pillar in high-contrast charcoal -->
    <rect x="0" y="0" width="56" height="280" rx="16" fill="{COLOR_CHARCOAL}" />

    <!-- Upper Slash -->
    <path d="M 88,160 L 216,32 C 224,24 236,24 244,32 L 256,44 C 264,52 264,64 256,72 L 144,184 Z" fill="url(#kunime-primary)" />

    <!-- Lower Slash -->
    <path d="M 88,120 L 256,232 C 264,240 264,252 256,260 L 236,276 C 228,284 216,284 208,276 L 72,168 Z" fill="url(#kunime-primary)" />

    <!-- Play Arrow in high-contrast charcoal -->
    <polygon points="112,96 224,170 112,244" fill="{COLOR_CHARCOAL}" />
  </g>

  <!-- Typography: KUNIME Wordmark in deep charcoal -->
  <g transform="translate(340, 205)">
    <text font-family="'Space Grotesk', 'DejaVu Sans', sans-serif" font-size="124" font-weight="900" letter-spacing="8" fill="{COLOR_CHARCOAL}">KUNIME</text>
  </g>

  <!-- Subtitle Accent + Tagline -->
  <g transform="translate(344, 258)">
    <rect x="0" y="-18" width="8" height="22" rx="4" fill="url(#kunime-primary)" />
    <text x="20" y="0" font-family="'Space Grotesk', 'DejaVu Sans', sans-serif" font-size="20" font-weight="700" letter-spacing="8" fill="#475569">ANIME STREAMING PLATFORM</text>
  </g>
</svg>
"""

# 5. Master Stacked Lockup - Dark Cinema Mode
STACKED_DARK_SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 720" width="100%" height="100%">
  <title>Kunime Stacked Brand Lockup (Dark)</title>
  <defs>
    <linearGradient id="kunime-primary" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{COLOR_GRAD_START}" />
      <stop offset="100%" stop-color="{COLOR_GRAD_END}" />
    </linearGradient>
  </defs>

  <!-- Cinema Dark Canvas -->
  <rect width="600" height="720" rx="48" fill="{COLOR_DARK_CANVAS}" />

  <!-- Symbol Centered Top -->
  <g transform="translate(165, 80)">
    <rect x="0" y="0" width="56" height="280" rx="16" fill="{COLOR_WHITE}" />
    <path d="M 88,160 L 216,32 C 224,24 236,24 244,32 L 256,44 C 264,52 264,64 256,72 L 144,184 Z" fill="url(#kunime-primary)" />
    <path d="M 88,120 L 256,232 C 264,240 264,252 256,260 L 236,276 C 228,284 216,284 208,276 L 72,168 Z" fill="url(#kunime-primary)" />
    <polygon points="112,96 224,170 112,244" fill="{COLOR_WHITE}" />
  </g>

  <!-- Wordmark Centered -->
  <g transform="translate(300, 480)" text-anchor="middle">
    <text font-family="'Space Grotesk', 'DejaVu Sans', sans-serif" font-size="104" font-weight="900" letter-spacing="10" fill="{COLOR_WHITE}">KUNIME</text>
  </g>

  <!-- Tagline Centered -->
  <g transform="translate(300, 545)" text-anchor="middle">
    <text font-family="'Space Grotesk', 'DejaVu Sans', sans-serif" font-size="22" font-weight="700" letter-spacing="8" fill="#94A3B8">ANIME STREAMING PLATFORM</text>
  </g>
</svg>
"""

# Write files
(OUT_DIR / "kunime-symbol.svg").write_text(SYMBOL_SVG, encoding="utf-8")
(OUT_DIR / "kunime-app-icon.svg").write_text(APP_ICON_SVG, encoding="utf-8")
(OUT_DIR / "kunime-horizontal.svg").write_text(HORIZONTAL_DARK_SVG, encoding="utf-8")
(OUT_DIR / "kunime-horizontal-dark.svg").write_text(HORIZONTAL_DARK_SVG, encoding="utf-8")
(OUT_DIR / "kunime-horizontal-light.svg").write_text(HORIZONTAL_LIGHT_SVG, encoding="utf-8")
(OUT_DIR / "kunime-stacked.svg").write_text(STACKED_DARK_SVG, encoding="utf-8")
(OUT_DIR / "kunime-stacked-dark.svg").write_text(STACKED_DARK_SVG, encoding="utf-8")

print("Generated master SVG files in /root/Build-app/branding:")
for f in OUT_DIR.glob("*.svg"):
    print(f" - {f.name} ({f.stat().st_size} bytes)")
