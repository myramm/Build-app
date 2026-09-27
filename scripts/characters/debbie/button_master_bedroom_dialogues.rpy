label debbie_dialogue_master_room_pre:
    scene debbie_bedroom_closeup2
    show old_debbie 55 at left
    show player 110 at right
    with dissolve
    debbie "Hai sayang..."

    debbie "Apakah kamu mencariku?"

    show old_debbie 54
    show player 111
    player_name "Ya..."

    show player 110
    show old_debbie 55
    debbie "Apakah ada sesuatu yang kamu inginkan dariku?"

    show old_debbie 54
    return

label debbie_dialogue_master_room_after_kiss_dialogue:
    debbie "Sekarang, apakah ada hal lain yang Anda inginkan?"

    show old_debbie 54
    return

label debbie_dialogue_master_room_kiss:
    show player 111 at right
    show old_debbie 54 at left
    player_name "Bolehkah aku berciuman?"

    show player 110
    show old_debbie 55
    debbie "Tentu saja sayang! Kemarilah."

    scene debbie_bedroom
    show old_debbie 79
    with fade
    debbie "Mmmm..."

    show old_debbie 80_79
    pause 3
    show old_debbie 75 at Position(xpos=750)
    show player 227 at Position(xpos=200)
    with fastdissolve
    debbie "Anda menjadi lebih baik dalam hal ini!"

    scene debbie_bedroom_closeup2
    show old_debbie 55 at left
    show player 110 at right
    with fade
    return

label debbie_dialogue_master_room_shower:
    show player 111
    player_name "Hai, {b}[deb_name]{/b}!"

    player_name "Mau mandi bersamaku?"

    show player 110
    show old_debbie 55
    debbie "Cuaca di rumah mulai panas..."

    debbie "Tentu! Mandi terdengar menyenangkan saat ini."

    debbie "Silakan saja, sayang. Aku akan ke sana sebentar lagi."

    scene shower_closeup
    show debbies 27
    with dissolve
    pause
    show debbies 28 at Position(xpos=487,ypos=768) with dissolve
    pause
    show debbies 34 with dissolve
    debbie "Maaf membuatmu menunggu, sayang..."

    return

label debbie_dialogue_master_room_sex_random_true:
    show old_debbie 54 at left
    show player 111 at right
    player_name "Aku merasa seperti... Melakukannya lagi denganmu."

    show player 110
    show old_debbie 55
    debbie "Tidak apa-apa!"

    debbie "Aku berharap kamu ingin..."

    show player 111
    show old_debbie 54
    player_name "Benar-benar?"

    show player 110
    show old_debbie 58 with dissolve
    debbie "Tentu saja! Bagaimanapun, kamu adalah laki-lakiku."

    show old_debbie 57
    player_name "!!!"
    show old_debbie 58
    debbie "Buka bajumu, sayang."

    show old_debbie 57
    show player 8f
    pause
    show player 261
    pause
    show player 263
    pause
    show old_debbie 103
    debbie "Mmm, ayo jemput aku, sayang!"

    show player 262 at right
    show old_debbie 102 at left
    player_name "Tak perlu memberitahuku dua kali..."

    return

label debbie_dialogue_master_room_sex_random_false:
    show old_debbie 54 at left
    show player 111 at right
    player_name "{b}[deb_name]{/b}, ingin bersenang-senang?"

    show player 110
    show old_debbie 54
    debbie "Oh?"

    show old_debbie 56 with dissolve
    debbie "Seperti... Ini menyenangkan?"

    show old_debbie 57
    show player 111
    player_name "Tentu saja..."

    show player 110
    show old_debbie 58
    debbie "Biarkan aku melihat ayammu itu..."

    show old_debbie 57
    show player 8f with dissolve
    pause
    show old_debbie 101
    show player 261 with dissolve
    pause
    show player 263 with dissolve
    pause
    show old_debbie 58
    debbie "Sepertinya Anda siap!"

    show old_debbie 57
    show player 262
    player_name "Aku sudah menantikan ini sejak aku bangun pagi ini."

    show player 263
    show old_debbie 58
    debbie "Saya juga."

    show old_debbie 102 with dissolve
    pause
    show old_debbie 103
    debbie "Datang dan ambillah, sayang."

    return

label debbie_dialogue_master_room_sex_after:
    hide player
    show old_debbie 104 at left
    with dissolve
    pause
    hide old_debbie
    hide player
    with dissolve
    scene debbie_bedroom_closeup_sex
    return

label debbie_dialogue_master_room_laundry_sex:
    show old_debbie 54
    show player 111
    player_name "Saya ingin tahu apakah Anda memerlukan bantuan di ruang bawah tanah."

    show player 110
    show old_debbie 55
    debbie "Di ruang bawah tanah? Untuk apa?"

    show player 111
    show old_debbie 54
    player_name "Mungkin saya bisa membantu Anda mencuci pakaian... Seperti yang kita lakukan terakhir kali?"

    show player 110
    show old_debbie 55
    debbie "Oh, begitu... Saya tahu persis apa yang Anda inginkan!"

    debbie "Beri aku waktu sebentar untuk bersiap."

    debbie "aku akan menemuimu di sana..."

    hide old_debbie
    hide player
    with dissolve
    return

label debbie_dialogue_master_room_watch_movie:
    show player 111
    player_name "Saya berpikir, kita harus menonton film lagi malam ini. Tertarik?"

    show player 110
    show old_debbie 55
    debbie "Mmm, nonton film malam, ya?"

    debbie "Kedengarannya itu ide yang bagus, sayang!"

    show player 111
    show old_debbie 54
    player_name "Luar biasa!"

    player_name "Kalau begitu, sampai jumpa malam ini di ruang tamu?"

    show player 110
    show old_debbie 55
    debbie "Saya tidak sabar..."

    return

label debbie_dialogue_master_room_leave:
    show old_debbie 54
    show player 111
    player_name "Tidak ada, {b}[deb_name]{/b}."

    player_name "Hanya ingin menyapa."

    show player 110
    show old_debbie 55
    debbie "Oh oke..."

    debbie "Baiklah, kembalilah jika kamu mau... Aku sedikit bosan..."

    debbie "Kita bisa bersenang-senang kapan saja kamu mau."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
