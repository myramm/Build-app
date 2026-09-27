label mayor_rumps_backyard_dialogue:

    if M_anon.is_state(S_ano18_yard):
        call ano18_yard_rump_back
        $ M_anon.trigger(T_ano18_yard)
        $ player.go_to(L_rump_kitchen)

    $ game.main()
    return


label rump_back_net:
    if M_melonia.is_state(S_mel01_init):
        call mel01_init_net

    elif M_melonia.is_state(S_mel01_hint):
        call mel01_hint_net

    elif M_melonia.is_state(S_mel01_find):
        call mel01_find_net
        $ player.get_item('leaf_skimmer')
        call popup ('give', 'leaf_skimmer')
        $ M_melonia.trigger(T_mel01_find)

    elif M_melonia.is_state(S_mel02_init):
        call mel02_init_net
        $ player.get_money(50)
        call popup ('earn', 50)
        $ game.timer.tick()
        $ M_melonia.trigger(T_mel02_init)

    elif M_melonia.is_state(S_mel03_init):
        call mel03_init_net
        $ player.get_money(200)
        call popup ('earn', 200)
        $ game.timer.tick()
        $ M_melonia.trigger(T_mel03_init)

    elif M_melonia.is_state(S_mel04_init):
        call mel04_init_net
        $ player.get_money(300)
        call popup ('earn', 300)
        $ game.timer.tick()
        $ player.go_to(L_rump_kitchen)
        $ M_melonia.trigger(T_mel04_init)

    elif M_melonia.is_state(S_mel05_init):
        call mel05_init_net
        $ player.get_money(350)
        call popup ('earn', 350)
        $ game.timer.tick()
        $ player.go_to(L_rump_lobby)
        $ M_melonia.trigger(T_mel05_init)
    else:

        call rump_back_net_dialogue

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
