label hallway_dialogue:
    $ player.go_to(L_home_hallway)
    if getPlayingSound("<loop 1>audio/ambience_shower_hallway.ogg") and game.in_shower is not None:
        $ playSound("<loop 1>audio/ambience_shower_hallway.ogg")

    if M_anon.is_state(S_ano02_next) and not M_jenny.once('ano02_next'):
        call anon02_next_home_hallway

    if M_jenny.is_state(S_jenny_start) and not game.timer.is_dark():
        call expression game.dialog_select("hallway_jenny_start")
        call jen_name_input_label (True)
        $ M_jenny.trigger(T_jenny_hallway)

    elif M_jenny.is_state(S_jenny_hallway_eavesdropping) and game.timer.is_dark():
        call expression game.dialog_select("hallway_jenny_hallway_eavesdropping")
        $ M_jenny.trigger(T_jenny_eavesdropped)
        $ player.spend_money(100)

    elif M_jenny.is_state(S_jenny_confront_her_hallway):
        call expression game.dialog_select("hallway_jenny_confront_her_hallway")
        $ M_jenny.trigger(T_jenny_wait_a_day)

    elif M_jenny.is_state(S_jenny_caught_talking_to_camslut) and game.timer.is_tick(2, 3):
        call expression game.dialog_select("hallway_jenny_caught_talking_to_camslut")
        $ game.timer.tick()
        $ player.go_to(L_home_bedroom)
        $ M_jenny.trigger(T_jenny_beaten_up_with_dildo)
        $ game.main()

    elif M_jenny.is_state(S_jenny_hallway_talk) and game.timer.is_morning():
        call expression game.dialog_select("hallway_jenny_hallway_talk")
        $ M_jenny.trigger(T_jenny_diary_clue)
        $ game.timer.tick()
        $ game.main()

    elif M_jenny.is_state(S_jen0m_food):
        $ game.main()

    if L_home_shower.is_here(M_jenny) and not game.timer.is_dark() and not M_jenny.get("seen_in_shower"):
        call expression game.dialog_select("hallway_jenny_in_shower")
        $ M_jenny.set("seen_in_shower", True)

    if M_debbie.is_state(S_debbie_sis_boobs_afterthoughts) and not game.timer.is_dark():
        call expression game.dialog_select("hallway_mom_sis_boobs_afterthoughts")
        $ M_debbie.trigger(T_debbie_sis_nice_boobs)

    elif M_debbie.is_state([S_debbie_shower_peek, S_debbie_shower_walk_in]) and L_home_shower.is_here(M_debbie) and not game.timer.is_dark():
        scene hallway
        show player 14 with dissolve
        player_name "( Someone's in the shower? )"

        player_name "( I wonder if it's {b}[deb_name]{/b}. )"

        show player 26
        player_name "( Maybe I can peek just a little... )"

        hide player with dissolve

    elif M_debbie.is_state(S_debbie_sleepover_offer) and game.timer.is_evening():
        call expression game.dialog_select("hallway_mom_sleepover_offer")
        $ M_debbie.trigger(T_debbie_sleepover_accept)

    elif M_debbie.is_state(S_debbie_movie_night_two) and game.timer.is_evening():
        call expression game.dialog_select("hallway_mom_movie_night_two")
        $ M_debbie.trigger(T_debbie_movie_invite)
        $ player.go_to(L_home_livingroom)
        $ game.main()


    if M_jenny.finished_state(S_jenny_cheerleader_sex) and M_debbie.get('sex available') and game.timer.is_morning() and not M_jenny.get('diary_extra_debbie', None):
        call expression game.dialog_select('hallway_jenny_acknowleges_debbie_sex')
        $ M_jenny.set('diary_extra_debbie', (M_jenny.diary_progress, game.timer.now))

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
