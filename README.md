# Remotion Video Project (Rendered with GitHub Actions)

Repositori ini berisi proyek Remotion yang di-render secara otomatis di cloud menggunakan **GitHub Actions** (RAM 7 GB, 60 FPS).

## 📁 Daftar Video Hasil Render (Folder `result/`)

### 1. `result/video1.mp4`
- **Judul**: *TAUKAH KAMU? Sistem Perang Modern Masa Kini*
- **Format**: Vertikal 1080 × 1920 (9:16), 60 FPS Murni (1.850 Frame)
- **Topik**: Drone intai, Satelit & Radar Phased Array, C4ISR tactical network, sistem pertahanan udara otomatis, dan jet siluman Gen-5.

### 2. `result/video2.mp4`
- **Judul**: *Cara Install Remotion + AI Skill | Bikin Video Otomatis Pakai Gemini!*
- **Format**: Vertikal 1080 × 1920 (9:16), 60 FPS Murni (3.770 Frame / ~62 detik)
- **Materi Lengkap 7 Langkah**:
  1. **Pengenalan**: Apa itu Remotion & konsep video as code.
  2. **Persiapan**: Cek Node.js (18+) dan npm di terminal.
  3. **Instalasi**: Menjalankan `npx create-video@latest` & memilih template TypeScript.
  4. **Pasang AI Skill**: `npx skills add remotion-dev/skills` agar Gemini/Claude paham aturan Remotion.
  5. **Remotion Studio**: Menjalankan `npm start` untuk live preview di browser.
  6. **Koding Komponen**: `spring()`, `interpolate()`, dan `useCurrentFrame()` untuk animasi 60 FPS.
  7. **Render MP4**: Menjalankan `npx remotion render` menghasilkan file MP4 final.
