label cafeteria_dialogue:
    $ player.go_to(L_school_cafeteria)
    call pa_announcement
    if M_diane.is_state(S_diane_delivery_3_drop_off_goods):
        call expression game.dialog_select("cafeteria_diane_delivery_3_drop_off_goods")
        $ player.remove_item('milk_9x9z2y')
        $ M_diane.trigger(T_diane_delivery_3_finished)

    if M_eve.is_state(S_eve_cafeteria_troubles) and game.timer.is_day():
        call expression game.dialog_select("cafeteria_eve_cafeteria_troubles")
        $ M_eve.trigger(T_eve_caf_lunch)
        $ game.timer.tick()
        $ player.go_to(L_school_floor2)
        $ game.main()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
