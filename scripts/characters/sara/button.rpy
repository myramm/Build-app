label sara_button_dialogue:
    call sara_button_stage

    if L_apt_lobby.is_here(M_sara):
        if not M_sara.once('job') and M_sara.once('met'):
            call sara_button_lobby.job
        else:
            call sara_button_lobby
    else:

        sara "Oh tidak! Apakah para pengembang juga lupa menghubungkan dialog ini?!"


    $ game.main()
    return

label sara_button_stage:
    if L_apt_lobby.is_here(M_sara):
        scene expression game.timer.image('location_apt_lobby_desk{}') as stage
        show sara
        show expression game.timer.image('sara_overlay_desk{}') as counter
    else:
        show expression player.location.background_blur as stage
        show sara
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
