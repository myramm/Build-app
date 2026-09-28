label odette_button_dialogue_legacy:
    scene expression player.location.background_blur

    if M_odette.pregnancy:
        jump odette_button_pregnancy_dialogue

    if M_eve.is_state(S_eve_big_sis_talk_odette):
        call expression game.dialog_select("button_odette_eve_big_sis_talk_odette")
        $ M_eve.trigger(T_eve_big_sis_talked_to_odette)
        $ game.main()
    elif M_eve.is_state(S_eve_big_sis_check_apartment):
        call expression game.dialog_select("button_odette_eve_big_sis_check_apartment")
        $ game.main()
    elif M_eve.is_state(S_eve_pot_cheerup, S_eve_pot_look_for_eve):
        call expression game.dialog_select("button_grace_odette_eve_pot_cheerup")
        $ player.go_to(L_tattooparlor)
        $ game.main()
    elif M_eve.is_state(S_eve_bike_breakdown_check_bike) and game.timer.is_weekend() and not game.timer.is_night():
        call expression game.dialog_select("button_odette_eve_bike_breakdown_check_bike")
        $ M_eve.trigger(T_eve_bike_breakdown_check_bike)
        $ player.go_to(L_tattooparlor)
        $ game.lock_ui()
        $ game.main()
    elif M_eve.is_state(S_eve_clients_wake_up_grace) and game.timer.is_day():
        call expression game.dialog_select("button_odette_eve_clients_wake_up_grace")
        $ game.main()
    elif M_eve.is_state(S_eve_party_speak_to_odette) and L_tattooparlor_roof.is_here(M_odette):
        call expression game.dialog_select("button_odette_eve_party_speak_to_odette")
        $ M_eve.trigger(T_eve_party_spoke_to_odette)
        $ game.main()
    elif M_eve.is_state(S_eve_party_speak_to_tuuku) and L_tattooparlor_roof.is_here(M_odette):
        call expression game.dialog_select("button_odette_eve_party_speak_to_tuuku")
        $ game.main()
    elif M_eve.is_state(S_eve_make_up_grace_upset):
        call expression game.dialog_select("button_odette_eve_make_up_grace_upset")
        $ M_eve.trigger(T_eve_make_up_mall)
        $ game.main()
    elif not M_odette.proposed_sex and M_eve.finished_state(S_eve_make_up_dress_table) and player.location == L_tattooparlor_garage:
        $ M_odette.set('proposed_sex', True)
        call expression game.dialog_select("button_odette_sex_proposal")
        menu:
            "Okay.":
                call expression game.dialog_select("button_odette_sex_proposal_okay")
                jump odette_1st_sex_bike
            "No, I can't.":
                call expression game.dialog_select("button_odette_sex_proposal_no")
                $ game.main()

    elif L_tattooparlor_interior.is_here(M_odette):
        if M_eve.between_states(S_eve_start, S_eve_big_sister_problems):
            call expression game.dialog_select("button_odette_intro_interior_e1e5")
            $ game.main()
        elif M_eve.between_states(S_eve_big_sister_problems, S_eve_detention):
            call expression game.dialog_select("button_odette_intro_interior_e6e14")
        elif M_eve.between_states(S_eve_detention, S_eve_make_up_dress_table):
            call expression game.dialog_select("button_odette_intro_interior_e15e20")
        else:
            call expression game.dialog_select("button_odette_intro_interior_e21")
    elif L_tattooparlor_garage.is_here(M_odette):
        if M_eve.between_states(S_eve_big_sister_problems, S_eve_detention):
            call expression game.dialog_select("button_odette_intro_garage_e6e14")
        elif M_eve.between_states(S_eve_detention, S_eve_make_up_dress_table):
            call expression game.dialog_select("button_odette_intro_garage_e15e20")
        else:
            call expression game.dialog_select("button_odette_intro_garage_e21")

    menu odette_menu_dialogue:
        "Party." if M_eve.is_state(S_eve_party_start) and game.timer.is_weekday():
            call expression game.dialog_select("odette_button_party_start")
            jump odette_menu_dialogue

        "Are you alright?" if M_eve.between_states(S_eve_big_sister_problems, S_eve_detention) and player.location == L_tattooparlor_garage:
            call expression game.dialog_select("button_odette_are_you_alright_1")
            jump odette_menu_dialogue

        "YES!" if M_odette.proposed_sex and player.location == L_tattooparlor_garage and not M_odette.hide_sex_proposal_options:
            if M_odette.bike_1st_time:
                call expression game.dialog_select("button_odette_wanna_fool_around_first_time")
                jump odette_1st_sex_bike
            call expression game.dialog_select("button_odette_accept_sex")
            $ M_odette.set("hide_sex_proposal_options", True)
            jump odette_sex_menu_options

        "No, thanks." if M_odette.proposed_sex and player.location == L_tattooparlor_garage and not M_odette.hide_sex_proposal_options:
            call expression game.dialog_select("button_odette_refuse_sex")
            $ M_odette.set("hide_sex_proposal_options", True)
            jump odette_menu_dialogue

        "Graveyard visit." if M_odette.is_state(S_ode01_done, S_ode02_init):
            call ode02_init_odette
            jump odette_menu_dialogue

        "The crypt?" if M_odette.finished_state(S_ode02_warn):
            call button_odette_crypt
            jump odette_menu_dialogue

        "Have you seen {b}Eve{/b}?" if player.location == L_tattooparlor_garage:
            call expression game.dialog_select("button_odette_have_you_seen_eve")
            jump odette_menu_dialogue

        "What are you reading?" if player.location == L_tattooparlor_interior:
            call expression game.dialog_select("button_odette_what_are_you_reading")
            jump odette_menu_dialogue

        "{b}Grace{/b} and {b}Tuuku{/b}?" if M_eve.between_states(S_eve_big_sister_problems, S_eve_detention) and player.location == L_tattooparlor_interior:
            call expression game.dialog_select("button_odette_grace_and_tuuku")
            jump odette_menu_dialogue

        "Are you alright?" if M_eve.between_states(S_eve_detention, S_eve_party_speak_to_tuuku) and player.location == L_tattooparlor_garage:
            call expression game.dialog_select("button_odette_are_you_alright_2")
            jump odette_menu_dialogue

        "Big fella?" if M_eve.finished_state(S_eve_detention):
            call expression game.dialog_select("button_odette_big_fella")
            jump odette_menu_dialogue

        "Progress with {b}Eve{/b}?" if M_eve.finished_state(S_eve_make_up_dress_table) and player.location == L_tattooparlor_interior:
            call expression game.dialog_select("button_odette_progress_with_eve")
            menu:
                "No way.":
                    call expression game.dialog_select("button_odette_progress_with_eve_no_way")
                "I'll think about it.":
                    call expression game.dialog_select("button_odette_progress_with_eve_think_about_it")
            jump odette_menu_dialogue

        "You and {b}Grace{/b}?" if M_eve.finished_state(S_eve_make_up_dress_table):
            call expression game.dialog_select("button_odette_you_and_grace")
            jump odette_menu_dialogue

        "Wanna fool around?" if M_odette.proposed_sex and player.location == L_tattooparlor_interior and not L_tattooparlor_interior.is_here(M_grace):
            if M_odette.bike_1st_time:
                call expression game.dialog_select("button_odette_wanna_fool_around_first_time")
                jump odette_1st_sex_bike
            call expression game.dialog_select("button_odette_wanna_fool_around")
            if _return:
                menu odette_sex_menu_options:
                    "On the couch. {color=fffa}[[Boobjob]{/color}":
                        call odette_repeat_boobjob
                    "On the couch. {color=fffa}[[Sex]{/color}":
                        call odette_repeat_sex_couch
                    "On the bike. {color=fffa}[[Sex]{/color}":
                        jump odette_repeat_sex_bike

            $ game.timer.tick()
            $ player.go_to(L_tattooparlor)

        "Never mind." if not (M_eve.finished_state(S_eve_make_up_dress_table) and player.location == L_tattooparlor_garage):
            if game.timer.is_morning():
                call expression game.dialog_select("button_odette_nevermind_morning")
            else:
                call expression game.dialog_select("button_odette_nevermind_generic")

        "I should go." if (M_eve.finished_state(S_eve_make_up_dress_table) and player.location == L_tattooparlor_garage):
            call expression game.dialog_select("button_odette_i_should_go")

    $ M_odette.set("hide_sex_proposal_options", False)

    $ game.main()

label odette_button_pregnancy_dialogue:
    if M_odette.pregnancy.character_bedridden:
        call expression game.dialog_select("button_odette_pregnancy_bedridden")
    elif L_tattooparlor_bathroom.is_here(M_odette):
        jump button_odette_pregnancy_bathroom_stage_4
    elif M_odette.pregnancy.gave_birth:
        call expression game.dialog_select("button_odette_pregnancy_gave_birth_intro")
    else:
        call expression game.dialog_select("button_odette_pregnancy_intro_{}".format(M_odette.pregnancy.stage))

    menu odette_menu_preg:
        "How are you feeling?" if M_odette.pregnancy.stage < 5:
            call expression game.dialog_select("button_odette_pregnancy_how_feeling_{}".format(M_odette.pregnancy.stage))
            jump odette_menu_preg

        "Yup." if M_odette.pregnancy.character_bedridden:
            call expression game.dialog_select("button_odette_pregnancy_yup")

        "Can I get you anything?" if M_odette.pregnancy.stage < 5:
            call expression game.dialog_select("button_odette_pregnancy_get_anything_{}".format(M_odette.pregnancy.stage))
            jump odette_menu_preg

        "You guys need anything?" if M_odette.pregnancy.gave_birth:
            call expression game.dialog_select("button_odette_pregnancy_gave_birth_need_anything")
            jump odette_menu_preg

        "I'll leave you be." if M_odette.pregnancy.gave_birth:
            call expression game.dialog_select("button_odette_pregnancy_gave_birth_leave")

        "I'll leave you be." if M_odette.pregnancy.stage < 5:
            call expression game.dialog_select("button_odette_pregnancy_leave_stage_{}".format(M_odette.pregnancy.stage))
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
