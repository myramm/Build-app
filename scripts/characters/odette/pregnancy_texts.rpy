label odette_pregnant_announcement_1:
    scene expression player.location.background_blur
    show anon f_looking_down with dissolve
    anon a_phone @ -m_talk "Hmm?"

    anon f_normal "Saya mendapat SMS dari {b}Eve{/b}!"

    hide anon with dissolve
    return

label odette_pregnant_announcement_2:
    scene expression player.location.background_blur
    if M_odette.pregnancy.first_baby:
        if player.location != L_map:
            show anon f_surprised with dissolve
        anon "{b}Odette{/b} sedang hamil?"

        anon "Mungkinkah itu milikku?"

        anon "{b}Saya mungkin harus mampir ke tempat Eve dan mencari tahu{/b}."

    else:
        if player.location != L_map:
            show anon f_shock with dissolve
        anon "{b}Odette{/b} sedang hamil?"

        anon "Mungkinkah itu milikku?"

        anon f_surprised "{b}Saya mungkin harus mampir ke tempat Eve dan mencari tahu{/b}."

    if player.location != L_map:
        hide anon with dissolve
    return

label odette_pregnant_labor_1:
    scene expression player.location.background_blur
    show anon f_looking_down with dissolve
    anon a_phone @ -m_talk "Hmm?"

    anon f_normal "Saya mendapat SMS dari {b}Eve{/b}!"

    hide anon with dissolve
    return

label odette_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_shock with dissolve
    anon "{b}Odette{/b} punya bayi?!"

    anon f_surprised "Sialan!"

    pause
    anon "Sebaiknya saya {b}pergi ke rumah sakit untuk memeriksanya{/b}."

    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
