label daisy_pregnant_announcement_1:
    scene expression player.location.background_blur
    show player 9 with dissolve
    player_name "Hmm?"
    player_name "I've got a text from {b}Diane{/b}!"
    hide player with dissolve
    return

label daisy_pregnant_announcement_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show player 10 with dissolve
    player_name "I wonder what's going on?"
    player_name "I should {b}swing by Diane's barn and see what's the matter{/b}."
    if player.location != L_map:
        hide player with dissolve
    return

label daisy_pregnant_labor_1:
    scene expression player.location.background_blur
    show player 14 with dissolve
    player_name "Looks like I got a text."
    hide player with dissolve
    return

label daisy_pregnant_labor_2:
    scene expression player.location.background_blur with None
    if player.location != L_map:
        show anon f_surprised with dissolve
    anon "Holy crap! The baby is here!"
    anon "I'd better {b}head to the barn to check on them{/b}."
    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
