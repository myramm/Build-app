label angelica_dialogue_ross_get_linens_pre:
    scene church_c
    show player 1 at left
    show ang 1 at right
    with dissolve
    return

label angelica_dialogue_ross_get_linens:
    show player 2
    player_name "Umm, aku sedang mengerjakan proyek seni untuk sekolah, dan kami memerlukan beberapa linen putih."

    player_name "Temanku {b}Mia{/b} bilang kamu mungkin bersedia menyisihkan sedikit."

    show player 1
    show ang 2
    angelica "Hmm, {b}Mia{/b} mengirimmu?"

    angelica "Dia seorang wanita muda yang taat."

    angelica "Saya kira saya bisa memberi Anda beberapa jubah baptisan kami yang lama. Lagi pula, mereka sedang bergejolak..."

    show player 2
    show ang 1
    player_name "Itu seharusnya bekerja dengan baik! Terima kasih banyak."

    show player 1
    show ang 2
    angelica "Jika Anda ingin berterima kasih kepada saya, mulailah datang ke kebaktian pada hari Minggu."

    show player 11
    show ang 1
    player_name "..."
    show ang 2
    angelica "Sekarang tunggu di sini sementara aku pergi mengambilnya."

    hide ang
    with dissolve
    show player 10
    player_name "Hah, itu mudah."

    show player 11
    player_name "..."
    show player 10
    player_name "Saya pikir pasti dia menginginkan sesuatu sebagai balasannya..."

    show player 11
    pause
    show ang 40 at right with dissolve
    pause
    show ang 41
    angelica "Ini dia."

    show ang 2
    show player 592
    with dissolve
    angelica "Beritahu {b}Mia{/b} Saya berharap bisa menemuinya lebih awal untuk kebaktian berikutnya! Dia sudah lama terlambat untuk mengaku dosa."

    show player 593
    show ang 1
    player_name "O-oke, aku akan memberitahunya."

    show player 592
    angelica "Hmm!"

    hide ang
    hide player
    show player 591 at Position (xpos=0.25, ypos=1.0)
    with dissolve
    player_name "... {b}Mia{/b} mungkin akan menanggung akibatnya dalam hal ini."

    player_name "Sebaiknya saya mengembalikan {b}Seprai{/b} ini ke {b}Nona Ross{/b}."

    return

label angelica_dialogue_change_pre:
    scene church_c with fade
    show player 10 at left
    show ang 1 at right
    with dissolve
    player_name "Hai, {b}Suster Angelica{/b}."

    show player 5
    show ang 2
    angelica "Kamu lagi."

    angelica "Apa yang kamu inginkan?"

    show ang 1
    return

label angelica_dialogue_change_talk:
    show player 10
    player_name "Saya hanya ingin bicara."

    show player 5
    show ang 2
    angelica "Diam."

    show ang 1
    show player 24
    player_name "Oh..."

    show ang 2
    angelica "Jika kamu ingin bicara, datanglah mengunjungiku pada malam hari di kamarku..."

    show ang 1
    show player 25
    player_name "Oke, kalau begitu. Maaf."

    hide player
    hide ang
    with dissolve
    return

label angelica_dialogue_change_graveyard:
    show player 10
    player_name "Bagaimana Anda mengakses kuburan?"

    show player 5
    show ang 2
    angelica "Itu terlarang."

    angelica "Meskipun terkunci, anak-anak nakal terus mencari cara untuk {b}menyelinap melalui pagar{/b}."

    show ang 1
    show player 12
    player_name "Tapi ayahku dimakamkan di sana."

    show player 5
    angelica "..."
    show ang 2
    angelica "Saya yakin dia benar."

    show ang 1
    show player 12
    player_name "Tapi-"

    show player 16
    show ang 2
    angelica "Pergi. Anda membuang-buang waktu saya."

    hide ang
    hide player
    show player 16
    with dissolve
    player_name "..."
    show player 12
    player_name "Mungkin saya bisa menemukan {b}jalan melewati pagar{/b} juga."

    hide player with dissolve
    return

label angelica_dialogue_change_leave:
    show player 10
    player_name "Sudahlah. Saya harus pergi."

    show player 5
    angelica "..."
    show ang 2
    angelica "Jangan buang waktuku seperti itu lagi."

    show ang 1
    show player 25
    player_name "Kamu benar, aku minta maaf..."

    hide player
    hide ang
    with dissolve
    return

label angelica_dialogue_pre:
    scene church_c
    show ang 2 at right
    show player 1 at left
    with dissolve
    angelica "Apakah Anda dari paroki ini, anak muda?"

    show ang 1
    show player 14
    player_name "Hai, aku sedang-"

    show ang 2
    show player 11
    angelica "Apakah Anda dari paroki ini, anak muda?"

    show ang 1
    show player 14
    player_name "Uhh... Tidak juga."

    show ang 2
    show player 11
    angelica "Apakah Anda percaya pada Tuhan?"

    show ang 1
    show player 10
    player_name "Ya..."

    show ang 2
    show player 11
    angelica "Saya minta maaf."

    angelica "Saya hanya bisa membantu mereka yang memiliki iman yang sama dengan Tuhan kita!"

    hide player
    hide ang
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
