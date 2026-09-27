label garage_dialogue:
    $ player.go_to(L_home_garage)
    if not game.timer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if M_dewitt.is_state([S_dewitt_garage_find_paint, S_dewitt_ask_deb_paint]):
        call expression game.dialog_select("garage_dewitt_find_paint")
        $ M_dewitt.trigger(T_dewitt_no_paint)
    $ game.main()
    return

label car_dialogue:
    scene expression background(512, 400, 1.6) as stage

    if M_debbie.is_state(S_debbie_fix_car):
        call debXX_call_home_garage_car
        if M_anon.finished_state(S_ano09_blow):
            $ M_debbie.trigger(T_debbie_extend_insurance)
        else:
            $ M_debbie.trigger(T_debbie_lapsed_insurance)

    elif M_debbie.is_state(S_debbie_car_callback):
        call debXX_cash_home_garage_car
        if _return:
            $ M_debbie.trigger(T_debbie_extend_insurance)

    elif M_debbie.is_state(S_debbie_mall_outing):
        call expression game.dialog_select("garage_car_mom_mall_outing")
        jump expression game.dialog_select("mall_dialogue")

    elif M_debbie.is_state(S_debbie_check_car):
        $ player.go_to(L_home_car)
        call expression game.dialog_select("garage_car_mom_check_car")
        $ player.location.call_screen(False)
    else:

        if seen_garage_locked:
            call expression game.dialog_select("garage_car_seen")
        else:
            call expression game.dialog_select("garage_car_not_seen")
            $ seen_garage_locked = True

    $ game.main()
    return

label garage_use_workbench:
    if game.timer.is_dark():
        call expression game.dialog_select("garage_use_workbench_night")
        $ game.main()
    if M_dewitt.is_state(S_dewitt_make_new_flute) and player.has_item("drill") and player.has_item("stick"):
        call expression game.dialog_select("garage_dewitt_make_new_flute")
        $ player.remove_item("broken_flute")
        $ player.remove_item("drill")
        $ player.remove_item("stick")
        $ player.get_item("flute")
        $ game.timer.tick()
        $ M_dewitt.trigger(T_dewitt_fix_flute)

    elif M_dewitt.is_state(S_dewitt_make_replacement_guitar) and player.has_item("paint") and player.has_item("wood_pile"):
        call expression game.dialog_select("garage_dewitt_make_replacement_guitar")
        $ player.remove_item("wood_pile")
        $ player.remove_item("paint")
        $ player.get_item("fake_guitar")
        $ game.timer.tick()
        $ M_dewitt.trigger(T_dewitt_made_replacement_guitar)

    elif M_ross.is_state(S_ross_get_easels) and player.has_item("wood_pile"):
        call expression game.dialog_select("garage_build_easels")
        $ player.remove_item("wood_pile")
        $ player.get_item("easels")
        $ game.timer.tick()
    else:

        call expression game.dialog_select("garage_workbench_not_needed")
    $ game.main()
    return

label car_engine_dialogue:
    $ game.main()
    return

label home_garage_shovel:
    if M_diane.is_state(S_dia01_find):
        call dia01_find_home_garage_shovel
        $ player.get_item("shovel")
        call popup ('give', 'shovel')
        $ M_diane.trigger(T_dia01_find)
    else:
        pass

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
