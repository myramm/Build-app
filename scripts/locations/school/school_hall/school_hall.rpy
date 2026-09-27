label school_mia_study_reminder:
    scene expression player.location.background_blur with None
    show player 4
    with dissolve
    player_name "( Hmm, now that I've caught up in French class, {b}I can help Mia with her studies{/b}. )"

    show player 1
    player_name "( I should {b}talk to her about it{/b}! )"

    return

label school_hall_dialogue:
    $ player.go_to(L_school_hall)

    if M_bissette.finished_state(S_bissette_study) and not M_mia.get("reminded study") and not game.timer.is_dark():
        call expression game.dialog_select("school_mia_study_reminder")
        $ M_mia.set("reminded study", True)

    if M_dewitt.is_state(S_dewitt_school_sneak_mission) and game.timer.is_dark():
        call school_dewitt_glue_mission_cult
        $ game.main()

    if not game.timer.is_weekend():
        if getPlayingSound("<loop 7 to 115>audio/ambience_school_hallway.ogg") and not game.timer.is_dark():
            $ playSound("<loop 7 to 115>audio/ambience_school_hallway.ogg", 1.0)

        if M_consuela.is_state(S_con02_job2) and not game.timer.is_dark():
            call con02_job2_school_hall
            $ L_hospital.unlock()
            $ player.go_to(L_hospital)
            $ M_consuela.trigger(T_con02_job2)
            $ game.main()

        if M_eve.is_state(S_eve_big_sister_problems) and game.timer.is_morning():
            call expression game.dialog_select("school_eve_big_sister_problems")
            $ M_eve.trigger(T_eve_big_sis_problem)
            $ game.main()
        elif M_eve.is_state(S_eve_apologize) and game.timer.is_day():
            call expression game.dialog_select("school_eve_apologize")
            $ M_eve.trigger(T_eve_apologized)
        elif M_eve.is_state(S_eve_school_stinker) and game.timer.is_morning():
            call expression game.dialog_select("school_eve_school_stinker")
            $ M_eve.trigger(T_eve_upset_pot)
            $ game.timer.tick()
            $ game.main()
        elif M_eve.is_state(S_eve_lesbians_aftermath) and game.timer.is_day():
            call expression game.dialog_select("school_eve_lesbians_aftermath")
            $ M_eve.trigger(T_eve_talked_about_grace_odette)
            $ game.timer.tick()
            $ player.go_to(L_school_lefthallway)
            $ game.main()

        if M_roxxy.is_state(S_roxxy_shower_event) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_shower_event")

        elif M_roxxy.is_state(S_roxxy_intense_gymercise) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_intense_gymercise")

        elif M_roxxy.is_state(S_roxxy_dexter_argument) and not M_roxxy.get("dexter argument got information") and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_dexter_argument")
            $ M_roxxy.set("dexter argument got information", True)
            $ player.go_to(L_map)
            $ game.main()

        elif M_roxxy.is_state(S_roxxy_dexter_confront) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_dexter_confront")
            $ M_roxxy.trigger(T_roxxy_do_assignment)

        elif M_roxxy.is_state(S_roxxy_assignment) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_assignment")
            $ M_roxxy.trigger(T_roxxy_study_at_roxxy)

        elif M_roxxy.is_state(S_roxxy_missing_outfit) and game.timer.is_morning():
            call expression game.dialog_select("school_roxxy_missing_outfit")
            $ M_roxxy.trigger(T_roxxy_find_cheerleader_outfit)
            $ player.go_to(L_map)
            $ game.main()

        elif M_roxxy.is_state(S_roxxy_return_to_school) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_return_to_school")
            $ M_roxxy.trigger(T_roxxy_returned_to_school)
            $ player.go_to(L_map)
            $ game.main()

        elif M_roxxy.is_state(S_roxxy_trailer_park_trouble) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_trailer_park_trouble")
            $ player.go_to(L_map)
            $ M_roxxy.trigger(T_roxxy_home_foreclosed)
            $ game.main()

        elif M_roxxy.is_state(S_roxxy_selling_meth_ask_roxxy) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_selling_meth_ask_roxxy")
            $ player.go_to(L_map)
            $ M_roxxy.trigger(T_roxxy_meth_asked_roxxy)
            $ game.main()

        elif M_roxxy.is_state(S_roxxy_shut_down_lab) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_shut_down_lab")
            $ M_roxxy.trigger(T_roxxy_failing_exams)

        elif M_roxxy.is_state(S_roxxy_give_exams) and not game.timer.is_dark():
            label roxxy_locker_rub_hscene_replay:
                call expression game.dialog_select("school_roxxy_give_exams")
            $ renpy.end_replay()
            $ persistent.cookie_jar["Roxxy"]["unlocked"] = True
            $ persistent.cookie_jar["Roxxy"]["gallery"]["03_unlocked"] = True
            $ player.remove_item("smith_exams")
            $ M_roxxy.trigger(T_roxxy_gave_exams)

        elif M_roxxy.is_state(S_roxxy_dexter_flirt) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_dexter_flirt")
            $ M_roxxy.trigger(T_roxxy_help_dewitt)

        elif M_roxxy.is_state(S_roxxy_do_pushups_intro) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_do_pushups_intro")
            $ M_roxxy.trigger(T_roxxy_dexter_challenge_pushups)
            call screen pushups_minigame

        elif M_roxxy.is_state(S_roxxy_trailer_park_romance) and game.timer.is_morning():
            call expression game.dialog_select("school_roxxy_trailer_park_romance_intro")
            menu:
                "Not right now.":
                    call expression game.dialog_select("school_roxxy_trailer_park_romance_no")
                "I can come.":

                    call expression game.dialog_select("school_roxxy_trailer_park_romance_yes")
                    $ M_roxxy.trigger(T_roxxy_accepted_picnic)

        elif M_roxxy.is_state(S_roxxy_dexter_basketball) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_dexter_basketball")
            $ M_roxxy.trigger(T_roxxy_basket_challenged)
            $ M_roxxy.set("basketball unlocked", True)
            jump basketball_minigame_prepare

        elif M_roxxy.is_state(S_roxxy_fight_dexter) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_fight_dexter")
            menu:
                "Tidak.":
                    show player 10 with dissolve
                    player_name "No, this is life or death... I should really prepare more."

                    $ player.go_to(L_map)
                    $ game.main()
                "Ya.":

                    show player 12 with dissolve
                    player_name "No more running..."

                    player_name "It's time to put {b}Dexter{/b} down for good!"

                    jump dexter_fight
            hide player with dissolve

        elif M_roxxy.get("roxxy trailer sex") >= 2 and not M_roxxy.get("roxxy locker sex") and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_locker_sex")
            call expression game.dialog_select("roxxy_locker_sex_loop_pre")
            jump expression game.dialog_select("roxxy_locker_sex_loop")

        if M_bissette.is_state(S_bissette_challenge) and not game.timer.is_dark():
            call expression game.dialog_select("school_bissette_challenge")
            $ M_bissette.trigger(T_bissette_challenge_thoughts)

            $ game.timer.tick()
            $ player.go_to(L_school_front)
            jump school_frontyard_dialogue

        if M_mia.is_state(S_mia_glasses_favor) and not game.timer.is_dark():
            call expression game.dialog_select("school_mia_glasses_favor")
            $ player.get_item("aviators")
            $ M_mia.trigger(T_mia_gives_glasses)

        if M_erik.is_state(S_erik_bully_fight) and L_school_hall.is_here(M_erik, M_dexter):
            call expression game.dialog_select("school_erik_bully_fight")
            if player.stats.dex() >= 4:
                $ display.toast(dex_pass)
                call expression game.dialog_select("school_erik_bully_fight_pass")
                $ M_erik.trigger(T_erik_bully_concuss)
                $ game.timer.tick(2)
                $ player.go_to(L_hospital_room)
                jump hospital_2nd_floor_room_dialogue
            else:
                $ display.toast(dex_fail)
                call expression game.dialog_select("school_erik_bully_fight_fail")

        elif M_roxxy.is_state(S_roxxy_start) and not game.timer.is_dark():
            call expression game.dialog_select("school_roxxy_intro_started")
            $ M_smith.trigger(T_smith_intro)
            $ M_roxxy.trigger(T_roxxy_teachers_berating)
            $ game.lock_ui()

        if M_dewitt.is_state(S_dewitt_talent_show_ask_annie) and not game.timer.is_dark():
            call expression game.dialog_select("school_hallway_dewitt_talent_show_ask_annie")

            $ M_dewitt.trigger(T_dewitt_annies_refusal)

        elif M_dewitt.is_state(S_dewitt_pre_talent_show_chat) and not game.timer.is_dark():
            call expression game.dialog_select("school_dewitt_pre_talent_show_chat")

            $ M_dewitt.trigger(T_dewitt_double_check_trap)

        if M_smith.is_state(S_smith_unlocked_locker) and not game.timer.is_dark():
            call expression game.dialog_select("school_hallway_smith_unlocked_locker")
            $ M_smith.trigger(T_smith_go_to_athletics)

        if M_diane.is_state(S_diane_delivery_3) and not game.timer.is_dark():
            call expression game.dialog_select("school_diane_delivery_3")
            $ M_diane.trigger(T_diane_make_delivery_3)
        call pa_announcement

    elif not M_dewitt.is_state(S_dewitt_school_sneak_mission) and not game.timer.is_dark():
        $ player.go_to(L_map)
        if not game.timer.is_dark():
            if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
                $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
        else:

            if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
                $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
        call expression game.dialog_select("school_weekend_lock")

    $ game.main()
    return


label school_locker_dialogue:
    $ player.go_to(L_school_locker_MC)
    if M_smith.is_state(S_smith_go_to_locker):
        call expression game.dialog_select("school_locker_smith_go_to_locker")
        $ M_smith.trigger(T_smith_unlocked_locker)

    elif M_roxxy.is_set("meet for locker sex") and not game.timer.is_dark():
        label roxxy_locker_fuck_hscene_replay:
            call expression game.dialog_select("school_roxxy_locker_sex_repeat")
        call expression game.dialog_select("roxxy_locker_sex_loop_pre")
        jump expression game.dialog_select("roxxy_locker_sex_loop")
    $ player.location.call_screen(False)
    return


label school_locker_report:
    call school_locker_report_dialogue

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
