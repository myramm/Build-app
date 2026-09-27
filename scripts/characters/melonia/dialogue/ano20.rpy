label ano20_init_melonia_guards:
    anon f_worried "Bisakah kamu membantu para penjaga?"

    melonia f_normal "Apakah sudah waktunya?"

    anon "Ya, tolong."

    melonia f_smirk "Saya tidak sabar untuk melihat wajah bodohnya begitu dia menyadari bahwa dia telah dirampok!"

    show anon f_normal
    melonia "Pastikan untuk tidak terlihat sampai saya mengirim penjaga pergi."

    anon "Tentu saja."

    melonia @ f_laugh "Hehe, ini akan menyenangkan!"

    hide melonia
    show anon:
        flip
        xoffset -500
    with dissolve
    pause
    anon f_worried "Wow, kamu sangat menikmati ini..."

    hide anon with dissolve

    scene expression background(480, 432, 4.5, l=L_rump_lobby) as stage
    show bodyguard:
        xoffset -600
    with fade
    bodyguard "{i}*Huh*{/i} Shift malam adalah yang terburuk..."

    melonia "Hei, bodoh!"

    show melonia f_smirk
    show bodyguard f_suspicious:
        flip
        xoffset 0
    with dissolve
    bodyguard @ -m_talk "Hmm?"

    bodyguard f_surprised "{b}Ny. Bokong{/b}?"

    bodyguard "Apa yang kamu lakukan di sini?"

    melonia @ f_eyeroll "Aku tinggal di sini, bodoh..."

    bodyguard "B-benar, tentu saja... maksudku-"

    melonia "{i}*Ahem*{/i} Ya, saya tahu maksud Anda."

    melonia "Dengar, jasamu tidak lagi diperlukan di sini malam ini."

    bodyguard "Saya minta maaf?"

    melonia "Aku dan suamiku sedang kedatangan tamu-tamu penting dan kami tidak membutuhkan sekelompok preman berjas murahan yang melirik dan membuat mereka merasa tidak nyaman."

    bodyguard f_normal "Oh, entahlah, Bu..."

    bodyguard "Saya mendapat perintah yang sangat ketat untuk-"

    melonia f_annoyed "Permisi?"

    melonia "Saya memberi perintah di sekitar sini atau Anda lupa?!"

    bodyguard f_surprised a_defensive "{i}*Gulp*{/i} T-tidak, tentu saja tidak!"

    melonia "Kamu punya waktu sampai sepuluh hitungan untuk menghilang dari pandanganku atau aku bersumpah, aku akan menyuruhmu menggosok toilet di Teluk Guantanamo sebelum akhir minggu ini!"

    bodyguard a_wave "Itu tidak perlu, aku-"

    melonia f_yell "SATU!"

    bodyguard a_defensive "Bu, tolong, izinkan saya-"

    melonia "DUA!"

    bodyguard "Walikota akan-"

    melonia "LIMA!!"

    bodyguard "Apa yang terjadi dengan tiga dan empat?!"

    melonia "TUJUH!!!"

    bodyguard "Eep!"

    hide bodyguard with fastdissolve
    melonia f_smirk "Hmph, bodoh..."

    pause
    show melonia f_smirk_up with dissolve:
        flip
        xoffset 200
    melonia "Anda bisa keluar sekarang."

    show anon f_worried:
        flip
    show melonia f_smirk
    with dissolve
    anon "Wow, itu tadi um..."

    melonia "Mengesankan?"

    anon "Tadinya saya akan mengatakan menakutkan tapi tentu saja, mari kita lakukan dengan mengesankan."

    melonia @ f_laugh "Hah!"

    melonia "Ya, itu berhasil, bukan?"

    melonia "Anda harus berada di kantor sendirian setidaknya selama beberapa jam..."

    anon f_normal "Aku tidak memerlukan waktu selama itu."

    melonia "Oh."

    melonia "Baiklah, silakan pecahkan beberapa barang, jika Anda mau."

    anon "Ehh, ya... Mungkin."

    melonia "Saya akan berada di atas di tempat tidur jika Anda bosan."

    melonia "Ngomong-ngomong, aku tidur telanjang..."

    show melonia f_smirk_lipbite
    anon f_surprised @ -m_talk "!!!"
    melonia f_smirk "Sekadar bahan untuk dipikirkan."

    hide melonia
    show anon:
        unflip
        xoffset 500
    with dissolve
    melonia "Selamat bersenang-senang!"

    show anon f_surprised_high
    pause
    show anon f_grin with {'master': dissolve}:
        flip
        xoffset 0
    anon f_grin @ -m_talk "( Hmm, telanjang {b}Melonia{/b}... )"

    anon f_flirt @ -m_talk "(Kau tahu, beberapa jam adalah waktu yang lama... Mungkin aku bisa saja-)"

    pause
    anon f_hurt @ -m_talk "(TIDAK! TIDAK! TIDAK!)"

    anon @ -m_talk "( Ayo, {b}[firstname]{/b}, fokus! )"

    anon f_angry @ -m_talk "(Saya di sini untuk mencari bukti dan mendapatkan keadilan bagi {b}Ayah{/b}. )"

    anon @ -m_talk "( Ayo {b}masuk ke sana dan temukan{/b}! )"

    hide anon with dissolve

    $ player.go_to(L_rump_lobby)
    $ L_rump_office.unlock()
    $ M_anon.trigger(T_ano20_init)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
