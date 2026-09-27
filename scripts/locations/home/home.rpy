label home_front_dialogue:
    $ player.go_to(L_home)

    if game.timer.is_dark():
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    else:

        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)

    if M_anon.is_state(S_ano02_thug):
        call ano02_thug_home
        $ M_anon.trigger(T_ano02_thug)

    elif M_anon.is_state(S_ano02_warn) and game.timer.is_morning():
        call ano02_warn_home
        $ M_anon.trigger(T_ano02_warn)
        $ game.timer.tick()

    elif M_anon.is_state(S_ano27_home):
        call ano27_home_home
        $ M_anon.trigger(T_ano27_home)

    elif M_roxxy.is_state(S_roxxy_studying_at_mcs, S_roxxy_cookies_and_milk):
        pass

    elif M_debbie.is_state(S_debbie_relaxing):
        scene expression player.location.background_blur
        call popup ('map')

    elif M_debbie.is_state(S_debbie_mrsj_visit) and not game.timer.is_dark():
        call expression game.dialog_select("home_front_mom_mrsj_visit")
        $ M_debbie.trigger(T_debbie_mrsj_condolences)

    elif M_debbie.is_state(S_debbie_mow_lawn):
        call expression game.dialog_select("home_front_mom_mow_lawn")
        $ M_debbie.trigger(T_debbie_mowed_lawn)

    elif M_debbie.is_state(S_debbie_car_fixed) and not game.timer.is_night():
        call expression game.dialog_select("home_front_mom_car_fixed")

        $ player.go_to(L_home_garage)
        call expression game.dialog_select("home_front_mom_car_fixed_check_car")
        $ M_debbie.set("jerk count", 0)
        $ M_debbie.set("sex speed", .3)
        $ animated = False
        menu:
            "A little longer.":
                call expression game.dialog_select("home_front_mom_car_fixed_check_car_little_longer")
                jump expression game.dialog_select("mom_car_jerk_loop")
            "Leave the car.":

                call expression game.dialog_select("home_front_mom_car_fixed_check_car_finished")

    elif M_debbie.is_state(S_debbie_bad_guys_revisit) and not game.timer.is_dark():
        call expression game.dialog_select("home_front_mom_bad_guys_revisit")
        $ M_debbie.trigger(T_debbie_bad_guys_beatup)
        $ game.timer.tick()
        jump expression game.dialog_select("hallway_dialogue")

    $ game.main()
    return


label home_main_police_cruiser:
    if M_anon.is_state(S_ano27_yumi):
        call ano27_yumi_police_cruiser

    elif M_anon.is_state(S_ano27_tony):
        call ano27_tony_police_cruiser

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
