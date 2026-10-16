# Kunime — Official Brand Identity & Design Guidelines

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
| **Cyber Crimson** | `#FF2A5F` | `rgb(255, 42, 95)` | Primary gradient start, key actions, live tags |
| **Neon Vermilion** | `#FF6B35` | `rgb(255, 107, 53)` | Primary gradient end, play accents, hover glows |
| **Cinema Obsidian** | `#090A10` | `rgb(9, 10, 16)` | App icon canvas, dark mode web background |
| **Pure White** | `#FFFFFF` | `rgb(255, 255, 255)` | Katana backbone, primary wordmark, play core |
| **Muted Slate** | `#94A3B8` | `rgb(148, 163, 184)` | Secondary taglines, subtitles, UI metadata |

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
