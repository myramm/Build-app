label eve_pregnant_announcement_1:
    scene expression player.location.background_blur with None
    show anon f_looking_down a_phone
    anon @ -m_talk "Hmm?"
    anon f_shock_down @ -m_talk "I've got a text from {b}Eve{/b}!"
    hide anon with dissolve
    return

label eve_pregnant_announcement_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_worried a_phone with dissolve
    anon "I wonder what's going on?"
    anon "I should {b}swing by Eve's place and check it out{/b}."
    if player.location != L_map:
        hide anon with dissolve
    return

label eve_pregnant_labor_1:
    scene expression player.location.background_blur
    show anon f_normal with dissolve
    anon "Looks like I got a text."
    hide anon with dissolve
    return

label eve_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_shock with dissolve
    anon @ -m_talk "{b}Eve{/b} had the baby?!"
    anon @ -m_talk "Holy crap!"
    pause
    anon f_worried "I'd better head to {b}the clinic{/b} to check on them."
    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
