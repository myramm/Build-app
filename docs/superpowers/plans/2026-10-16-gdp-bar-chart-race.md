# GDP Bar Chart Race (1950–2026) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

Build an ultra-smooth, 60 FPS TikTok-format (9:16 vertical 1080x1920) animated **GDP Bar Chart Race of World Economies from 1950 to 2026**, rendered via GitHub Actions to `result/video3.mp4`.

---

## File Structure

- `src/gdp/types.ts`: TypeScript interfaces for Country, GDP Record, and Year Data.
- `src/gdp/data.ts`: Historical & projection GDP database (1950–2026) and interpolation utilities.
- `src/gdp/GdpHeader.tsx`: Title header with dynamic giant year counter (1950 ➔ 2026).
- `src/gdp/GdpBar.tsx`: Animated horizontal bar with smooth spring rank repositioning and value count.
- `src/gdp/GdpMilestone.tsx`: Milestone toast notification on historical economic shifts (e.g. 1968, 1991, 2010).
- `src/GdpComposition.tsx`: Top-level Remotion composition assembling the bar chart race with audio.
- `src/Root.tsx`: Register `GdpRace` composition (1080x1920 @ 60 FPS, 3300 frames / 55s).
- `.github/workflows/render.yml`: Configure cloud rendering to output `result/video3.mp4`.

---

## Tasks

### Task 1: Historical GDP Dataset & Interpolation Engine
- [ ] Create `src/gdp/types.ts` defining data types (`CountryData`, `Milestone`).
- [ ] Create `src/gdp/data.ts` containing GDP figures (in Billion USD) from 1950 to 2026 for major global economies (US, China, Japan, Germany, UK, India, France, Italy, USSR/Russia, Brazil, Canada, South Korea).
- [ ] Implement `interpolateGdp(year: number)` returning smooth top 10 ranked countries at any fractional year.

### Task 2: Voiceover & Audio Ambience Generation
- [ ] Generate natural Indonesian voiceover for the TikTok intro using Edge-TTS ArdiNatural.
- [ ] Save audio to `public/audio/gdp/intro.mp3`.

### Task 3: Visual Components (Bars, Dynamic Year, Milestone Badges)
- [ ] Create `src/gdp/GdpHeader.tsx` displaying the title and a giant ticking year watermark.
- [ ] Create `src/gdp/GdpBar.tsx` featuring country flag, name, value label, and smooth vertical position transitions.
- [ ] Create `src/gdp/GdpMilestone.tsx` displaying historical event callouts.

### Task 4: Composition Assembly & Root Registration
- [ ] Create `src/GdpComposition.tsx` tying together the timeline, audio, and visual elements.
- [ ] Update `src/Root.tsx` to register `GdpRace` (3300 frames @ 60 FPS).

### Task 5: Workflow Configuration, GitHub Push & Render Execution
- [ ] Update `.github/workflows/render.yml` to render composition `GdpRace` to `result/video3.mp4`.
- [ ] Update `README.md` with details of `video3.mp4`.
- [ ] Commit and push to GitHub, trigger rendering, and verify `result/video3.mp4`.
