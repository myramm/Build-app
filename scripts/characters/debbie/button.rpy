label debbie_button_dialogue:
    if player.location == L_home_mombedroom:
        jump mom_dialogue_button_room

    if M_debbie.is_state(S_debbie_relaxing):
        call expression game.dialog_select("debbie_dialogue_mom_relaxing")
        $ game.main()

    elif M_debbie.is_set("sleep together") and not M_debbie.is_set("revealing") and player.location == L_home_kitchen:
        call expression game.dialog_select("debbie_dialogue_mom_not_revealing_kitchen")
        $ M_debbie.set("revealing", True)
        $ M_debbie.set("panties available", True)
        jump expression game.dialog_select("debbie_dialogue_options")

    elif M_debbie.is_state(S_debbie_laundry_help) and M_debbie.is_set('chores'):
        jump laundry_dialogue

    scene expression player.location.background_closeup with None

    if M_debbie.is_set("fetch lotion") and not M_debbie.is_set("retrieved lotion"):
        call expression game.dialog_select("debbie_dialogue_mom_fetch_lotion")

    elif M_debbie.is_set("fetch lotion") and M_debbie.is_set("retrieved lotion"):
        jump expression game.dialog_select("mom_lotion_fun")

    elif M_debbie.is_state(S_debbie_car_condition):
        call expression game.dialog_select("debbie_dialogue_mom_car_condition")
        $ M_debbie.trigger(T_debbie_deliver_car_news)

    elif M_jenny.is_state(S_jenny_pool_talk) and game.timer.is_weekend() and game.timer.is_morning():
        call expression game.dialog_select("debbie_dialogue_jenny_pool_talk")
        $ game.main()

    elif M_debbie.is_state(S_debbie_fix_car, S_debbie_car_callback):
        call expression game.dialog_select("debbie_dialogue_help_fix_car")

    elif M_debbie.is_state(S_debbie_car_delay, S_debbie_car_fixed):
        call expression game.dialog_select("debbie_dialogue_mech_en_route")
    else:

        if M_debbie.is_set("revealing") and player.location == L_home_kitchen:
            call expression game.dialog_select("debbie_dialogue_mom_revealing_kitchen_pre")
            menu:
                "Merasa pantat.":
                    if M_debbie.is_set("sex available"):
                        label mom_kitchen_replay:
                            call expression game.dialog_select("debbie_dialogue_mom_revealing_feel_ass_sex_pre")
                        $ M_debbie.set("sex speed", .175)
                        call expression game.dialog_select("debbie_dialogue_mom_revealing_feel_ass_sex_after")
                        jump expression game.dialog_select("mom_kitchen_fuck_loop")
                    else:

                        call expression game.dialog_select("debbie_dialogue_mom_revealing_feel_ass_no_sex")
                        jump expression game.dialog_select("debbie_dialogue_options")
                "Bicara.":

                    call expression game.dialog_select("debbie_dialogue_mom_revealing_talk")
                    jump expression game.dialog_select("debbie_dialogue_options")

        if M_debbie.is_set("revealing"):
            call expression game.dialog_select("debbie_dialogue_mom_revealing")
        else:

            call expression game.dialog_select("debbie_dialogue_mom_not_revealing")
        menu debbie_dialogue_options:
            "Kotak barang-barang." if M_anon.is_state(S_ano13_hint):
                call ano13_hint_debbie
                $ M_anon.trigger(T_ano13_hint)

            "Utangnya jelas." if M_anon.is_state(S_ano28_debt):

                hide player
                hide old_debbie
                show anon
                show debbie
                with fastdissolve
                call ano28_debt_debbie_debt
                $ game.timer.tick(3)
                $ player.go_to(L_home_bedroom)
                $ M_anon.trigger(T_ano28_debt)

            "Tanyakan tentang {b}Ayah{/b}." if M_debbie.is_set("dad question"):
                $ M_debbie.set("dad question", False)
                call expression game.dialog_select("debbie_dialogue_ask_about_dad")
                jump expression game.dialog_select("debbie_dialogue_options")

            "Tanyakan tentang masalah uang." if M_debbie.is_set("money question"):
                $ M_debbie.set("money question", False)
                call expression game.dialog_select("debbie_dialogue_ask_about_money_problems")
                jump expression game.dialog_select("debbie_dialogue_options")

            "Tanyakan tentang pria berjas." if M_debbie.is_set("bad guys question"):
                $ M_debbie.set("bad guys question", False)
                call expression game.dialog_select("debbie_dialogue_ask_about_men_in_suits")
                jump expression game.dialog_select("debbie_dialogue_options")

            "Cat." if M_dewitt.is_state([S_dewitt_ask_deb_paint, S_dewitt_ask_diane_paint, S_dewitt_shed_get_paint]):
                call expression game.dialog_select("debbie_dialogue_paint")
                $ M_dewitt.trigger(T_dewitt_diane_find_paint)
            "Membantu {b}[deb_name]{/b} di sekitar rumah.":

                if M_debbie.is_state([S_debbie_fill_mower, S_debbie_mow_lawn]):
                    call expression game.dialog_select("debbie_dialogue_help_mow_lawn")
                    $ game.main()

                elif M_debbie.between_states(S_debbie_sis_check, S_debbie_fix_pipe):
                    call expression game.dialog_select("debbie_dialogue_help_fix_broken_pipe")

                elif M_debbie.between_states(S_debbie_vacuum_help, S_debbie_laundry_help):
                    call expression game.dialog_select("debbie_dialogue_help_chores_pre")
                    if M_debbie.is_state(S_debbie_laundry_help) and M_debbie.is_set("chores"):
                        call expression game.dialog_select("debbie_dialogue_help_chores_later")
                    else:
                        call expression game.dialog_select("debbie_dialogue_help_chores_tomorrow")
                    call expression game.dialog_select("debbie_dialogue_help_chores_after")

                elif M_debbie.is_state(S_debbie_check_car):
                    call expression game.dialog_select("debbie_dialogue_help_check_car")
                else:

                    call expression game.dialog_select("debbie_dialogue_help_nothing")
                show player 1
                jump expression game.dialog_select("debbie_dialogue_options")

            "Oleskan losion." if M_debbie.is_set("lotion fun"):
                if M_debbie.is_set("sex available") and player.location == L_home_kitchen:
                    call expression game.dialog_select("debbie_dialogue_lotion_fun_had_sex")
                else:

                    call expression game.dialog_select("debbie_dialogue_lotion_fun")
                call expression game.dialog_select("debbie_dialogue_lotion_fun_after")
                $ M_debbie.set("fetch lotion", True)


            "Belanja." if M_debbie.is_state(S_debbie_hang_out_return) and player.location == L_home_kitchen:
                call expression game.dialog_select("debbie_dialogue_shopping")
                $ M_debbie.trigger(T_debbie_hang_out_accept)

            "Mandi." if M_debbie.is_set("sex available"):
                if player.location == L_home_basement:
                    call expression game.dialog_select("debbie_dialogue_shower_basement")

                elif player.location == L_home_kitchen:
                    call expression game.dialog_select("debbie_dialogue_shower_kitchen")
                jump expression game.dialog_select("mom_shower_question")

            "Seks di kamar Anda." if M_debbie.is_set("sex available"):
                if player.location == L_home_basement:
                    call expression game.dialog_select("debbie_dialogue_sex_in_debbies_room_basement")

                elif player.location == L_home_kitchen:
                    call expression game.dialog_select("debbie_dialogue_sex_in_debbies_room_kitchen")
                call expression game.dialog_select("debbie_dialogue_sex_in_debbies_room_after")
                jump expression game.dialog_select("mom_sex")

            "Seks di kamarku." if M_debbie.is_set("sex available") and not M_debbie.is_set("room sneak"):
                call expression game.dialog_select("debbie_dialogue_sex_in_my_room")
                $ M_debbie.set("room sneak", True)

            "Nongkrong di dalam mobil." if M_debbie.is_set("sex available"):
                call expression game.dialog_select("debbie_dialogue_sex_in_car")
                jump expression game.dialog_select("debbie_car_sex")

            "Tonton Film." if M_debbie.is_set("sex available") and not M_debbie.is_set("movie night"):
                call expression game.dialog_select("debbie_dialogue_watch_movie")
                $ M_debbie.set("movie night", True)

            "Binatu." if M_debbie.is_set("basement sex"):
                if player.location == L_home_basement:
                    label mom_basement_replay:
                        if not store._in_replay == None:
                            if randomizer() < 50:
                                jump expression game.dialog_select("basement_mom_sex")
                    call expression game.dialog_select("debbie_dialogue_laundry_sex_basement")
                    if not M_debbie.is_state(S_debbie_give_laundry) and randomizer() <= 50:
                        $ mom_basement_rand = True
                        call expression game.dialog_select("debbie_dialogue_laundry_sex_basement_random_true")
                    else:

                        $ mom_basement_rand = False
                        call expression game.dialog_select("debbie_dialogue_laundry_sex_basement_random_false")
                    $ M_debbie.set("sex speed", .4)
                    $ player.go_to(L_home_basement)
                    $ cum = False
                    $ anim_toggle = True
                    $ animated = False
                    $ xray = False
                    jump expression game.dialog_select("basement_mom_sex_loop")

                elif player.location == L_home_kitchen:
                    call expression game.dialog_select("debbie_dialogue_laundry_sex_kitchen")
                    jump expression game.dialog_select("basement_mom_sex")

            "Berciuman." if M_debbie.is_state(S_debbie_kissing_practice) and player.location == L_home_kitchen:
                call expression game.dialog_select("debbie_dialogue_kiss")
                menu:
                    "Bisakah kamu mengajariku?":
                        call expression game.dialog_select("debbie_dialogue_kiss_teach")
                        if player.stats.chr() >= 5:
                            $ display.toast(chr_pass)
                            jump expression game.dialog_select("mom_kissing_practice")
                        else:

                            $ display.toast(chr_fail)
                            call expression game.dialog_select("debbie_dialogue_kiss_teach_stat_fail")
                    "Tidak ada apa-apa.":

                        call expression game.dialog_select("debbie_dialogue_kiss_leave")

            "Berlatihlah berciuman." if M_debbie.is_set("practice kissing") and player.location == L_home_kitchen:
                call expression game.dialog_select("debbie_dialogue_kiss_practice")
                $ game.timer.tick()
            "Sudahlah.":

                call expression game.dialog_select("debbie_dialogue_leave")
    hide player
    hide old_debbie
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
