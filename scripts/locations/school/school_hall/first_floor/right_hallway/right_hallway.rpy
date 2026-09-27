label school_right_hallway_dialogue:
    $ player.go_to(L_school_righthallway)
    call pa_announcement
    if getPlayingSound("<loop 7 to 115>audio/ambience_school_hallway.ogg") and not game.timer.is_dark():
        $ playSound("<loop 7 to 115>audio/ambience_school_hallway.ogg", 1.0)

    if M_roxxy.is_state(S_roxxy_go_in_auditorium) and game.timer.is_day():
        call expression game.dialog_select("school_righthallway_roxxy_go_in_auditorium")
        $ M_roxxy.trigger(T_roxxy_invitation_bikini)
        $ player.go_to(L_school_hall)
        $ game.main()

    if M_eve.is_state(S_eve_ross_argument) and player.location.is_here(M_eve) and not M_dewitt.is_state(S_dewitt_attend_talent_show):
        call expression game.dialog_select("school_righthallway_eve_ross_argument")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
