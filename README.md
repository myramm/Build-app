# Summertime Saga v0.20.16 - Terjemahan Bahasa Indonesia

Repositori ini berisi file translasi lengkap ke dalam **Bahasa Indonesia** untuk **Summertime Saga v0.20.16 (Stable)** dan pipeline otomatisasi build APK Android.

---

## 📥 Download Game & File Terjemahan

Silakan unduh file terbaru melalui menu **[Releases](https://github.com/myramm/Build-app/releases)**:

1. **`SummertimeSaga-0.20.16-Indonesian.apk`** (~875 MB)
   * File APK siap pasang di HP Android.
   * Sudah ditandatangani (*signed*) menggunakan v1/v2/v3 signature.
   * Tidak akan kembali ke Bahasa Inggris (Bahasa Indonesia menjadi bahasa native).

2. **`SummertimeSaga_v0.20.16_Bahasa_Indonesia.zip`** (~2.8 MB)
   * Kumpulan 1.625 file script `.rpy` (75.875 baris dialog) yang sudah diterjemahkan.
   * Cocok untuk modding, backup, atau rebuild APK sendiri.

---

## 🛠️ Cara Penggunaan & Pemasangan

### Metode 1: Pasang APK Langsung di HP Android
1. Download file `SummertimeSaga-0.20.16-Indonesian.apk` dari tab [Releases](https://github.com/myramm/Build-app/releases).
2. Install di HP Android Anda (izinkan *Install Unknown Apps* jika muncul peringatan).
3. Buka game dan langsung mainkan dalam Bahasa Indonesia.

### Metode 2: Pasang File Script ke Folder Game (Tanpa Install APK Baru)
1. Download dan ekstrak `SummertimeSaga_v0.20.16_Bahasa_Indonesia.zip`.
2. Salin folder `scripts/` ke direktori penyimpanan game:
   ```
   Android/data/com.kompasproductions.summertimesaga/files/game/
   ```
3. Buka game seperti biasa.

---

## 📜 Statistik Translasi
* **Total File Script:** 1.625 file `.rpy`
* **Total Baris Dialog:** 75.875 baris teks
* **Proteksi Tag:** Tag formatting (`{b}`, `{i}`, `{color}`), variabel nama (`[player_name]`, `[firstname]`), dan karakter khusus dipertahankan 100% tanpa merusak kode Python / Ren'Py.
