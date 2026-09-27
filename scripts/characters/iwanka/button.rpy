label iwanka_button_dialogue:
    call iwanka_button_stage

    if M_anon.is_state(S_ano17_porn):
        call ano17_porn_iwanka
        $ M_anon.trigger(T_ano17_porn)
        $ player.go_to(L_erikhouse)
        $ game.timer.tick(3)

    elif M_iwanka.is_state(S_iwa01_init):
        call iwa01_init_iwanka
        $ M_iwanka.trigger(T_iwa01_init)
        $ player.go_to(L_rump_lobby)

    elif M_iwanka.is_state(S_iwa01_find):
        call iwa01_find_iwanka
        $ player.go_to(L_rump_lobby)

    elif M_iwanka.is_state(S_iwa01_give):
        call iwa01_give_iwanka
        $ player.remove_item('maid_uniform')
        $ M_iwanka.trigger(T_iwa01_give)
        if _return:
            $ M_iwanka.trigger(T_iwa01_wait)

    elif M_iwanka.is_state(S_iwa01_wait):
        call iwa01_wait_iwanka
        if _return:
            $ M_iwanka.trigger(T_iwa01_wait)

    elif 0 < M_iwanka.pregnancy.stage < 5:
        call iwanka_button_pregnant

    elif M_iwanka.pregnancy.character_bedridden:
        call iwanka_button_recovery

    elif M_iwanka.pregnancy.stage > 4:
        call iwanka_button_baby

    elif L_rump_second.is_here(M_iwanka):
        if M_iwanka.outfit.is_naked:
            call iwanka_button_bed
            if _return == 'afterglow':
                $ player.go_to(L_rump_lobby)
                $ game.timer.tick()
        else:
            call iwanka_button_bedroom

    elif L_boat_bridge.is_here(M_iwanka):
        call iwanka_button_yacht
        if _return == 'afterglow':
            $ game.timer.tick()

    $ game.main()
    return


label iwanka_button_stage:
    if L_rump_second.is_here(M_iwanka):
        if M_iwanka.pregnancy.stage < 2 and M_iwanka.outfit.is_naked:
            scene location_rump_iwanka_bed_closeup as stage
            show iwanka b_chair_naked:
                flip
                offset (0, -80)
                zoom .9
        else:
            scene expression background(288, 368, 3.5) as stage
            if 0 < M_iwanka.pregnancy.stage < 5:
                show iwanka b_magic
            else:
                show iwanka
    elif L_boat_bridge.is_here(M_iwanka):
        if M_iwanka.pregnancy.stage > 1:
            scene expression background(400, 328, 2.8) as stage
            show iwanka b_magic
        else:
            scene expression game.timer.image('location_boat_chair{}') as stage
            if M_iwanka.outfit.get == 'naked':
                show iwanka b_chair_naked
            else:
                show iwanka b_chair_swimsuit
    elif M_iwanka.pregnancy.character_bedridden:
        scene expression game.timer.image('location_hospital_baby_bed{}') as stage
        show iwanka b_gown_bed f_drunk
    else:
        scene expression player.location.background_blur as stage
        show iwanka
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
