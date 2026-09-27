label kevin_gym_take_it_easy:
    show player 14
    player_name "Aku akan keluar dari sini kawan."

    show player 13
    show old_kevin 11b with dissolve
    kevin "Sudah, kawan?"

    show old_kevin 11c
    show player 14
    player_name "Ya, aku punya beberapa hal lain yang perlu kulakukan."

    show player 13
    show old_kevin 9 with dissolve
    kevin "Ah, baiklah."

    show old_kevin 8
    show player 14
    player_name "Sampai jumpa lagi, {b}Kevin{/b}."

    hide old_kevin
    hide player
    with dissolve
    return

label kevin_gym_lets_lift:
    show player 14
    player_name "Ayo angkat saja."

    show player 13
    show old_kevin 9
    kevin "Oh, Anda siap memompa setrika?"

    show old_kevin 10 with dissolve
    kevin "Langsung saja, kawan."

    kevin "Ayo lakukan ini!"

    hide old_kevin
    hide player
    with dissolve
    return

label kevin_gym_intro:
    scene expression background(0, 440, 2.5) as stage
    show player 13 at left
    show old_kevin 9 at right
    with dissolve
    kevin "Hei kawan!"

    show old_kevin 8
    show player 14
    player_name "Ada apa, {b}Kevin{/b}?"

    show player 13
    show old_kevin 9
    kevin "Saya telah melatih otot bokong saya sepanjang pagi!"

    show old_kevin 13b with dissolve
    kevin "Rasakan betapa ketatnya anak-anak nakal ini!"

    show player 10b with dissolve
    player_name "Eh, tidak, terima kasih..."

    show player 5b
    kevin "Anda yakin, kawan?"

    kevin "Anda tidak tahu apa yang Anda lewatkan!"

    show old_kevin 8 with dissolve
    show player 29 with dissolve
    player_name "Hehe."

    show player 5 with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
