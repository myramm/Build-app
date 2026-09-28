label grace_pregnant_announcement_1:
    scene expression player.location.background_blur
    show anon f_looking_down with dissolve
    anon @ -m_talk "Hmm?"
    anon @ f_laugh a_cheering "I've got a text from someone!"
    hide anon with dissolve
    return

label grace_pregnant_announcement_2:
    scene expression player.location.background_blur
    if M_grace.pregnancy.first_baby:
        if player.location != L_map:
            show anon f_worried with dissolve
        anon "{b}Grace{/b} is sending me texts now?"
        anon "And she seems really worried about something..."
        anon "I should {b}swing by Eve's place and find out what's going on{/b}."
    else:
        if player.location != L_map:
            show anon with dissolve
        anon "{b}Grace{/b} is sending me texts again."
        anon "I should {b}swing by Eve's place and find out what's going on{/b}."
    if player.location != L_map:
        hide anon with dissolve
    return

label grace_pregnant_labor_1:
    scene expression player.location.background_blur
    show anon f_looking_down with dissolve
    anon @ -m_talk "Hmm?"
    anon @ f_laugh a_cheering "I've got a text from someone!"
    hide anon with dissolve
    return

label grace_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_shock with dissolve
    anon "{b}Grace{/b} had the baby?!"
    anon "Holy crap!"
    pause
    anon f_surprised "I'd better {b}head to the hospital to check on them{/b}."
    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
