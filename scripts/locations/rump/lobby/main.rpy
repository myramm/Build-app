label mayor_rumps_lobby_dialogue:

    if M_anon.is_state(S_ano18_rage):
        call ano18_rage_rump_lobby
        $ M_anon.trigger(T_ano18_rage)

    elif M_anon.is_state(S_ano18_flee):
        call ano18_flee_rump_lobby
        $ player.get_item('staff_badge')
        $ M_anon.trigger(T_ano18_flee)

    elif M_anon.finished_state(S_ano20_cops) and not M_consuela.finished_inclusive(S_con01_done):
        call con01_skip_rump_lobby
        $ L_church_front.unlock()
        $ player.go_to(L_rump_front)
        $ S_con01_take.delay = 0
        $ M_consuela.trigger(T_con01_skip)

    elif M_melonia.pregnancy and not M_melonia.pregnancy.announced_pregnancy:
        if M_melonia.pregnancy.first_baby:
            call rump_lobby_melonia_pregnancy_first
        else:
            call rump_lobby_melonia_pregnancy
        if _return:
            $ M_melonia.pregnancy.set('announced_pregnancy')
        else:
            $ M_melonia.pregnancy.abort_baby()
        $ game.timer.tick()

    elif M_iwanka.pregnancy.show_baby_intro:
        call rump_lobby_iwanka_baby_first
        $ M_iwanka.pregnancy.set('gave_birth_dialogue_seen')
        $ game.timer.tick()

    elif M_melonia.pregnancy.show_baby_intro:
        call rump_lobby_melonia_baby_first
        $ M_melonia.pregnancy.set('gave_birth_dialogue_seen')
        $ game.timer.tick()

    elif M_consuela.is_state(S_con01_give):
        call con01_give_rump_lobby
        $ player.remove_item('thotbot')
        $ L_church_front.unlock()
        $ player.go_to(L_rump_front)
        $ M_consuela.trigger(T_con01_give)

    elif M_thotbot.is_state(S_bot01_init):
        if M_consuela.finished_state(S_con01_skip):
            call bot01_init_rump_lobby.melonia
        else:
            call bot01_init_rump_lobby.ronald
        $ M_thotbot.trigger(T_bot01_init)

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
