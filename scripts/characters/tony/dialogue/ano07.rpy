label ano07_hint_tony:
    show anon with dissolve:
        flip
    tony @ a_frustrated "Kamu sudah mendapatkan roda baru, jagoan?"

    anon f_worried "Tidak, saya masih mengerjakannya."

    tony f_suspicious "Yah, jangan berlama-lama di sini..."

    tony @ a_point "{b}Kunjungi dealer mobil dan lihat kisaran harga Anda{/b}!"

    anon f_normal @ a_salute "Ya, tuan!"

    hide anon with dissolve
    return


label ano07_wage_tony:
    show anon with dissolve:
        flip
    anon "Hai, {b}Tony{/b}!"

    anon @ f_laugh "Saya berhasil!"

    tony "Kamu melakukan apa?"

    anon "Aku punya mobil untuk diriku sendiri!"

    tony @ a_point "Oh, kamu melakukannya ya?"

    anon "Ya, aku sudah memarkirnya di luar sekarang."

    tony @ a_frustrated "Baiklah, mari kita lihat, oke?"

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
    show tony_overlay_o_car as compact:
        flip
    with fade
    show anon behind compact with dissolve:
        flip
        xoffset -100
    tony f_suspicious "Astaga, benda apa ini?"

    tony "Apakah itu datang dengan dompet dan sepatu hak tinggi?"

    anon f_worried_low "Hei, ayolah {b}Tony{/b}... Itu satu-satunya barang yang mereka miliki dalam kisaran harga saya."

    tony f_normal "Hehe, cukup adil."

    anon f_normal "Saya mendapatkannya dengan harga kurang dari setengah harga juga."

    tony @ a_frustrated "Kerja bagus, juara!"

    tony "Tahukah Anda, saya yakin benda ini akan menarik banyak perhatian wanita!"

    anon @ f_laugh "Menurutmu begitu?"

    tony "Ah ya!"

    tony @ a_fists "Pastikan Anda menunjukkan rasa percaya diri saat mengendarainya, ya?"

    tony "Mereka akan menyerangmu seperti lebah di atas madu."

    anon "Saya harap Anda benar."

    show tony f_suspicious a_whisper with dissolve:
        unflip
        xoffset -400
    tony "Eh, {b}Maria{/b}!"

    tony "Keluar dari sini, cepat!"

    show tony f_normal a_idle with dissolve
    pause
    tony "Dia harus melihat ini..."

    show maria f_annoyed behind compact with dissolve:
        flip
        xoffset -200
    maria "Apa, anak itu mendapat mobil baru?"

    tony "Anda yakin."

    tony "{b}[firstname]{/b} sedang naik daun di dunia."

    maria f_surprised "!!!"
    maria "Ada apa dengan warnanya?"

    tony @ f_smirk_wink "Dia bilang itu satu-satunya barang yang mereka punya dalam kisaran harganya..."

    maria f_normal "Apakah begitu?"

    show tony with dissolve:
        flip
        xoffset 0
    anon "Ya, Bu."

    maria "Baiklah, aku akan mengatakan ini..."

    maria "Seorang pria berkeliling dengan benda ini, dia aneh atau sangat nyaman dengan kejantanannya."

    tony @ f_laugh a_belly "Hahahaah!"

    tony "Saya cukup yakin itu yang terakhir."

    maria "Ya, saya yakin."

    pause
    maria "Berhati-hatilah saat mengendarainya, ya?"

    maria "Kami akhirnya mendapatkan seorang pengantar barang yang baik."

    maria "Tuhan tahu apakah kita akan menemukan yang lain."

    maria "Selamat, Nak."

    maria "Saya suka warnanya."

    anon @ f_laugh "Terima kasih, {b}Maria{/b}."

    hide maria with dissolve
    pause
    show tony a_mc_hip_single:
        xoffset -68
    show tony_arms_dressed_a_mc_shoulder_single behind compact:
        flip
        xoffset -68
    with dissolve
    tony "Ya, Anda pasti telah memenangkan hatinya."

    anon "Ya?"

    tony "Anda pasti mendapat kesan yang baik dengan pizza itu, bukan?"

    anon "Saya rasa begitu."

    tony "Heh, attaboy!"

    tony "Ayo, kita mulai pengirimannya, ya?"

    tony "Aku harus melihat apakah aku akan memberimu kenaikan gaji lagi."

    hide tony_arms_dressed_a_mc_shoulder_single
    hide tony
    with dissolve
    anon @ a_salute "Ya, tuan!"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
