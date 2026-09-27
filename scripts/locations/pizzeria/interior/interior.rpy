label pizzeria_interior_dialogue:
    if M_anon.is_state(S_ano04_tony):
        call ano04_tony_pizzeria_interior
        $ M_anon.trigger(T_ano04_tony)
        if _return:
            call pizzeria_interior_job
        else:
            call popup ('earn', 200)
            $ player.get_money(200)
            $ M_tony.set('knows', bool(player.transport_level))

    elif M_anon.is_state(S_ano05_init) and game.timer.is_day():
        call ano05_init_pizzeria_interior
        $ L_dealership.unlock()
        $ M_anon.trigger(T_ano05_init)

    elif M_anon.is_state(S_ano06_init) and game.timer.is_morning():
        call ano06_init_pizzeria_interior
        $ M_anon.trigger(T_ano06_init)

    elif M_anon.is_state(S_ano06_coax) and game.timer.is_day():
        call ano06_coax_pizzeria_interior
        $ M_anon.trigger(T_ano06_coax)

    elif M_anon.is_state(S_ano07_init) and game.timer.is_day():
        call ano07_init_pizzeria_interior
        $ M_anon.trigger(T_ano07_init)

    elif M_anon.is_state(S_ano08_init) and game.timer.is_day():
        call ano08_init_pizzeria_interior
        $ M_anon.trigger(T_ano08_init)

    elif M_anon.is_state(S_ano09_init) and game.timer.is_day():
        call ano09_init_pizzeria_interior
        $ M_anon.trigger(T_ano09_init)

    elif M_anon.is_state(S_ano10_init):
        call ano10_init_pizzeria_interior
        $ M_anon.trigger(T_ano10_init)

    elif M_anon.is_state(S_ano10_tony):
        call ano10_tony_pizzeria_interior
        $ M_anon.trigger(T_ano10_tony)

    elif M_anon.is_state(S_ano11_init) and game.timer.is_day():
        call ano11_init_pizzeria_interior
        $ M_anon.trigger(T_ano11_init)

    elif M_anon.is_state(S_ano11_prep) and game.timer.is_evening():
        call ano11_prep_pizzeria_interior
        $ M_maria.set('sex', True)
        $ game.timer.tick()
        $ M_anon.trigger(T_ano11_prep)

    elif M_anon.is_state(S_ano12_init):
        call ano12_init_pizzeria_interior
        $ M_maria.pregnancy.set('announced_pregnancy')
        $ L_warehouse.unlock()
        $ player.go_to(L_pizzeria_exterior)
        $ M_anon.trigger(T_ano12_init)

    elif M_anon.is_state(S_ano13_tony) and game.timer.is_day():
        call ano13_tony_pizzeria_interior
        $ M_anon.trigger(T_ano13_tony)

    elif M_anon.is_state(S_ano13_tina):
        call ano13_tina_pizzeria_interior
        $ L_police_front.unlock()
        $ game.timer.tick()
        $ player.go_to(L_pizzeria_exterior)
        $ M_anon.trigger(T_ano13_tina)

    elif M_maria.pregnancy.gave_birth and not M_maria.pregnancy.gave_birth_dialogue_seen and M_maria.pregnancy.first_baby and game.timer.is_day():
        call pizzeria_interior_maria_baby
        $ M_maria.pregnancy.set('announced_pregnancy')
        $ M_maria.pregnancy.set('gave_birth_dialogue_seen')
        $ game.timer.tick()

    elif M_maria.pregnancy and not M_maria.pregnancy.announced_pregnancy:
        call pizzeria_interior_maria_pregnancy
        $ M_maria.pregnancy.set('announced_pregnancy')
        $ game.timer.tick()

    elif M_anon.is_state(S_ano22_init):
        call ano22_init_pizzeria_interior
        $ L_church_front.unlock()
        $ player.go_to(L_pizzeria_exterior)
        $ M_anon.trigger(T_ano22_init)

    elif M_anon.is_state(S_ano23_init):
        call ano23_init_pizzeria_interior
        $ player.go_to(L_pizzeria_exterior)
        $ M_anon.trigger(T_ano23_init)

    elif M_anon.is_state(S_ano25_plan):
        call ano25_init_pizzeria_interior
        $ game.timer.tick()
        $ player.go_to(L_pizzeria_exterior)
        $ M_anon.trigger(T_ano25_plan)

    elif M_anon.is_state(S_ano27_tony):
        call ano27_tony_pizzeria_interior
        $ player.go_to(L_map)
        $ M_anon.trigger(T_ano27_tony)

    elif M_diane.is_state(S_dia03_give):
        call dia03_give_pizzeria_interior
        $ M_diane.trigger(T_dia03_give)

    $ game.main()
    return


label pizzeria_interior_job:
    if M_anon.is_state(S_ano05_wage, S_ano06_cook, S_ano07_wage, S_ano08_sack,
                       S_ano09_wage):
        jump tony_button_dialogue

    if M_diane.is_state(S_dia03_stow):
        jump tony_button_dialogue

    show screen minigame_pizza(player.transport_level) with fade
    call screen empty()
    hide screen minigame_pizza

    python hide:
        correct = _return.count(True)
        pay = 30 if M_tony.knows else 50
        total = M_player.deliveries - correct

        wait = max(0, M_tony.cooldown - game.timer._game_day)

        if total <= 0:
            if M_anon.is_state(S_ano04_work):
                M_anon.trigger(T_ano04_work)
                M_anon._state.delay = wait
            elif M_anon.is_state(S_ano05_work):
                M_anon.trigger(T_ano05_work)
            elif M_anon.is_state(S_ano06_work):
                M_anon.trigger(T_ano06_work)
                M_anon._state.delay = wait
            elif M_anon.is_state(S_ano07_work):
                M_anon.trigger(T_ano07_work)
            elif M_anon.is_state(S_ano08_work):
                M_anon.trigger(T_ano08_work)
                M_anon._state.delay = wait
            elif M_anon.is_state(S_ano09_work):
                M_anon.trigger(T_ano09_work)
                M_anon._state.delay = wait

        M_player.set('deliveries', total)

        store.res = util.struct(pay=correct * pay * player.transport_level,
                                perfect=correct == len(_return))

    call pizzeria_interior_job_complete

    if res.pay:
        $ player.get_money(res.pay)
        call popup ('earn', res.pay)

    if M_anon.is_state(S_ano04_test):
        $ M_anon.trigger(T_ano04_test)
        $ M_player.set('mugged', game.timer._game_day - 2)

    $ game.timer.tick()

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
