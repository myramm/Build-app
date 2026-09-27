label dewitt_dialogue_dress_code:
    hide player
    show anon f_worried:
        flip
    anon "Sebenarnya, saya ingin berbicara dengan Anda tentang {b}Nyonya. Smith{/b}..."

    show dewitt 11b with dissolve
    dewitt "{i}*Sigh*{/i} Apa yang telah dilakukan wanita bodoh itu sekarang?"

    show dewitt 10b
    anon "Dia meminta {b}Annie{/b} menerapkan kebijakan aturan berpakaian yang baru, dan saya berharap Anda dapat berbicara dengannya tentang perubahan kebijakan tersebut?"

    show dewitt 11b
    dewitt "Ya ampun, percayalah, tidak ada yang lebih kucintai selain memberikan sedikit pikiranku pada wanita tua itu..."

    dewitt "... Tapi dia sudah memotong anggaran musikku sedemikian rupa sehingga pada dasarnya tidak ada!"

    dewitt "Jika saya menimbulkan masalah karena aturan berpakaian, siapa yang tahu apa yang akan terjadi?"

    show dewitt 10b
    anon "Y-ya, aku mengerti."

    show dewitt 2 with dissolve
    dewitt "Apakah Anda mencoba bertanya kepada guru lain?"

    show dewitt 1
    anon "aku akan bertanya pada mereka."

    show dewitt 2
    dewitt "Saya yakin salah satu dari mereka akan membantu Anda."

    show dewitt 1
    anon f_normal "Terima kasih, {b}Nona Dewitt{/b}."

    show dewitt 2
    dewitt "Semoga beruntung, gula."

    show dewitt 1
    hide anon with dissolve
    return

label dewitt_dialogue_dewitt_eve_meet_up:
    scene music_classroom_c
    show player 10 with dissolve
    player_name "Saya harus memberinya ruang untuk saat ini."

    player_name "Dan saya juga harus {b}mengunjungi Eve di taman pada malam hari{/b}."

    return

label dewitt_dialogue_dewitt_science_adhesive:
    scene music_classroom_c
    show player 17 with dissolve
    player_name "{b}Kevin{/b} akan membuat perekat di kelas {b}Nona Okita{/b}."

    player_name "Aku harus melihat apa yang dia lakukan."

    return

label dewitt_dialogue_dewitt_school_sneak_mission_help:
    scene music_classroom_c
    show player 10 with dissolve
    player_name "Mungkin {b}Erik{/b} akan membantuku {b}menyelinap ke sekolah malam ini{/b}."

    return

label dewitt_dialogue_dewitt_office_night_visit_delay:
    scene music_classroom_c
    show player 13 at left
    show dewitt 19f at right
    with dissolve
    dewitt "Ingat, aku punya satu kejutan lagi untukmu."

    hide player
    show dewitt 6f at left
    with dissolve
    dewitt "Anda harus datang ke kantor saya {b}besok{/b} sepulang sekolah jika Anda menginginkannya..."

    show player 29 at left
    show dewitt 18f at Position (xpos=300)
    with dissolve
    player_name "O-oke..."

    player_name "Saya akan berada di sana."

    show player 13 with dissolve
    show dewitt 19f
    dewitt "Hmm, aku tidak sabar!"

    dewitt "Sampai jumpa, {b}[firstname]{/b}."

    hide dewitt with dissolve
    show player 18
    player_name "..."
    return

label dewitt_dialogue_dewitt_office_night_visit:
    scene music_classroom_c
    show player 13 at left
    show dewitt 19f at right
    with dissolve
    dewitt "Ingat, aku punya satu kejutan lagi untukmu."

    hide player
    show dewitt 6f at left
    with dissolve
    dewitt "Kamu harus datang ke kantorku sepulang sekolah jika kamu menginginkannya..."

    show player 29 at left
    show dewitt 18f at Position (xpos=300)
    with dissolve
    player_name "O-oke..."

    player_name "Saya akan berada di sana."

    show player 13 with dissolve
    show dewitt 19f
    dewitt "Hmm, aku tidak sabar!"

    dewitt "Sampai jumpa, {b}[firstname]{/b}."

    hide dewitt with dissolve
    show player 18
    player_name "..."
    return

label dewitt_dialogue_dewitt_end:
    scene music_classroom_c
    show player 13f at right
    show dewitt 2 at left
    with dissolve
    dewitt "Terima kasih sekali lagi untuk semuanya, sayang!"

    show dewitt 1
    show player 14f
    player_name "Dengan senang hati, {b}Nona Dewitt{/b}."

    show player 13f
    show dewitt 19 with dissolve
    dewitt "Ingat, pintuku selalu terbuka untukmu."

    show dewitt 18
    show player 17f
    player_name "Ya, Bu."

    return

label dewitt_dialogue_intro:
    scene music_classroom_c
    show dewitt 1 at left
    show player 2f at right
    player_name "Hai, {b}Nona Dewitt{/b}."

    show dewitt 2
    show player 1f
    dewitt "Halo, {b}[firstname]{/b}!"

    dewitt "Siap bergabung bersama kami hari ini?"

    show dewitt 1
    show player 33f
    player_name "Tentu saja!"

    show dewitt 2
    show player 13f
    dewitt "Apakah ada sesuatu yang ingin Anda bicarakan?"

    show dewitt 1
    show player 34f
    return

label dewitt_dialogue_dewitt_find_flute:
    show player 10f
    player_name "Di mana saya harus mulai mencari seruling?"

    show player 5f
    show dewitt 2
    dewitt "Apakah Anda {b}memeriksa lembar pembayaran instrumen di loker kelas{/b}?"

    show dewitt 1
    show player 14f
    player_name "Oh ya!"

    player_name "Saya akan mencari petunjuk di sana!"

    show player 13f
    show dewitt 2
    dewitt "Sampai jumpa, gula!"

    return

label dewitt_dialogue_dewitt_make_new_flute:
    show player 10f
    player_name "Tentang seruling-"

    show player 11f
    show dewitt 2
    dewitt "Apakah Anda {b}menemukan serulingnya{/b}?"

    show dewitt 1
    show player 3f at Position (xoffset=-8) with dissolve
    player_name "..."
    show player 10f with dissolve
    player_name "Belum."

    show player 5f
    show dewitt 2
    dewitt "Saya harap itu tidak hilang."

    show dewitt 1
    show player 14f
    player_name "Jangan khawatir! Saya ikut!"

    show player 13f
    show dewitt 2
    dewitt "Terima kasih, {b}[firstname]{/b}!"

    hide dewitt with dissolve
    show player 4f with dissolve
    player_name "( {b}Erik{/b} bilang aku seharusnya bisa membuatnya. )"

    return

label dewitt_dialogue_talent_show_help:
    show player 10f
    player_name "Berapa banyak orang yang Anda butuhkan untuk pertunjukan bakat lagi?"

    show player 5f
    show dewitt 5
    dewitt "Saya berharap setidaknya {b}dua lagi{/b}."

    dewitt "Kurang dari itu dan saya khawatir kami harus membatalkannya."

    show dewitt 4
    show player 14f
    player_name "Baiklah, jangan khawatir, {b}Nona Dewitt{/b}! Aku akan mencari seseorang!"

    show player 13f
    show dewitt 5
    dewitt "Ah terima kasih, gula!"

    return

label dewitt_dialogue_leave:
    show player 10f
    player_name "Tidak juga..."

    player_name "Hanya berharap aku bisa mengejar ketinggalan."

    show dewitt 2
    show player 5f
    dewitt "Oh sayang. Kamu akan baik-baik saja!"

    show player 13f
    dewitt "Pilih instrumen dan duduklah!"

    dewitt "Kami akan membawa Anda kembali ke jalurnya..."

    show dewitt 1
    show player 14f
    player_name "Terima kasih, {b}Nona Dewitt{/b}..."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
