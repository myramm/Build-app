label jenny_pregnant_announcement_1:
    scene expression player.location.background_blur with None
    show anon f_looking_down a_phone
    anon @ -m_talk "Hmm?"

    anon f_shock_down @ -m_talk "Saya mendapat SMS dari {b}[jen_name]{/b}!"

    hide anon with dissolve
    return

label jenny_pregnant_announcement_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_worried a_phone with dissolve
    anon "Aku ingin tahu apa yang terjadi?"

    anon "Saya harus {b} mampir ke kamar [jen_name] dan melihat ada apa{/b}?"

    if player.location != L_map:
        hide anon with dissolve
    return

label jenny_pregnant_labor_1:
    scene expression player.location.background_blur
    show anon f_normal with dissolve
    anon "Sepertinya aku mendapat pesan teks."

    hide anon with dissolve
    return

label jenny_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_shock with dissolve
    anon @ -m_talk "{b}[jen_name]{/b} punya bayinya?!"

    anon @ -m_talk "Sialan!"

    pause
    anon f_worried "Sebaiknya saya pergi ke {b}klinik{/b} untuk memeriksanya."

    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
