label tattoo_parlor_apartment_dialogue:
    if M_eve.is_state(S_eve_visit_apartment) and game.timer.is_evening():
        call expression game.dialog_select("tattoo_parlor_apartment_eve_visit_apartment")
        $ M_eve.trigger(T_eve_visited_apartment)
    elif M_eve.is_state(S_eve_big_sis_check_apartment):
        call expression game.dialog_select("tattoo_parlor_apartment_eve_big_sis_check_apartment")
        $ M_eve.trigger(T_eve_big_sis_checked_apartment)
        $ game.timer.tick()
        $ player.go_to(L_map)
        $ game.main()
    elif M_eve.is_state(S_eve_bathroom_embarassed):
        call expression game.dialog_select("tattoo_parlor_apartment_eve_bathroom_embarassed")
        $ M_eve.trigger(T_eve_bathroom_event_left)
        $ player.go_to(L_map)
        $ game.timer.tick(3)
        $ game.main()
    elif M_eve.is_state(S_eve_pot_look_for_eve) and game.timer.is_tick(0, 1, 2):
        call expression game.dialog_select("tattoo_parlor_apartment_eve_pot_look_for_eve")
        $ M_eve.trigger(T_eve_pot_entered_apartment)
    elif M_eve.is_state(S_eve_clients_wake_up_grace) and game.timer.is_day():
        call expression game.dialog_select("tattoo_parlor_apartment_clients_wake_up_grace")
    elif M_eve.is_state(S_eve_make_up_dress_table) and not game.timer.is_night():
        call expression game.dialog_select("tattoo_parlor_apartment_eve_make_up_dress_table")
        $ player.remove_item("candle")
        $ player.remove_item("chocolates")
        $ player.remove_item("lasagna")
        jump eve_sex_jerk_intro

    if not M_eve.pregnancy or M_eve.pregnancy.announced_pregnancy:
        pass
    elif M_eve.pregnancy.first_baby:
        call expression game.dialog_select("tattoo_parlor_apartment_eve_pregnancy_first")
        $ M_eve.pregnancy.set('announced_pregnancy')

    if M_eve.pregnancy.gave_birth and not M_eve.pregnancy.character_bedridden and not M_eve.pregnancy.gave_birth_dialogue_seen and M_eve.pregnancy.first_baby:
        call expression game.dialog_select("tattoo_parlor_apartment_eve_baby_first")
        $ M_eve.pregnancy.set('gave_birth_dialogue_seen')

    if M_grace.pregnancy.gave_birth and not M_grace.pregnancy.character_bedridden and not M_grace.pregnancy.gave_birth_dialogue_seen and M_grace.pregnancy.first_baby:
        call expression game.dialog_select("tattoo_parlor_apartment_grace_pregnancy_first_baby")
        $ M_grace.pregnancy.set('gave_birth_dialogue_seen')

    if M_odette.pregnancy.gave_birth and not M_odette.pregnancy.character_bedridden and not M_odette.pregnancy.gave_birth_dialogue_seen and M_odette.pregnancy.first_baby:
        call expression game.dialog_select("tattoo_parlor_apartment_odette_pregnancy_first_baby")
        $ M_odette.pregnancy.set('gave_birth_dialogue_seen')

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
