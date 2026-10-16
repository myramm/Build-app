#!/usr/bin/env python3
"""
Generate 3 distinct logo concepts for "R-BOT Whatsapp" (Active since 2021):
1. concept-a.svg: Chat Bubble 'R' with Robot Visor (Recommended)
2. concept-b.svg: Mecha Robot Head Monogram
3. concept-c.svg: Automated Circuit Node 'R' with Est. 2021 heritage badge
"""

from pathlib import Path

OUT_DIR = Path("/root/Build-app/branding/r-bot/concepts")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# 1. Concept A: Chat Bubble 'R' with Robot Visor & WhatsApp Green
CONCEPT_A_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <title>R-BOT Concept A - Chat Visor R</title>
  <defs>
    <linearGradient id="wa-grad-a" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#25D366" />
      <stop offset="100%" stop-color="#00F2FE" />
    </linearGradient>
    <linearGradient id="bubble-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#111B21" />
      <stop offset="100%" stop-color="#0B141A" />
    </linearGradient>
  </defs>

  <!-- Deep WhatsApp Dark Background -->
  <rect width="512" height="512" rx="112" fill="url(#bubble-grad)" />

  <!-- Outer Speech Bubble Accent Ring with Tail -->
  <path d="M 256,76 C 156,76 76,156 76,256 C 76,290 85,322 102,350 L 82,414 C 80,422 88,430 96,428 L 164,406 C 191,424 222,436 256,436 C 356,436 436,356 436,256 C 436,156 356,76 256,76 Z" 
        fill="none" stroke="url(#wa-grad-a)" stroke-width="16" stroke-linecap="round" stroke-linejoin="round" />

  <!-- Central 'R' Robot Monogram -->
  <g transform="translate(18, -4)">
    <!-- Vertical Pillar -->
    <rect x="170" y="164" width="38" height="172" rx="14" fill="#FFFFFF" />

    <!-- Upper Loop with Robot Head Curvature -->
    <path d="M 208,164 L 274,164 C 314,164 340,190 340,224 C 340,258 314,284 274,284 L 208,284 Z" 
          fill="none" stroke="url(#wa-grad-a)" stroke-width="36" stroke-linecap="round" stroke-linejoin="round" />

    <!-- Robot Visor Eye inside Loop -->
    <rect x="230" y="210" width="56" height="24" rx="12" fill="#00F2FE" />
    <circle cx="246" cy="222" r="5" fill="#0B141A" />
    <circle cx="270" cy="222" r="5" fill="#0B141A" />

    <!-- Diagonal Katana-Clean Leg (Exact 45° angle) -->
    <path d="M 238,260 L 320,342 C 326,348 338,348 344,342 L 354,332 C 360,326 360,314 354,308 L 272,226 Z" 
          fill="url(#wa-grad-a)" />
  </g>
</svg>
"""

# 2. Concept B: Mecha Robot Head Monogram
CONCEPT_B_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <title>R-BOT Concept B - Mecha Head Monogram</title>
  <defs>
    <linearGradient id="wa-grad-b" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10B981" />
      <stop offset="100%" stop-color="#25D366" />
    </linearGradient>
  </defs>

  <!-- Deep Canvas -->
  <rect width="512" height="512" rx="112" fill="#0B141A" />

  <!-- Glowing Aura -->
  <circle cx="256" cy="256" r="150" fill="#25D366" opacity="0.08" />

  <!-- Robot Head Silhouette forming 'R' -->
  <g transform="translate(136, 126)">
    <!-- Left Ear / Backbone Pillar -->
    <rect x="0" y="0" width="48" height="260" rx="16" fill="#FFFFFF" />

    <!-- Top Antenna Pin -->
    <path d="M 24,0 L 24,-36 M 16,-36 L 32,-36" stroke="#25D366" stroke-width="12" stroke-linecap="round" />
    <circle cx="24" cy="-44" r="8" fill="#25D366" />

    <!-- Robot Cranium & Upper Loop -->
    <path d="M 48,0 L 150,0 C 200,0 232,32 232,80 C 232,128 200,160 150,160 L 48,160 Z" fill="url(#wa-grad-b)" />

    <!-- Visor Slot (Cut-out) -->
    <rect x="68" y="52" width="116" height="40" rx="14" fill="#0B141A" />
    <!-- Dual Cyan Sensor Eyes -->
    <circle cx="102" cy="72" r="10" fill="#00F2FE" />
    <circle cx="150" cy="72" r="10" fill="#00F2FE" />

    <!-- Diagonal Stride Leg -->
    <path d="M 120,140 L 220,240 C 228,248 240,248 248,240 L 254,234 C 262,226 262,214 254,206 L 160,112 Z" fill="url(#wa-grad-b)" />

    <!-- 3 Communicative WhatsApp Message Dots on Lower Jaw -->
    <circle cx="80" cy="216" r="10" fill="#25D366" />
    <circle cx="112" cy="216" r="10" fill="#25D366" />
    <circle cx="144" cy="216" r="10" fill="#25D366" />
  </g>
</svg>
"""

# 3. Concept C: Automated Circuit Loop 'R' with Heritage 2021
CONCEPT_C_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <title>R-BOT Concept C - Circuit Loop R</title>
  <defs>
    <linearGradient id="wa-grad-c" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#128C7E" />
      <stop offset="50%" stop-color="#25D366" />
      <stop offset="100%" stop-color="#34D399" />
    </linearGradient>
  </defs>

  <!-- Deep Canvas -->
  <rect width="512" height="512" rx="112" fill="#0C1317" />

  <!-- Outer Interlocking Chat Speech Bubble -->
  <path d="M 256,92 C 166,92 92,166 92,256 C 92,286 100,314 116,338 L 98,396 C 96,402 102,408 108,406 L 168,388 C 193,408 223,420 256,420 C 346,420 420,346 420,256 C 420,166 346,92 256,92 Z" 
        fill="#111B21" stroke="#1F2C34" stroke-width="6" />

  <!-- Glowing Geometric Circuit 'R' -->
  <g transform="translate(156, 140)">
    <!-- Vertical Data Bus (Pillar) -->
    <rect x="0" y="0" width="44" height="210" rx="14" fill="#FFFFFF" />
    <!-- Node circles -->
    <circle cx="22" cy="30" r="7" fill="#128C7E" />
    <circle cx="22" cy="180" r="7" fill="#128C7E" />

    <!-- Circuit Arc Upper Loop -->
    <path d="M 44,24 L 126,24 C 168,24 196,52 196,96 C 196,140 168,168 126,168 L 44,168" 
          fill="none" stroke="url(#wa-grad-c)" stroke-width="32" stroke-linecap="round" stroke-linejoin="round" />

    <!-- Core Automation Pulse Indicator -->
    <circle cx="110" cy="96" r="14" fill="#25D366" />
    <circle cx="110" cy="96" r="6" fill="#FFFFFF" />

    <!-- Circuit Strike Leg -->
    <path d="M 100,154 L 176,230 C 182,236 194,236 200,230 L 206,224 C 212,218 212,206 206,200 L 136,130 Z" 
          fill="url(#wa-grad-c)" />
  </g>

  <!-- Heritage Badge: EST. 2021 -->
  <g transform="translate(256, 460)" text-anchor="middle">
    <text font-family="'Space Grotesk', -apple-system, sans-serif" font-size="16" font-weight="800" letter-spacing="4" fill="#64748B">EST. 2021 • WHATSAPP BOT</text>
  </g>
</svg>
"""

(OUT_DIR / "concept-a.svg").write_text(CONCEPT_A_SVG, encoding="utf-8")
(OUT_DIR / "concept-b.svg").write_text(CONCEPT_B_SVG, encoding="utf-8")
(OUT_DIR / "concept-c.svg").write_text(CONCEPT_C_SVG, encoding="utf-8")

print("Generated 3 R-BOT concept SVGs:")
for f in OUT_DIR.glob("*.svg"):
    print(f" - {f.name} ({f.stat().st_size} bytes)")
