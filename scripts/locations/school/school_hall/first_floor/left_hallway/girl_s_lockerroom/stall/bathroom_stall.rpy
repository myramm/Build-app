label bathroom_stall_dialogue:
    if L_school_stall.is_here(M_judith):
        jump judith_toilet
    $ game.main()

label judith_toilet:
    if M_judith.get("in bathroom"):
        if M_judith.get("sex sequence locked"):
            call expression game.dialog_select("girls_lockerroom_judith_toilet_first_intro")
            menu:
                "You're not ugly!":
                    call expression game.dialog_select("girls_lockerroom_judith_toilet_first_not_ugly")
                    menu:
                        "Ok.":
                            call expression game.dialog_select("girls_lockerroom_judith_toilet_first_ok")
                            menu:
                                "Sure.":
                                    call expression game.dialog_select("girls_lockerroom_judith_toilet_first_sure")
                                    menu:
                                        "Yes.":
                                            $ M_judith.trigger(T_judith_comfort_her)
                                            $ M_judith.set("sex sequence locked", False)
                                            call expression game.dialog_select("girls_lockerroom_judith_toilet_first_yes")
                                            $ M_judith.set("in bathroom", False)
                                            $ M_judith.unforce()
                                        "We should stop.":

                                            call expression game.dialog_select("girls_lockerroom_judith_toilet_first_should_stop")
                                "I can't.":

                                    call expression game.dialog_select("girls_lockerroom_judith_toilet_first_cant")
                        "We should leave.":

                            call expression game.dialog_select("girls_lockerroom_judith_toilet_should_leave")
                "I know...":

                    call expression game.dialog_select("girls_lockerroom_judith_toilet_first_ugly")
            hide player
            hide old_judith
            with dissolve
            jump expression game.dialog_select("school_left_hallway_dialogue")
        else:

            call expression game.dialog_select("judith_toilet_replay")
    else:
        call expression game.dialog_select("girls_lockerroom_judith_toilet_not_here")
    jump expression game.dialog_select("school_girls_lockerroom_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
