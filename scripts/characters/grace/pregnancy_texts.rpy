label grace_pregnant_announcement_1:
    scene expression player.location.background_blur
    show anon f_looking_down with dissolve
    anon @ -m_talk "Hmm?"

    anon @ f_laugh a_cheering "Aku mendapat pesan dari seseorang!"

    hide anon with dissolve
    return

label grace_pregnant_announcement_2:
    scene expression player.location.background_blur
    if M_grace.pregnancy.first_baby:
        if player.location != L_map:
            show anon f_worried with dissolve
        anon "{b}Grace{/b} mengirimiku SMS sekarang?"

        anon "Dan dia sepertinya sangat khawatir tentang sesuatu..."

        anon "Aku harus {b}mampir ke tempat Eve dan mencari tahu apa yang terjadi{/b}."

    else:
        if player.location != L_map:
            show anon with dissolve
        anon "{b}Grace{/b} mengirimiku SMS lagi."

        anon "Aku harus {b}mampir ke tempat Eve dan mencari tahu apa yang terjadi{/b}."

    if player.location != L_map:
        hide anon with dissolve
    return

label grace_pregnant_labor_1:
    scene expression player.location.background_blur
    show anon f_looking_down with dissolve
    anon @ -m_talk "Hmm?"

    anon @ f_laugh a_cheering "Aku mendapat pesan dari seseorang!"

    hide anon with dissolve
    return

label grace_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_shock with dissolve
    anon "{b}Grace{/b} punya bayinya?!"

    anon "Sialan!"

    pause
    anon f_surprised "Sebaiknya saya {b}pergi ke rumah sakit untuk memeriksanya{/b}."

    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
