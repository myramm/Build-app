label liu_button_dialogue:
    call liu_button_stage

    if M_liu.is_state(S_liu01_init):
        call liu01_init_liu
        $ player.get_item('atm_card')
        call popup ('give', 'atm_card')
        $ M_liu.trigger(T_liu01_init)

    elif M_anon.is_state(S_ano14_init):
        call ano14_init_liu
        $ M_anon.trigger(T_ano14_init)

    elif M_anon.is_state(S_ano14_sobs):
        call ano14_sobs_liu
        $ M_anon.trigger(T_ano14_sobs)

    elif M_anon.is_state(S_ano23_seek):
        call ano23_seek_liu
        $ M_anon.trigger(T_ano23_seek)

    elif M_anon.is_state(S_ano26_talk):
        call ano26_talk_liu
        $ M_anon.trigger(T_ano26_talk)

    elif M_anon.between_states(S_ano27_init, S_ano27_done):
        call ano27_lock_liu

    elif 0 < M_liu.pregnancy.stage < 5:
        call liu_button_pregnant

    elif M_liu.pregnancy.character_bedridden:
        call liu_button_recovery

    elif M_liu.pregnancy.stage > 4:
        call liu_button_baby

    elif L_liu_lounge.is_here(M_liu):
        call liu_button_lounge

    elif L_liu_bedroom.is_here(M_liu):
        call liu_button_bedroom
    else:

        call liu_button_lobby

    if _return == 'ano28':
        $ player.remove_item('money_bag')
        if player.location == L_bank_lobby:
            $ player.go_to(L_bank)
        else:
            $ player.go_to(L_apt_hall2)
        $ M_anon.trigger(T_ano28_cash)

    elif _return == 'office':
        $ M_tina.trigger(T_tin02_init)

    elif _return == 'afterglow':
        $ game.timer.tick()
        if player.location == L_bank_lobby:
            $ player.go_to(L_bank)
        else:
            $ player.go_to(L_apt_hall2)

    $ game.main()
    return


label liu_button_stage:
    if L_bank_lobby.is_here(M_liu):
        scene location_bank_lobby_desk_day
        show liu a_typing f_happy_down
        show liu_desk as counter
        if M_liu.pregnancy.stage:
            show liu b_dressed_magic
    elif L_liu_lounge.is_here(M_liu):
        if M_liu.pregnancy.stage:
            scene expression background(768, 384, 2) as stage
            if M_liu.pregnancy.stage > 4:
                show liu a_baby b_robe_hair
            else:
                show liu b_robe_magic
        else:
            scene expression game.timer.image('location_liu_lounge_tea{}')
            show liu b_robe_tea
            show liu_overlay_o_tea_table as table
    elif L_liu_bedroom.is_here(M_liu):
        scene expression background(464, 392, 5) as stage
    elif M_liu.pregnancy.character_bedridden:
        scene expression game.timer.image('location_hospital_baby_bed{}')
        show liu b_gown_bed f_normal_down
    else:
        scene expression player.location.background_blur
        show liu
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
