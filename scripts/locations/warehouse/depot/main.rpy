label warehouse_depot_dialogue:
    if M_anon.is_state(S_ano27_peek):
        call ano27_peek_warehouse_depot
        $ player.go_to(L_warehouse_furnace)
        $ M_anon.trigger(T_ano27_peek)

    elif M_nadya.is_state(S_nad01_meet):
        call nad01_meet_warehouse_depot
        $ M_nadya.trigger(T_nad01_meet)

    elif M_khadne.is_state(S_kha01_talk):
        call kha01_talk_warehouse_depot
        $ M_khadne.trigger(T_kha01_talk)
        $ game.timer.tick(2)

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
