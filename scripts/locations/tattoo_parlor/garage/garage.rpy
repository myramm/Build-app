label tattoo_parlor_garage_dialogue:
    if M_eve.is_state(S_eve_visit_garage) and game.timer.is_evening():
        call expression game.dialog_select("tattoo_parlor_garage_eve_visit_garage")
        $ M_eve.trigger(T_eve_visited_garage)
    elif M_eve.is_state(S_eve_big_sis_check_garage):
        call expression game.dialog_select("tattoo_parlor_garage_eve_big_sis_check_garage")
        $ M_eve.trigger(T_eve_big_sis_checked_garage)
    elif M_eve.is_state(S_eve_bike_breakdown_repair, S_eve_bike_breakdown_repair_again) and game.timer.is_weekend() and not game.timer.is_night():
        if M_eve.is_state(S_eve_bike_breakdown_repair):
            call expression game.dialog_select("tattoo_parlor_garage_eve_bike_breakdown_repair_intro")
        else:
            call expression game.dialog_select("tattoo_parlor_garage_eve_bike_breakdown_repair_intro_repeat")
        if player.has_required_int(5):
            $ display.toast(int_pass)
            call expression game.dialog_select("tattoo_parlor_garage_eve_bike_breakdown_repair_pass")
            $ M_eve.trigger(T_eve_bike_breakdown_repair_pass)
            jump bike_repair_minigame_prepare
        $ display.toast(int_fail)
        if M_eve.is_state(S_eve_bike_breakdown_repair):
            call expression game.dialog_select("tattoo_parlor_garage_eve_bike_breakdown_repair_fail")
            $ M_eve.trigger(T_eve_bike_breakdown_repair_fail)
        else:
            call expression game.dialog_select("tattoo_parlor_garage_eve_bike_breakdown_repair_fail_repeat")
        call expression game.dialog_select("tattoo_parlor_garage_eve_bike_breakdown_repair_fail_continued")
        $ game.timer.tick(3)
        $ player.go_to(L_map)
        $ game.main()
    elif M_eve.is_state(S_eve_clients_check_shop) and game.timer.is_day():
        call expression game.dialog_select("tattoo_parlor_garage_eve_clients_check_shop")
        $ M_eve.trigger(T_eve_woke_odette)
    elif M_eve.is_state(S_eve_party_start) and game.timer.is_date(tod=(2, 3), dow=5):
        call expression game.dialog_select("tattoo_parlor_garage_eve_party_start")
        $ M_eve.trigger(T_eve_party_started)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
