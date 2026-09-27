label entrance_dialogue:
    $ player.go_to(L_home_entrance)
    if not game.timer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if M_anon.is_state(S_ano01_cops):
        call ano01_cops_home_entrance
        $ M_anon.trigger(T_ano01_cops)

    elif M_anon.is_state(S_ano21_home) and game.timer.is_dark():
        call ano21_home_home_lobby
        $ M_anon.trigger(T_ano21_home)

    elif M_anon.is_state(S_ano27_yumi):
        call ano27_yumi_home_lobby
        $ game.timer.tick()
        $ player.go_to(L_home)
        $ M_anon.trigger(T_ano27_yumi)

    elif M_anon.is_state(S_ano28_food):
        pass

    elif M_jenny.is_state(S_jen0m_food):
        $ game.main()

    elif M_nadya.is_state(S_nad01_thug):
        call nad01_thug_home_lobby
        $ M_nadya.trigger(T_nad01_thug)

    elif M_roxxy.is_state(S_roxxy_studying_at_mcs):
        call home_roxxy_studying_at_mcs
        $ player.go_to(L_home_bedroom)
        $ M_roxxy.trigger(T_roxxy_get_cheerleader)
        $ game.main()

    elif M_roxxy.is_state(S_roxxy_cookies_and_milk):
        call expression game.dialog_select("home_front_roxxy_cookies_and_milk")
        $ game.timer.tick(1)
        $ M_roxxy.trigger(T_roxxy_go_to_police)
        $ player.go_to(L_map)
        $ game.main()

    elif M_jenny.pregnancy.stage == 2 and M_jenny.pregnancy.first_baby and M_jenny.get("didnt_see_first_baby_dialogue"):
        call expression game.dialog_select("entrance_jenny_first_baby_stage_2_intro")
        if M_diane.finished_state(S_diane_check_barn_out):
            call expression game.dialog_select("entrance_jenny_first_baby_stage_2_diane")
        else:
            call expression game.dialog_select("entrance_jenny_first_baby_stage_2_no_diane")
        call expression game.dialog_select("entrance_jenny_first_baby_stage_2_end")
        $ M_jenny.set("didnt_see_first_baby_dialogue", False)
        $ player.go_to(L_home_livingroom)
        $ game.main()

    elif M_jenny.pregnancy.stage == 5 and M_jenny.pregnancy.first_baby and M_jenny.pregnancy.gave_birth and M_jenny.get("jenny_got_first_baby"):
        call expression game.dialog_select("entrance_jenny_pregnancy_first_baby_coming_home")
        $ M_jenny.set("jenny_got_first_baby", True)

    if M_erik.is_state(S_erik_bully_visit):
        call expression game.dialog_select("entrance_erik_bully_intro")
        $ M_erik.trigger(T_erik_bully_concern)

    if M_erik.is_state(S_erik_bully_recovered):
        call expression game.dialog_select("entrance_erik_bully_return")
        $ M_erik.trigger(T_erik_bully_debrief)

    if M_jenny.is_state(S_jenny_debbie_altercation) and game.timer.is_tick(1, 2):
        call expression game.dialog_select("entrance_jenny_debbie_altercation")
        $ M_jenny.trigger(T_jenny_altercation_with_debbie)

    elif M_jenny.is_state(S_jenny_catch_her_leaving):
        if not M_jenny.get("j10_caught_her_leaving"):
            $ M_jenny.set("j10_caught_her_leaving", True)
            call expression game.dialog_select("entrance_jenny_catch_her_leaving")
            if M_jenny.get("dominance") <= 0:
                call expression game.dialog_select("entrance_jenny_catch_her_leaving_sub_first")
            else:
                call expression game.dialog_select("entrance_jenny_catch_her_leaving_dom_first")
        else:
            call expression game.dialog_select("entrance_jenny_catch_her_leaving_repeat")
        if player.has_money(200):
            if M_jenny.get("dominance") <= 0:
                call expression game.dialog_select("entrance_jenny_catch_her_leaving_has_money_sub")
            else:
                call expression game.dialog_select("entrance_jenny_catch_her_leaving_has_money_dom")
            $ player.spend_money(200)
            $ M_jenny.trigger(T_jenny_leave_house)
        else:
            if M_jenny.get("dominance") <= 0:
                call expression game.dialog_select("entrance_jenny_catch_her_leaving_no_money_sub")
            else:
                if not M_jenny.get("j10_caught_her_leaving"):
                    call expression game.dialog_select("entrance_jenny_catch_her_leaving_no_money_dom_first")
                else:
                    call expression game.dialog_select("entrance_jenny_catch_her_leaving_no_money_dom")

    elif M_jenny.is_state(S_jenny_catch_her_jilling) and game.timer.is_evening():
        $ player.go_to(L_home_livingroom)
        call expression game.dialog_select("entrance_jenny_catch_her_jilling")
        jump jenny_couch_fj_loop

    elif M_jenny.is_state(S_jenny_want_some_breakfast) and game.timer.is_weekend() and game.timer.is_morning():
        call expression game.dialog_select("entrance_jenny_want_some_breakfast")
        $ player.go_to(L_home_kitchen)
        $ M_jenny.trigger(T_jenny_pool_talk)
        $ game.main()

    if M_mia.is_state(S_mia_angelicas_impatience):
        call expression game.dialog_select("entrance_mia_angelicas_impatience")
        $ M_mia.trigger(T_angelica_house_visit)


    elif M_mia.is_state(S_mia_angelicas_home_visit):
        call expression game.dialog_select("entrance_mia_angelicas_home_visit")
        $ M_mia.trigger(T_angelica_requires_whip)


    elif M_mia.is_state(S_mia_angelicas_final_home_visit):
        call expression game.dialog_select("entrance_mia_angelicas_final_home_visit")
        $ M_mia.trigger(T_angelica_strapon_request)



    if M_anon.is_state(S_ano01_done, S_ano02_done) and game.timer.is_morning():
        pass

    elif M_mia.is_state(S_mia_strip_aftermath) and game.timer.is_dark():
        pass

    elif M_debbie.is_state(S_debbie_overheard):
        call expression game.dialog_select("entrance_mom_overheard")
        $ M_debbie.trigger(T_debbie_check)


    elif M_debbie.is_state(S_debbie_lawn_help) and not game.timer.is_dark():
        call expression game.dialog_select("entrance_mom_lawn_help")
        $ M_debbie.trigger(T_debbie_help_mow)

    elif M_debbie.is_state(S_debbie_clothes_dirty):
        call expression game.dialog_select("entrance_mom_clothes_dirty")
        $ M_debbie.trigger(T_debbie_sis_bitch)

    elif M_debbie.is_state(S_debbie_pipe_help) and game.timer.is_morning():
        call expression game.dialog_select("entrance_mom_pipe_help")
        $ M_debbie.trigger(T_debbie_broken_pipe)

    elif M_debbie.is_state(S_debbie_movie_night) and game.timer.is_evening():
        call expression game.dialog_select("entrance_mom_movie_night")
        $ M_debbie.trigger(T_debbie_movie_invite)


    elif M_debbie.is_state(S_debbie_hang_out) and not game.timer.is_dark():
        call expression game.dialog_select("entrance_mom_hang_out")
        menu:
            "Ya.":
                call expression game.dialog_select("entrance_mom_hang_out_yes")
                $ M_debbie.trigger(T_debbie_hang_out_accept)
            "Tidak.":


                call expression game.dialog_select("entrance_mom_hang_out_no")
                $ M_debbie.trigger(T_debbie_hang_out_refuse)
        hide old_debbie
        hide player
        with dissolve

    elif M_debbie.is_state(S_debbie_spy) and not game.timer.is_dark():
        call expression game.dialog_select("entrance_mom_spy")

    elif M_debbie.is_state(S_debbie_kissing_practice) and not game.timer.is_dark():
        call expression game.dialog_select("entrance_mom_kissing_practice")

    elif M_debbie.is_state(S_debbie_car_broken) and game.timer.is_morning():
        call expression game.dialog_select("entrance_mom_car_broken")
        $ M_debbie.trigger(T_debbie_car_help)

    elif M_debbie.is_state(S_debbie_panties_masturbation_again) and not game.timer.is_dark():
        if L_home_basement.is_here(M_debbie):
            $ temp = "Basement"
        else:
            $ temp = "Kitchen"
        call expression game.dialog_select("entrance_mom_panties_masturbation_again")

    elif M_debbie.is_state(S_debbie_diane_visit) and game.timer.is_evening():
        call expression game.dialog_select("entrance_mom_diane_visit")

    elif M_debbie.is_state(S_debbie_midnight_search):
        jump mom_midnight_swim

    if M_diane.is_state(S_diane_debbie_evening_visit) and game.timer.is_evening():
        call expression game.dialog_select("entrance_diane_debbie_evening_visit_overhear")

    elif M_diane.is_state(S_diane_debbie_drop_off_request) and game.timer.is_evening():
        call expression game.dialog_select("entrance_diane_debbie_drop_off_request")
        $ player.go_to(L_diane_yard)
        $ M_diane.trigger(T_diane_debbie_request)

    elif M_diane.is_state(S_diane_couch_crashing):
        call expression game.dialog_select("entrance_diane_couch_crashing")
        $ M_diane.trigger(T_diane_moved_in)
        $ game.timer.tick(3)
        $ game.main()

    elif M_diane.is_state(S_diane_peeking) and game.timer.is_evening():
        call expression game.dialog_select("entrance_diane_peeking")

    elif M_diane.is_state(S_diane_checkup_results):
        call expression game.dialog_select("entrance_diane_checkup_results")
        $ M_diane.trigger(T_diane_package_block)
        $ game.timer.tick(3)
        $ game.main()

    if M_bissette.is_state(S_bissette_roxxy_jenny_mentoring) and game.timer.is_afternoon():
        if not M_roxxy.get("roxxy trailer sex"):
            call expression game.dialog_select("entrance_bissette_roxxy_jenny_mentoring")
        else:

            call expression game.dialog_select("entrance_bissette_roxxy_jenny_mentoring_sex")
        $ M_bissette.trigger(T_bissette_roxxy_jenny_hangout)

    if game.timer.is_evening() and M_diane.pregnancy.stage >= 5 and not M_diane.pregnancy.character_bedridden and not M_diane.pregnancy.gave_birth_dialogue_seen:
        call expression game.dialog_select("entrance_diane_gave_birth_dialogue_seen")
        $ M_diane.pregnancy.set('gave_birth_dialogue_seen')

    $ game.main()

label vacuum_dialogue:
    call expression game.dialog_select("entrance_mom_vacuum")
    menu:
        "Let me help.":
            call expression game.dialog_select("entrance_mom_vacuum_yes")
            $ game.timer.tick()
            $ M_debbie.trigger(T_debbie_vacuumed)
        "It's too loud.":
            call expression game.dialog_select("entrance_mom_vacuum_no")
    $ M_debbie.set("chores", False)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
