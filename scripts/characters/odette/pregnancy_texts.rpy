label odette_pregnant_announcement_1:
    scene expression player.location.background_blur
    show anon f_looking_down with dissolve
    anon a_phone @ -m_talk "Hmm?"
    anon f_normal "I've got a text from {b}Eve{/b}!"
    hide anon with dissolve
    return

label odette_pregnant_announcement_2:
    scene expression player.location.background_blur
    if M_odette.pregnancy.first_baby:
        if player.location != L_map:
            show anon f_surprised with dissolve
        anon "{b}Odette{/b} is pregnant?"
        anon "Could it be mine?"
        anon "{b}I should probably swing by Eve's place and find out{/b}."
    else:
        if player.location != L_map:
            show anon f_shock with dissolve
        anon "{b}Odette{/b} is pregnant?"
        anon "Could it be mine?"
        anon f_surprised "{b}I should probably swing by Eve's place and find out{/b}."
    if player.location != L_map:
        hide anon with dissolve
    return

label odette_pregnant_labor_1:
    scene expression player.location.background_blur
    show anon f_looking_down with dissolve
    anon a_phone @ -m_talk "Hmm?"
    anon f_normal "I've got a text from {b}Eve{/b}!"
    hide anon with dissolve
    return

label odette_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_shock with dissolve
    anon "{b}Odette{/b} had the baby?!"
    anon f_surprised "Holy crap!"
    pause
    anon "I'd better {b}head to the hospital to check on them{/b}."
    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
