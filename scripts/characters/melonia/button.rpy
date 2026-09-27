label melonia_button_dialogue:
    call melonia_button_stage

    if M_melonia.is_state(S_mel01_init) and game.timer.is_day():
        call mel01_init_melonia
        $ M_melonia.trigger(T_mel01_init)

    elif M_melonia.is_state(S_mel01_more):
        call mel01_more_melonia

    elif 0 < M_melonia.pregnancy.stage < 5:
        call melonia_button_pregnant

    elif M_melonia.pregnancy.character_bedridden:
        call melonia_button_recovery
        $ game.timer.tick()
        $ player.go_to(L_hospital_floor3)

    elif M_melonia.pregnancy.stage > 4:
        call melonia_button_baby (low=L_rump_back.is_here(M_melonia))
    else:

        call melonia_button_common (venue=('bedroom' if L_rump_master.is_here(M_melonia) else
                   'garden' if game.timer.is_morning() else 'hottub'), level=(M_anon.finished_state(S_ano20_done) +
                   M_melonia.finished_state(S_mel05_init)))



        if _return == 'afterglow':
            call popup ('earn', 150)
            $ player.get_money(150)
            $ game.timer.tick()
            $ player.go_to(L_rump_lobby)
        elif _return == 'dance':
            call popup ('earn', 50)
            $ player.get_money(50)
            $ game.timer.tick()
        elif _return == 'escape':
            $ player.go_to(L_rump_lobby)

    $ game.main()
    return


label melonia_button_stage:
    if L_rump_master.is_here(M_melonia):
        scene expression background(800, 384, 4.)
        if M_melonia.pregnancy.stage:
            show melonia b_magic
        else:
            show melonia
    elif L_rump_back.is_here(M_melonia):
        if game.timer.is_afternoon() and not M_melonia.is_state(S_mel01_init) and not 0 < M_melonia.pregnancy.stage < 5:
            scene expression background(712, 368, 2., b=.75) as stage:
                align (1., .5)
                zoom 2
            show location_rump_backyard_jacuzzi_overlay as hottubback:
                yoffset 140
            show melonia b_jacuzzi f_relax:
                yoffset 155
            show location_rump_backyard_jacuzzi_overlay as hottub:
                yoffset 155
            if M_melonia.outfit.is_naked:
                show melonia b_jacuzzi_topless
        else:
            if M_melonia.pregnancy.stage:
                scene expression background(672, 368, 4.) as stage
                show melonia b_magic
            else:
                scene expression background(544, 368, 2., b=.75) as stage:
                    align (1., .5)
                    zoom 2
                show melonia b_swimsuit
    elif M_melonia.pregnancy.character_bedridden:
        scene expression game.timer.image('location_hospital_baby_bed{}')
        show melonia b_gown_bed f_annoyed
    else:
        scene expression player.location.background_blur
        show melonia
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
