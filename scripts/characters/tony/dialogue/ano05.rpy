label ano05_hint_tony:
    show anon with dissolve:
        flip
    tony @ a_frustrated "Kamu sudah mendapatkan roda baru, jagoan?"

    anon f_worried "Tidak, saya masih mengerjakannya."

    tony f_suspicious "Yah, jangan berlama-lama di sini..."

    tony @ a_point "{b}Kunjungi dealer mobil dan lihat kisaran harga Anda{/b}!"

    anon f_normal @ a_salute "Ya, tuan!"

    hide anon with dissolve
    return


label ano05_wage_tony:
    show anon with dissolve:
        flip
    anon "Hai, {b}Tony{/b}!"

    anon "Saya berhasil!"

    tony "Kamu melakukan apa?"

    anon "Saya mendapatkan sendiri kendaraan!"

    tony "Oh, kamu melakukannya ya?"

    anon "Ya, aku sudah memarkirnya di luar sekarang."

    tony "Baiklah, mari kita lihat, oke?"

    hide tony
    show anon:
        unflip
        xoffset 500
    with {'master': dissolve}
    anon "Ya, tuan!"

    hide anon with dissolve

    scene expression background(712, 480, 2.0, l=L_pizzeria_exterior) as stage
    show tony f_normal_down:
        flip
    show tony_overlay_o_scooter as scooter
    with fade
    show anon f_shy_low behind scooter with dissolve:
        flip
        xoffset 100
    tony "Hei, lihat ini!"

    tony f_normal "Anda punya skuter kecil yang bagus, bukan?"

    anon f_normal "Anda yakin!"

    anon @ f_laugh a_point "Saya mendapatkannya dengan setengah harga juga."

    tony @ a_frustrated "Kerja bagus, juara!"

    tony "Aku sangat bangga padamu!"

    anon @ f_laugh "Terima kasih, {b}Tony{/b}!"

    show tony f_suspicious a_whisper with dissolve:
        unflip
        xoffset -400
    tony "Eh, {b}Maria{/b}!"

    tony "Keluar dari sini, cepat!"

    pause
    tony f_normal a_idle "Dia harus melihat ini..."

    show maria f_annoyed behind scooter with dissolve:
        flip
        xoffset -200
    maria "Apa yang kamu teriakkan?"

    tony @ a_point_back "Lihat roda baru pengantar barang kami."

    maria f_surprised "Ahh, jangan bilang kamu membelikan ini untuknya?"

    tony f_suspicious "Tentu saja saya tidak melakukannya!"

    tony "Dia membeli ini dengan uangnya sendiri yang dia hasilkan di sini, bekerja untukmu."

    maria f_normal "Apakah begitu?"

    show tony f_normal with dissolve:
        flip
        xoffset 0
    anon "Ya, Bu."

    maria "Yah, warnai aku terkejut."

    tony @ a_point "Sudah kubilang ya, yang ini penjaganya."

    tony "Eh?"

    tony "Bukankah aku sudah memberitahumu?"

    maria f_annoyed "Ya, ya..."

    maria "Jangan terlalu rendah hati sekarang, kera besar."

    tony @ f_laugh a_belly "Hahahaah!"

    tony a_heart "Dia datang ke sini sebagai laki-laki, tapi dia akan pergi sebagai laki-laki."

    tony "Aku beritahu kamu apa."

    maria "Aku akan kembali ke dapur sebelum calzonesku terbakar."

    maria f_normal "Selamat, Nak."

    maria "Saya suka warnanya."

    anon "Terima kasih, {b}Maria{/b}."

    hide maria with dissolve
    pause
    show tony a_mc_hip_single:
        xoffset 132
    show tony_arms_dressed_a_mc_shoulder_single behind scooter:
        flip
        xoffset 132
    with dissolve
    tony "Baiklah, kurasa aku harus mulai membayarmu lebih banyak sekarang, ya?"

    anon "Oh benar!"

    anon "Anda menjanjikan kenaikan gaji kepada saya, bukan?"

    tony "Ya, hanya jika Anda menginginkannya?"

    anon "Saya pasti menginginkannya!"

    tony "Heh, attaboy!"

    tony "Ayo, kita mulai pengirimannya, ya?"

    tony "Saya ingin melihat apa yang bisa dilakukan bayi ini."

    hide tony_arms_dressed_a_mc_shoulder_single
    hide tony
    with dissolve
    anon f_grin @ f_laugh "Ya, tuan!"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
