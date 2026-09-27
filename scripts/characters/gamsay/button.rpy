label gamsay_button_dialogue:
    call gamsay_button_stage

    if L_rump_kitchen.is_here(M_gamsay):
        if M_gamsay.is_state(S_gam_intro_ready):
            call gam01_gamsay_meet
            $ M_gamsay.trigger(T_gam_intro_met)
        else:
            call gamsay_button_kitchen

    $ game.main()
    return

label gamsay_button_stage:
    if L_rump_kitchen.is_here(M_gamsay):
        scene expression background(848, 400, 4.)
        show gamsay b_dressed_back:
            flip
            xoffset 450
    else:
        scene expression player.location.background_blur
        show gamsay
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
