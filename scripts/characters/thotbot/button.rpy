label thotbot_button_dialogue:
    call thotbot_button_stage

    if 4 < M_melonia.pregnancy.stage and not M_melonia.pregnancy.character_bedridden:
        call thotbot_button_baby

    elif L_rump_lobby.is_here(M_thotbot):
        call thotbot_button_mansion

    $ game.main()
    return

label thotbot_button_stage:
    if L_rump_lobby.is_here(M_thotbot):
        scene expression background(664, 432, 5.)
        show thotbot:
            xoffset -125
    elif L_rump_master.is_here(M_thotbot):
        scene expression background(520, 368, 3.5) as stage
        show thotbot a_baby:
            xoffset 300
    elif L_rump_back.is_here(M_thotbot):
        scene expression background(600, 368, 4.) as stage
        show thotbot a_baby:
            xoffset 200
    else:
        scene expression player.location.background_blur
        show thotbot
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
