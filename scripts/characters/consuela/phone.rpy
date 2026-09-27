label consuela_pregnant_announcement_1:
    scene expression player.location.background_blur
    show anon f_looking_down a_phone with dissolve
    anon @ -m_talk "Hmm?"

    anon f_shock_down @ -m_talk "(Saya mendapat SMS dari {b}Consuela{/b}?! )"

    hide anon with dissolve
    return

label consuela_pregnant_announcement_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_worried a_phone with dissolve
    anon "Apa yang sedang terjadi?"

    anon "{b}Saya mungkin harus pergi dan memeriksanya{/b}."

    if player.location != L_map:
        hide anon with dissolve
    return

label consuela_pregnant_labor_1:
    scene expression player.location.background_blur
    show anon f_normal with dissolve
    anon "Sepertinya aku mendapat pesan teks."

    hide anon with dissolve
    return

label consuela_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_shock a_phone with dissolve
    anon "Itu pasti bayinya!"

    anon "{b}Saya harus pergi ke klinik dan memeriksanya{/b}."

    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
