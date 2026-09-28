label grace_button_dialogue:
    scene expression player.location.background_closeup

    if M_grace.pregnancy:
        jump grace_button_pregnancy_dialogue

    if M_mia.is_state(S_mia_buy_tattoo) and player.location.is_here(M_mia):
        call expression game.dialog_select("button_grace_mia_get_tattoo")
    elif M_eve.is_state(S_eve_distract_grace):
        call expression game.dialog_select("button_grace_distract_grace")
        $ M_eve.trigger(T_eve_distracted_grace)
        $ game.main()
    elif M_eve.is_state(S_eve_bathroom_break):
        call expression game.dialog_select("button_grace_bathroom_break")
        $ game.main()
    elif M_eve.is_state(S_eve_pot_cheerup, S_eve_pot_look_for_eve):
        call expression game.dialog_select("button_grace_odette_eve_pot_cheerup")
        $ player.go_to(L_tattooparlor)
        $ game.main()
    elif M_eve.is_state(S_eve_talk_to_girls, S_eve_talked_to_eve):
        call expression game.dialog_select("grace_button_eve_talk_to_girls")
        if M_eve.is_state(S_eve_talked_to_eve):
            call expression game.dialog_select("eve_button_eve_talked_to_both_girls")
            $ game.timer.tick(3)
            $ player.go_to(L_map)
        hide anon with dissolve
        $ M_eve.trigger(T_eve_talked_to_grace)
        $ game.main()
    elif M_eve.is_state(S_eve_talked_to_grace):
        call expression game.dialog_select("grace_button_talked_to_grace")
        $ game.main()
    elif M_eve.is_state(S_eve_party_speak_to_grace):
        call expression game.dialog_select("grace_button_party_speak_to_grace")
        $ M_eve.trigger(T_eve_party_spoke_to_grace)
        $ game.main()
    elif M_eve.is_state(S_eve_party_speak_to_jenny, S_eve_party_speak_to_odette):
        call expression game.dialog_select("grace_button_party_generic")
        $ game.main()
    elif M_eve.is_state(S_eve_party_speak_to_tuuku):
        call expression game.dialog_select("grace_button_party_speak_to_tuuku")
        $ game.main()
    elif M_eve.is_state(S_eve_clients_take_care_clients) and game.timer.is_day():
        call expression game.dialog_select("tattoo_parlor_interior_eve_clients_take_care_clients")
        $ M_eve.trigger(T_eve_took_care_clients)
        $ game.timer.tick()
        $ game.main()
    elif M_eve.between_states(S_eve_start, S_eve_visit_bedroom):
        call expression game.dialog_select("grace_button_intro_e1e5")
    elif M_eve.between_states(S_eve_visit_bedroom, S_eve_voyeurism_follow_tent):
        call expression game.dialog_select("grace_button_intro_e5e14")
    elif M_eve.between_states(S_eve_voyeurism_follow_tent, S_eve_make_up_dress_table):
        call expression game.dialog_select("grace_button_intro_e14e20")
    elif player.location == L_tattooparlor_interior:
        call expression game.dialog_select("grace_button_intro_final_tattoo")
    elif player.location == L_tattooparlor_apartment:
        if game.timer.is_weekend() and game.timer.is_evening() and not M_odette.pregnancy and M_eve.finished_state(S_eve_make_up_dress_table):
            jump grace_button_livingroom_dialogue
        else:
            call expression game.dialog_select("grace_button_intro_final_apartment")

    show grace f_normal
    menu grace_menu_dialogue:
        "Tattoo." if M_mia.is_state(S_mia_buy_tattoo) and player.location.is_here(M_mia):
            call expression game.dialog_select("button_grace_tattoo_mia")
            menu:
                "I'll help you." if player.has_money(200):
                    call expression game.dialog_select("button_grace_tattoo_help")
                    $ player.spend_money(200)
                    $ game.timer.tick()
                    $ M_mia.trigger(T_mia_tattoo_done)
                "Come back later.":

                    call expression game.dialog_select("button_grace_tattoo_come_back")

        "Tattoo." if not M_mia.is_state(S_mia_buy_tattoo) and not player.location.is_here(M_mia) and M_eve.between_states(S_eve_start, S_eve_visit_bedroom):
            call expression game.dialog_select("button_grace_tattoo")
            jump grace_menu_dialogue

        "Paint." if M_ross.is_state(S_ross_get_paint_grace) and L_tattooparlor_interior.is_here(M_grace) and not player.has_item("ink"):
            call expression game.dialog_select("button_grace_paint")
            $ M_ross.set("talked to grace", True)

        "Party." if M_eve.is_state(S_eve_party_start) and game.timer.is_weekday():
            call expression game.dialog_select("grace_button_party_start")
            jump grace_menu_dialogue

        "You look familiar." if M_grace.is_state(S_grace_start) and not player.location.is_here(M_mia) and L_tattooparlor_interior.is_here(M_grace) and not M_eve.finished_state(S_eve_visit_tattoo_shop):
            call expression game.dialog_select("button_grace_you_look_familiar")
            $ M_grace.trigger(T_grace_intro)
            jump grace_menu_dialogue

        "Yup." if M_eve.between_states(S_eve_visit_bedroom, S_eve_voyeurism_follow_tent):
            call expression game.dialog_select("button_grace_yup")
            jump grace_menu_dialogue

        "{b}Odette{/b} and {b}Tuuku{/b}?" if M_eve.between_states(S_eve_visit_bedroom, S_eve_make_up_dress_table):
            call expression game.dialog_select("button_grace_odette_and_tuuku")
            jump grace_menu_dialogue

        "How's work going?" if M_eve.finished_state(S_eve_big_sis_check_apartment):
            if M_eve.finished_state(S_eve_clients_take_care_clients):
                call expression game.dialog_select("button_grace_how_work_going_e18")
            else:
                call expression game.dialog_select("button_grace_how_work_going_e6")
            jump grace_menu_dialogue

        "Apologize." if M_eve.between_states(S_eve_police_trouble, S_eve_make_up_dress_table):
            call expression game.dialog_select("button_grace_apologize")
            jump grace_menu_dialogue

        "{b}Eve{/b} around?" if M_eve.between_states(S_eve_voyeurism_follow_tent, S_eve_make_up_dress_table):
            call expression game.dialog_select("button_grace_eve_around")
            jump grace_menu_dialogue

        "Bike." if M_eve.finished_state(S_eve_bike_breakdown_start_repair):
            call expression game.dialog_select("button_grace_bike")
            jump grace_menu_dialogue

        "Really?" if M_eve.finished_state(S_eve_make_up_dress_table) and player.location == L_tattooparlor_interior:
            call expression game.dialog_select("button_grace_really")
            jump grace_menu_dialogue

        "You and {b}Odette{/b}?" if M_eve.finished_state(S_eve_make_up_dress_table):
            call expression game.dialog_select("button_grace_you_and_odette")
            jump grace_menu_dialogue

        "Is she here?" if player.location == L_tattooparlor_apartment:
            call expression game.dialog_select("button_grace_is_she_here")
            jump grace_menu_dialogue

        "Why do you meditate naked?" if player.location == L_tattooparlor_apartment and M_eve.finished_state(S_eve_make_up_dress_table):
            call expression game.dialog_select("button_grace_why_meditate_naked")
            jump grace_menu_dialogue

        "Massage?" if not M_grace.sex_1st_time and player.location == L_tattooparlor_apartment:
            call gra01_init_grace
            $ game.timer.tick()
            $ player.go_to(L_tattooparlor_fire_escape)

        "Never mind." if M_eve.between_states(S_eve_start, S_eve_voyeurism_follow_tent):
            call expression game.dialog_select("button_grace_nevermind")

        "I should go." if M_eve.between_states(S_eve_voyeurism_follow_tent, S_eve_make_up_dress_table):
            call expression game.dialog_select("button_grace_i_should_go")

        "Just saying hi." if M_eve.finished_state(S_eve_make_up_dress_table):
            call expression game.dialog_select("button_grace_just_saying_hi")

    $ game.main()

label grace_button_livingroom_dialogue:
    if M_odette.bike_1st_time or not M_eve.is_state(S_eve_end):
        call expression game.dialog_select("button_grace_livingroom_intro_no_threesome")
        $ game.main()
        return

    elif M_grace.sex_1st_time:
        $ M_grace.set('sex_1st_time', False)
        call expression game.dialog_select("grace_button_massage_sex_proposal")
        $ M_grace.set("grace_massage_alone", False)
        menu:
            "Yeah.":
                call expression game.dialog_select("grace_button_massage_sex_proposal_yeah")
            "I dunno.":
                call expression game.dialog_select("grace_button_massage_sex_proposal_dunno")
        jump grace_sex_massage_first_time

    call expression game.dialog_select("button_grace_livingroom_intro")
    menu grace_menu_livingroom:
        "Yes, please!":
            call expression game.dialog_select("button_grace_livinroom_yes_please")
            jump grace_odette_sex_massage_repeat
        "Speak with {b}Odette{/b}?":

            call expression game.dialog_select("button_grace_livingroom_speak_with_odette")
            menu:
                "Yeah.":
                    call expression game.dialog_select("button_grace_livinroom_odette_yeah")
                    jump odette_repeat_sex_bike.segue
                "No, thanks.":

                    call expression game.dialog_select("button_grace_livingroom_odette_no")
                    $ game.main()
        "No, thanks.":

            call expression game.dialog_select("button_grace_livingroom_no_thanks")
    $ game.main()

label grace_button_pregnancy_dialogue:
    if M_grace.pregnancy.character_bedridden:
        call expression game.dialog_select("button_grace_pregnancy_bedridden_intro")
    elif L_tattooparlor_bathroom.is_here(M_grace):
        jump button_grace_pregnancy_bathroom_4
    elif M_grace.pregnancy.gave_birth:
        call expression game.dialog_select("button_grace_pregnancy_gave_birth_intro")
    else:
        call expression game.dialog_select("button_grace_pregnancy_intro")
    menu grace_menu_pregnancy_dialogue:
        "How are you feeling?" if M_grace.pregnancy.stage < 5:
            call expression game.dialog_select("button_grace_pregnancy_how_are_you_feeling_{}".format(M_grace.pregnancy.stage))
            jump grace_menu_pregnancy_dialogue

        "Can I get you anything?" if M_grace.pregnancy.stage < 5:
            call expression game.dialog_select("button_grace_get_you_something_{}".format(M_grace.pregnancy.stage))
            jump grace_menu_pregnancy_dialogue

        "Yup." if M_grace.pregnancy.character_bedridden:
            call expression game.dialog_select("button_grace_pregnancy_bedridden_yup")

        "You guys need anything?" if M_grace.pregnancy.gave_birth:
            call expression game.dialog_select("button_grace_pregnancy_need_anything_babies")
            jump grace_menu_pregnancy_dialogue

        "I'll leave you be." if not M_grace.pregnancy.character_bedridden:
            if M_grace.pregnancy.gave_birth:
                call expression game.dialog_select("button_grace_ill_leave_you_be_baby")
            else:
                call expression game.dialog_select("button_grace_ill_leave_you_be")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
