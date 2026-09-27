label school_frontyard_dialogue:
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if M_erik.is_state(S_erik_intro_met):
        call expression game.dialog_select("school_erik_intro_started")
        $ L_map.lock()
        $ M_mia.trigger(T_all_school_entrance)

    elif M_erik.is_state(S_erik_intro_done):
        call expression game.dialog_select("school_erik_how_you_doin")
        $ L_diane_yard.unlock()
        $ L_map.unlock(False, False)
        $ M_erik.trigger(T_erik_intro_done)
        $ game.sleep_lock = False
        jump town_map_dialogue

    elif M_dewitt.is_state(S_dewitt_school_sneak_mission_ready) and game.timer.is_dark():
        call school_dewitt_glue_mission
        $ player.go_to(L_school_frenchclassroom)
        $ M_dewitt.trigger(T_dewitt_erik_met)

    elif M_mrsj.is_state(S_mrsj_cupid_ready):
        if not M_erik.once('gf_prompt'):
            call school_mrsj_cupid_ready

    elif M_june.finished_state(S_june_date_ready) and not M_erik.get('confessed'):
        if not M_erik.once('gf_prompt'):
            call school_june_date_ready

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
