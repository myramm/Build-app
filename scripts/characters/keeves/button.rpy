label keeves_button_dialogue:
    call keeves_button_stage

    if L_church.is_here(M_keeves):
        if M_keeves.is_state(S_kee_intro_meet):
            call kee01_keeves_meet
            $ M_keeves.trigger(T_kee_intro_met)
        else:
            call keeves_button_church

    $ game.main()
    return

label keeves_button_stage:
    if L_church.is_here(M_keeves):
        scene expression background(632, 416, 6.)
        show keeves
        show location_church_day_closeup_altar as altar at left
    else:
        scene expression player.location.background_blur
        show keeves
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
