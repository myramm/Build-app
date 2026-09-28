label bedroom_dialogue:
    if motion in route(L_map, L_home_bedroom):
        if M_anon.is_state(S_ano21_home) and game.timer.is_dark():
            $ player.go_to(L_home_entrance)
            jump entrance_dialogue

        if M_anon.is_state(S_ano27_home):
            $ player.go_to(L_home)
            jump home_front_dialogue

        if M_debbie.is_state(S_debbie_overheard):
            $ player.go_to(L_home_entrance)
            jump entrance_dialogue

        if M_erik.is_state(S_erik_bully_recovered):
            $ player.go_to(L_home_entrance)
            jump entrance_dialogue

        if M_diane.is_state(S_diane_debbie_drop_off_request) and game.timer.is_evening():
            $ player.go_to(L_home_entrance)
            jump entrance_dialogue

        if M_diane.is_state(S_diane_checkup_results):
            $ player.go_to(L_home_entrance)
            jump entrance_dialogue

        if M_roxxy.is_state(S_roxxy_studying_at_mcs):
            $ player.go_to(L_home_entrance)
            jump entrance_dialogue

    $ player.go_to(L_home_bedroom)
    $ M_player.set("on_jenny_pc", False)

    if M_player.just_wokeup:
        call expression game.dialog_select("player_just_wokeup")

    if M_mia.is_state(S_mia_tattoo_idea):
        call bedroom_mia_tattoo_idea
        $ M_mia.trigger(T_mia_tattoo_start)

    elif M_mia.is_state(S_mia_strip_aftermath):
        call expression game.dialog_select("bedroom_mia_strip_aftermath_grounded")
        $ M_mia.trigger(T_mia_grounded)

    elif M_mia.is_state(S_mia_concerning_visit):
        call expression game.dialog_select("bedroom_mia_concerning_visit")

    elif M_mia.is_state(S_mia_urgent_message):
        call expression game.dialog_select("bedroom_mia_urgent_message")
        $ player.receive_message("mia02")

    elif M_debbie.is_state(S_debbie_overheard) and game.timer.is_dark():
        call expression game.dialog_select("bedroom_mom_overheard")
        $ M_debbie.trigger(T_debbie_check)

    elif M_debbie.is_state(S_debbie_movie_afterthoughts):
        call expression game.dialog_select("bedroom_mom_movie_afterthoughts")
        $ M_debbie.trigger(T_debbie_movie_night_finish)

    elif M_debbie.is_state(S_debbie_movie_afterthoughts_two):
        call expression game.dialog_select("bedroom_mom_afterthoughts_two")
        $ M_debbie.trigger(T_debbie_movie_night_finish)

    elif M_debbie.is_state(S_debbie_note) and game.timer.is_dark():
        call expression game.dialog_select("bedroom_mom_note")

    elif M_bissette.is_state(S_bissette_french_food_assignment):
        call expression game.dialog_select("bedroom_bissette_french_food_assignment")

    elif M_dewitt.is_state(S_dewitt_make_replacement_guitar) and player.has_item("paint") and player.has_item("wood_pile"):
        call expression game.dialog_select("bedroom_dewitt_make_replacement_guitar")

    elif M_jenny.is_state(S_jenny_figure_out_password) and game.timer.is_dark() and not M_jenny.get("pc_hacked"):
        call expression game.dialog_select("bedroom_jenny_hack_computer_notice")
        $ M_jenny.set("hack_pc_notice", True)

    elif M_jenny.is_state(S_jenny_checked_for_new_video):
        call expression game.dialog_select("bedroom_jenny_checked_for_new_video")
        $ M_jenny.trigger(T_jenny_get_her_a_new_toy)

    $ game.main()

label sleeping:
    if M_anon.is_state(S_ano03_done, S_ano12_done, S_ano21_home, S_ano21_done):
        jump resume_sleeping_bedroom

    elif M_mia.is_state(S_mia_midnight_call):
        call expression game.dialog_select("bedroom_sleeping_mia_midnight_call")
        $ game.timer.tick(3)
        $ player.receive_message("mia01")
        $ game.main()

    elif M_debbie.is_state([S_debbie_romance_movie, S_debbie_romance_movie_two]):
        call expression game.dialog_select("bedroom_sleeping_debbie_movie_night")
        $ game.main()

    elif M_debbie.is_state(S_debbie_sleepover):
        call expression game.dialog_select("bedroom_sleeping_debbie_sleepover")
        $ game.main()

    elif M_debbie.is_set("room sneak"):
        jump expression game.dialog_select("bedroom_debbie_sleepover")

    elif M_erik.is_state(S_erik_bully_tired):
        call expression game.dialog_select("bedroom_erik_bully_tired")
        $ M_erik.trigger(T_erik_bully_sleep)

    elif M_erik.is_state(S_erik_thief_active) and randomizer() > 66:
        call bedroom_erik_thief_noise
        if _return:
            $ game.timer.tick(3)
            $ M_erik.trigger(T_erik_thief_spot)
            $ player.go_to(L_erikhouse)
            $ game.main()
        else:
            $ M_erik.trigger(T_erik_thief_ignore)

    elif M_dewitt.is_state(S_dewitt_eve_karaoke):
        call expression game.dialog_select("bedroom_sleeping_dewitt_eve_karaoke")
        $ game.main()

    elif M_dewitt.is_state(S_dewitt_school_sneak_mission):
        call expression game.dialog_select("bedroom_sleeping_dewitt_school_sneak_mission")
        $ game.main()

    elif M_debbie.is_state(S_debbie_solo_dream):
        call expression game.dialog_select("bedroom_sleeping_debbie_solo_dream")
        $ M_debbie.trigger(T_debbie_dream)

    elif M_debbie.is_state(S_debbie_night_visit):
        call expression game.dialog_select("bedroom_sleeping_debbie_night_visit")
        $ M_debbie.trigger(T_debbie_midnight_fun)

    elif M_debbie.is_state(S_debbie_night_visit_two):
        call expression game.dialog_select("bedroom_sleeping_debbie_night_visit_two")
        $ persistent.cookie_jar["Debbie"]["unlocked"] = True
        $ persistent.cookie_jar["Debbie"]["gallery"]["03_unlocked"] = True
        $ M_debbie.trigger(T_debbie_midnight_fun)

    elif M_debbie.is_state(S_debbie_midnight_noises):
        call expression game.dialog_select("bedroom_sleeping_debbie_midnight_noises")
        $ M_debbie.trigger(T_debbie_midnight_wakeup)
        $ game.timer.tick(3)
        $ game.main()

    elif M_debbie.is_state(S_debbie_night_visit_three):
        label mom_mc_sexvisit:
            call expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three")
        $ keep_going = 0
        $ M_debbie.set("change angle", False)
        call expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three_loop")

    elif random.randint(1, 100) <= M_jenny.max("sneak_in_chance", "forced_sneak_in_chance") and not M_jenny.pregnancy:
        jump jenny_mc_room_sex_on_sleep
    else:

        show expression game.timer.image("bedroom{}")

    label resume_sleeping_bedroom:
    if M_player.is_set("pet cat"):
        if M_jenny.get("had_sex_bedroom"):
            scene expression "backgrounds/location_home_bedroom_sleeping6.jpg" with fade
        else:
            scene location_home_bedroom_sleeping3 with fade
    else:
        if M_jenny.get("had_sex_bedroom"):
            scene expression "backgrounds/location_home_bedroom_sleeping5.jpg" with fade
        else:
            scene location_home_bedroom_sleeping with fade

    call sleep_lock_check
    call popup ('sleep')

    if M_anon.is_state(S_ano28_init):
        pass

    elif M_jenny.get('had_sex_bedroom'):
        call player_just_wokeup (woke_with=M_jenny)

    elif M_debbie.is_state(S_debbie_smith_dream):
        call bedroom_sleeping_debbie_smith_dream
        $ M_debbie.trigger(T_debbie_dream)
        $ M_player.set("just wokeup", False)

    $ checkpoint()

    jump expression game.dialog_select("bedroom_dialogue")

label jerking_off_dialogue:
    scene expression game.timer.image("bedroom{}")
    if M_diane.is_state(S_diane_peeking_masturbate):
        jump diane_masturbatory_fantasy_d17
    menu:
        "Jerk off.":
            $ A_solo_pleasure.unlock()
            menu:
                "{b}Eve{/b}." if M_player.is_set("jerk eve"):
                    call expression game.dialog_select("bedroom_sleeping_jerk_off_eve")
                    scene black with dissolve
                    $ game.timer.tick()

                "{b}Mia{/b}." if M_player.is_set("jerk mia"):
                    call expression game.dialog_select("bedroom_sleeping_jerk_off_mia")
                    scene black with dissolve
                    $ game.timer.tick()

                "{b}Roxxy{/b}." if M_player.is_set("jerk roxxy"):
                    call expression game.dialog_select("bedroom_sleeping_jerk_off_roxxy")
                    scene black with dissolve
                    $ game.timer.tick()

                "{b}[deb_name]{/b}." if M_player.is_set("jerk mom"):
                    call expression game.dialog_select("bedroom_sleeping_jerk_off_debbie")
                    scene black with dissolve
                    $ game.timer.tick()

                "{b}Diane{/b}." if M_player.is_set("jerk diane"):
                    call expression game.dialog_select("bedroom_sleeping_jerk_off_diane")
                    scene black with dissolve
                    $ game.timer.tick()

                "{b}[jen_name]{/b}." if M_player.is_set("jerk jenny"):
                    call expression game.dialog_select("bedroom_sleeping_jerk_off_jenny")
                    scene black with dissolve
                    $ game.timer.tick()
                "Never mind.":

                    pass
        "Leave.":

            pass

    $ game.main()

label diane_masturbatory_fantasy_d17:
    call expression game.dialog_select("bedroom_sleeping_jerk_off_diane")
    pause
    player_name "Mmm, {b}Diane{/b}!"
    scene expression "backgrounds/location_home_hallway_night_blur.jpg"
    show diane b_nightgown f_scared
    with dissolve
    diane @ -m_talk "( ... )"
    diane @ -m_talk "( Oh, what am I doing? )"
    pause
    diane @ -m_talk "( Am I really considering this?! )"
    pause
    player_name "Mmm, {b}Diane{/b}!"
    show diane f_surprised
    diane @ -m_talk "( !!! )" with hpunch
    diane @ -m_talk "( {b}[firstname]{/b}? )"
    scene expression "backgrounds/location_home_bedroom_cutscene11.jpg" with fade
    diane "( Is he- )"
    pause
    diane "( !!! )"
    pause
    diane "( Oh my goodness... )"
    pause
    diane "( It's so big! )"
    pause
    player_name "Haah, here it comes!"
    scene expression "backgrounds/location_home_bedroom_cutscene11b.jpg" with fade
    pause
    player_name "HNNGGG!!!"
    diane "( !!! )" with hpunch
    pause
    diane "( Look at all that cum! )"
    pause
    player_name "Ahh, {b}Diane{/b}!"
    pause
    scene expression "backgrounds/location_home_bedroom_cutscene12.jpg" with fade
    diane "( All of that... Was for me? )"
    pause
    player_name "Haah... Haah..."
    scene black with fade
    diane "{b}[firstname]{/b}?"
    scene expression "backgrounds/location_home_bedroom_sex03.jpg"
    show player afterjerk 1
    show diane b_nightgown f_smirk
    player_name "!!!" with hpunch
    player_name "{b}Diane{/b}?"
    player_name "What are you-"
    show player afterjerk 2
    show diane f_reading_intrigued
    diane "Shh."
    show diane b_nightgown_sit f_smirk_fardown with dissolve
    diane "I had no idea you-"
    show diane b_nightgown_sit_stroke1
    pause
    show diane b_nightgown_sit_stroke2
    diane "T-there's so much..."
    show player afterjerk 1
    player_name "Y-yeah."
    show diane b_nightgown_sit_kiss
    player_name "!!!" with hpunch
    show player afterjerk 3
    pause
    show player afterjerk 2
    show diane b_nightgown_sit_stroke
    diane "Mmm, I think I want to do this {b}[firstname]{/b}..."
    diane "I want you to breed me."
    show player afterjerk 1
    player_name "Y-you do?"
    show player afterjerk 2
    diane "Mmmhmm!"
    show player afterjerk 1
    player_name "What about {b}[deb_name]{/b}?"
    show player afterjerk 2
    diane "When the time comes, I'll speak with her."
    diane "I'll just have to hope she can forgive me..."
    show player afterjerk 1
    player_name "I think she'll understand, {b}Diane{/b}."
    show player afterjerk 3
    show diane b_nightgown_sit_kiss
    with dissolve
    diane "Mmm."
    pause
    show player afterjerk 2
    show diane b_nightgown_sit_stroke
    with dissolve
    diane "Oh, I want you inside me so bad!"
    diane "... But not yet!"
    player_name "Hmm?"
    diane "I want our first time to be special."
    diane "{b}Come see me tomorrow at the barn{/b}."
    show player afterjerk 1
    player_name "O-okay."
    show player afterjerk 3
    show diane b_nightgown_sit_kiss
    with dissolve
    pause
    show diane b_nightgown_sit
    show player afterjerk 2
    diane "Goodnight, stud."
    show player afterjerk 1
    player_name "Goodnight, {b}Diane{/b}..."
    hide diane with dissolve
    pause
    show player afterjerk 1
    player_name "( Yeah, like I'm really gonna be able to sleep after that... )"
    hide player with dissolve
    $ M_diane.trigger(T_diane_learns_your_secret)
    $ game.timer.tick()
    $ game.unlock_ui()
    $ game.main()
    return

label home_bedroom_drawing2:
    call home_bedroom_drawing2_dialogue

    $ game.main()
    return

label home_bedroom_picture3:
    call home_bedroom_picture3_dialogue

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
