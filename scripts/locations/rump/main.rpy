label mayor_rumps_frontyard_dialogue:

    if M_anon.is_state(S_ano15_init, S_ano15_hint) and game.timer.is_weekday() and game.timer.is_afternoon():
        call ano15_init_rump_front
        $ player.go_to(L_map)
        $ game.timer.tick()
        $ M_anon.trigger(T_ano15_pass)

    elif M_iwanka.is_state(S_iwa01_exit):
        call iwa01_exit_rump_front
        $ L_pier.unlock()
        $ player.go_to(L_map)
        $ M_iwanka.trigger(T_iwa01_exit)

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
