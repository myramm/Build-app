label dewitt_dialogue_lounge_intro:
    scene location_school_lounge_couch
    show player 10 at left
    show dewittl 5 at right
    with dissolve
    pause
    show dewittl 1 with dissolve
    player_name "Oh, hai, {b}Nona Dewitt{/b}."

    show player 11
    show dewittl 3 with dissolve
    dewitt "{b}[firstname]{/b}? Kamu tidak seharusnya berada di sini..."

    show player 10
    show dewittl 2
    player_name "Ya maaf."

    show player 2
    player_name "{b}Nona Ross{/b} menyuruh saya mencari majalah lama."

    player_name "Kami sedang membuat kolase!"

    show player 1
    show dewittl 3
    dewitt "Kolase, ya?"

    dewitt "Saya selalu membuatnya ketika saya masih muda!"

    show player 2
    show dewittl 2
    player_name "Apa yang sedang kamu camilan?"

    show player 1
    show dewittl 3b at Position(xpos=0.965, ypos=1.0) with dissolve
    dewitt "Oh ini?"

    show dewittl 3 at right with dissolve
    dewitt "Ini adalah salah satu brownies {i}spesial{/i}Barbara{/b}."

    show player 2
    show dewittl 2
    player_name "Saya tidak tahu {b}Nona Ross{/b} bisa membuat kue?"

    show player 1
    show dewittl 3
    dewitt "Dia membuat brownies TERBAIK!"

    dewitt "Saya tidak pernah merasa cukup!"

    show player 2
    show dewittl 2
    player_name "... Rapi!"

    player_name "Jadi, menurut Anda apakah saya dapat menyediakan beberapa majalah itu di atas meja?"

    show player 1
    show dewittl 3
    dewitt "Saya tidak mengerti mengapa tidak."

    show player 2
    show dewittl 2
    player_name "Kagum-"

    show player 11
    show dewittl 6 with dissolve
    dewitt "Jika Anda dapat menjawab pertanyaan dari tes saya berikutnya!"

    show player 10
    show dewittl 2 with dissolve
    player_name "Benar-benar?"

    show player 11
    show dewittl 3
    dewitt "Tidak ada yang gratis dalam hidup, {b}[firstname]{/b}."

    dewitt "Sekarang mari kita lihat..."

    dewitt "Seruling termasuk dalam kelompok instrumen yang mana?"

    return

label dewitt_dialogue_lounge_stat_pass:
    show player 2 at left
    show dewittl 2 at right
    player_name "Itu mudah! Angin kayu."

    show player 1
    show dewittl 3
    dewitt "Bagus sekali, {b}[firstname]{/b}!"

    dewitt "Saya kira Anda telah memperhatikan di kelas."

    show dewittl 4 with dissolve
    dewitt "Silakan ambil majalah sebanyak yang Anda perlukan."

    show player 595 with dissolve
    show dewittl 2
    player_name "Luar biasa!"

    player_name "Terima kasih, {b}Nona Dewitt{/b}! Nikmati brownies Anda!"

    show player 594
    show dewittl 1b at Position(xpos=0.965, ypos=1.0) with dissolve
    dewitt "Oh, bagus sekali! Hmm..."

    return

label dewitt_dialogue_lounge_stat_fail:
    show player 10
    show dewittl 2
    player_name "Err... Instrumen punya keluarga?"

    show player 11
    show dewittl 3
    dewitt "Heh, itu sesuatu yang sebaiknya kau pikirkan jika kau menginginkan majalah-majalah ini."

    dewitt "Kembalilah ketika Anda tahu jawabannya."

    show dewittl 2
    show player 10
    player_name "Ah, kawan..."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
