label diane_pregnant_announcement_1:
    scene expression player.location.background_blur
    show player 9 with dissolve
    player_name "Hmm?"
    player_name "I've got a text from {b}Diane{/b}!"
    hide player with dissolve
    return

label diane_pregnant_announcement_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show player 12 with dissolve
    player_name "I wonder what's going on?"
    player_name "I should {b}swing by Diane's barn and see what's the matter{/b}."
    if player.location != L_map:
        hide player with dissolve
    return

label diane_pregnant_labor_1:
    scene expression player.location.background_blur
    show player 14 with dissolve
    player_name "Looks like I got a text."
    hide player with dissolve
    return

label diane_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_shock with dissolve
    anon "The baby is coming!"
    anon f_surprised_teeth @ f_shock "Holy crap!"
    pause
    anon f_shock "I'd better {b}head to the hospital to check on them{/b}!"
    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
