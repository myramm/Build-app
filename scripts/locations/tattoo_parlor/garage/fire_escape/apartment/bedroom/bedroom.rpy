label tattoo_parlor_bedroom_dialogue:
    if M_eve.is_state(S_eve_visit_bedroom) and game.timer.is_evening():
        call expression game.dialog_select("tattoo_parlor_bedroom_eve_visit_bedroom")
        $ game.timer.tick(3)
        $ M_eve.trigger(T_eve_visited_bedroom)
        $ player.go_to(L_map)
        $ game.main()
    elif M_eve.is_state(S_eve_bathroom_break):
        call expression game.dialog_select("tattoo_parlor_bedroom_eve_bathroom_break")
    elif M_eve.is_state(S_eve_pot_cheerup) and game.timer.is_tick(0, 1, 2):
        call expression game.dialog_select("tattoo_parlor_bedroom_eve_pot_cheerup")
        $ M_eve.trigger(T_eve_pot_cheered_up)
        $ game.timer.tick(3)
        $ player.go_to(L_map)
        $ game.main()
    elif M_eve.is_state(S_eve_clients_wake_up_grace) and game.timer.is_day():
        call expression game.dialog_select("tattoo_parlor_bedroom_eve_clients_wake_up_grace")
        $ M_eve.trigger(T_eve_woke_grace)
        $ player.go_to(L_tattooparlor)
        $ game.main()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
