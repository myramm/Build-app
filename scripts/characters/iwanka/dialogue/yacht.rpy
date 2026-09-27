label iwanka_button_yacht:
    show anon b_onbed_back with dissolve:
        flip
        offset (100, 110)
    iwanka "Hei, kamu berhasil!"

    show iwanka f_excited
    anon "Ya."

    iwanka "Tarik kursi."

    iwanka "Siapkan minuman untuk dirimu sendiri."

    pause
    iwanka f_smirk "Kecuali Anda siap untuk beralih ke aktivitas yang lebih berat?"


    menu iwanka_button_yacht.choice:
        "Kamu terlihat sangat seksi...":
            jump iwanka_button_yacht.sexy
        "Kapal pesiar ini luar biasa!":

            jump iwanka_button_yacht.yacht
        "Seks oral.":

            jump iwanka_button_yacht.blowjob
        "Seks.":

            jump iwanka_button_yacht.suggest
        "Saya tidak bisa tinggal.":

            pass

    anon f_normal "Saya tidak bisa tinggal."

    iwanka f_pouting "Tunggu, kamu sudah berangkat?!"

    anon "Ya, maaf..."

    iwanka "Tapi aku benar-benar akan melompati tulangmu!"

    anon "Mungkin lain kali."

    iwanka f_sad "Aduh..."

    hide anon with dissolve
    return


label iwanka_button_yacht.blowjob:
    anon f_normal "Bolehkah memberiku pekerjaan pukulan?"

    iwanka f_smirk "Sebuah pekerjaan pukulan?"

    iwanka "Baiklah, menurutku itu adil setelah semua yang telah kamu lakukan untukku."

    hide iwanka with dissolve
    show anon f_flirt_grin with {'master': dissolve}:
        unflip
        xoffset 650
    iwanka "Ayolah!"

    hide anon with {'master': fastdissolve}
    anon "Tepat di belakangmu!"


    scene expression background(512, 344, 3, l=L_boat_cabin) as stage
    show iwanka b_magic f_smirk
    with fade
    show anon f_flirt with dissolve
    if M_iwanka.outfit.get == 'swimsuit':
        show iwanka a_undress b_swimsuit with dissolve
        pause
        show anon f_flirt_low
        show iwanka b_swimsuit_undress2
        with dissolve
        pause
        show iwanka b_naked a_undress_swimsuit3 with dissolve
        pause
        show anon f_flirt
        show iwanka b_naked a_idle
        with dissolve
    else:
        show iwanka b_naked
    iwanka "Heh, kenapa kamu menatapku seperti itu?"

    anon @ -m_talk "Hmm?"

    anon f_shy "T-tidak ada, aku hanya-"

    pause
    anon f_flirt "Kamu benar-benar seksi."

    iwanka @ f_eyeroll "Hmm, ya."

    iwanka a_hip "Apakah kita melakukan ini atau apa?"

    anon "Ya, tolong."

    iwanka "Kalau begitu, silakan duduk."

    anon "Y-ya, oke."


    call scene_iwanka_blowjob.yacht
    $ unlock_scene('iwanka', '01_unlocked', variant='yacht')

    scene expression background(512, 344, 3, l=L_boat_cabin) as stage
    show iwanka b_naked o_cum f_smirk
    show anon f_flirt
    with fade
    anon "Terima kasih telah melakukan itu."

    iwanka "Tidak masalah."

    iwanka @ f_laugh "Itu menyenangkan!"

    pause
    iwanka "Sekarang, permisi..."

    iwanka "... Aku akan membersihkan diriku sendiri."

    anon "Y-ya, tentu saja."

    anon @ a_wave "Sampai jumpa nanti."

    iwanka "Sampai jumpa, {b}[firstname]{/b}."

    hide anon with dissolve
    return 'afterglow'


label iwanka_button_yacht.sex:
    iwanka f_excited @ f_laugh "Tentu saja!"

    hide iwanka with dissolve
    show anon f_surprised with {'master': dissolve}:
        unflip
        xoffset 650
    iwanka "Apa yang kamu tunggu? Undangan?"

    hide anon with {'master': fastdissolve}
    anon "!!!"

    scene expression background(240, 344, 3, l=L_boat_cabin) as stage
    show iwanka b_magic f_smirk
    with fade
    show anon f_flirt with dissolve
    show iwanka b_swimsuit a_undress f_smirk_down
    show anon b_dressed_changing3
    with dissolve
    pause
    show iwanka b_swimsuit_undress2
    show anon b_dressed_changing2
    with dissolve
    pause
    show iwanka b_naked a_undress_swimsuit3
    show anon b_naked_undress_bottom
    with dissolve
    pause
    show iwanka b_naked a_hip f_smirk
    show anon b_naked od_naked_dick1
    with dissolve
    iwanka "Pastikan saja kamu benar-benar meniduriku kali ini!"

    iwanka "Dan mungkin membuatku sedikit tersedak."

    anon f_surprised "Hah?!"

    show anon b_empty od_empty:
        xoffset 300
        unflip
    show iwanka b_naked_pulling_anon behind anon:
        unflip
        xoffset 300
    with dissolve
    iwanka "Ayolah!"

    anon "A-wah, tunggu sebentar!"


    call scene_iwanka_sex.yacht
    $ unlock_scene('iwanka', '02_unlocked', variant='yacht')

    scene location_boat_interior_bed_closeup
    show iwanka b_onbed_cuddle_naked f_content_closed
    show anon b_empty f_flirt_low:
        xzoom -1
        offset (84, -17)
    show anon_overlay_dick_onbed_naked_od_dick1
    with fade
    iwanka "Hmm, bagus sekali!"

    anon "Y-ya, kamu juga."

    pause
    show iwanka f_excited_up
    iwanka "Saya yakin Anda senang Anda datang ke sini sekarang, ya?"

    anon "Ya, sangat senang!"

    iwanka @ f_laugh "hehe!"

    iwanka f_content_closed "Kau tahu, kau bisa jalan-jalan sebentar..."

    iwanka "... Jika kamu mau."

    anon "Oh?"

    iwanka "Ya, aku suka berbaring di sini bersamamu."

    iwanka "Itu ummm, entahlah..."

    anon "Bagus?"

    iwanka @ f_excited_up "... Ya."

    iwanka "Bagus."

    anon "Baiklah, tapi hanya sebentar."

    iwanka "Mm, oke."

    pause
    iwanka "Terima kasih, {b}[firstname]{/b}."


    scene expression background(512, 344, 3, l=L_boat_cabin, o=1) as stage
    show anon
    show iwanka b_naked f_excited
    with slowfade
    iwanka "Itu menyenangkan!"

    anon "Ya, benar."

    hide anon
    show iwanka b_naked_kiss:
        xoffset -200
    with dissolve
    pause
    show iwanka b_naked:
        xoffset 0
    show anon f_shy
    with dissolve
    iwanka "Ayo segera lakukan lagi, oke?"

    anon "Tentu saja."

    hide anon with dissolve
    return 'afterglow'


label iwanka_button_yacht.sexy:
    anon f_flirt "Kamu terlihat sangat seksi..."

    iwanka f_smirk "Yah, aku harap begitu!"

    iwanka "Setelah semua uang yang ayahku habiskan untuk operasi plastikku..."

    anon f_surprised_low "Anda pernah menjalani operasi plastik?!"

    iwanka "Tiga kali."

    pause
    iwanka @ f_thinking "Hmm, empat jika kamu menghitung payudaraku."

    anon "Kamu tampak terlalu muda untuk semua itu!"

    iwanka "Anda tidak pernah terlalu muda untuk menyempurnakan diri Anda secara visual."

    show anon f_worried_low
    pause
    iwanka "Setidaknya, itulah yang dikatakan dokter bedah plastik ayahku..."

    jump iwanka_button_yacht.choice


label iwanka_button_yacht.suggest:
    anon f_flirt "Ingin melakukannya?"


    if game.timer.is_evening():
        jump iwanka_button_yacht.sex

    iwanka "Aku sedang berjemur sekarang... Tapi mungkin nanti, oke?"

    show anon f_sad
    pause
    jump iwanka_button_yacht.choice


label iwanka_button_yacht.yacht:
    anon f_normal "Kapal pesiar ini luar biasa!"

    iwanka f_normal "Benar?!"

    iwanka f_excited "Saya senang berada di sini, di lautan."

    iwanka @ f_laugh "Ditambah lagi ada wifi dan TV satelit."

    anon @ f_surprised "Sialan, benarkah?"

    iwanka "Ya, ayahku mengeluarkan lebih banyak uang untuk menjadi mucikari daripada perahu itu sendiri."

    anon "Itu gila!"

    iwanka "Sistem keamanan mutakhir, perabotan mewah, dek berpemanas, bar yang terisi penuh, audio khusus berkualitas teater..."

    iwanka "... Dan ada tiang penari telanjang di sekitar sini."

    anon f_surprised "Benar-benar?"

    anon f_flirt "Saya ingin itu!"

    iwanka @ f_laugh "Hehe, saya yakin Anda akan melakukannya."

    jump iwanka_button_yacht.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
