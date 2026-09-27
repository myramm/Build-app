label warehouse_storage_dialogue:

    if M_anon.is_state(S_ano27_help):
        $ M_player.set('ano27_hero', 'tony' if M_tony.watches else
                                     'harold' if M_mia.finished_state(S_mia_route_split) else
                                     'somrak' if player.stats.dex() == 10 else
                                     None)
        call ano27_help_warehouse_storage
        $ player.go_to(L_warehouse_depot)
        $ M_anon.trigger(T_ano27_help)

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
