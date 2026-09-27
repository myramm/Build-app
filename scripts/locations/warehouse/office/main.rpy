label warehouse_office_dialogue:

    if M_anon.is_state(S_ano27_boss):
        call ano27_boss_warehouse_office
        $ M_nadya.set('killer', _return)
        $ M_anon.trigger(T_ano27_boss)
        $ player.go_to(L_home_bedroom)
        jump resume_sleeping_bedroom

    elif M_nadya.is_state(S_nad01_find):
        $ player.go_to(L_warehouse_depot)
        jump svetlana_button_dialogue

    elif 1 < M_nadya.pregnancy.stage:
        pass

    elif M_katya.is_state(S_kat01_init) and game.timer.is_evening():
        call kat01_init_office
        $ game.timer.tick()
        $ player.go_to(L_warehouse)
        $ M_katya.trigger(T_kat01_init)

    elif M_svetlana.is_state(S_sve01_lewd) and game.timer.is_day():
        call sve01_lewd_office
        $ game.timer.tick()
        $ player.go_to(L_warehouse_furnace)
        $ M_svetlana.trigger(T_sve01_lewd)
        $ M_katya.move(L_NULL, 2)
        $ M_nadya.move(L_NULL, 2)
        $ M_svetlana.move(L_NULL, 2)

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
