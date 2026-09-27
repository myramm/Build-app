label school_girls_lockerroom_dialogue:
    $ player.go_to(L_school_girlsroom)
    call pa_announcement
    if M_roxxy.is_state(S_roxxy_lockerroom_event):
        call expression game.dialog_select("girls_lockerroom_roxxy_lockerroom_event")
        $ M_roxxy.trigger(T_roxxy_argument)

        $ player.go_to(L_school_lefthallway)
        $ game.main()
    elif M_judith.is_state(S_judith_in_girls_bathroom):
        call expression game.dialog_select("girls_lockerroom_judith_in_girls_bathroom")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
