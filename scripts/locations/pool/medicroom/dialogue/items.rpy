label medic_room_toolbag_dialogue:
    scene expression player.location.background_blur
    show anon f_shy_low a_toolbag with dissolve
    anon "Hey, I bet this is {b}Jiang's lucky tool bag{/b}."
    anon "It's strange, he said he was fixing the water filtration unit but then what was his bag doing in here?"
    pause
    anon "Oh well, I should hurry up and bring it back to him."
    show anon f_shy_down a_backpack with dissolve
    pause
    anon a_idle f_normal "Hopefully he's managed to get ahold of {b}Kim{/b}'s phone by now."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
