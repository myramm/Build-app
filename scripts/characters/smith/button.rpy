label smith_button_dialogue:
    scene expression player.location.background_closeup
    if M_smith.is_state(S_smith_intro):
        call expression game.dialog_select("smith_button_intro")
        $ M_smith.trigger(T_smith_go_to_locker)
    elif M_smith.is_state(S_smith_go_to_locker):
        call expression game.dialog_select("smith_button_go_to_locker")
    elif M_eve.is_state(S_eve_school_dress_code):
        call expression game.dialog_select("smith_button_eve_school_dress_code")
        $ M_eve.trigger(T_eve_talked_to_smith_dress_code)
    else:
        if L_school_smithoffice.is_here(M_smith):
            call expression game.dialog_select("smith_button_get_out")
            $ player.go_to(L_school_floor3)
        elif L_school_teacherslounge.is_here(M_smith):
            call expression game.dialog_select("smith_button_teachers_lounge")
            $ player.go_to(L_school_floor2)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
