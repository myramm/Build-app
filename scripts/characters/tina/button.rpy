label tina_button_dialogue:
    call tina_button_stage

    if 0 < M_tina.pregnancy.stage < 5:
        call tina_button_pregnant

    elif M_tina.pregnancy.character_bedridden:
        call tina_button_recovery

    elif M_tina.pregnancy.stage > 4:
        call tina_button_baby

    elif L_bank_lobby.is_here(M_tina):
        call tina_button_bank

    elif L_bank_cubicle.is_here(M_tina):
        call tina_button_bank
    else:

        tina f_surprised "Bagaimana kamu sampai di sini?"


    if _return == 'schedule':
        $ M_tina.set('sex', game.timer._game_day)

    elif _return == 'afterglow':
        $ game.timer.tick()
        $ player.go_to(L_bank)

    $ game.main()
    return


label tina_button_stage:
    if L_tina_lounge.is_here(M_tina):
        scene expression background(840, 424, 3.) as stage
        if M_tina.pregnancy.stage > 4:
            show tina b_casual a_baby f_normal_down
        elif M_tina.pregnancy:
            show tina b_magic
        else:
            show tina
    elif L_bank_lobby.is_here(M_tina):
        scene expression background(384, 472, 3.5) as stage
        show tina o_glasses at flip
        if 1 < M_tina.pregnancy.stage < 5:
            show tina b_magic
    elif L_bank_cubicle.is_here(M_tina):
        scene expression background(712, 400, 2.5) as stage
        show tina o_glasses
        if 1 < M_tina.pregnancy.stage < 5:
            show tina b_magic
    elif M_tina.pregnancy.character_bedridden:
        scene expression game.timer.image('location_hospital_baby_bed{}')
        show tina b_gown_bed f_normal_down
    else:
        scene expression player.location.background_blur
        show tina
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
