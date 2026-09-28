label consuela_pregnant_announcement_1:
    scene expression player.location.background_blur
    show anon f_looking_down a_phone with dissolve
    anon @ -m_talk "Hmm?"
    anon f_shock_down @ -m_talk "( I've got a text from {b}Consuela{/b}?! )"
    hide anon with dissolve
    return

label consuela_pregnant_announcement_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_worried a_phone with dissolve
    anon "What the heck is going on?"
    anon "{b}I should probably go and check on her{/b}."
    if player.location != L_map:
        hide anon with dissolve
    return

label consuela_pregnant_labor_1:
    scene expression player.location.background_blur
    show anon f_normal with dissolve
    anon "Looks like I got a text."
    hide anon with dissolve
    return

label consuela_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_shock a_phone with dissolve
    anon "It has to be the baby!"
    anon "{b}I should head to the clinic and check on her{/b}."
    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
