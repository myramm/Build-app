label dianes_lobby_dialogue:
    $ player.go_to(L_diane_home)
    if M_diane.is_state(S_diane_look_in_kitchen):
        call expression game.dialog_select("dianes_lobby_look_in_kitchen")
    $ game.main()

label dianelobby_locked:
    if player.location == L_diane_kitchen:
        scene dianekitchen
    elif player.location == L_diane_yard:
        scene location_diane_front_day_blur
    show anon with dissolve
    anon "I think I hear someone in the backyard. I should check and see if it's {b}Diane{/b}."

    hide anon with dissolve
    return

label dianekitchen_locked:
    scene expression player.location.background_blur
    show anon f_worried with dissolve
    anon "I shouldn't go inside there without permission."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
