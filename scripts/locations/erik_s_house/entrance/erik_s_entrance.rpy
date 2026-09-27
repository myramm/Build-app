label eriks_house_entrance_dialogue:
    if not game.timer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if M_anon.is_state(S_ano17_init) and game.timer.is_evening() and not M_dewitt.is_state(S_dewitt_eve_karaoke):
        call ano17_init_erikhouse_entrance
        $ M_anon.trigger(T_ano17_init)
        $ player.go_to(L_erikhouse_basement)

    elif M_mrsj.is_state(S_mrsj_start):
        call expression game.dialog_select("eriks_house_intro")
        $ M_mrsj.trigger(T_mrsj_intro_met)

    elif M_erik.is_state(S_erik_orc_acquired) and L_erikhouse_entrance.is_here(M_mrsj):
        call expression game.dialog_select("erikentrance_erik_orcette_inspection")
        $ M_erik.trigger(T_erik_orc_intercept)

    elif M_mrsj.is_state(S_mrsj_yoga_ready) and L_erikhouse_entrance.is_here(M_mrsj):
        call expression game.dialog_select("erikentrance_mrsj_yoga")
        $ player.get_item("instructions1")
        $ M_mrsj.trigger(T_mrsj_yoga_request)

    elif M_mrsj.is_state(S_mrsj_yoga_report) and L_erikhouse_entrance.is_here(M_mrsj):
        call expression game.dialog_select("erikentrance_mrsj_yoga_thanks")
        $ M_mrsj.trigger(T_mrsj_yoga_thanks)

    elif M_erik.is_state(S_erik_feed_ready) and game.timer.is_dark():
        call expression game.dialog_select("erikentrance_erik_feed_intro")
        $ M_erik.trigger(T_erik_feed_quiet)

    elif M_erik.is_state(S_erik_thief_caught) and L_erikhouse_entrance.is_here(M_mrsj):
        call expression game.dialog_select("erikentrance_erik_thief_thanks")
        $ M_erik.trigger(T_erik_thief_thanks)

    elif M_erik.is_state(S_erik_poker_ready) and L_erikhouse_erikroom.is_here(M_erik) and L_erikhouse_mrsjroom.is_here(M_mrsj):
        call expression game.dialog_select("erikentrance_erik_poker_intro")
        $ M_erik.trigger(T_erik_poker_idea)

    elif M_erik.is_state(S_erik_fork_ready) and L_erikhouse_entrance.is_here(M_mrsj):
        call expression game.dialog_select("erikentrance_erik_fork_intro")
        $ M_erik.trigger(T_erik_fork_guilt)

    elif M_mrsj.is_state(S_mrsj_cupid_couple) and L_erikhouse_entrance.is_here(M_erik, M_june):
        call expression game.dialog_select("erikentrance_mrsj_cupid_couple")
        $ M_mrsj.trigger(T_mrsj_cupid_happy)

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
