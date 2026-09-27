label tony_button_dialogue:
    call tony_button_stage

    if M_diane.is_state(S_dia03_stow):
        call dia03_trip_tony

    elif M_anon.is_state(S_ano04_test):
        if game.timer.is_day():
            call ano04_test_tony
            if player.transport_level:
                call pizzeria_interior_job
        else:
            call ano04_late_tony

    elif M_anon.between_states(S_ano05_prat, S_ano05_sale) and game.timer.is_day():
        call ano05_hint_tony

    elif M_anon.is_state(S_ano05_wage) and game.timer.is_day():
        call ano05_wage_tony
        $ M_anon.trigger(T_ano05_wage)
        $ M_maria.set('met', True)

    elif M_anon.is_state(S_ano06_cook):
        call ano06_cook_tony

    elif M_anon.between_states(S_ano07_deal, S_ano07_sale) and game.timer.is_day():
        call ano07_hint_tony

    elif M_anon.is_state(S_ano07_wage) and game.timer.is_day():
        call ano07_wage_tony
        $ M_anon.trigger(T_ano07_wage)

    elif M_anon.is_state(S_ano08_sack) and game.timer.is_day():
        call ano08_sack_tony

    elif M_anon.is_state(S_ano08_sack):
        call ano08_late_tony

    elif M_anon.between_states(S_ano09_brat, S_ano09_sale) and game.timer.is_day():
        call ano09_hint_tony

    elif M_anon.is_state(S_ano09_wage) and game.timer.is_day():
        call ano09_wage_tony
        $ M_anon.trigger(T_ano09_wage)

    elif M_anon.is_state(S_ano25_sick) and L_bank.is_here(M_tony):
        call ano25_find_tony.bank

    elif M_anon.is_state(S_ano25_sick):
        call ano25_find_tony.pizzeria

    elif M_anon.is_state(S_ano26_init) and L_bank.is_here(M_tony):
        call ano26_init_tony.bank
        $ player.remove_item('duffel')
        $ player.go_to(L_bank_lobby)
        $ M_anon.trigger(T_ano26_init)

    elif M_anon.is_state(S_ano26_init):
        call ano26_init_tony.pizzeria

    elif M_anon.is_state(S_ano26_talk):
        call ano26_talk_tony

    elif M_anon.is_state(S_ano26_move):
        call ano26_move_tony

    elif M_eve.is_state(S_eve_make_up_pick_up_lasagna) and L_pizzeria_interior.is_here(M_tony):
        call eve20_tony_lasagna
        if _return:
            $ M_eve.trigger(T_eve_picked_up_lasagna)
            $ M_maria.set('met', True)
            $ player.go_to(L_pizzeria_exterior)

    elif M_maria.pregnancy.stage > 4 and game.timer.is_morning():
        call tony_button_baby

    elif L_pizzeria_interior.is_here(M_tony):
        call tony_button_pizzeria

    elif L_pizzeria_kitchen.is_here(M_tony):
        call tony_button_pizzeria

    elif L_maria_lounge.is_here(M_tony):
        if game.timer.is_evening():
            call tony_button_sleep
        else:
            call tony_button_lounge

    if _return:
        $ player.spend_money(items[_return]['cost'])
        $ player.get_item(_return)
        call popup ('give', _return)

    if M_anon.is_state(S_ano14_done):
        $ L_rump_front.unlock()
        $ M_anon.trigger(T_ano14_done)

    $ game.main()
    return

label tony_button_stage:
    if L_pizzeria_interior.is_here(M_tony):
        scene expression player.location.background_closeup
        if M_maria.pregnancy.stage > 4 and game.timer.is_morning():
            show tony a_baby f_normal_down
        show tony:
            flip
        show expression game.timer.image('char_xtra_12{}') as counter
    elif L_pizzeria_kitchen.is_here(M_tony):
        scene expression background(620, 436, 3.) as stage
        show tony a_broom
    elif L_maria_lounge.is_here(M_tony):
        scene expression background(176, 400, 3.) as stage
        show tony b_casual at flip
    elif L_bank.is_here(M_tony):
        scene expression background(776, 440, 8, t=1) as stage
        show tony b_casual a_crossed at flip
    else:
        scene expression player.location.background_blur
        show tony
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
