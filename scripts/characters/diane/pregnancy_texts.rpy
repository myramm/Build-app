label diane_pregnant_announcement_1:
    scene expression player.location.background_blur
    show player 9 with dissolve
    player_name "Hmm?"

    player_name "Saya mendapat SMS dari {b}Diane{/b}!"

    hide player with dissolve
    return

label diane_pregnant_announcement_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show player 12 with dissolve
    player_name "Aku ingin tahu apa yang terjadi?"

    player_name "Aku harus {b} mampir ke gudang Diane dan melihat ada apa{/b}."

    if player.location != L_map:
        hide player with dissolve
    return

label diane_pregnant_labor_1:
    scene expression player.location.background_blur
    show player 14 with dissolve
    player_name "Sepertinya aku mendapat pesan teks."

    hide player with dissolve
    return

label diane_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_shock with dissolve
    anon "Bayinya akan lahir!"

    anon f_surprised_teeth @ f_shock "Sialan!"

    pause
    anon f_shock "Sebaiknya saya {b}pergi ke rumah sakit untuk memeriksanya{/b}!"

    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
