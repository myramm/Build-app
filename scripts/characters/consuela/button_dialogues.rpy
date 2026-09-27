label button_consuela_intro:
    show player 10 at left
    show consuela
    with dissolve
    player_name "Halo, {b}Consuela{/b}."

    show player 5
    show consuela f_unsure
    consuela "Halo, {b}Tuan [firstname]{/b}."

    show consuela f_normal
    show player 12
    player_name "Anda cukup menghubungi saya {b}[firstname]{/b}..."

    show player 5
    show consuela f_unsure
    consuela "Apa?"

    consuela "Tidak ada bahasa Inggris."

    show consuela f_normal
    show player 10
    player_name "Oh, uhh..."

    show player 5
    pause
    consuela @ -m_talk "..."
    show player 3 with dissolve
    player_name "..."
    show consuela f_unsure
    consuela "Ehh... aku bersih-bersih sekarang."

    consuela "ya?"

    show consuela f_normal
    show player 10 with dissolve
    player_name "Oh ya."

    player_name "Eh, maksudku... Ya!"

    show player 14
    player_name "Terima kasih, {b}Consuela{/b}."

    show player 13
    consuela "Sama-sama, {b}Tuan [firstname]{/b}."

    hide player
    hide consuela
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
