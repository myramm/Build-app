label movie_theatre_dialogue:
    $ player.go_to(L_movie_theatre)
    if L_movie_theatre.first_visit:
        call expression game.dialog_select("movie_theatre_first_visit")
        $ L_movie_theatre.visited()
        if M_jenny.is_state(S_jenny_find_stalker):
            scene black with dissolve
            pause 1
            call expression game.dialog_select("movie_theatre_jenny_find_stalker")
            $ game.timer.tick()
            $ M_jenny.trigger(T_jenny_its_mr_bubbles)
            call global_lock_check (L_mall)
            return
        else:
            call expression game.dialog_select("movie_theatre_first_visit_2")
        $ game.main()

    if M_jenny.is_state(S_jenny_find_stalker):
        call expression game.dialog_select("movie_theatre_jenny_find_stalker")
        $ M_jenny.trigger(T_jenny_its_mr_bubbles)
        $ game.timer.tick()
        call global_lock_check (L_mall)
        return
    elif M_jenny.is_state(S_jenny_movie_date):
        call expression game.dialog_select("movie_theatre_jenny_movie_date")
        $ M_jenny.trigger(T_jenny_righteous_punch)
        $ player.go_to(L_home_hallway)
        $ game.main()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
